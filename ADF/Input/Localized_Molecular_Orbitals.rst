.. index:: localized orbitals 
.. index:: orbital localization 
.. index:: Boys-Foster localization
.. index:: Pipek-Mezey localization

Localized Molecular Orbitals
****************************

ADF provides the Boys-Foster method and Pipek-Mezey method for localization of Molecular Orbitals [#ref1]_ [#ref2]_ [#ref3]_. This implies a unitary transformation of the occupied molecular orbitals as computed in the SCF procedure, with the objective to obtain a (transformed) set of orbitals that represent exactly the same charge density but with molecular orbitals that are more localized in space than the original MOs. 

The goal of orbital-localization lies in analysis: the localized orbitals provide an easier-to-interpret picture. 
The localized molecular orbitals can be visualized with the ADF-GUI.

Orbital localization procedures require a measure of the localization of the orbitals which can then be optimized in the space of the allowed unitary transformations. Methods advocated in the literature differ in the definition of this measure. The Boys-Foster method minimizes the mean extension of the occupied orbitals around their center of gravity; see the literature for details. 
The Pipek-Mezey localization maximizes the sum of orbital-dependent partial charges on the nuclei, see literature for details.
Both Boys-Foster localization method and Pipek-Mezey localization method have been implemented in ADF, see Ref. [#ref1]_.

Occasionally it is useful to apply the localization only to a subset of the MOs, with the objective to expose certain features better. This is accomplished by performing the localization in a number of distinct steps, where at each step the localization is restricted by keeping a subset of the MOs frozen. A case is worked out in the Examples document. 

The computation of localized orbitals is controlled with the block-type key. By default (if the key is not supplied in input) no orbital localization is carried out. 

.. _keyscheme LOCORB: 


::

   LOCORB {nopop store}
     {Criterion <BOYS|PM>}
     Spintype FrozenMOs
     Spintype FrozenMOs
     ...
   end

``nopop``
   Specifies that no SFO population analysis is to be carried out on the localized MOs. By default this population analysis will be printed in the output file. 

``store``
   Specifies that the transformation from MOs to localized MOs is stored on adf.rkf (TAPE21).

``Criterion <BOYS|PM>``
   By default the Boys-Foster localization method is used if Criterion is not specified and in case 'Criterion BOYS' is specified. If 'Criterion PM' is specified, the Pipek-Mezey localization method is used.

``Spintype``
   Must be either alfa or beta (not case sensitive) and refers to spin-A and spin-B orbitals respectively. In a spin-restricted run beta records are meaningless and must not be used. 

``FrozenMOs``
   A list (possibly empty) of integers, referring to a list of MOs from the SCF, and/or labels of irreducible representations. The integers and/or labels may be given in any order. 

Each record Spintype FrozenMOs in the data block defines a localization *cycle* in which the localization procedure is carried out on all orbitals (of the indicated spin), except those indicated by the FrozenMOs. 

For either spin at least one localization cycle is carried out. If no data record for that spin is found in the data block, a full localization is performed, without any MOs excluded. 

The data block may be completely empty (but the record end must be supplied since the key is block-type) and would be equivalent with specifying two records, one for either spin, without any FrozenMOs: 

::

   LOCORB {nopop}
   end

is equivalent with 

::

   LOCORB {nopop}
     alfa
     beta
   end

The integers in FrozenMOs refer to an overall list of SCF MOs consisting of all valence MOs in each symmetry representation up to and including the highest non-empty one. So, when for instance in the first irrep MO #4 is the highest non-empty one and in the second irrep mo #2 is the highest non-empty one, then in the overall list the first 4 are the orbitals of the first irrep, the no.s 5 and 6 are from the second irrep, et cetera. 

Each symmetry label in FrozenMOs collectively denotes in one stroke all molecular orbitals of that representation up to and including the highest occupied one (in that symmetry). The label may be the name of an irreducible representation or of a subspecies. In the former case all partner representations are denoted collectively. In an atom symmetry for instance, specifying P would be equivalent to P:x P:y P:z. 

Note that if the final SCF has in any symmetry representation empty orbitals *below* the highest non-empty orbital in that symmetry  - violating the Aufbau principle - then these empty orbitals are included in the above-defined overall list and hence a FrozenMOs specification is necessary, namely to avoid mixing MOs with different occupation numbers in the localization. 

.. note::

  It is imperative that in a particular localization cycle only MOs from the SCF are combined that have identical occupation numbers. If this is violated the program will carry out the localization without error message, but the results are incorrect in the sense that the density defined by the localized orbitals is *not* the same anymore as the SCF density. 

  So, if any of the MOs in the overall list defined above is not fully occupied (open shell, excited state, ...) you need to define precisely the localization cycles - localizing in each cycle only MOs with identical occupations and freezing all others - in order to obtain sensible results.


In the output file the localized MOs are printed as expansions in SFOs and (optionally) a population analysis is given, again in terms of the SFOs. Furthermore, each localized MO has associated with it an energy value and an occupation number. The energy is the expectation value of the Fock operator for the orbital. The occupation number is obtained as a weighted sum from the SCF MOs that were combined into the localized orbital. As mentioned before one should combine only SCF MOs with identical occupations into a localized orbital, in which case its occupation number will be the same. The printout of the occupation number of the localized orbital allows therefore a verification that a correct localization procedure has been carried out. 

.. _PLMO:

Perturbed Localized Molecular Orbitals
--------------------------------------

Perturbed localized molecular orbitals, correct to first order in an applied field, can be calculated in case of AORESPONSE.
Can be used if the applied field changes the density in first order.
Ref. [#ref1]_ describes this functionality and the implementation in ADF in detail, and gives some examples.
The perturbed localized molecular orbitals can be visualized with the ADF-GUI.
In addition to the AORESPONSE and the LOCORB key one has to specify the PERTLOC key in order to calculate these perturbed localized molecular orbitals.
The optional subkeywords of the block key PERTLOC are described below.

::

   LOCORB ..
     ..
   End
   AORESPONSE
     ..
   End
   PERTLOC
     efield
     bfield
     alfa
     gprime
     beta
     <static|dynamic>
     <diag|fulltens>
   End

``efield``
   The perturbation is an electric field (default).

``bfield``
   The perturbation is a magnetic field. Should be consistent with AORESPONSE.

``alfa``
   Analyze the static or dynamic polarizability.

``gprime``
   Analyze the G' (gyration) tensor, for optical rotation dispersion. Requires a frequency dependent perturbation field, with a frequency (omega) unequal to zero.

``beta``
   Analyze the optical rotation parameter beta. The relation to G' is beta = -G'/omega. The optical rotation parameter beta is calculated directly [#ref4]_ and has a well-defined static limit, i.e. omega can be zero or non-zero.

``<static|dynamic>``
   The static or dynamic (frequency dependent) subkeyword should be consistent with what is used in AORESPONSE. Static is default, should be used for a static field. Dynamic should be used for a frequency dependent perturbation field.

``<diag|fulltens>``
   Diag is default, which will only analyze the diagonal of the response tensor. If fulltens is specified the full tensor is analyzed.

.. only:: html

  .. rubric:: References

.. [#ref1] J.\  Autschbach and H.F. King, *Analyzing molecular static linear response properties with perturbed localized orbitals*, `Journal of Chemical Physics 133, 044109 (2010) <https://doi.org/10.1063/1.3455709>`__ 

.. [#ref2] C.\  Edmiston and K. Rudenberg, *Localized Atomic and Molecular Orbitals*, `Reviews of Modern Physics 35, 457 (1963) <https://doi.org/10.1103/RevModPhys.35.457>`__ 

.. [#ref3] J.M Foster and S.F. Boys, *Canonical Configurational Interaction Procedure*, `Reviews of Modern Physics 32, 300 (1960) <https://doi.org/10.1103/RevModPhys.32.300>`__ 

.. [#ref4] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *A Density Functional Theory study of frequency-dependent polarizabilities and van der Waals dispersion coefficients for polyatomic molecules*, `Journal of Chemical Physics 103, 9347 (1995) <https://doi.org/10.1063/1.469994>`__ 
