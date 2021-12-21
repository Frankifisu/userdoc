
========================================
Theory and usage
========================================

The MLPotential engine in the Amsterdam Modeling Suite can calculate the
potential energy surface using several different types of machine learning (ML)
potentials.

Quickstart guide
-----------------------

To set up a simple MLPotential job using the graphical user interface, see the
`ANI-1ccx Thermochemistry tutorial <../Tutorials/StructureAndReactivity/ANI1ccxThermochemistry.html>`__.

Theory of ML potentials
-----------------------------------------

With machine learning potentials, it is possible to quickly evaluate the
energies and forces in a system with close to first-principles accuracy.
Machine learning potentials are fitted (trained, parameterized) to reproduce
reference data, typically calculated using an ab initio or DFT method.
Machine learning potentials are sometimes referred to as machine learning
force fields, or as interatomic potentials based on machine learning.

Several types of machine learning potentials exist, for example neural-network-based
methods and kernel-based methods.

Several types of **neural network potentials** exist. It is common for such
potentials to calculate the total energy as a sum of atomic contributions. In a
**high-dimensional neural network potential** (HDNNP), as proposed by Behler and
Parrinello [#refbehlerparrinello]_, each atomic contribution is calculated by means of a feed-forward
neural network, that takes in a representation of the chemical environment
around the atom as input. This representation, or atomic environment
**descriptor** or **fingerprint**, consists of a vector of rotationally, translationally, and
permutationally invariant functions known as **atom-centered symmetry functions** (ACSF).

**Graph convolutional neural network potentials** (GCNNPs), or **message-passing network neural
potentials**, similarly construct the total energy by summing up atomic
contribution, but the appropriate representations of local atomic chemical
environments are learned from the reference data.

**Kernel-based methods** make predictions based on how similar a system is to
the systems in the training set. 

There are also other types of machine learning potentials. For more detailed
information, see for example references [#refbehlerml]_ and [#refmuellerml]_.


.. _installation:

Installation and uninstallation
-------------------------------

The Amsterdam Modeling Suite by default does not include the Python
packages necessary to run the machine learning potential backends.

If you set up an MLPotential job via the **graphical user interface**, you will be asked
to install the packages if they have not been installed already when you save your input. 
You can also use the `package manager <../GUI/AMSpackages.html>`__. 
Moreover, the run script will also contain instructions to install the necessary packages if needed,
so that you can seamlessly run MLPotential jobs also on `remote machines <../GUI/AMSjobs.html#queues>`__.

A **command-line installation tool** can also be used, for instance to install the torchani backend::

   "$AMSBIN"/amspackages install torchani

The packages are installed into the `AMS Python environment <../Scripting/Python_Stack/Python_Stack.html>`__,
and do not affect any other Python installation on the system. For the
installation, an internet connection is required, unless you have configured the package manager for `offline use <../Installation/Optional_Components.html#using-a-local-package-source>`__ .

To **uninstall** a package, e.g. ``torchani``, run::

   "$AMSBIN"/amspackages remove torchani

The package manager automatically installs necessary python dependencies such as PyTorch, but if you require a different
version you can use pip::

   "$AMSBIN"/amspython -m pip install -U torch

.. note::

   Packages installed through pip alone by the user will not show up as installed in the package manager, but they will
   be detected and used if possible.

If you install the a package into your amspython environment, using ``amspython -m pip install``,
the package manager will not display it in its overview. 
However, it will allow you to make use of it for running calculations with the ML Potential module. 
If you want to make sure that the version you installed will be detected, you can use 

.. code:: sh

      $ "$AMSBIN"/amspackages check --pip torch
      05-11 10:47:57 torch is not installed!
      05-11 10:47:57 User installed version located through pip: torch==1.8.1

We won't be able to guarantee that all versions you install yourself work, but you may for instance be able to use this 
to install GPU supported versions of Torch that match your specific drivers. 
   

Included (pre-parameterized) models
-------------------------------------

A **model** is the combination of a functional form with a set of parameters. Three pre-parameterized models can be selected, ANI-2x, ANI-1ccx, and ANI-1x. The predictions from these models are calculated from **ensembles**, meaning that the final prediction is an average over several independently trained neural networks.

.. csv-table:: Pre-parameterized models for the MLPotential engine
   :delim: ,
   :header: "", "ANI-2x", "ANI-1ccx", "ANI-1x"

   Functional form, HDNNP, HDNNP, HDNNP
   Ensemble size,8,8,8
   Atomic environment descriptor, ACSF, ACSF, ACSF
   Supported elements,"H, C, N, O, F, S, Cl","H, C, N, O","H, C, N, O"
   Training set structures, organic molecules, organic molecules, organic molecules
   Reference method, "ωB97-x/6-31G(d)", "DLPNO-CCSD(T)/CBS", "ωB97-x/6-31G(d)"
   Backend, TorchANI, TorchANI, TorchANI
   Reference, [#refani2x]_, [#refani1ccx]_, [#refani1x]_

For the ANI-\*x models, the standard deviation for the energy predictions are
calculated for the "main" output molecule (e.g., the final point of a geometry
optimization). The summary statistics can be found in the ``mlpotential.txt``
file in the ``worker.0`` subdirectory of the results directory.


.. scmautodoc:: mlpotential Model
   :nosummary:

Custom models (custom parameters)
---------------------------------

Set ``Model`` to **Custom** and specify which backend to use with the ``Backend`` option. 
In a typical case, you would have used that backend to train your own machine
learning potential.

The backend reads the parameters, and any other necessary information (for
example neural network architecture), from either a file or a directory.
Specify the ``ParameterFile`` or ``ParameterDir`` option accordingly, with a
path to the file or directory. Read the backend's documentation to find out
which option is appropriate.

Some backends may require that an energy unit (``MLEnergyUnit``) and/or distance
unit (``MLDistanceUnit``) be specified. These units correspond to the units
used during the training of the machine learning potential. 


Example::

   Engine MLPotential
       Backend SchNetPack
       Model Custom
       ParameterFile ethanol.schnet-model
       MLEnergyUnit kcal/mol
       MLDistanceUnit angstrom
   EndEngine


.. scmautodoc:: mlpotential Backend
   :nosummary:

.. scmautodoc:: mlpotential MLDistanceUnit
   :nosummary:

.. scmautodoc:: mlpotential MLEnergyUnit
   :nosummary:

.. scmautodoc:: mlpotential ParameterDir
   :nosummary:

.. scmautodoc:: mlpotential ParameterFile
   :nosummary:



Backends
------------

.. csv-table:: Backends supported by the MLPotential engine.
   :delim: ,
   :header: "", "PiNN", "SchNetPack", "sGDML", TorchANI
   :widths: 1, 1, 1, 1, 1

   Reference, [#refpinn]_, [#refschnetpack]_, [#refsgdml]_, [#reftorchani]_
   Methods, "HDNNPs, GCNNPs, ...", "HDNNPs, GCNNPs, ...", "GDML, sGDML", "[ensembles of] HDNNPs"
   Pre-built models, none, none, none, "ANI-1x, ANI-2x, ANI-1ccx"
   Parameters from,ParameterDir,ParameterFile,ParameterFile,ParameterFile
   Kernel-based, No, No, Yes, No
   ML framework, TensorFlow 1.15, PyTorch, "none, PyTorch", PyTorch

.. note::

   For **sGDML**, the order of the atoms in the input file **must** match the
   order of atoms which was used during the fitting of the model.

.. note::
    
   If you use a custom parameter file with **TorchANI**, the model specified
   via ``ParameterFile filename.pt`` is loaded with
   ``torch.load('filename.pt')['model']``, such that a forward call should be
   accessible via ``torch.load('filename.pt')['model']((species,
   coordinates))``. The energy shifter is not read from custom parameter files,
   so the absolute predicted energies will be shifted with respect to the
   reference data, but this does not affect relative energies (e.g., reaction energies).

CPU and GPU (CUDA), parallelization
-----------------------------------

By default a calculation will run on the CPU, and use all available CPU power.
To limit the number of threads, the ``NumThreads`` keyword can be used if the
backend uses PyTorch as its machine learning framework.  Alternatively, you can
set the environment variable OMP_NUM_THREADS.

To use a CUDA-enabled GPU, ensure that a CUDA-enabled version of TensorFlow or
PyTorch has been installed (see :ref:`installation`). Then set ``Device`` to
the device on which you would like to run, for example, **cuda:0**.
Calculations are typically much faster on the GPU than on the CPU.


.. scmautodoc:: mlpotential Device
   :nosummary:

.. scmautodoc:: mlpotential NumThreads
   :nosummary:

.. note::

   Because the calculation runs in a separate process, the number of threads is controlled
   by the input keyword NumThreads and *not* by the environment variable NSCM. **We recommend
   setting NSCM=1** when using the MLPotential engine.

   **Only single-node** calculations are currently supported.

Troubleshooting
----------------------------
If you run a PyTorch-based backend and receive an error message starting with::

   sh: line 1: 1351 Illegal instruction: 4 sh 

you may be attempting to run PyTorch on a rather old cpu. You could try to upgrade PyTorch to a newer version::

   "$AMSBIN"/amspython -m pip install torch -U -f https://download.pytorch.org/whl/torch_stable.html

If this does not help, please contact SCM support.

Support
------------------

SCM does not provide support for parameterization using the MLPotential
backends. SCM only provides technical (non-scientific) support for running
simulations via the AMS driver.

Technical information
-----------------------------

Each of the supported backends can be used as `ASE (Atomic Simulation
Environment) calculators <../Scripting/ASE/ASE.html>`__. The MLPotential engine
is an interface to those ASE calculators. The communication between the AMS
driver and the backends is implemented with a `named pipe interface
<../AMS/Input_Output.html#pipe-interface>`__. The MLPotential engine launches a
python script, ``ase_calculators.py``, which initializes the ASE calculator.
The exact command that is executed is written as ``WorkerCommand`` in the
output.



References
----------

.. [#refbehlerparrinello] \J. Behler, M. Parrinello. Phys. Rev. Lett. 98 (2007) 146401 `<https://doi.org/10.1103/PhysRevLett.98.146401>`__

.. [#refbehlerml] \J. Behler. J. Chem. Phys. 145 (2016) 170901. `<https://doi.org/10.1063/1.4966192>`__

.. [#refmuellerml] \T. Mueller, A. Hernandez, C. Wang. J. Chem. Phys. 152 (2020) 050902. `<https://doi.org/10.1063/1.4966192>`__

.. [#refani2x] \C. Devereux et al., J. Chem. Theory Comput. 16 (2020) 4192-4202. `<https://doi.org/10.1021/acs.jctc.0c00121>`__

.. [#refani1ccx] \J. S. Smith et al., Nat. Commun. 10 (2019) 2903. `<https://doi.org/10.1038/s41467-019-10827-4>`__

.. [#refani1x] \J. S. Smith et al., J. Chem. Phys. 148 (2018) 241733. `<https://doi.org/10.1063/1.5023802>`__

.. [#refpinn] \Y. Shao et al., J. Chem. Inf. Model. 60 (2020) 1184-1193. `<https://doi.org/10.1021/acs.jcim.9b00994>`__

.. [#refschnetpack] \K. T. Schütt et al., J. Chem. Theory Comput. 15 (2019) 448-455. `<https://doi.org/10.1021/acs.jctc.8b00908>`__

.. [#refsgdml] \S. Chmiela et al. Comp. Phys. Commun. 240 (2019) 38-45. `<https://doi.org/10.1016/j.cpc.2019.02.007>`__

.. [#reftorchani] \X. Gao et al. J. Chem. Inf. Model (2020). `<https://doi.org/10.1021/acs.jcim.0c00451>`__

