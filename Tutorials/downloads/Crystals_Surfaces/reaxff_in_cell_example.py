######################
# Calculate the "in-cell" effect for ReaxFF
# This file is part of the "Crystals and Surfaces" tutorial of the Amsterdam Modeling Suite
# Calculate the energies of an isolated water molecule, a ZnO slab, and a system in which the water molecule and ZnO slab are widely separated
# Eslab + Emol does not equal Ewidelyseparated, because of charge transfer between the water molecule and ZnO slab when they are widely separated.
# The energy difference is calculated for larger and larger surface supercell (at a constant thickness)
# For thicker slabs or bigger adsorbates, the effect would increase even more.
# Usage: $AMSBIN/plams -f incell reaxff_in_cell_example.py
###########################

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

####### 
# Settings
######
config.erase_workdir = True # set to True to not keep any files
slab_1x1_mol = Molecule('5dl_ZnO_10-10_ReaxFF.xyz')
supercells = [2,3,4,6,9]

Eslab = {}
Emol = {}
Ewidelyseparated = {}

s = Settings()
s.input.ams.Task = 'SinglePoint'
s.input.ReaxFF.ForceField = 'ZnOH.ff'
s.runscript.nproc = 1

def add_water(mol, x=0, y=0, z=0):
    ret = mol.copy()
    ret.add_atom(Atom(symbol="O", coords=(x+0., y+0., z+0.59372000)))
    ret.add_atom(Atom(symbol="H", coords=(x+0., y+0.76544, z-0.00836)))
    ret.add_atom(Atom(symbol="H", coords=(x+0., y-0.76544, z-0.00836)))
    return ret


for i in supercells:
    z = 30 #z coordinate of water molecule
    slab_mol = slab_1x1_mol.supercell(i,i)
    slab_job = AMSJob(settings=s, molecule=slab_mol, name='slab_{}'.format(i))
    water_mol = add_water(Molecule(), z=z)
    #water_mol.lattice = slab_mol.lattice.copy()
    water_job = AMSJob(settings=s, molecule=water_mol, name='water_{}'.format(i))
    widelyseparated_mol = add_water(slab_mol, z=z)
    widelyseparated_job = AMSJob(settings=s, molecule=widelyseparated_mol, name='widelyseparated_{}'.format(i))

    slab_job.run()
    water_job.run()
    widelyseparated_job.run()

    n = len(slab_mol)
    Eslab[n] = slab_job.results.get_energy(unit='kcal/mol')
    Emol[n] = water_job.results.get_energy(unit='kcal/mol')
    Ewidelyseparated[n] = widelyseparated_job.results.get_energy(unit='kcal/mol')

print("n_atoms_in_slab, Eslab, Emol, Eslab+Emol, Ewidelyseparated, Eslab+Emol-Ewidelyseparated [kcal/mol]")
x = []
y = []
for k in Eslab:
    diff_standard_vs_incell = Eslab[k]+Emol[k]-Ewidelyseparated[k]
    print("{} {} {} {} {} {}".format(k, Eslab[k], Emol[k], Eslab[k]+Emol[k], Ewidelyseparated[k], diff_standard_vs_incell))
    x.append(k)
    y.append(diff_standard_vs_incell)

# create plot
plt.plot(x, y, '-', x, y, 'o')
plt.xlabel('# atoms in slab')
plt.ylabel('Eslab+Emol-Ewidelyseparated (kcal/mol)')
plt.title(r'ReaxFF standard vs. in-cell for H$_2$O on ZnO(10$\bar{1}$0)')
plt.savefig("standard_vs_incell.png")




