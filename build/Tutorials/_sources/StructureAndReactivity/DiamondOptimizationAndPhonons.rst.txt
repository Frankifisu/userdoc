.. This tutorial has been recorded: examples/tutorials/ams-phonons
.. Keep the recording in sync so it may be used to generate the images!

.. _Diamond_lattice_optim:

Diamond Lattice Optimization and Phonons
****************************************

This tutorial will show you how to:

* Perform a |GO| (including lattice vectors optimization) for a periodic system
* Calculate and visualize the |phonon| dispersion curves

Set up the calculation
======================

Let us begin by starting up the AMSinput GUI module:

.. rst-class:: steps

  \
    | 1. Start **AMSjobs**
    | 2. Click on **SCM → New Input**. This will open **AMSinput**
    | 3. In **AMSinput**, select the DFTB panel: |ADFPanel| **→** |DFTBPanel|


Now we will import the diamond structure from our database:

.. rst-class:: steps

  \
    | 1. Search for **Diamond** in the **search box** |Search|
    | 2. Select **Crystals → C**

.. image:: /Images/DiamondOptimizationAndPhonons/phonons_import_diamond.png


Phonons should be calculated for the optimal geometry. We therefore first need to perform a |GO|:

.. rst-class:: steps

  \
    | In the **Main panel**
    | 1. Select **Task → Geometry Optimization**

By default, only the internal degrees of freedom are optimized in a geometry optimization (i.e. the atomic positions within the unit cell are optimized, but the lattice vectors are **not** optimized).
In order to obtain a proper phonon spectrum, one **needs to optimize the lattice vectors as well as the internal degrees of freedom**.
When optimizing the geometry for a phonon calculation, we generally recommend using a strict convergence threshold for both the nuclear and lattice degrees of freedom.

.. rst-class:: steps

  \
    | 1. Click on **Details → Geometry Optimization**
    | 2. **Tick** the **Optimize Lattice** check-box
    | 3. Set the **Gradient Convergence** threshold to **1e-4** Hartree/Angstrom
    | 4. Set the **Stress energy per atom** threshold to **1e-5** Hartree

.. image:: /Images/DiamondOptimizationAndPhonons/phonons_geo_opt_details.png

Finally we also need to specify that we want to calculate phonons at the end of the optimization.

.. rst-class:: steps

  \
    | 1. Switch to the **Properties → Phonons and Elastic tensor** panel
    | 2. **Tick** the **Phonons** check-box

Optionally, you can tweak the settings of the |phonon| calculation in the panel **Details → Phonons**. Using a larger super cell in **Details → Phonons** will result in more accurate phonon curves, but will also significantly increase the computation time.

.. image:: /Images/DiamondOptimizationAndPhonons/phonons_enabled.png

We will now set a few options specific to |DFTB|.

.. rst-class:: steps

  \
    | 1. Go to the **Main panel**
    | 2. Select **Model → SCC-DFTB**
    | 2. Select **Parameter Directory → DFTB.org/mio-1-1**
    | 3. Go to the **Details → K-Space Integration** panel
    | 4. Set **K-space grid type** to **Symmetric**

.. image:: /Images/DiamondOptimizationAndPhonons/phonons_kspace.png

We explicitly ask for the symmetric k-space integration grid for our calculation of diamond, which is a highly symmetric system. For such a system the symmetric grid is more accurate and faster. However, unless your system is highly symmetric, we recommend using the default (regular) grid.


Run the calculation
===================

We are now ready to run the calculation.

.. rst-class:: steps

  \
    | 1. Click on **File → Save** and name it "diamond_phonons"
    | 2. Click on **File → Run**


This will open **AMSjobs** and start the calculation. You can monitor the progress of your calculation by opening the log file:

.. rst-class:: steps

  \
    | In **AMSjobs**:
    | 1. Right-click on your job and select **Logfile** to see the log file
    | 2. Right-click on your job and select **Movie** to monitor the progress of the geometry optimization
    | 3. Click on **Graph → Lattice Vectors** to monitor also the lattice optimization
    | 3. Wait for the calculation to finish. It should only take a couple of steps.

.. image:: /Images/DiamondOptimizationAndPhonons/phonons_opt.png

As you can see the high symmetry of the system is maintained: All angles between the lattice vectors are 60 degrees and all vectors keep the same length.
However, the entire crystal has shrunk ever so slightly.
(The strict nuclear gradients convergence threshold we set earlier actually did not matter, as all the nuclear gradients disappear due to the symmetry of the system. We were therefore essentially only optimizing the lattice degrees of freedom.)


Visualize the Phonons
=====================

Once the calculation is completed, you can visualize the phonon dispersion curves:

.. rst-class:: steps

  \
    | In **AMSjobs**, right-click on your job and select **Band Structure**

This will open the AMSbandstructure visualization program:

.. image:: /Images/DiamondOptimizationAndPhonons/phonons_dispersion.png


You can visualize the motion of the atoms for certain modes (marked by a blue dot in the dispersion curves):

.. rst-class:: steps

  \
    | Click on one of the "Modes" dots in the phonon dispersion curves


.. image:: /Images/DiamondOptimizationAndPhonons/phonons_modes.png


You can also visualize the electronic band structure and density of states computed by |DFTB|:

.. rst-class:: steps

  \
    | In the AMSbandstructure module, click on **Options → Bandstructure**


.. image:: /Images/DiamondOptimizationAndPhonons/phonons_band_structure.png



Thermodynamic properties derived from the phonon calculation are printed to the output file. To open the output file:

.. rst-class:: steps

  \
    | In **AMSjobs**, right-click on your job and select **Output**
    | In **AMSoutput**, search for "Thermo"


.. image:: /Images/DiamondOptimizationAndPhonons/phonons_out_thermo.png


.. |GO| replace:: `geometry optimization <../../AMS/Tasks/Geometry_Optimization.html>`__

.. |DFTB| replace:: `DFTB <../../DFTB/index.html>`__

.. |phonon| replace:: `phonon <../../AMS/Vibrational_Spectroscopy.html#phonons>`__
