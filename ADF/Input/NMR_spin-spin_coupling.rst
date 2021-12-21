.. index:: cpl module 
.. _NMR ss coupling const: 


NMR spin-spin coupling constants
================================

The NMR spin-spin coupling constants [#ref1]_ [#ref2]_ have been implemented in a separate program CPL. It can be combined with ZORA and Spin-Orbit treatment of relativistic effects to study heavy elements. The original version of this part of the User's Guide was written by Jochen Autschbach, primary author of the CPL code. 

.. index:: NMR spin-spin couplings 
.. index:: NSSCC 
.. index:: nuclear spin-spin coupling constant 
.. index:: spin-spin coupling constant 

Two GUI tutorials on spin-spin coupling constant calculations are currently available:

+ Chemical shifts and nuclear spin-spin coupling constants w. NBO analysis: `Analysis of NMR parameters with Localized Molecular Orbitals <../../Tutorials/NMR/NMRAnalysisWithNLMOAndNBO.html>`_ 
+ Chemical shifts and nuclear spin-spin coupling constants w. visualization of the spectrum in the GUI: `H-NMR spectrum with spin-spin coupling <../../Tutorials/NMR/H-NMRSpectrumSpin-SpinCoupling.html>`_ 

Introduction
------------

The CPL code of the Amsterdam Density Functional program system allows the user to calculate *Nuclear Spin-spin Coupling Constants* (NSSCCs) [#ref1]_ [#ref2]_. NSSCCs are usually observed in NMR (Nuclear Magnetic Resonance) spectroscopy and give rise to the splitting of the signals of the NMR spectrum in multiplets. They contain a wealth of information about the geometric and electronic structure of the compound being investigated.  

The calculation needs a standard adf.rkf (TAPE21) ADF output file. CPL reads also an input key and optional settings from stdin (usually from an input file). Technical parameters such as the maximum memory usage can be set here as well.  

One of the key features of the program is its ability to treat heavy nuclei with the ZORA relativistic formalism. We refer the reader to the literature for details about our implementation [#ref1]_ [#ref2]_, and the general review on relativistic computations of NMR parameters [#ref5]_. Please use the information printed in the output header of the CPL program in order to provide references of this work in scientific publications.  

The development of the CPL program started in 2000. CPL provides the main functionality in order to evaluate NSSCCs based on DFT, as well as a number of additional features in order to provide an analysis of the results. Several analysis features for the coupling constant have been added, see the CONTRIBUTIONS sub key. Please report bugs or suggestions to SCM at support@scm.com. 

.. index:: reduced spin-spin coupling constant 

**Theoretical and technical aspects**

Within the non-relativistic theory of nuclear spin-spin coupling, there are four terms contributing to the NSSCC between two nuclei A and B: the paramagnetic and diamagnetic orbital terms (OP and OD, respectively), and the electron-spin dependent Fermi-contact (FC) and spin-dipole term (SD). In the literature, the OP and OD terms are often named PSO and DSO (for paramagnetic and diamagnetic spin-orbital). In the more general ZORA formulation, very similar operators are responsible for the NSSCC, therefore we use the same terminology for the individual contributions. In general, the interpretation of the results for a heavy atom system is basically equivalent to a non-relativistic situation.  

In most cases, the FC term yields the most important contribution to the NSSCC. However, many exceptions are known for which one or each of the other terms can be non-negligible or even dominant. We therefore suggest that you always check, at least for a smaller but similar model system, or by using a smaller basis set, which of the four terms are negligible and which are dominant.  

By default, the CPL program computes the FC coupling between the first and all other nuclei of the molecule, respectively. Other couplings or the computation of the OP, OD and SD terms can be requested by input switches (see the 'Running CPL' section of this document for details). 

All contributions to the NSSCC are evaluated with the help of the numerical integration scheme implemented into ADF. In general, the computation of the OD term is computationally very cheap, since only integrals involving the electron density have to be evaluated. The next expensive term is the OP term. For this contribution, the first-order perturbed MOs have to be computed. With the available density functionals in ADF, the OP term does not cause a change in the Kohn-Sham potential, and the first-order MOs can be computed directly (i.e. without an iterative procedure). This is equivalent to the approach that has been implemented in the NMR code for ADF. 

Both the FC and the SD terms induce electron spin-density to first-order as a perturbation. Equivalent to the iterative solution of the unperturbed Kohn-Sham equations, the first-order MOs depend on that first-order spin-density, which in turn depends on the first-order MOs. Therefore, in order to evaluate the FC and SD NSSCC contributions, the CPL program carries out a SCF cycle. In the scalar or non-relativistic case, the computational cost for the FC term is comparable to an ADF single point calculation with a local density functional. The evaluation of the SD term is more expensive. The current implementation utilizes the CPL spin-orbit code to compute the combined FC+SD contribution and therefore leaves some room for future speed-ups. In most cases, the SD term yields a negligible NSSCC and the much faster code for the scalar- or non-relativistic FC term can be used. However, it is very important to include the SD term in the computation if coupling anisotropies are to be evaluated. 

In the case where the NSSCC computation is based on spin-orbit coupled relativistic two component ZORA MOs, the SD term causes only a marginal increase in computational time as compared to the FC term alone. Generally, in this case the computational cost for the FC term is already approximately one order of magnitude higher than in the scalar or non-relativistic case, since the 3 (x, y, z) components of the spin-density with respect to 3 components of the perturbation, respectively, have to be determined self-consistently. The additional presence of the SD term only shows up in a somewhat more costly evaluation of the matrix elements of the perturbation operator. However, CPL spends most of its computational time in the SCF cycle. Therefore, in spin-orbit computations the computation of the FC+SD terms is the default. The OP term has to be evaluated self-consistently, too, in this case and is added as a perturbation in the SCF cycle upon request. 

We use the terminology 'perturbing' and 'responding nucleus' within the CPL output. The 'perturbing' nucleus is the one, for which the first-order MOs have to be computed (self-consistently), while the NSSCC is then determined by these first-order MOs and the FC, SD, and OP matrix elements of the second, 'responding' nucleus. For the OD term, this distinction makes no sense but is used in the output for reasons of consistency.  

Experimental NSSCCs between two nuclei A and B are usually reported as J(A,B) in Hertz. From a computational point of view, the so-called reduced NSSCCs K(A,B) are more convenient for comparisons. CPL outputs both. The J's are set to zero in case the nuclear magneto-gyric ratio of one of the nuclei A or B is not available at run time.  

.. index:: spin-spin Diamagnetic orbital term 
.. index:: spin-spin Fermi-Contact term 
.. index:: spin-spin Paramagnetic orbital term 
.. index:: spin-spin Spin-Dipole term 

**Further technical aspects and current limitations**

In order to facilitate the future computation of rather large molecules, all matrix elements of the perturbation operators FC, SD, and OP are evaluated in the Slater AO basis that is specified as input in the CREATE runs of ADF. The AO matrix elements are further transformed to the basis of MOs and the calculation proceeds within the MO basis. This allows for a convenient analysis of the results in terms of contributions from individual occupied and virtual MOs. Such an analysis can be requested by input. 

The matrix elements themselves as well as the first-order contributions to the potential are evaluated by numerical integration. The CPL code, which is parallelized, can use multiple processors for these steps of the computation. The accuracy setting for the numerical integration is of high importance to obtain accurate matrix elements. Furthermore, the basis set being employed needs to be flexible enough to describe the perturbation correctly. This means usually that modified basis sets have to be used in particular for heavy element calculations.  

The first-order potential is currently approximated by the VWN functional. The X:math:`\alpha` potential is available as an alternative but usually leads to less accurate results. In ADF2009.01 the first order potential of the PBE family of GGA functionals and the hybrid PBE0 functional can be used. 

Currently, only spin-restricted computations for systems with an even number of electrons are supported. Further, the calculation does not make use of symmetry and must be based on an ADF run with input SYMMETRY=NOSYM. Non-Aufbau configurations are not supported. The atom input list must not contain dummy atoms. 

With the present version of CPL, the SD term and the FC/SD cross term cannot be evaluated separately. Either, the sum of FC + SD + cross terms, or the FC term individually, are computed.  

CPL is restartable after various time-consuming steps of the computation. 

In ADF2009.01 the hybrid PBE0 functional can be used in combination with NMR spin-spin coupling calculations, see the documentation for the extra keys that are needed. However, other hybrid functionals and Hartree-Fock can not or should not be used in combination with NMR spin-spin coupling calculations. 

In ADF2009.01 the effects of a finite size of a nucleus on the spin-spin couplings can be calculated. A finite size of the nucleus can be set with the NUCLEARMODEL key in the input for the ADF calculation. 

**Bug fix in case more than 1 perturbing atom and DSO or PSO**

In the ADF2006.01b version a bug in the CPL module is fixed that gave problems in ADF2006.01 and older versions. The problem in ADF2006.01 and older versions is: In case there is more than 1 perturbing atom and the DSO or PSO term is calculated, only the results of the spin-spin couplings for the first perturbing atom are correct, but the results of the other spin-spin couplings may be incorrect. 


Input file for CPL: adf.rkf
---------------------------

In order to run the CPL code, you need the general ADF output file adf.rkf named TAPE21 being present in the directory where CPL is running.
Alternatively one can use the key ADFFile to point to an adf.rkf file. 
Most of the computation's specific settings will be taken from adf.rkf (TAPE21), such as the integration accuracy, the basis set, the density functional being employed, nuclear coordinates, and so on. *That also means that nearly all of the aspects that affect the quality of CPL's results are already determined in the input for the ADF run*. Five aspects are of particular importance here: 

1. The numerical integration accuracy: the perturbation operators are large in the vicinity of the nuclei. Therefore, you have to make sure that the integration grid is fine enough in the atomic core regions.

2. The basis set: NSSCCs are sensitive chemical probes, and therefore flexible basis sets have to be employed in order to yield a valid description of the MOs that determine the NSSCCs. We have found that it is imperative to use at least a TZ2P basis set. Additional polarization functions in the valence shell may be necessary. Furthermore, the FC perturbation usually requires additional steep 1s functions (i.e. with exponents much higher than the nuclear charge) for a proper description. In the relativistic heavy element case, the use of additional steep basis functions as compared to the ZORA/TZ2P basis is mandatory. The use of steep functions is only of high importance for those nuclei, for which the NSSCC is to be evaluated.  In ADF2017 specialized large all electron basis sets have been added in the directory $AMSHOME/atomicdata/ADF/ZORA/TZ2P-J and $AMSHOME/atomicdata/ADF/ZORA/QZ4P-J, suitable for NSSCCs, where steep basis functions have been added, which is especially important for the FC term. Previously in ADF2009.01 for a limited number of elements basis sets suitable for NSSCCs have been added to the ADF basis set directory, in the directory $AMSHOME/atomicdata/ADF/ZORA/jcpl. These specialized basis sets are especially important for the heavy NMR nuclei. For the nuclei for which NSSCCs are to be evaluated, it is necessary to use all-electron basis sets. This is not a restriction due to the implementation, but we have found that, with the available frozen core basis sets, the flexibility of the basis in the vicinity of the nuclei is not sufficient. It is possible to use frozen core basis sets if you add enough basis functions in the core region such that the basis approaches the flexibility of at least a double-zeta all-electron basis there [#ref1]_. In that sense, the savings in computational time due to usage of a frozen core basis are not as pronounced as in standard ADF computations. Unless reliable frozen-core basis sets for the NSSCC computation are available we strongly discourage the use of frozen core basis sets with the CPL program!

3.  The finite size of a nucleus: typically, the isotropic J-couplings are reduced in magnitude by about 10 to 15 % for couplings between one of the heaviest NMR nuclei and a light atomic ligand, and even more so for couplings between two heavy atoms, see Ref. [#ref7]_. However, one should have really large basis sets with tight basis functions to observe this effect in calculations, see the previous point about basis sets. The TZ2P-J, QZ4P-J, and jcpl basis sets are suitable for finite nucleus calculations. A finite size of the molecule can be set in the ADF program with the key NUCLEARMODEL::

           NuclearModel Gaussian

4. The density functional: the results of the CPL code depend mostly on the shape of the MOs that have been determined by ADF, and their orbital energies. Both, in turn, depend on the density functional or Kohn-Sham potential that has been chosen for the ADF run (and the basis set quality). It is difficult to give a general advice here concerning the NSSCCs. So far we have found that the use of GGAs improves the NSSCCs with respect to experiment in most cases in comparison to LDA. Different GGAs often yield very similar results. Further, in particular for those cases for which the OP term is large or even dominant, both standard LDAs and GGAs sometimes do not provide an accurate enough description of the orbitals, and deviation of the CPL results as compared to experiment can be substantial. Future developments of density functionals might be able to cure these problems. For the time being, we recommend that you base the CPL run on different choices of density functionals in the ADF run, and investigate the convergence of the result with respect to basis set and integration accuracy. Note that CPL itself uses the VWN functional by default to determine the first-order perturbed MOs. There are enough indications to believe that this is a reasonable approximation for NMR purposes. In ADF2009.01 the first order potential of the PBE family of GGA functionals and the first order potential of the hybrid PBE0 functional can be used. See Refs. [#ref9]_ [#ref10]_ for applications of such first order potentials. However, other hybrid functionals and Hartree-Fock can not or should not be used in combination with NMR spin-spin coupling calculations.

5. Modeling the experimental setup: computing such sensitive numbers as NMR chemical shifts and in particular NSSCCs can result in substantial deviations from experimental data. The simple reason might be that the isolated system that has been computed at zero temperature is not at all a good approximation to the system that has been studied experimentally. We [#ref11]_ [#ref14]_ and other authors have found that in particular solvent effects can contribute very substantially to the NSSCC. In case you are comparing CPL results to experimental data obtained in strongly coordinating solvents we suggest that you consider solvent effects as a major influence. We have found that even weakly coordinating solvents can cause sizable effects on the NSSCCs for coordinatively unsaturated metal complexes. Other sources of errors can be the neglect of vibrational corrections to the NSSCCs (usually in the range of a few percent).

If the parameters of the underlying ADF computation are carefully chosen and the density functional is able to provide an accurate description of the molecule under investigation, it is possible to compute NSSCCs by means of DFT with very satisfactory accuracy (please note that for properties as sensitive as NSSCCs, agreement with experimental results within about 10% error can be regarded as quite good). Further, chemical trends will be correctly reproduced for a related series of molecules in most cases. However, due to the inherent approximate character of the density functionals currently available with ADF, and necessary basis set limitations, great care should be taken that the results are reliable. *CPL assumes Aufbau configurations. Please make sure that there are no empty orbitals with energies below the highest occupied MO (HOMO). In addition, the SYMMETRY NOSYM key has to be used in the ADF computation.*


Running CPL
-----------

**Main input switches**

With the ADF output TAPE21 present in the current working directory, the CPL code is invoked by::

  $AMSBIN/cpl < input_file

where input_file contains the input for CPL. Best is supply also the TAPE10 of the ADF calculation in addition to TAPE21 (specify SAVE TAPE10 in the ADF input file).

input_file must contain at least one block-type input key in order to start the CPL run. The input key is  

.. _keyscheme cpl: 
.. _keyscheme cpl NMRCOUPLING: 

::

   $AMSBIN/cpl << eor
     NMRCOUPLING
     END
   eor

This represents a minimal input file for CPL. The NMRCOUPLING key hosts all optional keys that are relevant for the NSSCCs themselves. In addition to the mandatory NMRCOUPLING key, CPL recognizes the following input switches: 

::

  $AMSBIN/cpl << eor
    ADFFile adffile
    TAPE10File tape10file
    ..
  eor

adffile is the path to an adf.rkf (TAPE21) file from which nmr reads data and to which nmr writes data. Default TAPE21.
tape10file is the ath to a TAPE10 file from which nmr reads data. Default TAPE10.


::

   $AMSBIN/cpl << eor
     GGA
     ...
   eor

See the separate section for this key, which influences the first order potential that is used. 

::

   $AMSBIN/cpl << eor
     RESTART /full/path/to/restart_file
     ...
   eor

restart the computation from file restart_file (full pathname should be given). This is the TAPE13 produced during a CPL run. By default, TAPE13 is deleted after a successful completion of CPL. As with ADF restarts, you can not use the name TAPE13 for restart_file but you have to rename it, e.g. to tape13.restart.


::

   $AMSBIN/cpl << eor
     SAVE TAPE13
     ...
   eor

keep the restart file even after a successful completion of CPL. TAPE13 is currently the only file that is meaningful as a parameter to SAVE. 

**NMRCOUPLING subkeys**

The available switches within a NMRCOUPLING/END block control the computation of the NSSCCs. By default, the program will evaluate the FC coupling contribution for the first nucleus being the perturbing nucleus and all remaining nuclei responding. 

Please **note** that the ordering of atoms in CPL is generally different from the ADF input. The ordering of atoms is the one being stored in TAPE21 and it is grouped by fragment types. In case you are in doubt about the ordering of atoms, you can run CPL for a few seconds. It will print a list of atoms with their coordinates. The ordering is currently the same as required the NMR program in the ADF program system. On the other hand, note that for the subkeys ATOMPERT and ATOMRESP the number of the atoms refer to the input ordering in the ADF calculation. Curly brackets are not part of a key.

Available subkeys are: 

::

   $AMSBIN/cpl << eor
     NMRCOUPLING
       NUCLEI {npert nresp1 nresp2}
       ATOMPERT {npert1 npert2 npert3}
       ATOMRESP {nresp1 nresp2 nresp3}
       GAMMA {nnuc gamma}
       DSO
       PSO
       SD
       FC
       SCF {ITERATIONS=25 | NOCYCLE | CONVERGE=1e-4 }
       XALPHA
       CONTRIBUTIONS {1E19} {LMO, SFO, LMO2, SFO2}
     END
     ... 
   eor

``NUCLEI {npert nresp1 nresp2}``
   Use nucleus no. npert as the perturbing nucleus, and nuclei nresp1, nresp2, etc as responding nuclei. You can supply more than one NUCLEI keys, in which case CPL evaluates the first-order MOs for each perturbing nucleus that is specified and computes the NSSCCs between all specified responding nuclei. For each NUCLEI line in the input, CPL has to perform an SCF cycle. Note: for the numbers of the atoms the internal CPL numbering should be used. 

``ATOMPERT {npert1 npert2 npert3}``
   See next subkey ATOMRESP.

``ATOMRESP {nresp1 nresp2 nresp3}``
   ATOMPERT: use nucleus no. npert1, npert2, etc. as the perturbing nuclei. ATOMRESP: use nucleus no. nresp1, nresp2, etc. as the responding nuclei. You can supply more than one ATOMPERT and (or) ATOMRESP key. CPL computes the NSSCCs for all pairs of combinations of perturbing atoms and responding atoms. For each perturbing atom CPL has to perform an SCF cycle, which is the expensive part in the calculation. Note: the numbers refer to the input ordering in the ADF calculation. Use the subkey NUCLEI to specify the nuclei according to the internal CPL numbers of the atoms. 

``GAMMA {nnuc gamma}``
   Input a non-default magneto-gyric ratio of g = gamma for nucleus no. nnuc, in units of rad/(T s). Note that one should include the the typical 10\ :sup:`7`  factor. CPL normally uses the g value of the most abundant NMR active isotope for a nucleus of a given charge by default. With the GAMMA keyword you can override this value or supply a value if CPL does not know about it. A list of g's that is used in the computation is printed in the output. You have to provide the GAMMA key for each nucleus you want to specify. 

``DSO``
   Compute the diamagnetic orbital term for each NSSCC that is requested (not default) 

``PSO``
   Compute the paramagnetic orbital term for each NSSCC (not default) 

``SD``
   Compute the SD term for each NSSCC. This is only default for spin-orbit ADF runs. The output will contain the sum of the FC and SD contributions. *Please note that requesting this option results in a greatly increased computational cost in scalar or non-relativistic runs.* The option NOSD will turn the SD computation off in spin-orbit runs and has no effect otherwise. 

``FC``
   Compute the FC contribution to the NSSCCs. This is the default option. Please note that it is currently not possible to compute the SD term without the FC term. Consult the 'practical aspects' section for instructions how to estimate the FC/SD cross term. The option NOFC will disable both the FC and SD computation. 

``SCF {ITERATIONS=25 | NOCYCLE | CONVERGE=1e-4 }``
   Settings related to the SCF cycle that is carried out by CPL. Valid options are (with default values if applicable): 

   ``ITERATIONS 25``
      maximum number of iterations 

   ``NOCYCLE``
      perform no cycle, equivalent to ITERATIONS 0 

   ``CONVERGE 1e-4``
      convergence criterion, an input of e corresponds approximately to a convergence of log(-e) digits, i.e. the results will be converged to about four significant digits by default. The measurement for the convergence is based on the sum *S* of the magnitudes of all occupied-virtual matrix elements of the induced first-order exchange potential. Note that the actual convergence criterion being used in the computation is e times *S* of the first cycle, i.e. the convergence criterion is set relative to the initial value of *S*. 

``XALPHA``
   Use first-order Xalpha potential instead of VWN potential (default). This will usually decrease the accuracy for couplings involving hydrogen, and does not have a large effect for couplings between heavier nuclei (not default). The key is mainly intended to ensure compatibility with our previously published results. 

``CONTRIBUTIONS {1e19} {LMO, SFO, LMO2, SFO2}``
   Print contributions from individual orbitals to the FC and OP term of the NSSCCs that are larger in magnitude than a certain threshold. The threshold refers to the reduced coupling constant K in SI units (not default). Additionally, an analysis in terms of Boys localized MOs (see User's Guide and SFOs. At present, either each key LMO, SFO, LMO2, SFO2 can be used individually, or grouped as {LMO, SFO2} or {SFO2, LMO}. If you need all analyses or different combinations, it is recommended to restart the CPL calculation from TAPE13, and to specify 0 iterations in the SCF. This way, the only additional computational cost should be the analysis itself. 

   The equation and an application for the analyses due to the LMO and SFO keys is described in Refs. [#ref25]_ [#ref26]_. The other analysis is based on the same equation as in Ref. [#ref8]_. For an NBO analysis of the spin-spin couplings, see the  :ref:`section on NBO analysis<NBO_PROPERTIES>`. 

   In order for the LMO-based analyses to work, the MO → LMO transformation matrix needs to be stored on TAPE21. In the ADF input, you can achieve this with the option "STORE" to the LOCORB key, i.e. ::

      LOCORB STORE
         ... options
      END

.. _keyscheme cpl GGA: 


**GGA key**


::

   $AMSBIN/cpl << eor
     GGA
     ...
   eor

``GGA``
   Use first-order GGA potential instead of the first-order VWN potential. Should only be used for the PBE family of GGA exchange-correlation functionals and for the hybrid functional PBE0. See Refs. [#ref9]_ [#ref10]_ for applications of calculating spin-spin couplings with PBE0. However, other hybrid functionals and Hartree-Fock can not or should not be used in combination with this key GGA. For consistency reasons of the first-order potential one should use the keyword USESPCODE in the ADF calculation. An example input for ADF for the hybrid PBE0 would then contain: 

::

   USESPCODE
   XC
    hybrid PBE0
   End


Practical Aspects
-----------------

**Minimal input**

The default settings for CPL are invoked by the simple minimal content of the input file:  

::

   $AMSBIN/cpl << eor
     NMRCOUPLING
     END
   eor

This is equivalent to 

::

   $AMSBIN/cpl << eor
     NMRCOUPLING
      NUCLEI 1 2 3 4 5 6 7 8 ..(up to number of atoms)
      SCF CONVERGE 1e-4 ITERATIONS 25
      FC
     END
   eor

**Restarts**

CPL is restartable after the computation of each the complete set of FC or FC/SD and OP matrix elements, and after their transformation to the MO basis. Further, in spin-orbit runs or in scalar- or non-relativistic computations involving the SD term, CPL is restartable after each SCF cycle. As with ADF restarts, you need to supply a proper input file for a restarted computation, and the restart file TAPE13 (which needs to be renamed). Changing the input of a calculation for a restart is not supported. In restarted runs, the program will automatically continue at the latest possible point before the execution stopped, and changing the input between restarts can cause inconsistencies that may lead to a crash. 

Unless you are computing a very large molecule, the most likely need for a restart will probably occur during a computation of the FC/SD SCF cycle. We have already mentioned that this is a very time consuming part of the computation, and for this reason CPL can be restarted after each completed SCF cycle. The convergence of the results should not be affected by a restart. You can, e.g., use this in order to complete a lengthy CPL computation in case you have tight time limits in your queuing system, or after a power loss.  

**How to avoid the unnecessary computation of many SCF cycles**

As already mentioned, once the first-order MOs with respect to the perturbation by one of the nuclear spins have been determined, the NSSCC between this and all other nuclei can be computed rather quickly. For each nucleus that participates in at least one of the coupling constants to be determined, the matrix elements of the FC, SD, and OP operators have to be evaluated once (unless the computation of the respective terms is disabled).  

You can use this information in order to minimize the number of nuclei for which an SCF cycle has to be performed. This can lead to a great speedup of the computation. The final result, the NSSCC between A and B, does not depend on which nucleus has been chosen as the 'perturbing' one, and which as the 'responding' one (convergence has to be good enough, though). Suppose you want to compute the NSSCCs in the water molecule, with O being nucleus no. 1. In that case, 

::

   NUCLEI 1 2 3
   NUCLEI 2 3

yields the same O-H and H-H coupling constants as the input 

::

   NUCLEI 2 1
   NUCLEI 1 3
   NUCLEI 3 2

but with less computational effort due to the fact that only 2 instead of 3 SCF cycles will be performed. The example chosen here is trivial, but in other cases it can be worthwhile to consider different sequences of computations. 

Alternatively you can use the ATOMPERT and ATOMRESP subkeys: 

::

   ATOMPERT 1 2
   ATOMRESP 2 3

which will calculate the spin-spin coupling of the nuclei 1-2, 1-3, and 2-3 (skips 2-2, since the nuclei are the same), which are the same O-H and H-H couplings as before. 


**Note**: The numbers of the nuclei for the subkeys ATOMPERT and ATOMRESP refer to the input ordering in the ADF calculation, whereas the numbers of the nuclei for the subkey NUCLEI refer to the internal CPL numbers of the atoms. 

**Computing individual terms in the coupling tensor**

As we have mentioned before, the FC, OP and OD terms can be calculated individually, but not the SD term. In case the SD input option is given, the FC+SD contribution is evaluated instead. This is NOT equal to the sum of the individual FC and SD contributions since there is a cross term between these two. Due to computational simplicity and efficiency, CPL evaluates either the matrix elements for the FC operator, or the combined ones for FC+SD. The final result therefore contains either FC only, or FC, SD plus the cross terms. Only the latter, in addition to the OP and OD contributions, should be compared to experimental results. We will implement the computation of the individual SD term in a future version of CPL in order to assist the analysis of the CPL results.  

Likewise, in a spin-orbit based relativistic computation, there exists a cross term between the spin-dependent FC and SD terms, and the OP term. In the scalar- or non-relativistic limit, this contribution is always zero. With the PSO option present, CPL computes the FC, SD and OP terms including all cross contributions. Even though the output suggests that the individual OP and FC+SD terms are printed, they contain additional cross terms if spin-orbit coupling is large. You can run CPL with the options 

::

   $AMSBIN/cpl << eor
     NMRCOUPLING
      NOFC
      NOSD
      PSO
     END
     ...
   eor

in order to evaluate the individual OP contribution(s). In a second run, you can then compute just the FC+SD contributions. The differences between these two CPL runs and a third one with all three terms present yields the relativistic (FC+SD)/OP cross term.  

**Two-bond and more-bond couplings**

CPL does not discriminate between one-bond and two-bond couplings etc. in any technical sense. Even though we [#ref1]_ [#ref2]_  [#ref11]_ [#ref14]_ have validated the code mostly for one-bond NSSCCs, the coupling between any pair of nuclei in the molecule can be computed. See Ref. [#ref11]_ for an example.  

**Principal axis system, the whole coupling tensor**

CPL evaluates the complete 3x3 coupling tensor with respect to the Cartesian input coordinate system. Depending on the orientation of the molecule, and the local symmetry, the coupling tensor has in fact often only a small number of independent components. CPL evaluates the 'principal components' by the following procedure: the 3x3 matrix is transformed into the basis of the eigenvectors of its symmetric part. This diagonalizes the symmetric part of the coupling tensor. A set of eigenvectors (= 'principal axis system') is also printed.  


.. only:: html

  .. rubric:: References

Main references [#ref1]_ [#ref2]_ [#ref14]_ [#ref11]_ [#ref7]_ [#ref9]_ [#ref10]_ [#ref5]_.

See also refs. [#ref20]_ [#ref21]_ [#ref8]_ [#ref23]_ [#ref24]_.

.. [#ref1] J.\  Autschbach and T. Ziegler, *Nuclear spin-spin coupling constants from regular approximate density functional calculations. I. Formalism and scalar relativistic results for heavy metal compounds*, `Journal of Chemical Physics 113, 936 (2000) <https://doi.org/10.1063/1.481874>`__ 

.. [#ref2] J.\  Autschbach, and T. Ziegler, *Nuclear spin-spin coupling constants from regular approximate relativistic density functional calculations. II. Spin-orbit coupling effects and anisotropies*, `Journal of Chemical Physics 113, 9410 (2000) <https://doi.org/10.1063/1.1321310>`__ 

.. [#ref5] J.\  Autschbach and S. Zheng, *Relativistic computations of NMR parameters from first principles: Theory and applications*, `Annual Reports on NMR Spectroscopy 67, 1 (2009) <https://doi.org/10.1016/S0066-4103(09)06701-5>`__ 

.. [#ref7] J.\  Autschbach, *Magnitude of Finite-Nucleus-Size Effects in Relativistic Density Functional Computations of Indirect NMR Nuclear Spin-Spin Coupling Constants*, `ChemPhysChem 10, 2274 (2009) <https://doi.org/10.1002/cphc.200900271>`__ 

.. [#ref8] J.\  Khandogin, T. Ziegler, *A density functional study of nuclear magnetic resonance spin-spin coupling constants in transition metal systems*, `Spectrochimica Acta Part A 55, 607 (1999) <https://doi.org/10.1016/S1386-1425(98)00265-0>`__ 

.. [#ref9] J.\  Autschbach, *Two-component relativistic hybrid density functional computations of nuclear spin-spin coupling tensors using Slater-type basis sets and density-fitting techniques*, `Journal of Chemical Physics 129, 094105 (2008) <https://doi.org/10.1063/1.2969100>`__, Erratum: `Journal of Chemical Physics 130, 209901 (2009) <https://doi.org/10.1063/1.3131724>`__ 

.. [#ref10] D.L. Bryce and J. Autschbach, *Relativistic hybrid density functional calculations of indirect nuclear spin-spin coupling tensors . Comparison with experiment for diatomic alkali metal halides*, `Canadian Journal of Chemistry 87, 927 (2009) <https://doi.org/10.1139/V09-040>`__ 

.. [#ref11] J.\  Autschbach and T. Ziegler, *A Theoretical Investigation of the Remarkable Nuclear Spin.Spin Coupling Pattern in* [(NC)\ :sub:`5` Pt-Tl(CN)]\ :sup:`-`, `Journal of the American Chemical Society 123, 5320 (2001) <https://doi.org/10.1021/ja003866d>`__ 

.. [#ref14] J.\  Autschbach and T. Ziegler, *Solvent Effects on Heavy Atom Nuclear Spin.Spin Coupling Constants: A Theoretical Study of Hg.C and Pt.P Couplings*, `Journal of the American Chemical Society 123, 3341 (2001) <https://doi.org/10.1021/ja003481v>`__ 

.. [#ref20] N.F. Ramsey, *Electron Coupled Interactions between Nuclear Spins in Molecules*, `Physical Review 91, 303 (1953) <https://doi.org/10.1103/PhysRev.91.303>`__ 

.. [#ref21] R.M. Dickson, T. Ziegler, *NMR Spin-Spin Coupling Constants from Density Functional Theory with Slater-Type Basis Functions*, `Journal of Physical Chemistry 100, 5286 (1996) <https://doi.org/10.1021/jp951930l>`__ 

.. [#ref23] D.L. Bryce, R. Wasylishen, *Indirect Nuclear Spin-Spin Coupling Tensors in Diatomic Molecules: A Comparison of Results Obtained by Experiment and First Principles Calculations*, `Journal of the American Chemical Society 122, 3197 (2000) <https://doi.org/10.1021/ja9942134>`__ 

.. [#ref24] G.\  Schreckenbach, S.K. Wolff, T. Ziegler, *Covering the Entire Periodic Table: Relativistic Density Functional Calculations of NMR Chemical Shifts in Diamagnetic Actinide Compounds*, in `Modeling NMR chemical shifts, ACS Symposium Series, Vol 732, J.C. Facelli, A.C. de Dios, Editors (American Chemical Society, Washington DC, 1999), Chapter 7 <https://doi.org/10.1021/bk-1999-0732.ch007>`__ 

.. [#ref25] J.\  Autschbach, C.D. Igna, T. Ziegler, *A theoretical investigation of the apparently irregular behavior of Pt-Pt spin-spin coupling constants* `Journal of the American Chemical Society 125, 1028 (2003) <https://doi.org/10.1021/ja027931q>`__ 

.. [#ref26] B.L. Guennic, K. Matsumoto, J. Autschbach, *On the NMR properties of platinum thallium bonded complexes: Analysis of relativistic density functional theory results*, `Magnetic Resonance in Chemistry 42, S99 (2004) <https://doi.org/10.1002/mrc.1450>`__ 
