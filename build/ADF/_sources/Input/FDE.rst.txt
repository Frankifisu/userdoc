.. _FDE: 
.. index:: frozen-density embedding 
.. index:: Wesolowski-Warshel FDE 
.. index:: subsystem DFT 
.. index:: FDE 



FDE: Frozen Density Embedding
=============================

The Frozen-Density-Embedding (FDE) option invokes calculation of the effective embedding potential introduced by Wesolowski and Warshel [#ref1]_ in order to take into account the effect of the environment on the electronic structure of an embedded system. The embedding potential (Eq. 3 in Ref. [#ref5]_) depends  explicitly  on electron densities corresponding to the embedded subsystem (e.g. a solvated molecule) and its environment (e.g. solvent). For a detailed review, see Ref. [#ref3]_. The ADF implementation of the method is described in detail in Ref. [#ref2]_ [#ref4]_.

A time-dependent linear-response generalization of this embedding scheme was derived in Ref. [#ref7]_. Its implementation in an approximate form, which assumes a localized response of the embedded system only (uncoupled FDE), is described in the supplementary material to Ref. [#ref8]_. For possible drawbacks and pitfalls in connection with this approximation, see Refs. [#ref2]_ [#ref9]_ [#ref10]_. 

The theory of coupled excited states for subsystems is described in Refs. [#ref74]_ [#ref72]_, and extended for general response properties in Ref. [#ref11]_. This theory (subsystem TDDFT, coupled FDE) allows to treat the mutual response of several subsystems, including the ones that are considered environment. 

A generalization of the FDE scheme to the calculation of NMR shieldings has been given in Ref. [#ref12]_, where also the approximations involved and possible problems are discussed.  

With the exception of interaction energies, the current implementation in ADF only allows the calculation of molecular properties that only depend on the electron density and of response properties using TDDFT. For an application to the calculation of several molecular properties in solution and a comparison to the DRF model also available in ADF, see Ref. [#ref9]_. For further applications of the ADF implementation, see Ref. [#ref14]_ (weakly interacting complexes), Refs. [#ref2]_ [#ref9]_ [#ref79]_ [#ref80]_ (solvent effects), and Refs. [#ref81]_ [#ref82]_ (other environment effects). 

.. _keyscheme FDE:

To invoke a frozen-density embedding calculation, two additional specifications in the input are required. First, one or more frozen fragments have to be included in the FRAGMENTS block, and second, the block key FDE has to be included.  In the simplest case, this input should look like this::

   FRAGMENTS
      ...
      FragType FragFile type=FDE
      ...
   END
   
   FDE
      PW91K
   end

In the FRAGMENTS block, for any fragment it is possible to specify the option type=FDE to indicate that the density of this fragment is kept frozen. This density is imported from the file FragFile. The frozen fragments have to be included in addition to the usual, non-frozen fragments. The atoms of the frozen fragments have to be included in the ATOMS block. As with normal fragments, the fragment found in the file will be rotated and translated to its position specified in the ATOMS block.  For more details on specifying fragments, see the section 'fragment files'.  In the FDE input block, the recommended PW91k (also known as GGA97) approximant is recommended for the non-additive kinetic energy (the default is the local density approximant).  A recommended alternative is NDSD. For all other options the defaults will be used. 

Please note that throughout the FDE part of the documentation, the word "approximant" is used instead of the more usual "functional" to emphasize that the exact functional is not known, also in the case of the kinetic energy functional. In the literature one may encounter both words used interchangeably.  

By including more than one frozen fragment, it is possible to use a frozen fragment that  is a superposition of the densities of isolated molecules (this was possible in the previous version of ADF using the DENSPREP option). For a discussion and tests of the use of such approximate environment densities, see Ref. [#ref2]_. 

There is no restriction on the use of symmetry in FDE calculations, and usually the correct symmetry will be detected automatically. However, in the preparation of frozen fragments that will be rotated and/or translated in the FDE calculation, one has to include the keyword NOSYMFIT for technical reasons. 

In the current implementation, only the electron density of the embedded (non-frozen) system is  calculated. Therefore, with the exception of interaction energies, only properties that depend directly on the electron density  (e.g. dipole moments) are available. In particular, the calculation of  energy gradients is not implemented yet. All quantities given in the output refer (unless  explicitly specified otherwise) to the non-frozen system only. 

To employ the extension of FDE to the calculation of NMR shieldings, the file TAPE10 has to be used in 
the FDE calculation (by including the option SAVE TAPE10), and  subsequently the NMR shielding has to be calculated using the program NMR (not with EPR).  
The TDDFT extension of the FDE formalism allows the calculation of electronic excitation  energies and polarizabilities. This extension is automatically activated if FDE is used  in combination with the EXCITATIONS or the RESPONSE key. To allow the mutual response of several subsystems, see the section on [:ref:`subsystem TDDFT <subsystem TDDFT>`]. 


Fragment-specific FDE options
-----------------------------

For each frozen fragment, several additional options can be applied. To do this, the fragment specification is used as a subblock key by appending a & sign. The subblock is terminated with SubEnd. This subblock key looks, in the most general form, as follows: 

::

   FRAGMENTS
     ... 
     FragType FragFile type=FDE &
        {FDEOPTIONS [USEBASIS] [RELAX or FREEZEANDTHAW] [OPTIMIZE]}
        {FDEDENSTYPE [SCF | SCFexact | SCFfitted ]}
        {RELAXCYCLES n or FREEZEANDTHAWCYCLES n}
        {XC [LDA | GGA ggapotx ggapotc | MODEL SAOP]}
     SubEnd
     ...
   END

``FDEOPTIONS``
   ``FDEOPTIONS USEBASIS``
      If the USEBASIS option is specified, the basis functions of this frozen fragment will be included in the calculation of the embedded subsystem.   This allows to expand the density of the embedded subsystem using not only atom-centered basis sets localized in the embedded subsystem but also the ones in the environment Ref. [#ref18]_. In large-scale simulations using the embedding potential, this option is recommended to be used in the preparation stage to investigate the basis set dependence of the results (chapter 5.3 in Ref. [#ref3]_). This option is also an indispensable element in the procedure introduced in Ref. [#ref18]_ to test approximants to the kinetic-energy component of the embedding potential introduced by Wesolowski and Warshel. 

   ``FDEOPTIONS RELAX or FREEZEANDTHAW``
      If the RELAX option (or equivalent FREEZEANDTHAW option) is specified, the density of this frozen fragment will be relaxed in freeze-and-thaw cycles [#ref5]_, i.e., the embedded subsystem is frozen, while this fragment is thawed. This is repeated, until convergence is reached or until the maximum number  of iterations has been performed. By relaxing frozen fragments, it is possible to improve a given approximate environment density by including the polarization of the environment due to the embedded system. This option is recommended to be used in the preparation stage of a large-scale numerical simulation. The freeze-and-thaw calculations lead to a pair of electron densities (embedded system and environment) that minimizes the total energy. As a consequence, the electron density of the environment derived from the freeze-and-thaw calculations can be used as a reference to verify the adequacy of the assumed electron density for the environment in a large-scale simulation. Due to technical restrictions, freeze-and-thaw is not possible if an open-shell (unrestricted) fragment is present. 

   ``FDEOPTIONS USEBASIS RELAX or FDEOPTIONS USEBASIS FREEZEANDTHAW``
      It is further possible to combine USEBASIS and RELAX or FREEZEANDTHAW. In this case, the basis functions of the non-frozen fragment will be included when the density of the fragment is relaxed. This allows fully relaxed calculations with supermolecular expansion of the electron density of each subsystem. This option is to be used to test approximants to the kinetic-energy component of the embedding potential introduced by Wesolowski and Warshel by means of the procedure introduced in ref. [#ref18]_. 

   .. ``FDEOPTIONS OPTIMIZE``
   ..    If the key ``FDEOPTIONS OPTIMIZE`` is not specified, then only the active fragment is optimized in a Geometry Optimization run (the FDE fragments are not optimized).
   ..    If you include ``FDEOPTIONS OPTIMIZE``, then the corresponding FDE fragment will also be optimized. 
   ..    The ``OPTIMIZE`` key implicitly activates the option ``RELAX``, which is necessary to evaluate the nuclear gradients of the respective fragment [Ref. [#ref21]_.
   ..    The ``OPTIMIZE`` key only supports mono-molecular basis set expansions and can therefore NOT be combined with the ``USEBASIS`` option.
   ..    For Geometry Optimizations the usage of the ``FULLGRID`` option is recommended.

   ..    **Note**:: When performing :ref:`geometry optimization<keyscheme GEOMETRY>` ICW FDE one must:

   ..    - Disable :ref:`symmetry <appendix symmetry>` (``Symmetry NOSYM``)
   ..    - Use the :ref:`old optimizer branch<keyscheme GEOMETRY>` (``Branch Old``)
   ..    - Use Cartesian coordinates in the :ref:`optimization procedure<keyscheme GEOMETRY>` (``Optim Cartesian``)


``FDEDENSTYPE``
   The FDEDENSTYPE option can be used to specify which density is read from the fragment file. The possible options are: 

   ``FDEDENSTYPE SCF (or FDEDENSTYPE SCFexact)``
      The exact density (not calculated using the fit functions) is used. This is the default. 

   ``FDEDENSTYPE SCFfitted``
      The fitted density is used. This is less accurate but can be significantly faster.  

``RELAXCYCLES n or FREEZEANDTHAWCYCLES n``
   This gives the maximum number of freeze-and-thaw cycles that are performed for this fragment. If the maximum number given in the FDE block is smaller, or if convergence is reached earlier, then fewer cycles are performed. For historical reasons, two equivalent keywords are available. 

``XC``
   The XC option can be used to select the exchange-correlation potential that is used for this fragment when it is relaxed. By default, the same potential as for the non-frozen system is used, but in some cases it might be preferable to use another approximation for certain fragments. An example is given in Ref. [#ref14]_. 

   ``XC LDA``
      This option selects LDA as exchange-correlation potential for relaxing this fragment. 

   ``XC GGA ggapotx ggapotc``
      This selects a GGA potential for relaxing this fragment. The GGA potential is specified by giving the name of the exchange potential, followed by the name of the correlation potential.  The available potentials are listed in the documentation for the XC key. 

   ``XC MODEL SAOP``
      This selects the model potential SAOP for relaxing this fragment. 

Kinetic energy approximants
---------------------------

The approximants to the kinetic energy dependent component of the embedding potential are described here. 


::

   FDE
     {approximants to the kinetic energy dependent
                   component of the embedding potential}
     {CJCORR [rho_cutoff]}
     {GGAPOTXFD exchange approximant}
     {GGAPOTCFD correlation approximant}
   end

``approximants to the kinetic energy dependent component of the embedding potential``
   Several approximants to the kinetic-energy-dependent component of the  effective potential given in Eq. (21) of ref. [#ref1]_ are available. None of them is applicable if the embedded system is covalently bound to its environment. The user is recommended to look at the numerical value of the TSNAD(LDA) parameter which is given in the units of energy and can be considered as a measure of the overlap. The following rule of thumb should be applied: if this parameter is smaller than the estimated interaction energy between the embedded subsystem and the environment, then the available approximants are most probably adequate. If it exceeds this limit, the results can be less reliable.  Printing TSNAD(LDA) is not done by default, as it can be quite time-consuming. Its printing is switched on by including "EXTPRINTENERGY", and "PRINTRHO2", and "FULLGRID" in the FDE input block.  If no kinetic energy approximant is specified, by default the local-density approximation (Thomas-Fermi approximant) is used. For an assessment of approximants for weakly overlapping pairs of densities see Refs. [#ref18]_ [#ref26]_ [#ref24]_ [#ref27]_. Based on these studies, the use of PW91k (= GGA97) is recommended. 

   **APPROXIMANTS TO BE USED IN NORMAL APPLICATIONS** 

   ``THOMASFERMI (default)``
      Local-density-approximation form of vt[rhoA,rhoB] [#ref30]_  derived from Thomas-Fermi expression for Ts[rho] [#ref28]_ [#ref29]_. 

   ``GGA97 (or PW91K)``
      Generalized-gradient-approximation form of vt[rhoA,rhoB] [#ref26]_ derived from the  Lembarki-Chermette [#ref32]_ approximant to Ts[rho]. This approximant is currently the recommended one based on the numerical analysis of its accuracy [#ref24]_ [#ref26]_  and the fact that the used enhancement factor disappears at large reduced density gradients, i.e. where the second-order gradient-expansion approximation fails [#ref18]_ [#ref27]_. 

   ``NDSD``
      Similarly to GGA97, the NDSD approximant is constructed by taking into account the asymptotic behavior of the functional vt[rhoA,rhoB] at small density gradients. In the construction of NDSD, the exact property of vt[rhoA,rhoB] at rho_A :math:`\rightarrow` 0 and for :math:`\int` rhoB = 2 given in Eq. A6 of Ref. [#ref36]_ is also taken into account. The analysis of the accuracy of this potential [#ref36]_ shows that NDSD is of the same or superior quality as GGA97. NDSD is, therefore, recommended as the successor of GGA97 to be used anywhere where the quality of the results depends directly on the accuracy of the potential vt[rhoA,rhoB], i.e., for obtaining electronic-structure-dependent properties. The analytical form of the corresponding approximant to the functional  Ts\ :sup:`nad`  [\rho_A,\rho_B]$ exists (Eq. 23 in Ref. [#ref36]_). It is not possible, however, to obtain the analytical form of the  corresponding parent functional for the kinetic energy Ts[rho]. To reflect this and the fact that, similarly to the GGA approximants to vt[rhoA,rhoB], the numerical values of only first- and second derivatives  of density are needed, the label NDSD (Non-Decomposable Second Derivatives) is used.  

   **OBSOLETE APPROXIMANTS** (can be used but GGA97 leads usually to a better embedding potential see refs. [#ref18]_ [#ref26]_) 

   ``LLP91``
      Generalized-gradient-approximation form of vt[rhoA,rhoB] [#ref18]_ derived from Lee-Lee-Parr [#ref39]_ approximant to Ts[rho]. 

   ``PW86k``
      Generalized-gradient-approximation form of vt[rhoA,rhoB] [#ref18]_ derived from the Fuentealba-Reyes approximant to Ts[rho] [#ref42]_. 

   ``THAKKAR92``
      Generalized-gradient-approximation form of vt[rhoA,rhoB] [#ref26]_ derived from the Thakkar approximant to Ts[rho] [#ref43]_. 

   **APPROXIMANTS WHICH MIGHT BE USEFUL ONLY FOR THEORY DEVELOPMENT** 

   The accuracy of **some** of these approximants was investigated in detail [#ref26]_ [#ref18]_  [#ref24]_ [#ref27]_.  Each of them was shown to lead to a qualitatively incorrect embedding potential. They shouldn't be used in practical applications. 

   ``COULOMB``
      Neglecting completely vt[rhoA,rhoB] (vt[rhoA,rhoB] equals zero) together with the exchange-correlation component of the embedding potential introduced by Wesolowski and Warshel.  

   ``TF9W``
      The approximant to vt[rhoA,rhoB]  [#ref1]_ derived from the second-order gradient expansion [#ref42]_ for Ts[rho]. 

   ``WEIZ``
      The approximant to vt[rhoA,rhoB]  [#ref27]_ derived from the von Weizsäcker approximant to Ts[rho] [#ref7]_. 

   ``OL91A``
      Generalized-gradient-approximation form of vt[rhoA,rhoB] [#ref18]_ derived from the first  Ou-Yang and Levy approximant to Ts[rho] [#ref53]_. 

   ``OL91B``
      Generalized-gradient-approximation form of vt[rhoA,rhoB] [#ref26]_ derived from the second  Ou-Yang and Levy approximant to Ts[rho] [#ref53]_. 

   ``E00``
      Generalized-gradient-approximation form of vt[rhoA,rhoB]  [#ref57]_ derived from a kinetic energy functional by Ernzerhof [#ref58]_ which represents the gradient expansion approximation up to the fourth order. 

   ``P92``
      Generalized-gradient-approximation form of vt[rhoA,rhoB] [#ref57]_ derived from a kinetic energy functional by Perdew [#ref60]_ which represents the gradient expansion approximation up to the sixth order. 

   **LONG DISTANCE CORRECTIONS TO THE EFFECTIVE POTENTIAL** 

``CJCORR``
   Option to switch on a long-distance correction. By default this option is not used. As was shown in Ref. [#ref61]_, with the available approximate kinetic-energy approximants, the embedding potential has the wrong form in  the limit of a large separation of the subsystems. In particular, it was shown that this can have serious consequences in the case of "supermolecular expansion of electron density of each subsystem" calculations (USEBASIS option). In Ref. [#ref61]_, a correction is proposed that enforces the correct long-distance limit. (See also this reference for limitations of this correction.) 

   ``CJCORR [rho_cutoff]``
      This option switches on the long-distance correction. This option has to be used in combination with one of the above kinetic-energy approximants. By default, a density cut-off of 0.1 is employed. 

   **NONADDITIVE EXCHANGE-CORRELATION APPROXIMANT** 

``GGAPOTXFDGGAPOTCFD``
   Option to specify the non-additive exchange-correlation approximant. By default, in the construction of the effective embedding potential the exchange-correlation approximant that was specified in the XC block is used. It is possible to specify a different approximant with the GGAPOTXFD and GGAPOTCFD options. This is particularly useful in combination with the use of model potentials like SAOP, that can not be used in the embedding potential because of their orbital  dependence. (For a discussion, see Ref. [#ref14]_.) 

   ``GGAPOTXFD exchange approximant``
      The exchange approximant is used in the construction of the embedding potential. The same exchange approximants as in the XC key are available. 

   ``GGAPOTCFD correlation approximant``
      The correlation approximant is used in the construction of the embedding potential. The same correlation approximants as in the XC key are available. 

General FDE options
-------------------

In addition to the fragment-specific options and the kinetic energy approximants, there are also a number of options available  in FDE calculations that will be described in the following. 

::

   FDE
     {FULLGRID}
     {RELAXCYCLES n or FREEZEANDTHAWCYCLES n}
     {RELAXPOSTSCF or FREEZEANDTHAWPOSTSCF}
     {EXTPRINTENERGY}
     {PRINTRHO2}
     {ENERGY}
     {SDFTENERGY}
     {DIPOLE}
   end

``FULLGRID``
   By default, FULLGRID is not used, and in FDE calculations the integration grid is generated as described in Ref. [#ref2]_ by including only atoms of the frozen subsystem that are close to the embedded subsystem in the generation of the integration grid. The distance cutoff used is chosen automatically, based on the extent of the basis functions of the embedded subsystem. (It can also be chosen manually, see the option qpnear in the INTEGRATION key) This scheme results in an efficient and accurate integration grid. However, it is possible that the default integration scheme is not accurate enough. This can be the case for weakly interacting systems and when the distance between the frozen and the embedded  system is large. It is therefore recommended to check the quality of the default integration grid by comparing to results obtained using the full supermolecular grid (FULLGRID option). 

   If the subkey FULLGRID is included, all atoms of the frozen system are included in the generation of the integration grid. This results in the same grid that would be  used in a supermolecular calculation of the combined frozen and embedded  system. The integration grid generated by this option might be much larger than the default grid.  This option should be used to check the quality of the default integration grid. 

``RELAXCYCLES n or FREEZEANDTHAWCYCLES n``
   Specifies the maximum number n of freeze-and-thaw iterations [#ref5]_ that are performed (for frozen fragments with the RELAX) option. If a smaller number of iterations is specified as a fragment-specific option, for this fragment this smaller number is used. Furthermore, if convergence is reached earlier, no more iterations will  be performed. 

``RELAXPOSTSCF or FREEZEANDTHAWPOSTSCF``
   If this option is included, several post-SCF properties will be calculated after each freeze-and-thaw cycle [Ref.  [#ref5]_.  These are otherwise only calculated in the last cycle. 

``EXTPRINTENERGYPRINTRHO2``
   If the options EXTPRINTENERGY and PRINTRHO2 are included (both are needed and should be listed on separate lines),  several additional quantities will be printed, including TSNAD(LDA). In order to obtain meaningful numbers, also the FULLGRID keyword (see above) has to be used. 

.. index:: FDE energy 

``ENERGY``
   Option to switch on the calculation of the FDE energy as the sum of the energy E[rhoA] of the active, embedded system and the interaction energy Eint[rhoA,rhoB] of the embedded system with the frozen environment. This relies on the calculation of the total energy for the embedded system and all caveats and restrictions for total energy evaluations apply (see keyword :ref:`TOTALENERGY<totalenergy>`). All energy contributions are evaluated on the grid of the active subsystem. Some contributions to the interaction energy Eint[rhoA,rhoB] require an accurate integration grid in the region of the environment. Thus, in pure embedding calculations (without fragment-specific option RELAX), an accurate calculation of the FDE energy requires a full supermolecular integration grid (FULLGRID option). Details on the implementation and the performance of kinetic energy functionals for interaction energies are documented in Ref. [#ref57]_ 

   The calculation of the full, variationally minimized subsystem DFT energy, that is, the sum of the energy of two subsystems E[rhoA] and E[rhoB] and their interaction energy Eint[rhoA,rhoB] in the framework of FDE, is invoked if then the fragment densities are relaxed in freeze-and-thaw cycles (option RELAXCYCLES and fragment-specific FDE option RELAX). In this case the supermolecular integration grid is not required. Instead, in each step of the freeze-and-thaw cycle, the critical energy terms are taken from the previous freeze-and-thaw step of the presently frozen fragment. The convergence of the energy contributions with the number of freeze-and-thaw iterations should be carefully monitored. Due to conceptual problems for the evaluation of the non-additive kinetic energy contribution, only two subsystems, that is, one frozen fragment, is supported for FDE energy calculations with freeze-and-thaw.
   
``SDFTENERGY``
   This is a generalization of the original ENERGY implementation that allows for the evaluation of the FDE/sDFT total energy.
   Usage of a supermolecular integration grid is recommended (FULLGRID option), because of the non-additive kinetic and XC contributions.
   EXTPRINTENERGY can be combined with this option to print the subsystem DFT energy after each freeze-and-thaw cycle.
   For pure embedding calculations, the SDFTENERGY implementation reads the total energy from each frozen fragment's adf.rkf (TAPE21) file.
   The total energy of frozen fragments is not (re-)evaluated during FDE calculations.
   It is therefore mandatory to add the :ref:`TOTALENERGY<totalenergy>` keyword to the preparatory isolated fragment calculations.

``DIPOLE``
   The dipole of the supersystem is calculated as the sum of analytically integrated fragment dipole moments.
   Note that the dipole moment becomes origin dependent for charged (sub-)fragments.
   The current implementation does NOT take care of this.

.. _FDE EO:

Frozen Density Embedding with External Orthogonality
----------------------------------------------------

An implementation of External Orthogonality (EO)  into the FDE framework in ADF can be found in Ref. [#ref67]_.
In this method in the fragment calculation one need to specify ghost atoms at the positions of the atoms in all the other fragments.
Thus each fragment is calculated in the supermolecular basis.

::

   AOMat2File
   IgnoreOverlap
   FDE
     EXTERNALORTHO {factor} 
     ...
   END

``EXTERNALORTHO``
   Used to specify the use of external orthogonality (EO) in the FDE block, with an optional factor (default factor is 1e6). Note that the overlap region is defined by
   ghost atoms, and the general keyword IGNOREOVERLAP is necessary. Additionally, the general keyword  AOMAT2FILE  is required to save some important fragment AO matrices to adf.rkf for use in an EO calculation.  it is recommended that one uses the  STOFIT keyword for the STOFIT density fitting method.

.. _FDE and COSMO:
.. index:: localized COSMO

FDE and (localized) COSMO
-------------------------

COSMO solvation can be included in combination with FDE.
This means that a COSMO cavity will be created that holds both the active and frozen fragments.

For very large systems the solution of the COSMO equations can become the bottleneck of the calculation. 
A local COSMO variant, which exploits the subsystem nature of the underlying electronic description, is implemented in ADF, see
Ref. [#ref68]_.
This method, called LoCOSMO, is an approximation to regular COSMO for fragment-based electronic structure methods.
If a given fragment is active (i.e. only its own density changes over the SCF cycles), the surface charges outside a given radius around this fragment will be kept fixed in magnitude (excluded from the COSMO optimization).
However, no interactions are ignored by adding a corresponding constant term to the COSMO solution vector. 

::

   SOLVATION
     ..
     CHARGED LoCosmo LoCosmoDist
   END

``LoCosmo LoCosmoDist``
   If LoCosmo is included the local COSMO will be used in the calculation. LoCosmoDist is a cutoff radius (Angstrom), which must be specified by the user, if LoCOSMO is included. All surface charges within this radius from any atom of the active fragment are included in the active charge space. A sensible value for LoCosmoDist is 5.0 Angstrom.

To be really useful, Freeze-and-Thaw cycles should be carried out with LoCOSMO. After each fragment calculation, the KF file LOCSURCH is written to disk. If present, this file will be automatically read in during the next (LoCOSMO) fragment calculation. This means that if the internal FT cycles are used by specifying RELAXCYCLES, the code creates and reads in the file in a fully automatic fashion. LOCSURCH is neither created nor read during a regular COSMO calculation. 

In case one calculates excitation energies with the EXCITATION block key, and LoCOSMO is specified, only the solvent response due to surface charges within the specified cutoff radius will be taken into account, see also Ref. [#ref69]_.
It should be noted that in a regular (uncoupled) FDE TDDFT calculation, the response due to the frozen density is neglected.


.. index:: FDE and QM/FQ(Fμ)
.. _FDE and QM/FQ(Fμ):

FDE and QM/FQ(Fμ)
-----------------

FDE can also be combined with the :ref:`QM/FQ(Fμ)<FQQM>` method which can be used to embed a quantum system in a polarizable classical environment.
The fluctuating classical layer can be included in all stages of an FDE calculation, i.e. when performing the separate calculations for the two isolated fragments as well as the full FDE system.
There is also the possibility of using the QM/FQ(Fμ) method to account for the mutual response of the subsystems by endowing the frozen layer's atoms with fluctuating charges (and dipoles), provided a suitable parametrization is available.
See the :ref:`QM/FQ(Fμ)<FQQM>` manual page for more details.


.. index:: subsystem TDDFT 
.. _subsystem TDDFT:

Subsystem TDDFT, coupled FDE
----------------------------


The linear-response subsystem TDDFT code implements the theory of coupled excited states for subsystems as described in Refs. [#ref74]_ [#ref72]_. This theory is based on the FDE extension to excited states [#ref7]_, which is implemented in ADF in a local response approximation, i.e., neglecting the dynamic response of the environment [#ref8]_.   

The subsystem TDDFT code allows to treat the mutual response of several subsystems, including the ones that are considered environment. A more typical situation would be a system composed of several equivalent chromophores treated as individual subsystems. In this case, the local response approximation leads to uncoupled excited states of the subsystems (hence the acronym FDEu is employed often),  while the subsystem TDDFT code couples the monomer excitations to obtain the excited states of the total system (often denoted as coupled frozen density embedding, FDEc). This can be related to excitonic couplings between the monomers [#ref72]_.  

The current implementation is restricted to NOSYM calculations and Singlet-Singlet excitations without frozen core approximation. It makes use of the ALDA kernel (including a Thomas-Fermi part for the contribution arising from the non-additive kinetic energy) for consistency with the uncoupled FDE implementation for excited states. Some features have not or not extensively been tested and should be used with great care, e.g., linear dependencies in the basis set. Details on the calculation of transition moments, oscillator and rotational strengths are described in Ref. [#ref11]_. 

Subsystem TDDFT (FDEc) calculations can be invoked with the SUBEXCI key. 

**SUBEXCI input**

FDEc calculations on coupled excited states first require that an uncoupled FDE-TDDFT calculation has been performed for every subsystem that should be included in the coupled calculation, and that the corresponding adf.rkf files, in which the considered subsystems are "active", have been saved (see the separate FDE input description).  This means that it is not possible to use the information on  frozen/inactive fragments from a adf.rkf file of a previous uncoupled FDE calculation, which contains all subsystems. 

Although it is technically possible to use adf.rkf files from non-FDE calculations on the separate subsystems, this would lead to results that are inconsistent with the subsystem TDDFT methodology from Ref. [#ref74]_. In any case, a previous TDDFT calculation for each subsystem that should be included in the coupling procedure is necessary. If that is not the case, the subsystem will still be considered in the calculation of the total electron density (needed in the setup of the exchange-correlation kernel), but will not be included in the coupling procedure. 

The first subsystem should always be one of the coupled subsystems. The input will then look like the corresponding input for an uncoupled FDE-TDDFT calculation, but in addition should contain the following block: 

.. _keyscheme SUBEXCI: 


::

   SUBEXCI
     {LOWEST nlowest}
     {OPTSTATES list_of_optstates}
     {CTHRES coupling_threshold}
     {SFTHRES solutionfactor_threshold}
     {COUPLBLOCK}
     {TDA}
     {CICOUPL}
   END

``LOWEST nlowest``
   The selection of the excited states to be coupled consists of two steps. First, a number of reference states are selected. As a default, the nlowest (default: 10) lowest excited states present on the fragment file for the first subsystem are considered. 

``OPTSTATES list_of_optstates``
   If the keyword OPTSTATES is given, only those excited states of the first subsystem are considered as reference states that are given in the list_of_optstates (numbers of states separated by blanks).  

``CTHRES coupling_threshold``
   Second, all excitations of all subsystems (present on the fragment adf.rkf files) with an excitation energy that differs by less than coupling_threshold (to be given in units of eV; default: 30 eV)  from one of the reference states are selected to be included in the coupling. Note that additional excited states of system 1 may be included here. 

``COUPLBLOCK``
   If COUPLBLOCK is specified in the input, all couplings between all of these local excited states are included. Otherwise (default), the coupling_threshold is also applied to select pairs of states for which couplings are calculated. I.e., couplings are not calculated if the two particular states to be coupled  differ in energy by more than coupling_threshold. 

``SFTHRES solutionfactor_threshold``
   To reduce the computational effort, it is possible to ignore the effect of orbital pairs with coefficients less than solutionfactor_threshold in the solution factors (TDDFT eigenvectors) of the underlying uncoupled calculation in the construction of the exact trial densities during the calculation of the coupling matrix elements. These orbital pair contributions are not ignored in the subsequent calculation of transition moments,  oscillator, and rotational strengths. The default value of 0.00001 typically leads to a precision of the coupled excitation energies of about 0.0001 eV.  

``TDA``
   TDA specifies the use of the Tamm-Dancoff-Approximation (:ref:`TDA`) in the underlying uncoupled FDE-TDDFT calculations (Ref. [#ref75]_). Contrary to the full SUBEXCI-TDDFT variant, SUBEXCI-TDA allows for the usage of hybrid functionals in the underlying uncoupled FDE-TDDFT calculations. 

``CICOUPL``
   Within the Tamm-Dancoff Approximation, the couplings between localized excited states on different subsystems correspond directly to so-called exciton couplings (see Ref. [#ref75]_). The CICOUPL keyword, in conjunction with TDA, prints these exciton couplings. It is also possible to use CICOUPL with full FDEc-TDDFT. In that case, the excitonic couplings between monomers are reconstructed from an effective 2x2 CIS-like eigenvalue problem, as e.g. done in Ref. [#ref72]_. 

In addition, the input file may contain either an EXCITATION block or the keyword DIFFUSE. Both options lead to a slight adaption of the integration grid. Apart from this, the EXCITATION block will be ignored.  

The key ALLOW PARTIALSUPERFRAGS is currently necessary to be able to use subsystem information for only one subsystem from a adf.rkf file of a previous FDE calculation: 

::

   ALLOW PARTIALSUPERFRAGS



Restrictions and pitfalls
-------------------------

In the current implementation, only the electron density of the embedded system is  calculated. Therefore, with the exception of interaction energies, only properties that depend directly on the electron density  (e.g., dipole moments) are available. In addition, the TDDFT extension allows the  calculation of electronic excitation energies and polarizabilities, and NMR shieldings can be calculated. 

.. warning:: 
   
   EVERYTHING ELSE IS NOT YET IMPLEMENTED. THE RESULTS OBTAINED FOR OTHER PROPERTIES MIGHT BE MEANINGLESS.

**Kinetic energy approximant:** Although the effective embedding potential is derived from first principles using universal density approximants, the ADF implementation relies on approximations. Currently, two implemented approximations are recommended [#ref24]_: PW91k (also known as GGA97) which uses electron densities and the corresponding gradients to express the non-additive kinetic energy component of the embedding potential, or TF (Thomas-Fermi LDA approximant), which does not use gradients at all. Either approximation is applicable only in cases where the overlap between electron densities of the corresponding interactions is small.  Note: so far, no approximation has been developed for the strong-overlap case -  two subsystem linked by covalent bonds for instance.  

.. only:: html

  .. rubric:: References

.. [#ref1] T.A. Wesolowski and A. Warshel, *Frozen Density Functional Approach for ab-initio Calculations of Solvated Molecules*, `Journal of Physical Chemistry 97, 8050 (1993) <https://doi.org/10.1021/j100132a040>`__ 

.. [#ref2] J.\  Neugebauer, C.R. Jacob, T.A. Wesolowski and E.J. Baerends, *An Explicit Quantum Chemical Method for Modeling Large Solvation Shells Applied to Aminocoumarin C151*, `Journal of Physical Chemistry A 109, 7805 (2005) <https://doi.org/10.1021/jp0528764>`__ 

.. [#ref3] T.A. Wesolowski, in: Computational Chemistry: Reviews of Current Trends - Vol. 10, World Scientific, 2006. 

.. [#ref4] C.R. Jacob, J. Neugebauer and L. Visscher, *A flexible implementation of frozen-density embedding for use in multilevel simulations*, `Journal of Computational Chemistry 29, 1011 (2008) <https://doi.org/10.1002/jcc.20861>`__ 

.. [#ref5] T.A. Wesolowski and J. Weber, *Kohn-Sham equations with constrained electron density: an iterative evaluation of the ground-state electron density of interacting molecules*, `Chemical Physics Letters 248, 71 (1996) <https://doi.org/10.1016/0009-2614(95)01281-8>`__ 

.. [#ref7] M.E. Casida and T.A. Wesolowski, *Generalization of the Kohn-Sham equations with constrained electron density formalism and its time-dependent response theory formulation*, `International Journal of Quantum Chemistry 96, 577 (2004) <https://doi.org/10.1002/qua.10744>`__ 

.. [#ref8] T.A. Wesolowski, *Hydrogen-Bonding-Induced Shifts of the Excitation Energies in Nucleic Acid Bases: An Interplay between Electrostatic and Electron Density Overlap Effects*, `Journal of the American Chemical Society 126, 11444 (2004) <https://doi.org/10.1021/ja048846g>`__ 

.. [#ref9] C.R. Jacob, J. Neugebauer, L. Jensen and L. Visscher, *Comparison of frozen-density embedding and discrete reaction field solvent models for molecular properties*, `Physical Chemistry Chemical Physics 8, 2349 (2006) <https://doi.org/10.1039/B601997H>`__ 

.. [#ref10] J.\  Neugebauer and E.J. Baerends, *Exploring the Ability of Frozen-Density Embedding to Model Induced Circular Dichroism*, `Journal of Physical Chemistry A 110, 8786 (2006) <https://doi.org/10.1021/jp0622280>`__ 

.. [#ref11] J.\  Neugebauer, *On the calculation of general response properties in subsystem density functional theory*, `Journal of Chemical Physics 131, 084104 (2009) <https://doi.org/10.1063/1.3212883>`__. 

.. [#ref12] C.R. Jacob and L. Visscher, *Calculation of nuclear magnetic resonance shieldings using frozen-density embedding*, `Journal of Chemical Physics 125, 194104 (2006) <https://doi.org/10.1063/1.2370947>`__ 

.. [#ref14] C.R. Jacob, T.A. Wesolowski and L. Visscher, *Orbital-free embedding applied to the calculation of induced dipole moments in* CO2\ :sup:`...` X *(X=He, Ne, Ar, Kr, Xe, Hg) van der Waals complexes*, `Journal of Chemical Physics 123, 174104 (2005) <https://doi.org/10.1063/1.2107567>`__ 

.. [#ref18] T.A. Wesolowski and J. Weber, *Kohn-Sham equations with constrained electron density: The effect of various kinetic energy functional parametrizations on the ground-state molecular properties*, `International Journal of Quantum Chemistry 61, 303 (1997) <https://doi.org/10.1002/(SICI)1097-461X(1997)61:2%3C303::AID-QUA13%3E3.0.CO;2-C>`__ 

.. [#ref21] D.\  Schlüns, M. Franchini, A. W. Götz, J. Neugebauer, C. R. Jacob ,L. Visscher, *Analytical gradients for subsystem density functional theory within the slater-function-based amsterdam density functional program*, `J. Comput. Chem. 38, 4 (2017) <https://doi.org/10.1002/jcc.24670>`__

.. [#ref24] T.A. Wesolowski, *Density functional theory with approximate kinetic energy functionals applied to hydrogen bonds*, `Journal of Chemical Physics 106, 8516 (1997) <https://doi.org/10.1063/1.473907>`__ 

.. [#ref26] T.A. Wesolowski, H. Chermette and J. Weber, *Accuracy of Approximate Kinetic Energy Functionals in the Model of Kohn-Sham Equations with Constrained Electron Density: the* FH\ :sup:`...` NCH *complex as a Test Case*, `Journal of Chemical Physics 105, 9182 (1996) <https://doi.org/10.1063/1.472823>`__ 

.. [#ref27] Y.A. Bernard, M. Dulak, J.W. Kaminski and T.A. Wesolowski, *The energy-differences based exact criterion for testing approximations to the functional for the kinetic energy of non-interacting electrons*, `Journal of Physics A 41, 55302 (2008) <https://doi.org/10.1088/1751-8113/41/5/055302>`__ 

.. [#ref28] L.H. Thomas, *The calculation of atomic fields*, `Mathematical Proceedings of the Cambridge Philosophical Society 23, 542 (1927) <https://doi.org/10.1017/S0305004100011683>`__ 

.. [#ref29] E.\  Fermi, *Eine statistische Methode zur Bestimmung einiger Eigenschaften des Atoms und ihre Anwendung auf die Theorie des periodischen Systems der Elemente*, `Zeitschrift für Physik 48, 73 (1928) <https://doi.org/10.1007/BF01351576>`__ 

.. [#ref30] P.\  Cortona, *Self-consistently determined properties of solids without band-structure calculations*, `Physical Review B 44, 8454 (1991) <https://doi.org/10.1103/PhysRevB.44.8454>`__ 

.. [#ref32] A.\  Lembarki and H. Chermette, *Obtaining a gradient-corrected kinetic-energy functional from the Perdew-Wang exchange functional*, `Physical Review A 50, 5328 (1994) <https://doi.org/10.1103/PhysRevA.50.5328>`__ 

.. [#ref36] J.M. Garcia Lastra, J.W. Kaminski and T.A. Wesolowski, *Orbital-free effective embedding potential at nuclear cusps*, `Journal of Chemical Physics 129, 074107 (2008) <https://doi.org/10.1063/1.2969814>`__ 

.. [#ref39] H.\  Lee, C. Lee and R.G. Parr, *Conjoint gradient correction to the Hartree-Fock kinetic- and exchange-energy density functionals*, `Physical Review A 44, 768 (1991) <https://doi.org/10.1103/PhysRevA.44.768>`__ 

.. [#ref42] D.A. Kirzhnits, Soviet Physics JETP-USSR 5, 64 (1957) 

.. [#ref43] A.J. Thakkar, *Comparison of kinetic-energy density functionals*, `Physical Review A 46, 6920 (1992) <https://doi.org/10.1103/PhysRevA.46.6920>`__ 

.. [#ref53] H.\  Ou-Yang and M. Levy, *Approximate noninteracting kinetic energy functionals from a nonuniform scaling requirement*, `International Journal of Quantum Chemistry 40, 379 (1991) <https://doi.org/10.1002/qua.560400309>`__ 

.. [#ref57] A.W. Götz, S.M. Beyhan and L. Visscher, *Performance of Kinetic Energy Functionals for Interaction Energies in a Subsystem Formulation of Density Functional Theory*, `Journal of Chemical Theory and Computation 5, 3161 (2009) <https://doi.org/10.1021/ct9001784>`__ 

.. [#ref58] M.\  Ernzerhof, *The role of the kinetic energy density in approximations to the exchange energy*, `Journal of Molecular Structure: THEOCHEM 501-502, 59 (2000) <https://doi.org/10.1016/S0166-1280(99)00414-5>`__ 

.. [#ref60] J.P. Perdew, *Generalized gradient approximation for the fermion kinetic energy as a functional of the density*, `Physics Letters A 165, 79 (1992) <https://doi.org/10.1016/0375-9601(92)91058-Y>`__ 

.. [#ref61] C.R. Jacob, S.M., Beyhan and L. Visscher, *Exact functional derivative of the nonadditive kinetic-energy bifunctional in the long-distance limit*, `Journal of Chemical Physics 126, 234116 (2007) <https://doi.org/10.1063/1.2743013>`__ 

.. [#ref67] D.V. Chulhai and L. Jensen, *Frozen Density Embedding with External Orthogonality in Delocalized Covalent Systems*, `Journal of Chemical Theory and Computation 11, 3080 (2015) <https://doi.org/10.1021/acs.jctc.5b00293>`__. 

.. [#ref68] A.\  Goez, and J. Neugebauer, *A Local Variant of the Conductor-Like Screening Model for Fragment-Based Electronic-Structure Method*, `Journal of Chemical Theory and Computation 11, 5277 (2015) <https://doi.org/10.1021/acs.jctc.5b00832>`__ 

.. [#ref69] A.\  Goez, and J. Neugebauer, *Including protein density relaxation effects in first-principles embedding calculations of cofactor excitation energies*, `Molecular Physics 115, 526 (2016) <https://doi.org/10.1080/00268976.2016.1199823>`__ 

.. [#ref72] J.\  Neugebauer, *Photophysical Properties of Natural Light-Harvesting Complexes Studied by Subsystem Density Functional Theory*, `Journal of Physical Chemistry B 112, 2207 (2008) <https://doi.org/10.1021/jp709956k>`__ 

.. [#ref74] J.\  Neugebauer, *Couplings between electronic transitions in a subsystem formulation of time-dependent density functional theory*, `Journal of Chemical Physics 126, 134116 (2007) <https://doi.org/10.1063/1.2713754>`__. 

.. [#ref75] C.\  König, N. Schlüter. J. Neugebauer, *Direct Determination of Exciton Couplings from Subsystem TDDFT within the Tamm-Dancoff Approximation*, `Journal of Chemical Physics 138, 034104 (2013) <https://doi.org/10.1063/1.4774117>`__ 

.. [#ref79] J.\  Neugebauer, M.J. Louwerse, E.J. Baerends and T.A. Wesolowski, *The merits of the frozen-density embedding scheme to model solvatochromic shifts*, `Journal of Chemical Physics 122, 94115 (2005) <https://doi.org/10.1063/1.1858411>`__ 

.. [#ref80] J.\  Neugebauer, M.J. Louwerse, P. Belanzoni, T.A. Wesolowski and E.J. Baerends, *Modeling solvent effects on electron-spin-resonance hyperfine couplings by frozen-density embedding*, `Journal of Chemical Physics 123, 114101 (2005) <https://doi.org/10.1063/1.2033749>`__ 

.. [#ref81] M.\  Zbiri, M. Atanasov, C. Daul, J.-M. Garcia Lastra and T.A. Wesolowski, *Application of the density functional theory derived orbital-free embedding potential to calculate the splitting energies of lanthanide cations in chloroelpasolite crystals*, `Chemical Physics Letters 397, 441 (2004) <https://doi.org/10.1016/j.cplett.2004.09.010>`__ 

.. [#ref82] M.\  Zbiri, C.A. Daul and T.A. Wesolowski, *Effect of the f-Orbital Delocalization on the Ligand-Field Splitting Energies in Lanthanide-Containing Elpasolites*, `Journal of Chemical Theory and Computation 2, 1106 (2006) <https://doi.org/10.1021/ct060035a>`__ 
