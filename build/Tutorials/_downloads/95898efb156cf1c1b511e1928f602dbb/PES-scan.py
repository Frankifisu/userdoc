# PLAMS version of the AMS tutorial:
# Transition state search, optimization and characterization of a Ziegler Natta Catalyst
# www.scm.com/doc...
# Part 1: PES Scan 

# Generate a molecule object from xyz coordinates
molecule = Molecule('ethene-metallocenium.xyz')
molecule.properties.charge = 1
settings = Settings()

# Engine settings: GFN-1xTB with implicit Tolene solvation
settings.input.dftb.Model = 'GFN1-xTB'
settings.input.dftb.Solvation.Solvent = 'Toluene'

# AMS settings for PES scan 
settings.input.ams.Task = 'PESScan'

# Loosened convergence criteria
settings.input.ams.GeometryOptimization.Convergence.Energy = '5.0e-5 [Hartree]'
settings.input.ams.GeometryOptimization.Convergence.Gradients = '5.0e-3'
settings.input.ams.GeometryOptimization.Convergence.Step = '5.0e-3 [Angstrom]'

# PES scan (see online tutorial for choice of scan coordinates)
settings.input.ams.PESScan.ScanCoordinate.nPoints = '20'
settings.input.ams.PESScan.ScanCoordinate.Distance = ['1 28 3.205 2.3', '29 25 3.295 1.5'] 

# setting up the AMS job with the molecule and settings object
job = AMSJob(molecule=molecule, settings=settings, name='pes_scan')

# run the calulation
result = job.run()

# list of final energies from the 1D PES scan
energies = result.readrkf('PESScan','PES')
# find index of entry with highest energy
highest_energy = max(energies)
highest_energy_index = energies.index(highest_energy)

# lookup which geometry in the history section corresponds to which PESscan point
history_indices = result.readrkf('PESScan','HistoryIndices')
history_index = history_indices[highest_energy_index]

# read the corresponding geometry from the history section
highest_energy_geo = result.get_history_molecule(history_index)

# print results to command line
print('== Results ==')
print('Transition state geometry (guess):')
print(highest_energy_geo)
print('Energy         : {:.3f} kcal/mol'.format(Units.convert(highest_energy, 'au', 'kcal/mol')))
print('PES point nr.  : {:d}'.format(highest_energy_index+1))

# write TS guess geometry to file
highest_energy_geo.write('TS-guess.xyz')
