#!/usr/bin/env amspython
# coding: utf-8

# ### Run a reference job

# ResultsImporters work on finished reference job. Here, we run a geometry optimization on a water molecule with the UFF force field. The calculation is run from python with [PLAMS](../../../Tutorials/WorkflowsAndAutomation/PythonScriptingWithPLAMS.html), but you can also run it with the [graphical user interface](../../../Tutorials/GettingStarted/GeometryOptimizationOfEthanol.html) and skip to [Water molecule reference data](#water-molecule-reference-data).

from scm.params import *
from scm.plams import *
init(path='/tmp', folder='demo_results_importer') # set path=None to use the current working directory, for example if you do not have /tmp on your system

# set up a water molecule, can also be set up as mol = Molecule('water.yz') or mol = from_smiles('O')
mol = Molecule()
mol.add_atom(Atom(symbol='O', coords=(0,0,0)))
mol.add_atom(Atom(symbol='H', coords=(1,0,0)))
mol.add_atom(Atom(symbol='H', coords=(-0.7,0.7,0)))

ref_settings = Settings()
ref_settings.runscript.nproc = 1   # run jobs in serial
ref_settings.input.ams.task = 'GeometryOptimization'
ref_settings.input.forcefield.type = 'UFF'        # run UFF reference calculation
#ref_settings.input.adf.xc.gga = 'PBE'            # run DFT reference calculation with ADF
#ref_settings.input.band.xc.gga = 'PBE'           # run DFT reference calculation with BAND
#ref_settings.input.dftb.model = 'GFN1-xTB'       # run DFTB reference calculation
#ref_settings.input.reaxff.forcefield = 'CHO.ff'  # run ReaxFF reference calculation

water_ams_results_file = AMSJob(settings=ref_settings, 
                                molecule=mol, 
                                name='water_ref_geo_opt').run().rkfpath()

print("AMS results file located in " + water_ams_results_file)


# This creates directory containing the **ams.rkf** result file. You can open it in AMSmovie to visualize the trajectory.

# ### Water molecule reference data

# The goal of a ParAMS parametrization is to **as closely as possible reproduce results from reference calculations**. Four types of results will be demonstrated for the water molecule reference calculation:
# 
# - The calculated **charges** and **forces** at the final geometry. The corresponding job during the parametrization is a **SinglePoint** on the optimized geometry from the reference calculation
# 
# - The optimized O-H **bond length** and H-O-H **angle** with the parametrized engine. The corresponding job during the parametrization is a **GeometryOptimization** starting from the optimized geometry from the reference calculation
# 
# - **Relative energies** between multiple snapshots from the geometry optimization trajectory, and **forces** from those same snapshots
# 
# - A **reaction energy**, in this case the **propene combustion energy** for the reaction C$_3$H$_6$(g) + (9/2) O$_2$(g) → 3 CO$_2$(g) + 3 H$_2$O(g)

# ### Initialize the ResultsImporter
You can **set the preferred units** that you like to work in when initializing the ResultsImporter. Here, we set the energy unit to **kcal/mol**, and the force unit to **kcal/mol/angstrom**. If no units are set, some :ref:`default units <AvailableExtractors>` will be used. 

You can also specify the default **maximum number of iterations** for geometry optimization jobs. During the parametrization, it is often convenient to limit the maximum number of steps for individual geometry optimization jobs, so that the job is guaranteed to finish in a reasonable amount of time, even for unreasonable parameter combinations.
results_importer_settings = Settings()
results_importer_settings.units.energy = 'kcal/mol' 
results_importer_settings.units.forces = 'kcal/mol/angstrom'
results_importer_settings.default_go_settings.MaxIterations = 20   # set to False to have unlimited iterations
ri = ResultsImporter(settings=results_importer_settings)


print(type(ri.job_collection))
print(type(ri.engine_collection))
print(type(ri.data_set))


# ### Add a singlepoint calculation on the optimized geometry

# The jobs in the job collection are run repeatedly during the ParAMS optimization. They can have any task, for example ``SinglePoint`` or ``GeometryOptimization``.
# 
# ResultsImporters add jobs to the job collection. The **molecular structure is taken from the reference job**, but the Task is not. **The Task for jobs added via a results importer defaults to** ``SinglePoint``, even if the reference job was a ``GeometryOptimization``!
# 
# 

ri.add_singlejob(water_ams_results_file,   # path to ams.rkf or to the jobname.results folder
                 properties=['charges', 'forces'],
                 name='water_singlepoint') # custom name for this job


# The ``add_singlejob`` results importer has affected the JobCollection, DataSet, and EngineCollection inside ``ri`` variable. It returns the expressions added to the DataSet (see more below).
# 
# The job 'water_singlepoint' has been added to the job collection:

print(ri.job_collection)


# Above, the **AMSInput** block contains input to the *AMS Driver*, defining a job that will be repeatedly run during the parametrization. The **Atoms** block contains the optimized water molecule from the reference UFF calculation, and the **task** is set to **SinglePoint**. Because we requested the forces, **properties gradients yes** is set. This guarantees that we will be able to extract the forces during the parametrization.
# 
# The **Origin**, **OriginalEnergyHartree**, **Hash_1** and **Hash_2** are only used internally by the ResultsImporter. For example, the hashes help to prevent adding the same job twice to the job collection.
# 
# The **ReferenceEngineID** contains a reference to an engine in the **EngineCollection**. This entry in the engine collection contains the settings for the reference job that was run in the beginning. It is not strictly needed for the parametrization.

print(ri.engine_collection)


# **The data_set (training set)** contains two entries

print(ri.data_set)


# The two data_set entries have *ReferenceValues* taken from the reference job. The *Unit* for the forces is kcal/mol/angstrom, which was specified as the preferred unit when initializing the ResultsImporter. The *Sigma* values correspond to the default sigma values for the ``charges`` and ``forces`` extractors. The *Weight* default value is 1.0

# The results importer has added three pieces of metadata: **Group, SubGroup, and INFO_ReferenceEngineIDs**. The **Group** specifies the type of quantity, and the **SubGroup** from which job the reference data comes. The **Group** and **SubGroup** can be used to help with postprocessing results. The **INFO_ReferenceEngineIDs** contains all the reference engines that were used in the calculation of the reference value.
# 
# You can change the *Weight* or *Sigma* just like in a standalone DataSet:

ri.data_set[0].sigma = 0.2
ri.data_set[0].weight = 3.14
print(ri.data_set[0])


# Alternatively, you can also specify the weight and sigma values when calling the ``add_singlejob`` results importer (see next section).

# ### Add a geometry optimization job extracting the bond length and bond angle
# 
# To fit structural results like bond lengths or bond angles, it is necessary to run ``GeometryOptimization`` jobs during the parametrization. Use the ``task`` keyword in ``add_singlejob()``. 
# 
# The ``properties`` can either be given in a list as before, or a ``dict`` with more details (set *weight*, *sigma*, and *unit*). 
# 
# The ``distance`` and ``angle`` extractors accept the atom ids of the atoms. The atom ids start with 0, so atom 0 is the first atom (the O atom), atom 1 is the second atom (one of the H atoms), and atom 2 is the the third atom (the other H atom).

ri.add_singlejob(water_ams_results_file,         # path to ams.rkf
                 properties={
                     'distance(0,1)': {  # extract O-H bond length
                         'weight': 2.0,
                         'sigma': 0.1,
                      },
                      'angle(1,0,2)': {}, #  H-O-H angle, use default weight and sigma
                 },
                 task='GeometryOptimization',    # set task to GeometryOptimization
                 name='water_geo_opt')           # set a custom name     


print(ri.job_collection['water_geo_opt'])


# Above, the **task** is set to **GeometryOptimization** as requested. There's also a **geometryoptimization** block setting the maximum number of iterations to 20, as was specified in the [ResultsImporter initialization](#initialize-the-resultsimporter). 

print(ri.data_set[-2:])   # the two last added entries


# The UFF-optimized water molecule has an O-H bond length of 0.99 angstrom, and an H-O-H angle of 104.46 degrees.

# ### Add a trajectory
# 
# If you have a trajectory file, for example from a geometry optimization or molecular dynamics simulation, you can extract reference results from N equally spaced frames in the trajectory with the ``add_trajectory_singlepoints()`` results importer. The following properties are supported:
# 
# * energy
# * relative_energies
# * forces
# * stresstensor
# 
# The properties can only be extracted if they are stored on the trajectory file. For example, forces are not stored by default in AMS MD simulations, but must be enabled before running the simulation.
# 
# Below the relative_energies and forces from the UFF geometry optimization on the water molecule are extracted. The ``relative_to: min_global`` ensures that the global minimum is included, and that energies are relative to that one. Setting N = 4 will give 3 relative energies and 4 forces added to the data_set.

new_expr = ri.add_trajectory_singlepoints(water_ams_results_file,
                             properties={
                                'relative_energies': {
                                    'relative_to': 'min_global',
                                },
                                'forces': {},
                             },
                             N=4) # get 4 frames

# print only expression and reference value, the full data_set entry can also be printed: print(ri.data_set[expression])
for expression in new_expr:
    print(expression)
    print(ri.data_set[expression].reference,'\n')


# The job collection contains single point calculations with molecules taken from the respective frames in the reference trajectory. Above we didn't specify a ``name`` when calling ``add_trajectory_singlepoints``, so the name is guessed from the reference job.
# 
# For example, ``water_ref_geo_opt_frame001`` corresponds to the input molecule defined at the beginning of this demonstration:

print(ri.job_collection['water_ref_geo_opt_frame001'])


# The ``add_trajectory_singlepoints`` results importer adds another metadata to the job_collection: ``Frame``, corresponding to the frame in the ``Origin`` file from which the input molecule was taken.

# ### Add a reaction energy

# Here we demonstrate **propene combustion**:  C$_3$H$_6$(g) + (9/2) O$_2$(g) → 3 CO$_2$(g) + 3 H$_2$O(g). We will first need to calculate three more reference jobs for C$_3$H$_6$ (propene), O$_2$ and CO$_2$. **Note that this reaction energy is described very poorly with UFF** (ΔH⁰ = -1.4 kcal/mol, experimental value: -491.8 kcal/mol). To get a more realistic energy, use a different reference engine.
# 
# Below, the ``from_smiles`` function from PLAMS converts a SMILES string to a ``Molecule``. Before running the jobs, ``init()`` needs to have been called (that was done in [Run a reference job](#run-a-reference-job)).

results_files = {}
for name, smiles in ('O2', 'O=O'), ('propene', 'CC=C'), ('CO2', 'O=C=O'):
    results_files[name] = AMSJob(settings=ref_settings, molecule=from_smiles(smiles), name=name).run().rkfpath()
print(results_files)


ri.add_reaction_energy(reactants=(results_files['propene'], results_files['O2']),
                       products=(results_files['CO2'], water_ams_results_file),
                       normalization='r0',   # make the coefficient for the first reactant (propene)
                       normalization_value=1.0, #  == 1.0
                       task='GeometryOptimization',
                       sigma=5.0)
print(ri.data_set[-1])


# The ``add_reaction_energy`` results importer also works for reactions **without reference jobs**. If you know the reaction energy, for example from experimental data or from computational codes not supported by ParAMS, it is enough to simply pass in ``Molecule``s instead of ams.rkf files. This is demonstrated below for the reaction C$_2$H$_4$(g) + HCl(g) → C$_2$H$_5$Cl(g)

ri.add_reaction_energy(reactants=[from_smiles('C=C'), from_smiles('Cl')],
                       products=[from_smiles('CCCl')],
                       reactants_names=['ethylene', 'HCl'],
                       products_names=['chloroethane'],
                       task='GeometryOptimization',
                       normalization='r0',
                       reference=-17.1,
                       unit='kcal/mol',
                       metadata={
                           'Source': 'J. Appl. Chem. USSR, 1979, 52, 1439-1442',
                       })
print(ri.data_set[-1])


# The jobs added to the job collection will be run during the parametrization. The **ReferenceEngineID** is set to None, since the molecule did not come from a reference calculation but simply as a set of XYZ coordinates. For example, the job ``'chloroethane'`` looks like this:

print(ri.job_collection['chloroethane'])


# ### Training set, validation set, and other data sets
# 
# ParAMS can handle an arbitrary number of data sets. Often during parametrization, it is a good idea to have a validation set. During the parameter fitting, the loss function for the training set is minimized, and the loss function for the validation set is monitored to make sure that there is no overfitting.
# 
# By default, the data set entries added with a results importer are added to the **training set**. To specify a different data set, simply add for example ``data_set='validation_set'`` to the results importer. For example:

ri.add_singlejob(water_ams_results_file, properties=['energy'], data_set='validation_set')


# The training set can be accessed with either ``ri.data_set`` or ``ri.get_data_set('training_set')``. The validation set is accessed with ``ri.get_data_set('validation_set')``:

print(ri.get_data_set('validation_set'))


# ### Exit PLAMS
# 
# If you used PLAMS to run the reference jobs, the ``finish()`` function [should be called at the end](../../../plams/started.html#running-plams), if ``init()`` was called at the beginning.

finish()


# ### Save to disk
The :meth:`store()` method saves
# * the job collection to ``job_collection.yaml`` and ``job_collection.pkl``
# * the training set to ``training_set.yaml`` and ``training_set.pkl``
# * any other data sets, e.g. ``validation_set.yaml`` and ``validation_set.pkl``
# * the engine collection to ``engine_collection.yaml``
# * the settings used for the results importer to ``results_importer_settings.yaml``
# 
# The ``.yaml`` files are text based, and the ``.pkl`` files are binary. The binary files are faster to load than the text files.

ri.store(folder='saved_files', backup=True, text=True, binary=True)


# You can later load those files into another results importer in a separate script. It is in general recommended to repeatedly extend a data_set, rather than to create many small data_sets and try to merge them all at once. This is because entries in the job_collection and data_set need to be unique.
# 
# To load from files, initialize the results importer with 
# ```text
# new_ri = ResultsImporter(job_collection='/path/job_collection.pkl', 
#                          data_set={'training_set': '/path/training_set.yaml', 'validation_set': '/path/validation_set.yaml'}, 
#                          engine_collection='/path/engine_collection.yaml', 
#                          settings='/path/results_importer_settings.yaml')
# ```
