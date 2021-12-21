
Results on Output
*****************

The (standard) output file contains information of the main characteristics of the run, the SCF and geometry optimization results, bonding energy and population analyzes. Major parts of output can be regulated with print switches, see section :ref:`controlling_printed_output`. 

By default the program produces quite a bit of output, for a large part related to (Mulliken-type) population analyzes of the molecule in total, as well as of individual orbitals, both in terms of the elementary basis functions and in terms of the SFOs, the symmetry-adapted Fragment Orbitals. 

The fragment-oriented approach of ADF is very suitable for a thorough chemical analysis of molecular orbital properties and a conceptual representation of results. New users are advised to spend time and get familiar with the SFO-type analysis. It is an extremely more powerful tool to understand the electronic structure of the molecule than the classical atomic orbital populations. 

The results for structure and reactivity, spectroscopic properties, transport properties that are printed are meant to be self-explanatory.
See also the input options for each of these properties.

Electronic Configuration
========================

The direct results from the SCF are the orbital energies and occupation numbers. This defines the electronic configuration: the occupation numbers and HOMO and LUMO energies for instance show whether or not the aufbau principle is satisfied in the final situation. 

.. index:: XPS 
.. index:: X-ray photoelectron spectroscopy 

The energies of the Core Orbitals can be used to interpret for instance XPS (X-ray Photoelectron Spectroscopy) data: from Koopman's theorem these core orbital energies are an approximation to the core ionization energies. This neglects the effect of relaxation upon the ionization so that absolute energy values may not be very good; relative values, however, should be fair and can therefore be used to study (relative) chemical shifts. 

.. index:: charge analysis 
.. _ATOMCHARGES: 
.. index:: Mulliken population 
.. _results mulliken:

Mulliken populations
====================

Mulliken populations are based on the elementary atomic basis functions (bas). The individual BAS populations are printed together with summaries of the populations in all basis functions with the same angular moment quantum number on the same atom. A final summary is obtained by adding all functions on each atom, yielding the atom-atom populations. The atom-atom populations per l-value can be obtained if the key EXTENDEDPOPAN is included. The atomic gross charges are derived from the net and the overlap populations in the usual way. In addition, a population analysis may be given of individual MOs (by default this is suppressed). See the EPrint keys SCF (option mopop) and orbpop. 

Mulliken-type populations are computed and printed at various levels of refinement (ranging from *per-basis function* to *per-fragment type*, data for the whole molecule as well as for individual MOs), and in two different representations, one based on the elementary basis functions (bas), the other on SFOs (Symmetrized Fragment Orbitals). This is potentially a very large amount of data. Precisely what is printed by default, and how this can be modified so as to suppress output or, alternatively, to get more information, is regulated by the print keys (print, eprint). 

.. index:: Hirshfeld charges 
.. index:: VDD charges 
.. index:: Voronoi deformation density 
.. _results hirshfeld:


Hirshfeld charges, Voronoi deformation density
==============================================

Mulliken populations can be summarized to yield atomic charges. Alternative methods exist to deduce atom charges from the self-consistent results of a molecular calculation. Several of those alternatives are provided by ADF: Hirshfeld analysis, Voronoi analysis, multipole derived charges, and charge model 5. 

Of the methods applied in ADF to compute charges (Mulliken, Hirshfeld, Voronoi) we recommend the Hirshfeld analysis [#ref2]_,  [#ref3]_ and the analysis based on Voronoi *deformation* density (VDD) charges [#ref1]_,  [#ref4]_, see below. The fragments to which the Hirshfeld charges apply are enumerated in the early geometry part of the output file, where for each fragment the numbers of the atoms are given that belong to the fragment. The sum of the Hirshfeld charges may not add up to the analytical net total charge of the molecule. Any deviation from this is caused by numerical integration precision (small effect) and the neglect of long-distance terms that ADF uses to speed up the integral evaluations. This approximation does not affect very much the energy and molecular orbital properties, but it does show up in the sum-of-charges somewhat more. It does not indicate an error (unless the deviation is really large, say in the order of 1‰ of the total number of electrons). 

The Hirshfeld analysis produces a charge value per fragment, computed as the integral of the SCF charge density over space, in each point weighted by the relative fraction of the (initial) density of that fragment in the total initial (sum-of-fragments) density: 

.. math:: 

   Q^\text{frag(i)} = \int \rho^\text{SCF} \rho^\text{initial frag(i)} / \sum_j \rho^\text{initial frag(j)}    \qquad (5.1.1)

The VDD method is based on the *deformation* density and a rigorous partitioning of space into non-overlapping atomic areas, the so-called Voronoi cells [#ref1]_ [#ref4]_ [#ref7]_. The Voronoi cell of an atom *A* is the region in space closer to nucleus *A* than to any other nucleus (cf. Wigner-Seitz cells in crystals). The VDD charge of an atom *A* monitors the *flow* of charge into, or out of the atomic Voronoi cell as a result of 'turning on' the chemical interactions between the atoms. The VDD method summarizes the three-dimensional deformation density on a per-atom basis. It is conceptually simple and affords a transparent interpretation based on the plausible notion of charge redistribution due to chemical bonding, i.e. the gain or loss of charge in well-defined geometrical compartments of space. For the use of VDD in analyzes involving molecular fragments, see Ref. [#ref8]_. 

In the same fashion as for the Hirshfeld analysis, a summation over all atoms is given which should yield zero (for a neutral molecule). The deviation from zero is caused by numerical integration and by neglect-of-long-distance-terms; the same remarks apply as for the Hirshfeld analysis above. 

The partitioning of space, using mid-way separation planes, is inappropriate to produce useful absolute numbers when neighboring atoms have very different sizes, for instance, Hydrogen and a heavy metal. However, *changes* in the density analyzed in this way do give a reasonable general insight in the effect of bonding on the location of charge densities, in particular because the Voronoi data per atom are split up in contributions within the atomic sphere and the rest of its Voronoi cell. 

Hirshfeld and Voronoi charge analyzes are printed at the end of the SCF (of the last geometry, in case of an Optimization). 

The Hirshfeld analysis in ADF produces charges *per fragment*, so that *atomic* charges are obtained only if single-atom fragments are used. This limitation does not apply to Voronoi charges (data per atom). Mulliken charges are given both per atom *and* per fragment. 

In the printout of charges per fragment (as for the Hirshfeld analysis), you have to be aware of the *ordering* of fragments. A complete list of fragments is printed in the early GEOMETRY section of standard output, where you also find which atom(s) correspond(s) to which fragment. Note that even when you use single-atom fragments only, the order of fragments is usually quite different from the order of atoms in your input file. Typically (but not necessarily exactly in each case), when you use single-atom fragments: consider the first non-dummy atom in your ATOMS block. This defines the first atom *type*. Then browse the ATOMS list until you find an atom of a different type. This defines the second atom type, and so on. The single-atom fragment list will often be such that you first get *all* atoms of the first atom type, then all atoms of the second type, and so on. Check the printed list-of-fragments always, to avoid mistakes in assigning Hirshfeld charges to atoms (fragments). 


.. index:: multipole derived charges 
.. index:: MDC 
.. _MDC:


Multipole derived charges
=========================

The multipole derived charges (MDC) analysis [#ref9]_ uses the atomic multipoles (obtained from the fitted density) up to some level X, and reconstructs these multipoles exactly (up to level X) by distributing charges over all atoms. This is achieved by using Lagrange multipliers and a weight function to keep the multipoles local. Since the atomic multipoles are reconstructed up to level X, the molecular multipoles are represented also up to level X. The recommended level is to reconstruct up to quadrupole: MDC-q charges. The SCF should have converged for a meaningful MDC analysis. 


.. index:: charge model 5 
.. index:: CM5 
.. _CM5:


Charge model 5
==============

The charge model 5 (CM5) [#ref10]_ [#ref11]_ uses the Hirshfeld analysis in combination with a parametrization to yield atomic charges that can accurately reproduce dipole moments obtained from experimental results. For input, use the keyword  :ref:`CM5<keyscheme CM5>`. 

.. _BONDORDERS: 
.. index:: bond order 
.. index:: Nalewajski-Mrozek bond order 

Bond order analysis
===================


The bond order analysis (see :ref:`bond_roders_input`). produces the output in which the bond order values are printed for each pair of atoms for which the Nalewajski-Mrozek bond order value is larger than the threshold that can be specified with the keyword BONDORDER. For convenience the printed bond orders are accompanied by the corresponding inter-atomic distance.  In the Nalewajski-Mrozek approach [#ref14]_ [#ref15]_ [#ref22]_ [#ref23]_ [#ref24]_ [#ref25]_ the bond order indices b\ :sub:`AB`  are calculated based on  the one- and two-center valence indices 

.. math::

   b_{AB} = V_{AB} + W^{AB}_A V_A + W^{AB}_B V_B

with the weighting factors for one-center indices given by 

.. math::

   W^{XY}_X = \frac{V^\text{COV}_{XY}}{\sum_Z V^\text{COV}_{XZ}}


Unlike other definitions of covalent bond orders, the Nalewajski-Mrozek valence indices comprise both, covalent and ionic contributions. There exist three alternative sets of the Nalewajski-Mrozek valence indices [#ref14]_ [#ref15]_ [#ref22]_ [#ref23]_ [#ref24]_ [#ref25]_ [#ref12]_. The bond order indices calculated from each set of the valence indices differ slightly due to arbitrariness in the way of splitting the one-center terms between bonds. More detailed description of alternative valence indices and their physical meaning is summarized in [#ref14]_; see also original papers [#ref15]_ [#ref22]_ [#ref23]_ [#ref24]_ [#ref25]_. 

By default the bond order indices based on the valence indices obtained from partitioning of  :math:`Tr(P\Delta P)` are printed in the ADF output. Note that in this version the covalent two-center part (also printed in the output) is equal to the Gopinathan-Jug [#ref15]_ bond order.  The default values are: 

.. math::

      & V_A = V^\text{ion}_A + V^\text{COV}_A \\
      & V^\text{ion}_A = \sum_{a \in A} \left(  P^\alpha_{aa} \Delta P^\alpha_{aa}  +  P^\beta_{aa} \Delta P^\beta_{aa}  \right) \\
      & V^\text{COV}_A = 2 \sum_{a \in A} \sum_{a' \in A, a<a`} \left(  P^\alpha_{aa'} \Delta P^\alpha_{a'a}  +  P^\beta_{aa'} \Delta P^\beta_{a'a}  \right) \\
      & V^\text{COV}_{AB} = 2 \sum_{a \in A} \sum_{b \in B} \left(  P^\alpha_{ab} \Delta P^\alpha_{ba}  +  P^\beta_{ab} \Delta P^\beta_{ba}  \right)

To produce the values from all alternative versions of Nalewajski-Mrozek valence indices, accompanied by the Gopinathan-Jug [#ref15]_ and Mayer [#ref12]_ bond orders, see the keyword BONDORDER. 

The Mayer [#ref12]_ bond orders can also be calculated (see :ref:`BondOrders%PrintAll <adf-key-BondOrders>`). The two implementations of calculating the Mayer bond orders differ slightly if one uses frozen cores. They should agree exactly in all electron calculations. 

.. index:: dipole moment 
.. index:: quadrupole moment 

Dipole moment, Quadrupole moment, Electrostatic potential
=========================================================

Dipole moment. Note that in a ion the value of the dipole moment depends on the choice of the origin, as follows from elementary electrostatic theory. 

Quadrupole moment. Note that the value of the quadrupole moment often depends on the choice of the origin, as follows from elementary electrostatic theory. 

Electrostatic potential at the nuclei: the Coulomb potential of the molecule at the nuclear positions, where the contribution from the nucleus itself is omitted. 

.. index:: population analysis 

Fragments and Basis Functions
=============================

``SFOs``
  SFOs: the Symmetry combinations of Fragment Orbitals. The SFOs are the basic conceptual entities for the analysis of MOs and other results. Note: The FO *coefficients* that expand the SFOs are normalized in the sense that they add up (squared) to unity. The resulting SFO *function* is not necessarily a normalized function. The FOs are normalized, so it depends on the *overlap* between the FOs what the self-overlap and hence the norm of the SFO is. Also printed are, for each subspecies in each irrep separately, the indices of the elementary basis functions from which the FOs and hence the SFOs are built up. (The overlap matrix of SFOs is printed much later, in the SFO Populations section after everything (SCF, Geometry) has cycled to convergence).

``Elementary basis functions (BAS)``
  First the lists of function *sets*, defined by radial behavior and the angular quantum number, are printed for all atom types on which the functions are centered. Thereafter follows the complete BAS list where the function sets have been expanded over all atoms (the *sets* are printed only for the atom *types*) and also over all Cartesian harmonics (6, not 5 *d*-functions, et cetera). In this printout the numbering can be found to which the SFO survey above refers.


MO analysis
===========

``MOs expanded in SFOs``
  This gives a useful characterization of the character of the self-consistent molecular orbitals. Additional information is supplied by the SFO population analysis, see below. The definition of the SFOs in terms of the Fragment MOs has been given in a earlier part of output (section build). The SFO occupation numbers that applied in the fragments are printed. This allows a determination of the orbital interactions represented in a MO. Be aware that the bonding/antibonding nature of a SFO combination in a mo is determined by the relative signs of the coefficients *and* by the overlap of the SFOs. This overlap *may be negative!* Note also that SFOs are generally *not* normalized functions. The SFO overlap matrix is printed later, in the SFO-populations part below. 

.. index:: SFO population analysis 

``SFO population analysis``
  For each irrep: 

  - Overlap matrix of the SFOs. Diagonal elements are not equal to 1.0 if the SFO is a linear combination of two or more Fragment Orbitals. The Fragment Orbitals themselves are normalized so the diagonal elements of the SFO overlap matrix give information about the overlap of the Fragment Orbitals that were combined to build the SFO. 
  - Populations on a per-fragment basis for a selected set of MOs (see EPrint, subkey *OrbPop*). This part is by default *not* printed, see EPRINT subkey *SFO*. 
  - SFO contributions per MO: populations for each of the selected MOs. In these data the MO occupation numbers are not included, so that also useful information about the virtual MOs is obtained. The printout is in matrix form, with the MOs as columns. In each printed matrix a row (corresponding to a particular SFO) is omitted if all populations of that SFO are very small in all of the MOs that are represented in that matrix. See eprint, subkey *orbpop*. Note that this method to define SFO populations (for orbitals) is very similar to the classical Mulliken type analysis, in particular regarding the aspect that *gross* populations are obtained as the diagonal (*net*) populations plus half of the related off-diagonal (overlap) populations. Occasionally this may result in negative (!) values for the population of certain SFOs, or in percentages higher than 100%. If you have such results and wonder if they can be right, work out one of the offending cases by hand, using the printed SFO overlap matrix and the printed expansion of the MOs in SFOs to compute 'by hand' the population matrix of the pertaining MO. To avoid doing large calculations it is usually sufficient to take only the few largest MO expansion coefficients; this should at least qualitatively give the correct outcomes. 
  - Total SFO gross populations in a symmetry representation: from a summation over all MOs (not only those analyzed in the previous section of output) in the symmetry representation under consideration. In the gross populations the MO occupation numbers have been included. 
  - (Per spin): A full list of all MOs (combining all symmetry representations), ordered by energy, with their most significant SFO populations. Since there might be several significant SFO populations for a particular MO, and an SFO may actually be a linear combination of several (symmetry-related) Fragment Orbitals, this table could get quite extensive. In order to confine each SFO population specification to one line of output, the SFOs are indicated by the characteristics of the first term (Fragment Orbital) of its expansion in Fragment Orbitals. So, if you see the SFO given as the '2 P:x on the first Carbon fragment', it may actually refer to the symmetry combination of, for instance, 2P:x and 2P:y orbitals on the first, second and third Carbon fragments. A full definition of all SFOs in terms of the constituting Fragment Orbitals is given in an early part of the output. 


.. index:: bond energy analysis
.. index:: energy decomposition analysis


Bond energy analysis
====================

The bond energy and its decomposition in conceptually useful terms: Pauli (exchange) repulsion, total steric repulsion, orbital interactions (partitioned into the contributions from the distinct irreducible representations), and corrections for some approximations (fitting and Transition State analysis procedure). For a discussion of bonding energy decompositions and applications see e.g. refs. [#ref19]_ [#ref20]_ [#ref21]_ [#ref26]_ [#ref27]_ [#ref28]_ [#ref29]_ [#ref30]_ [#ref31]_ [#ref32]_.

The program prints the bonding energy (not in a Create or Frequencies run) and its decomposition in terms that are useful for chemical interpretation. The *total* energy is not computed. The bonding energy is defined relative to the fragments. When *basic atoms* are employed as fragments one should realize that these do not represent the atomic ground state since they are computed as spin-restricted and spherically symmetric objects, with possibly fractional occupation numbers. The correct multiplet state is not computed. To obtain the bonding energy with respect to isolated atoms you should therefore add atomic correction terms to account for spin polarization and the multiplet state. See also the SLATERDETERMINANTS key and the discussion on multiplet states. 

The spin polarization energy can be computed by running the single atom unrestricted, using as fragment the corresponding (restricted) basic atom. The true multiplet state is not necessarily obtained in this way. 

For the comparison of computed bonding energies with experimental data one should furthermore be aware of any aspects that are not represented in the computational formalism, such as zero-point motions and environment (solvent) effects. 

In a Geometry Optimization or Transition State search, the program may print a bonding energy evaluation at each geometry (depending on print switches). A  test-energy value is written in the log file. This is *not* the bonding energy, although the difference is usually small. The test-energy printed in the log file is the energy expression from which the energy gradients are computed. The true bonding energy contains in addition a few (small) correction terms that are mostly related to the fit incompleteness. These correction terms are usually very small. 

If Electric Fields are used in the computation (homogeneous and/or point charges), the printed Bonding Energy is the energy of the molecule in the field minus the energy of the fragments in the same field. The energy terms due to the field are also printed separately so that one can subtract them from the total bonding energy to obtain the energy-change without field-terms. 

.. only:: html

  .. rubric:: References

.. [#ref1] G.\  te Velde, *Numerical integration and other methodological aspects of bandstructure calculations*, in *Chemistry*. 1990, Vrije Universiteit: Amsterdam. 

.. [#ref2] F.L. Hirshfeld, *Bonded-atom fragments for describing molecular charge densities*, `Theoretica Chimica Acta 44, 129 (1977) <https://doi.org/10.1007/BF00549096>`__ 

.. [#ref3] K.B. Wiberg and P.R. Rablen, *Comparison of atomic charges derived via different procedures*, `Journal of Computational Chemistry 14, 1504 (1993) <https://doi.org/10.1002/jcc.540141213>`__ 

.. [#ref4] F.M. Bickelhaupt, N.J.R. van Eikema Hommes, C. Fonseca Guerra and E.J. Baerends, *The Carbon-Lithium Electron Pair Bond in* (CH3Li)\ :sub:`n` (n = 1, 2, 4), `Organometallics 15, 2923 (1996) <https://doi.org/10.1021/om950966x>`__ 

.. [#ref7] C.\  Fonseca Guerra, J.-W. Handgraaf, E. J. Baerends and F. M. Bickelhaupt, *Voronoi Deformation Density (VDD) charges. Assessment of the Mulliken, Bader, Hirshfeld, Weinhold and VDD methods for Charge Analysis*, `Journal of Computational Chemistry 25, 189 (2004) <https://doi.org/10.1002/jcc.10351>`__ 

.. [#ref8] C.\  Fonseca Guerra, F.M. Bickelhaupt, J.G. Snijders and E.J. Baerends, *The Nature of the Hydrogen Bond in DNA Base Pairs: The Role of Charge Transfer and Resonance Assistance*, `Chemistry - A European Journal 5, 3581 (1999) <https://doi.org/10.1002/(SICI)1521-3765(19991203)5:12%3C3581::AID-CHEM3581%3E3.0.CO;2-Y>`__ 

.. [#ref9] M.\  Swart, P.Th. van Duijnen and J.G. Snijders, *A charge analysis derived from an atomic multipole expansion*, `Journal of Computational Chemistry 22, 79 (2001) <https://doi.org/10.1002/1096-987X(20010115)22:1%3C79::AID-JCC8%3E3.0.CO;2-B>`__ 

.. [#ref10] A.V. Marenich, S.V. Jerome, C.J. Cramer, D.G. Truhlar, *Charge Model 5: An Extension of Hirshfeld Population Analysis for the Accurate Description of Molecular Interactions in Gaseous and Condensed Phases*, `Journal of Chemical Theory and Computation 8, 527 (2012) <https://doi.org/10.1021/ct200866d>`__ 

.. [#ref11] C.A. Peeples and G. Schreckenbach, *Implementation of the SM12 Solvation Model into ADF and Comparison with COSMO*, `Journal of Chemical Theory and Computation 12, 4033 (2016) <https://doi.org/10.1021/acs.jctc.6b00410>`__

.. [#ref12] I.\  Mayer, *Charge, bond order and valence in the ab initio SCF theory*, `Chemical Physics Letters 97, 270 (1983) <https://doi.org/10.1016/0009-2614(83)80005-0>`__ 

.. [#ref14] A.\  Michalak, R.L. De Kock and T. Ziegler, *Bond Multiplicity in Transition-Metal Complexes: Applications of Two-Electron Valence Indices*, `Journal of Physical Chemistry A 112, 7256 (2008) <https://doi.org/10.1021/jp800139g>`__ 

.. [#ref15] M.S. Gopinathan and K. Jug, *Valency. I. A quantum chemical definition and properties*, `Theoretica Chimica Acta 1983 63, 497 (1983) <https://doi.org/10.1007/BF00552652>`__ 

.. [#ref19] T.\  Ziegler and A. Rauk, *On the calculation of Bonding Energies by the Hartree Fock Slater method. I. The Transition State Method*, `Theoretica Chimica Acta 46, 1 (1977) <https://doi.org/10.1007/BF00551648>`__ 

.. [#ref20] T.\  Ziegler and A. Rauk, *A theoretical study of the ethylene-metal bond in complexes between copper(1+), silver(1+), gold(1+), platinum(0) or platinum(2+) and ethylene, based on the Hartree-Fock-Slater transition-state method*, `Inorganic Chemistry 18, 1558 (1979) <https://doi.org/10.1021/ic50196a034>`__ 

.. [#ref21] F.M. Bickelhaupt, N.M. Nibbering, E.M. van Wezenbeek and E.J. Baerends, *The Central Bond in the Three CN* Dimers NC_CN, CN-CN, and CN-NC: Electron Pair Bonding and Pauli Repulsion Effects*, `Journal of Physical Chemistry 96, 4864 (1992) <https://doi.org/10.1021/j100191a027>`__ 

.. [#ref22] R.F. Nalewajski and J. Mrozek, *Modified valence indices from the two-particle density matrix*, `International Journal of Quantum Chemistry 51, 187 (1994) <https://doi.org/10.1002/qua.560510403>`__ 

.. [#ref23] R.F. Nalewajski, J. Mrozek and A. Michalak, *Two-electron valence indices from the Kohn-Sham orbitals*, `International Journal of Quantum Chemistry 61, 589 (1997) <https://doi.org/10.1002/(SICI)1097-461X(1997)61:3%3C589::AID-QUA28%3E3.0.CO;2-2>`__ 

.. [#ref24] R.F. Nalewajski, J. Mrozek and A. Michalak, *Exploring Bonding Patterns of Molecular Systems Using Quantum Mechanical Bond Multiplicities*, `Polish Journal of Chemistry 72, 1779 (1998) <http://ichf.edu.pl/pjch/pj-1998/pj07s98.htm#1779>`__ 

.. [#ref25] R.F. Nalewajski, J. Mrozek and G. Mazur, *Quantum chemical valence indices from the one-determinantal difference approach*, `Canadian Journal of Chemistry 74, 1121 (1996) <https://doi.org/10.1139/v96-126>`__ 

.. [#ref26] K.\  Kitaura and K. Morokuma, *A new energy decomposition scheme for molecular interactions within the Hartree-Fock approximation*, `International Journal of Quantum Chemistry 10, 325 (1976) <https://doi.org/10.1002/qua.560100211>`__ 

.. [#ref27] T.\  Ziegler and A. Rauk, *Carbon monoxide, carbon monosulfide, molecular nitrogen, phosphorus trifluoride, and methyl isocyanide as sigma donors and pi acceptors. A theoretical study by the Hartree-Fock-Slater transition-state method*, `Inorganic Chemistry 18, 1755 (1979) <https://doi.org/10.1021/ic50197a006>`__ 

.. [#ref28] H.\  Fujimoto, J. Osamura and T. Minato, *Orbital interaction and chemical bonds. Exchange repulsion and rehybridization in chemical reactions*, `Journal of the American Chemical Society 100, 2954 (1978) <https://doi.org/10.1021/ja00478a004>`__ 

.. [#ref29] S.\  Wolfe, D.J. Mitchell and M.-H. Whangbo, *On the role of steric effects in the perturbational molecular orbital method of conformational analysis*, `Journal of the American Chemical Society 100, 1936 (1978) <https://doi.org/10.1021/ja00474a055>`__ 

.. [#ref30] A.J. Stone and R.W. Erskine, *Intermolecular self-consistent-field perturbation theory for organic reactions. I. Theory and implementation; nucleophilic attack on carbonyl compounds*, `Journal of the American Chemical Society 102, 7185 (1980) <https://doi.org/10.1021/ja00544a003>`__ 

.. [#ref31] F.\  Bernardi, A. Bottoni, A. Mangini and G. Tonachini, *Quantitative orbital analysis of ab initio SCF=MO computations : Part II. Conformational preferences in H2N---OH and H2N---SH*, `Journal of Molecular Structure: THEOCHEM 86, 163 (1981) <https://doi.org/10.1016/0166-1280(81)85082-8>`__ 

.. [#ref32] P.J. van den Hoek and E.J. Baerends, *Chemical bonding at metal-semiconductor interfaces*, `Applied Surface Science 41/42, 236 (1989) <https://doi.org/10.1016/0169-4332(89)90063-9>`__ 

