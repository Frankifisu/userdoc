Example inputfiles
##################

A set with many more examples is provided in the $AMSHOME/examples/quild directory.

Vibrational frequencies for multi-level QM/QM scheme
****************************************************

.. code-block:: shell

   $AMSBIN/quild << eor
   ATOMS
    C               -0.759255999    0.032048841    0.000000000
    C                0.759255999   -0.032048841    0.000000000
    H               -1.179949313   -0.464915468    0.890460461
    H               -1.179949313   -0.464915468   -0.890460461
    H               -1.115011042    1.076188400    0.000000000
    H                1.179949313    0.464915468    0.890460461
    H                1.179949313    0.464915468   -0.890460461
    H                1.115011042   -1.076188400    0.000000000
   END

   GEOMETRY
    Frequencies
   END

   AnalyticalFreq
   End

   Integration 7.0 7.0
   SCF
    converge 1.0e-7 1.0e-7
    diis ok=0.01
   END

   QUILD
     NR_REGIONS=2

     REGION 1
       1-8
     SUBEND

     REGION 2
       2 6-8
     SUBEND

     DESCRIPTION 1 ADF
       BASIS
         type DZ
         core Large
       END
     SUBEND

     DESCRIPTION 2 ADF  ! adding NUMFREQ would use numerical Hessian
                        ! (not necessary in this case,
                        ! because Analytical Hessian is available)
       BASIS
         type TZP
         core Large
       END
     SUBEND

     INTERACTIONS
        TOTAL description 1
        REPLACE region 2  description 2 for description 1
     SUBEND
   END
   END INPUT
   eor
   rm quildjob*

Symmetry rotation with T\ :sub:`d`  symmetry for geometry and C\ :sub:`2v`  for orbitals
*****************************************************************************************

.. code-block:: shell

   $AMSBIN/quild << eor
   Title JCTC systems

   Occupations smearq=0.0 &
           A1          10.0     //      9.0
           A2           3.0     //      2.0
           B1           6.0     //      5.0
           B2           6.0     //      5.0
   End

   Symmetry C(2v)

   QUILD
    Symgeo T(d)
    Symrot
      -0.7071067811865475 -0.7071067811865475 0.0
      -0.7071067811865475  0.7071067811865475 0.0
       0.0 0.0 1.0
    Subend
   End

   Atoms
    Fe               0.000000000    0.000000000    0.000000000
    Cl              -1.326583289    1.326583289    1.326583289
    Cl              -1.326583289   -1.326583289   -1.326583289
    Cl               1.326583289    1.326583289   -1.326583289
    Cl               1.326583289   -1.326583289    1.326583289
   End

   Geometry
   End

   Charge -2 4
   Unrestricted

   XC
    LDA VWN
    GGA OPBE
   END

   BASIS
    type TZ2P
    core SMALL
   END

   SCF
    converge 1.0e-6 1.0e-6
    iterations 99
    diis ok=0.01
   END

   INTEGRATION 6.0 6.0

   EPRINT
    SFO noeig noovl
   END

   endinput
   eor

Optimization with B3LYP through the post-SCF METAGGA scheme
***********************************************************

.. code-block:: shell

   $AMSBIN/quild << eor
   title Geometry optimization
   EPRINT
    SFO NOEIG NOOVL
   END
   XC
    GGA BLYP
   END
   ATOMS
   O      .000000     .000000     .000000
   C      .000000     .000000    1.128100
   END
   BASIS
    type DZ
    core NONE
   END
   GEOMETRY
   END
   SCF
    diis ok=0.01
    converge 1.0e-5 1.0e-5
   END
   QUILD
     cvg_grd 1.0e-4
     numgrad 1
     SMETAGGA B3LYP(VWN5)
   END
   METAGGA
   HFEXCHANGE
   INTEGRATION 5.0 5.0
   endinput
   eor

Optimization with B3LYP as SCF functional
*****************************************

.. code-block:: shell

   $AMSBIN/quild << eor
   title Geometry optimization
   EPRINT
    SFO NOEIG NOOVL
   END
   XC
    HYBRID B3LYP
   END
   ATOMS
   O      .000000     .000000     .000000
   C      .000000     .000000    1.128100
   END
   BASIS
    type DZ
    core NONE
   END
   GEOMETRY
   END
   SCF
    diis ok=0.01
    converge 1.0e-5 1.0e-5
   END
   QUILD
     cvg_grd 1.0e-4
     numgrad 2
   END
   INTEGRATION 5.0 5.0
   endinput
   eor

Geometry optimization with QM/MM treatment of water dimer
*********************************************************

.. code-block:: shell

   TITLE QM/MM calculation setup by pdb2adf: M.Swart, 2005

   GEOMETRY
   END

   ATOMS
   O      0.0000     0.0000     0.0000
   H     -0.5220     0.2660    -0.7570
   H     -0.5220     0.2660     0.7570
   O      0.0000    -3.2000     0.0000
   H      0.0570    -2.2440     0.0000
   H      0.9110    -3.4950     0.0000
   END

   QUILD
     NR_REGIONS=2

     INTERACTIONS
       TOTAL     description 1
       REPLACE region 1   description 3 for description 2
     SUBEND

     REGION 1
       1-3
     SUBEND
     REGION 2
       4-6
     SUBEND

     DESCRIPTION 1 NEWMM
       QMMM
         FORCE_FIELD_FILE $AMSRESOURCES/ForceFields/amber95.ff
         MM_CONNECTION_TABLE
           1 OW  QM     2     3
           2 HW  QM     1
           3 HW  QM     1
           4 OW  MM     5     6
           5 HW  MM     4
           6 HW  MM     4
         SUBEND
         CHARGES
           1  -0.8340
           2   0.4170
           3   0.4170
           4  -0.8340
           5   0.4170
           6   0.4170
         SUBEND
       END
     SUBEND

     DESCRIPTION 2 NEWMM
       QMMM
         FORCE_FIELD_FILE $AMSRESOURCES/ForceFields/amber95.ff
         MM_CONNECTION_TABLE
           1 OW  QM     2     3
           2 HW  QM     1
           3 HW  QM     1
         SUBEND
         CHARGES
           1  -0.8340
           2   0.4170
           3   0.4170
         SUBEND
       END
     SUBEND

     DESCRIPTION 3
       EPRINT
         SFO NOEIG NOOVL
       END
       XC
        GGA Becke-Perdew
       END
       BASIS
        type TZP
        core small
       END
       SCF
        Converge 1.0e-5 1.0e-5
        Iterations 99
       END
       INTEGRATION 5.0 5.0 5.0
       CHARGE   0.0
     SUBEND

   END

   ENDINPUT
   eor

LinearTransit run for bimolecular nucleophilic reaction of F\ :sup:`-`  and CH\ :sub:`3` Cl
*******************************************************************************************

.. code-block:: shell

   $AMSBIN/quild << eor
   Title LinearTransit for Sn2 reaction of F- + CH3Cl

   XC
    GGA OPBE
   END

   QUILD
     nrlt 11
     cvg_grd 1.0e-4
     CONSTR
       dist 1 6 2.5 1.5
     SUBEND
   END

   ATOMS
      C             0.000000     0.000000     0.000000
      H            -0.530807     0.919384693     0.112892
      H            -0.530807    -0.919384693     0.112892
      H             1.061614     0.000000     0.112892
      Cl            0.000000     0.000000    -1.724300
      F             0.000000     0.000000     2.500000
   END

   Geometry
   End

   BASIS
    type TZ2P
    core NONE
   END

   INTEGRATION 6.0 6.0

   SCF
    converge 1.0e-6 1.0e-6
    diis ok=0.01
    iterations 99
   END

   Charge -1

   EPRINT
    SFO noeig noovl
   END

   endinput
   eor

Geometry optimization of pure spin state for spin-contaminated system
*********************************************************************

.. code-block:: shell

   $AMSBIN/quild << eor
   Title InorgChimActa paper

   EPRINT
     SFO NOEIG NOOVL
   END

   XC
    GGA OPBE
   END

   GEOMETRY
   END

   BASIS
    type TZP
    core SMALL
   END

   SCF
    Iterations 99
    Diis ok=0.01
    Mix 0.1
    converge 1.0e-6 1.0e-6
   END

   INTEGRATION 6.0 6.0 6.0

   QUILD

     INTERACTIONS
       TOTAL  description 1
       S2CORR description 2
     SUBEND

     DESCRIPTION 1
       Occupations smearq=0.0 &
          AA1           4.0     //      5.0
          AA2           0.0     //      0.0
          EE1           8.0     //      8.0
          EE2           6.0     //      4.0
         AAA1           0.0     //      0.0
         AAA2           4.0     //      4.0
         EEE1           6.0     //      6.0
         EEE2           4.0     //      4.0
       End
       CHARGE 0.0 1.0
       Unrestricted
     SUBEND

     DESCRIPTION 2
       Occupations smearq=0.0 &
          AA1           5.0     //      4.0
          AA2           0.0     //      0.0
          EE1           8.0     //      8.0
          EE2           6.0     //      4.0
         AAA1           0.0     //      0.0
         AAA2           4.0     //      4.0
         EEE1           6.0     //      6.0
         EEE2           4.0     //      4.0
       End
       CHARGE 0.0 3.0
       Unrestricted
     SUBEND

   END
   SYMMETRY D(5H)

   ATOMS
    V       0.00000     0.00000     0.00000
    C       1.20500    -1.66000     0.00000
    C       0.37237    -1.66000     1.14602
    C      -0.97487    -1.66000     0.70828
    C      -0.97487    -1.66000    -0.70828
    C       0.37237    -1.66000    -1.14602
    H       2.29965    -1.70014     0.00000
    H       0.71063    -1.70014     2.18710
    H      -1.86046    -1.70014     1.35170
    H      -1.86046    -1.70014    -1.35170
    H       0.71063    -1.70014    -2.18710
    C      -0.97487     1.66000     0.70828
    C       0.37237     1.66000     1.14602
    C       1.20500     1.66000     0.00000
    C       0.37237     1.66000    -1.14602
    C      -0.97487     1.66000    -0.70828
    H      -1.86046     1.70014     1.35170
    H       0.71063     1.70014     2.18710
    H       2.29965     1.70014     0.00000
    H       0.71063     1.70014    -2.18710
    H      -1.86046     1.70014    -1.35170
   END

   endinput
   eor

LinearTransit run for water dimer
*********************************

.. code-block:: shell

   $AMSBIN/quild << eor
   TITLE QUILD (QUantum-regions Interconnected by Local Descriptions) input

   QUILD
     Constr
       dist 1 2 2.6 3.4
     Subend
     nrlt 9
     cvg_grd 1.0e-4
   END

   XC
    GGA PW91
   END

   BASIS
     TYPE DZP
     CORE small
   END

   INTEGRATION 6.0 6.0

   SCF
     converge 1.0e-6 1.0e-6
     diis ok=0.01 n=5 bfac=0.2
     iterations 99
   END

   GEOMETRY
   END

   Occupations smearq=0.0

   ATOMS
   O       -1.262468     -0.389110      0.000000
   O        1.537530      0.425178      0.000000
   H       -1.540482      0.138323      0.765971
   H       -1.540482      0.138323     -0.765971
   H        0.654929      0.010487      0.000000
   H        2.150974     -0.323200      0.000000
   END

   EPRINT
     SFO NOEIG NOOVL
   END

   ENDINPUT
   eor


.. _AMSExample:

Interface to the AMS driver
***************************

This is a simple geometry optimization, showing how to use the DFTB engine in
Quild2019 through the AMS driver interface.

.. code-block:: shell

   $AMSBIN/quild << eor

   ATOMS
       1  H   0.000000   2.182973   1.259286
       2  H   0.000000  -2.182973   1.259286
       3  H   0.000000   2.182973  -1.259286
       4  H   0.000000  -2.182973  -1.259286
       5  C   0.000000   0.000000   1.441079
       6  C   0.000000   0.000000  -1.441079
       7  C   0.000000   1.266644   0.674582
       8  C   0.000000  -1.266644   0.674582
       9  C   0.000000   1.266644  -0.674582
      10  C   0.000000  -1.266644  -0.674582
      11  O   0.000000   0.000000   2.678518
      12  O   0.000000   0.000000  -2.678518
   END

   GEOMETRY
   END

   NOPRINT LOGFILE
   QUILD
     idcvg 1
     logfile_quild 1

     NR_REGIONS=1

     REGION 1
       GUIINFO Label All Show 0 MolVis {Balls And Sticks}
       1-6
     SUBEND

     DESCRIPTION 1 AMS

       Task SinglePoint

       Properties
           Gradients true
       End

       System
       -> Atoms
       End

       Engine DFTB
           ResourcesDir DFTB.org/3ob-3-1
       EndEngine

     SUBEND

     INTERACTIONS
        TOTAL description 1
     SUBEND
   END

   eor
