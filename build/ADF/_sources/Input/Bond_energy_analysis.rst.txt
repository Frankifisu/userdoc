
Bond energy analysis
********************

No special input keys are required.
However, if one has open shell fragments, see key UNRESTRICTEDFRAGMENTS or key FRAGOCCUPATIONS.


.. index:: bond energy analysis

.. index:: energy decomposition analysis

ADF calculates various chemically meaningful terms that add up to the bond energy, with an adaptation of Morokuma's bond energy decomposition to the Kohn-Sham MO method. The individual terms are chemically intuitive quantities such as electrostatic energy, Pauli repulsion, and orbital interactions. The latter are symmetry decomposed according to the Ziegler transition state method. For a discussion of bonding energy decompositions and applications see e.g. ref. [#ref1]_ [#ref2]_ [#ref3]_ [#ref14]_ [#ref15]_ [#ref16]_ [#ref17]_ [#ref18]_ [#ref19]_ [#ref20]_. For a discussion of forming electron pair bonding between open shell molecules see Ref. [#ref4]_.
For an ETS-NOCV analysis of the orbital interaction, see Ref. [#ref5]_.

In ADF2012 the calculation of the Pauli repulsion for metaGGA's and metahybrids is implemented. Note that for hybrids this was already implemented before in case of closed shell fragments. In ADF2012 for hybrids, metaGGA's, and metahybrids the calculation of the Pauli repulsion is also implemented if one is simulating an unrestricted fragment with the key FRAGOCCUPATIONS. 

In ADF2012 for hybrids the exact exchange contribution to the Pauli term is isolated and the contributions to the orbital term are divided among orbital symmetries. 


Bond energy details
===================

In the framework of Kohn-Sham MO theory and in conjunction with the fragment approach, one can decompose the bond energy between the fragments of a molecular system - say, a base and a substrate for E2 elimination - into contributions associated with the various orbital and electrostatic interactions. In ADF, we follow a Morokuma-type energy decomposition method. The overall bond energy :math:`\Delta E` is divided into two major components. In the first place, the preparation energy :math:`\Delta E_\text{prep}` corresponding to the amount of energy required to deform the separated fragments, A and B say, from their equilibrium structure to the geometry they acquire in the overall molecule ( :math:`\Delta E_\text{prep,geo}` ), and to excite them to their valence electronic configuration ( :math:`\Delta E_\text{prep el}` ). In the second place, the interaction energy :math:`\Delta E_\text{int}` between the prepared fragments. 

.. math::

   \Delta E = \Delta E_\text{prep} + \Delta E_\text{int} = \Delta E_\text{prep,geo} + \Delta E_\text{prep,el} + \Delta E_\text{int}

In the following step, the interaction energy :math:`\Delta E_\text{int}` is further decomposed into three physically meaningful terms, which are printed in the ADF output file. 


.. math::

   \Delta E_\text{int} = \Delta V_\text{elst} + \Delta E_\text{Pauli} + \Delta E_\text{oi} = \Delta E^0 + \Delta E_\text{oi}

The term :math:`\Delta V_\text{elst}`  corresponds to the classical electrostatic interaction between the unperturbed charge distributions of the prepared fragments as they are brought together at their final positions, giving rise to an overall density that is simply a superposition of fragment densities :math:`\rho_A + \rho_B`. (Note that we use the convention that energy terms containing potential energy only, kinetic energy only, or both kinetic and potential energy are indicated by V, T, and E, respectively.) For neutral fragments, :math:`\Delta V_\text{elst}` is usually attractive. The Pauli repulsion :math:`\Delta E_\text{Pauli}`  arises as the energy change associated with going from :math:`\rho_A + \rho_B` the wave function :math:`\Psi^0 = NA[\Psi_A \Psi_B]` that properly obeys the Pauli principle through explicit antisymmetrization (*A* operator) and renormalization (*N* constant) of the product of fragment wave functions. It comprises the destabilizing interactions between occupied orbitals, and is responsible for any steric repulsion. In case of neutral fragments, it can be useful to combine :math:`\Delta V_\text{elst}`  and :math:`\Delta E_\text{Pauli}`  in a term :math:`\Delta E_0` which, in the past, has been conceived as the steric interaction. However, we prefer to reserve the designation steric interaction or repulsion for :math:`\Delta E_\text{Pauli}`  because that is, as already mentioned, the only source of net repulsive interactions between molecular fragments. Finally, the wavefunction is allowed to relax from :math:`\Psi^0` to the fully converged wave function :math:`\Psi`. The associated orbital interaction energy :math:`\Delta E_\text{oi}` accounts for electron pair bonding, charge transfer (e.g., HOMO-LUMO interactions) and polarization (empty/occupied orbital mixing on one fragment due to the presence of another fragment). In a symmetric molecule this can be further decomposed into the contributions from the distinct irreducible representations :math:`\Gamma` of the interacting system using the extended transition state method. In systems with a clear :math:`\sigma`/:math:`\pi` separation, this symmetry partitioning proves to be very informative. 


.. math::

   \Delta E_\text{oi} = \sum_\Gamma  \Delta E_{\text{oi},\Gamma} 

An alternative, which can also be used in asymmetric molecules, is the ETS-NOCV analysis, which decomposes the bonding interactions in the context of natural orbitals for chemical valence, see Refs [#ref5]_ [#ref7]_ [#ref8]_.

The pure orbital interaction effect of forming electron pair bonding between open shell molecules can approximately be calculated with a bond energy analysis in which all virtual orbitals are removed from the fragments, see Ref. [#ref4]_.

An extensive discussion of the physical meaning of all the terms in the energy decomposition is given in F.M. Bickelhaupt and E.J. Baerends, *Kohn-Sham Density Functional Theory: Predicting and Understanding Chemistry*, In: Rev. Comput. Chem.; Lipkowitz, K. B. and Boyd, D. B., Eds.; Wiley-VCH: New York, 2000, Vol. 15, 1-86. 

Text is mostly taken from: *Chemistry with ADF*, G. te Velde, F.M. Bickelhaupt, E.J. Baerends, C. Fonseca Guerra, S.J.A. van Gisbergen, J.G. Snijders, T. Ziegler `Journal of Computational Chemistry 22, 931 (2001) <https://doi.org/10.1002/jcc.1056>`__.


.. index:: total energy 
.. _totalenergy: 


Notes on double-hybrid functionals and MP2
==========================================

Since ADF2019.3, double-hybrid density functionals have been implemented in ADF. These include contributions from virtual orbitals from a :ref:`MP2 calculation <keyscheme MBPT>`. The evaluation of MP2 energies requires orbital energies as input, which, however, are not available for orthogonal fragments. Thus, whenever a double-hybrid calculation is carried out, the Bonding energy with respect to the individual fragments is calculated and printed out. However, all terms which rely on the orthogonal fragment density (e.g. Pauli repulsion terms) do not include the MP2 part of the double-hybrid.

Total energy evaluation
=======================

ADF normally does not calculate the total energy of a system (the energy wrt bare nuclei and free electrons). However, ADF calculates the energy of the system with respect to fragment energies. By default, these fragments are the spherical spin-restricted neutral atoms, but one can also use larger fragments. For this reason total energies from other programs could not be compared to ADF directly. Note, however, that only energy difference comparisons are meaningful. These are the only energies that play a role in chemistry of course, and for this one does not need total energies.  

If you really want to calculate the total energies, there are two options in ADF 

**Total energy by adding the binding energy of the atoms**

There is a work-around to calculate the total energy of a system: calculate the total energies of the atomic fragments and add them to the bonding energy. Because total energy of an atom is, by definition, the energy difference between the atom and the (nucleus+free electrons) system one can calculate it by calculating a single atom with the charge equal to the number of electrons. 'Bonding energy' of such an 'atom' will then be equal to negative of the total energy of the atomic fragment. Care should be taken to apply this procedure to frozen-core fragments. In this case, it only makes sense to remove the valence electrons and leave the frozen core. 

**TOTALENERGY keyword**

The total energies have not been tested extensively and should therefore be used with caution. In addition to bond energies it is now possible to compute total energies with ADF by including the keyword TOTALENERGY in the input. This work is in progress. 

.. _keyscheme TOTALENERGY: 


::

   TOTALENERGY

The total energy will be computed for the chosen XC functional (LDA, GGA, hybrid functionals, or Hartree-Fock). MetaGGA functionals, (ZORA) scalar relativistic and relativistic spin-orbit calculations, electric fields and QM/MM are not supported yet. 

In particular the requirements to the integration accuracy are somewhat higher than for bond energies. It is recommended to use an integration grid (BeckeGrid) of quality "Good". If in doubt, a convergence test with respect to the integration accuracy is recommended. 


.. index:: interacting quantum atoms
.. index:: IQA
.. _IQA: 

Interacting Quantum Atoms (IQA)
===============================

.. Note ::

   This part of the code has been completely rewritten and it is now parallelized. However, **symmetry is still not allowed** so please use the NOSYM option. Besides, it is restricted to **closed-shell systems** (and will be extended to open-shells very soon). Relativistic calculations are not recommended. More precisely, in case of relativistic calculations components based on the electron density will be correct (such as Coulomb interactions) but those depending explicitely on the wavefunction will be wrong.

The interacting quantum atoms approach (IQA) has been developed by Angel Martín Pendás and coworkers in the framework of real-space partitions of the molecular space [#ref10]_ [#ref11]_ [#ref21]_. This can be seen as an alternative to the Bickelhaupt-Baerends' bond energy decomposition scheme but for the **total energy** of the molecular system. In this new version, a full IQA decomposition is now proposed as the default procedure, including both intra-atomic and inter-atomic interactions (see below). 

In a wavefunction context, the IQA QTAIM partition of the molecular energy leads exactly to:

:math:`E=\sum _A\left(T^A+E_{Ne}^{AA}+E_{eeCl}^{AA}+E_{eeXC}^{AA}\right)+\frac 1 2\sum _{A{\neq}B}\left(E_{NN}^{AB}+E_{eN}^{AB}+E_{Ne}^{AB}+E_{eeCl}^{AB}+E_{eeXC}^{AB}\right)`

The first four terms of the right-hand side in the equation above correspond to intra-atomic (also coined 'self') terms for each atom 'A': the atomic kinetic energy (T\ :sup:`A`), the interaction energy between the nucleus and the electron density inside basin A :math:`(E_{Ne}^{AA})`, and the repulsion energy between electrons in A, decomposed into classical electrostatic (:math:`E_{eeCl}^{AA}`) and exchange-correlation contributions  (:math:`E_{eeXC}^{AA}`).

The last sum in the equation corresponds to the interactions between each atom pair 'AB' (bonded or not bonded by a bond path): the repulsion energy between nuclei in A and B (:math:`E_{NN}^{AB}`), the attraction of the electrons in A by the nucleus in B (:math:`E_{eN}^{AB}`) the attraction of the electrons in B by the nucleus in A (:math:`E_{Ne}^{AB}`), and the repulsion energy between electrons in A with those in B, which can be split into a classical electrostatic contribution (:math:`E_{eeCl}^{AB}`) and an exchange-correlation one (:math:`E_{eeXC}^{AB}`).

Within a Kohn-Sham DFT framework, the implementation of this partition is not straightforward (see ref. [#ref12]_ for more details). In ADF2018 a partial energy decomposition limited to **interatomic interactions** was proposed. For any atom-atom pair 'AB', we evaluate:

:math:`E_{inter}^{AB}=E_{NN}^{AB}+E_{eN}^{AB}\left[\rho \right]+E_{Ne}^{AB}\left[\rho \right]+E_{eeCl}^{AB}\left[\rho \right]+E_{eeX}^{AB}\left[\left\{\psi _i^{KS}\right\}\right]`

where :math:`E_{eeX}^{AB}\left[\left\{\psi _i^{KS}\right\}\right]` corresponds to the full exact exchange ('HF-like') interacting energy between the two atoms. Tognetti and Joubert have shown that despite underlying approximations, this expression can be safely used at least for semi-quantitative purposes [#ref13]_.

Three energetic terms are printed for each atom pair. The first one corresponds to the *total* interaction energy between the two atoms ( :math:`E_{inter}^{AB}`). This energy is then split into two contributions: the 'covalent part' corresponds to the exchange energy between the two atomic basins ( :math:`E_{eeX}^{AB}\left[\left\{\psi _i^{KS}\right\}\right]`), while the 'ionic one' is the sum of all remaining electrostatic contributions ( :math:`E_{NN}^{AB}+E_{eN}^{AB}+E_{Ne}^{AB}\left[\rho \right]+E_{eeCl}^{AB}\left[\rho \right]`).

As already mentioned, a full IQA decomposition is now automatically performed, including intra-atomic terms (a detailed description of the implementation will be soon available).
Choosing the **verbose mode** allows to give more details about the energy decomposition (all terms are detailed in this case and described in the output itself).

You can activate these atom-atom interactions via the IQA input block:

.. scmautodoc:: adf IQA Enabled Print AtomsToDo


.. only:: html

  .. rubric:: References


.. [#ref1] T.\  Ziegler and A. Rauk, *On the calculation of Bonding Energies by the Hartree Fock Slater method. I. The Transition State Method*, `Theoretica Chimica Acta 46, 1 (1977) <https://doi.org/10.1007/BF00551648>`__ 

.. [#ref2] T.\  Ziegler and A. Rauk, *A theoretical study of the ethylene-metal bond in complexes between copper(1+), silver(1+), gold(1+), platinum(0) or platinum(2+) and ethylene, based on the Hartree-Fock-Slater transition-state method*, `Inorganic Chemistry 18, 1558 (1979) <https://doi.org/10.1021/ic50196a034>`__ 

.. [#ref3] F.M. Bickelhaupt, N.M. Nibbering, E.M. van Wezenbeek and E.J. Baerends, *The Central Bond in the Three CN* Dimers NC_CN, CN-CN, and CN-NC: Electron Pair Bonding and Pauli Repulsion Effects*, `Journal of Physical Chemistry 96, 4864 (1992) <https://doi.org/10.1021/j100191a027>`__ 

.. [#ref4] F.M. Bickelhaupt, M. Solà, C. Fonseca Guerra, *Highly polar bonds and the meaning of covalency and ionicity -- structure and bonding of alkali metal hydride oligomers*, `Faraday Discussions 135, 451 (2007) <https://doi.org/10.1039/B606093E>`__ 

.. [#ref5] M.\  Mitoraj, A. Michalak and T. Ziegler, *A Combined Charge and Energy Decomposition Scheme for Bond Analysis*, `Journal of Chemical Theory and Computation 5, 962 (2009) <https://doi.org/10.1021/ct800503d>`__ 

.. [#ref7] M.\  Mitoraj, A. Michalak and T. Ziegler, *On the Nature of the Agostic Bond between Metal Centers and Beta-Hydrogen Atoms in Alkyl Complexes. An Analysis Based on the Extended Transition State Method and the Natural Orbitals for Chemical Valence Scheme (ETS-NOCV)*, `Organometallics 28, 3727 (2009) <https://doi.org/10.1021/om900203m>`__ 

.. [#ref8] M.\  Mitoraj, and A. Michalak, *Natural orbitals for chemical valence as descriptors of chemical bonding in transition metal complexes*, `Journal of Molecular Modeling 13, 347 (2007) <https://doi.org/10.1007/s00894-006-0149-4>`__ 

.. [#ref10] M.A. Blanco, A.M. Pendás and E. Francisco, *Interacting Quantum Atoms: a correlated energy decomposition scheme based on the quantum theory of atoms in molecules*, `Journal of Chemical Theory and Computation 1, 1096 (2005) <https://doi.org/10.1021/ct0501093>`__.

.. [#ref11] A.M. Pendás, MA. Blanco and E. Francisco, *A molecular energy decomposition scheme for atoms in molecules*, `Journal of Chemical Theory and Computation 2, 90 (2006) <https://doi.org/10.1021/ct0502209>`__.

.. [#ref12] V.\  Tognetti and L. Joubert, *On Atoms-in-Molecules Energies from Kohn–Sham calculations*, `ChemPhysChem 18, 2675 (2017) <https://doi.org/10.1002/cphc.201700637>`__.

.. [#ref13] V.\  Tognetti and L. Joubert, *On the physical role of exchange in the formation of an intramolecular bond path between two electronegative atoms*, `Journal of Chemical Physics 138, 024102 (2013) <https://doi.org/10.1063/1.4770495>`__.

.. [#ref14]  K.\  Kitaura and K. Morokuma, *A new energy decomposition scheme for molecular interactions within the Hartree-Fock approximation*, `International Journal of Quantum Chemistry 10, 325 (1976) <https://doi.org/10.1002/qua.560100211>`__ 

.. [#ref15]  T.\  Ziegler and A. Rauk, *Carbon monoxide, carbon monosulfide, molecular nitrogen, phosphorus trifluoride, and methyl isocyanide as sigma donors and pi acceptors. A theoretical study by the Hartree-Fock-Slater transition-state method*, `Inorganic Chemistry 18, 1755 (1979) <https://doi.org/10.1021/ic50197a006>`__ 

.. [#ref16]  H.\  Fujimoto, J. Osamura and T. Minato, *Orbital interaction and chemical bonds. Exchange repulsion and rehybridization in chemical reactions*, `Journal of the American Chemical Society 100, 2954 (1978) <https://doi.org/10.1021/ja00478a004>`__ 

.. [#ref17]  S.\  Wolfe, D.J. Mitchell and M.-H. Whangbo, *On the role of steric effects in the perturbational molecular orbital method of conformational analysis*, `Journal of the American Chemical Society 100, 1936 (1978) <https://doi.org/10.1021/ja00474a055>`__ 

.. [#ref18] A.J. Stone and R.W. Erskine, *Intermolecular self-consistent-field perturbation theory for organic reactions. I. Theory and implementation; nucleophilic attack on carbonyl compounds*, `Journal of the American Chemical Society 102, 7185 (1980) <https://doi.org/10.1021/ja00544a003>`__ 

.. [#ref19] F.\  Bernardi, A. Bottoni, A. Mangini and G. Tonachini, *Quantitative orbital analysis of ab initio SCF=MO computations : Part II. Conformational preferences in H2N---OH and H2N---SH*, `Journal of Molecular Structure: THEOCHEM 86, 163 (1981) <https://doi.org/10.1016/0166-1280(81)85082-8>`__ 

.. [#ref20] P.J. van den Hoek and E.J. Baerends, *Chemical bonding at metal-semiconductor interfaces*, `Applied Surface Science 41/42, 236 (1989) <https://doi.org/10.1016/0169-4332(89)90063-9>`__ 

.. [#ref21] J. M. Guevara-Vela, E. Francisco, T. Rocha-Rinza and A. M. Pendás, *Interacting Quantum Atoms - A review*, `Molecules 25, 4028 (2020) <https://doi.org/10.3390/molecules25174028>`__
