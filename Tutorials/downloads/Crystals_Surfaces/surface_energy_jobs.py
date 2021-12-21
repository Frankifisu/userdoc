#######
# Example for calculating the surface energy of ZnO(10-10) with SCC-DFTB DFTB.org/znorg-0-1
# Part of the "Crystals and Surfaces" tutorial in the Amsterdam Modeling Suite
# USAGE: $AMSBIN/plams -f slab_1010_normal surface_energy_jobs.py
# 1) optimize lattice with Good k-space sampling
# 2) create slabs of various thicknesses from the optimized lattice parameters
# 3) run the jobs
# The "normalkspace_bulk" job recalculates the bulk cell with Normal kspace sampling, to illustrate that "surface energy method 2" (see the tutorial) is very sensitive to the k-space sampling.
# To get the surface energy, run the postprocessing script: $AMSBIN/plams surface_energy_postprocessing.py
#############

import ase
from scipy import stats
import numpy as np

#########
# Modify these variables as necessary
###########3
bulk_filename = 'ZnO_wurtzite.xyz'
surface_kspace_quality = 'Normal'
slab_thicknesses = [6,8,10,12,14]
relaxed_atoms_per_side_of_slab = -1 # set to negative number to relax everything
surface_indices = [1,0,0] # [1,0,0] = ZnO(10-10); [1,1,0] = ZnO(11-20)
num_processes = None # set to None to use all processors, or to e.g. 4 to parallelize over 4 cores


##### Lattice optimization of the bulk, kspace at least good.
bs = Settings() #bulk settings
bs.input.ams.task = 'geometryoptimization'
bs.input.ams.geometryoptimization.optimizelattice = 'Yes'
bs.input.dftb.model = 'SCC-DFTB'
bs.input.dftb.resourcesdir = 'DFTB.org/znorg-0-1'
bs.input.dftb.kspace.quality = 'good'

bulk_mol = Molecule(bulk_filename)
bulk_job = AMSJob(settings=bs, molecule=bulk_mol, name='lattice_optimization')
bulk_job.run()

optimized_bulk_mol = bulk_job.results.get_main_molecule()

##### Get the bulk energy with "normal" kspace sampling
bs_normal = bs.copy()
bs_normal.input.ams.geometryoptimization.optimizelattice = 'No'
bs_normal.input.dftb.kspace.quality = 'Normal'

bulk_normal_job = AMSJob(settings=bs_normal, molecule=optimized_bulk_mol, name='normalkspace_bulk')
bulk_normal_job.run()


###### Set up and run slab calculations
slab_jobs = []
ss = bs.copy() # slab settings
ss.input.ams.geometryoptimization.optimizelattice = 'No'
ss.input.dftb.kspace.quality = surface_kspace_quality
ss.runscript.nproc = num_processes

optimized_bulk_atoms = toASE(optimized_bulk_mol) 

def get_slab(bulk_atoms, indices=None, nlayers=4, vacuum=12, tol=1e-6):
    from ase.build import surface, sort
    if indices is None:
        indices = [1,0,0]
    slab = surface(bulk_atoms, indices, nlayers, vacuum, tol)
    slab = sort(slab, tags=slab.get_positions()[:,2])
    slab.set_pbc((True, True, False))
    return slab

for nlayers in slab_thicknesses:
    slab = get_slab(optimized_bulk_atoms, surface_indices, nlayers)
    slab_mol = fromASE(slab)

    if relaxed_atoms_per_side_of_slab > 0:
        fixed_atoms = list(range(relaxed_atoms_per_side_of_slab+1, len(slab_mol)-relaxed_atoms_per_side_of_slab+1))
        ss.input.ams.Constraints.Atom = fixed_atoms
    else:
        ss.input.ams.Constraints = None

    slab_job = AMSJob(settings=ss.copy(), molecule=slab_mol, name='{}layers_{}kspace_{}relaxed_{}surface'.format(nlayers, ss.input.dftb.kspace.quality, relaxed_atoms_per_side_of_slab, "".join([str(i) for i in surface_indices])))

    slab_job.nlayers = nlayers
    slab_job.surfacearea = np.linalg.det(slab.get_cell()[:2, :2]) # square angstroms

    slab_jobs.append(slab_job)

for job in slab_jobs:
    job.run()

