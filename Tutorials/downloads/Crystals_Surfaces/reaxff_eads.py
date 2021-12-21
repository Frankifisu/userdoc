# Calculate the adsorption energy of water on ZnO using ReaxFF with the "standard" and "in-cell" approaches
# This file is part of the "Crystals and Surfaces" tutorial of the Amsterdam Modeling Suite.
# USAGE: $AMSBIN/plams reaxff_eads.py

systems = read_molecules('systems/')

s = Settings()
s.input.ams.Task = 'GeometryOptimization'
s.input.ReaxFF.ForceField = 'ZnOH.ff'
s.runscript.nproc = 1

jobs = []
for name,system in systems.items():
    job = AMSJob(settings=s, name=name, molecule=system)
    job.run()
    jobs.append(job)

print("Energies in kcal/mol")
E = {}
for job in jobs:
    E[job.name] = job.results.get_energy(unit='kcal/mol')
    print("{} {}".format(job.name, E[job.name]))

print("Eslab+Emol {}".format(E['slab']+E['mol']))
print("Eads_standard {}".format(E['slab']+E['mol']-E['slab_and_mol']))
print("Eads_incell {}".format(E['slab_and_mol_widely_separated']-E['slab_and_mol']))


