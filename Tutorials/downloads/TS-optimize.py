# PLAMS version of the AMS tutorial:
# Transition state search, optimization and characterization of a Ziegler Natta Catalyst
# www.scm.com/doc...
# Part 2: TS search

# Read in the xyz file TS-guess.xyz generated in Part 1
molecule = Molecule('TS-guess.xyz')
molecule.properties.charge = 1
settings = Settings()

# Engine settings: GFN-1xTB with implicit Tolene solvation
settings.input.dftb.Model = 'GFN1-xTB'
settings.input.dftb.Solvation.Solvent = 'Toluene'

# AMS settings for TS search 
settings.input.ams.Task = 'TransitionStateSearch'
settings.input.ams.Properties.NormalModes = 'Yes'
settings.input.ams.GeometryOptimization.InitialHessian.Type = 'Calculate'

# setting up the AMS job with the molecule and settings object
job = AMSJob(molecule=molecule, settings=settings, name='ts_search')

# run the calulation
result = job.run()

# results
energy = result.get_energy(unit='kcal/mol')
frequencies = result.get_frequencies(unit='cm^-1')
optimized_molecule = result.get_main_molecule()
# read the classification of the PES point from file dftb.rkf
character = result.readrkf('AMSResults', 'PESPointCharacter', file='engine')

# print results
print('== Results ==')
print('Optimized geometry:')
print(optimized_molecule)
print('Character   : {}'.format(character))
print('Energy      : {:.3f} kcal/mol'.format(energy))
print('Frequencies : {} cm^-1'.format(frequencies))