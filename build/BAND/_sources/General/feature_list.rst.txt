
Feature List
************

Model Hamiltonians
==================

* :ref:`XC energy functionals and potentials <XC>`

  * :ref:`LDA <LDA>`, :ref:`GGA <GGA>`, :ref:`meta-GGA <MetaGGA>`, :ref:`Model potentials <ModelPotentials>` 
  * :ref:`Range-separated Hybrids <Range Separated Hybrids>`
  * :ref:`GGA+U (Hubbard) <HubbardU>`
  * :ref:`LibXC library <LIBXC>`
  * :ref:`Grimme dispersion corrections <DispersionCorrection>` 

* :ref:`Relativistic effects: ZORA and spin-orbit coupling <spin_orbit>` (including non-collinear magnetization)

* :ref:`COSMO <COSMO>` solvation model

* Homogeneous :ref:`electric <ElectricField>` and :ref:`magnetic <MagneticField>` fields


Structure and Reactivity
========================

* Geometry optimization, transition state search, linear transit, PES-scan, molecular dynamics via **AMS**. See the `AMS Manual <../../AMS/index.html>`__ for details.

* Formation energy with respect to isolated atoms (which are computed with a fully numerical Herman-Skillman type subprogram)


Spectroscopy and Properties
===========================

* Normal modes, phonon dispersion curves (and related thermodynamic properties) and elastic tensor via **AMS** See the `AMS Manual <../../AMS/index.html>`__ for details.

* Frequency-dependent dielectric function of systems periodic in one, two and three dimensions in the :ref:`Time-dependent Current-DFT <TDCDFT>` (TD-CDFT) formalism

* :ref:`ESR and EPR <ESR_EPR>` (electron paramagnetic resonance) and :ref:`EFG <EFG>` (Nuclear Quadrupole Interaction)


* :ref:`Form factors <FormFactors>` (X-ray structures)

* :ref:`NMR shielding tensor <NMR>`


Charge transport
================

* :ref:`Non-Equilibrium Green's Function <NEGF>` (NEGF) for calculating transmission function and current

* :ref:`Effective mass <EffectiveMass>` for electrons and holes mobility 


Analysis
========

* :ref:`Various Atomic charges <AtomicCharges>`, including Mulliken, Hirshfeld, CM5 and Voronoi

* Mulliken populations for basis functions, overlap populations between atoms or between basis functions

* :ref:`Densities-of-States <DOS>`: DOS, PDOS and OPWDOS/COOP (see also: `Band Structure and COOP tutorial <../../Tutorials/Analysis/BandsAndCOOP.html>`_)

* :ref:`Local Densities-of-States <LDOS>` LDOS (STM images)

* :ref:`3D filed plotting of various properties <3DFieldVisualization>`, such as orbitals (Bloch-waves), deformation densities, Coulomb potentials, ...

* :ref:`Band Structure plot <BandStructure>` along edges of the Brillouin zone 

* :ref:`Fragment <fragments>` orbitals and a Mulliken type population analysis in terms of the fragment orbitals

* :ref:`Quantum Theory of Atoms In Molecules <QTAIM>` (QT-AIM, aka Bader Analysis). Atomic charges and critical points

* Electron Localization Function (:ref:`ELF <ELF>`)

* Fragment based Periodic Energy Decomposition Analysis (:ref:`PEDA <PEDA>`)

* PEDA combined with Natural Orbitals for Chemical Valency (NOCV) to decompose the orbital relaxation (:ref:`PEDA-NOCV <PEDA-NOCV>`) 



.. Technical Overview
.. ==================


.. .. math::

..    H \psi_i^\mathbf{k} (\mathbf{r}) = \epsilon_i^\mathbf{k} \psi_i^\mathbf{k} (\mathbf{r})


.. .. math::

..    \left[ \hat{T} + V_\text{nuclei} (\mathbf{r}) + V_\text{electrons}(\rho(\mathbf{r}),\mathbf{r}) + V_\text{XC} (\rho(\mathbf{r}),\mathbf{r}) \right] \psi_i^\mathbf{k} (\mathbf{r}) = \epsilon_i^\mathbf{k} \psi_i^\mathbf{k} (\mathbf{r})




.. Bloch functions and basis set
.. -----------------------------


.. The Bloch functions :math:`\psi_i^\mathbf{k} (\mathbf{r})` are constructed from the basis functions :math:`\chi_j (\mathbf{r})` as follows:

.. .. math::

..    \psi_i^\mathbf{k} (\mathbf{r}) & = \sum_j C_{ij}^\mathbf{k} \phi_j^\mathbf{k} (\mathbf{r})

..    \phi_j^\mathbf{k} (\mathbf{r}) & =  \sum_\mathbf{R} e^{i \mathbf{k} \mathbf{R}} \chi_j(\mathbf{r}-\mathbf{R}) 

.. where :math:`\mathbf{R}` is a lattice translation, :math:`\mathbf{k}` is a vector in the first Brillouin zone (see also :ref:`KSpace <keyscheme KSPACE>`) and :math:`C_{ij}^\mathbf{k}` are expansion coefficients (often called orbital coefficients).

.. The atom-centered basis functions :math:`\chi_j (\mathbf{r})` are the product of a radial function :math:`R(\bar{r})` and a Real Spherical Harmonic :math:`Z^{\ell}_{m} (\bar{\theta}, \bar{\phi})`:

.. .. math::

..    \chi(\mathbf{r}) = R(\bar{r}) Z^{\ell}_{m} (\bar{\theta}, \bar{\phi})

.. where :math:`(\bar{r},\bar{\theta},\bar{\phi})` are spherical coordinates centered on the nucleus.

.. The Basis Sets consists of NAOs (Numerical Atomic Orbitals, obtained by solving numerically the Kohn-Sham equations for the isolated spherical atoms) augmented by a set of STOs (Slater Type Orbitals).
