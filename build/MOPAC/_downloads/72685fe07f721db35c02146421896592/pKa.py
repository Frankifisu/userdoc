from scm.plams.interfaces.molecule.rdkit import from_smiles
import numpy as np
import multiprocessing

# In this example we compute pKa (acid dissociation constant) using MOPAC for a set of
# molecules. The molecules are defined using smiles strings, and are converted to xyz 
# structures using the plams-rdkit interface.

# Important note: the predicted pKa strongly depend on the molecule's conformer.
# Here we use the lowest conformer predicted by rdkit's UFF.
# The difference between the values computed here and the results on the 
# MOPAC website (ref_mopac_pKa) is due to different conformers 

# Data taken from the online MOPAC manual: http://openmopac.net/manual/ (only a sub set)
data_tmp = [
   # Molecule name                 smiles                            exp_pKa   ref_mopac_pKa (from mopac's website)
   ['1-Naphthoic_acid',           'C1=CC=C2C(=C1)C=CC=C2C(=O)O',      3.69,     4.35],
   ['2,2,2-Trichloroethanol',     'C(C(Cl)(Cl)Cl)O',                 12.02,    12.22],
   ['2,2,2-Trifluoroethanol',     'C(C(F)(F)F)O',                    12.40,    12.27], 
   ['2,2-Dimethylpropionic_acid', 'CC(C)(C)C(=O)O',                   5.03,     5.23],
   ['2,3,4,6-Tetrachlorophenol',  'C1=C(C(=C(C(=C1Cl)Cl)Cl)O)Cl',     7.10,     6.08],
   ['Acetic_acid',                'CC(=O)O',                          4.76,     5.00],
   ['Acrylic_acid',               'C=CC(=O)O',                        4.25,     4.65],
   ['Benzoid_acid',               'C1=CC=C(C=C1)C(=O)O',              4.20,     4.30],
   ['Citric_acid',                'C(C(=O)O)C(CC(=O)O)(C(=O)O)O',     3.13,     2.56],
   ['Ethanol',                    'CCO',                             16.00,    16.37],
   ['Formic_acid',                'C(=O)O',                           3.77,     3.77],
   ['Glycine',                    'C(C(=O)O)N',                       2.35,     2.53],
   ['Isoleucine',                 'CCC(C)C(C(=O)O)N',                 2.32,     2.48],
   ['Methanol',                   'CO',                              15.54,    15.23],
   ['o-Nitrophenol',              'C1=CC=C(C(=C1)[N+](=O)[O-])O',     7.17,     7.52],
   ['Pentachlorophenol',          'C1(=C(C(=C(C(=C1Cl)Cl)Cl)Cl)Cl)O', 4.90,     5.55],
   ['Phenol',                     'C1=CC=C(C=C1)O',                  10.00,     9.71],
   ['Pyruvic_acid',               'CC(=O)C(=O)O',                     2.50,     2.85],
   ['T-Butanol',                  'CC(C)(C)O',                       17.00,    16.25],
   ['Terephthalic_acid',          'C1=CC(=CC=C1C(=O)O)C(=O)O',        3.51,     3.59],
   ['Valine',                     'CC(C)C(C(=O)O)N',                  2.29,     2.61],
   ['Water',                      'O',                               15.74,    15.75]]

# Turn data_tmp into a dictionary: 
systems = [{'name':d[0], 'smiles':d[1], 'exp_pKa':d[2], 'ref_mopac_pKa':d[3]} for d in data_tmp] 

# Create the molecules from the smiles using rdkit:
molecules = []
for system in systems:
   # Compute 30 conformers, optimize with UFF and pick the lowest in energy.
   mol = from_smiles(system['smiles'], nconfs=30, forcefield='uff')[0]

   mol.properties.name = system['name']
   mol.properties.exp_pKa = system['exp_pKa']
   mol.properties.ref_mopac_pKa = system['ref_mopac_pKa']
   
   molecules.append(mol)

# MOPAC input:
s = Settings()
s.runscript.nproc = 1 # serial calculation
s.input.ams.Task = 'GeometryOptimization'
s.input.ams.GeometryOptimization.Convergence.Step = 1.0e-3
s.input.ams.GeometryOptimization.Convergence.Gradients = 1.0e-5
s.input.mopac.model = 'PM6'
s.input.mopac.properties.pKa = 'Yes'

# Set up and run jobs:
jobs = MultiJob(children=[AMSJob(name=mol.properties.name, molecule=mol, settings=s) for mol in molecules])
jr = JobRunner(parallel=True, maxjobs=multiprocessing.cpu_count()) # run jobs in parallel
jobs.run(jobrunner=jr)

# Collect results:
for i, mol in enumerate(molecules):
   pKaValues = jobs.children[i].results.readrkf('Properties', 'pKaValues', file='mopac')
   mol.properties.calc_pKa = np.mean(pKaValues) # If there is more than one pKa, take the average value
 
# Print results in a table:
print("Results:\n")
print("| {:28} | {:8} | {:8} | {:8} | {:8} |".format("Molecule", "exp pKa", "calc pKa", "ref", 'calc-exp'))
for mol in molecules:
   print("| {:28} | {:>8.2f} | {:>8.4f} | {:>8.2f} | {:>8.2f} |".format(mol.properties.name, mol.properties.exp_pKa, mol.properties.calc_pKa, mol.properties.ref_mopac_pKa, mol.properties.calc_pKa-mol.properties.exp_pKa))
print("")

errors = [mol.properties.calc_pKa - mol.properties.exp_pKa for mol in molecules]

print("Mean signed error  : {:4.2f}".format(np.mean(errors)))
print("Mean unsigned error: {:4.2f}".format(np.mean([abs(e) for e in errors])))
print("Root mean square error: {:4.2f}".format(np.sqrt(np.mean([e**2 for e in errors]))))
print("Done")
