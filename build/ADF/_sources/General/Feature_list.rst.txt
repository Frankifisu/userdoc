.. _LISTOFFEATURES: 

Feature List
************

Model Hamiltonians
==================

* :ref:`XC energy functionals and potentials<XC>`

  * :ref:`LDA<LDA>`, :ref:`GGA<GGA>`, :ref:`meta-GGA<MetaGGA>`, :ref:`model potentials<MODELPOTENTIALS>` 
  * :ref:`(meta-)hybrid <hybrids>`, :ref:`range-separated<RS_FUNCTIONAL>`, :ref:`double-hybrids<DoubleHybrid>`
  * :ref:`dispersion corrected<MM dispersion>` 

* :ref:`Many-Body Perturbation Theory<MBPT>`

  + :ref:`MP2 <MP2>`, :ref:`RPA <RPA>`
  + :ref:`GW approximation<GWscheme>`: G\ :sub:`0`\ W\ :sub:`0`, evGW

* :ref:`Relativistic effects <RELATIVITY>`
  
  * scalar relativity, spin-orbit coupling
  * ZORA, X2C

* Solvents and other environments
 
  * :ref:`COSMO<COSMO>`, :ref:`SM12<SM12>`, :ref:`DIM/QM<DIMQM>`, :ref:`QM/FQ<FQQM>`, :ref:`SCRF<SCRF>`, :ref:`FDE<FDE>`, :ref:`3D-RISM <3D-RISM>`
  * Quild, QM/MM, QM/QM (see the `Hybrid engine <../../Hybrid/index.html>`__)

* Homogeneous electric field and point charges (see |AMS|)

Structure and Reactivity
========================

* Geometry Optimizations (see |AMS|)
* Linear transit, PES scan, Transition state search, Nudged Elastic Band (NEB) (see |AMS|)
* Intrinsic Reaction Coordinate (IRC) (see |AMS|)
* :ref:`Excited state optimizations with TDDFT gradients<EXCITEDGO>` (see also |AMS|)

Optimizations can be done in Cartesian and delocalized coordinates. Various restraints and constraints can be imposed. Hessians are available analytically for most GGAs, and numerically otherwise. Preoptimization is possible, for example, with DFTB.

Spectroscopic properties
========================

* Vibrational Spectroscopy (see |AMS|)

  * IR frequencies and intensities (see |AMS|)
  * Mobile Block Hessian (MBH),  Vibrational Circular Dichroism (VCD) (see |AMS|)
  * Raman intensities (see |AMS|)
  * Resonance Raman frequency-dependent polarizabilities or excited state gradients (see |AMS|)
  * vibrational Raman optical activity (VROA) (see |AMS|)
  * Franck-Condon Factors  (see |AMS|)

* :ref:`Excitation energies: UV/Vis spectra, X-ray absorption, CD, MCD<excitation energies>`

  * :ref:`UV/Vis spectra, oscillator strengths<UV_VIS>`,  :ref:`open shell excitations<EXCITATION_OPEN>`,  :ref:`spin-orbit coupled excitations<excitations SO>`
  * :ref:`core excitations<EXCITATION_CORE>`,  :ref:`Quadrupole oscillator strengths<quadrupole oscillator strength>`, :ref:`XES<XES>`
  * :ref:`TD-DFT+TB<TD-DFTB>`, :ref:`sTDA, sTDDFT<sTDA>`
  * vibrationally resolved electronic spectra (see |AMS|)
  * :ref:`excited state optimizations<EXCITEDGO>` (see also |AMS|)
  * :ref:`CD spectra<UV_VIS>`,  :ref:`MCD<MCD>`
  * :ref:`LFDFT<LFDFT>`

* :ref:`(Hyper-)Polarizabilities, dispersion coefficients, ORD, magnetizabilities, Verdet constants<POLARIZABILITIES>`

  * :ref:`frequency-dependent (hyper)polarizabilities<response>`,  :ref:`lifetime effects<LIFETIMEEFFECTS>`
  * :ref:`POLTDDFT<POLTDDFT>`
  * :ref:`van der Waals dispersion coefficients<C6DISPERSION>`
  * :ref:`optical rotatory dispersion (ORD)<ORD>`
  * :ref:`magnetizability<MAGNETIZABILITY>`
  * :ref:`Verdet constants, Faraday terms <AORESPONSE>`

* NMR 

  * :ref:`chemical shifts<NMR_SHIELDING_NMR>` 
  * :ref:`spin-spin couplings<NMR ss coupling const>` 

* ESR (EPR)

  * :ref:`g-tensors (g-factor)<ESR>` 
  * :ref:`A-tensor (hyperfine interaction)<ESR>`
  * :ref:`zero-field splitting (ZFS, D-tensor)<ESR>` 

* :ref:`Nuclear quadrupole interaction (EFG), ESR Q-tensor<EFG>` 
* :ref:`Mössbauer<MOSSBAUER>`,  :ref:`NRVS<NRVS>` 



Charge transport properties
===========================

* :ref:`charge transfer integrals<TRANSFERINTEGRALS>` 
* :ref:`Non-self-consistent Green's function calculation<GREEN>`



Analysis
========

* :ref:`Fragments<FRAGMENTS>` 
* :ref:`Bond energy decomposition<BE_ANALYSIS>`,  :ref:`ETS-NOCV<NOCV>` 
* Advanced charge density and MO analysis

  * :ref:`Mulliken<results mulliken>`,  :ref:`Multipole-derived charges<MDC>` 
  * :ref:`Hirshfeld charges, Voronoi deformation density<ATOMCHARGES>`,  :ref:`CM5 charges<CM5>`, :ref:`FOD<FOD>`
  * :ref:`bond orders: Mayer, Nalewajski-Mrozek<BONDORDERS>` 
  * :ref:`Bader (QT-AIM)<BADER>`, :ref:`Conceptual DFT<ConceptualDFT>`
  * :ref:`NB0 6.0<NBO>` 
  * :ref:`(partial) DOS<DOS>` 

* :ref:`Molecular symmetry<SYMMETRY>`, :ref:`Schönfliess symbols and symmetry labels<SCHOENFLIES>`



Accuracy and Efficiency
=======================

* :ref:`Slater-type basis sets<BASIS>`

  * :ref:`Z = 1 to 120, all electron, frozen-core, non-relativistic and relativistic<basis sets>`
  * :ref:`SZ, DZ, DZP, TZP, TZ2P, QZ4P, even-tempered, diffuse<basis sets>`

* :ref:`Integration scheme<ACCURACY>`
* Parallelization (see |AMS|)
* :ref:`Linear scaling / distance cut-offs<LINEARSCALING>`
* :ref:`Density fit<DENSITYFIT>` and  :ref:`frozen core approximation<FROZEN_CORE>`
* SCF convergence: :ref:`simple damping, DIIS, EDIIS, ADIIS, LISTi, ARH<DIIS>`

.. |AMS| replace:: `AMS driver <../../AMS/index.html>`__
