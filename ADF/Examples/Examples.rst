.. index:: examples
.. _examples:


Examples
########

Introduction
************

The ADF package contains a series of sample runs. They consists of UNIX scripts (to run the calculations) and the resulting output files.

The examples serve: 

+  To demonstrate how to do calculations. The number of options available in ADF is substantial and the sample runs do not cover all of them. They should be sufficient, however, to get a feeling for how to explore the possibilities.

+  To work out special applications that do not fit well in the User's Guide.

**Note:** Most of the provided samples have been devised to be short and simple, at the expense of physical or chemical relevance and precision or general quality of results. They serve primarily to illustrate the use of input, necessary files, and type of results. The descriptions have been kept brief. Extensive information about using keywords in input and their implications is given in the User's Manual. 

Where references are made to the operating system (OS) and to the file system on your computer, the terminology of a UNIX type OS is used. 

All sample files are stored in subdirectories under ``$AMSHOME/examples/``, where ``$AMSHOME`` is the main directory of the ADF package. There are many subdirectories in ``$AMSHOME/examples/``: the examples presented in this section are located in ``$AMSHOME/examples/adf/``.
Each sample run has its own directory. For instance, ``$AMSHOME/examples/adf/HCN/`` contains an ADF calculation on the HCN molecule. 

Each sample subdirectory contains: 

+  A file TestName.run: the UNIX script to execute the calculation(s). A sample may involve several calculations, for instance a few CREATE runs (with ADF), then a molecular calculation (also ADF), and finally a NMR calculation (with the NMR program) to compute chemical shifts.

+  A file TestName_orig.out.gz: the resulting output(s) against which you can compare the outcome of your own calculation. Note: the files are compressed using `gzip <https://en.wikipedia.org/wiki/Gzip>`__.

+  Zero or more files with a .ams extension. These files, if present, are intended for AMSinput  and demonstrate the same functionality as the two files above. However, there are also  differences between the .ams and the TestName.run files so the results obtained with the .ams files **cannot be compared directly** with TestName_orig.out. Also, the TestName.run file usually contains more than one calculation, for which more than one .ams file is required. That's why in some directories you may find more than one .ams file.  

Technical notes: 

+  Running the examples on Windows:  You can run an example calculation by double-clicking on the appropriate .run file.  After the calculation has finished, you can compare the TestName.out file with the  reference TestName_orig.out file. See remarks about comparing output files below. 

+  The UNIX scripts make use of the *rm* (remove) command. Some UNIX users may have aliased the *rm* command. They should accordingly adapt these commands in the sample scripts so as to make sure that the scripts will remove the files. New users may get stuck initially because of files that are lingering around after an earlier attempt to run one of the examples. In a subsequent run, when the program tries to open a similar (temporary or result) file again, an error may occur if such a file already exists. Always make sure that no files are left in the run-directory except those that are required specifically.

+  It is a good idea to run each example in a separate directory that contains no other important files.  

+  The run-scripts use the environment variables ``AMSBIN`` and ``AMSRESOURCES``. They stand respectively for the directory that contains the program executables and the main directory of the basis set files.  To use the scripts as they are you must have defined the variables ``AMSBIN`` and ``AMSRESOURCES`` in your environment. If a parallel (PVM or MPI) version has been installed, it is preferable to have also the environment variable ``NSCM``. This defines the default number of parallel processes that the program will try to use. Consult the Installation Manual for details.

+  As you will note the sample run scripts refer to the programs by names like 'adf', 'nmr', and so on. When you inspect your ``$AMSBIN`` directory, however, you may find that the program executables have names 'adf.exe', 'nmr.exe'. There are also files in ``$AMSBIN`` with names 'adf', 'nmr', but these are in fact scripts to execute the binaries. We strongly recommend that you use these scripts in your calculations, in particular when running parallel jobs: the scripts take care of some aspects that you have to do otherwise yourself in each calculation.

+  You need a license file to run any calculations successfully. If you have troubles with your license file, consult the Installation manual. If that doesn't help contact us at support@scm.com


When you compare your own results with the sample outputs, you should check in particular (as far as applicable): 

+  Occupation numbers and energies of the one-electron orbitals;

+ The optimized geometry;

+ Vibrational frequencies;

+ The bonding energy and the various terms in which it has been decomposed;

+ The dipole moment;

+ The logfile.  At the end of a calculation the logfile is automatically appended (by the program itself) to the standard output.

General remarks about comparisons: 

+  For technical reasons, the discussion of which is beyond the scope of this document, differences between results obtained on different machines (or with different numbers of parallel processes) may be much larger than you would expect. They may significantly exceed the machine precision. What you should check is that they fall well (by at least an order of magnitude) within the *numerical integration* precision used in the calculation.

+  For similar reasons the orientation of the molecule used by the program may be different on different machines, even when the same input is supplied. In such cases the different orientations should be related and only differ in some trivial way, such as by a simple rotation of all coordinates by 90 degrees around the z-axis. When in doubt, contact an ADF representative.

.. _examples specialXC:

Model Hamiltonians
******************

Special exchange-correlation functionals
========================================

.. toctree::
   :maxdepth: 1

   CO_model
   OH_MetaGGA
   HI_EFG
   H2PO_B3LYP
   LCY-BP_H2O
   CAMY-B3LYP_H2O
   Water_MP2_AO
   WaterDimer_SOS-MP2_AO
   Water_MeOH_B2GPPLYP
   Water_MeOH_DODSCAN
   MP2_Li
   RPA_H2O
   RPA-SOSSX_H2O
   MM_Dispersion
   methane_dimer_dispersion
   Benzene_dimer_tshaped


.. _examples relativistic effects:


Relativistic effects: ZORA, X2C, spin-orbit coupling
====================================================

.. toctree::
   :maxdepth: 1

   Au2_ZORA
   SO_ZORA_Bi2
   Tl_noncollinear
   AuH_analyse_exciso
   HgI2
   I2_SO_MP2


.. _examples solvents:


Solvents, other environments
============================

.. toctree::
   :maxdepth: 1

   Solv_HCl
   Acetamide_SM12
   Field_PtCO
   Efield.PntQ_N2
   3D-RISM



FDE: Frozen Density Embedding
=============================

.. toctree::
   :maxdepth: 1

   FDE_H2O_128
   FDE_HeCO2_freezeandthaw
   FDE_Energy_NH3-H2O
   FDE_Energy_H2O-Ne_unrestricted
   GO_FDE_H2O-Li
   FDE_NMR_relax
   FDE_CPL_NH3-H2O
   SUBEXCI_dimer
   LoCOSMO_H2O-NH3
   LoCOSMO_H2O-NH3_TDDFT



.. _examples QMMM:

QM/MM calculations
==================

.. _examples Quild:

Quild: Quantum-regions Interconnected by Local Descriptions
===========================================================

+ Quild manual: `Quild examples <../../Quild/Example_inputfiles.html>`_ 


.. _examples DIMQM: 

DIM/QM: Discrete Interaction Model/Quantum Mechanics
====================================================

.. toctree::
   :maxdepth: 1

   DIMQM_DRF_BE
   DIMQM_DRF_Hyperpol
   DIMQM_DRF_plams
   DIMQM_DRF2
   DIMQM_CPIM_Excitations
   DIMQM_JACOBI
   DIMQM_LOCAL
   DIMQM_READLCLFLD
   DIMQM_Gradients
   DIMQM_PIM_Pol
   DIMQM_Raman
   DIMQM_SEROA
   DIMQM_PIM_CMM


QM/FQ: Quantum Mechanics/Fluctuating Charges
============================================

.. toctree::
   :maxdepth: 1

   FQQM_scf
   FQQM_aoresponse
   FQQM_response
   FQQM_td


.. _STRUCTURE: 

.. _examples GO: 

Structure and Reactivity
************************

Geometry Optimizations
======================


.. toctree::
   :maxdepth: 1

   GO_H2O  
   GO_restraint 
   GO_constraints 
   InitHess
   GO_LiF_Efield 



.. _examples reactivity: 


Transition States, Linear Transits, Intrinsic Reaction Coordinates
==================================================================

.. toctree::
   :maxdepth: 1

   HCN
   TS_C2H6
   TS_CH4_HgCl2
   TSRC_SN2
   Transit_H2O



Total energy, Multiplet States, S2, Localized hole, CEBE
========================================================

.. toctree::
   :maxdepth: 1

   Energy_H2O
   SD_CrNH3_6
   CuH+_S-squared
   ModStPot_N2+
   Fe4S4_BrokenSymm
   CEBE_NNO
   CEBE_HI
   WaterDimer



.. _SPECTROSCOPY: 

.. _examples IR: 

Spectroscopic Properties
************************

IR Frequencies, (resonance) Raman, VROA, VCD
============================================


.. toctree::
   :maxdepth: 1

   Freq_NH3
   Freq_UF6
   H2O_HF_freq
   CN_SecDeriv
   CH4_SecDeriv
   HI_SecDer_ZORA
   MBH_Ethanol
   MBH_CH4
   Freq_NH3_RAMAN
   HI_Raman
   HF_ResonanceRaman
   VROA
   VROA_RESO
   DFTB_modes_ADF_Raman_VROA
   VCD_COG_NHDT
   VCD_CHFClBr_DZP


.. _TDDFT: 
.. _examples excitations: 


Excitation energies: UV/Vis spectra, X-ray absorption, CD, MCD
==============================================================

.. toctree::
   :maxdepth: 1

   Au2_Resp
   CN_unr_exci
   SiH2_spinflip
   N2_TDHF
   Pyridine_CAM-B3LYP
   CAMY-B3LYP_TDDFT_H2O
   XCFUN_FULLKERNEL_TDDFT_H2O
   XCFUN_TDDFT_H2O
   TiCl4_CoreExci
   TiCl4_XASXES
   Ne_exciso
   AgI_asoexcit
   PbF_excisou
   DMO_CD
   Twist_Ethene_TDDFT
   H2O_MCD
   H2O_MCD_ZFS
   Formamide_CVnDFT
   NH3_HDA
   H2O_SO_HDA
   TD-DFTB_betacarotene
   Adenine_sTDA
   Adenine_sTDDFT
   Bimane_wB97X
   TCNE-Benzene_wB97


.. _examples EGO:


Excited state (geometry) optimizations
======================================

.. toctree::
   :maxdepth: 1

   EGO_N2
   EGO_CH2O_trip_constr 
   EGO_CH2_sf
   EGO_PH2


.. _examples vibrationally resolved electronic spectra:


Vibrationally resolved electronic spectra
=========================================

.. toctree::
   :maxdepth: 1

   FranckCondon_NO2
   Naphthalene_VST

.. _examples response: 


(Hyper-)Polarizabilities, dispersion coefficients, ORD, magnetizabilities, Verdet constants
===========================================================================================

.. toctree::
   :maxdepth: 1

   AgI_SO_Pol
   LiH_DampedBeta
   LiH_DampedGamma
   H2O_Verdet
   Disper_HF
   DMO_ORD
   DMO_ORD_aoresponse
   ALPHA_DENSITY
   Hyperpol
   DampedVerdet
   H2O_magnet
   H2O_TD_magnet
   C2H4_TDCDFT
   Au10_POLTDDFT
   NH3_POLTDDFT


.. _examples LFDFT: 

Ligand Field DFT (LFDFT)
========================

.. toctree::
   :maxdepth: 1

   Co_LFDFT
   Pr_LFDFT
   Co_LFDFT_gtensor
   Cu_LFDFT_gtensor
   Er_LFDFT_MCD

.. _examples NMR: 


NMR chemical shifts and spin-spin coupling constants
====================================================

.. toctree::
   :maxdepth: 1

   HBr
   HgMeBr_pnr
   CH4_SAOP
   NMR_NICS
   NMR_B3LYP
   CPL_C2H2
   CPL_HF_hybrid
   PbH4_finitenuc



.. _examples ESR: 


ESR/EPR g-tensor, A-tensor, Q-tensor, ZFS
=========================================

.. toctree::
   :maxdepth: 1

   ESR_HfV
   VO_collinear
   ESR_HgF_2der
   ESR_TiF3
   PdH_ESR_X2C
   NH_ZFS
   Phenylnitrene_ZFS


.. _examples EFG: 


EFG, Mössbauer
==============

.. toctree::
   :maxdepth: 1

   Mossbauer
   Hg_Mossbauer_X2C


.. _examples GW: 

GW
==

.. toctree::
   :maxdepth: 1

   GW_H2O
   GW_O3
   GW_Phenol
   evGW_H2O
   qsGW_N2
   G3W2_H2O




.. _examples transport: 


Transport properties
********************

Charge transfer integrals (transport properties)
================================================

.. toctree::
   :maxdepth: 1

   AT_transferintegrals
   ElectronTransfer_FDE_H2O
   ChargeSeparation_Toluene_TCNE
   XCDFT_FDE_ET_ethylene



Non-self-consistent Green's function calculation
================================================

.. toctree::
   :maxdepth: 1

   green_Al
   green_Au
   green_WBL
   green_BDT



.. _examples analysis: 

.. _Fragment: 

Analysis
********

Fragment orbitals, bond energy decomposition
============================================


.. toctree::
   :maxdepth: 1

   Frags_NiCO4
   Frags_PtCl4H2
   UnrFrag_H2
   PCCP_Unr_BondEnergy
   NaCl_ionicbonding
   NaCl_pairbonding
   EDA_meta_gga_hybrid
   EDA_Unr_C2H4_Cu_C2H4
   EDA_Unr_CH3I
   TlH_SO_analysis
   PyFrag

Localized orbitals, bond orders, charge analysis
================================================

.. toctree::
   :maxdepth: 1

   LocMO_Resp
   CM5_chargemodel
   BondOrder

ETS-NOCV
========

.. toctree::
   :maxdepth: 1

   Diimina_NOCV
   Hplus_CO_etsnocv
   NOCV_CrCO5-CH2
   CH3_CH3_etsnocv

QTAIM
=====

.. toctree::
   :maxdepth: 1

   Bader
   Bader_Reactivity
   IQA
   Aromaticity

DOS: Density of states
======================

.. toctree::
   :maxdepth: 1

   DOS_Cu4CO



Third party analysis software
=============================

.. toctree::
   :maxdepth: 1

   AIM_HF
   H2O_ADFNBO
   AlCl3_efgnbo
   CH4_nmrnbo
   CPL_CH3OH_NBO
   EGO_H2O_multi
   CalcOverlapOnly



.. _examples ACCURACY: 


Accuracy and Efficiency
***********************

BSSE, SCF convergence, Frequencies
==================================

.. toctree::
   :maxdepth: 1

   BSSE_CrCO6
   SCF_Ti2O4
   Freq_NH3_Scan



Speed
=====

.. toctree::
   :maxdepth: 1

   Multiresolution_H2O

.. _examples scripting: 


Scripting
*********

Prepare an ADF job and generate a report
========================================

.. toctree::
   :maxdepth: 1

   BakersetSP
   ConvergenceTestCH4
   LoopAtomsLigands

List of Examples
****************

.. hlist::
   :columns: 2

   * :ref:`3D-RISM<example 3D-RISM>`
   * :ref:`Acetamide_SM12<example Acetamide_SM12>`
   * :ref:`Adenine_sTDA<example Adenine_sTDA>`
   * :ref:`Adenine_sTDDFT<example Adenine_sTDDFT>`
   * :ref:`AgI_SO_Pol<example AgI_SO_Pol>`
   * :ref:`AgI_asoexcit<example AgI_asoexcit>`
   * :ref:`AIM_HF<example AIM_HF>`
   * :ref:`AlCl3_efgnbo<example AlCl3_efgnbo>`
   * :ref:`ALPHA_DENSITY<example ALPHA_DENSITY>`
   * :ref:`Aromaticity<example Aromaticity>`
   * :ref:`AT_transferintegrals<example AT_transferintegrals>`
   * :ref:`Au2_Resp<example Au2_Resp>`
   * :ref:`Au2_ZORA<example Au2_ZORA>`
   * :ref:`Au10_POLTDDFT<example Au10_POLTDDFT>`
   * :ref:`AuH_analyse_exciso<example AuH_analyse_exciso>`
   * :ref:`Bader<example Bader>`
   * :ref:`Bader_Reactivity<example Bader_Reactivity>`
   * :ref:`BakersetSP<example BakersetSP>`
   * :ref:`Benzene_dimer_tshaped<example Benzene_dimer_tshaped>`
   * :ref:`Bimane_wB97X<example Bimane_wB97X>`
   * :ref:`BondOrder<example BondOrder>`
   * :ref:`BSSE_CrCO6<example BSSE_CrCO6>`
   * :ref:`C2H4_TDCDFT<example C2H4_TDCDFT>`
   * :ref:`CalcOverlapOnly<example CalcOverlapOnly>`
   * :ref:`CAMY-B3LYP_H2O<example CAMY-B3LYP_H2O>`
   * :ref:`CAMY-B3LYP_TDDFT_H2O<example CAMY-B3LYP_TDDFT_H2O>`
   * :ref:`CEBE_HI<example CEBE_HI>`
   * :ref:`CEBE_NNO<example CEBE_NNO>`
   * :ref:`CH3_CH3_etsnocv<example CH3_CH3_etsnocv>`
   * :ref:`CH4_SAOP<example CH4_SAOP>`
   * :ref:`CH4_SecDeriv<example CH4_SecDeriv>`
   * :ref:`CH4_nmrnbo<example CH4_nmrnbo>`
   * :ref:`ChargeSeparation_Toluene_TCNE<example ChargeSeparation_Toluene_TCNE>`
   * :ref:`CM5_chargemodel<example CM5_chargemodel>`
   * :ref:`CN_SecDeriv<example CN_SecDeriv>`
   * :ref:`CN_unr_exci<example CN_unr_exci>`
   * :ref:`Co_LFDFT<example Co_LFDFT>`
   * :ref:`Co_LFDFT_gtensor<example Co_LFDFT_gtensor>`
   * :ref:`CO_model<example CO_model>`
   * :ref:`ConvergenceTestCH4<example ConvergenceTestCH4>`
   * :ref:`CPL_C2H2<example CPL_C2H2>`
   * :ref:`CPL_CH3OH_NBO<example CPL_CH3OH_NBO>`
   * :ref:`CPL_HF_hybrid<example CPL_HF_hybrid>`
   * :ref:`Cu_LFDFT_gtensor<example Cu_LFDFT_gtensor>`
   * :ref:`CuH+_S-squared<example CuH+_S-squared>`
   * :ref:`DampedVerdet<example DampedVerdet>`
   * :ref:`DFTB_modes_ADF_Raman_VROA<example DFTB_modes_ADF_Raman_VROA>`
   * :ref:`Diimina_NOCV<example Diimina_NOCV>`
   * :ref:`DIMQM_CPIM_Excitations<example DIMQM_CPIM_Excitations>`
   * :ref:`DIMQM_DRF2<example DIMQM_DRF2>`
   * :ref:`DIMQM_DRF_BE<example DIMQM_DRF_BE>`
   * :ref:`DIMQM_DRF_Hyperpol<example DIMQM_DRF_Hyperpol>`
   * :ref:`DIMQM_DRF_plams<example DIMQM_DRF_plams>`
   * :ref:`DIMQM_Gradients<example DIMQM_Gradients>`
   * :ref:`DIMQM_JACOBI<example DIMQM_JACOBI>`
   * :ref:`DIMQM_LOCAL<example DIMQM_LOCAL>`
   * :ref:`DIMQM_PIM_CMM<example DIMQM_PIM_CMM>`
   * :ref:`DIMQM_PIM_Pol<example DIMQM_PIM_Pol>`
   * :ref:`DIMQM_Raman<example DIMQM_Raman>`
   * :ref:`DIMQM_READLCLFLD<example DIMQM_READLCLFLD>`
   * :ref:`DIMQM_SEROA<example DIMQM_SEROA>`
   * :ref:`Disper_HF<example Disper_HF>`
   * :ref:`DMO_CD<example DMO_CD>`
   * :ref:`DMO_ORD<example DMO_ORD>`
   * :ref:`DMO_ORD_aoresponse<example DMO_ORD_aoresponse>`
   * :ref:`DOS_Cu4CO<example DOS_Cu4CO>`
   * :ref:`EDA_meta_gga_hybrid<example EDA_meta_gga_hybrid>`
   * :ref:`EDA_Unr_C2H4_Cu_C2H4<example EDA_Unr_C2H4_Cu_C2H4>`
   * :ref:`EDA_Unr_CH3I<example EDA_Unr_CH3I>`
   * :ref:`Efield.PntQ_N2<example Efield.PntQ_N2>`
   * :ref:`EGO_CH2O_trip_constr<example EGO_CH2O_trip_constr>`
   * :ref:`EGO_CH2_sf<example EGO_CH2_sf>`
   * :ref:`EGO_H2O_multi<example EGO_H2O_multi>`
   * :ref:`EGO_N2<example EGO_N2>`
   * :ref:`EGO_N2_EIGENF<example EGO_N2_EIGENF>`
   * :ref:`EGO_PH2<example EGO_PH2>`
   * :ref:`ElectronTransfer_FDE_H2O<example ElectronTransfer_FDE_H2O>`
   * :ref:`Energy_H2O<example Energy_H2O>`
   * :ref:`Er_LFDFT_MCD<example Er_LFDFT_MCD>`
   * :ref:`ESR_HfV<example ESR_HfV>`
   * :ref:`ESR_HgF_2der<example ESR_HgF_2der>`
   * :ref:`ESR_TiF3<example ESR_TiF3>`
   * :ref:`evGW_H2O<example evGW_H2O>`
   * :ref:`FDE_CPL_NH3-H2O<example FDE_CPL_NH3-H2O>`
   * :ref:`FDE_Energy_H2O-Ne_unrestricted<example FDE_Energy_H2O-Ne_unrestricted>`
   * :ref:`FDE_Energy_NH3-H2O<example FDE_Energy_NH3-H2O>`
   * :ref:`FDE_H2O_128<example FDE_H2O_128>`
   * :ref:`FDE_HeCO2_freezeandthaw<example FDE_HeCO2_freezeandthaw>`
   * :ref:`FDE_NMR_relax<example FDE_NMR_relax>`
   * :ref:`Fe4S4_BrokenSymm<example Fe4S4_BrokenSymm>`
   * :ref:`Field_PtCO<example Field_PtCO>`
   * :ref:`Formamide_CVnDFT<example Formamide_CVnDFT>`
   * :ref:`FQQM_aoresponse<example FQQM_aoresponse>`
   * :ref:`FQQM_response<example FQQM_response>`
   * :ref:`FQQM_scf<example FQQM_scf>`
   * :ref:`FQQM_td<example FQQM_td>`
   * :ref:`Frags_NiCO4<example Frags_NiCO4>`
   * :ref:`Frags_PtCl4H2<example Frags_PtCl4H2>`
   * :ref:`FranckCondon_NO2<example FranckCondon_NO2>`
   * :ref:`Freq_NH3<example Freq_NH3>`
   * :ref:`Freq_NH3_RAMAN<example Freq_NH3_RAMAN>`
   * :ref:`Freq_NH3_Scan<example Freq_NH3_Scan>`
   * :ref:`Freq_UF6<example Freq_UF6>`
   * :ref:`G3W2_H2O<example G3W2_H2O>`
   * :ref:`GO_FDE_H2O-Li<example GO_FDE_H2O-Li>`
   * :ref:`GO_H2O<example GO_H2O>`
   * :ref:`GO_LiF_Efield<example GO_LiF_Efield>`
   * :ref:`GO_constraints<example GO_constraints>`
   * :ref:`GO_restraint<example GO_restraint>`
   * :ref:`green_Al<example green_Al>`
   * :ref:`green_Au<example green_Au>`
   * :ref:`green_BDT<example green_BDT>`
   * :ref:`green_WBL<example green_WBL>`
   * :ref:`GW_H2O<example GW_H2O>`
   * :ref:`GW_O3<example GW_O3>`
   * :ref:`GW_Phenol<example GW_Phenol>`
   * :ref:`H2O_ADFNBO<example H2O_ADFNBO>`
   * :ref:`H2O_HF_freq<example H2O_HF_freq>`
   * :ref:`H2O_MCD<example H2O_MCD>`
   * :ref:`H2O_MCD_ZFS<example H2O_MCD_ZFS>`
   * :ref:`H2O_SO_HDA<example H2O_SO_HDA>`
   * :ref:`H2O_TD_magnet<example H2O_TD_magnet>`
   * :ref:`H2O_Verdet<example H2O_Verdet>`
   * :ref:`H2O_magnet<example H2O_magnet>`
   * :ref:`H2PO_B3LYP<example H2PO_B3LYP>`
   * :ref:`HBr<example HBr>`
   * :ref:`HCN<example HCN>`
   * :ref:`HF_ResonanceRaman<example HF_ResonanceRaman>`
   * :ref:`HgI2<example HgI2>`
   * :ref:`Hg_Mossbauer_X2C<example Hg_Mossbauer_X2C>`
   * :ref:`HgMeBr_pnr<example HgMeBr_pnr>`
   * :ref:`HgMeBr_psc<example HgMeBr_psc>`
   * :ref:`HgMeBr_zso<example HgMeBr_zso>`
   * :ref:`HI_EFG<example HI_EFG>`
   * :ref:`HI_Raman<example HI_Raman>`
   * :ref:`HI_SecDer_ZORA<example HI_SecDer_ZORA>`
   * :ref:`Hplus_CO_etsnocv<example Hplus_CO_etsnocv>`
   * :ref:`Hyperpol<example Hyperpol>`
   * :ref:`I2_SO_MP2<example I2_SO_MP2>`
   * :ref:`InitHess<example InitHess>`
   * :ref:`IQA<example IQA>`
   * :ref:`LCY-BP_H2O<example LCY-BP_H2O>`
   * :ref:`LiH_DampedBeta<example LiH_DampedBeta>`
   * :ref:`LiH_DampedGamma<example LiH_DampedGamma>`
   * :ref:`LoCOSMO_H2O-NH3<example LoCOSMO_H2O-NH3>`
   * :ref:`LoCOSMO_H2O-NH3_TDDFT<example LoCOSMO_H2O-NH3_TDDFT>`
   * :ref:`LocMO_Resp<example LocMO_Resp>`
   * :ref:`LoopAtomsLigands<example LoopAtomsLigands>`
   * :ref:`MBH_CH4<example MBH_CH4>`
   * :ref:`MBH_Ethanol<example MBH_Ethanol>`
   * :ref:`methane_dimer_dispersion<example methane_dimer_dispersion>`
   * :ref:`MM_Dispersion<example MM_Dispersion>`
   * :ref:`ModStPot_N2+<example ModStPot_N2+>`
   * :ref:`Mossbauer<example Mossbauer>`
   * :ref:`MP2_Li<example MP2_Li>`
   * :ref:`Multiresolution_H2O<example Multiresolution_H2O>`
   * :ref:`N2_TDHF<example N2_TDHF>`
   * :ref:`NaCl_ionicbonding<example NaCl_ionicbonding>`
   * :ref:`NaCl_pairbonding<example NaCl_pairbonding>`
   * :ref:`Naphthalene_VST<example Naphthalene_VST>`
   * :ref:`Ne_CoreExci<example Ne_CoreExci>`
   * :ref:`Ne_exciso<example Ne_exciso>`
   * :ref:`NH_ZFS<example NH_ZFS>`
   * :ref:`NH3_HDA<example NH3_HDA>`
   * :ref:`NH3_POLTDDFT<example NH3_POLTDDFT>`
   * :ref:`NMR_B3LYP<example NMR_B3LYP>`
   * :ref:`NMR_NICS<example NMR_NICS>`
   * :ref:`NOCV_CrCO5-CH2<example NOCV_CrCO5-CH2>`
   * :ref:`OH_MetaGGA<example OH_MetaGGA>`
   * :ref:`PCCP_Unr_BondEnergy<example PCCP_Unr_BondEnergy>`
   * :ref:`PbF_excisou<example PbF_excisou>`
   * :ref:`PbH4_finitenuc<example PbH4_finitenuc>`
   * :ref:`pdb2adf<examples QMMM>`
   * :ref:`PdH_ESR_X2C<example PdH_ESR_X2C>`
   * :ref:`Phenylnitrene_ZFS<example Phenylnitrene_ZFS>`
   * :ref:`Pr_LFDFT<example Pr_LFDFT>`
   * :ref:`PyFrag<example PyFrag>`
   * :ref:`Pyridine_CAM-B3LYP<example Pyridine_CAM-B3LYP>`
   * :ref:`QM/MM<examples QMMM>`
   * :ref:`qsGW_N2<example qsGW_N2>`
   * :ref:`Quild<examples Quild>`
   * :ref:`RPA_H2O<example RPA_H2O>`
   * :ref:`RPA-SOSSX_H2O<example RPA-SOSSX_H2O>`
   * :ref:`SCF_Ti2O4<example SCF_Ti2O4>`
   * :ref:`SD_CrNH3_6<example SD_CrNH3_6>`
   * :ref:`SiH2_spinflip<example SiH2_spinflip>`
   * :ref:`SO_ZORA_Bi2<example SO_ZORA_Bi2>`
   * :ref:`Solv_HCl<example Solv_HCl>`
   * :ref:`SUBEXCI_dimer<example SUBEXCI_dimer>`
   * :ref:`TCNE-Benzene_wB97<example TCNE-Benzene_wB97>`
   * :ref:`TD-DFTB_betacarotene<example TD-DFTB_betacarotene>`
   * :ref:`TiCl4_CoreExci<example TiCl4_CoreExci>`
   * :ref:`TiCl4_XASXES<example TiCl4_XASXES>`
   * :ref:`TlH_SO_analysis<example TlH_SO_analysis>`
   * :ref:`Tl_noncollinear<example Tl_noncollinear>`
   * :ref:`Transit_H2O<example Transit_H2O>`
   * :ref:`TSRC_SN2<example TSRC_SN2>`
   * :ref:`TS_C2H6<example TS_C2H6>`
   * :ref:`TS_CH4_HgCl2<example TS_CH4_HgCl2>`
   * :ref:`Twist_Ethene_TDDFT<example Twist_Ethene_TDDFT>`
   * :ref:`UnrFrag_H2<example UnrFrag_H2>`
   * :ref:`VCD_CHFClBr_DZP<example VCD_CHFClBr_DZP>`
   * :ref:`VCD_COG_NHDT<example VCD_COG_NHDT>`
   * :ref:`VO_collinear<example VO_collinear>`
   * :ref:`VROA<example VROA>`
   * :ref:`VROA_RESO<example VROA_RESO>`
   * :ref:`Water_MeOH_B2GPPLYP<example Water_MeOH_B2GPPLYP>`
   * :ref:`Water_MeOH_DODSCAN<example Water_MeOH_DODSCAN>`
   * :ref:`Water_MP2_AO<example Water_MP2_AO>`
   * :ref:`WaterDimer<example WaterDimer>`
   * :ref:`WaterDimer_SOS-MP2_AO<example WaterDimer_SOS-MP2_AO>`
   * :ref:`XCDFT_FDE_ET_ethylene<example XCDFT_FDE_ET_ethylene>`
   * :ref:`XCFUN_FULLKERNEL_TDDFT_H2O<example XCFUN_FULLKERNEL_TDDFT_H2O>`
   * :ref:`XCFUN_TDDFT_H2O<example XCFUN_TDDFT_H2O>`
