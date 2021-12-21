.. _qe_geometry_optimization: 

Geometry and Lattice Optimization
*********************************

This tutorial will teach you how to: 

* set up an optimization of the geometry (including lattice) of a solid with Quantum ESPRESSO
* view the results using AMSmovie


Step 1: Start AMSinput
======================

.. rst-class:: steps

  \
    | Start AMSinput
    | Switch to **Quantum ESPRESSO**: |ADFPanel| **→** |QuantumESPRESSOPanel|

If you have not yet installed Quantum ESPRESSO a dialog will pop up suggesting to install Quantum ESPRESSO by downloading it from the SCM web site.
This is required for this tutorial to work. Downloading may take a while as it is a big package.

.. image:: /Images/QEGeometryOptimization/QE-main.png


Step 2: Set up the system - Silicon
===================================

.. rst-class:: steps

  \
    | Press cmd-F or ctrl-F to activate the search box |Search|
    | Type 'Si' in the search box
    | Click on 'Si' in the list of Crystals
    | Click on |PeriodicViewTool| to enable the periodic display

As we want to demonstrate lattice optimization, we will change the lattice a little so something will happen:

.. rst-class:: steps

  \
    | In the Main panel click the |MoreBtn| button to the right of the Periodicity option
    | Change all non-zero values in the lattice vectors to 3.0

.. image:: /Images/QEGeometryOptimization/lattice-editted.png
  :align: center


Step 3: Setting up the calculation
==================================

First set up the required geometry optimization:

.. rst-class:: steps

  \
    | Click on Main to go back to the Main panel
    | Switch the **Task** to **GeometryOptimization**
    | Click the |MoreBtn| button to go to the optimization details
    | Check the **Optimize lattice** check box

.. image:: /Images/QEGeometryOptimization/optimize-lattice.png
  :align: center

.. rst-class:: steps

  \
    | Click on Main to go back to the Main panel

We also need to set up the general calculation options. 

For this tutorial we will leave most options at their default values.
For real-live application you certainly will have to check if your results are converged with respect to the K-points grid and wavefunction energy cutoff.

One option that must be set by the user is the pseudopotential to use. 
The three options that follow the Pseudopotentials title work as a filter: all pseudopotentials from the pseudopotential directory that
are available for the elements in your system are shown. By choosing options (relativity, XC and type) you narrow down the list of available pseudopotentials.

.. rst-class:: steps

  \
    | Move your mouse over the pseudopotentials Type menu, and check the information in the balloon

.. image:: /Images/QEGeometryOptimization/pptype-balloon.png
  :width: 80%
  :align: center

.. rst-class:: steps

  \
    | Select 'PBE' from the **XC** menu
    | Select 'van' from the **Type** menu


This is just an example, you will need to determine yourself (through calculation and/or literature) which pseudopotentials are best fit for your work. 
The choice we make in this tutorial is in no way an advise on which pseudopotential to use.

Finally, set an appropriate k-space sampling (see :ref:`k_space_sampling` for some recommendation).

.. rst-class:: steps

  \
    | Set **K-points N** to ``10, 10, 10``


.. image:: /Images/QEGeometryOptimization/geometry-setup.png



Step 4: Running your job
========================

Running your job on your local machine is very simple:

.. rst-class:: steps

  \
    | Use the Run command from the File menu: **File → Run**
    | In the Save File dialog that pops up save your job as 'silicon-geometry'

Your job should start running. In the AMSjobs window you can follow its progress, click on the progress lines to open AMStail showing full details of the progress.

When your job is ready AMSjobs will show this, and AMSinput will prompt you to update the geometry.
If you click 'Yes' the geometry (both the atom coordinates and the lattice vectors) will be updated with the results of your calculation.
Now you could continue to perform any other calculation on the optimized system using Quantum ESPRESSO or other AMS engines (like BAND or DFTB).


Step 5: Checking the results
============================

At the end of the calculation an RKF file is automatically created based on the results of Quantum ESPRESSO. RKF files are used by the programs of the AMS suite,
so we can now use all the GUI modules to examine the results.

In this tutorial we will have a look at the geometry optimization using AMSmovie:

.. rst-class:: steps

  \
    | In AMSjobs make sure your silicon-geometry job is selected (by clicking on it)
    | Start AMSmovie **SCM → Movie**

.. rst-class:: steps

  \
    | **In AMSmovie:**
    | show the energy graph: **Graph → Energy**
    | In AMSmovie, show the length of a lattice vector: **Graph → Lattice Vector Length → Vector 1**
    | Click the play button on the left

.. image:: /Images/QEGeometryOptimization/geometry-graph.png
