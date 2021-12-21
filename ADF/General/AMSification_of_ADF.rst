.. _AMSIFICATION:

AMSification of ADF
*******************

Restructuring of the input
==========================

The input for the following features belongs (mostly) to the `AMS driver <../../AMS/index.html>`__ part of the input:

* `Geometry, System definition <../../AMS/System.html>`__

  * Geometry
  * Total charge
  * Masses of atoms (isotopes)
  * Electric field, point charges
  * Regions

* `Structure and Reactivity, Molecular Dynamics <../../AMS/Tasks/TOC.html>`__

  * Geometry Optimizations 
  * Linear Transit (LT), Transition States (TS), Nudged Elastic Band (NEB), TSRC
  * Intrinsic Reaction Coordinate (IRC)
  * Constraints, restraints
  * Excited state optimizations
  * Molecular Dynamics

* `Gradients, Hessian, Thermodynamics <../../AMS/Gradients_Stress_Elasticity.html>`__

  * Nuclear gradients, Hessian, PES point character
  * Thermodynamics, gas phase Gibbs free energy

* `Vibrational Spectroscopy <../../AMS/Vibrational_Spectroscopy.html>`__

  * IR frequencies and intensities
  * Mobile Block Hessian (MBH),  Mode Scanning, Mode Refinement, Mode Tracking
  * (Resonance) Raman, vibrational Raman optical activity (VROA)
  * Vibrational Circular Dichroism (VCD)

* `Vibrational resolved electronic spectra <../../AMS/Vibrationally_resolved_electronic_spectra.html>`__

  * Vibrational resolved absorption, emission, phosphorescence, ionization
  * Adiabatic Hessian Franck-Condon
  * Vertical Gradient Franck-Condon

The input for QM/MM, QM/QM, Quild calculations uses the Hybrid engine

* Model Hamiltonians

  * `QM/MM, QM/QM, Quild <../../Hybrid/index.html>`__

The input for most other features belongs to the ADF engine part of the input.

Restructuring of input keys
===========================

.. csv-table:: 
   :header: "ADF2019 key / feature", "ADF2020 key / AMS2020 key / comments"

      $ADFBIN                       , $AMSBIN
      $ADFHOME                      , $AMSHOME
      $ADFRESOURCES                 , $AMSRESOURCES=$AMSHOME/atomicdata
      $ADFHOME/atomicdata           , $AMSHOME/atomicdata/ADF. Directory with ADF basis sets.
      $ADFHOME/atomicdata/ZORA      , $AMSHOME/atomicdata/ADF/ZORA. Directory with ADF ZORA basis sets.
      'ANALYTICALFREQ'              , subkey 'NormalModes' of key 'Properties' in |AMS|.
      'AORESPONSE'                  , subkey 'FreqRange' and 'Frequency' removed. Use new subkey 'Frequencies'.
      'ATOMPROPS'                   , key removed. See :ref:`alternative elements<Alternative Elements>`.
      'ATOMS'                       , subkey 'Atoms' of key 'System' in |AMS|.
       ...  f=fragtype/n            , ...  adf.f=fragtype|n.
       ...  R=CosmoRadius           , ...  adf.R=CosmoRadius.
      'CHARGE'                      , subkey 'Charge' of key 'System' in |AMS|. key 'SpinPolarization' in ADF.
      'CONSTRAINTS'                 , key 'Constraints' in |AMS|.
      'COLLINEAR'                   , subkey 'SpinOrbitMagnetization Collinear' in key 'Relativity' in ADF.
      'CRDFILEXYZ'                  , key removed.
      'CRDFILEMOL'                  , key removed.
      EField                        , subkey 'ElectroStaticEmbedding%ElectricField' of key 'System' in |AMS|.
      fcf                           , program 'fcf' documented in |AMS|
      'GEOMETRY'                    , key 'Task' and key 'Properties' in |AMS|.
      Geometry optimization         , key 'Task GeometryOptimization' in |AMS|.
      'GEOVAR'                      , key removed.
      'GRADIENT'                    , subkey 'Gradients' of key 'Properties' in |AMS|.
      'HESSDIAG'                    , key removed.
      'HESSTEST'                    , key removed.
      Initial Hessian               , subkey 'InitialHessian' of key 'GeometryOptimization' in |AMS|.
      Intrinsic Reaction Coordinate , key 'Task IRC' in |AMS|.
      IR frequencies                , subkey 'NormalModes' of key 'Properties' in |AMS|.
      ... Mobile Block Hessian      , subkey 'Displacements Block' of key 'NormalModes' in |AMS|.
      ... symmetric displacements   , subkey 'Displacements Symmetric' of key 'NormalModes' in |AMS|.
      'IRCSTART'                    , key removed.
      'ISOTOPICSHIFT'               , key removed.
      Linear Transit                , key 'Task PESScan' in |AMS|.
      'LINEARCONSTRAINTS'           , key removed.
      MBH                           , subkey 'Displacements Block' of key 'NormalModes' in |AMS|.
      'MP2'                         , key 'MBPT'.
      'NONCOLLINEAR'                , subkey 'SpinOrbitMagnetization NonCollinear' in key 'Relativity' in ADF.
      Nudged Elastic Band           , key 'Task NEB' in |AMS|.
      Partial Hessian               , subkey 'SelectedRegionForHessian' and 'NormalModes' of key 'Properties' in |AMS|.
      'POINTCHARGES'                , subkey 'ElectroStaticEmbedding%MultipolePotential' of key 'System' in |AMS|.
      'POLTDDFT'                    , subkey 'NFreq' and 'NGrid' added.
      'QMMM'                        , `Hybrid engine <../../Hybrid/index.html>`__.
      QM/MM; QM/QM; Quild           , `Hybrid engine <../../Hybrid/index.html>`__.
      Raman                         , subkey 'Raman' of key 'Properties' in |AMS|.
      'RELATIVISTIC'                , block key 'Relativity' in ADF.
      'RESPONSE'                    , "subkey 'FrqBeg', 'FrqEnd, and 'NFreq' removed. Use new subkey 'Frequencies'."
      'RESTRAINT'                   , key 'Restraints' in |AMS|.
      'Restart'                     , The file should be specified in 'EngineRestart' in |AMS|
      'SYMMETRY'                    , both in ADF and |AMS|.
      symmetrization                , ADF does not symmetrize anymore. Subkey 'Symmetrize' of key 'System' in |AMS|.
      'THERMO'                      , key 'Thermo' in |AMS|.
      Transit State search          , key 'Task TransitionStateSearch' in |AMS|.
      'UNITS'                       , key removed. Possibility added to add units for many keys.
      VCD                           , subkey 'VCD' of key 'Properties' in |AMS|.
      vcdtools                      , program 'vcdtools' documented in |AMS|
      VIBRON module                 , VIBRON module removed. For resonance Raman application see |AMS|.
      VROA                          , subkey 'VROA' of key 'Properties' in |AMS|.

Example shell script changes
============================

The example below shows how a shell script for ADF2019 is converted to ADF2020 (see also :ref:`automatic_conversion`).

**ADF2019 shell script (obsolete):**

.. code-block:: none

  #!/bin/sh

  # This is a shell script for ADF2019 which will not work for ADF2020

  $ADFBIN/adf <<eor
     Title WATER Geometry Optimization
     Atoms
        O             0.000000     0.000000     0.000000
        H             0.000000    -0.689440    -0.578509
        H             0.000000     0.689440    -0.578509
     End
     Geometry
        Converge grad=1e-4
     End
     Basis
        Type TZP
     End
     XC
        GGA PBE
     End
  eor


**ADF2020 shell script:**

.. code-block:: none

   #!/bin/sh

   # This is a shell script for ADF2020

   # You should use '$ADFBIN/ams' instead of '$ADFBIN/adf'

   $ADFBIN/ams <<eor
      # Input options for the AMS driver: 

      System
         Atoms
            O             0.000000     0.000000     0.000000
            H             0.000000    -0.689440    -0.578509
            H             0.000000     0.689440    -0.578509
         End
      End
      Task GeometryOptimization
      GeometryOptimization
         Convergence gradients=1e-4
      End

      # The input options for ADF, which are described in this manual, 
      # should be specified in the 'Engine ADF' block:

      Engine ADF
         Basis
            Type TZP
         End
         XC
            GGA PBE
         End
      EndEngine
   eor

.. _automatic_conversion:

Automatic tool for conversion of ADF2019 shell scripts
======================================================

The executable ``$AMSBIN/adf`` no longer performs ADF calculations. Instead, it will call an **input-conversion tool** [#conversion]_ which will automatically convert an ADF2019 input into an ADF2020 input. 

For example, if you save and execute the following script (note that the ``$AMSBIN/adf`` executable is used):

.. code-block:: bash
   :emphasize-lines: 6

   #!/bin/sh

   # This is a shell scripts of an ADF2019 calculation, which will not work for ADF2020
   # If you execute this script, the ADF2019 input will be converted into an ADF2020 input.

   $AMSBIN/adf <<eor
      Atoms
         O             0.000000     0.000000     0.000000
         H             0.000000    -0.689440    -0.578509
         H             0.000000     0.689440    -0.578509
      End
   
      Basis
         Type TZP
      End
   eor

no ADF calculation will actually be performed. Instead, the input conversion tool will be called, and you will obtain the new shell script for ADF2020 (note the ``$AMSBIN/ams`` executable):

.. code-block:: bash
  :emphasize-lines: 21

  # =========
  # IMPORTANT
  # =========

  # Starting from AMS2020, ADF can only be used through the AMS driver program.
  # Many input options for ADF have changed since the 2019 version.
  # Below you will find an automatically-converted input script for AMS2020.
  # The automatic conversion is not 100% accurate, so double check your input!

  #          ==================================================
  #          Automatic conversion of ADF-2019 input to AMS-2020
  #          ==================================================
  
  # === NOTES ===
  # - "TAPE21" is now called "adf.rkf" and is located in AMS results folder (by default "ams.results")
  # - Unlike ADF2019, AMS does not symmetrize the structure by default. See "System -> Symmetrize" in the AMS driver manual.
  # - The AMS default symmetrization tolerance is larger than the ADF2019 one. See "Symmetry -> SymmetrizeTolerance" in the AMS driver manual.
  # - Scalar relativistic effects (ZORA) are included by default in the 2020 version of ADF.


  $AMSBIN/ams << eor
  System
    Atoms
      O      0.0000000000      0.0000000000      0.0000000000 
      H      0.0000000000     -0.6894400000     -0.5785090000 
      H      0.0000000000      0.6894400000     -0.5785090000 
    End
    Symmetrize True
  End

  Symmetry
    SymmetrizeTolerance 0.001
  End

  Engine ADF
    Relativity
      Level None
    End

    Basis
      Type TZP
    End
  EndEngine

  eor

The conversion tool might raise ``WARNINGS``. Make sure to address them before using the converted the script!

.. [#conversion] You can find the actual python script that performs the ADF2019 to ADF2020 conversion in ``$AMSHOME/Utils/adf_to_ams_input_converter.py``.


Input, execution and output
***************************

See the AMS driver documentation:

* `Input, execution and output section of the AMS driver manual <../../AMS/Input_Output.html>`__

ADF specific files
==================

The ADF engine may generate several output / result files, along that ADF writes part of the standard output file.
The most important one is adf.rkf (previously ADF<=2019 known as TAPE21 or as a .t21 file), the general result file.
The adf.rkf contains relevant information about the outcome of the calculation.
It is a binary file that contains a lot of information about the calculation, such as the one-electron orbitals expressed in the basis functions.
It can be used as a fragment file for subsequent calculations, or can be used as input to a property program, like NMR, CPL, or LFDFT.

Files attached to the job, such as fragment files, are by default also assumed to exist in the directory where you start AMS.
You must take care to move or copy required files to that directory before starting the calculation, or to provide via input adequate information to the program where to find the files. In many cases you can specify a complete path to the file. 

Most files that are generated by the program, in particular the standard result file that can be used as a fragment file in other calculations, are *binary* files.
A binary file should usually not be moved from one machine to another, i.e. it may not be readable by another machine than the one that generated the file, unless the two machines are of the same type. The ADF package provides utilities to convert the ADF binary result files from binary to ASCII, and vice versa, so that you don't have to regenerate your fragment libraries when going to another machine.
See the `Scripting Section <../../Scripting/Commandline_Tools/KF_command_line_utilities.html>`_ for further details regarding such aspects.

ADF is an engine that lends itself particularly well for chemical analysis. This is a direct result of the fragment-based approach, where properties of the molecule are related to the properties of the constituent fragments, which is precisely how the chemist thinks. Molecular Orbitals are (optionally) analyzed extensively as how they are composed from occupied and virtual fragment orbitals. This inherently implies a large amount of output. Even computations on small molecules may produce startlingly many pages of output. This is not necessarily so because you can regulate the production of output in detail. Obviously, some kind of *default* production of output had to be implemented. The field of ADF users is so wide and diverse that it is hard to satisfy everybody as regards this default level of output. Depending on your purposes the automatic settings, which determine how much output is generated without instructions to the contrary, may yield boringly many numbers that you just skip through in search for the one value you're interested in, or it may be widely insufficient. Therefore, take notice of the possibilities to regulate output. 

Above all, however get familiar with the analysis tools that ADF provides to see in what ways these may help to interpret your results. In a later chapter a global description of output is given as it is normally produced. The chapter below gives an introduction in some of the essential features of ADF, which may be sufficiently different from what you are used to in other Quantum Chemistry codes to deserve your attention.

.. |AMS| replace:: `AMS driver <../../AMS/index.html>`__
