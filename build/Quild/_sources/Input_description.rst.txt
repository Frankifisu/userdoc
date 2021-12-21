Input description
#################

Relevant Keywords in QUILD block
********************************

.. csv-table:: 
   :widths: 110,50,500

   name,default,description
   CVG_ENR,1.0e-5,Convergence criterion for energy (when IDCVG :math:`\geq` 2)
   CVG_GRD,1.0e-4,"Convergence criterion for maximum component of gradient; depending on the value of IDELOCAL, either the delocalized or Cartesian gradient is checked"
   CVG_STP,1.0e-4,Convergence criterion for maximum component of step (when IDCVG :math:`\geq` 2)
   DIFSTEP,1.0e-5,Stepsize for numerical differentiation (with numerical gradients/Hessian))
   I_ADD_DUMMIES,1,Index to do (1) or do not (0) add dummy atoms for avoiding (nearly-)linear angles
   ICREATE,7,Index which method to use for generating the primitive coordinates
   IDCVG,1,"Index how to signal convergence:"
   , ,"1.\  check nr. of negative Hessian eigenvalues is correct and max. component
   and rms value of gradient are less than the convergence criterion (see CVG_GRD)"
   , ,"3.\  same as 1, but both max. component of step and change in energy should be less than
   their respective convergence criteria (see CVG_STP and CVG_ENR)"
   , ,"2.\  same as 3, but only of the additional criteria has to be fulfilled"
   IDELOCAL,1,"Kind of coordinates to use in the geometry optimization:"
   , ,"1.\  adapted delocalized coordinates"
   , ,"0.\  Cartesian coordinates"
   IDIIS,3,"Kind of GDIIS equations to use:"
   , ,"0.\  original GDIIS"
   , ,"1.\  same as 0, but with Farkas-Schlegel rules applied"
   , ,"2.\  use gradient as error vector"
   , ,"3.\  same as 2, but with Farkas-Schlegel rules applied"
   , ,"4.\  use 'energy' vector as error vector"
   , ,"5.\  same as 4, but with Farkas-Schlegel rules applied"
   IDSTEP,5,"Step to take:"
   , ,"1.\  RSO for minimizations, RFO (Baker) for TransitionStates"
   , ,"3.\  RFO (Baker) always"
   , ,"5.\  Generalized RSO (Swart) using image-function for TransitionStates"
   IEXCST,1,"Number of excited state to use for numerical gradients
   By default for singlet excited state; triplet excited state can be used by
   adding ONLYTRIP keyword to EXCITATIONS block on input"
   IHOPT,3,"Index for force constants method to use for initial Hessian:"
   , ,"0.\  Baker (0.5 bonds, 0.2 angles, 0.1 dihedrals)"
   , ,"1.\  Thomas Fischer"
   , ,"2.\  simplification of Lindh"
   , ,"3.\  Swart-Bickelhaupt scheme"
   , ,"7.\  Swart generalized scheme (works well for close to minima)"
   IHUPD,-1 cq. 4,"Index for Hessian update scheme:"
   , ,"1.\  BFGS for Hessian (-1  BFGS for inverse Hessian)"
   , ,"2.\  Powell-symmetric-Broyden, PSB (for Transition States)"
   , ,"3.\  Murtagh-Sargent (Symmetric Rank-One, SR1)"
   , ,"4.\  Bofill weighted combi of PSB and SR1 (for Transition State)"
   , ,"5.\  Farkas-Schlegel weighted combi of BFGS and SR1"
   , ,"6.\  Bakken-Halgaker combi of BFGS and SR1"
   IQUILD_OUTPUT,1,"Amount of output requested, debug output :math:`\geq` 2"
   IRESTART,0,"Index if ADF/ORCA jobs should restart from t21.files from previous geometry "
   , ,"< 0 ORCA uses restart, ADF not"
   , ,"> 0 both ORCA and ADF use restart"
   ITRUST,0,Index if dynamic trust radius should be used (1) or not (0)
   MXDIIS,5,Maximum number of GDIIS vectors to use
   MXGEO,50,Maximum number of geometry cycles (overrides value read from ITERATIONS in GEOMETRY block)
   NR_REGIONS,1,Number of different regions for multi-level approach
   NRLT,0,Number of LinearTransit steps
   RTRUST,0.20,Trust radius value
   SMETAGGA,-,"String for functional from METAGGA post-SCF scheme to use for numerical gradients, should be given exactly as on METAGGA output"
   TRUST_ALFA,1.20,Factor to increase trust radius with if :math:`\Delta` energy agrees with model prediction
   TRUST_BETA,0.70,Factor to decrease trust radius with if :math:`\Delta` energy does not agree with model
   TRUST_GOOD,0.80,Lower threshold for increasing trust radius
   TRUST_RMIN,0.40,Upper threshold for increasing trust radius
   
The other keywords that are printed in the output are for debug purposes, under development, or of technical nature. More information about them can be obtained (if needed) from SCM or M. Swart. 

CONSTR subblock in QUILD block
******************************

Constraints can be supplied in the CONSTR subblock of QUILD. Below are the different option that are possible: 

::

   QUILD
     CONSTR
       dist   1 2         0.9
       angle  1 2 3     120.0
       dihed  1 2 3 4   100.0
       x      1           0.0   ! only with idelocal=0
       y      1           0.0   ! only with idelocal=0
       z      1           0.0   ! only with idelocal=0
     SUBEND
   END

The units of these constraints are determined by the parameters in the UNITS block. The numbers in this subblock refer like usual to the atom numbers, as they are found in the ATOMS block. 

A special case is observed for LinearTransit calculations, as given in the example below. 

::

   QUILD
     nrlt 11
     CONSTR
       dist   1 2         1.0    2.0
       angle  1 2 3     120.0   70.0
     SUBEND
   END

Here there are two LinearTransit coordinates, i.e. the distance between atoms 1 and 2 and the angle 1-2-3. The distance between atoms 1 and 4 is a simple constraint throughout the whole calculation. 

FROZEN subblock in QUILD block
******************************

.. _FROZEN: 

Another way to introduce constraints is by freezing certain atoms. This can be achieved with the FROZEN subblock of QUILD, where either all three Cartesian (x, y, z) coordinates of an atom (or a series of atoms) can be frozen, or only one of the three: 

::

   QUILD
     FROZEN
       x      1-37   ! the X-coordinates of atoms 1 to 37 are kept frozen
       xyz   48-256  ! the X,Y,Z-coordinates of atoms 48 to 256 are kept frozen
     SUBEND
   END

SYMROT subblock in QUILD block
******************************

.. _SYMROT: 

Sometimes, one wants to lower the symmetry because of more convenient descriptions of d-orbitals of transition metals for instance. In that case, if one still wants to maintain the higher symmetry for the geometry, one can use the SYMROT subblock to rotate the coordinates. For instance, for Fe(II)(Cl)\ :sub:`4` \ :sup:`2-`  with T\ :sub:`d`  geometric symmetry, the Fe d-orbitals are not conveniently separated. This might be better done within C\ :sub:`2v`  symmetry: 

::

   Symmetry C(2v)
   
   QUILD
    Symgeo T(d)
    Symrot
      -0.7071067811865475 -0.7071067811865475  0.0
      -0.7071067811865475  0.7071067811865475  0.0
       0.0                 0.0                 1.0
    Subend
   End
   
   Atoms
    Fe               0.000000000    0.000000000    0.000000000
    Cl              -1.326583289    1.326583289    1.326583289
    Cl              -1.326583289   -1.326583289   -1.326583289
    Cl               1.326583289    1.326583289   -1.326583289
    Cl               1.326583289   -1.326583289    1.326583289
   End

This transforms the coordinates from T\ :sub:`d`  symmetry: 

::

   Atomic coordinates
   
    atom       nr    x (Bohrs)   y (Bohrs)   z (Bohrs)       x (angs)    y (angs)    z (angs)
   --------------------------------------------------------------------------------------------
    FE          1      0.00000     0.00000     0.00000        0.00000     0.00000     0.00000
    CL          2     -2.50688     2.50688     2.50688       -1.32658     1.32658     1.32658
    CL          3     -2.50688    -2.50688    -2.50688       -1.32658    -1.32658    -1.32658
    CL          4      2.50688     2.50688    -2.50688        1.32658     1.32658    -1.32658
    CL          5      2.50688    -2.50688     2.50688        1.32658    -1.32658     1.32658

to  C\ :sub:`2v`  symmetry: 

::

   SYMMETRY C(2V)
   Atoms
    FE               0.000000000    0.000000000    0.000000000 
    CL               0.000000000    1.876072079    1.326583289
    CL               1.876072079    0.000000000   -1.326583289
    CL              -1.876072079    0.000000000   -1.326583289
    CL               0.000000000   -1.876072079    1.326583289
   End          

The particular rotation matrix to be used depends on the choice made by the user for how to represent the molecule in the lower symmetry (see AMSinput how to impose symmetry). 

TSRC subblock in QUILD block
****************************

The Transition State Reaction Coordinates that are used to construct the special initial Hessian, should be given in the TSRC subblock of QUILD. Similar to the CONSTR subblock, the distances, angles, or dihedrals should be specified, one per line, with atom numbers. The atom numbers should refer to the atoms as they are found in the ATOMS block. 

::

   QUILD
     TSRC
       dist   1 2
       angle  1 2 3
       dihed  1 2 3 4
     SUBEND
   END

REGION subblocks in QUILD block
*******************************

The definition of the different regions should be given in REGION subblocks of QUILD. Although the program counts the number of regions itself, it should be regarded good practice to make sure that the NR_REGIONS keyword corresponds to the correct number of REGION subblocks. 

::

   QUILD
     NR_REGIONS 2
     REGION 1
       1-11
     SUBEND
     REGION 2
       12 14 13 15 16 17 19 18 22 21 20
     SUBEND
   END

The order in which the atom numbers are given does not matter, and in order that the input is easier to make and read, shortcuts are introduced. For instance, the "1-11" shortcut corresponds to "1 2 3 4 5 6 7 8 9 10 11" etc. Unlike other multi-level approaches, there is no need to have a shell structure for the different regions. I.e., the regions can overlap, or be defined as given above for DNA. 

ADDREMOVE subblock in QUILD block
*********************************

There is no ADDREMOVE subblock of QUILD active yet, but in the future it will be added to be able to control how the capping atoms will be added in the case of regions with dangling bonds. I.e., which elements should be added, and so on. For the moment, only hydrogens will be added, which works without problems for QM/QM and/or QM/MM calculations on DNA, or simple peptides. Future developments should decide whether this needs to be adapted. 

DESCRIPTION subblocks in QUILD block
************************************

In case of multi-level jobs, where different regions are treated with different methodologies, the different methodologies should be given in the DESCRIPTION subblocks. 

::

   QUILD
     DESCRIPTION 1 ADF [NUMFREQ]
       XC
         GGA OPBE
       END
       BASIS
         type TZ2P
         core NONE
       END
     SUBEND
     DESCRIPTION 2 ADF NUMGRAD
       XC
         HYBRID B3LYP
       END
       basis
         type DZ
         core NONE
       end
     SUBEND
     DESCRIPTION 3 ORCA NUMFREQ
       %method method hf
        runtyp gradient
       end
       %basis basis sto_3g
       end
       %coords
         mult 2
         charge -1
       end
     SUBEND
     DESCRIPTION 4 NEWMM NUMFREQ
       QMMM
         FORCE_FIELD_FILE $AMSRESOURCES/ForceFields/amber95.ff
         QMMM_INFO
          -1    OW  QM  -0.8340  HOH     1  O         2      3
           2    HW  QM   0.4170  HOH     1  H1       -1
           3    HW  QM   0.4170  HOH     1  H2       -1      
           4    OW  MM  -0.8340  HOH     2  O         5      6
           5    HW  MM   0.4170  HOH     2  H1        4
           6    HW  MM   0.4170  HOH     2  H2        4
         SUBEND
       END
     SUBEND
     DESCRIPTION 5 DFTB NUMFREQ
       CHARGE 0
       GEOMETRY
         runtype SP
         iterations 1
       END  1
     SUBEND
     DESCRIPTION 6 MOPAC NUMFREQ
       AUX(0) BONDS CHARGE=0 SCFCRT=1.0D-8 PM3 1SCF GRAD
       Coordinates generated by AMSinput (c) SCM 1998-2009
     SUBEND
     DESCRIPTION 7 GENERIC NUMGRAD NUMFREQ
     ! input-description specific for GENERIC program
     ! for the system under study (see above)
     SUBEND
   END

Description 1 here applies to OPBE/TZ2P(ae) with ADF, description 2 to B3LYP/DZ(ae) with ADF, description 3 to UHF/STO-3G through the ORCA interface, and finally descriptions 4 to 7 apply to description for NEWMM, DFTB, MOPAC and GENERIC respectively. 

The input for multi-level approaches has been explained above. The standard input should be given for ADF, DFTB and NEWMM. See the corresponding User Manuals for ADF, DFTB and ADF-QM/MM respectively for them. Also for ORCA should standard input be used, the only exception being the total charge and multiplicity, which should be given as a partial  %coords block. The QUILD program will then add the atomic coordinates to this block for the "black-box" inputfiles. 

Numerical versus analytical Hessians for multi-level vibrational frequencies
****************************************************************************

The descriptions on the previous page indicate for some of the programs, whether the gradients and Hessians can be obtained analytically (no extra keywords necessary) or numerically. In the latter case, depending on if it is for the gradients or Hessian, one should add NUMGRAD or NUMFREQ to the DESCRIPTION line (see previous page). The QUILD program will then take care of preparing the correct number of jobs etc. 

Use of a GENERIC description for use with user-provided QM-program
******************************************************************

.. _GENERIC: 

The 2009.01 version of QUILD allows the user to create his/her own script for use with a QM-program (e.g. HONDO, Molcas, etc.) for which no standard interface is available yet within QUILD. For this purpose (and with the GENERIC description above), the QUILD program writes a generalized inputfile for this script that consists of the following: 

Line 1: 

::

   NAT IQRUN
   NAT    number of atoms
   IQRUN  type of job:
          0 single-point energy
          1 single-point energy+grad
          2 single-point energy+grad+Hess

Line 2 to NAT+1 

::

   ATOM X  Y  Z
   ATOM   atomname
   X      Cartesian X-coordinate (in Å)
   Y      Cartesian Y-coordinate (in Å)
   Z      Cartesian Z-coordinate (in Å)

Remaining lines 

::

   User provided lines on input (within DESCRIPTION block)

The user should then make sure that his/her script runs their program, and extract data from it in the following manner (the QUILD program reads these lines as free format, e.g. spaces or upper/lowercase are not important): 

::

   # ----------------------------------------------
   # lines starting with # will be ignored by QUILD
   # ----------------------------------------------
   # ---------------
   # number of atoms
   # ---------------
   [nat]     3
   # ----------------------
   # total energy (Hartree)
   # ----------------------
   [energy]  -74.964263362500
   # ----------------------------
   # cartesian coordinates (Bohr)
   # ----------------------------
   [xyz]       0.0000000    0.0000000    0.0000000
   [xyz]       0.0000000   -1.4572640   -1.1166010
   [xyz]       0.0000000    1.4572640   -1.1166010
   # --------------------
   # expectation value S2
   # --------------------
   [s2]        0.000000000000
   [sz]        0.000000000000
   # ------------------------------
   # energy gradient (Hartree/Bohr)
   # ------------------------------
   [grad]      0.0000000      0.0000000     -0.0424023
   [grad]      0.0000000    0.0073465    0.0212011
   [grad]      0.0000000   -0.0073465    0.0212011
   # ------------------------------
   # Hessian matrix (Hartree/Bohr2)
   # ------------------------------
   [hess]    -0.03797442   0.00000000   0.00000000   0.01898721   0.00000000   0.00000000
   [hess]     0.01898721   0.00000000   0.00000000   0.00000000   0.93011207   0.00000000
   [hess]     0.00000000  -0.46505603  -0.37088899   0.00000000  -0.46505603   0.37088899
   [hess]     0.00000000   0.00000000   0.62917145   0.00000000  -0.24554704  -0.31458572
   [hess]     0.00000000   0.24554704  -0.31458572   0.01898721   0.00000000   0.00000000
   [hess]    -0.01201427   0.00000000   0.00000000  -0.00697295   0.00000000   0.00000000
   [hess]     0.00000000  -0.46505603  -0.24554704   0.00000000   0.49190911   0.30821802
   [hess]     0.00000000  -0.02685307  -0.06267097   0.00000000  -0.37088899  -0.31458572
   [hess]     0.00000000   0.30821802   0.29686554   0.00000000   0.06267097   0.01772018
   [hess]     0.01898721   0.00000000   0.00000000  -0.00697295   0.00000000   0.00000000
   [hess]    -0.01201427   0.00000000   0.00000000   0.00000000  -0.46505603   0.24554704
   [hess]     0.00000000  -0.02685307   0.06267097   0.00000000   0.49190911  -0.30821802
   [hess]     0.00000000   0.37088899  -0.31458572   0.00000000  -0.06267097   0.01772018
   [hess]     0.00000000  -0.30821802   0.29686554
   
   # ------------------------------------------------------
   # example of data for S2-correction
   # in this case the Sz and S2 values should also be given
   # ------------------------------------------------------
   # ---------------
   # number of atoms
   # ---------------
   [nat]     2
   # ----------------------
   # total energy (Hartree)
   # ----------------------
   [energy]  -74.362823992381
   # ----------------------------
   # cartesian coordinates (Bohr)
   # ----------------------------
   [xyz]       0.0000000    0.0000000    0.0000000
   [xyz]       0.0000000    1.4572640   -1.1166010
   # --------------------
   # expectation value S2
   # --------------------
   [s2]        0.753292786229
   [sz]        0.500000000000

Spin-contamination correction per region
****************************************

.. _SPINCONTAMINATION: 

Previously, the spin-contamination correction was done for the complete system, but starting from version 2009.01 it can be performed for different regions, as in the following example: 

::

   QUILD
     DESCRIPTION 1 ADF
       Occupations smearq=0.0  &
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
     
     DESCRIPTION 2 ADF
       Occupations smearq=0.0  &
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
   
     INTERACTIONS
       TOTAL  description 1
       S2CORR region 1 spin-splus-description 2 for contaminated-description 1
     SUBEND
   
   END
   SYMMETRY D(5H)

Note that this in this case, the spin-contaminated system (doublet) consists of a triplet-alfa in the EE2-irrep coupled with a doublet-beta in the AA1-irrep. This is corrected for by a pure quartet, and the corresponding energies corrected: 

::

   Values for S2correction  1 :
   s2cont        1.75396
   s2pure        0.75000
   s2plus        3.78716
   a_s2          0.33056
   jobsigns  job  2   -0.49378     job  1    1.49378

INTERACTIONS subblock in QUILD block
************************************

One of the most important input-parts for multi-level jobs is the INTERACTIONS subblock of QUILD, where one should define how the different descriptions should be applied to the different regions. At the part where we explained the multi-level approaches, we already showed some examples of how to combine different methodologies. Below is another example input where all possible options are given. 

::

   QUILD
     INTERACTIONS
       TOTAL     description 1
       REPLACE   region 1 region 2    description 3 for description 2
       REPLACE   region 1             description 4 for description 3
       INTXN     region 1 region 2    description 3 for description 2
       S2CORR    region 1  spin-splus-description 2 for contaminated-description 1
     SUBEND
   END

If an INTERACTIONS subblock is present (if none is present it means no multi-level setup is done, i.e. pure QM or MM), there should always be a line with the description of the total system, as shown in the first line of the INTERACTIONS subblock. Then if you want to replace the interactions for one (or more) region(s), you could do so as indicated in the second and third line. Finally, if you want to replace the interaction between two regions, as we need for DNA where we replace the BP86 :math:`\pi`-stacking by LDA :math:`\pi`-stacking, the fourth line of the INTERACTIONS subblock should be used. Finally, the last line can be used for spin-contamination corrections for one (or more) regions. 

Note that in all cases it is not necessary at all to add the "region", "description" and "for" words in the INTERACTIONS subblock; they are ignored when reading the input. The program reads the line, uses the last two integers for the descriptions and the ones before for the regions. Therefore, a completely equivalent input would be as shown below. However, for better readability, it is to be advised to always use the additional text anyway. 

::

   QUILD
     INTERACTIONS
       TOTAL             1
       REPLACE   1 2   3 2
       REPLACE   1     4 3
       INTXN     1 2   3 2
       S2CORR    1     2 1
       S2CORR    1 3   2 1
     SUBEND
   END

Note that in the last line, it is indicated that the spin-contamination correction is applied to regions 1 and 3 together.  

INLINE options in the QUILD block
*********************************

Similar to the situation in ADF, one can use the INLINE directive to read specific input-lines from a file rather than from input. In general, this should make no difference, but in rare instances (for instance if the $ sign is needed in inputfiles for one of the programs), it might become useful. 

