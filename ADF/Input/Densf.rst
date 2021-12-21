.. index:: densf module 


Densf: Volume Maps
******************

*densf* is an auxiliary program to generate values of molecular orbitals, charge densities and potentials in a user-specified grid, to be used typically for plotting or graphical display. The TAPE41 result file can be used directly by the AMSview program to visualize these properties. 

*densf* requires an ascii input file where the user specifies the grid and the items that he/she wishes to see calculated on the grid, plus the standard result file adf.rkf (TAPE21) from an *adf* calculation. * densf* writes a summary of the items that have been requested to standard output, together with some general information. 

*densf* produces a (binary) KF file TAPE41, see OUTPUTFILE keyword below. TAPE41 is a KF file and all KF utilities can be used to inspect and process its data. 

*densf* can also read and write cube files. See the CUBINPUT and CUBOUTPUT input options for details. 

Examples of using *densf* are contained in the set of sample runs; see the :ref:`ADF Examples<examples>`.


Input
=====

The input for *densf* is keyword oriented. The keywords may be specified in any order.

Below follows a list of the allowed keywords with their description. 

.. _keyscheme densf: 


::

   $AMSBIN/densf << eor
   ADFFILE {file}
   OUTPUTFILE {file}
   VTKFILE {file}
   CUBINPUT {file}
   CUBOUTPUT {file}
   GRID ...
   UNITS ...
   Density ...
   KinDens ...
   Laplacian ...
   DenGrad ...
   DenHess ...
   Potential ...
   Orbitals ...
   NOCV ...
   NCI ...
   SEDD
   DualDescriptor
   eor

**Input/Output files**

::

   ADFFILE {file}

ADFFILE keyword specifies path to the adf.rkf file from which *densf* reads the input data. Absence of the keyword is treated as if **ADFFILE TAPE21** has been specified. 

::

   OUTPUTFILE {file}

OUTPUTFILE keyword specifies path to the (possibly existing) TAPE41 file. If the file exists, *densf* will read grid specifications from it ignoring GRID keyword in the input. Computed quantities are saved in the file overwriting existing data with the same name, if any. 

::

   VTKFILE {file}

VTKFILE keyword specifies path to a file in the format readable by VTK directly. This option exists primarily for better integration with ADF-GUI and the user should not specify it. 

::

   CUBINPUT {file}

If the CUBINPUT keyword is present then the grid as specified in the **file** is used to calculate all requested quantities. Any volume data found in the cube file is also saved in the output file. NOTE: CUBINPUT option cannot be used with a pre-existing TAPE41 file because they both specify the grid, which may lead to a conflict. 

::

   CUBOUTPUT {file}

Presence of the CUBOUTPUT keyword tells densf to save all computed quantities as cube files using **file** as filename prefix. The prefix can also contain a complete path including directories. For example, specifying the following in the densf input 

::

   CUBOUTPUT /home/myhome/H2O
   Density SCF

will result in a file /home/myhome/H2O%SCF%Density.cub being created containing volume data for the total SCF density. One file per requested quantity is created. 

The OUTPUTFILE, CUBOUTPUT and VTKFILE options are mutually exclusive. Absence of any of these options is treated as if **OUTPUTFILE TAPE41** has been specified. 

**Grid**

The grid can be specified using the Grid block key.  

In its simplest form the block can be written as follows: 

::

   GRID {save} {coarse|medium|fine}
   END
   EXTEND grid_extent

If the word *save* is specified, the program will store all grid points on TAPE41 (in addition to the specification of the grid that is always stored). The default is NOT to store all the grid points. 

Either coarse, medium or fine may be specified. This instructs the program to generate the grid automatically within a box enclosing all atoms of the molecule. The distance between grid points is 0.5, 0.2 or 0.1 bohr for the coarse, medium and fine grid, respectively. Obviously, the size of the result file TAPE41 depends strongly on this specification. By default a coarse grid is generated. 
The size of the grid box is determined by the atomic coordinates and the grid extent. The latter is by default equal to 4.0 Bohr and can be changed using the EXTEND keyword, in which case it is affected by the unit_of_length value specified in the UNITS block (see below).

For more detailed grid specification the following Grid block can be used: 

::

   Grid {save}
    x0 y0 z0
    n1 [n2 [n3]]
    v1x v1y v1z length1
    [v2x v2y v2z length2]
    [v3x v3y v3z length3]
   END

The rows of the Grid block are specified as follows: 

+ Row 1: three coordinates for the 'origin' (one of the corners) of the grid.

+ Row 2: up to three integers specifying the numbers of points in each direction. The number of integers defines the dimensionality of the grid.

+ Rows 3 to 5: up to three rows, one per grid dimension. Each row contains components of the direction vector and the length of the grid in this dimension. The absolute magnitude of the vector components is irrelevant as it will be scaled to fit the given number of points into the grid length in this dimension. The unit of length for the grid size is by default Angstrom. The default can be overridden by using the input key UNITS, see below.

Notes:

+ The second row ('three integers...') specifies the number of grid *points* in the different directions. The corresponding number of steps or intervals is one less!

+ If the TAPE41 result file is to be used by AMSview, the grid must be a 3-dimensional orthogonal one, with the same step size for all three dimensions.

+ If the output TAPE41 file already exists and it contains valid grid data or if CUBINPUT is specified then the GRID input is ignored.

+ The unit of length used in the input file has no relation to how the data are stored on the result file and how the program processes the data internally. Internal processing and storage on file is in bohr (atomic units).

**Inline Grid**

DENSF can read grid as list of points. When specifying inline grid the GRID keyword should look as follows: 

::

   Grid Inline
     x1 y1 z1
     x2 y2 z2
     ...
     xN yN zN
   End

Here, x#, y#, and z# are coordinates of points at which requested properties will be calculated. This feature may be used, for example, by external programs to calculate various properties at a number of points exactly and avoid interpolation with its inaccuracy. This feature should be used only when the output file has a TAPE41 format.

**Units**

The unit of length can be set with the Units block:

::

   UNITS
    Length unit_of_length
   END

The unit-of-length will apply to the grid specification in the input file. Default is angstrom. 

**Density**

Generates the charge density in the grid. It is a simple keyword (not block-type). 

::

   density {fit} {frag} {ortho} {scf} {trans}

Occurrence of the word fit specifies that all densities specified in this record will be computed from the fit functions (an approximation to the exact density), rather than from the occupied molecular orbitals. 

frag, ortho, scf, and trans causes each of the corresponding densities to be computed. frag stands for the sum-of-fragments (i.e. the initial) density, scf for the final result of the *adf* calculation, ortho for the orthogonalized fragments (orthogonalization to account for the Pauli repulsion, see the ADF User's Guide), and trans for excitation transition density.

Transition density is a product of initial and final states of an excitation. In the simplest case when initial and final states consist of one molecular orbital each, in this case the corresponding transition density is a product of the two MOs. To obtain transition densities one needs to perform an excitations calculation with ADF, see EXCITATIONS keyword in ADF User's Guide. Transition densities for all excitations found in the input adf.rkf (TAPE21) file will be calculated. The transition densities are always fit-densities. 

If both the exact and the fit-densities are required the density keyword must be repeated, once with and once without the fit option specified. 

The default (when the DENSITY key does not occur in the input file) is to calculate the final SCF density and the sum-of-fragments density. 

The frozen core density is calculated with: 

::

   density core

**Kinetic Energy Density and Electron Localization Function (ELF)**

::

   KinDens {frag} {orth} {scf}

Generates the Kinetic energy density and electron localization function on the grid.

Occurrence of any of the words requests calculation of the two quantities (KinDens and ELF) based on the corresponding density: sum-of-fragments, orthogonalized fragments, or SCF, respectively. If none of the options is present, scf is assumed. 

**Laplacian of the Density**

The Laplacian of the exact SCF density is calculated with: 

::

   Laplacian

The Laplacian of the fitted SCF density is calculated with: 

::

   Laplacian fit

The LAPLACIAN key can occur multiple times. The LAPLACIAN feature is also supported by AMSview. 

**Gradient of the Density**

The gradient of the exact SCF density is calculated with: 

::

   DenGrad

The gradient of the fitted SCF density is calculated with: 

::

   DenGrad fit

The gradient of the frozen core density is calculated with: 

::

   DenGrad core

**Hessian of the Density**

The DENGRAD key can occur multiple times. This feature should be used only when the output file has a TAPE41 format. 

The Hessian of the exact SCF density is calculated with: 

::

   DenHess

The Hessian of the fitted SCF density is calculated with: 

::

   DenHess fit

The Hessian of the frozen core density is calculated with: 

::

   DenHess core

The DENHESS key can occur multiple times. This feature should be used only when the output file has a TAPE41 format. 

**Potential**

Generates the coulomb and/or exchange-correlation potential in the grid. 

::

   potential {coul / XC} {frag} {ortho} {scf}

frag, ortho, and scf are as for the density: at least one must be specified. 

coul and XC specify that the Coulomb potential, respectively the exchange-correlation potential must be computed. Precisely one of these options must be specified in the record. If both potential types are required, another input record with the potential key must be used. 

In the present release the xc option is not yet operational. 

The default (when the POTENTIAL key does not occur in the input) is to calculate the SCF Coulomb potential. 

**Orbitals**

A block type key in which the required molecular orbitals are specified. The key can be repeated in input any number of times; all occurrences are read and applied. 

::

   Orbitals {GRAD} type
    (data)
   END

The argument of the orbitals key (type) must be scf (for the scf orbitals) or loc (for the localized molecular orbitals, see the ADF User's Guide) or generic (see separate section). 

The SCF type can have an optional GRAD specifier which requests calculation of the MO gradients.

In many data records in the ORBITALS block, as noted in the description of these data records, you may specify a HOMOLUMO range. 

A HOMOLUMO range is the following: 

::

     {HOMO{{-}n}} {LUMO{{+}n}}

HOMO: the highest occupied orbital HOMO-n, with n an integer: the highest (n+1) occupied orbitals LUMO: the lowest virtual orbital LUMO+n, with n an integer: the lowest (n+1) virtual orbitals. 

The HOMO part, or the LUMO part, or both must be specified. The integer n with sign is always optional, and the sign is always optional (and has no meaning, it is intended to enhance readability). 

Thus, as an example,

::

      HOMO-1 LUMO+1

means a range of 4 orbitals: the two highest occupied ones, and the two lowest virtuals. 

Each data record in the orbitals block must have either of the following formats: 

the word alpha or beta.
   This specifies that subsequent records refer to spin-alpha or spin-beta orbitals respectively. In a restricted calculation this has no meaning and beta must not be specified. alpha and/or beta may occur any number of times in the orbitals block. All records until the first occurrence of alpha or beta are assumed to refer to spin-alpha orbitals.

label n1, n2, n3, ...
   label is one of the subspecies of the point group symmetry used in the adf calculation and n1 etc. are indices of the molecular orbitals (in that subspecies) that are to be computed. This format is meaningless and must not be used for the loc orbitals type, because localized orbitals do not (necessarily) belong anymore to a particular symmetry 

label HOMOLUMO 
   label is one of the subspecies of the point group symmetry used in the calculation, the orbitals follow from the HOMOLUMO range.

label occ or label virt
   occ specifies all orbitals (in that symmetry representation) up to and including the highest occupied one. virt specifies all orbitals above the highest occupied one. In this context partially occupied orbitals are considered occupied. Note carefully that if in a particular symmetry representation an empty orbital is computed below the highest occupied one in that same representation (excited state), that particular empty one is included in the list of occ. Again, this format is meaningless and must therefore not be used for the loc type of orbitals.

all occ or all virt or all HOMOLUMO
   Specifies for each symmetry representation:

   + all orbitals up to and including the highest occupied one (in that symmetry), or
   + all orbitals above the highest occupied one, or
   + all orbitals defined by the HOMOLUMO range.

   This form is not to be used for the LOC type of orbitals. However, using this for LOC will not result in an error but will be interpreted as identical to the following format.

all
   This format must be used only for the LOC type of orbitals and simply means: all computed localized orbitals (irrespective of occupation numbers).

n1, n2, ...
   a simple list of integer indices. This format must be used only for the loc type of orbitals since no reference is made to any symmetry representation. The indices refer of course to the list of localized orbitals as computed by ADF.


The default value used when the ORBITALS key is not present is: 

::

   Orbitals SCF
    All HOMO-1 LUMO+1
   End

**NOCV**

In ADF2009.01 it is possible to use DENSF to calculate :math:`\epsilon^* \phi^2` values of Natural Orbitals for Chemical Valence (NOCVs). Additional information on NOCVs is available in Ref. [#ref1]_. 

The relevant part of the DENSF input is as follows: 

For spin-unrestricted: 

::

   NOCV
     Alpha
      N1:math:`\alpha`
      N2:math:`\alpha`
      ...
     Beta
      N1:math:`\beta`
      N2:math:`\beta`
      ...
   END

For spin-restricted: 

::

   NOCV
      N1
      N2
      ...
   END

N1, N2, etc. specify sequential numbers of the orbitals for which :math:`\epsilon^* \phi^2` is to be calculated.

*Alpha* and *Beta* specify that the numbers that follow refer to spin :math:`\alpha` and :math:`\beta`, respectively. Both *Alpha* and *Beta* are optional, *Alpha* being assumed if omitted. The NOCV input block must be closed with "END". 

Alternatively, one can specify to calculate all (alpha- or beta-) NOCV's: 

For spin-unrestricted: 

::

   NOCV
     Alpha
      ALL
     Beta
      ALL
   END

For both spin-restricted and spin-unrestricted: 

::

   NOCV
      ALL
   END

The last and probably the most convenient form of the NOCV input blocks lets one to specify an NOCV eigenvalue threshold as a criterion for selecting orbitals: 

For spin-unrestricted: 

::

   NOCV
     Alpha
      THRESH threshold
     Beta
      THRESH threshold
   END

For both spin-restricted and spin-unrestricted: 

::

   NOCV
      THRESH threshold
   END

When this form of the input is used, only those NOCVs will be included whose absolute eigenvalue is equal to or larger than the given *threshold*. 

**NOCV profile**

It is possible to compute an integral profile of the NOCV :math:`\epsilon^* \phi^2` function along a given line. To calculate a single point of the profile the :math:`\epsilon^* \phi^2` is integrated in the plane orthogonal to the profile axis and passing through the point. In addition to the input above used for selecting NOCVs, the following input is required to calculate the profile:

::

   NOCV
      PROFILE
   END
   LINE
      x1 y1 z1
      x2 y2 z2
      delta
   END

The LINE input block is used to define the axis along which the profile will be generated. The (*x1,y1,z1*) point defines the origin of the profile axis and (*x2,y2,z2*) defines the second point of the line and the positive direction. The distance between the point does not matter. The *delta* value is the distance between two point in the profile. All values are given in the units specified in the UNITS input block. The positions of the left- and rightmost profile points depend on coordinates of the atoms and the grid extent value (specified by the EXTEND keyword, see above). 

**Generic orbitals**

There is also a possibility to calculate any orbital as long as it is present in the t21 file in the BAS representation. The input syntax is as follows: 

::

   Orbitals GenBas
    section1%variable1
    section2%variable2
   End

In the example above, each line contains the section and variable name of the orbital  in the input t21 file. The length of the variable should be equal to the number of atomic functions (naos) and it is supposed to contain expansion coefficients of the orbital on the basis of atomic (primitive) functions. 

The calculation results are stored in the output file in sections and variables with exactly the same names as specified in the input. The section and variable names may contain spaces although the leading and training spaces are discarded. 

**NCI**

.. _NCI: 

The areas of non-covalent interactions (NCI), see Refs. [#ref4]_ [#ref5]_, can be recognized by the a low value of the electron density coupled with a low value of RDG (reduced density gradient *s* = 1/2 (3 :math:`\pi`\ :sup:`2` )\ :sup:`-1/3`  \| :math:`\nabla \rho`\| :math:`\rho`\ :sup:`-4/3` ) and a negative (or a small positive) value of the second eigenvalue of the Hessian of the electron density ( :math:`\lambda`\ :sub:`2` ). The regions of significant hydrogen bonding are recognized by strictly negative :math:`\lambda`\ :sub:`2` while in the regions of VdW interactions it may be slightly positive. The relevant DENSF input keyword is: 

::

   NCI {BOTH|FIT} {RHOVDW=*RhoVdW*} {RDG=*Rdg*}

All arguments are optional 

By default, the exact density is used to calculate the NCI properties. If FIT is specified then the fitted density is used to calculate the fields and their names are prepended with "Fit". If BOTH is specified then the NCI properties are calculated using both exact and the fitted density. Again names of the fields calculated from the fitted density start with "Fit" 

The remaining arguments set relevant thresholds (all in atomic units): *RhoVdW*: density threshold for detection of weak interaction regions (default 0.02); *Rdg*: threshold on the reduced density gradient value *s* (default 0.5). A point is considered for NCI only if *s* value is smaller than Rdg. 

DENSF creates three variables per density type (exact or fitted) when NCI is present in the input: *SCF%RDG* (or *SCF%FitRDG*): the reduced density gradient value *s*; *SCF%DenSigned* (or *SCF%FitDenSigned*): the sign(:math:`\lambda`\ :sub:`2` ) :math:`\rho` value for regions where *s* < *Rdg*; *SCF%NCI* (or *SCF%FitNCI*): the NCI flag value, see below; 

If the point is considered for NCI (that is if *s* < *Rdg*), the sign( :math:`\lambda`\ :sub:`2` ) :math:`\rho` value (or :math:`\rho`) is tested against *RhoVdW*. If :math:`\rho` < *RhoVdW* then the NCI value is set to 1 to flag a VdW interaction region. If sign( :math:`\lambda`\ :sub:`2` ) :math:`\rho` < -*RhoVdW* then the NCI value is set to -1 to flag a hydrogen bonding region. In all other cases the NCI value is zero. 

AMSview visualization of NCI: use 'Isosurface:with phase' isosurface of property NCI (at 0.5).
Alternative visualization of NCI: use colored isosurface with isosurface of property RDGforNCI (at 0.5) colored with NCI (range -0.5 to 0.5).
The value of RDGforNCI is the same as RDG (reduced density gradient) except in regions where the density is larger than 0.05, in order to get rid of surfaces around atoms, that one would see if one is using an isosurface of RDG.
One may need a medium or fine grid for best visualization.

**SEDD**

.. _SEDD: 
.. _DORI: 

The single exponential decay detector (SEDD), see Ref. [#ref2]_, extracts information about bonding and localization in atoms, molecules, or molecular assemblies. The practical evaluation of SEDD does not require any explicit information about the orbitals. The only quantity needed is the electron density (calculated or experimental) and its derivatives up to the second order. For the exact equation to be used, and pictures, see Ref. [#ref2]_. 

Specifying SEDD in the input also invokes calculation of the Density Overlap Regions Indicator (DORI) [#ref3]_. The DORI is best visualized as a 0.9 isosurface colored with the sign( :math:`\lambda`\ :sub:`2` ) :math:`\rho` value (see the DenSigned variable from the NCI keyword above).
AMSview visualization of DORI: use colored isosurface with isosurface of property DORI (at 0.9) colored with DenSigned (range -0.02 to 0.02).
One may need a medium or fine grid for best visualization.

**DualDescriptor**

Calculate the dual descriptor (DD) in the frontier molecular orbitals approximations. The DD is essentially a difference between (an average of) the square of the lowest unoccupied and the highest occupied molecular orbitals: :math:`DD = \frac{1}{N_{LUMO}} ( \sum_i^{N_{LUMO}} {\psi^2_i} ) - \frac{1}{N_{HOMO}} ( \sum_j^{N_{HOMO}} {\psi^2_j} )`, where *i* and *j* are indices of orbitals within 10\ :sup:`-3` Hartree of the LUMO and HOMO, respectively. Please note that this method will produce incorrect results for molecules with fractional occupation numbers.

Result: TAPE41
==============

Follows a description of the contents of TAPE41. We start with a brief discussion of the sections. At the end you can find an uncommented list of all variables and sections. Note that some data are only generated when certain keywords are provided. 

**Sections on TAPE41**

**Grid** 

This is a general section. It contains the grid data and some more general info. 

The grid characteristics are stored as: 

+ The 'origin' of the grid.

+ The numbers of points in three independent directions.

+ Three vectors, called 'x-vector', 'y-vector' and 'z-vector'. They are the *steps* in the three independent directions that define the grid.

If the save option was used in input (key grid) also all grid coordinates are stored: for each point three coordinates (xyz), also if only a 2-dimensional or 1-dimensional grid has been generated (a 2D grid does not necessarily lie in the xy-plane). 

*Note that the grid values are now stored in a simpler manner than in previous (prior to 2004) versions of densf, because the 'x values', 'y values', and 'z values' now each have their own, separate sections.* 

The remaining (general) data in this section comprises: 

+ The number of subspecies ('symmetries') for which data such as Molecular Orbitals may be present.

+ The names of the subspecies.

+ A logical with the name 'unrestricted', which flags whether the data pertain to an unrestricted calculation.

+ The total number of grid points.

**SumFrag** 

Contains grid data of the Sum-of-fragments (charge density, coulomb potential, kinetic energy density, ELF, etc.). 

**Ortho** 

Contains similar data for the orthogonalized-fragments. 

**SCF** 

Contains the (spin) density, potential, etc. of the final (scf) solution. 

**Core** 

Contains grid data of the frozen core (charge density, gradients, Hessian). 

**TransDens_L1_L2** 

Contains grid data for electron transition densities. L1 is either SS or ST, and L2 is a symmetry  label for all transitions in the section. Here SS and ST stand for Singlet-Singlet and  Singlet-Triplet, respectively. Variables in each section are Fitdensity_N and Coulpot_N for  the density and Coulomb potential for excitation N within this spin and symmetry. 

**SCF_label** 

'Label' is one of the symmetry subspecies. 

Each such section contains the total number of orbitals in that subspecies (as used in the *adf* calculation), with their occupation numbers and energy eigenvalues. 

In addition it contains the grid-values of the (user-specified subset of) MOs in that subspecies. The variable name corresponding to an orbital is simply its index in the energy-ordered list of all orbitals (in that subspecies): '1', '2', etc. 

In case of spin-orbit coupling spinors are calculated. The label is one of the double group symmetry subspecies, and
the square root of the density of the spinor is calculated with an approximate phase factor.
The full description of the spinor can be found in the section SO_label.

**SO_label** 

'Label' is one of the double group symmetry subspecies. 

The grid-values of the (user-specified subset of) spinors in that subspecies.
A spinor is a two-component complex wave function, which can be described with four real functions: real part alpha, real part beta, imaginary part alpha, and imaginary part beta.
The variable name corresponding to a spinor is its index in the energy-ordered list of all orbitals (in that subspecies), combined with the real alpha part, the real beta part, the imaginary alpha part, or the imaginary beta part: '1_alpha_R', '1_beta_R', '1_alpha_I', '1_beta_I', '2_alpha_R', etc.

**LocOrb** 

Values of the localized orbitals. 

**NOCV** 

Values related to the NOCVs. 

**Profile**

Values related to the NOCV profile. The variables whose name start with "Dif" contain the in-plane integral (in e/Bohr) for the given point on the profile axis. A variable without "Dif" in the name contains the integral (in electrons) of the corresponding "Dif" variable on the (-infinity,x) interval.

**Geometry** 

Some general geometric information: the number of atoms (not counting any dummy atoms that may have been used in the *adf* calculation), their Cartesian coordinates (in bohr) and nuclear charges. 

Note: the *order* of the atoms here is not necessarily identical to the input list of atoms: they are grouped by atom type. 

+ In an unrestricted calculation the section SCF_label is replaced by SCF_label_A and SCF_label_B for the spin-alpha and spin-beta data, respectively, and similarly for LocOrb: LocOrb_A and LocOrb_B.

+ One or more subspecies may not have been used in the *adf* calculation. This happens when the basis set used in that calculation does not contain the necessary functions to span symmetry-adapted combinations of basis functions for that subspecies. In such a case the corresponding section on TAPE41 will not be created by *densf*.

+ If you want to verify the contents of TAPE41, use the *pkf* utility to obtain a survey or *dmpkf* to get a complete ASCII printout.

The information is presented in three columns. In the left-most column, section and variable names are printed, variable names being indented. In the middle column, variable's type and size is given. If the type is omitted, double precision floating point is assumed. The right-most column contains comments, if any.

Note that the name of a section of variable may consist of more than one word and that blanks in such names are significant. Furthermore, they are case-sensitive. Each line below contains the name of only one section or variable. 

::

         NAME           length           Comment
   Grid
     Start_point          (3)
     nr of points x       (one integer)
     nr of points y       (idem)
     nr of points z       (idem)
     total nr of points   (idem)
     x-vector             (3)
     y-vector             (3)
     z-vector             (3)
     nr of symmetries     (one integer)
     labels               (nr of symmetries160 characters)
     unrestricted         (one logical)
   SumFrag
     CoulPot              (total nr of points)
     XCPot_A              (idem)   spin-restricted: XCPot
     XCPOt_B              (idem)
     Density_A            (idem)   spin-restricted: Density
     Density_B            (idem)
     Fitdensity_A         (idem)   spin-restricted: Fitdensity
     Fitdensity_B         (idem)
     Kinetic Energy Density_A (idem)   spin-restricted:
                                       Kinetic Energy Density
     Kinetic Energy Density_B (idem)
     ELF_A                (idem)   spin-restricted: ELF
     ELF_B                (idem)
   Ortho
     Same variables as in SumFrag
   SCF
     Same variables as in SumFrag and Ortho, and:
     DensityLap_A         (idem)   spin-restricted: DensityLap
     DensityLap_B         (idem)
     DensityGradX_A       (idem)   spin-restricted: DensityGradX
     DensityGradX_B       (idem)
     DensityGradY_A       (idem)   spin-restricted: DensityGradY
     DensityGradY_B       (idem)
     DensityGradZ_A       (idem)   spin-restricted: DensityGradZ
     DensityGradZ_B       (idem)
     DensityHessXX_A      (idem)   spin-restricted: DensityHessXX
     DensityHessXX_B      (idem)
     DensityHessXY_A      (idem)   spin-restricted: DensityHessXY
     DensityHessXY_B      (idem)
     DensityHessXZ_A      (idem)   spin-restricted: DensityHessXZ
     DensityHessXZ_B      (idem)
     DensityHessYY_A      (idem)   spin-restricted: DensityHessYY
     DensityHessYY_B      (idem)
     DensityHessYZ_A      (idem)   spin-restricted: DensityHessYZ
     DensityHessYZ_B      (idem)
     DensityHessZZ_A      (idem)   spin-restricted: DensityHessZZ
     DensityHessZZ_B      (idem)
     DenSigned            (idem)   sign( :math:`\lambda`\ :sub:`2` ) :math:`\rho`
     FitDenSigned         (idem)
     RDG                  (idem)   reduced density gradient
     FitRDG               (idem)
     NCI                  (idem)   +/-1 flag for non-covalent interaction regions
     FitNCI               (idem)
     SEDD                 (idem)   single exponential decay detector
     DORI                 (idem)   density overlap regions indicator
   Core
     Density              (total nr. of points)
     DensityGradX         (idem)
     DensityGradY         (idem)
     DensityGradZ         (idem)
     DensityHessXX        (idem)
     DensityHessXY        (idem)
     DensityHessXZ        (idem)
     DensityHessYY        (idem)
     DensityHessYZ        (idem)
     DensityHessZZ        (idem)
   TransDens_L1_L2                    L1: SS or ST; L2 is excitation's symmetry
     Fitdensity_1         (total nr. of points)
     Fitdensity_2         (idem)
     Fitdensity_3         (idem)
     Coulpot_1            (idem)
     Coulpot_2            (idem)
     Coulpot_3            (idem)
   SCF_label_A
        (label is a symmetry subspecies.
         Spin-restricted: SCF_label)
     nr of orbitals       (one integer)
     Occupations          (nr of orbitals)
     Eigenvalues          (idem)
     1                    (total nr of points)
     2                    (idem)
     3                    (idem)
        (as many as there are Molecular Orbitals in that
         symmetry representation for the indicated spin)
   SCF_label_B 
        (only if spin-unrestricted same variable as
         in SCF_label_A)
   SO_label
        (label is a double group symmetry subspecies.)
     1_alpha_R            (total nr of points) real alpha part of the 1st spinor 
     1_beta_R             (idem) real beta part of the 1st spinor
     1_alpha_I            (idem) imaginary alpha part of the 1st spinor
     1_beta_I             (idem) imaginary beta part of the 1st spinor
     2_alpha_R            (idem) real alpha part of the 2nd spinor
     2_beta_R             (idem) real beta part of the 2nd spinor
     2_alpha_I            (idem) imaginary alpha part of the 2nd spinor
     2_beta_I             (idem) imaginary beta part of the 2nd spinor
        (as many as there are spinors in that
         double group symmetry representation)
   LocOrb_A                           if unrestricted, otherwise
                                      LocOrb
     nr of orbitals       (one integer)
     1                    (total nr. of points)
     2                    (idem)
     (etc)
   NOCV
     Dens_A number(occupation number)     (total nr. of points)
     Dens_B number(occupation number)     (idem)
     (etc)
   Profile
     DifDens_A number*(NOCV eigenvalue)   (number of profile points)
     DifDens_B number*(NOCV eigenvalue)   (idem)
     DifSumDens_A number                  (idem)
     DifSumDens_B number                  (idem)
     DifRestSumDensities_A                (idem)
     DifRestSumDensities_B                (idem)
     DifSumBelow_A                        (idem)
     DifSumBelow_B                        (idem)
     Dens_A number*(NOCV eigenvalue)      (idem)
     Dens_B number*(NOCV eigenvalue)      (idem)
     SumDens_A number                     (idem)
     SumDens_B number                     (idem)
     RestSumDensities_A                   (idem)
     RestSumDensities_B                   (idem)
     SumBelow_A                           (idem)
     SumBelow_B                           (idem)
   Geometry
     nnuc                 (one integer)
        (nr of nuclei, omitting dummy atoms)
     xyznuc               (nnuc times 3) 
        (the atoms are not in the same order as in the adf input
         file. Rather they are grouped by atomtype.)
     qtch                 (nnuc)       Atomic charges
   x values
          x values        (total nr. of points)
   y values
          y values        (idem)
   z values
          z values        (idem)


.. only:: html

  .. rubric:: References

.. [#ref1] A.\  Michalak, M. Mitoraj, and T. Ziegler, *Bond Orbitals from Chemical Valence Theory*, `Journal of Physical Chemistry A 112, 1933 (2008) <https://doi.org/10.1021/jp075460u>`__ 

.. [#ref2] P.\  de Silva, J. Korchowiec, T.A. Wesolowski, *Revealing the Bonding Pattern from the Molecular Electron Density Using Single Exponential Decay Detector: An Orbital-Free Alternative to the Electron Localization Function*, `ChemPhysChem 13, 3462 (2012) <https://doi.org/10.1002/cphc.201200500>`__ 

.. [#ref3] P.\  de Silva and C. Corminboeuf, *Simultaneous Visualization of Covalent and Noncovalent Interactions Using Regions of Density Overlap*, `Journal of Chemical Theory and Computation 10, 3745 (2014) <https://doi.org/10.1021/ct500490b>`__

.. [#ref4] E.R. Johnson, S. Keinan, P. Mori-Sánchez, J. Contreras-García A.J. Cohen, and W. Yang, *Revealing Non-Covalent Interactions*, `Journal of the AmericanChemical Society 132, 6498 (2010) <https://doi.org/10.1021/ja100936w>`__

.. [#ref5] J.\  Contreras-García E.R. Johnson, S. Keinan, R. Chaudret, J-P. Piquemal, D.N. Beratan, and W. Yang, *NCIPLOT: A Program for Plotting Noncovalent Interaction Regions*, `Journal of Chemical Theory and Computation 7, 625 (2011) <https://doi.org/10.1021/ct100641a>`__

