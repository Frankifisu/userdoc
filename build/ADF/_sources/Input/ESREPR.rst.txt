.. index:: ESR 
.. index:: EPR 
.. index:: electron spin resonance 
.. index:: electron paramagnetic resonance 
.. _ESR: 


ESR/EPR
*******

The EPR (ESR) g-tensor, hyperfine interaction (A-tensor), nuclear quadrupole interaction (Q-tensor), and zero-field splitting (ZFS, D-tensor) can be calculated. Effects due to spin-orbit coupling can be included. All electron basis sets can be used. 

The separate program EPR/NMR ($AMSBIN/epr) program is no longer documented, since most of its capabilities are implemented in newer modules. See for the documentation of the EPR/NMR module in the `old ADF 2010 Properties document <http://downloads.scm.com/Doc/Doc2010/ADF/Properties/Properties.pdf>`_, and Refs. [#ref1]_ [#ref2]_. 


.. index:: A-tensor 
.. index:: hyperfine interaction 

.. _keyscheme ESR: 

ESR/EPR g-tensor and A-tensor
=============================

**A-tensor, no spin-orbit coupling**

::

   $AMSBIN/ams << eor
   ...
   Engine ADF
     ESR
     END
     SpinPolarization spinpolarization
     unrestricted Yes
     {Relativity
        level scalar
        formalism ZORA
     End}
     {NUCLEARMODEL gaussian}
     ...
   EndEngine
   eor


If spin-orbit coupling is neglected, the spin in the effective spin Hamiltonian, which is commonly used for the interpretation of ESR experiments, is the real electronic spin of the paramagnetic molecule. In the spin-unrestricted DFT calculations one then uses eigenfunctions of S\ :sub:`z` . The A-tensor can then simply be calculated as expectation value of the corresponding operator, see Ref. [#ref3]_. 

The A-tensor will be calculated for all nuclei. Terms due to the spin-polarization density at the nucleus are included in the evaluation of the A-tensor. For an accurate evaluation of the spin-polarization density at the nucleus it is important to use an all-electron basis set for the nuclei that one is interested in, avoiding the frozen core approximation. For heavy elements the incorporation of a Gaussian finite nucleus model can be important. However, one should have really large basis sets with tight basis functions to observe this effect in calculations. One possibility is to use the $AMSHOME/atomicdata/ADF/ZORA/QZ4P basis set, although even this large basis set is not large enough sometimes. The basis sets in the directories ZORA/TZ2P-J, ZORA/Z4P-J, and ZORA/jcpl are suitable for finite nucleus calculations. 

In case one uses a finite nuclear model for the charge distribution, starting from ADF2013 ADF also uses a finite distribution of the nuclear magnetic dipole moment for the calculation of the A-tensor. 

.. _keyscheme cpl HYPERFINE: 

**A-tensor, perturbative inclusion spin-orbit coupling**

::

   $AMSBIN/ams << eor
   ...
   Engine ADF
     SpinPolarization spinpolarization
     unrestricted Yes
     Relativity
       Level Scalar
       Formalism ZORA
     End
     Symmetry NOSYM
     ...
   EndEngine
   eor
   
   $AMSBIN/cpl << eor
   adffile ams.results/adf.rkf
   hyperfine
    atoms 1 2 :: calculates A-tensor for atom 1 and 2, input order
    SCF Converge=1e-7 {Iterations=25}
   end
   ...
   eor

The calculation of A-tensors is implemented in the CPL program as a second derivative property (spin-orbit coupling and nuclear magnetic field as perturbation) within the two-component relativistic zeroth-order regular approximation (ZORA), see Ref. [#ref4]_. This implementation allows for hybrid (only PBE0) DFT calculations, but not metaGGA's and not metahybrids. 

Note that the CPKS convergence in CPL has to be set tightly (1e-7 or 1e-8) to get converged PSOSO terms for the A-tensor. For hyperfine calculations the default value is 1e-7. 

.. index:: nmr module
.. _keyscheme nmr GFACTORS: 


**g-tensor, perturbative inclusion spin-orbit coupling**

::

   $AMSBIN/ams << eor
   ...
   Engine ADF
     SpinPolarization spinpolarization
     unrestricted Yes
     Relativity
       level scalar
       formalism ZORA
     End
     Symmetry NOSYM
     ...
   EndEngine
   eor
   
   $AMSBIN/nmr << eor
   adffile ams.results/adf.rkf
   nmr
    gfactors 
    u1k best
    calc all
    out iso tens 
   end
   end input
   eor

The calculation of g-tensors is implemented in the NMR program as a second derivative property (spin-orbit coupling and external magnetic field as perturbation) within the two-component relativistic zeroth-order regular approximation (ZORA), see Ref. [#ref5]_. This implementation allows for hybrid (B3LYP, PBE0, etc) DFT calculations, but not metaGGA's and not metahybrids. This implementation requires the use of all electron basis sets. 

For an older implementation of this method,  see the EPR/NMR module documentation in the `old ADF 2010 Properties document <http://downloads.scm.com/Doc/Doc2010/ADF/Properties/Properties.pdf>`_, and Refs. [#ref1]_ [#ref2]_ [#ref8]_ [#ref9]_. 

**g-tensor and A-tensor, self consistent spin-orbit coupling**

::

   $AMSBIN/ams << eor
   ...
   Engine ADF
     ESR
     END
     unrestricted Yes
     Relativity
       Level Spin-Orbit
       Formalism ZORA
       SpinOrbitMagnetization Collinear
     End
     Symmetry NOSYM
   eor

.. index:: g-tensor 

.. index:: Zeeman interaction 

In a spin-orbit coupled spin unrestricted relativistic ZORA calculation and the ESR block key, the g-tensor and the nuclear magnetic dipole hyperfine interaction (A-tensor) will be calculated, see also Refs. [#ref3]_ [#ref10]_. In such a calculation degenerate perturbation theory is used with the external magnetic field or nuclear magnetic field as perturbation. The calculation must use the collinear approximation, and symmetry must be NOSYM. This implementation does allow for metaGGA, and (meta-)hybrid DFT calculations, but then GIAO's are not used. There may be more than one unpaired electron. Terms due to the spin-polarization density at the nucleus are included in the evaluation of the A-tensor. However, one can not set the number of unpaired electrons, the 'spinpolarization' argument of the key CHARGE will be ignored. 

Note: in a spin-orbit coupled spin restricted relativistic ZORA calculation and the ESR block key, ADF will also calculate and print the nuclear magnetic dipole hyperfine interaction, but the terms due to the spin-polarization density at the nucleus are absent. Furthermore, if there is more than one unpaired electron, the computed results will simply be incorrect, without any warning from the program. On the other hand, in case of one unpaired electron, and very large effects of spin-orbit coupling, the spin-restricted calculation may be of interest, since it uses Kramer's symmetry exact. 


ESR/EPR Q-tensor
================

For the calculation of the ESR Q-tensor see the key  :ref:`QTENS<keyscheme QTENS>`. 

.. _ZFS:
.. index:: zero-field splitting 
.. index:: ZFS ground state 

ESR/EPR Zero-field splitting (D-tensor)
=======================================

With the keyword ZFS the zero-field splitting (ZFS) of the ground state can be calculated. 

.. _keyscheme ZFS: 


::

   ZFS
   {HARTREEFOCK}

Zero-field splitting is the breaking of degeneracies of the ground state that is not described by a standard non-relativistic Hamiltonian. ZFS as calculated by ADF is that exhibited by molecules whose ground state has spin S>1/2 and no spatial degeneracy. This type of ZFS has two contributions, second-order spin-orbit coupling and direct electron spin-spin coupling. The calculation of ZFS with DFT is described in Ref. [#ref6]_ [#ref7]_ [#ref11]_ [#ref12]_.
With the keyword ZFS the spin-orbit coupling term is included. If one also wants to calculate the direct electron spin-spin term, one has to include the key HARTREEFOCK, which calculates the Coulomb and (Hartree-Fock like) exchange contributions to the direct electron spin-spin term.
In the spin-orbit coupling term no Hartree-Fock like exchange contributions are included.

::

   HARTREEFOCK

ZFS can be calculated in combination with LDA and GGAs but not hybrid or meta-GGA functionals. In order to calculate ZFS, The ``Relativity -> level`` should be set to ``Scalar`` and ``Relativity -> Formalism`` to ``ZORA`` (these are the default values).

Just the simple keyword ZFS is needed in order to calculate zero-field splitting. Several optional  additional keywords can also be included. The complete list is: 

::

   ZFS {PEDERSON|NEESE} {ANALYSIS|FULLANALYSIS}

``PEDERSON|NEESE``
   PEDERSON: The available approaches for calculating ZFS with DFT each differ subtly from the others.  We believe that the method proposed by van Wüllen and coworkers [#ref11]_ [#ref12]_ is the most theoretically complete but it may be that for certain systems the other approaches are more accurate. The van Wüllen  formulation is the default but if the PEDERSON keyword in included then the equation proposed  by Pederson and Khanna [#ref6]_ is used.  NEESE: If the NEESE keyword is included then the equation for ZFS proposed by Neese [#ref7]_ is used. 

``ANALYSIS|FULLANALYSIS``
   ANALYSIS: Neese has presented some interesting analyses of ZFS [#ref7]_. If the ANALYSIS keyword is invoked then the contributions to the ZFS is divided into terms from alpha-beta, alpha-alpha, beta-beta and beta-alpha one-electron excitations.  FULLANALYSIS: The output requested by the ANALYSIS keyword is further extended to analyze each of the alpha-beta, alpha-alpha, beta-beta and beta-alpha  contributions in terms of the individual  one-electron excitations. 

.. only:: html

  .. rubric:: References

.. [#ref1] G.\  Schreckenbach and T. Ziegler, *Calculation of the G-tensor of electron paramagnetic resonance spectroscopy using Gauge-Including Atomic Orbitals and Density Functional Theory*, `Journal of Physical Chemistry A 101, 3388 (1997) <https://doi.org/10.1021/jp963060t>`__ 

.. [#ref2] S.\  Patchkovskii and T. Ziegler, *Calculation of the EPR g-Tensors of High-Spin Radicals with Density Functional Theory*, `Journal of Physical Chemistry A 105, 5490 (2001) <https://doi.org/10.1021/jp010457a>`__ 

.. [#ref3] E.\  van Lenthe, A. van der Avoird and P.E.S. Wormer, *Density functional calculations of molecular hyperfine interactions in the zero order regular approximation for relativistic effects*, `Journal of Chemical Physics 108, 4783 (1998) <https://doi.org/10.1063/1.475889>`__ 

.. [#ref4] J.\  Autschbach, S. Patchkovskii, and B. Pritchard, *Calculation of Hyperfine Tensors and Paramagnetic NMR Shifts Using the Relativistic Zeroth-Order Regular Approximation and Density Functional Theory*, `Journal of Chemical Theory and Computation 7, 2175 (2011) <https://doi.org/10.1021/ct200143w>`__ 

.. [#ref5] J.\  Autschbach and B. Pritchard, *Calculation of molecular g-tensors using the zeroth-order regular approximation and density functional theory: expectation value versus linear response approaches*, `Theoretical Chemistry Accounts 129, 453 (2011) <https://doi.org/10.1007/s00214-010-0880-x>`__ 

.. [#ref6] M.R. Pederson, S.N. Khanna, *Magnetic anisotropy barrier for spin tunneling in* Mn\ :sub:`12` O\ :sub:`12` *molecules*, `Physical Review B 60, 9566 (1999) <https://doi.org/10.1103/PhysRevB.60.9566>`__ 

.. [#ref7] F.\  Neese, *Calculation of the zero-field splitting tensor on the basis of hybrid density functional and Hartree-Fock theory*, `Journal of Chemical Physics 127, 164112 (2007) <https://doi.org/10.1063/1.2772857>`__ 

.. [#ref8] S.\  Patchkovskii and G. Schreckenbach in Calculation of NMR and EPR parameters, ISBN13: 9783527307791, M. Kaupp, M. Bühl, V.G. Malkin, Editors, (Wiley, Weinheim, 2004). 

.. [#ref9] S.\  Patchkovskii, R.S. Strong, C.J. Pickard and S. Un, *Gauge invariance of the spin-other-orbit contribution to the g-tensors of electron paramagnetic resonance*, `Journal of Chemical Physics 122, 214101 (2005) <https://doi.org/10.1063/1.1917840>`__ 

.. [#ref10] E.\  van Lenthe, A. van der Avoird and P.E.S. Wormer, *Density functional calculations of molecular g-tensors in the zero order regular approximation for relativistic effects*, `Journal of Chemical Physics 107, 2488 (1997) <https://doi.org/10.1063/1.474590>`__ 

.. [#ref11] C.\  van Wüllen, *Magnetic anisotropy from density functional calculations. Comparison of different approaches:* Mn\ :sub:`12` O\ :sub:`12` *acetate as a test case*, `Journal of Chemical Physics 130, 194109 (2009) <https://doi.org/10.1063/1.3134430>`__ 

.. [#ref12] S.\  Schmitt, P. Jost, C. van Wüllen, *Zero-field splittings from density functional calculations: Analysis and improvement of known methods*, `Journal of Chemical Physics 134, 194113 (2011) <https://doi.org/10.1063/1.3590362>`__ 
