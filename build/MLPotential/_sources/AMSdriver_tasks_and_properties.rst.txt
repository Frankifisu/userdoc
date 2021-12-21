
.. index:: AMS driver

AMS driver's tasks and properties
#################################

MLPotential is an `engine <../AMS/Engines.html>`__ used by the AMS driver. While the specific options for the MLPotential engine are described in this manual, the definition of the system, the selection of the task and certain (potential-energy-surface-related) properties are documented in the AMS driver's manual.

In this page you will find useful links to the relevant sections of the `AMS driver's Manual <../AMS/index.html>`__.

.. index:: Geometry
.. index:: Atoms
.. index:: Coordinates
.. index:: Lattice Vectors
.. index:: Charge
.. index:: Isotopes
.. index:: Point Charges
.. index:: xyz


Geometry, System definition
===========================

The definition of the system, i.e. the atom types and atomic coordinates (and optionally, the lattice vectors and atomic masses for isotopes) are part of the AMS driver input. See the `System definition section of the AMS manual <../AMS/System.html>`__.


.. index:: AMS driver
.. index:: Task
.. index:: Potential Energy Surface
.. index:: PES
.. index:: Single Point 
.. index:: Geometry Optimization
.. index:: Transition State Search 
.. index:: IRC (Intrinsic Reaction Coordinate)
.. index:: PESScan (Potential Energy Surface Scan)
.. index:: Linear Transit
.. index:: NEB (Nudged Elastic Band)
.. index:: Vibrational Analysis
.. index:: Molecular Dynamics
.. index:: GCMC (Grand Canonical Monte Carlo)


Tasks: exploring the PES
========================

The job of the AMS driver is to handle all changes in the simulated system's geometry, e.g. during a geometry optimization or molecular dynamics calculation, using energy and forces calculated by the engine.

These are the tasks available in the AMS driver:

* `GCMC (Grand Canonical Monte Carlo) <../AMS/Tasks/GCMC.html>`__
* `Geometry Optimization <../AMS/Tasks/Geometry_Optimization.html>`__
* `IRC (Intrinsic Reaction Coordinate) <../AMS/Tasks/IRC.html>`__
* `Molecular Dynamics <../AMS/Tasks/Molecular_Dynamics.html>`__
* `NEB (Nudged Elastic Band) <../AMS/Tasks/NEB.html>`__
* `PESScan (Potential Energy Surface Scan, including linear transit) <../AMS/Tasks/PES_Scan.html>`__
* `Single Point <../AMS/Tasks/Single_Point.html>`__
* `Transition State Search <../AMS/Tasks/Transition_State_Search.html>`__
* `Vibrational Analysis <../AMS/Vibrational_Spectroscopy.html>`__



.. index:: Elastic tensor
.. index:: Nuclear gradients (forces)
.. index:: Hessian
.. index:: Thermodynamic properties
.. index:: PES point character
.. index:: Phonons
.. index:: Stress tensor
.. index:: Elastic tensor

Properties in the AMS driver
============================

The following properties can be requested to the MLPotential engine in the AMS driver's input: 

* `Elastic tensor <../AMS/Gradients_Stress_Elasticity.html#elastictensor>`__
* `Hessian <../AMS/Gradients_Stress_Elasticity.html#hessian>`__
* `Nuclear gradients (forces) <../AMS/Gradients_Stress_Elasticity.html#nucleargradients>`__
* `Normal modes <../AMS/Vibrational_Spectroscopy.html#irfrequencies>`__
* `PES point character <../AMS/Gradients_Stress_Elasticity.html#pespointcharacterization>`__
* `Phonons <../AMS/Vibrational_Spectroscopy.html#phonons>`__
* `Stress tensor <../AMS/Gradients_Stress_Elasticity.html#stresstensor>`__
* `Thermodynamic properties <../AMS/Vibrational_Spectroscopy.html#thermodynamics>`__
