.. _Examples:

Examples
########

Introduction
============

The ADF package contains a series of sample runs for the BAND program. Provided are UNIX scripts to run the calculations and the resulting output files.  

The examples serve: 

+  To check that the program has been installed correctly: run the sample inputs and compare the results with the provided outputs. *Read the remarks below about such comparisons.*

+  To demonstrate how to do calculations: an illustration to the User manuals. The number of options available in BAND is substantial and the sample runs do not cover all of them. They should be sufficient, however, to get a feeling for how to explore the possibilities.

+  To work out special applications that do not fit well in the User's Guide.

Where references are made to the operating system (OS) and to the file system on your computer the terminology of UNIX type OSs is used.

All sample files are stored in subdirectories under $AMSHOME/examples/, where $AMSHOME is the main directory of the ADF package. The main subdirectory for the BAND examples is $AMSHOME/examples/band. Each sample run has its own directory. For instance, $AMSHOME/examples/band/NaCl/ contains a BAND calculation on the NaCl bulk crystal. Each sample subdirectory contains: 

+  A file TestName.run: the UNIX script to execute the calculation or sequence of calculations of the example

+  A file TestName_orig.out: the resulting output(s) against which you can compare the outcome of your own calculation.

Notes: 

+  Running the examples on Windows: You can run an example calculation by double-clicking on the appropriate .run file.  After the calculation has finished, you can compare the TestName.out file with the  reference TestName_orig.out file. See remarks about comparing output files below. 

+  The UNIX scripts make use of the *rm* (remove) command. Some UNIX users may have aliased the *rm* command. They should accordingly adapt these commands in the sample scripts so as to make sure that the scripts will remove the files. New users may get stuck initially because of files that are lingering around after an earlier attempt to run one of the examples. In a subsequent run, when the program tries to open a similar (temporary or result) file again, an error may occur if such a file already exists. Always make sure that no files are left in the run-directory except those that are required specifically.

+  It is a good idea to run each example in a separate directory that contains no other important files.  

+  The run-scripts use the environment variables AMSBIN and AMSRESOURCES. They stand respectively for the directory that contains the program executables and the main directory of the database.  To use the scripts as they are you must have defined the variables AMSBIN and AMSRESOURCES in your environment. If a parallel (PVM or MPI) version has been installed, it is preferable to have also the environment variable NSCM. This defines the default number of parallel processes that the program will try to use. Consult the Installation Manual for details.

+  As you will note the sample run scripts refer to the programs by names like 'adf', 'band', and so on. When you inspect your $AMSBIN directory, however, you may find that the program executables have names 'adf.exe', 'band.exe'. There are also files in $AMSBIN with names 'adf', 'band', but these are in fact scripts to execute the binaries. We strongly recommend that you use these scripts in your calculations, in particular when running parallel jobs: the scripts take care of some aspects that you have to do otherwise yourself in each calculation.

+  You need a license file to run any calculations successfully. If you have troubles with your license file, consult the Installation manual. If that doesn't help contact us at support@scm.com

Many of the provided samples have been devised to be short and simple, at the expense of physical or chemical relevance and precision or general quality of results. They serve primarily to illustrate the use of input, necessary files, and type of results. The descriptions have been kept brief. Extensive information about using keywords in input and their implications is given in the User's Guide and the Utilities and Property Programs documents (NMR, DIRAC, and other utility programs). 

When you compare your own results with the sample outputs, you should check in particular (as far as applicable): 

+ Occupation numbers and energies of the one-electron orbitals;

+ The optimized geometry;

+ Vibrational frequencies;

+ The bonding energy and the various terms in which it has been decomposed;

+ The dipole moment;

+ The logfile. At the end of a calculation the logfile is automatically appended (by the program itself) to the standard output.

General remarks about comparisons: 

+  For technical reasons, discussion of which is beyond the scope of this document, differences between results obtained on different machines, or with different numbers of parallel processes, may be much larger than you would expect.  They may significantly exceed the machine precision. What you should check is that they fall well (by at least an order of magnitude) within the *numerical integration* precision used in the calculation.

+  For similar reasons the orientation of the molecule used by the program may be different on different machines, even when the same input is supplied. In such cases the different orientations should be related and only differ in some trivial way, such as by a simple rotation of all coordinates by 90 degrees around the z-axis. When in doubt, contact an ADF representative.

+  A BAND run may generate, apart from result files that you may want to save, a few scratch files. The UNIX scripts that run the samples take care of removing these files after the calculations have finished, to avoid that the program aborts in the next run by attempting to open a 'new' file that is found to exist already.

+  A sample calculation may use one or more data files, in particular *fragment* files. The samples are self-contained: they first run the necessary pre-calculations to produce the fragment files. In 'normal' research work you may have libraries of fragments available, first for the 'basic atoms', and later, as projects are developing, also for larger fragments so that you can start immediately on the actual system by attaching the appropriate fragment files.

Default settings of print options result in a considerable amount of output. This is also the case in some of the sample runs, although in many of them quite a bit of 'standard' output is suppressed by inserting applicable print control keys in the input file. Consult the User's Guide about how to regulate input with keys in the input file. 


Model Hamiltonians
==================

.. toctree::
   :maxdepth: 1
   
   BetaIron
   BFieldLdotB
   Graphene_Dispersion
   HonPerovskite_Solvation
   EField
   FiniteNucleus
   NiO_Hubbard
   ZnS_ModelPotential
   DFTHalf_Si


Precision and performance
=========================

.. toctree::
   :maxdepth: 1

   BasisDefaults
   Peptide_NumericalQuality
   Multiresolution_H2O
   BSSE
   BandAutomations


Restarts
========

.. toctree::
   :maxdepth: 1

   RestartSCF
   RestartProperties
   BeO_tape41


NEGF
====

.. toctree::
   :maxdepth: 1

   NEGF_Cr_wire
   NEGF_bias
   NEGF_Conductance


Structure and Reactivity
========================

.. toctree::
   :maxdepth: 1

   NaCl
   COChainFreqTS
   H_ref
   BNForce
   H2BulkGeo


Time dependent DFT
==================

.. toctree::
   :maxdepth: 1

   NewResp_2DMoS2Restart
   NewResp_3DCopper
   NewResp_PlotInducedDensity
   OldResp_Diamond


Spectroscopy
============

.. toctree::
   :maxdepth: 1

   TiF3a
   TiF3g
   PE-NMR
   SnO_EFG
   GraphenePhonons


Analysis
========

.. toctree::
   :maxdepth: 1

   Frags_COCu
   GridKey
   PEDA_0D_PtCl4H2
   PEDA_MgO+CO
   PEDANOCV_MgO+CO
   Li2O_Bader
   PropertiesAtNuclei
   Li_BZPlot
   EffectiveMass
   Si_ElectronHole
   BNSlabLDOS


List of Examples
================

.. hlist::
   :columns: 3

   * :ref:`BasisDefaults <example BasisDefaults>`
   * :ref:`BeO_tape41 <example BeO_tape41>`
   * :ref:`BetaIron <example BetaIron>`
   * :ref:`BFieldLdotB <example BFieldLdotB>`
   * :ref:`BNForce <example BNForce>`
   * :ref:`BSSE <example BSSE>`
   * :ref:`COChainFreqTS <example COChainFreqTS>`
   * :ref:`EffectiveMass<example EffectiveMass>`
   * :ref:`EField<example EField>`
   * :ref:`FiniteNucleus<example FiniteNucleus>`
   * :ref:`Frags_COCu<example Frags_COCu>`
   * :ref:`Graphene_Dispersion<example Graphene_Dispersion>`
   * :ref:`GraphenePhonons<example GraphenePhonons>`
   * :ref:`GridKey <example GridKey>`
   * :ref:`H2BulkGeo<example H2BulkGeo>`
   * :ref:`H_ref<example H_ref>`
   * :ref:`HonPerovskite_Solvation<example HonPerovskite_Solvation>`
   * :ref:`Li2O_Bader<example Li2O_Bader>`
   * :ref:`Li_BZPlot<example Li_BZPlot>`
   * :ref:`Multiresolution_H2O<example Multiresolution_H2O>`
   * :ref:`NaCl<example NaCl>`
   * :ref:`NEGF <example NEGF_Cr_wire>`
   * :ref:`NEGF with bias <example NEGF_bias>`
   * :ref:`NEGF_Conductance <example NEGF_Conductance>`
   * :ref:`NewResp_3DCopper <example NewResp_3DCopper>`
   * :ref:`NewResp_PlotInducedDensity <example NewResp_PlotInducedDensity>`
   * :ref:`NewResponse for 2D Slab <example NewResp_2DMoS2Restart>`
   * :ref:`NiO_Hubbard<example NiO_Hubbard>`
   * :ref:`OldResp_Diamond<example OldResp_Diamond>`
   * :ref:`PE-NMR<example PE-NMR>`
   * :ref:`PEDA <example PEDA_MgO+CO>`
   * :ref:`PEDANOCV <example PEDANOCV_MgO+CO>`
   * :ref:`Peptide_NumericalQuality<example Peptide_NumericalQuality>`
   * :ref:`PropertiesAtNuclei<example PropertiesAtNuclei>`
   * :ref:`Restart a SCF <example RestartSCF>`
   * :ref:`Restart for Properties<example RestartProperties>`
   * :ref:`Si_ElectronHole<example Si_ElectronHole>`
   * :ref:`SnO_EFG<example SnO_EFG>`
   * :ref:`TiF3a<example TiF3a>`
   * :ref:`TiF3g<example TiF3g>`
   * :ref:`ZnS_ModelPotential<example ZnS_ModelPotential>`
