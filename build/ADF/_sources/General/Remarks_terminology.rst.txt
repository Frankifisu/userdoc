.. _remarks_and_terminology:

Technical remarks, Terminology
******************************

A few words about ADF as regards its technical setup and the names and abbreviations used in this manual. References to these will be made in the discussion of output and print switches. 


Density functional theory
=========================

The underlying theory of the ADF engine is the Kohn-Sham approach to the Density-Functional Theory (DFT). Kohn-Sham DFT is an important first-principles computational method to predict chemical properties accurately and to analyze and interpret these in convenient and simple chemical terms. 

The reasons for its popularity and success are easy to understand. In the first place, the DFT approach is in principle exact. In particular, the Kohn-Sham method implies a one-electron picture of the many-electron systems but yields in principle the exact electron density (and related properties) and the total energy. The exact exchange-correlation (XC) functional is unknown, but the currently available XC functionals provide in most cases already a 'chemical' accuracy of a few kcal/mol for binding energies. Moreover, the quest for more accurate ones based on a more detailed understanding of their essential properties is continuing. 

In the past two decades, computational chemistry has evolved from a curiosity of theoreticians into a mainstream tool used by all types of chemists, physicists and engineers who have an interest in research and development. In that time Density Functional Theory has become the dominant method for modeling chemistry at the molecular level. 

In the second place, it preserves at all levels of approximation the appealing one-electron molecular orbital (MO) view on chemical reactions and properties. The computed orbitals are suitable for the typical MO-theoretical analyses and interpretations. The KS method effectively incorporates all correlation effects. 

In the third place, it is a relatively efficient computational method, and its fundamental scaling properties do not deteriorate when methodological precision is increased, in particular, when a more accurate XC functional is applied. Recent research paves the way to implementations that scale only linearly with the system size. This brings within reach the treatment by fundamental quantum chemical methods of systems with hundreds, maybe even thousands of atoms. 

DFT gives superior accuracy to Hartree-Fock theory and semi-empirical approaches, and it is well suited for molecules containing metal atoms. In contrast to conventional ab initio methods (MP2, CI, CC), it enables accurate treatment of systems with several hundreds of atoms (or several thousands with QM/MM). 

Text is mostly taken from: *Chemistry with ADF*, G. te Velde, F.M. Bickelhaupt, E.J. Baerends, C. Fonseca Guerra, S.J.A. van Gisbergen, J.G. Snijders, T. Ziegler, , `Journal of Computational Chemistry 22, 931 (2001) <https://doi.org/10.1002/jcc.1056>`__ 


The Kohn-Sham MO model
======================

The basic postulate in Kohn-Sham DFT is that we can apply a one-electron formulation to the system of N interacting electrons by introducing a suitable local potential :math:`V_\text{XC} (r)`, in addition to any external potentials :math:`V_\text{ext} (r)` and the Coulomb potential of the electron cloud :math:`V_\text{C} (r)`, and solving: 

.. math::

  [T +  V_\text{ext} (r) + V_\text{C} (r) + V_\text{XC} (r)]  \phi_i (r) = \epsilon_i \phi_i (r) 

Here T is the kinetic energy operator. The potential :math:`V_\text{XC} (r)`  is the functional derivative with respect to the density :math:`\rho` of :math:`E_\text{XC}` [:math:`\rho`], the exchange-correlation energy functional. The one-electron molecular orbitals (MOs) :math:`\phi`\ :sub:`i`  with corresponding orbital energies :math:`\epsilon_i`  define the exact electronic charge density and give, in principle, access to all properties because these are expressible as functional of the density, in particular the energy. Moreover, they provide an intuitively appealing view of the system as being built from independent-electron orbitals with all ensuing interpretations. The exact form of the exact energy density :math:`E_\text{XC} (r)`, representing and incorporating all exchange and correlation (XC) effects is unknown. From general principles one can formulate conditions on what :math:`E_\text{XC} (r)` should look like, and several, more and more advanced expressions have been advocated for it in the literature. Their application to real systems has been impressively successful, and it seems likely that a further increase of accuracy is a matter of time. 

.. index:: basis functions 
.. index:: STO 
.. _BASIS: 

Basis functions and orbitals
============================

Let us make a clear distinction between (basis) *functions* and *orbitals*, even where these phrases are sometimes mixed up in the traditional terminology. Orbitals are always specific combinations of the basis functions. Orbitals are related to the computed eigenfunctions of some Fock operator or Hamiltonian occurring in the run or in a related preceding calculation. Functions are merely the elementary mathematical entities in which the orbitals are expressed. A Slater Type Orbital (STO), for instance is a function, not an orbital. 

The physical meaning of one-electron orbitals in DFT has often been questioned. We believe that they are useful quantities for interpretation, just like the HF orbitals. For a recent discussion see ref. [#ref1]_. 

**See also**

* ADF-GUI tutorial: `basis set effects <../../Tutorials/WorkflowsAndAutomation/GeneratingABatchOfJobs.html>`_


.. index:: Cartesian functions 
.. index:: BAS 


Cartesian function sets, spurious components
--------------------------------------------

ADF employs Slater-type exponential basis functions centered on the atoms. Such a function consists of an exponential part exp(-ar) and a polynomial pre-factor r\ :sup:`kr` x\ :sup:`kx` y\ :sup:`ky` z\ :sup:`kz` . A function *set* is characterized by its radial behavior (the exponential part and the power of r, kr) and by its angular momentum quantum number *l*. The functions in such a set consist of all possible combinations x\ :sup:`kx` y\ :sup:`ky` z\ :sup:`kz` , such that kx+ky+kz=l. These are denoted the *Cartesian* spherical harmonics. 

The Cartesian function sets are very suitable for computational manipulations, but they have a drawback. By inspection it is easily verified that a *d*-set consists of 6 Cartesian functions, while there can of course be only 5 true *d*-type functions among them: one (linear combination) of them is in fact an *s*-type function (x\ :sup:`2` +y\ :sup:`2` +z\ :sup:`2` ). Similarly, there are 10 *f*-type Cartesian functions, 3 of which are in fact *p*-functions. And so on. In ADF all such lower-*l* (combinations of) functions are projected out of the basis and not employed. As a consequence the basis set *size* in the sense of the number of degrees of freedom and hence the number of possible eigenfunctions of the Fock operator is smaller than the number of expansion coefficients that refer to the primitive (Cartesian) basis functions. 

The abbreviation BAS is used for references to the elementary Cartesian basis functions. 


.. _FROZEN_CORE: 
.. index:: frozen core approximation 


Frozen core: Core Orbitals and Core Functions
---------------------------------------------

To speed up the computation the innermost atomic shells are kept frozen. The frozen Core Orbitals (CO), which are solutions of a large-basis all-electron calculation on the isolated atom, are expressed in an auxiliary set of (Slater-type) basis functions cor-bas, distinct from the valence set. The core basis set and the COs expansion coefficients are stored in the basis set files. 

Orthogonality of the valence Molecular Orbitals (MO) to the COs is achieved with the help of so-called Core Functions (CF). These functions are included in the valence set but they are not additional degrees of freedom. Each of the normal valence functions is combined with a linear combination of all CFs in the molecule in such a way that the transformed function (cbas) is orthogonal to all frozen COs in the molecule. There are exactly as many CFs as COs so the orthogonality condition for all valence basis functions amounts to the solution of a linear system where the number of conditions equals the number of parameters. 

This aspect once more increases the discrepancy between the number of expansion coefficients of an MO and the number of MOs: the expansion coefficients in the most elementary bas representation run over all bas functions, including the CFs among them. At some places there may, alternatively, be expansions in the core-orthogonalized BAS functions, CBAS, where the CFs do not count anymore: they are included implicitly in the cbas functions. 


.. _SYMMETRY: 
.. index:: symmetry 
.. index:: irreducible representation 


Symmetry
--------

The Overlap and Fock matrices become block-diagonal by using symmetry-adapted combination of the (C)BAS functions, such that each such function transforms under the symmetry operators as one of the subspecies of the irreducible representations (irrep) of the symmetry group. Symmetry adapted functions are denoted (C)SBAS. 

For a given irrep and subspecies not all elementary basis functions can participate in the symmetry adapted combinations. For instance, for an atom in a reflection plane a basis function that is anti-symmetric with respect to the reflection cannot be part of any symmetric combination of functions. In particular for higher symmetries the number of BAS functions that are relevant for a subspecies may be considerably smaller than the total number of BAS functions. This is used to cut down expansion lengths, both as used internally in the computation and construction of the Fock matrix, and in printed output. The printed expansion coefficients (in the bas representation) refer only to the participating BAS functions. A defining list of them is printed at an early stage of the run for each of the subspecies. 


.. index:: orthonormal basis 


Orthonormal basis
-----------------

It is often computationally convenient to use an orthonormal basis. This is constructed from the CSBAS basis by a Lowdin orthogonalization procedure. The resulting symmetry-adapted orthonormal basis is denoted low. 

The MOs are computed by diagonalization of the Fock matrix in the LOW representation. The resulting eigenvectors are easily transformed back to any other representation whenever suitable, such as for instance to the primitive Cartesian bas representation (including the CFs). 


.. index:: fragment orbitals 
.. index:: SFO 


Fragments
---------

Except in Create mode, where a *basic atom* is constructed, the system is built up from fragments and the corresponding fragment files are attached to the run. The ADF engine reads from the files the fragment MOs and these are used as (compound) *basis functions* for the molecular calculation. The fragment MOs are called Fragment Orbitals (FO). 

FOs belong of course to one of the symmetry representations of the fragment, but not necessarily to a symmetry representation of the new molecule. The FOs are therefore combined into symmetry-adapted combinations, SFOs, to serve as a symmetry-adapted basis in the molecule. These combinations may involve one or more FOs from the same fragment and/or from different fragments. In the latter case the fragments must be symmetry related by one of the operators of the molecule. Symmetry related fragments must of course be identical, apart from their spatial location: they must be of the same fragment *type*. 

FOs are naturally orthogonal to the Core Orbitals of their own fragment, but not necessarily to COs of other fragments. By a suitable combination of the SFOs with all CFs in the molecule we obtain the core-orthogonalized symmetry-adapted CSFOs. 

The CSFOs can be transformed to an orthonormal basis by a Lowdin transformation. The resulting basis is called low, as above. 



Summary of functions and orbitals
---------------------------------

In Create mode the (conceptual) approach is: 

BAS → (core-orthogonalization) → CBAS → (symmetry) → CSBAS → (orthonormality) → LOW → (Fock diagonalization) → MO 

In Fragment mode: 

FO (=MO from fragment file) → (symmetry) → SFO → (core-orth.) → CSFO → (orthonormality) → LOW → (Fock diagonalization) → MO 



Acronyms
--------

``BAS``
   Elementary Cartesian basis functions, consisting of a radial part (exponential factor and power of r) and an angular part (Cartesian spherical harmonic). The complete BAS set contains spurious lower-*l* combinations; these combinations are projected out and not used in the calculation. The BAS set contains also Core Functions. 

``SBAS``
   Symmetry-adapted combination of BAS functions. 

``CF``
   Core Function, part of the bas set. The CFs do not represent degrees of freedom in the basis set but serve only to ensure orthogonalization of the valence space to all frozen Core Orbitals. 

``CBAS``
   Core-orthogonalized elementary basis functions: the true valence (not-CF) BAS functions transformed by adding a suitable combination of the CFs. The total number of CBAS + the total number of of CFs equals the total number of BAS. 

``CSBAS``
   Symmetry-adapted combination of cbas functions. 

``CO``
   Frozen Core Orbitals, expressed as linear combinations of an auxiliary corbas basis set. The corbas set plays no role in the further discussion. The corbas functions are *not* the CFs. 

   The number of COs equals the number of CFs. 

``LOW``
   Lowdin orthonormalized symmetry-adapted core-orthogonalized basis. In Create mode they are derived directly from the BAS functions, in Fragment mode from the Fragment Orbitals, which are themselves of course expressible in the BAS set. 

``FO``
   Fragment Orbital: the MO of a fragment calculation, now used as a *basis function* in the molecule of which the fragment is part. 

``SFO``
   Symmetry adapted combination of FOs. 

``CSFO``
   Core-orthogonalized SFO. 



.. index:: fit functions
.. _FIT:

Coulomb potential evaluation, density fitting
=============================================


Using Slater-type basis functions yields awkward multi-center integrals in the evaluation of the Coulomb potential. We therefore first need to find an approximate density-representation for which the Coulomb integral can be evaluated efficiently. This procedure is commonly referred to as density fitting. The default density fitting procedure in ADF is described in Ref. [#ref2]_. 

One of the most important properties of a molecule is its energy, or its bonding energy with respect to the constituent fragments. The approximate nature of the fitting procedure introduces two types of errors. The first is that, since the Coulomb potential is only approximated, the SCF solution itself, i.e. the set of self-consistent Molecular Orbitals and their energy eigenvalues may be slightly wrong, yielding an error in the charge density and hence in the energy. Since the energy is to first order stable with respect to changes in the mo coefficients this error in the energy can be assumed very small. The second type of error derives from the computation of the energy from the (self-consistent) charge density, via the Coulomb potential. Let 

.. math::

   \rho \equiv \rho_{exact} (r) = \rho_{fit} (r) + \delta (r)

and 

.. math::

   V_{fit} (r) = \int \rho_{fit} (r')/|r-r'| dr

For the Coulomb energy of the charge density we have 

.. math::

   2E_{Coul} & = \iint \rho(r) \rho(r')/|r-r'| dr dr' = \int \rho (r) V_{fit} (r) dr + \iint \rho(r) \delta(r)/|r-r'| dr dr' \\
             & = \int V_{fit} (r) (\rho(r)+\delta(r)) dr + \iint \delta(r) \delta(r')/|r-r'| dr dr'

from which we see that the fit error is corrected to first order (by adding the fit deficiency :math:`\delta(r)` to the exact charge density when integrating against the fit potential) and that only a second order term remains that cannot be evaluated, the last term in the right-hand-side of the last equation.

A fair impression of the fit quality and the importance of the second order error term is obtained by checking  

+ the size of the first order correction term :math:`\int V_{fit} (r) \delta(r) dr` and 
+ the norm of the deficiency function, :math:`\int \delta^2(r) dr` . 

Both are printed in standard output, at the end of the output of the SCF procedure computational report. They are usually very small, which gives some confidence that the second order fit error can be ignored. 



.. index:: bond energy analysis 
.. index:: energy decomposition analysis 
.. _BE_ANALYSIS: 

Three-step build-up of the bonding
==================================

The approach of ADF is based on fragments. This applies not only in the analysis at the end of the computation but also in the set-up of the ADF engine. The computation of the molecule from its constituent fragments takes place in three steps, and these are reflected in the analysis of bond energy components. 

First, the (free, unrelaxed) fragments are placed at their positions in the molecule. This implies an *electrostatic* interaction: for each fragment the Coulomb interaction of its undisturbed charge density with the fields of the other fragments. 

Next, the Pauli exclusion principle is applied. Even without considering self-consistency the one-electron orbitals of the combined fragments cannot represent a correct one-determinant wave function because the orbitals of different fragments are not orthogonal to one another. The ADF engine performs an orthonormalization of the occupied Fragment Orbitals to obtain an antisymmetrized product. This implies a change in the total molecular charge density from the sum-of-fragments to what is called the sum-of-*orthogonalized*-fragments. The corresponding (repulsive) energy term is evaluated separately and is called *Exchange* repulsion, or alternatively *Pauli* repulsion. The phrase *orthogonal(ized) fragments*, if you find it elsewhere in this manual or in the source code of ADF, refers to this aspect. The sum of Pauli repulsion and electrostatic interaction is called the *steric interaction*. 

The third phase is the relaxation to self-consistency, with of course the ensuing contributions to the bond energy. 


Transition State procedure
==========================

This phrase stands for an analysis method described in ref. [#ref4]_ and has no relation to transition states in chemical reactions. An extensive discussion of bond energy analysis by ADF is given in ref. [#ref5]_ [#ref6]_. 

The energy associated with a change in charge density, say the relaxation to self-consistency from the sum-of-orthogonal-fragments, can be computed by subtracting final and initial energies, each obtained from the corresponding charge density. For purposes of analysis the change in energy dE can be reformulated as 


.. math::

   dE = \int dr \left( \left(\rho_\text{final}(r) - \rho_\text{initial}(r) \right) \int_{\rho_\text{initial}}^{\rho_\text{final}} d\rho F[\rho (r)] \right) \quad (1.2.8)
   
F(:math:`\rho`) is the Fock operator belonging to the charge density :math:`\rho` 

By writing the density difference :math:`\rho`\ :sub:`final`  - :math:`\rho`\ :sub:`initial`  a summation over contributions from the different irreducible representations :math:`\Gamma` of the molecular symmetry group, an expression is obtained that lends itself for a decomposition of the bond energy into terms from the different symmetry representations: 

.. math::

   dE = \sum_\Gamma \int dr \left( \Delta \rho^\Gamma (r) \int_{\rho_\text{initial}}^{\rho_\text{final}} d\rho F[\rho (r)] \right) \quad (1.2.9)

   
The integral of the Fock operator over the charge density is now approximated by a weighted summation (in fact, a Simpson integration): 


.. math::

   \int_{\rho_\text{initial}}^{\rho_\text{final}} d\rho F[\rho (r)] \approx  \frac{1}{6} F[\rho_\text{initial}] + \frac{2}{3} F[\rho_\text{average}] + \frac{1}{6} F[\rho_\text{final}] \quad (1.2.10)

where

.. math::

   \rho_\text{average} = \frac{1}{2} (\rho_\text{initial} + \rho_\text{final}) \quad (1.2.11)
   
The term with the Fock operator due to the average charge density has given rise to the phrase *transition state*. To avoid confusion we will often refer to it as to the transition *field*. 

The approximate integral (1.2.10) involves two errors. The first, rather obvious, is the approximation of the exact integral in (1.2.9) by the weighted sum in (1.2.10). Except in pathological cases this approximation is highly accurate. 

The second error comes from the fact that the Coulomb and XC potentials in the Fock operator are computed from the *fit* density. This is only an approximation to the true density, while in the original bond-energy expression (energy due to the final density minus energy due to the initial density) no potentials occur and the *exact* charge density can be used. As mentioned before, these fit-related errors are usually small. For the XC potential the true density can be used if one includes the keyword EXACTDENSITY. 

All such errors in the total bonding energy are easily corrected by comparing the summation over the :math:`\Gamma`\ s with the correct value for the total bonding interaction term. The difference is simply added to the total bond energy, so no true error remains. We only have a (correction) term that can't be split in contributions from the distinct symmetry representations. In the printed bond energy analysis such small corrections are 'distributed' over the other terms by scaling the other terms such that their sum is the correct total value. 


.. only:: html

  .. rubric:: References

.. [#ref1] F.M. Bickelhaupt and E.J. Baerends, *Kohn-Sham DFT: Predicting and Understanding Chemistry*, in *Reviews in Computational Chemistry*, D.B. Boyd and K.B. Lipkowitz, Editors. 2000, Wiley-VCH: New York. p. 1-86. 

.. [#ref2] M.\  Franchini, P.H.T. Philipsen, E. van Lenthe, L. Visscher, *Accurate Coulomb Potentials for Periodic and Molecular Systems through Density Fitting*, `Journal of Chemical Theory and Computation 10, 1994 (2014) <https://doi.org/10.1021/ct500172n>`__ 

.. [#ref3] E.J. Baerends, D.E. Ellis and P. Ros, *Self-consistent molecular Hartree-Fock-Slater calculations I. The computational procedure*, `Chemical Physics 2, 41 (1973) <https://doi.org/10.1016/0301-0104(73)80059-X>`__ 

.. [#ref4] T.\  Ziegler and A. Rauk, *On the calculation of Bonding Energies by the Hartree Fock Slater method. I. The Transition State Method*, `Theoretica Chimica Acta 46, 1 (1977) <https://doi.org/10.1007/BF00551648>`__ 

.. [#ref5] P.J. van den Hoek, A.W. Kleyn and E.J. Baerends, *What is the origin of the repulsive wall in atom-atom potentials*, Comments Atomic and Molecular Physics 23, 93 (1989) 

.. [#ref6] E.J. Baerends, *Pauli repulsion effects in scattering from and catalysis by surface*, in *Cluster models for surface and bulk phenomena*, ISBN13: 9780306441028, G. Puccchiori, P.S. Bagus and F. Parmigiani, Editors. 1992, Springer: New-York. p. 189-207. 
