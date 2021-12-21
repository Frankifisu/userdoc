# Calculate lattice parameters of ZnO using DFTB for different k-space samplings
# This file is part of the "Crystals and Surfaces" tutorial of the Amsterdam Modeling Suite
# USAGE: $AMSBIN/plams dftb_lattopt_example.py

mol = Molecule('ZnO_wurtzite.xyz')

s = Settings()
s.input.ams.Task = 'GeometryOptimization'
s.input.ams.GeometryOptimization.OptimizeLattice = 'Yes'
s.input.dftb.model = 'SCC-DFTB'
s.input.dftb.resourcesdir = 'DFTB.org/znorg-0-1'

jobs = []

for kspace in ['Basic', 'Normal', 'Good', 'VeryGood']:
    s.input.dftb.kspace.quality = kspace
    jobs.append(AMSJob(settings=s, molecule=mol, name=kspace))

for job in jobs:
    job.run()

print("ZnO wurtzite optimized with SCC-DFTB znorg-0-1")
print("lengths in angstrom, angles in degrees")
print("kspace a b c alpha beta gamma")
for job in jobs:
    try:
        opt_mol = job.results.get_main_molecule()
        cellpars = list(toASE(opt_mol).get_cell_lengths_and_angles())
        print("{} {:.3f} {:.3f} {:.3f} {:.3f} {:.3f} {:.3f}".format(job.name, cellpars[0], cellpars[1], cellpars[2], cellpars[3], cellpars[4], cellpars[5]))
    except:
        pass

        
