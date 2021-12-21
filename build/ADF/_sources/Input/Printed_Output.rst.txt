.. _controlling_printed_output:

Controlling printed Output
**************************

The amount of printed output is regulated with the keys Print, NoPrint, EPrint and Debug. (No)Print and Debug are simple keys, EPrint is a block type key. 

Many print options pertain to debugging  situations and are included here only for completeness. This section is intended to give a survey of all possibilities. Some items may be mentioned again in other sections where the subject of a particular print switch is discussed. 

.. _keyscheme PRINT: 

Print / NoPrint
===============

::

   PRINT Argumentlist
   Print Argumentlist
   NoPrint Argumentlist

``Argumentlist``
   A sequence of names separated by blanks or commas. The keys Print and NoPrint may occur any number of times in the input file. The names in the argument list may refer to various items. For some of them printing is normally on, and you can turn them off with NoPrint. For others the default is not printing; use Print to override that. 

Follows a list of the recognized items that are applicable in the argument lists, with a short explanation and defaults. Item names must be used exactly as given in the table - abbreviated or elongated forms will not be recognized - but they are not case sensitive. 


**Items**


``Atdist``
   Default: No

   Inter-atomic distance matrix at each new geometry (in an optimization)

``Bas``
   Default: Yes

   General control of output related to elementary basis functions (bas).

``Character-Table``
   Default: No

   Table of characters for the irreducible representations of the point group symmetry.

``Computation``
   Default: Yes

   Reports progress of the computation, with (concise) info about each SCF cycle.

``Core``
   Default: No

   Description of the frozen core: frozen core expansion functions (corbas) and the expansion coefficients for the frozen orbitals. This printing can only be activated if Functions is also *on*, otherwise it is ignored.

``CoreOrt``
   Default: No

   The valence basis set contains auxiliary Core Functions. They are not degrees of freedom but are used solely to ensure orthogonalization of the valence set to the frozen Core Orbitals. The orthogonalization coefficients and some related overlap matrices are printed.

``CoreTable``
   Default: No

   Internally the charge density and potential of the atomic frozen cores are processed as tables with values for a sequence of radial distances. A few initial and a few final values from these tables are printed, along with the (radial) integral of the core density, which should yield the number of core electrons.

``EKin``
   Default: No

   At the end of SCF: Kinetic energy of each occupied MO.

``EPauli``
   Default: Yes

   The repulsive Pauli term in the bonding energy (also called exchange repulsion) with its decomposition in density functional (lda and nl) and Coulomb terms.

``Fit``
   Default: Yes

   General control of output related to the density fitting.

``Fmat``
   Default: No

   Fock matrix computed at each cycle of the SCF.

``FmatSFO``
   Default: No

   Fock matrix (and overlap matrix) in the basis of symmetrized fragment orbitals (SFOs). This option requires the FULLFOCK and ALLPOINTS keyword to be present in the input. The matrix is printed only at the last SCF cycle. Use 1 iteration in the SCF for the Fock matrix at the first SCF cycle.

``Frag``
   Default: No

   General control of output related to build-molecule-from-fragments.

``Functions``
   Default: Yes

   List of employed Slater-type exponential basis functions and fit functions.

``Group-Operators``
   Default: No

   3\*3 matrices of point group symmetry operators, with the axis and angle of rotation

``Irrep-Matrices`` 
   Default No

   Irreducible representation matrices

``Logfile``
   Default: Yes

   At the end of the calculation a copy of the log file is appended to standard output

``low``
   Default: No

   Construction of the LOW basis from the elementary BAS functions and from the SFOs: combination coefficients

``lowMO``
   Default: No

   MOs are printed in the LOW (Lowdin) representation, in the RESULTS section

``OvlBAS``
   Default: No

   overlap matrices processed during the construction of the LOW basis. Only printed in case OLDORTHON is used in input.

``Pmat``
   Default: No

   The density matrix (in Lowdin representation) in each cycle of the SCF.

``QMpot``
   Default: Yes

   At the end of the SCF for each atom the electrostatic potential at its nucleus (excluding its own contribution of course).

``SCF``
   Default: Yes

   Controls the information about progress of the SCF procedure. Applies only if the print switch computation is on.

``sdiis``
   Default: No

   Expansion coefficients applied by the DIIS procedure during the SCF.

``sdiismat``
   Default: No

   Turns on sdiis(see above) *and* prints the *error vector* constructed by the DIIS routine (this is the commutator of the Fock matrix and the Density matrix). This is used to determine the DIIS expansion coefficients and to assess convergence.

``SFO``
   Default: depends on system size

   General control of SFO-related output (if SFO subkey of key EPRINT is used). If turned off, (almost) all such output is suppressed. If on, such printing is controlled by the eprint subkey SFO. The default depends on the system size: if the number of primitive STOs < 1000, the default is Yes, else No.

``Smat``
   Default: No

   Overlap matrix of BAS functions.

``Smearq``
   Default: No

   Smear parameter - if and when applied - used in the determination of electronic occupation numbers for the MOs, with details of how it works out at every cycle of the SCF. For debugging purposes.

``SpinOrbit``
   Default: No

   detailed information about how double-group symmetry representations are related to the single group representations

``Tails``
   Default: No

   In each block of integration points (see Blocks) the evaluation of (Slater-type) exponential functions (basis, fit) is skipped when the function has become negligible for all points in that block due to the distance of those points from the atom where the function is centered. The relative savings due to this distance screening is printed at the first geometry cycle (use debug for printing at all cycles).

``TechPar``
   Default: Yes

   Technical parameters such as maximum vector length in vectorized numerical integration loops, SCF parameters.

*Arguments for the keys PRINT and NOPRINT.*
   
For print switches Frag, Fit, Numint, Repeat, SCF, SFO, TF, see the key EPRINT below. 

.. index:: debug 
.. _keyscheme DEBUG: 

Debug
=====

The key DEBUG is used to generate extensive output that is usually only relevant for debugging purposes. It operates exactly like the PRINT key but there is no converse: nodebug is not recognized; it would be irrelevant anyway because by default all debug print switches are off. 

A  list of the possible items for the DEBUG key is given below. 

All items of the print list can also be used with the debug key. If they are not mentioned in table III, the meaning is the same as for the print key, but the corresponding output may be generated more often, for instance at every SCF cycle rather than at the last one only. 

.. csv-table:: Table III. Arguments for the print key DEBUG. All debug switches are by default off.
   :widths: 100,460

   **Item**,**Explanation**
   Basis,"Construction of the orthonormal LOW basis from elementary (BAS) and fragment (FO) basis."
   Core,Core Orthogonalization procedure
   Ekin,Kinetic energy matrices. (compare the print switches EKIN)
   Fit,Construction of the symmetry adapted fit functions
   Fitint,Construction of integrals used in the Fit procedure.
   Gradients,The gradients split out in parts.
   NumInt,"Numerical integration. Very extensive output"
         ,"(including the coordinates and weights of all generated points)."
   Pmat,"P-matrix (density matrix) during SCF"
       ,"and in the ETS analysis program in the BAS representation."
   Rhofih,Computation of fit coefficients during the SCF.
   SCF,"Extensive output during the SCF procedure about many different items."
      ,"See also EPRINT, subkey SCF."
   SDIIS,"All data concerning the DIIS as used during the SCF."
   TransitionField,"The Transition State procedure to compute and analyze certain terms in the bonding energy."
                  ,"The distinct components, the involved transition field Fock matrices, etc."
   
   

Eprint
======

The key EPRINT is an extended version of the (no)print key, employed for print switches that require more specification than just off or on.  

Contrary to what is the case for the keys print and noprint, the key EPRINT must occur only once in the input file; any subsequent occurrences are incorrect and ignored or lead to abort. 

.. _keyscheme EPRINT: 


::

   EPRINT
     subkey
     subkey
     ...
   end

``subkey``
   A subkey-type structure: it consists of a keyword followed by data, so that it functions as a simple (sub)key, *or* it is a keyword followed by a data *block* which must then end with the word subend. 

The subkeys used in the EPRINT data block are called Eprint keys. A complete list of them is given below. All available EPRINT keys are discussed in the schemes below. The enclosing records EPRINT and end are omitted in these schemes. 

.. csv-table:: Table IV. List of EPRINT subkeys.
   :widths: 100,460

   **EPRINT subkeys**,**Subject**
   :ref:`AtomPop<results mulliken>`, Mulliken population analysis on a per-atom basis
   :ref:`BASPop<EPRINT BASPOP>`, Mulliken population analysis on a per-bas-function basis
   :ref:`Eigval<EPRINT EIGVAL>`,One-electron orbital energies
   :ref:`Fit<EPRINT FIT>`,Fit functions and fit coefficients
   :ref:`Frag<EPRINT FRAG>`,Building of the molecule from fragments.
   :ref:`FragPop<EPRINT FRAGPOP>`,Mulliken population analysis on a per fragment basis
   :ref:`NumInt<EPRINT NUMINT>`,Numerical Integration
   :ref:`OrbPop<EPRINT ORBPOP>`,"(Mulliken type) population analysis for individual MOs"
   :ref:`OrbPopEr<EPRINT ORBPOPER>`,Energy Range (ER) in hartree units for the OrbPop subkey
   :ref:`Repeat<EPRINT REPEAT>`,"repetition of output in Geometry iterations (SCF, optimization, ...)"
   :ref:`SCF<EPRINT SCF>`,Self Consistent Field procedure
   :ref:`SFO<EPRINT SFO>`,"Information related to the Symmetrized Fragment Orbitals and the analysis"
   :ref:`TF<EPRINT TF>`,"Transition Field method."
   
   

Eprint subkeys vs. Print switches
=================================

Several EPRINT subkeys are merely shortcuts for normal (no)print switches. All such simple subkeys are used in the following way: 

::

   EPRINT
     ESUBKEY argumentlist
   END

``Esubkey``
   One of the following EPRINT subkeys: Fit, Frag, NumInt, Repeat, SCF, sdiis, SFO, TF.


``argumentlist``
   A sequence of names, separated by delimiters. Each of these names will be concatenated with the esubkey and the combination will be stored as a normal print switch. Example: Frag rot, SFO will be concatenated to fragrot and fragsfo and both will be stored as print switches. All such combinations can also be specified directly with the key PRINT. The example is therefore exactly equivalent with the input specification: print FragRot, Fragsfo**** 

If any of the names starts with the two characters no, the *remainder* of the name will be concatenated with the EPRINT, but now the result will be stored and treated as a  noprint switch. Items that are on by default can in this way be turned off. Example: 

::

   EPRINT
     FRAG noRot Eig
   END

This turns Rot *off* and Eig *on* for the EPRINT subkey Frag. Equivalent would be: 

.. _keyscheme NOPRINT: 


::

   NOPRINT FragRot
   Print FragEig

Follows a description of all simple EPrint subkeys: 

.. _EPRINT FIT: 

**Fit**

The subkey fit controls output of how the elementary fit functions are combined into the symmetric (A1) fit functions. It controls also printing of the initial (start-up) and the final (SCF) fit coefficients. 

::

   EPRINT
     FIT list
   END

``list``
   A list of items, separated by blanks or commas. The following items are recognized: Charge, Coef, Comb. 

``Charge``
   The amount of electronic charge contained in the fit (start-up), total and per fragment. 

``Coef``
   The fit coefficients that give the expansion of the charge density in the elementary fit functions. 

``Comb``
   The construction of the totally symmetric (A1) fit function combinations from the elementary fit functions. 

   By default all options are off. 

.. _EPRINT FRAG: 

**Frag**

The subkey frag controls output of how the molecule is built up from its fragments. 

::

   EPRINT
     FRAG list
   END

``list``
   A list of items, separated by blanks or commas. The following items are recognized: Eig, Fit, Rot, SFO. 

``Eig``
   The expansion coefficients in elementary functions (bas) of the fragment Molecular Orbitals as they are on the fragment file. 

``Rot``
   The rotation (and translation) required to map the master fragment (i.e. the geometrical data on the fragment file) onto the actual fragment which is part of the current molecule. N.B.: if eig and rot are both *on*, the rotated fragment orbitals are printed also. 

``Fit``
   The fit coefficients that describe the fitted charge density of the fragments after the rotation from the *master* fragment on file to the actual fragment. These are the molecular fit coefficients that are used (by default) to construct the total molecular start-up (fitted) charge density and hence the initial Coulomb and XC potential derived from it. 

``SFO``
   The Symmetry-adapted combinations of Fragment Orbitals that are used in the current calculation. This feature ensures that the definition of the SFOs is printed. This will happen anyway whenever the EPRINT subkey SFO itself is activated. By default all options are off. Remark: SFO analysis in a Spin-Orbit relativistic calculation is implemented only in the case there is one scalar relativistic fragment, which is the whole molecule. 


.. _EPRINT NUMINT: 

**NumInt**

Output related to the numerical integration procedure. 

::

   EPRINT
     NUMINT list
   END

``list``
   A list of items, separated by blanks or commas. The following items are recognized: Res. 

   In case of the old deprecated Voronoi numerical integration grid, in addition the following undocumented items are recognized: All, Geo, Ovl, Par, Pnt, Sym, Test.

``Res``
   results as regards the total number of points, the sum-of-weights and the partitioning of the points in blocks (for segmented vectorization). 

   By default Res is on. 

.. _EPRINT ORBPOP: 

**OrbPop**

Specifies that (Mulliken type) population analysis should be printed for individual MOs, both on a per-SFO basis and on a per-bas function basis. The format of the subkey is as follows: 

::

   EPRINT
     ORBPOP TOL=X Nocc Nunocc
     SUBEND
   END

X is the threshold for the SFO coefficient value to include in  the listing for the per-SFO analysis. Nocc is the number of the highest occupied  and Nunocc is the number of the lowest unoccupied orbitals to analyze. 

**OrbPopEr**

.. _EPRINT ORBPOPER: 

Specifies the energy range for the MOs to which the OrbPop key applies. The default range is from -0.7 below the HOMO to 0.2 Hartree above the LUMO. Usage:  

::

   EPRINT
     OrbPopER minEn maxEn
   END

where minEn and maxEn are both in Hartree, and have the defaults just specified. In order to get information on many more orbitals, simply specify a large negative value for minen and a large positive value to maxen. 

.. _EPRINT REPEAT: 

**Repeat**

Control the repetition of output in Geometry iterations: optimization, computation of frequencies, transition state search. 

::

   EPRINT
     Repeat list
   END

``list``
   contains one or more of the following items: NumInt, SCF. 

``NumInt``
   Output from the numerical integration procedure, like parameters, numbers of points generated, test data is controlled by the *numint* subkey (see below). The *repeat* subkey controls whether the output is repeated for all geometries (if the flag is on) or only for the first (if the flag is off). Some concise info is produced (repeatedly) anyway if the print switch computation is on. 

``SCF``
   Controls similarly the SCF output, like population analysis and orbital eigenvalues. If the flag is on, these items are printed at the last SCF cycle in every geometry, otherwise only at the last geometry. 

   By default both options are off. 

.. _EPRINT SCF: 

**SCF**

Output during the SCF procedure. 

::

   EPRINT
     SCF list
   END

``list``
   is a list of items, separated by blanks or commas. The following items are recognized: Eigval, Eigvec, Err, Fmat, Keeporb, MOPop, Occ, Pmat, Pop, Start. 

``Eigval``
   Eigenvalues of the one-electron orbitals at the last SCF cycle. In a run with multiple SCF runs (Geometry Optimization,..) this printing occurs only for the last SCF procedure. See also the eigval subkey of EPRINT. (Use the *repeat* subkey of EPRINT to get output for the last SCF procedure at each SCF run, use DEBUG SCFEIGVAL to get output on all SCF cycles). 

``Eigvec``
   MO eigenvector coefficients in the BAS representation. Only printed on the last SCF cycle. 

``Err``
   SCF error data which are checked for convergence. By default this takes effect after cycle 25 of the SCF. If the key is set it takes effect at the first cycle. Optionally one may type ErrN,where n is an integer (written directly after Err without a blank in between), in which case the key takes effect at cycle n. 

``Fmat``
   Fock matrix in the low representation. 

``Keeporb``
   If the KeepOrbitals option is activated (see the key SCF), output is generated whenever this option actually results in a change of occupation numbers as regards the energy ordering. 

``Occ``
   concise output of SCF occupation numbers on last SCF cycle if no eigenvalues are printed (see: Eigval). 

``moPop``
   Mulliken populations in terms of the elementary basis functions (bas), per MO, for input-specified MOs (see the EPRINT subkey *orbpop*) 

``Pmat``
   Density matrix 

``Pop``
   General control of bas Mulliken populations. This supervises all printing (whether populations are printed or not) according to the EPRINT subkeys *atompop, fragpop, orbpop* (the latter only as regards the bas population analysis at the end of the SCF procedure). 

``Start``
   Data pertaining to the *first* SCF cycle (of the *first* SCF procedure, in case of an optimization; use *repeat* to get this for *all* SCFs). 

By default Eigval, Keeporb, Occ, and Pop are on, the others off. 

.. _EPRINT SFO: 

**SFO**

Information pertaining to the use of Symmetrized Fragment Orbitals (for analysis purposes). 

::

   EPRINT
     SFO list
   END

``list``
   A list of items, separated by blanks or commas. The following items are recognized: eig, eigcf, orbpop, grosspop, fragpop, ovl. 

``Eig``
   The MO coefficients in terms of the SFOs. 

``Eigcf``
   idem, but now also containing the coefficients pertaining to the CoreFunctions. 

``OrbPop``
   population analysis of individual orbitals. The orbitals analyzed are set with the EPRINT subkey *orbpop*. 

``GrossPop``
   Gross populations of the SFOs, split out in symmetry representations. GrossPop is automatically turned on when OrbPop is activated. 

``FragPop``
   Population analysis on a per-FragmentType basis. This analysis does in fact not depend on the SFOs (ie, the result does not depend on how the SFOs are defined), but the computation of these populations takes place in the SFO-analysis module, which is why it is controlled by the SFO print option. FragPop output is given per orbital when OrbPop is activated, per symmetry representation when GrossPop is activated, and as a sum-over-all-orbitals-in-all-irreps otherwise (if FragPop is active). 

``Ovl``
   Overlap matrix of the SFO basis, separately for each symmetry representation. 

   By default orbpop is on, the other options off.

   In a Spin-Orbit calculation the SFO analysis is not yet implemented completely. 

*Remark*: the options eig and eigcf replace the previous (now disabled) simple print options eigsfo and eigsfo. 

Note that the simple print key SFO controls whether or not the EPRINT subkey *sfo* is effective at all. 

.. _EPRINT TF: 

**TransitionField**

Part of the bonding energy is computed and analyzed by the so-called Transition State procedure [#ref2]_,  [#ref3]_. This has nothing to do with physical transition states, but is related to the Fock operator defined by an average charge density, where the average is taken of the initial (sum-of-orthogonalized-fragments) and the final (SCF) charge density. There is also an analogous term where the average is taken of the sum-of-fragments and the sum-of-orthogonalized-fragments. Various terms, Fock operators and Density Matrices used in this approach may be printed. To avoid confusion with real Transition States (saddle points in the molecular Energy surface) the phrase TransitionField is used here. 

::

   EPRINT
     TF list
   END

``List``
   A list of items, separated by blanks or commas. The following items are recognized: Energy, Fmat, DiagFmat, FragPmat, DiagFragPmat, F*dPmat, DiagF*dPmat, OrbE. 

``Energy``
   Energy terms computed from the TransitionField. 

``Fmat``
   TransitionField Fock matrices. 

``DiagFmat``
   Idem, but only the diagonal elements. 

``FragPmat``
   The molecular P-matrix constructed from the sum-of-fragments. 

``DiagFragPmat``
   idem, but only the diagonal elements. 

``F*dPmat``
   The TransitionField energy term can be expressed as a Fock operator times the difference between two P-matrices (initial and final density). 

``DiagF*dPmat``
   only diagonal elements 

``OrbE``
   Orbital energies in the TransitionField. 

By default all options are off. 


Other Eprint subkeys
====================

We discuss now the remaining EPRINT sub keys that are not simple shortcuts for print switches. 

.. _EPRINT EIGVAL: 

::

   EPRINT
     Eigval noccup {nvirtual}
   END

This specifies the *number* of one-electron orbitals for which in the SCF procedure energies and occupation numbers are printed whenever such data is output: the highest noccup occupied orbitals and the lowest nvirtual empty orbitals. Default values are noccup=10, nvirtual=10. If only one integer is specified it is taken as the noccup value and nvirtual is assumed to retain its standard value (10). Printing can be turned off completely with the EPRINT sub key SCF, see above. 

**Mulliken Population Analysis**

.. _EPRINT ATOMPOP: 

All population subkeys of EPRINT refer to *Mulliken* type populations. 

::

   EPRINT
     ATOMPOP level
   END

Populations accumulated per atom. 

level must be none, gross or matrix. none completely suppresses printing of the populations; gross yields the gross populations; matrix produces the complete matrix of net and overlap populations. Default value: matrix. 

.. _EPRINT BASPOP: 

::

   EPRINT
     BASPop level
   END

Populations are printed per elementary (bas) basis function. The level options are none, short, gross, matrix. none, gross and matrix are as for atompop. 

short yields a summary of BAS gross populations accumulated per angular momentum (*l*) value and per atom. 

Default value: gross. 

.. _EPRINT FRAGPOP: 

::

   EPRINT
     FragPop level
   END

Completely similar to the atompop case, but now the populations per *fragment*. Of course in the case of single-atom fragments this is the same as atompop and only one of them is printed. Default: matrix. 


For all three population keys atompop, fragpop and baspop, specification of a higher level implies that the lower-level data, which are in general summaries of the more detailed higher level options, are also printed. 

Printing of any populations at the end of the SCF procedure is controlled with the EPRINT sub key *SCF* (pop). 


**Population Analysis per MO**

A very detailed population analysis tool is available: the populations *per orbital* (MO). The printed values are independent of the occupation numbers of the MOs, so they are not populations in a strict sense. The actual populations are obtained by multiplying the results with the orbital occupations. 

The analysis is given in terms of the SFOs and provides a very useful characterization of the MOs at the end of the calculation, after any geometry optimization has finished. This feature is now also available in a Spin-Orbit coupled relativistic calculation, in the case there is one scalar relativistic fragment, which is the whole molecule. 

The same analysis is optionally (see EPRINT subkey *SCF*, option mopop also provided in terms of the elementary basis functions (bas). 


::

   EPRINT
     OrbPop {noccup {nvirtual}} {tol=tol}
       subspecies orbitals
       subspecies orbitals
       ...
     subend
   END

``noccup``
   Determines how many of the highest occupied orbitals are analyzed in each irrep. Default noccup=10. 

``nvirtual``
   Determines in similar fashion how many of the lowest virtual orbitals are analyzed in each irrep. Default nvirtual=4. 

``tol``
   Tolerance parameter. Output of SFO contributions smaller than this tolerance may be suppressed. Default: 1e-2. 


``subspecies``
   One of the subspecies of the molecular symmetry group. Can not be used (yet) in a Spin-Orbit coupled calculation. 

``orbitals``
   A list of integers denoting the valence orbitals (in energy ordering) in this subspecies that you want to analyze. This overrules the noccup,nvirtual specification for that symmetry representation. In an unrestricted calculation two sequences of integers must be supplied, separated by a double slash (//). 

Any subset of the subspecies can be specified; it is not necessary to use all of them. No subspecies must occur more than once in the data block. This can not be used in a Spin-Orbit coupled equation (yet). 

A total SFO gross populations analysis (from a summation over the occupied MOs) and an SFO population analysis per fragment type are preformed unless *all* MO SFO-populations are suppressed. 

.. index:: reduction of output 

Reduction of output
===================

One of the strong points of ADF is the analysis in terms of fragments and fragment orbitals (SFOs) that the program provides. This aspect causes a lot of output to be produced, in particular as regards information that pertains to the SFOs. 

Furthermore, during the SCF and, if applicable, geometry optimizations, quite a bit of output is produced that has relevance merely to check progress of the computation and to understand the causes for failure when such might happen. 

If you dislike the standard amount of output you may benefit from the following suggestions: 

If you are not interested in info about progress of the computation:  

::

   NOPRINT Computation

If you'd like to suppress only the SCF-related part of the computational report: 

::

   NOPRINT SCF

If you don't want to see any SFO stuff:  

::

   NOPRINT SFO

To keep the SFO *definitions* (in an early part of output) but suppress the SFO-mo coefficients and the SFO overlap matrix: 

::

   EPRINT
    SFO noeig, noovl
   END

Note: the SFO-overlap matrix is relevant only when you have the SFO-MO coefficients: the overlap info is needed then to interpret the bonding/anti-bonding nature of the various SFO components in an MO. 

If you are not interested in the SFO *populations*: 

::

   EPRINT
    SFO noorbpop
   END


.. only:: html

  .. rubric:: References

.. [#ref1] L.\  Versluis, The determination of molecular structures by the HFS method, PhD thesis, University of Calgary, 1989

.. [#ref2] T.\  Ziegler and A. Rauk, *On the calculation of Bonding Energies by the Hartree Fock Slater method. I. The Transition State Method*, `Theoretica Chimica Acta 46, 1 (1977) <https://doi.org/10.1007/BF00551648>`__ 

.. [#ref3] T.\  Ziegler and A. Rauk, *A theoretical study of the ethylene-metal bond in complexes between copper(1+), silver(1+), gold(1+), platinum(0) or platinum(2+) and ethylene, based on the Hartree-Fock-Slater transition-state method*, `Inorganic Chemistry 18, 1558 (1979) <https://doi.org/10.1021/ic50196a034>`__ 
