
Structure and Reactivity
########################


\ 
   | **See also:**
   | ADF-GUI tutorials: `geometry optimization <../../Tutorials/GettingStarted/GeometryOptimizationOfEthanol.html>`_,  `vibrational frequencies <../../Tutorials/VibrationalSpectroscopy/IRSpectrumOfEthane.html>`_, `spin coupling in Fe4S4 <../../Tutorials/ElectronicStructureModelHamiltonians/SpinCouplingInFe4S4Cluster.html>`_ 
   | Examples: :ref:`geometry optimization<examples GO>`, :ref:`reactivity<examples reactivity>` 


Single point calculations
=========================

.. index:: single point

A single point calculation calculates one point on the potential energy surface.

* `Single point calculations section of the AMS manual <../../AMS/Tasks/Single_Point.html>`__.

Geometry optimization
=====================

.. index:: geometry optimization 
.. index:: delocalized coordinates
.. index:: initial Hessian 
.. index:: constrained optimizations 
.. index:: block constraints 
.. index:: restrained optimizations 

A geometry optimization tries to find a (local) minimum on the potential energy surface, where the gradients are zero and the Hessian only has positive eigen values.
With AMS one can do an optimization using delocalized or Cartesian coordinates. Constraints (also block constraints) and restraints are possible. An initial Hessain can be provided.

* `Geometry Optimization section of the AMS manual <../../AMS/Tasks/Geometry_Optimization.html>`__.

Transition state search
=======================

.. index:: transition state 
.. index:: TS (transition state) 
.. index:: TSRC

A transition state corresponds to a saddle point on the potential energy surface, where the gradients are zero and the Hessian has one negative eigen value.

* `Transition state search section of the AMS manual <../../AMS/Tasks/Transition_State_Search.html>`__.

A reaction coordinate for transition state search can be specified.

Linear Transit, PES scan
========================

.. index:: LT (linear transit) 
.. index:: linear transit
.. index:: PES scan

The PES scan task in AMS allows users to scan the potential energy surface of a system along one or multiple degrees of freedom, while relaxing all other degrees of freedom. If only one coordinate is scanned, this kind of calculation is usually just called a linear transit. 

* `Linear Transit, PES scan section of the AMS manual <../../AMS/Tasks/PES_Scan.html>`__.

Nudged Elastic Band (NEB)
=========================

.. index:: NEB 
.. index:: nudged elastic band

The Nudged Elastic Band (NEB) method can be used to find a reaction path and the transition state between a reactant and a product state.

* `Nudged Elastic Band (NEB) section of the AMS manual <../../AMS/Tasks/NEB.html>`__.

Intrinsic Reaction Coordinate (IRC)
===================================

.. index:: IRC 
.. index:: intrinsic reaction coordinate 
.. index:: reaction path

The path of a chemical reaction can be traced from the transition state to the products and/or reactants using the IRC method.

* `Intrinsic Reaction Coordinate (IRC) section of the AMS manual <../../AMS/Tasks/IRC.html>`__.

Excited state optimizations
===========================

ADF can calculate the nuclear gradient for a particular electronically excited state, which makes it possible to do excited state optimizations.

* :ref:`Excited state gradient section of the ADF manual <EXCITEDGO>`,
* `Excited state optimizations section of the AMS manual <../../AMS/Tasks/Excited_State_Optimizations.html>`__.

Molecular dynamics
==================

.. index:: molecular dynamics

Molecular dynamics can be used to simulate the evolution of a system in time.

* `Molecular dynamics section of the AMS manual <../../AMS/Tasks/Molecular_Dynamics.html>`__.

Gradients, Hessian, Thermodynamics
##################################

Gradients
=========

.. index:: nuclear gradients
.. index:: gradients

A nuclear gradient is the first derivative of the energy with respect to the nuclear coordinates.
The nuclear gradients are not forces, the difference being the sign. 

* `Nuclear gradients section of the AMS manual <../../AMS/Gradients_Stress_Elasticity.html#nuclear-gradients>`__.

Hessian
=========

.. index:: Hessian 
.. index:: force constants
.. index:: partial Hessian

A Hessian is the second derivative of the energy with respect to the nuclear coordinates.

* `Hessian section of the AMS manual <../../AMS/Gradients_Stress_Elasticity.html#hessian>`__.

One can also calculate a partial Hessian. The Hessian calculation is related to the calculation of IR frequencies, see
the `IR frequencies and normal modes section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html#ir-frequencies-and-normal-modes>`__.

PES point character
===================

.. index:: PES point character

The AMS driver can quickly, and without calculating the full Hessian, characterize a PES point as a local minimum, a transition state, a higher order saddle point, or a non-stationary point.

* `PES point character section of the AMS manual <../../AMS/Gradients_Stress_Elasticity.html#pes-point-character>`__.


Thermodynamics, gas phase Gibbs free energy
===========================================

At the end of a completed IR Frequencies (normal modes) calculation, a survey is given of thermodynamic properties: entropy, internal energy, constant volume heat capacity, enthalpy and Gibbs free energy, see:

* `IR frequencies section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html#irfrequencies>`__

  * Thermodynamics
  * Gibbs free energy change for a gas phase reaction
