Spectroscopy and properties
###########################


Electronic structure of periodic systems
========================================

.. index:: Band structure
.. index:: Fat bands

.. scmautodoc:: dftb Periodic EffectiveMass BandStructure BZPath DOS


.. _TDDFTB:

Excited states with time-dependent DFTB
=======================================

DFTB allows for excited state calculations on molecular systems by means of single orbital transitions as well as time-dependent DFTB as published by Niehaus et al. in *Phys. Rev. B* **63**, 085108 (2001).
Singlet-singlet as well as singlet-triplet excitations can be calculated.
DFTB also supports the calculation of excited state gradients, which allows geometry optimizations and vibrational frequency calculations for excited states.

The TD-DFTB implementation uses the PRIMME library (PReconditioned Iterative MultiMethod Eigensolver) by Andreas Stathopoulos and James R. McCombs,  `PRIMME: PReconditioned Iterative MultiMethod Eigensolver <http://www.cs.wm.edu/~andreas/publications/primmeTOMS.pdf>`__:  `Methods and software description ACM Transaction on Mathematical Software Vol. 37, No. 2, (2010), 21:1--21:30 <https://doi.org/10.1145/1731022.1731031>`__.

DFTB excited state calculations are controlled by the following keywords:

.. scmautodoc:: dftb Properties Excitations


.. index:: Phonons
.. index:: Thermodynamic properties
.. index:: Zero-point energy
.. index:: Internal energy
.. index:: Entropy
.. index:: Free energy
.. index:: Specific heat
.. index:: Hessian
.. index:: Normal modes
.. index:: Frequencies

Excited state gradients
=======================

Excited state gradients can be calculated with TD-DFTB, see the section :ref:`Excited states with time-dependent DFTB <TDDFTB>`.

Frequencies, phonons, VCD
=========================

Frequencies, phonons, and VCD and can be computed via numerical differentiation by the AMS driver.
Several thermodynamic properties, such as zero-point energy, internal energy, entropy, free energy and specific heat are computed by default when calculating phonons.

* `AMS manual: Vibrational Analysis <../AMS/Vibrational_Spectroscopy.html>`__

  + `AMS manual: Infrared (IR) spectra / Normal Modes <../AMS/Vibrational_Spectroscopy.html#irfrequencies>`__
  + `AMS manual: Phonons <../AMS/Vibrational_Spectroscopy.html#phonons>`__
  + `AMS manual: Thermodynamic properties <../AMS/Vibrational_Spectroscopy.html#thermodynamics>`__
  + `AMS manual: VCD (Vibrational Circular Dichroism) <../AMS/Vibrational_Spectroscopy.html#vcd>`__

.. index:: vibrationally resolved electronic spectra 
.. index:: Franck-Condon factors 
.. index:: fluorescence 
.. index:: phosphorescence 

Vibrationally resolved electronic spectra
=========================================

* `AMS manual: Vibrationally resolved electronic spectra <../AMS/Vibrationally_resolved_electronic_spectra.html>`__.

  + `AMS manual: AH-FC Adiabatic Hessian Franck-Condon <../AMS/Utilities/FCF_module.html>`__.
  + `AMS manual: VG-FC Vertical Gradient Franck-Condon <../AMS/Utilities/FCF_module.html>`__.

.. index:: Elastic tensor
.. index:: Bulk modulus
.. index:: Shear modulus
.. index:: Young modulus

Stress tensor, Elasticity
=========================

The stress tensor and elastic tensor (and related elastic properties such as bulk modulus, shear modulus and young modulus) can be computed via numerical differentiation by AMS.

* `AMS manual: Stress tensor <../AMS/Gradients_Stress_Elasticity.html#stresstensor>`__
* `AMS manual: Elastic tensor <../AMS/Gradients_Stress_Elasticity.html#elastictensor>`__

.. index::Mayer bond orders

Charges, Bond Orders, Dipole Moment, Polarizability
===================================================

Charges, Mayer bond orders, Dipole Moment, and Polarizability can be requested to the DFTB engine in the AMS driver's input:

* `AMS manual: Atomic charges <../AMS/Properties.html#charges>`__
* `AMS manual: Bond orders <../AMS/Properties.html#bondorders>`__
* `AMS manual: Dipole Moment  <../AMS/Properties.html#dipolemoment>`__
* `AMS manual: Dipole Gradients <../AMS/Properties.html#dipolegradients>`__

.. _PROPERTIES:
.. _FRAGMENTS:

Fragment orbital analysis
=========================

The fragment orbital analysis is not available for periodic systems calculated with multiple K-points.

A Mulliken population analysis based on the elementary atomic basis functions can be calculated with

::

   Properties
      Fragments
      End
   End

For an atomic Mulliken population one should not specify any subkey ``File`` in Properties%Fragments.

A Mulliken population analysis based on orbitals coming from larger fragments, that may consist of more than 1 atom, can be calculated if one includes the binary dftb.rkf result files of the calculated fragments in the input, for example, like:

::

   Properties
      Fragments
         File frag1.results/dftb.rkf
         File frag2.results/dftb.rkf
      End
   End

Note that the nuclear coordinates of the atoms in the fragments should be at the exact same position as in the whole system.
In addition, each atom of the whole system should be present exactly once in one of the fragment dftb.rkf files.

.. scmautodoc:: dftb Properties Fragments
   :noref:
   :skipblockdescription:

.. index::NBO

NBO analysis
============

An input for the GENNBO program of Prof. Weinholds Natural Bond Orbital (NBO) package, by E. Glendening et al. can be made, using the key Properties%NBOInput.
Not available for periodic systems.

.. scmautodoc:: dftb Properties NBOInput
   :noref:
   :skipblockdescription:

The GENNBO executable is included in the AMS distribution.
The GENNBO program can be called with:

.. code-block:: none

   #!/bin/sh
   $AMSBIN/gennbo6 ams.results/dftb-nboInput.FILE47
