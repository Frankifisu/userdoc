
Advanced charge density and bond order analysis
***********************************************

In addition to Mulliken charge analysis, ADF calculates several atomic charges that do not share the flaws of Mulliken (strong basis set dependence). The multipole-derived charge analysis exactly reproduces dipole and higher multipole moments of the molecule. Other charge analysis methods ('Voronoi deformation density' and 'Hirshfeld' provide atomic charges that agree well with chemical intuition. Nalewajski bond orders can be calculated and show good agreement with experimental trends and chemical intuition, even for transition metal compounds. 

Note that the amount of data can be regulated with the keys PRINT, NoPrint, EPrint and Debug. 


Charges, Populations
====================

**Mulliken populations**

See the input key  :ref:`EPRINT<keyscheme EPRINT>`. See also the  :ref:`section on Mulliken populations <results mulliken>`. 

**Hirshfeld charges, Voronoi deformation density**

No special input key required. See also the :ref:`section on Hirshfeld charges, Voronoi deformation density<results hirshfeld>`. 

**Multipole derived charges**

No special input key required. See also the  :ref:`section on MDC<MDC>`. 

**Charge model 5 (CM5)**

Charges calculated with CM5 activated by keyword 

.. _keyscheme CM5: 


::

   CM5

See also the  :ref:`section on CM5<CM5>`. 

Only one of the charges above can be returned to the AMS driver, in case charges are needed at the driver level or explicitly requested with ``Properties%Charges`` in the AMS driver input. The choice for which charge analysis scheme is used for the returned charges in made with the ``AtomicChargesTypeForAMS`` keyword.

.. scmautodoc:: adf AtomicChargesTypeForAMS


.. index:: bond order 
.. index:: Mayer bond order
.. _bond_roders_input:

Bond orders
===========


The calculation of bond orders can be requested at the AMS driver level (see the `Properties section of the AMS driver manual <../../AMS/Properties.html>`__)::

   $AMSBIN/ams << eor
   ...
   Properties 
      BondOrders Yes
   End

   Engine ADF
      ...
   EndEngine
   eor

By default, bond orders are computed using the Nalewajski-Mrozek [#ref3]_ [#ref4]_ [#ref39]_ [#ref40]_ [#ref41]_ method. There exist three alternative definitions of the valence and bond order indices within the Nalewajski-Mrozek approach. By default the values obtained from partitioning of Tr(P :math:`\Delta` \P) (i.e. Nalewajski-Mrozek-3) are calculated and printed in the output. For more information on alternative Nalewajski-Mrozek bond order indices see (see also: :ref:`section on bond order analysis<BONDORDERS>`). 


In the ``Engine ADF`` part of the input, you can specify the following options:

.. scmautodoc:: adf BondOrders


The bond order analysis is based on SFOs. The symmetry used in the calculation should be ``NOSYM``. The bond analysis may be used also for multi-atomic fragments. The fragment-fragment bond orders are printed in such a case. Note that in the present implementation all fragment types should be different. 

Mayer bond orders and Mulliken atom-atom populations per l-value can be enabled using the ``ExtendedPopan`` key:

.. scmautodoc:: adf ExtendedPopan


See also the :ref:`section on bond order analysis<BONDORDERS>`. 

.. index:: ETS-NOCV 
.. index:: NOCV 
.. index:: NOCV-Hirshfeld
.. _NOCV: 

ETS-NOCV: Natural Orbitals for Chemical Valence
===============================================

With the ETS-NOCV charge and energy decomposition scheme the deformation density is partitioned into the different components (:math:`\sigma`, :math:`\pi`, :math:`\delta`) of the chemical bond. The energy contributions to the total bond energy is calculated for each specific orbital interactions between fragments, giving insight in the orbital interactions also for non-symmetric molecules. The ETS-NOCV analysis offers a compact quantitative picture of the chemical bond, which is also qualitatively attractive to chemists. 

.. tip::
  See also the `EDA-NOCV tutorial <../../Tutorials/Analysis/EDA.html#eda-nocv>`__ 

The Natural Orbitals for Chemical Valence (NOCV) approach has been derived from the  Nalewajski-Mrozek valence theory  [#ref3]_,  [#ref4]_.  From the mathematical point of view, each NOCV  :math:`\psi`\ :sub:`i`  is defined as an eigenvector of the deformation density matrix  in the basis of fragment orbitals.  

.. math::

   \Delta P \Psi_i = \nu_i \Psi_i

Thus, the deformation density :math:`\Delta`:math:`\rho` can be expressed in the NOCV representation  as a sum of pairs of complimentary eigenfunctions (:math:`\psi_{-k}`, :math:`\psi_k`)  corresponding to eigenvalues -:math:`\nu`\ :sub:`k`  and :math:`\nu`\ :sub:`k`  with the same  absolute value but opposite signs: 

.. math::

   \Delta \rho (r) = \sum \Delta \rho_k (r) = \sum \nu_k \left(  -\Psi^2_{-k} (r) + \Psi^2_{k} (r)   \right)


here, k goes over the pairs of NOCV's. 

In the combined ETS-NOCV scheme the orbital interaction term :math:`\Delta E_\text{orb}`   is expressed in terms of NOCV's as  [#ref5]_,  [#ref6]_: 

.. math::

   \Delta E_\text{orb} = \sum \Delta E_k^\text{orb} = \sum \nu_k \left( -F^\text{TS}_{-k} + F^{TS}_k \right)

here, :math:`-F^\text{TS}_{-k}` and :math:`F^{TS}_k` are diagonal transition-state  Kohn-Sham matrix elements corresponding to NOCV's with eigenvalues -:math:`\nu`\ :sub:`k`  and :math:`\nu`\ :sub:`k` , respectively. The advantage of this expression is that usually only a few complimentary NOCV pairs  significantly contribute to the total :math:`\Delta E_\text{orb}`. Another advantage of this approach  is that not only can each :math:`\Delta \rho_k (r)` be visualized but there is also a  well defined bonding energy contribution :math:`\Delta E_k^\text{orb}` corresponding to it. 

**Remarks**

The ETS-NOCV analysis is often not very useful when atomic fragments are used. No symmetry must be used  in the final calculation, thus, use a Symmetry NOSYM keyword if your molecule is symmetric.  The analysis is not completely implemented for meta-GGA's and meta-hybrids. 

Improvements in ADF2012 to both the ETS and NOCV analysis with hybrids. ETS: Now the exact exchange contribution to the Pauli term is isolated and the contributions to the orbital term are divided among orbital symmetries. NOCV: The exact exchange contribution to the Fock operator is included when calculating energy contributions. These changes do not apply to meta-hybrids. 

**Usage**

In order to perform the ETS-NOCV analysis, the following two keywords must be specified at the same time: 

.. _keyscheme ETSNOCV: 


::

   ETSNOCV 
      {RHOKMIN rhokmin}
      {EKMIN ekmin}
      {ENOCV enocv}
   End
   PRINT {ETSLOWDIN | ETSLOWDIN-Unrestricted}

``ETSNOCV``
   The ETSNOCV keyword specifies thresholds for printing of NOCV-related information. All three arguments are optional and when all three are omitted only the NOCV's corresponding to eigenvalues abs :math:`(\nu_k) \geq 0.05` are included in the analysis.  

   ``RHOKMIN``
      The threshold for population analysis of each deformation density contribution  in terms of individual SFO's. 

   ``EKMIN``
      The threshold for orbital interaction energy contributions corresponding to  deformation density components originating from each NOCV-pairs.  

   ``ENOCV``
      The threshold for NOCV-eigenvalues. 

``PRINT {ETSLOWDIN | ETSLOWDIN-Unrestricted}``
   Only one of the two PRINT options is supposed to be used to activate printing of ETS-NOCV results.  The choice depends on the bonding situation. 

   ``ETSLOWDIN``
      If one is interested in a description of bonding between closed-shell molecular fragments, then  'PRINT ETSLOWDIN' keyword must be used. In such a case one set of NOCV's originating from the  total deformation density matrix :math:`\Delta P = ( \Delta P_\alpha + \Delta P_\beta)` will be printed out. See the example of carbene bonding between closed shell CH2 and Cr(CO)5.  

   ``ETSLOWDIN-Unrestricted``
      If, however, one is interested in a description of bonding between open-shell molecular fragments  then the 'PRINT ETSLOWDIN-Unrestricted' keyword must be used. In this case two sets of NOCV's originating from :math:`\Delta P_\alpha` and :math:`\Delta P_\beta`  will be printed out.  See the example of CH3-CH3 bonding between two CH3 radicals with opposite spins.  This option must also be used when one wants to analyze bonding in a molecule with unpaired electrons. 

``PRINT NOCVHirshfeld``
   The NOCVs can be integrated per fragment using the Hirshfeld partitioning scheme. Using these integrals, one can distinguish between inter- and intra-fragment NOCVs. An inter-fragment NOCV has non-zero integral Hirshfeld :math:`\Delta Q` value and corresponds to a charge transfer between fragments. An intra-fragment NOCV has a small :math:`\Delta Q` value and corresponds to polarization of the fragments. When 'PRINT NOCVHirshfeld' is specified, the :math:`\int{\Delta \rho} = -\Delta Q` values per NOCV are printed to the output file in the "Hirshfeld partitioning" table at the end of the ETS-NOCV section. 

.. index:: NBO-analysis 
.. index:: adfnbo 
.. index:: gennbo 
.. _NBO: 

Adfnbo, gennbo: NBO analysis
============================

* :download:`(PDF) NBO manual<../download/nbo6_manual.pdf>`

Dr. Autschbach, SCM, and Prof. Weinhold have collaborated to prepare a simple in put file generator, called adfnbo, for the GENNBO program of Prof. Weinholds Natural Bond Orbital (NBO) package. In ADF2013 and later the NBO 6.0 version is supported  `http://nbo6.chem.wisc.edu <http://nbo6.chem.wisc.edu>`__. 

The GENNBO executable is included in the ADF distribution and can be enabled via the license file for all those who buy an NBO license from SCM ( `info@scm.com <mailto:info@scm.com>`__). An extensive documentation of GENNBO is part of the NBO manual. The application of ADFNBO to frozen-core basis sets needs to be further tested. Usage can be found below and in the Examples Document. 

Next a brief summary of the capabilities of GENNBO is given (by Prof. Weinhold). GENNBO implements most capabilities of the full NBO 6.0 program suite as described on the NBO website:  `http://nbo6.chem.wisc.edu <http://nbo6.chem.wisc.edu>`__ These include determination of natural atomic orbitals (NAOs), bond orbitals (NBOs), and localized MOs (NLMOs), as well as the associated NPA (atomic charges and orbital populations) and NRT (resonance structures, weightings, bond orders) valence descriptors, for a wide variety of uncorrelated and correlated (variational, perturbative, or density functional) theoretical levels. GENNBO-supported options include all keywords except those explicitly requiring interactive communication with the host electronic structure system (viz., $DEL deletions, NEDA, NCS, NJC). The GENNBO program typically sits conveniently on the PC desktop, ready to analyze (or re-analyze at will, with altered options) the final results of a complex ADF calculation performed on a remote cluster. 

GENNBO "communicates" with the original ADF calculation through an archive file (JOB.47 file, preserving all necessary details of the final density) that is initially generated by ADF and subsequently becomes the input file for GENNBO. The .47 file contains a standard $NBO ... $END keylist that can be edited with a standard word processor or text editor to include chosen NBO keyword options, just as though they might have appeared in the original input stream of an interactive ADFNBO run. The stand-alone GENNBO program therefore allows many alternative NBO analysis options to be explored at leisure, without costly re-calculation of the wave function. 

In ADF2018 the NBO 6.0 version6 in the ADF distribution is updated to the March 2017 version, see also
`http://nbo6.chem.wisc.edu <http://nbo6.chem.wisc.edu>`__:
"The 14-Mar-2017 distribution includes a number of other features of interest to general NBO users:
The default NAO search algorithm has been modified to better preserve core-valence separation in rare cases where numerical near-degeneracies can lead to unphysical core-valence mixing. The numerical effects are generally negligible except where they become necessary. The "OLDNAO" keyword restores the legacy NAO algorithm for comparison purposes."

This new NAO method may change the NBO analysis of some properties (EFG, NMR) quite substantially, especially individual contributions.

**Usage**

ADF needs to write some data to file, which is done by including FULLFOCK, AOMAT2FILE, SAVE TAPE15, and SYMMETRY NOSYM in the input file for ADF.
An all electron basis set is needed.
Use the key 'spherical' in the adfnbo input.
A file named FILE47 is generated by adfnbo which is an input file for the general NBO program gennbo6.
Thus the usage is like

::

   $AMSBIN/ams <<eor
   ...
   Engine ADF
      Basis
        ...
        Core None
      End
      FullFock
      AOMat2File
      Save TAPE15
      Symmetry Nosym
   EndEngine
   eor

   $AMSBIN/adfnbo <<eor
      write
      fock
      spherical
      end input
   eor

   $AMSBIN/gennbo6 FILE47



.. _NBO_PROPERTIES: 

NBO analysis of EFG, NMR chemical shifts, NMR spin-spin coupling
----------------------------------------------------------------

For certain molecular properties it is possible to perform detailed analyses in terms of Natural Bond Orbitals (NBOs) and Natural Localized Molecular Orbitals (NLMOs). These features generally require a sequence of ADF and/or property code runs. An initial non-relativistic or scalar relativistic ADF run, followed by the generation of NBO and NLMO data, is required, and the resulting data files need to be present in subsequent property calculations, along with a keyword indicating that the NBO analysis is requested in the property module. 

We have noted in the past some slight loss of numerical accuracy of the results after going through the various orbital transformations in the NBO - NLMO sequence. It is important that the user verifies in each case that the total contributions from the analysis are in agreement with the total calculated property, within the numerical integration accuracy limits. In order to assist the user with this, the analysis program always print the total analysis contributions, including small non-printed values. 

Moreover, there appears to be a problem with the analysis of the Fock matrix in the NBO program in conjunction with ADF calculations. Therefore please do NOT use the Fock matrix second order perturbation theory analysis in NBO at this time. We will remove this disclaimer once the issue has been fixed. Applications of the NBO-NLMO property analysis codes have so far given no indication that the Fock matrix issue interferes with the analysis. 

Important note: If properties are analyzed from within spin-orbit relativistic computations, the NBO/NLMO analysis is performed in terms of scalar (spin-free) relativistic orbitals, as detailed in the technical references. The results from these analyses are exact in the sense that they fully reproduce the final spin-orbit property result, and they allow to dissect the property in terms of more intuitive one component real scalar relativistic localized orbitals. Typically, the property analysis in a spin-orbit calculation involves contributions from unoccupied scalar NLMOs, whereas there are no such contributions if a non-relativistic or scalar relativistic property is analyzed. 

Available properties for NBO analysis: EFG, NMR chemical shifts and NMR spin-spin coupling. 

**NBO analysis of EFG**

EFGs: non-relativistic and scalar ZORA, in ADF/AOResponse. Requires initial ADF run with 

::

   AOresponse
    donothing
   End

in order to generate orbitals that re equivalent to those generated in the subsequent ADF run where the EFG is calculated. Alternatively, simply calculate the EFG twice, once before the NBO generation step, and once afterward. 

The next step (see below) is to create the NBOs and the required data files for the analysis. Afterward, in the second ADF run, use 

::

   Aoresponse
    efg NUC nbo
   end

``efg NUC nbo``
   Here NUC is the number of the nucleus at which the EFG is to be computed (ADF internal atom ordering). Example: efg 1 nbo. 

The threshold for printing the EFG-NBO contributions to output can be adjusted via the ``Tresh`` options. The default is 0.05, which means that only orbitals with absolute value contribution larger than 5% of the total EFG are printed. To increase the number of contributions printed, specify a smaller threshold. For example::

   Aoresponse
      efg 1 nbo Tresh 0.01
   end

In addition to the optional NBO analysis, the EFG program in AOResponse prints a Mulliken type analysis of the EFG principal components, and an analysis in terms of canonical MOs. 

**WARNING**: The ordering of the principal components is lowest to highest including the sign. That is, we have :math:`V11 \leq V22 \leq V33`. This does not conform to the usual convention of :math:`|V11| \leq |V22| \leq |V33|`. Please make sure you select the right component for your analysis. 

Example job: $AMSHOME/examples/adf/AlCl3_efgnbo. For an explanation of the output and a general usage tutorial, see [#ref7]_. Further references and recommended citations, see [#ref8]_. 

**NBO analysis of NMR Chemical shift**

An implementation is currently available for spin-orbit ZORA computations. If scalar ZORA calculations are to be analyzed, provide the input keyword 

::

   FAKESO

in the NMR input (outside of the 'nmr' keyword). If this feature is requested one should restrict the calculation to a single shielding tensor per NMR run. It would be good practice to check the results against regular NMR calculations where the analysis feature is not requested. No ZORA scaling is applied in the analysis results. The data should be equivalent to a regular computation in the NMR input with 

::

   NMR
    u1k best
    calc all
   END

Depending on whether scalar or spin-orbit calculations are to be analyzed, the sequence of calculations is different: 

**scalar**: 

1. ADF, scalar ZORA, symmetry NOSYM, closed shell
2. generate NBOs and required data files for analysis 
3. NMR with FAKESO and analysis keywords, use adf.rkf (previously known as TAPE21), TAPE10 from step 1. 

**spin-orbit**: 

1. ADF, scalar ZORA, closed shell
2. generate NBOs and required data files for analysis 
3. delete adf.rkf, TAPE10, TAPE15
4. ADF, spin-orbit ZORA, symmetry NOSYM, closed shell
5. NMR with analysis keywords, using adf.rkf, TAPE10 from step 4

In the NMR run, in addition to the NMR keyword, provide the following 

::

   analysis
    print 0.01
    canonical
    nbo
    components
   end

The optional canonical keyword can be used independently from the NBO analysis features. It enables an analysis of the shielding in terms of the canonical MOs. The components keyword is optional and enables an analysis not only of the isotropic shielding but also of each principal component of the tensor. The print keyword selects printout of contributions relative to the total diamagnetic, paramagnetic. In the example, only contributions greater than 1% are printed. Set to zero to print ALL contributions. 

Example job: $AMSHOME/examples/adf/CH4_nmrnbo. References [#ref42]_ [#ref43]_ [#ref44]_. 

**NBO analysis of NMR spin-spin coupling (J-coupling)**

Non-relativistic, scalar ZORA, spin-orbit ZORA 

The sequence of jobs is similar to those in the NMR section. 

**scalar** or **non-relativistic**: 

1. ADF, scalar ZORA or nonrel. 
2. generate NBOs and required data files for analysis 
3. CPL with analysis keyword, use adf.rkf (previously known as TAPE21), TAPE10 from step 1. 

**spin-orbit**: 

1. ADF, scalar ZORA 
2. generate NBOs and required data files for analysis 
3. delete adf.rkf, TAPE10, TAPE15
4. ADF, spin-orbit ZORA 
5. CPL with analysis keyword, using adf.rkf, TAPE10 from step 4

In the CPL run provide the following 'contributions' keyword to enable the analysis 


::

   nmrcoupling
      ... other options
      contributions 1E19 nbo
   end

The numerical value selects a print threshold in SI units of T**2/J for the analysis. Increase the value to obtain less detail in the analysis. By default, 'contributions' triggers an analysis of the J-coupling in terms of canonical MOs. The nbo keyword enables in addition the NBO-NLMO analysis. 

Please note that due to the history of how the program was developed the output from the scalar/nrel. analysis and from the spin-orbit calculations differs somewhat. The qualitative content is the same. 

In scalar ZORA or non-relativistic CPL calculations without the SD term an orbital based analysis is only performed for the Fermi-contact mechanism. If you also need an analysis for the PSO and SD mechanisms but do not want to run a spin-orbit calculation with ADF please use the SD or NOSD keywords which will cause the spin-orbit branch of the CPL code to be used. In ZORA spin-orbit calculations the FC, SD, PSO, and cross terms are analyzed together by default. You can selectively switch them on or off in order to get individual mechanism analyses. The DSO mechanism is often negligible. An analysis tool for this mechanism has therefore not yet been developed. 

Example job: $AMSHOME/examples/adf/CPL_CH3OH_NBO. References NMR spin-spin couplings with NBO analysis [#ref44]_ [#ref45]_ [#ref46]_ [#ref47]_:

**Generation of NBOs**

How to generate the NBOs, NLMOs, and the data files needed for these calculations (step 2 below is step 2 in the examples above): 

1. run ADF with scalar ZORA or non-relativistic options, and keep adf.rkf and TAPE15.  

::

   AMS_JOBNAME=Scalar $AMSBIN/ams <<eor
     ...
   eor

2. 

::

   # run adfnbo in WRITE  mode to create the gennbo input file FILE47
   # and one of the required property analysis files, adfnbo.kf
   
   $AMSBIN/adfnbo << eor
    ADFfile Scalar.results/adf.rkf
    TAPE15file Scalar.results/TAPE15
    write
    spherical
   eor
   
   rm -f adfnbo.37 adfnbo.39 adfnbo.49 adfnbo.48
   $AMSBIN/gennbo6 << FILE47
   
   # run adfnbo in COPY mode to create the second property analysis
   # file, adfnbo2.kf
   
   $AMSBIN/adfnbo <<  eor
    ADFfile Scalar.results/adf.rkf
    TAPE15file Scalar.results/TAPE15
    spherical
    copy
   eor
   
   # run adfnbo in READ mode: prepare locorb on TAPE21
   
   $AMSBIN/adfnbo <<  eor
    ADFfile scalar.results/adf.rkf
    TAPE15file scalar.results/TAPE15
    spherical
    read
   eor
   
   rm -f adfnbo.37 adfnbo.39 adfnbo.49 adfnbo.48
   
   # keep the adf.rkf after this sequence in order to
   # be able to plot the NBOs and NLMOs with amsview
   
   # clean up, keep adfnbo*.kf for any NBO property analyses.

.. index:: Bader analysis 
.. index:: AIM 
.. index:: QTAIM 
.. index:: atoms in molecules 
.. index:: Fukui descriptors
.. index:: conceptual DFT descriptors
.. index:: LI-DI matrix
.. index:: dual descriptor domains

QTAIM: Atoms in Molecules
=========================

One can calculate local and atomic properties using a real-space partition of the electronic density. It is based on the quantum theory of atoms in molecules (QTAIM) developed by Richard Bader [#ref9]_. Another possibility for Bader analysis is to use the adf2aim utility with a third party program such as Xaim.

Local, atomic, and non-local properties
---------------------------------------

.. _BADER: 
.. _QTAIM: 

The QTAIM input block replaces the *Bader* keyword. The former *Bader Reactivity* option now corresponds to the new *ConceptualDFT* block (see below).

The QTAIM functionality encompasses two different but related features: topology analysis of the electron density gradient field [#ref10]_, and calculation of the condensed atomic properties by integrating various local functions over atomic basins [#ref48]_ [#ref49]_. These calculation can also be used for relatively large systems (hundreds of atoms). The topology analysis is performed at all levels of the analysis and it produces a list of the molecule's electron density critical points and bond paths that can be visualized by the AMSview GUI module. Besides, the following properties at the critical points are calculated: electron density, its Laplacian and Hessian matrix, ellipticity, Jenkins' metallicity index [#ref12]_, reduced density gradient, DFT energy density variation rates [#ref13]_, and Abramov's local energy components [#ref14]_. At the *Extended* analysis level the following condensed atomic properties are calculated: atomic charges, integral of the density Laplacian, dipole and quadrupole moments, Shannon and Renyi entropies, spatial distribution of the molecular orbitals over atomic basins. If the *Energy* keyword is specified, also the atomic energies [#ref11]_ are calculated. At the *Full* level, also the atom-atom matrix elements of the localization (LI) and delocalization (DI) indices [#ref50]_ [#ref51]_ are computed. 


.. _keyscheme QTAIM: 

.. scmautodoc:: adf QTAIM AnalysisLevel Energy AtomsToDo Spacing
   :nosummary:
   :noref:

Note that the accuracy of condensed atomic properties can be estimated by integrating the Laplacian of the electron density over a given basin, which, ideally, must vanish. The accuracy of the method can be improved by using a larger integration grid (NumericalQuality). Usually, the default grid is sufficient to achieve the accuracy of 10\ :sup:`-3` a.u. (differences of milliHartree in the energies). Unfortunately, the convergence of the electron density Laplacian integral with the grid size is not monotonous. Therefore this type of Bader atomic property calculation should be considered for applications where computational efficiency is critical and moderate accuracy is sufficient. 

.. Note::
   The *Energy* keyword requires calculation of the total energy so it has the same limitations as the *TotalEnergy* keyword. For example, it is not compatible with relativistic calculations. The electron density topology analysis, however, *is* possible for all-electron scalar-relativistic calculations as was shown in [#ref15]_. 

.. Note::
   Atomic energies are correct only at equilibrium geometries (the virial theorem is used).

.. _ADF2AIM: 
.. index:: adf2aim 

ADF2AIM
-------

The ADF utility adf2aim (original name rdt21) developed by Xavi Lopez, Engelber Sans and Carles Bo converts an ADF adf.rkf (formerly known as TAPE21) to WFN format (for Bader analysis) 

The program rdt21 is now called adf2aim and is part of the ADF package. 

The WFN file is an input file for the third party program Xaim (see  `http://www.quimica.urv.es/XAIM <http://www.quimica.urv.es/XAIM>`__ for details), which is a graphical user interface to programs that can perform the Bader analysis. Usage of adf2aim can be found in the Examples Document. 


.. Aromaticity
.. index:: aromaticity
.. index:: Iring aromaticity index
.. index:: MCI aromaticity index

Aromaticity index with QTAIM
----------------------------

The cyclic delocalization of mobile electrons in two or three dimensions is probably one of the key aspects that characterize aromatic compounds.
However, aromaticity cannot be measured directly by any physical or chemical experiment because it is not a well-defined magnitude.
One can define indicators of aromaticity, some of which are implemented in ADF.
The matrix of localization/delocalization indices (LI-DI) and the following from it Iring (ring index) and MCI (multi center index) aromaticity indices 
(see Ref. [#ref16]_) 
can be computed for rings specified by the user. The rings are specified using the AROMATICITY input block, one line per ring. 
For example, for a benzene molecule where atoms 1-6 are carbon atoms the input would look like this:

.. _keyscheme AROMATICITY:

::

   AROMATICITY
     1 2 3 4 5 6
   END

The program does not check whether the atoms in the AROMATICITY input block are connected so it is responsibility of the user 
to specify them correctly. Moreover, for the Iring index to be calculated correctly the atoms must be listed in the order they are 
connected in the ring.

Calculation of the aromaticity indices invokes the QTAIM analysis automatically and uses its results so all accuracy considerations 
for the QTAIM key above are also valid here. This feature requires that the calculation is performed without symmetry (Symmetry NOSYM).

Results of the calculation are printed to the output under the "Aromaticity Index" header. The first table presents the total number of 
electrons per atom and their breakdown in "localized" and "delocalized". Note: the total number of electrons per atom 
:math:`N_{total} = N_{loc} + N_{deloc} / 2` since delocalized electrons are counted twice. The second table presents the Iring and 
MCI ring indices for each ring specified in the AROMATICITY block. These results (and the original LiDi matrix from which they are 
computed) are stored in the Properties section in the t21 file.

.. _ConceptualDFT:

Conceptual DFT
==============

Global, atomic, and non-local descriptors
-----------------------------------------

The *ConceptualDFT* block replaces and extends the set of features behind the *Bader Reactivity* keyword found in the ADF versions before ADF2019. The frontier molecular orbital (FMO) approximation is used for all calculations. Orbital degeneracy is taken into account following Martinez [#ref17]_. All these descriptors are described in Ref. [#ref18]_. Which exactly descriptors are calculated depends on the *AnalysisLevel* key:

* *Normal:* global conceptual DFT descriptors, i.e. electronic chemical potential, electronegativity (its opposite), hardness and softness, hyperhardness [#ref19]_, electrophilicity index [#ref20]_, dissociation energies (nucleofuge and electrofuge, see Ref. [#ref21]_), electrodonating and electroaccepting powers [#ref22]_ and the net electrophilicity [#ref23]_. Also, new global descriptors called *global dual descriptors* :math:`\Delta f+` and :math:`\Delta f-` are calculated [#ref24]_, which correspond to the spatial integral of the positive (electrophilic) or negative (nucleophilic) regions of the original dual descriptor, respectively. These descriptors allow for comparing total reactivity of molecules, in contrast with Fukui functions or original dual descriptor that integrate over the whole space to 1 or 0 for all molecules. 
* *Extended:* both global and atomic properties, including condensed (QTAIM) descriptors in both canonical and grand canonical ensembles. More precisely, the following properties are computed: condensed Fukui functions [#ref26]_, dual descriptor [#ref25]_ [#ref27]_ and some of their composite functions [#ref52]_ [#ref53]_ [#ref54]_, as well as condensed local electrophilicity and nucleophilicity [#ref28]_.
* *Full:* all properties are calculated, including non-local ones, such as the condensed linear response function [#ref29]_ and the softness kernel [#ref30]_.

Please note that atomic electronegativities [#ref31]_ are calculated separately with an optional *Electronegativity* keyword. In contrast with other properties, it requires all-electron basis sets and triggers the *TotalEnergy* keyword.

.. _keyscheme ConceptualDFT: 

.. scmautodoc:: adf ConceptualDFT AnalysisLevel Electronegativity AtomsToDo
   :nosummary:
   :noref:

For more information about *Conceptual DFT*, we suggest the reading of these excellent reviews: Refs. [#ref33]_ and [#ref32]_.
   
Domains of the dual descriptor
------------------------------
   
In a recent paper [#ref34]_, Tognetti et al. proposed a real-space partitioning scheme of the dual descriptor (DD) into chemically meaningful *reactivity domains*. Basically, a predominantly electrophilic (nucleophilic) DD domain constitutes a region of space where this function remains positive (negative). They can be visualized using the GUI and quantitative information can be obtained using the additional *Domains* key block.

.. Note::
      This analysis requires that the calculation is performed without symmetry (Symmetry NOSYM)

.. scmautodoc:: adf ConceptualDFT Domains
   :nosummary:
   :noref:



.. _DAMQT:
.. index:: adf2damqt

adf2damqt: DAMQT interface
==========================

Interface (adf2damqt) to the 3rd party DAMQT 2.0 package [#ref35]_, which can analyze the electron density in molecules, and related quantities.
DAMQT includes the method of deformed atoms in molecules (DAM).
The DAMQT 2.0 package is described in Ref. [#ref35]_.
In the ADF calculation TAPE15 and adf.rkf need to be saved.
The executable adf2damqt can be run with up to three optional arguments.
If no argument is supplied, "ADF" is chosen as default root name (fname) for files generated by the interface,
and files containing electron density matrix (fname.den) and molecular orbitals (fname.SLorba and, eventually, fname.SLorbb) will be created in a format suitable to be read by DAMQT.

::

   $AMSBIN/ams << eor
   ...
   Engine ADF
      ...
      SAVE TAPE15
   EndEngine
   eor
   mv ams.results/adf.rkf TAPE21
   mv ams.results/TAPE15 TAPE15
   $AMSBIN/adf2damqt {fname {SPIN} {NOORBITALS}}

``fname``
  If a specific name is desired for the files (fname), it must be supplied as first optional argument,
  provided that the name does not coincide with any of the two additional options SPIN and NOORBITALS.

``SPIN``
  SPIN: for storing spin density matrix in fname.den file (instead of total electron density, which is the default).

``NOORBITALS``
  NOORBITALS: to prevent generation of files with molecular orbitals (by default orbitals are generated).

  SPIN and NOORBITALS are case insensitive and can be given in any order (but always after optional fname when required).


.. _FOD:
.. index:: FOD
.. index:: fractional orbital density

FOD: fractional orbital density
===============================

Following the analysis method by Grimme and Hansen (Ref. [#ref37]_)
a fractional occupation number weighted electron density (FOD) can be plotted with AMSview.
The scalar field is obtained by finite-temperature DFT calculations with pre-defined electronic temperature :math:`T_{el}`,
typically :math:`T_{el}` =5000 K, and for hybrids :math:`T_{el}` =20000*(amount of HF exchange)+5000, see Ref. [#ref37]_.
This analysis tool can be used to determine whether static electron-correlation effects are important.

::

   OCCUPATIONS ELECTRONICTEMPERATURE=5000

The NFOD (integrated FOD) is written in the output of ADF.
The FOD can be visualized with AMSview.
The contour surface value in AMSview should be set to 0.005 (:math:`e/(bohr)^3`).


.. only:: html

  .. rubric:: References

.. [#ref1] I.\  Mayer, *Charge, bond order and valence in the ab initio SCF theory*, `Chemical Physics Letters 97, 270 (1983) <https://doi.org/10.1016/0009-2614(83)80005-0>`__ 

.. [#ref2] M.S. Gopinathan and K. Jug, *Valency. I. A quantum chemical definition and properties*, `Theoretica Chimica Acta 1983 63, 497 (1983) <https://doi.org/10.1007/BF00552652>`__ 

.. [#ref3] A.\  Michalak, R.L. De Kock and T. Ziegler, *Bond Multiplicity in Transition-Metal Complexes: Applications of Two-Electron Valence Indices*, `Journal of Physical Chemistry A 112, 7256 (2008) <https://doi.org/10.1021/jp800139g>`__ 

.. [#ref4] R.F. Nalewajski, J. Mrozek and A. Michalak, *Two-electron valence indices from the Kohn-Sham orbitals*, `International Journal of Quantum Chemistry 61, 589 (1997) <https://doi.org/10.1002/(SICI)1097-461X(1997)61:3%3C589::AID-QUA28%3E3.0.CO;2-2>`__ 

.. [#ref5] M.\  Mitoraj, A. Michalak and T. Ziegler, *A Combined Charge and Energy Decomposition Scheme for Bond Analysis*, `Journal of Chemical Theory and Computation 5, 962 (2009) <https://doi.org/10.1021/ct800503d>`__ 

.. [#ref6] M.\  Mitoraj, A. Michalak and T. Ziegler, *On the Nature of the Agostic Bond between Metal Centers and Beta-Hydrogen Atoms in Alkyl Complexes. An Analysis Based on the Extended Transition State Method and the Natural Orbitals for Chemical Valence Scheme (ETS-NOCV)*, `Organometallics 28, 3727 (2009) <https://doi.org/10.1021/om900203m>`__ 

.. [#ref7] J.\  Autschbach, S. Zheng, and R.W. Schurko, *Analysis of Electric Field Gradient Tensors at Quadrupolar Nuclei in Common Structural Motifs*, `Concepts in Magnetic Resonance Part A 36A, 84 (2010) <https://doi.org/10.1002/cmr.a.20155>`__ 

.. [#ref8] A.J. Rossini, R.W. Mills, G.A. Briscoe, E.L. Norton, S.J. Geier, I. Hung, S. Zheng, J. Autschbach, and R.W. Schurko, *Solid-State Chlorine NMR of Group IV Transition Metal Organometallic Complexes*, `Journal of the American Chemical Society 131, 3317 (2009) <https://doi.org/10.1021/ja808390a>`__ 

.. [#ref9] P.L.A. Popelier, *Atoms in Molecules An Introduction*, Pearson Education, Harlow, 2000.

.. [#ref10] J.I. Rodríguez, *An Efficient Method for Computing the QTAIM Topology of a Scalar Field: The Electron Density Case*, `Journal of Computational Chemistry 34, 681 (2013) <https://doi.org/10.1002/jcc.23180>`__ 

.. [#ref11] J.I. Rodríguez, .W. Ayers, A.W. Götz, and F.L. Castillo-Alvarado, *Virial theorem in the Kohn-Sham density-functional theory formalism: Accurate calculation of the atomic quantum theory of atoms in molecules energies*, `Journal of Chemical Physics 131, 021101 (2009) <https://doi.org/10.1063/1.3160670>`__

.. [#ref12] P.W Ayers, S. Jenkins, *Bond metallicity measures*, `Comput. Theor. Chem. 1053, 112 (2015) <https://doi.org/10.1016/j.comptc.2014.10.040>`__.

.. [#ref13] V.\  Tognetti, L. Joubert, *Density functional theory and Bader's atoms-in-molecules theory: towards a vivid dialogue*, `Phys. Chem. Chem. Phys. 16, 14539 (2014) <https://doi.org/10.1039/C3CP55526G>`__.

.. [#ref14] Y.A. Abramov, *On the Possibility of Kinetic Energy Density Evaluation from the Experimental Electron-Density Distribution*, `Acta Cryst. A53, 264 (1997) <https://doi.org/10.1107/S010876739601495X>`__.

.. [#ref15] J.S.M. Anderson, J.I. Rodriguez, P.W. Ayers, and A.W. Götz, *Relativistic (SR-ZORA) Quantum Theory of Atoms in Molecules Properties*, `Journal of Computational Chemistry 82, 81 (2017) <https://doi.org/10.1002/jcc.24520>`__. 

.. [#ref16] F.\  Feixas, E. Matito, J. Poater and M. Sola, *Quantifying aromaticity with electron delocalisation measures*, `Chem. Soc. Rev. 44, 6434 (2015) <https://doi.org/10.1039/c5cs00066a>`__

.. [#ref17] J.\  Martínez, *Local Reactivity Descriptors from Degenerate Frontier Molecular Orbitals*, `Chem. Phys. Lett. 478, 310-322 (2009) <https://doi.org/10.1016/j.cplett.2009.07.086>`__ 

.. [#ref18] G.\  Hoffmann, V. Tognetti and L. Joubert, *Can molecular and atomic descriptors predict the electrophilicity of Michael acceptors?*, `J. Mol. Model. 24, 281 (2018) <https://doi.org/10.1007/s00894-018-3802-9>`__.

.. [#ref19] C.\  Morell, A. Grand, A. Toro-Labbé, *Is hyper-hardness more chemically relevant than expected ?*, `J. Mol. Model. 19, 2893 (2013) <https://doi.org/10.1007/s00894-013-1778-z>`__

.. [#ref20] R.G. Parr, L.v. Szenpály, S. Liu, *Electrophilicity index*, `J. Am. Chem. Soc. 121, 1922 (1999) <https://doi.org/10.1021/ja983494x>`__

.. [#ref21] P.W. Ayers, J.S.M. Anderson, J.I. Rodrigueza, Z. Jaweda, *Indices for predicting the quality of leaving groups*, `Phys. Chem. Chem. Phys. 7, 1918 (2005) <https://doi.org/10.1039/b500996k>`__

.. [#ref22] J.L. Gázquez, A. Cedillo, A. Vela, *Electrodonating and electroaccepting powers*, `J. Phys. Chem. A 111, 1966 (2007) <https://doi.org/10.1021/jp065459f>`__

.. [#ref23] P.K. Chattaraj, A. Chakraborty, S. Giri, *Net electrophilicity*, `J. Phys. Chem. A 113, 10068 (2009) <https://doi.org/10.1021/jp904674x>`__

.. [#ref24] F.\  Guégan, P. Mignon, V. Tognetti, L. Joubert, C. Morell, *Dual descriptor and molecular electrostatic potential: complementary tools for the study of the coordination chemistry of ambiphilic ligands*, `Phys. Chem. Chem. Phys. 16, 15558 (2014) <https://doi.org/10.1039/c4cp01613k>`__

.. [#ref25] F.\  Zielinski, V. Tognetti, L. Joubert, *Condensed descriptors for reactivity: A methodological study*, `Chem. Phys. Lett. 527, 67 (2012) <https://doi.org/10.1016/j.cplett.2012.01.011>`__.

.. [#ref26] R.G. Parr, W.T. Yang, *Density functional approach to the frontier-electron theory of chemical reactivity*, `J. Am. Chem. Soc. 106, 4049 (1984) <https://doi.org/10.1021/ja00326a036>`__

.. [#ref27] C.\  Morell, A. Grand, A. Toro-Labbé, *New Dual Descriptor for Chemical reactivity*, `J. Phys. Chem. A 109, 205 (2005) <https://doi.org/10.1021/jp046577a>`__

.. [#ref28] C.\  Morell C. , J.L. Gázquez, A. Vela, F. Guégan, H. Chermette, *Revisiting electroaccepting and electrodonating powers: proposals for local electrophilicity and local nucleophilicity descriptors*, `Phys. Chem. Chem. Phys. 16, 26832 (2014) <https://doi.org/10.1039/c4cp03167a>`__

.. [#ref29] P.\  Geerlings, S. Fias, Z. Boisdenghien, F. De Proft, *Conceptual DFT: chemistry from the linear response function*, `Chem. Soc. Rev. 43, 4989 (2014) <https://doi.org/10.1039/C3CS60456J>`__.

.. [#ref30] S.\  Fias, F. Heidar-Zadeh, P. Geerlings, P.W. Ayers, *Chemical transferability of functional groups follows from the nearsightedness of electronic matter*, `PNAS 114, 11633 (2017) <https://doi.org/10.1073/pnas.1615053114>`__

.. [#ref31] V.\  Tognetti, C. Morell, L. Joubert, *Atomic electronegativities in molecules*, `Chem. Phys. Lett. 635, 111 (2015) <https://doi.org/10.1016/j.cplett.2015.05.057>`__.

.. [#ref32] P.\  Geerlings, F. de Proft, W. Langenaecker, *Conceptual Density Functional Theory*, `Chem. Rev. 103, 1793 (2003) <https://doi.org/10.1021/cr990029p>`__.

.. [#ref33] H.\  Chermette, *Chemical reactivity indexes in density functional theory*, `J. Comput. Chem. 20, 129 (1999) <https://doi.org/10.1002/(SICI)1096-987X(19990115)20:1%3C129::AID-JCC13%3E3.0.CO;2-A>`__

.. [#ref34] V.\  Tognetti, C. Morell, L. Joubert, *Quantifying electro/nucleophilicity by partitioning the dual descriptor*, `J. Comput. Chem. 36, 649 (2015) <https://doi.org/10.1002/jcc.23840>`__.

.. [#ref35] R.\  López, J.F. Rico, G. Ramírez, I. Ema, D. Zorrilla, *DAMQT 2.0: A new version of the DAMQT package for the analysis of electron density in molecules*, `Computer Physics Communications 192, 289 (2015) <https://doi.org/10.1016/j.cpc.2015.02.027>`__ 

.. [#ref37] S.\  Grimme and A. Hansen, *A Practicable Real-Space Measure and Visualization of Static Electron-Correlation Effects*, `Angewandte Chemie International Edition 54, 12308 (2015) <https://doi.org/10.1002/anie.201501887>`__ 

.. [#ref39] R.F. Nalewajski and J. Mrozek, *Modified valence indices from the two-particle density matrix*, `International Journal of Quantum Chemistry 51, 187 (1994) <https://doi.org/10.1002/qua.560510403>`__ 

.. [#ref40] R.F. Nalewajski, J. Mrozek and A. Michalak, *Exploring Bonding Patterns of Molecular Systems Using Quantum Mechanical Bond Multiplicities*, `Polish Journal of Chemistry 72, 1779 (1998) <http://ichf.edu.pl/pjch/pj-1998/pj07s98.htm#1779>`__ 

.. [#ref41] R.F. Nalewajski, J. Mrozek and G. Mazur, *Quantum chemical valence indices from the one-determinantal difference approach*, `Canadian Journal of Chemistry 74, 1121 (1996) <https://doi.org/10.1139/v96-126>`__ 

.. [#ref42] J.\  Autschbach, *Analyzing NMR shielding tensors calculated with two-component relativistic methods using spin-free localized molecular orbitals*, `Journal of Chemical Physics 128, 164112 (2008) <https://doi.org/10.1063/1.2905235>`__ 

.. [#ref43] J.\  Autschbach and S. Zheng, *Analyzing Pt chemical shifts calculated from relativistic density functional theory using localized orbitals: The role of Pt 5d lone pairs*, `Magnetic Resonance in Chemistry 46, S45 (2008) <https://doi.org/10.1002/mrc.2289>`__ 

.. [#ref44] J.\  Autschbach and S. Zheng, *Relativistic computations of NMR parameters from first principles: Theory and applications*, `Annual Reports on NMR Spectroscopy 67, 1 (2009) <https://doi.org/10.1016/S0066-4103(09)06701-5>`__ 

.. [#ref45] J.\  Autschbach, *Analyzing molecular properties calculated with two-component relativistic methods using spin-free Natural Bond Orbitals: NMR spin-spin coupling constants* `Journal of Chemical Physics 127, 124106 (2007) <https://doi.org/10.1063/1.2768363>`__ 

.. [#ref46] J.\  Autschbach and B. Le Guennic, *Analyzing and interpreting NMR spin-spin coupling constants from molecular orbital calculations*, `Journal of Chemical Education 84, 156 (2007) <https://doi.org/10.1021/ed084p156>`__ 

.. [#ref47] A.M.A. Boshaala, S.J. Simpson, J. Autschbach and S. Zheng, *Synthesis and Characterization of the Trihalophosphine Compounds of Ruthenium* [RuX\ :sub:`2` (:math:`\eta`\ :sup:`6` -cymene)(PY\ :sub:`3` )] (X = Cl, Br, Y = F, Cl, Br) and the Related PF\ :sub:`2` (NMe\ :sub:`2` ) and P(NMe\ :sub:`2` )\ :sub:`3` Compounds; Multinuclear NMR Spectroscopy and the X-ray Single Crystal Structures of [RuBr\ :sub:`2` (:math:`\eta`\ :sup:`6` -cymene)(PF\ :sub:`3` )], [RuBr\ :sub:`2` (:math:`\eta`\ :sup:`6` -cymene)(PF\ :sub:`2` {NMe\ :sub:`2` })], and [RuI\ :sub:`2` (:math:`\eta`\ :sup:`6` -cymene)(P{NMe\ :sub:`2` }\ :sub:`3` )], `Inorganic Chemistry 47, 9279 (2008) <https://doi.org/10.1021/ic800611h>`__ 

.. [#ref48] J.I. Rodríguez, A.M. Köster, P.W. Ayers, A. Santos-Valle, A. Vela and G. Merino, *An efficient grid-based scheme to compute QTAIM atomic properties without explicit calculation of zero-flux surfaces*, `Journal of Computational Chemistry 30, 1082 (2009) <https://doi.org/10.1002/jcc.21134>`__ 

.. [#ref49] J.I. Rodríguez, R.F.W. Bader, P.W. Ayers, C. Michel, A.W. Götz and C. Bo, *A high performance grid-based algorithm for computing QTAIM properties*, `Chemical Physics Letters 472, 149 (2009) <https://doi.org/10.1016/j.cplett.2009.02.081>`__ 

.. [#ref50] X.\  Fradera, M.A Austen, *The Lewis model and beyond*, R.F.W. Bader, `J. Phys. Chem. A 103, 304 (1999) <https://doi.org/10.1021/jp983362q>`__.

.. [#ref51] J.\  Poater, M. Solà, M. Duran, X. Fradera, *The calculation of electron localization and delocalization indices at the Hartree–Fock, density functional and post-Hartree–Fock levels of theory*, `Theor. Chem. Acc. 107, 362 (2002) <https://doi.org/10.1007/s00214-002-0356-8>`__.

.. [#ref52] A.\  Toro-Labbé, P. Jaque, J.S. Murray and P. Politzer, *Connection between the average local ionization energy and the Fukui function*, `Chem. Phys. Lett. 407, 143 (2005) <https://doi.org/10.1016/j.cplett.2005.03.041>`__

.. [#ref53] J.\  Padmanabhan, R. Parthasarathi, M. Elango, V. Subramanian, B.S. Krishnamoorthy, S. Gutierrez-Oliva, A. Toro-Labbé, D. R. Roy, P. K. Chattaraj, *Multiphilic descriptor for chemical reactivity and selectivity*, `J. Phys. Chem. A 111, 130 (2007) <https://doi.org/10.1021/jp0718909>`__

.. [#ref54] P.K. Chattaraj, B. Maiti, U. Sarkar, *Philicity: A unified treatment of chemical reactivity and selectivity*, `J. Phys. Chem. A 107, 4973 (2003) <https://doi.org/10.1021/jp034707u>`__
