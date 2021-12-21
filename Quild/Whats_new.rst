What's new in the 2018 version
##############################

An interface to the `AMS driver <../AMS/index.html>`__ has been added, allowing QUILD to use all `AMS engines <../AMS/Engines.html>`__ to be used with QUILD. The interfaces to the old standalone programs (e.g. DFTB) have been removed, since these do not exist anymore in the 2018 release. See :ref:`AMS driver interface example<AMSExample>`.

What's new in the 2017 version
##############################

Anti-ferromagnetic coupling
***************************

Automated optimization for anti-ferromagnetically coupled dinuclear transition-metal systems (with SpinFlip approach in ADF).
See Ref. [:ref:`48<reference 48>`].

Upscaling low frequencies in Gibbs free energy
**********************************************

Upscaling of low frequencies for correct entropy in Gibbs free energy
(controlled by FREQ_CUTOFF keyword, in cm-1)
(both scaled and unscaled Gibbs free energy is given).

Bug fix
*******

Bugfix for combination of delocalized coordinates and frozen coordinates.

What's new in the 2009.01 version
#################################

GUI-support
***********

AMSinput has been adapted to provide full support for the multi-level setup in QUILD. 

Symmetry within QUILD
*********************

QUILD tries to use symmetry as much as possible, but only for the geometry; as such, more symmetries are possible than within ADF (for the orbitals). For instance, it enables the use of S4 symmetry for the geometry and C2 for the orbitals. Moreover, with the use of the  :ref:`SYMROT<SYMROT>` subblock one can rotate coordinates from e.g. D5h to C2v for ferrocene. Therefore, this allows the separation of geometric and orbital symmetry. 

More QM programs
****************

Apart from ADF, NewMM and ORCA (for which an interface was already present), the new version includes interfaces to DFTB and MOPAC, and a  :ref:`GENERIC<GENERIC>` one to accommodate a generic QM program maintained by the user itself. The user-program only has to be able to transform the QUILD-generated coordinates into an energy/gradient etc. and return data in the format as specified (a simple text file). A working example for HONDO is available. 

Frequency calculations for QM, MM and multi-level QM/QM and QM/MM schemes
*************************************************************************

Fully operational calculation of the Hessian in case of multi-level schemes, where for each description either an analytical or numerical setup can be chosen. This can be applied automatically for either QM calculations, MM calculations, or multi-level QM/MM or QM/QM calculations (including spin-contamination corrections). A full summary of the important thermodynamic properties (enthalpy at 0K and 298K, entropy, Gibbs free energy) is reported in the output, for instance: 

::

   ##########################################################################################
                      S U M M A R Y    O F    E N E R G Y    T E R M S
   ##########################################################################################
   Pauli Repulsion:              1.234817178116662     33.6011       774.86      3242.01
   Electrostatic Interactions:  -0.238553103747176     -6.4914      -149.69      -626.32
   Orbital Interactions:        -1.496489120691529    -40.7215      -939.06     -3929.03
   Quild Bonding Energy:        -0.500224957131303    -13.6118      -313.90     -1313.34
   -------------------------------------------------------------------------------------
   Zero-Point Energy:            0.020896706726649      0.5686        13.11        54.86
   Enthalpy H            (0K):  -0.479328250404654    -13.0432      -300.78     -1258.48
   d(Enthalpy H)  (0 = 298K):   0.002837412889686      0.0772         1.78         7.45
   Enthalpy H          (298K):  -0.476490837514968    -12.9660      -299.00     -1251.03
   -T*S                (298K):  -0.021452035100450     -0.5837       -13.46       -56.32
   Gibbs-free-energy   (298K):  -0.497942872615418    -13.5497      -312.46     -1307.35
   ##########################################################################################

Spin-contamination correction per region
****************************************

The spin-contamination (S\ :sup:`2` ) correction has been folded into the multi-level setup, which means the user can do a S\ :sup:`2` -correction for only one region. This option is now available for energy, gradients (optimizations, TSs) and Hessians (vibrational frequencies, numerical and analytical). See the section on  :ref:`spin-contamination correction per region<SPINCONTAMINATION>` for more details. 

Improved TransitionState (TS) search
************************************

Simplification of initial Hessian generation, which makes it generally available for any elements of the Periodic Table. This should further enhance Transition State searches, which for Baker's set of 25 TSs results in complete localization of all TSs within 343 cycles (i.e. 14 cycles per TS). 

Simplified and more detailed output
***********************************

The QUILD output has been drastically reduced (e.g. without the repetitive output of the Create runs in ADF), and at the same time more detail is given. At each optimization step, the progress of the optimization is reported: 

::

   Geometry Optimization Progress
   -------------------------------------------------------
   Item                     Value           Crit    Convgd
   -------------------------------------------------------
   Gradient Max          0.052637       0.000100        NO
   Gradient RMS          0.011095       0.000100        NO
   Step Max              0.000000       0.000100       YES
   Step RMS              0.000000       0.000100       YES
   del(Energy)        -168.585008       0.000010        NO
   # neg. Hesseig.              0              0       YES
   -------------------------------------------------------

and the components of the multi-level energy expression are explicitly mentioned: 

::

   Energy terms for job    1    jobsign:  1 (MOPAC job, SCF energy)
   ----------------------------------------------------------------------------------------
     Pauli Repulsion:                  0.000000000000      0.0000         0.00         0.00
     Electrostatic Interactions:       0.000000000000      0.0000         0.00         0.00
     Orbital Interactions:             0.000000000000      0.0000         0.00         0.00
     Region Bonding Energy:         -272.352918801950  -7411.1000   -170904.05   -715062.49
    
   Energy terms for job    2    jobsign:  1 (ADF job, SCF energy)
   ----------------------------------------------------------------------------------------
     Pauli Repulsion:                 65.846536707515   1791.7754     41319.33    172880.06
     Electrostatic Interactions:      -5.166530552507   -140.5884     -3242.05    -13564.72
     Orbital Interactions:           -66.098012956421  -1798.6184    -41477.13   -173540.31
     Region Bonding Energy:           -5.418006801413   -147.4315     -3399.85    -14224.97
    
   Energy terms for job    3    jobsign: -1 (MOPAC job, SCF energy)
   ----------------------------------------------------------------------------------------
     Pauli Repulsion:                  0.000000000000      0.0000         0.00         0.00
     Electrostatic Interactions:       0.000000000000      0.0000         0.00         0.00
     Orbital Interactions:             0.000000000000      0.0000         0.00         0.00
     Region Bonding Energy:         -109.185918021950  -2971.1000    -68515.21   -286667.59
    
   ----------------------------------------------------------------------------------------
   Total (multi-level) QUILD energy
   ----------------------------------------------------------------------------------------
     Quild Bonding Energy:          -168.585007581413  -4587.4315   -105788.70   -442619.87
   ========================================================================================

Improved generation of primitive coordinates
********************************************

A new subroutine is used for generating the primitive coordinates, which should lead to less and more important coordinates (icreate 7). 

Frozen coordinates versus constraints
*************************************

A number of Cartesian coordinates can be kept frozen (with the  :ref:`FROZEN<FROZEN>` subblock), without the need to put additional constraints that may be sometimes awkward to put. This can be for instance be the case when the user wants to treat the active site of an enzyme and freeze certain atoms (e.g. the C? atoms) to mimic the effect of the protein environment. 

Numerical gradients per region
******************************

The numerical gradients that can be used within QUILD are now completely generalized, and can be specified per region. For instance, if one wants to use the numerical gradient of a hybrid-metagga functional (such as e.g. mPBE0KCIS) for a small part of the total system, and the analytical gradient of a GGA for the rest, it is simple and straightforward to achieve this: 

::

   QUILD   
     SMETAGGA mPBE0KCIS
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
     ! MM input for NewMM, not explicitly shown here
     SUBEND
   
     DESCRIPTION 2 NEWMM
     ! MM input for NewMM, not explicitly shown here
     SUBEND
   
     DESCRIPTION 3 NUMGRAD MGGA
       BASIS
        type DZ
        core small
       END
       SCF
        Converge 1.0e-7 1.0e-7
        Iterations 99
        diis ok=0.01
       END
       INTEGRATION 7.0 7.0 7.0
       CHARGE   0.0
       METAGGA
     SUBEND
   
   END

