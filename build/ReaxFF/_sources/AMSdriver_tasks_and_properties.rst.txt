
.. index:: AMS driver

.. _ams_tasks:

AMS driver's tasks and properties
#################################

ReaxFF is an `engine <../AMS/Engines.html>`__ used by the AMS driver. While ReaxFF's specific options and properties are described in this manual, the definition of the system, the selection of the task and certain (PES-related) properties are documented in the AMS driver's manual.

In this page you will find useful links to the relevant sections of the `AMS driver's Manual <../AMS/index.html>`__.

.. index:: Geometry
.. index:: Atoms
.. index:: Coordinates
.. index:: Lattice Vectors
.. index:: Charge
.. index:: Isotopes
.. index:: xyz


Geometry, System definition
===========================

The definition of the system, i.e. the atom types and atomic coordinates (and optionally, the systems' net charge, the lattice vector, atomic masses for isotopes) are part of the AMS driver input. See the `System definition section of the AMS manual <../AMS/System.html>`__.


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

* `Single Point <../AMS/Tasks/Single_Point.html>`__
* `Geometry Optimization <../AMS/Tasks/Geometry_Optimization.html>`__
* `Transition State Search <../AMS/Tasks/Transition_State_Search.html>`__
* `IRC (Intrinsic Reaction Coordinate) <../AMS/Tasks/IRC.html>`__
* `PESScan (Potential Energy Surface Scan, including linear transit) <../AMS/Tasks/PES_Scan.html>`__
* `NEB (Nudged Elastic Band) <../AMS/Tasks/NEB.html>`__
* `Vibrational Analysis <../AMS/Vibrational_Spectroscopy.html>`__
* `Molecular Dynamics <../AMS/Tasks/Molecular_Dynamics.html>`__
* `GCMC (Grand Canonical Monte Carlo) <../AMS/Tasks/GCMC.html>`__



.. index:: Bond orders
.. index:: Atomic charges
.. index:: Elastic tensor
.. index:: Nuclear Gradients / Forces
.. index:: Hessian
.. index:: Molecules detection
.. index:: Thermodynamic properties
.. index:: PES point character
.. index:: Phonons
.. index:: Stress tensor
.. index:: Elastic tensor

Properties in the AMS driver
============================

The following properties can be requested to the ReaxFF engine in the AMS driver's input: 

* `Bond orders <../AMS/Properties.html#bondorders>`__
* `Atomic charges <../AMS/Properties.html#charges>`__
* `Elastic tensor <../AMS/Gradients_Stress_Elasticity.html#elastictensor>`__
* `Nuclear Gradients / Forces <../AMS/Gradients_Stress_Elasticity.html#nucleargradients>`__
* `Hessian <../AMS/Gradients_Stress_Elasticity.html#hessian>`__
* `Thermodynamic properties <../AMS/Vibrational_Spectroscopy.html#thermodynamics>`__
* `PES point character <../AMS/Gradients_Stress_Elasticity.html#pespointcharacterization>`__
* `Phonons <../AMS/Vibrational_Spectroscopy.html#phonons>`__
* `Stress tensor <../AMS/Gradients_Stress_Elasticity.html#stresstensor>`__
* `Elastic tensor <../AMS/Gradients_Stress_Elasticity.html#elastictensor>`__
