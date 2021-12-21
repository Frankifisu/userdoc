
Introduction
************

In AMS2020 is ADF is only accessible through the AMS driver program. 
ADF (Amsterdam Density Functional) is an AMS engine for calculations on atoms and molecules (in gas phase or solution). It can be used for the study of such diverse fields as molecular spectroscopy, organic and inorganic chemistry, crystallography and pharmacochemistry.  The AMS engine BAND is available for the study of periodic systems: crystals, surfaces, and polymers. The separate COSMO-RS program is used for calculating thermodynamic properties of (mixed) fluids. 

The underlying theory is the Kohn-Sham approach to Density-Functional Theory (DFT). This implies a one-electron picture of the many-electron systems but yields in principle the exact electron density (and related properties) and the total energy. 

If ADF is a new for you we recommend that you carefully read the section :ref:`remarks_and_terminology`, which presents a discussion of a few ADF-typical aspects and terminology. This will help you to understand and appreciate the output of an ADF calculation. 

ADF has been developed since the early 1970s (at that time called HFS, later AMOL, see also refs. [#ref1]_ [#ref2]_ [#ref3]_, mainly by the two theoretical chemistry groups of, respectively, the Vrije Universiteit in Amsterdam ( `http://www.chem.vu.nl/en/research/division-theoretical-chemistry/index.asp <http://www.chem.vu.nl/en/research/division-theoretical-chemistry/index.asp>`__) and the University of Calgary, Canada. Other researchers have also contributed. As a major research tool of these academic development groups, ADF is in continuous development and retains a firm basis in the academic world. 

Maintenance and distribution of the commercial (export) version of the program is done by Software for Chemistry \& Materials B.V. (SCM) ( `http://www.scm.com <http://www.scm.com>`__), a company based in Amsterdam, formally split off from the theoretical chemistry group in Amsterdam but practically still very much a part of it. Documentation such as User manuals, Installation instructions, Examples, Theoretical documents can be found at the SCM web site. 

Publications based on research with ADF should include appropriate references to the program. We recommend that references are made both to the program itself and to publications related to its development and structure. See the :ref:`Required Citations <Required Citations>`. 

The installation of the  Amsterdam Modeling Suite (AMS) program package is explained in the `Installation manual <../../Installation/index.html>`__. This User's Guide describes how to use the program, how input is structured, what files are produced, and so on. Some special applications of ADF are described in the :ref:`Examples <examples>`. 

Where references are made to the operating system (OS) and to the file system on your computer the terminology of UNIX type OSs is used.

The AMS package is in continuous development to extend its functionality and applicability, to increase its efficiency and user-friendliness, and of course to correct errors. We appreciate comments and suggestions for improvement of the software and the documentation. 

ADF is an AMS Engine
====================

The most important change in AMS2020 is that ADF is only accessible via the AMS driver program.
We recommend you to first read the `General section of the AMS Manual <../../AMS/General.html>`__
More details this can be found in the section :ref:`AMSification of ADF<AMSIFICATION>`


Functionality
=============

+ Computation of any electronic configuration

+ Excitation energies, oscillator strengths, transition dipole moments, (hyper)polarizabilities, Van der Waals dispersion coefficients, CD spectra, ORD, MCD, VCD, magnetizabilities, Verdet constants, using Time-Dependent Density Functional Theory (TDDFT)

+ ESR (EPR) g-tensors, A-tensors, NQCCs

+ NMR chemical shifts and spin-spin coupling constants

+ Mössbauer spectroscopy

+ Transport properties: charge transfer integrals, NEGF

+ Various other molecular properties

+ Treatment of large systems and environment by the QM/MM (Quantum Mechanics / Molecular Mechanics) hybrid approach.



Applicability
=============

All elements of the periodic table can be used (Z = 1-120). For each of the elements, basis sets of different sizes are available, ranging from minimal to high quality. Special basis sets are provided for relativistic calculations within the ZORA approach and for response calculations that require additional diffuse basis functions. 


Model Hamiltonian
=================

+ A choice of Density Functionals, both for the Local Density Approximation (LDA), for the Generalized Gradient Approximation (GGA), for (range-separated) hybrid functionals (not for all properties available), and for meta-GGA functionals (not for all properties available) are available.

+ Spin: restricted or unrestricted

+ Relativistic effects: scalar approximation and spin-orbit (double-group symmetry), using the (now recommended) ZORA or the (previously used) Pauli formalism, X2C

+ Environment: Solvent Effects, Homogeneous Electric Field, Point Charges (Madelung Fields), QM/MM method, FDE

+ Constrained Density Functional Theory


Analysis
========

+ Decomposition of the bond energy in 'chemical' components (steric interaction, Pauli repulsion, orbital interactions...)

+ Natural orbitals for chemical valence (ETS-NOCV)

+ Representation of data (Molecular Orbital coefficients, Mulliken Populations) in terms of the constituent chemical fragments in the molecule, along with the conventional representation in elementary basis functions

+ Atomic charge determination by Hirshfeld analysis and by Voronoi analysis, multipole derived charges, along with the classical Mulliken populations, and Mayer bond orders

+ QTAIM analysis based on local, atomic and non-local descriptors for bonding description.

+ Conceptual DFT descriptors including global, atomic, non-local ones and a detailed analysis of the dual descriptor’s domains (predominantly electrophilic or nucleophilic regions).

+ Bond energy decomposition based on the interacting quantum atoms (IQA) approach and using QTAIM real-space partition. Any atom-atom interaction can be evaluated and decomposed into electrostatic (ionic) and exchange (covalent) contributions.

+ Localized molecular orbitals


Technical
=========

+ The implementation is based upon a highly optimized numerical integration scheme for the evaluation of matrix elements of the Fock operator, property integrals involving the charge density, etc. The code has been vectorized and parallelized.

+ Basis functions are Slater-Type Orbitals (STOs). A database is available with several basis sets for each atom in the periodic table of elements.

+ The Coulomb potential is evaluated via an accurate fitting of the charge density.

+ A frozen core facility is provided for an efficient treatment of the inner atomic shells.

+ Extensive use is made of point group symmetry. Most of the commonly encountered symmetry groups are available.

+ Linear scaling techniques are used to speed up calculations on large molecules

.. _FRAGMENTS: 
.. index:: fragments 

Fragments
=========

ADF has a fragment oriented approach: the poly-atomic system to be computed is conceptually built up from fragments, the molecular one-electron orbitals are calculated as linear combinations of fragment orbitals, and final analyzes of e.g. the bonding energy are in terms of fragment properties. The fragments may be single atoms or larger moieties. 

When you compute a system in terms of its constituent fragments, these fragments must have been computed before and their properties must be passed on to the current calculation. This is done by attaching *fragment files*, which contain the necessary information. A fragment file is simply the standard result file of an ADF calculation on that fragment. 

When using Basic Atoms as fragments, you do not need to create the fragment files yourself; ADF will create the required fragment files automatically. We therefore recommend this feature for starting ADF users. 

.. index:: basic atoms 


Basic atoms
-----------

Obviously there must be a set of fundamental fragments that are not defined in terms of smaller fragments. Therefore ADF has two modes of execution: the normal mode, using fragments, and the create mode, in which a fundamental fragment is generated. Such a fundamental fragment *must* be a single atom, spherically symmetric and spin-restricted (i.e. spin-:math:`\alpha` and spin-:math:`\beta` orbitals are spatially identical, they are equally occupied, and fractional occupations are applied, if necessary, to distribute the electrons equally over symmetry-degenerate states). Such a fundamental fragment is denoted a *basic atom*. The basic atoms are the smallest building blocks from which any 'real' calculations are started. 

One should realize that the basic atoms are artificial objects that are convenient in the computational approach but that do not necessarily represent real atoms very well (in fact, usually not at all). The bonding energy of a molecule with respect to basic atoms, for instance, should be corrected for this discrepancy in order to get a decent comparison against experimental data. See ref. [#ref4]_ for a discussion and for examples of applicable values. 

A basic atom is computed in the conventional way. The one-electron orbitals are determined as linear combinations of basis functions; the frozen core approximation may be applied for the inner atomic states; a particular type of density functional can be chosen, et cetera. You may have, for instance, different basic Copper atoms by using different basis sets, by choosing different levels of frozen core approximations, or by applying different density functionals. 


Automatic mode
--------------

If you are using 'Basic Atom' fragments only, you do not need to prepare the corresponding fragment files yourself; ADF will generate all the required fragment files for you. This makes your job scripts and ADF inputs simpler, it ensures that consistent options for the create runs and molecular runs are used.


Slater-type basis sets
======================

ADF uses Slater-Type Orbitals (STO's) as basis functions. Slaters can display the correct nuclear cusp and asymptotic decay.

.. math::
   
   f(\mathbf{r}) = Y_{lm} r^n e^{-\zeta r}


The center of the function is at a nucleus, the  :math:`Y_{lm}` are spherical harmonics, and the exponential factor :math:`\zeta` (zeta) determines the long-range decay of the function.  

ADF comes with a database of thoroughly tested basis set files, ranging in quality from single-zeta to quadruple-zeta basis sets with various diffuse and polarization functions. All-electron and frozen-core basis sets are available for all elements, including lanthanides and actinides. The frozen-core approximation can be used to considerably reduce the computation time for systems with heavy nuclei, in a controlled manner. 

.. only:: html

  .. rubric:: References

.. [#ref1] E.J. Baerends, D.E. Ellis and P. Ros, *Self-consistent molecular Hartree-Fock-Slater calculations I. The computational procedure*, `Chemical Physics 2, 41 (1973) <https://doi.org/10.1016/0301-0104(73)80059-X>`__ 

.. [#ref2] E.J. Baerends and P. Ros, *Evaluation of the LCAO Hartree-Fock-Slater method: Applications to transition-metal complexes*, `International Journal of Quantum Chemistry 14, S12, 169 (1978) <https://doi.org/10.1002/qua.560140814>`__ 

.. [#ref3] G.\  te Velde, F.M. Bickelhaupt, E.J. Baerends, C. Fonseca Guerra, S.J.A. van Gisbergen, J.G. Snijders, T. Ziegler, *Chemistry with ADF*, `Journal of Computational Chemistry 22, 931 (2001) <https://doi.org/10.1002/jcc.1056>`__ 

.. [#ref4] E.J. Baerends, V. Branchadell and M. Sodupe, *Atomic reference-energies for density functional calculations*, `Chemical Physics Letters 265,481 (1997) <https://doi.org/10.1016/S0009-2614(96)01449-2>`__ 
