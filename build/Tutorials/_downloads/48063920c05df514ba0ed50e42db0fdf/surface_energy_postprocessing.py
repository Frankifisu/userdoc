# postprocessing script for calculating surface energies
# part of the "Crystals and Surfaces" tutorial in the Amsterdam Modeling Suite
# first run the surface_energy_jobs.py script
# set the variable jobdir to the directory with calculation results
# USAGE: $AMSBIN/plams surface_energy_postprocessing.py

from scipy import stats
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

config.erase_workdir = True

###################
# set jobdir to the plams working directory where the jobs were run
###################
jobdir = 'slab_1010_normal'

jobs = load_all(jobdir)

bulk_e_good = bulk_e_normal = 0
data = []
for path,job in jobs.items():
    if job.name == 'lattice_optimization':
        bulk_e_good = job.results.get_energy()
        n_bulk_atoms = len(job.results.get_main_molecule())
    elif job.name == 'normalkspace_bulk':
        bulk_e_normal = job.results.get_energy()
    else:
        mol = job.results.get_main_molecule()
        n_slab_atoms = len(mol)
        energy = job.results.get_energy()
        surfacearea = np.linalg.det(toASE(mol).get_cell()[:2,:2]) # square angstrom
        data.append([n_slab_atoms, energy, surfacearea])

n_atoms_index = 0
e_index = 1
area_index = 2

data = np.array(data)
data = data[data[:,n_atoms_index].argsort()] # sort w.r.t first column, i.e. n_atoms

print("#atoms, energy, surfacearea")
print(data)

use_last_n_datapoints = 3
x_data = data[-use_last_n_datapoints:,n_atoms_index] # n_atomss
y_data = data[-use_last_n_datapoints:,e_index] # energies
slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
# the intercept = 2*A*ESurf, the area is the same for all jobs
Esurf = intercept / (2*surfacearea)
conversion = Units.convert(1.0, 'Hartree', 'J') / Units.convert(1.0, 'angstrom', 'm')**2


# create a plot

max_n_atoms = np.max(data[:,n_atoms_index])
linear_fit_data = np.array([[0, intercept], [max_n_atoms, slope*max_n_atoms+intercept]])
plt.plot(data[:,n_atoms_index], data[:,e_index], 'ro', linear_fit_data[:,0], linear_fit_data[:,1], 'b-')
plt.style.use('seaborn')
plt.ylabel("Energy (Ha)")
plt.xlabel(r'# atoms in ZnO(10$\bar{1}$0) slab')
min_x = 0
max_x = int(max_n_atoms*1.1)
min_y = int(data[-1,e_index]*1.1)
max_y = 1
plt.axis([min_x, max_x, min_y,max_y])
plt.annotate('intercept = {:.6f} Ha'.format(intercept), xy=(0., 0.), xytext=(0.1*(max_x-min_x)+min_x, 0.95*(max_y-min_y)+min_y), arrowprops={'arrowstyle': '-|>'})
plt.title(r'Slab energies for ZnO(10$\bar{1}$0) (k-space quality normal)')
plt.savefig("{}.png".format(jobdir))


print("Surface energy from slope (method 1): {}".format(Esurf*conversion)) 
print("Effective bulk energy: {}".format(slope))
print("Good bulk energy: {}".format(bulk_e_good/n_bulk_atoms))
print("Normal bulk energy: {}".format(bulk_e_normal/n_bulk_atoms))

naive_Esurf = ( data[-1,e_index] - (data[-1,n_atoms_index]/n_bulk_atoms)*bulk_e_good ) / (2*surfacearea) 
naive_Esurf *= conversion
print("Naive surface energy w.r.t. good bulk (method 2): {}".format(naive_Esurf)) 
naive_Esurf = ( data[-1,e_index] - (data[-1,n_atoms_index]/n_bulk_atoms)*bulk_e_normal ) / (2*surfacearea) 
naive_Esurf *= conversion
print("Naive surface energy w.r.t. normal bulk (method 2): {}".format(naive_Esurf)) 

