from scm.plams import *
import multiprocessing, os
import numpy as np



def get_md_job(mol, temperature, name):

    ####### SETTINGS ######
    s = Settings()
    s.input.ams.Task = 'MolecularDynamics'
    s.input.ams.MolecularDynamics.NSteps = 200_000
    s.input.ams.MolecularDynamics.TimeStep = 1 #in fs
    s.input.ams.MolecularDynamics.Trajectory.SamplingFreq = 2 #in steps
    s.input.ams.MolecularDynamics.Trajectory.WriteVelocities = 'No'
    s.input.ams.MolecularDynamics.Trajectory.WriteCharges = 'No'
    s.input.ams.MolecularDynamics.Trajectory.WriteBonds = 'No'
    s.input.ams.MolecularDynamics.Trajectory.WriteMolecules = 'No'
    s.input.ams.MolecularDynamics.InitialVelocities.Temperature = temperature
    s.input.ams.MolecularDynamics.Thermostat.Type = 'NHC'
    s.input.ams.MolecularDynamics.Thermostat.Temperature = temperature
    s.input.ams.MolecularDynamics.Thermostat.Tau = 100
    s.input.ams.MolecularDynamics.CalcPressure = 'Yes'
    for i, l in enumerate(mol.lattice):
        s.input.ams.System.Lattice[f'_{i+1}'] = f'{l[0]} {l[1]} {l[2]}'
    s.input.ForceField.Type = 'GAFF'
    s.input.ForceField.AntechamberIntegration = 'Yes'
    return AMSJob(name=name, molecule=mol, settings=s)


def get_analysis_job(KFFilename, name):
    s = Settings()
    s.input.Task = 'AutoCorrelation'
    s.input.AutoCorrelation.Property = 'PressureTensor'
    s.input.AutoCorrelation.VecElements.Index = [4, 5, 6]
    s.input.AutoCorrelation.MaxStep = 3000
    s.input.TrajectoryInfo.Trajectory.KFFilename = KFFilename
    s.input.TrajectoryInfo.Trajectory.Range = '4000 100001'
    return AMSAnalysisJob(name=name, settings=s)


def get_viscosities(molfile, temperatures, name):
    ''' 
    Main function used to calculate the viscosity at certain temperatures
    First does MD simulations and then analysis to obtain the viscosity
    '''

    def get_MD_temperature(KFFilename, steps_fraction=0.4):
        #steps_fraction sets what part of the set to use. If set to 0.2 it will use the last 20% of the run
        reader = KFReader(KFFilename)
        MDtemperatures = np.fromiter( KFHistory(reader, 'MDHistory').iter('Temperature'), float )
        average = np.mean(MDtemperatures[int(-integrals.size*steps_fraction):])
        sd = np.std(MDtemperatures[int(-integrals.size*steps_fraction):])
        return average, sd

    def get_ACF_integral(KFFilename, steps_fraction=0.4):
        reader = KFReader(KFFilename)
        integrals = np.asarray(reader.read('Integral(1)', 'y-axis'))
        average = np.mean(integrals[int(-integrals.size*steps_fraction):])
        sd = np.std(integrals[int(-integrals.size*steps_fraction):])

        #convert them to Pa^2 s
        average = average * Units.conversion_ratio('au', 'Pa')**2 * 1e-15
        sd = sd  * Units.conversion_ratio('au', 'Pa')**2 * 1e-15
        return average, sd


    init(folder=f'{name}')

    #here we make sure PLAMS does parallelization
    config.default_jobrunner = JobRunner(parallel=True, maxjobs=multiprocessing.cpu_count())
    config.job.runscript.nproc = 1

    ######### MAIN SETTINGS #########
    analysisname = name + '_analysis'

    ######### JOBS RUNNING #########
    mol = Molecule(molfile)
    volume = mol.unit_cell_volume()

    print(f'Beginning viscosity calculations {name}')
    print(f'I will perform {len(temperatures)} MD runs with volume: {volume:.2f} angstrom^3')

    ##### MD RUNS
    print('Starting MD runs ...')
    #start the jobs
    MDresults = [get_md_job(mol, T, name + f'_T{T}').run() for T in temperatures]

    #wait for the jobs to finish and get the rkf files
    MDrkf = [r['ams.rkf'] for r in MDresults if r.ok()]
    MDtemperatures = [get_MD_temperature(rkf) for rkf in MDrkf]

    # print('MD run results:')
    # print('\tTarget T (K) | Observed T +- SD (K)')
    # for T, Tobs in zip(temperatures, MDtemperatures):
    #     print(f'\t{T: >12} | {Tobs[0]:.2f} +- {Tobs[1]:.2f}')

    ##### ANALYSIS RUNS
    print('Starting analysis runs ...')
    analysisresults = [get_analysis_job(rkf, analysisname + f'_T{T}').run() for rkf, T in zip(MDrkf, temperatures)]
    #wait for runs to finish. AMSAnalysisResults does not have method ok
    while not all(r.job.check() for r in analysisresults):
        pass
    #once done grab the rkf files
    analysisrkf = [r[f'{r.job.name}.kf'] for r in analysisresults]

    #read the ACF integral and calculate the viscosities
    kB = Units.constants['k_B']
    ACF = [get_ACF_integral(rkf) for rkf in analysisrkf] # in Pa^2 s from au^2 fs
    viscosities = [volume*1e-30/(kB*Tobs[0]) * integral[0] for Tobs, integral in zip(MDtemperatures, ACF)]

    finish()

    results = {
        'temperatures': [t[0] for t in MDtemperatures], #in K
        'temperature_stdevs': [t[1] for t in MDtemperatures], #in K
        'viscosities': viscosities, #in Pa s
    }

    return results


if __name__ == '__main__':
    molfile = 'benzene_bulk_16.xyz' #system to do the MD on
    temperatures = [100, 150, 200, 250, 298, 350, 400, 450] 

    r = get_viscosities(molfile, temperatures, 'Benzene')

    print('All simulations are now done')
    print('Temperature +- SD (K) | Viscosity (mPa s)')
    for t, tsd, v in zip(r['temperatures'], r['temperature_stdevs'], r['viscosities']):
        print(f'{t: >11.2f} +- {tsd: <6.2f} | {v*1000:.5f}')
