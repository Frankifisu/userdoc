.. _TAPE21:
.. index:: TAPE21 
.. index:: adf.rkf 

adf.rkf (TAPE21)
================

adf.rkf is the general result file of an ADF calculation. In ADF<=2019 it was known as TAPE21.
It is a KF file: Direct-Access, binary, and keyword driven. It contains information about the calculation. You can use it as a fragment file in a subsequent calculation on a bigger molecule, where the current one may be a part, or in an analysis program. 
Part of what used to be on TAPE21 is since the AMSification of ADF in ams.rkf.

The contents of adf.rkf is keyword-accessible and you may use the KF utilities (see `Scripting Section <../../Scripting/Commandline_Tools/KF_command_line_utilities.html>`_) for conversion of adf.rkf from binary to ASCII format and vice versa. This facility is also useful when you intend to use a adf.rkf result file produced on one type of hardware, for a continuation run on a quite different computer: Transform the binary file to ASCII format with the KF utilities on the first machine. Then transport the ASCII file to the other machine, and make a binary out of it again. 

Another utility (*pkf*) can be used to obtain a summary of the contents of adf.rkf. The output should be more or less self-documenting: all variables are listed by name, type (integer, real, ..) and size (number of array elements) and grouped in named sections. 

The data on adf.rkf is organized in Sections which group together related data. Each section contains a number of variables. Each variable may be an array or a scalar and may be integer, real, logical or character type. 

A complete dump of the contents of adf.rkf is obtained with *dmpkf*. The resulting ASCII file contains for all variables on the file: 

+ The name of the section it belongs to;

+ The name of the variable itself;

+ Three integers coding for the data of the variable:

+ The number of data elements reserved on the file for the variable;

+ The number of data elements actually used for the variable.    In virtually all cases the number of *used* elements is equal to the number of *reserved* elements.    The number of *used* elements is relevant for interpreting the data, the    number of *reserved* elements    has only relevance for the management of    data on the file by kf-specific modules and utilities;

+ An integer code for the data type: 1=integer, 2=real, 3=character, 4=logical;

+ The variable value(s).

A typical case of the contents of adf.rkf obtained by *dmpkf* operating on the binary adf.rkf file from an optimization run on H2O would be: 

.. csv-table:: 
   :widths: 250,350

   **contents of adf.rkf**,**comment**
   General,name of (first) section
   file-ident,name of (first) variable in the current section (General)
   6 6 3,"characteristics of the data: 6 elements reserved    on file for the variable, 6 data elements actually used, 3=integer code    for the data type: character"
   TAPE21,Value of the variable fileident in the section General.
   General,again: name of the section
   title,name of the (second) variable
   80 80 3,"reserved and used number of data elements    (both 80), and the data type code (3: character)"
   Water Geometry Optimization with Internal Coordinates,value
   (etc.),(etc.)
   
A description of the various utilities that can be used to process adf.rkf can be found in other parts of this ADF manual. 

ams.rkf 
-------

The main ams.rkf file is written by the AMS driver. It contains high level
information about the trajectory that the AMS driver took over the potential
energy surface.
This file contains information on geometry optimization, transition state search,
linear transit, PES scan, NEB, or IRC, if that was requested in the calculation.
For a geometry optimization or transition state search, for example, it contains the
history of how the systems geometry changed during the optimization as well as
the final optimized geometry.
The format in which this information is written
is independent from which engine was used for a calculation.

If a property, like vibrational modes, is tied to a special point on the potential energy surface,
it is stored in the engine main output file adf.rkf.

Contents of adf.rkf 
-------------------

Follows a survey of the sections and variables on adf.rkf (formerly known as TAPE21).
Details may differ between different kind of calculations (SinglePoint, normal modes, ...). Most items should be self-explanatory. Some are only significant for internal proceedings of the program and will not be explained in detail. The sections are described in an order that corresponds to the order in which they are generated and hence printed by the KF utility programs. However, the order of generation depends somewhat on the type of application, so some difference may be found when comparing to your own adf.rkf printout. 

Note that after the AMSification of ADF properties about the trajectory that the AMS driver took over the potential
energy surface are written to ams.rkf.
The vibrational modes are written to adf.rkf, but are in a different format than it used to be.

Note that variable and section names may contain spaces: these are significant. 

A special section is the 'SUPERINDEX' section, which is in fact a table-of-contents that lists all the sections in the file, with technical information regarding their position on the file, the amount of data corresponding to that section and similar items. The SUPERINDEX section is not discussed further here. See the KF documentation for more details. 

**Section General**

General information about the calculation and the file 

``fileident``
   Name of the file. Here: adf.rkf 

``jobid``
   ADF release number with date and time of the calculation 

``title``
   Title of the calculation. This may have been set in the input file, or be internally generated. In a create run it is picked up from the Create basis set file (if no input value for the title key has been given). 

``runtype``
   The type of calculation, for instance SinglePoint or Frequencies 

``nspin``
   1 for a spin-restricted calculation, 2 for spin-unrestricted 

``nspinf``
   Similar for the fragment occupation numbers as they are used in the calculation, See the key FRAGOCCUPATIONS 

``ldapot``
   An integer code for the applied LDA part of the XC potential functional used in the SCF. 1 for VWN, 2 for VWN+Stoll ... 

``xcparv``
   X-alpha parameter value. Only relevant for the X-alpha LDA potential, meaningless if another LDA potential functional has been selected. 

``ldaen``
   As for ldapot: integer code for the LDA part of the Density Functional, now however pertaining to the (post-SCF) energy evaluation. Usually ldaen and ldapot are identical. See the key XC for details. 

``xcpare``
   As xcparv, but now for the energy evaluation. 

``ggapot``
   Specification (string) of the GGA part of the XC potential used in the SCF, for instance 'Becke Perdew'. If no GGA potential is applied, the string ggapot is empty. 

``ggaen``
   Similar for the GGA part of the XC energy evaluation 

``iopcor``
   Code for usage of frozen core: 1=use frozen cores, 0=pseudopotentials. Pseudopotentials are not supported anymore in ADF, so this variable must always be 1. 

``electrons``
   The number of valence electrons Note that this is not necessarily the same as what may consider, chemically, as the valence space. Rather, it equals the total number of electrons in the calculation minus the electrons in the frozen core orbitals. 

``unit of length``
   Transformation factor between input-used geometrical units (for distances) and atomic units (bohr). If input of, say, the atomic coordinates is in Angstrom, the unit of length is approximately 1.89 

``unit of angle``
   Similar for angles. Internal units in the program are radians. Input (bond and dihedral angles) may be in degrees, in which case the unit of angle equals approximately 0.017 

**Section Geometry**

Geometrical data such as number of atoms, coordinates, etc: Most variable names should be self-explanatory 

``grouplabel``
   Point group symmetry (string) used in the calculation, for instance O(H). This may be set in the input file. 

``Geometric Symmetry``
   Auto-determined ('true') symmetry (considering the nuclear frame and any external fields, but not taking into account any user-defined MO occupation numbers and hence the electronic charge distribution. 

``symmetry tolerance``
   Threshold for allowed deviation of input atomic coordinates from symmetry to be detected or verified. 

``orient``
   Affine transformation (3,4 matrix: rotation and translation) between the input coordinates and the frame in which the program processes the atoms. ADF has certain orientation requirements for all supported point group symmetries and may rotate and translate the input coordinates accordingly. 

``oinver``
   The inverse transformation of orient 

``lrotat``
   A logical flag to signal whether or not a rotation has been applied between the input frame and the internally used frame. 

``nr of fragmenttypes``
   The number of distinct types of fragments 

``nr of dummy fragmenttypes``
   Idem, but counting only dummy atom fragments. A dummy fragment, if it exists, must consist of one single (dummy) atom. 

``fragmenttype``
   Names (string) of the fragment types. 

``fragment mass``
   Sum of atomic masses in the fragment. 

``fragment charge``
   An array with 3 values per fragment type (nftypes,3): 1=sum of nuclear charges, 2=sum of effective nuclear charges (discounting for the frozen core shells), 3=nr of valence electrons 

``fframe``
   Signals whether or not special local coordinate frames are used for the atoms. Usually this is not so, in which case the variable has the value DEFAULT. fframe is an array that runs over the atoms. See the 'z=' option to the data in the ATOMS input key block. 

``cum nr of fragments``
   An array (0:nftyps) that gives the total number of fragments for the fragment types up to and including the indexed one. The ordering of fragments and fragment types is printed in the standard output file. 

``nr of fragments``
   The total number of fragments in the calculation This equals the last element of the previous variable 'cum nr of fragments' 

``nr of dummy fragments``
   The total number of fragments that each consist of a single dummy atom. 

``fragment mapping``
   Affine transformation matrices (3,4: rotation and translation), one for each fragment in the molecule, that transform the fragment coordinates as they are on the fragment file(s), to the actual position of the fragments in the molecule. 

``cum nr of atomtypes``
   An array (0:fragmenttypes) that counts the number of atom types up to and including the indexed fragment type. 

``nr of atomtypes``
   Total number of atom types in the molecule. Must equal the last element of the 'cum nr of atomtypes' array 

``nr of dummy atomtypes``
   Similar, now counting only the atom types consisting of a dummy atom. 

``atomtype``
   Names (strings) of the atom types 

``mass``
   Atomic masses: array running over the atom types. Compare 'fragment mass'. 

``charge``
   Similar as for 'fragment charge', but now the values per atom type. 

``cum nr of atoms``
   An array (0:atomtypes) that counts the number of atoms up to and including the indexed atom type. 

``nr of atoms``
   Total number of atoms. Must equal the last element of the array 'cum nr of atoms'. 

``nr of dummy atoms``
   Total number of dummy atoms 

``atmcrd``
   Type of atomic coordinates in input: CART (Cartesian) or ZMAT (Internal). 

``kmatrix InputOrder``
   The connection matrix listing (and referencing) the atoms in the order as they were in the input file. This ordering aspect is significant because internally the program reorders the atoms and groups them together by atom type and fragment type. Hence it is relevant to know what ordering (input- or internal-) is assumed in data arrays. 

``zaxis``
   For each atom the direction of the local z-axis. Normally this is identical to the standard (0,0,1), but it may be different for analysis purposes. See the 'z=' option to the data records in the ATOMS block. 

``fragment and atomtype index``
   An integer array (natoms,2) that specifies for each atom the fragment and the atom type it belongs to. 

``atom order index``
   An integer array (natoms,2) that defines the re-ordering of atoms between the list in the input file and the internally used list (which is driven by fragment types, fragments, atom types; dummies come last). The internally used list can be derived from the printout of the fragments, early in the standard output. 

``kmatrix``
   The connection matrix using the internally applied ordering of atoms 

``xyz``
   Cartesian coordinates of the atoms, in the internally used ordering of atoms 

``xyz Inputorder``
   Similar, but now for the ordering of atoms as in the input file. 

``zmatrix``
   Internal (Z-matrix) atomic coordinates 

``zmatrix Inputorder``
   Internal coordinates in the input-order of atoms 

``Atomic Distances``
   Inter atomic distance matrix 

``ntyp``
   Number of atom types, not counting dummy atoms, 

``nqptr``
   A cumulative counting array, very similar to 'cum nr of atoms' Differences: it runs only over 'ntyp' atom types (not including dummy atoms) and its indexing as well as its values are shifted by one: nqptr(k) is the total number of atoms plus one, counting the atom types up to and including #(k-1) 

``nnuc``
   Total number of non-dummy atoms 

``qtch``
   Nuclear charges of the non-dummy atoms 

``qeff``
   Effective nuclear charges (subtracting charge for the frozen core shells) of the non-dummy atoms 

``nfragm``
   Total number of non-dummy fragments 

``nofrag_1``
   Integer array specifying for each non-dummy atom the fragment it belongs to. 

``nofrag_2``
   Integer array specifying for each non-dummy atom the fragment type it belongs to 

``nuclab``
   Names of the non-dummy atom types. 

**Section Fragments**

(To be completed) 

``FragmentFile``
   Names of all used fragment files 

``FragRun Ident,Title``
   Job identification and title of each fragment run that is used in the current molecule 

**Section AtomTypes**

(To be completed) 

**Section Properties**

``AtomCharge Mulliken``
   Atomic charges derived from Mulliken population analysis. 

``Dipole``
   Dipole moment in atomic units. 

``FragmentCharge Hirshfeld``
   Fragment charges derived from Hirshfeld analysis 

``AtomCharge_initial Voronoi``
   Atomic charges derived from Voronoi analysis for the initial (sum-of-fragments) charge density 

``AtomCharge_SCF Voronoi``
   Similar as the previous item, but now for the SCF density 

``Electrostatic Pot. at Nuclei``
   Coulomb potentials at the positions of the atoms, not including the contribution from the nucleus itself 

**Section Basis**

Information about the (valence) basis set 

``nbset``
   The total number of basis 'sets', where a 'set' here means a Cartesian function set (3 for a *p*-type function, 6 for a *d*-type function, and so on), given by an entry in the 'list-of-basis-functions' in the data base file. 

``nbaspt``
   Cumulative number of basis sets (see previous variable, for 'set'), on a per atom type basis. Only non-dummy atoms (type) are considered. nbaspt(k) is 1+nr-of-basis sets up to, but not including atom type #k 

``nqbas``
   Main quantum number of each basis set. A 1s function has nqbas()=1 

``lqbas``
   Angular momentum quantum number of each basis set. The current implementation of ADF supports only *s, p, d,*and* f* basis functions, so the allowed lqbas values are 0, 1, 2, and 3 

``alfbas``
   The exponential decay parameters of the STO functions in the basis set 

``basnrm``
   Normalization coefficients for the basis sets 

``naos``
   The total number of basis functions, counting all Cartesian polynomials and all copies of the functions on the atoms of the pertaining atom type 

``nbos``
   The total number of Cartesian basis functions, *not* counting the copies of the functions on the different atoms of the atom type: the functions are defined per atom type and are (for nbos) counted only once. The next few variables relate to lists of basis functions that run from 1 to nbos: all the Cartesian polynomials, but counting the function only once per atom type. Essentially, this means counting all functions with distinct characteristics (apart from their geometrical center). 

``nbptr``
   Index array of the nbos functions, where the entries are the cumulative numbers of functions (+1) up to, but not including the atom type. The size of the array is (ntyp+1): one plus the number of (non-dummy) atom types. 

``kx``
   Powers of x of the nbos Cartesian STO basis functions 

``ky``
   Powers of y of the nbos Cartesian STO basis functions 

``kz``
   Powers of z of the nbos Cartesian STO basis functions 

``kr``
   Powers of r of the nbos Cartesian STO basis functions 

``alf``
   Exponential decay factors of the nbos Cartesian STO basis functions 

``bnorm``
   Normalization factors for the nbos Cartesian STO basis functions 

``nprta``
   Consider a list of all (naos) Cartesian STO basis functions, including copies of the functions on all atoms of the same atom type. Build that list by first taking all true valence functions on all atoms (loop over atom types, inner loops over atoms, inner loop over basis sets of the atom type, inner loop over Cartesian polynomials for the function set), then all auxiliary core-orthogonalization functions (similar loop structure). nprta(i) gives the index in that list of function #*i*, where *i* corresponds to a similar list of all naos functions in which the core and valence subsets are not separated. 

``norde``
   An array that runs over the non-dummy atom types. Each element gives the maximum of the main quantum number for all STO basis and fit functions corresponding to that atom type. 

``lorde``
   As norde, but lorde applies to the angular momentum quantum numbers. 

**Section Core**

Information about frozen core orbitals and the Slater-type exponential functions used to describe them. 

``nrcset``
   The number of STO function sets to describe the frozen core orbitals in the calculation. The array is sized (0:llqcor,1:ntyp). llqcor is the maximum l-value in core orbitals (3), ntyp is the number of non-dummy atom types. 

``nrcorb``
   An array (0:llqcor, 1:ntyp) specifying the number of frozen core orbitals per *l*-value and per non-dummy atom type. 

``ncset``
   The total number of core expansion STO function sets, not counting copies on all atoms, and not counting the Cartesian polynomials (1 value per *p*-set, et cetera) 

``ncorpt``
   Index array: 1 + cumulative number of core expansion sets up to, but not including, the indexed atom type. The array runs from 1 to ntyp+1 

``nqcor``
   Main quantum numbers for the core expansion sets 

``lqcor``
   Angular momentum quantum numbers for the core expansion sets. 

``alfcor``
   Exponential decay factors for the core expansion sets. 

``cornrm``
   Normalization factors for the core expansion sets. 

``ncos``
   Total number of core expansion functions, counting all copies on different atoms of each atom type, and counting all Cartesian polynomials. 

``nccpt``
   Index array: 1 + cumulative number of core orbitals, counting all copies on different atoms and all Cartesian (sub) functions. 

``ncptr``
   Similar, but applying to the STO core expansion functions. 

``ccor``
   All core expansion coefficients, which express the core orbitals in the core expansion functions. The array stores the expansion coefficient sequence for each core orbital shell (not for each Cartesian sub function) and only one sequence per orbital per atom type (no duplication for the different atoms of the atom type). 

``npos``
   An index array. For each atom type: the index where its data are stored on the adf.rkf core data file. npos(k) may be zero if no data for atom type #k are available on TAPE12. 

``kcos``
   The total number of core expansion functions, like ncos, but now counting only the truly independent functions. For instance: 5 functions per *d*-set, while in ncos there are 6 functions per *d*-set. The *s*-type combination in the 6-membered *d*-set is in the calculation projected out and does not represent a degree of freedom. 

``s``
   The (kcos,kcos) overlap matrix of the core expansion functions. Note that, since the dimension is (kcos,kcos), the *s*-type combination has been eliminated, and likewise for the 3 *p*-type functions in each *f*-set. 

``idfcor``
   Integer that indicates whether or not the core set contains *d*- and/or *f*-type functions. 1=yes, 0=no 

``nd``
   Total number of *d*-type core orbital sets (not counting the Cartesian sub functions) 

``nf``
   Total number of *f*-type core orbital sets (not counting the Cartesian sub functions) 

``ndorb``
   An array running over the *d*-type core orbital sets (loop over atom types, loop over atoms, loop over core orbitals with *l*=2). It gives for each the index of the orbital (the first of the Cartesian subset) in the overall list of all core orbitals in the molecule (including the spurious *s*-type functions in the *d*-sets, and so on) 

``nforb``
   Similar as ndorb, but now for the *f*-type core orbitals. 

``cmat``
   Overlap matrix between core-orbitals (ncos, counting all Cartesian functions including the *s*-type function in each *d*-set, et cetera), and the basis functions. In the list of basis functions, all core functions (the auxiliary orthogonalization functions) come before all true valence basis functions, see array NPRTA. 

**Section Fit**

This section stores information about the fit functions, which are used for the Coulomb potential evaluation. 

``Unrestr.SumFrag``
   A logical that flags whether or not the fit coefficients have been set and stored for the sum-of-fragments, but adjusted for the unrestricted fragments option (see the keys UnrestrictedFragments, ModifyStartPotential). 

``coef_SumFrag``
   Fit coefficients pertaining to the sum-of-fragments charge density. 

``coef_SCF``
   SCF fit coefficients. 

``nfset``
   Total number of fit function sets (not counting the Cartesian sub functions, not counting the copies of the functions on the atoms of an atom type) 

``nfitpt``
   Index array: 1+the total number of fit function sets up to, but not including, the indicated atom type. 

``nqfit``
   Main quantum numbers of the fit sets 

``lqfit``
   Angular momentum quantum numbers of the fit sets 

``alffit``
   Exponential decay factors of the STO fit sets. 

``fitnmr``
   Normalization factors for the STO fit sets. 

``nfos``
   Total number of Cartesian fit functions, not counting copies on all atoms of an atom type, but including all (for instance, 6 for a *d*-set) Cartesian sub functions. 

``nfptr``
   Index array: 1+ total number of Cartesian (see variable nfos) fit functions, up to but not including the indicated atom type. 

``nprimf``
   Total number of Cartesian ('primitive') fit functions, counting also the copies on all atoms of each atom type. 

``nsfos``
   The total number of fully symmetric (A1 symmetry) fit function combinations that represent the true dimension (variational freedom) of the space of fit functions in the calculation. 

``na1ptr``
   Index array, like nfptr, but applying to the nsfos symmetric function combinations. 

``niskf``
   This refers to an atom-limited symmetry combination of primitive fit functions, in the code and some documentation indicated as a 'g'. A 'g' is the specific part of a molecule-wide A1 fit function combination (see nsfos) that consists of all the terms that are centered on one particular atom. The number niskf gives the total number of such 'g' function combinations. To clarify this, consider an A1 fit function combination in the molecule. Assume, that it consists of a specific linear combination the following functions: a p-x function on atom A, its partner p-y function, and the corresponding p-x and p-y functions on atom B. (Atoms A and B must be symmetry equivalent). In this example we have one A1 function (in the list of nsfos such functions) and two 'g''s. Each 'g' consists of a p-x and a p-y function combination on a specific atom. 

``iskf``
   Compound index array. It runs over the niskf 'g' fit function combinations and has 4 entries for each function (1:4,1:niskf). The meaning of the entries is as follows. #1=number of the fit set (not counting the copies of fit functions on different atoms of an atom type, and not counting the Cartesian sub functions) this 'g' belongs to. #2=index where the combination coefficients for this 'g' start in the arrays cofcom and numcom (see next). #3=number of terms in the expansion of this 'g'. #4=number of the molecular fit A1 function combination this 'g' belongs to. 

``na1cof``
   Length of the arrays numcom and cofcom, see next 

``numcom``
   Numcom (and cofcom) consists of a sequence of smaller sub arrays. Each sub array gives the expansion of a 'g' function in terms of the Cartesian functions in the pertaining fit function set. The elements of numcom specify the particular Cartesian sub functions that participate in the expansion. Its values are therefore limited to lie between 1 and (L+1)(L+2)/2, where L is the maximum *l*-value occurring in the fit function sets. 

``cofcom``
   Compare numcom: cofcom gives the actual expansion coefficients for the expression of a 'g' function in primitive Cartesian fit functions. 

**Section Num Int Params**

Numerical integration parameters: the general precision parameter, but also more technical parameters used by the grid-generating modules. 

``method``
   Label of the method used to generate the grid. Usually: 'polyhedra' 

``accint min``
   Minimum integration precision parameter. It is the lower bound of the range in which the value of the actual numerical integration precision parameter may vary. 

``accint max``
   Maximum value of the precision general parameter 

``accint``
   Actual value of the precision parameter. This variable governs by default almost all other integration parameters. 

``ldim``
   In fact, this a geometric parameter: the number of dimensions in which the system is periodic. For molecules this is zero. 

``PointChargeTypes``
   The number of point charges types used in the calculation. Point charges belong to a different point charge type if, and only if, their strengths are not equal. 

``accsph``
   The precision parameter that determines the (radial) integration grid in the atomic spheres 

``accpyr``
   The precision parameter that determines the general precision level of the grid in the atomic polyhedra 

``accout``
   The precision parameter that determines the general precision level of the grid in the outer region 

``accpyu``
   The precision parameter that determines the 1D grid along the first direction in the quadrangles and triangles of the bases of the atomic pyramids 

``accpyv``
   The precision parameter that determines the 1D grid along the second direction in the quadrangles and triangles of the bases of the atomic pyramids 

``accpyw``
   The precision parameter that determines the 1D radial integration in the atomic pyramids, between the atomic sphere surfaces and the pyramid basis 

``frange``
   Estimated maximum range of functions, to determine how far the integration grid has to extend outwards, away from the molecule 

``rspher``
   An array with the radii of the atomic sphere (a value per atom type) 

``rsph0``
   The smallest sphere radius 

``rsphx``
   The largest sphere radius 

``dishul``
   The distance between the innermost boundary planes, which separate the atomic pyramids from the outer region, and the surfaces of the outermost atoms 

``nouter``
   The number of intervals in which the outward (radial) integration in the outer region is broken up 

``outrad``
   The precision parameter that determines the outward radial integration in the outer region 

``outpar``
   The precision parameter that determines the 2D integrals in the outer region parallel to the boundary planes 

``linteg``
   An array with maximum angular momentum quantum numbers (one value per atom type), to determine the angular integration grid in the atomic spheres 

``lintgx``
   Maximum of linteg() 

``linrot``
   Angular momentum quantum number to determine the rotational integration parameter around the molecular axis (in linear molecules only) 

``ntyps``
   The number of atom types as seen by the numerical integration grid generator. This means in practice: the number of non-dummy atom types plus the number of point charge types. 

``nnucs``
   The number of atoms as seen by the numerical integration grid generator. This means in practice: the number of non-dummy atoms plus the number of point charges. 

``qatm``
   Nuclear charges for all ntyps atom types 

``nratst1``
   The numerical integration grid generator automatically determines the symmetry of the nuclear (nnucs atoms!) frame and then puts the atoms in sets of symmetry equivalent ones. nratst1() is an array (0:ntyps) that contains the cumulative number of atoms in the symmetry sets. nratst1(k) is the total number of atoms in the sets up to and including set #k 

``xyzatm``
   Cartesian coordinates of the atoms. 

``linteg all``
   Similar to array linteg(), extended to include also the point charge types 

``npowx``
   Maximum power of the radial variable *r*, in the set of test functions that the grid generator uses to tune the grid 

``alfas``
   An array that stores the exponential decay factors of all test functions, ordered by atom type and by the power of the radial variable *r*. 

**Section Symmetry**

Symmetry related data. 

``nogr``
   The number of symmetry operators in the point group used in the calculation. NB, for the special cases of infinite symmetries, only the operators corresponding to finite elements are counted. Therefore, ATOM has nogr=1 (only the unit operator); C(LIN) has nogr=1, D(LIN) has nogr=2. 

``faith``
   An array that stores all the (3,3) symmetry operator matrices in the real space representation 

``nsetat``
   The number of sets of symmetry equivalent atoms under the used symmetry 

``napp``
   An array that stores for each atom the number of the symmetry set it belongs to 

``notyps``
   An array that stores for each set of symmetry equivalent atoms, the atom type to which the set belongs 

``noat``
   Map between the normal list of atoms and the symmetry sets. When you loop over the symmetry sets and, inside, loop over the atoms in each set, you thereby run over the index of noat(). The value points to the position of that atom in the original (not set-ordered) list. 

``ntr``
   An array (nogr,nnuc) that stores for the each atom A and each symmetry operator R, the atom onto with A is mapped by R. The row index runs over all symmetry operators, the column index over the atoms. 

``npeq``
   The number of symmetry unique pairs of atoms 

``jjsym``
   An array that runs over the npeq sets of symmetry equivalent atom pairs. Its value gives for the indicated set the index of a (c.f. the first) atom pair in that set. 

``jasym``
   An array that runs over the npeq sets of equivalent atom pairs. Its value gives for the indicated the set the number of pairs in that set. 

``ja1ok``
   An array (1:npeq), with values 0 or 1. 1=the pair density can be fitted using A1 fit functions only. 0=all fit functions (on the involved atoms) are to be used. The value 1 may arise because of symmetry properties, or because the distance between the atoms is so large that the inaccuracy from using only A1 fit functions can be neglected. 

``ntr_setat``
   A condensed variety of array ntr: the columns are not the atoms, but the nsetat sets of symmetry equivalent atoms. The value is the index of the atom, onto which a representative (c.f. the first) atom of the indicated symmetry set is mapped by the given symmetry operator. 

``igr``
   A code that fixes, together with nogr and ngr, the point group symmetry. See the header of routine adf/maisya for a list 

``ngr``
   One of the code components that fix the symmetry group. See routine adf/maisya 

``grouplabel``
   Schönfliess symbol as used in ADF 

``nsym``
   The number of symmetry representation (including subspecies) used in the calculation. 

``norb``
   For each of the nsym representations the number of basis function combinations (SFOs) that belong to it. 

``nfcn``
   For each of the nsym representations the number of primitive atom centered basis functions that participate in the representation. 

``ncbs``
   For each of the nsym representations the number of core orthogonalization functions that participate in the representation. 

``jsyml``
   For each of the nsym representations: if it belongs to a one-dimensional irrep, the value is 1, otherwise: for the first subspecies in the irrep the value is the dimension of the irrep, for the other subspecies in the same irrep the value is 0 

``symlab``
   For each of the nsym representations the label (string) of the representation 

``norboc``
   An array  (-2:2,nsym). The column runs over the symmetry representations. The positive row indices (1,2) specify for spin-A and spin-B (the latter only if the calculation is spin-unrestricted), the highest non-empty orbital. The negative indices (-1,-2) specify for spin-A and spin-B (if the unrestricted fragment option is used) the total number of non-empty SFOs. The zero row index specifies the number of non-empty SFOs, before applying any fragment occupation changes. 

**Section Spin_orbit**

(To be completed) 

**Section Energy**

``XC energies``
   16 elements of an array enxc(2,2,4): exchange-correlation energies of various charge densities: first index: 1=exchange term, 2=correlation term second index: 1=lda tern, 2=gga term third index: 1=energy of fragments (summed over fragments), 2=energy of sum-of-fragments density, 3=energy of orthogonalized fragments, 4=SCF. 

``Pauli TS Correction (LDA)``
   Correction to the 'Transition State' method to compute terms in the bonding energy, in this case the Pauli exchange energy term. The Pauli TS Correction is not separately printed in the standard output file, but included in the Pauli interaction term. 

``Pauli FitCorrection``
   The first-order correction to the Pauli exchange interaction term, for the error in the Coulomb energy due to the fit incompleteness. This correction term is not printed in the output file but included in the Pauli interaction term 

``Elstat Core terms``
   An obsolete variable, not used in the energy computation 

``Elstat Fitcorrection``
   The first-order correction to the electrostatic interaction term (putting the fragments together, without any relaxation of Pauli orthogonalization), for the error in the Coulomb energy due to the fit incompleteness 

``Orb.Int. FitCorrection``
   The first-order correction to the electrostatic interaction term in the SCF relaxation energy (Orbital Interactions), for the error in the Coulomb energy due to the fit incompleteness. This term is not printed (anymore) separately, but incorporated in the symmetry-specific interaction terms. 

``Orb.Int. TSCorrection (LDA)``
   The difference between the representation-specific orbital interaction terms added, and a straightforward computation of the SCF relaxation energy is the result of the neglect of higher order terms in the Taylor expansion that underlies the 'Transition State' method. This difference, therefore, corrects exactly this neglect. It is not printed separately anymore in the output, but incorporated in (distributed over) the representation-specific orbital interaction terms. 

``Ebond due to Efield``
   Bond energy term due to any homogeneous electric field 

``Corr. due to Orthogonalization``
   For analysis purposes, the concept of 'orthogonalized fragments' has been introduced and the bonding energy is split in a part that describes the difference between the sum-of-fragments situation and the orthogonalized-fragments density at the one hand, and the SCF relaxation (from the orthogonalized fragments density) at the other. Both terms contain a first order fit correction term. The result of adding the two parts is not identical to computing the total bonding energy directly and applying the first order correction to that approach. The difference is given by this term, which therefore corrects for the additional second order fit errors caused by using the orthogonalized fragments split-up 

``SumFragmentsSCF FitCorrection``
   The 'true' first order fit correction for the complete bonding energy, resulting from a direct calculation that takes the sum-of-fragments as starting point and the SCF as final situation, without the intermediate step of orthogonalized fragments. 

``Pauli Efield``
   The contribution to the Pauli interaction energy due to any electric field 

``Orb.Int. Efield``
   The contribution to the SCF relaxation energy (orbital interactions) due to any electric field 

``Electrostatic Interaction``
   The electrostatic interaction energy including any first order fit correction (if computed from the fit density) 

``Pauli Total``
   The Pauli exchange (orbital orthogonalization) interaction energy 

``Steric Electrostatic``
   INCORRECT. Do not use. The electrostatic interaction energy including any first order fit correction (if computed from the fit density) 

``Steric Total``
   The total steric interaction energy, consisting of the electrostatic and the Pauli interactions 

``Orb.Int. *Irrep*``
   *Irrep* stands for one of the irreps of the point group symmetry. The value gives the orbital interaction (SCF relaxation) term for that symmetry representation 

``Orb.Int. Total``
   The total orbital interaction energy 

``SCF Bond Energy``
   Total bonding energy 

``elstat``
   INCORRECT. Do not use. Electrostatic interaction energy. Same as the 'Electrostatic Interaction' variable in this section 

``Bond Energy``
   Total bonding energy, same as the 'SCF Bond Energy' variable 

``Pauli Kinetic``
   Kinetic energy term in the Pauli exchange interaction energy 

``Pauli Coulomb``
   Coulomb energy term in the Pauli exchange interaction energy 

``Pauli Kinetic+Coulomb``
   Sum of the kinetic and Coulomb terms in the Pauli exchange interaction energy 

**Section Point_Charges**

``NumberofPointCharges``
   The total number of point charges used 

``PointCharges``
   The array with point charge values: (4,np), where np is the number of point charges and the 4 components are, respectively, the x y z components and the strength. 

**Section GeoOpt**

Optimization data. 

Where references are made to the list of atoms, the atoms are assumed to be in internal order. This may be different from the input-list of atoms. 

``nfree``
   number of independent optimization variables 

``idfree``
   indices (3,nr-of-atoms) for all atomic coordinates referring to the optimization variables (values 1..nfree) and/or LinearTransit parameters (values nfree+k, k being the k-th LT parameter). A zero value means that the coordinate is frozen. 

``all freedoms``
   A logical the flags whether or not all fundamental degrees of freedom in the system are allowed to vary. This is not the case when constraints are applied. 

``Gradients``
   The most recent values for the derivatives of the energy with respect to the atomic coordinates (cartesian or z-matrix, depending on the type of optimization variables). 

``kmatrix``
   The connection matrix. 

``Hessian_CART``
   The Hessian matrix (second derivatives) as a n*n matrix, in the Cartesian coordinates representation. Note that the reduced storage mode (typically, Fortran upper-triangular) is not applied. 

``Hessian inverted_CART``
   The *inverted* Hessian, in Cartesian coordinates 

Note: in most cases only one, or maybe two of the Hessian cases are present on TAPE13. They can be transformed into each other quite easily. The order of atoms is the same as in the input. 

**Sections Ftyp n**

*n* is an integer. All such sections give general information about fragment type #n, and more specifically about the ADF calculation that produced the corresponding fragment file. 

``jobid``
   Job identification of the fragment run 

``title``
   Title of that calculation 

``nsym``
   Number of symmetry representations (subspecies) used 

``norb``
   For each representation the size of the Fock matrix (variational degrees of freedom) 

``bb``
   Labels of the subspecies 

``igr``
   (Partial) code for the point group symmetry 

``ngr``
   (Partial) code for the point group symmetry 

``grouplabel``
   Schönfliess symbol of the point group symmetry (of the fragment calculation) 

``nfcn``
   An array over the representation: for each subspecies the number of primitive STO basis functions that participate in that subspecies 

``jsyml``
   An array (1:nsym). Value 1 means that the corresponding subspecies belongs to a 1D irrep. A value larger than 1 means a correspondingly higher dimensionality of the irrep *and* indicates that that subspecies is the first in that irrep. A value 0, finally, means that it is not the first subspecies in its irrep. 

``nfrag``
   Number of fragments used in that fragment calculation 

``natom``
   Number of atoms in the fragment 

``naos``
   Number of primitive atomic basis functions 

``nrat 1``
   Maps the atoms of this fragment (the '1' signals the first fragment of this type) onto the list of all atoms 

``rotfrg``
   Rotation matrix to map the fragment coordinates as they are on the fragment file onto their actual orientation in the molecule 

``nsot``
   Total number of MO degrees of freedom, summation over all subspecies 

``nmis``
   The number of symmetry representations that could not be spanned by the basis set 

``mis``
   Indices of the missing symmetry representations 

**Sections Ftyp n?**

*n* stands for the n-th fragment type. The ? stands for one of the symmetry representations (of the point group symmetry used in the fragment calculation) 

``froc``
   MO occupation numbers for the MOs in this subspecies 

``eps``
   Orbital energies When they result from a ZORA calculation, the non-scaled values are stored on file (the scaled values are printed in the standard output file). 

``eigvf``
   Fragment MO eigenvectors, expressed in all the primitive atomic orbitals of the fragment. 

``nsos 1``
   Total number of MOs in this subspecies: size of variational problem 

``nbas 1``
   Number of primitive atomic basis functions that participate in this subspecies 

``npart 1``
   Indices that give for each of the nbas functions, the number of the basis function in the list of all basis functions 

``FO 1``
   The fragment MOs (nbas*nsos coefficients) 

``nocc 1``
   Number of non-empty orbitals 

**Sections X**

X stands here for the label of a subspecies of the point group symmetry, for instance A1. Depending on the point group symmetry, there may be many such sections, each corresponding to one of the subspecies. All such sections have an identical structure. 

``nmo_A``
   The number of MOs with spin-A, for which the coefficient vectors are calculated. During the SCF this may be severely reduced, at the end it is usually the complete basis in the pertaining symmetry representation. 

``nmo_B``
   Similar for spin b. This variable is not present in a restricted calculation. 

``SFO``
   The definition of the SFOs in the representation, consisting of expansion coefficients in terms of the primitive atomic STO basis functions 

``frocf``
   The occupation numbers of the SFOs in this representation 

``npart``
   A list of indices of the bas functions that are used in this symmetry representation 

``froc_A``
   The occupation numbers of the MOs in the representation, for spin-A 

``froc_B``
   Similar for spin-B, if a spin-unrestricted calculation is performed 

``smx``
   Overlap matrix between core functions and SFOs 

``frocor``
   SFO occupation numbers 

``Orth-Bas``
   The orthogonalized fragment orbitals in the BAS representation. 

``Low-Bas``
   The Lowdin orbitals in the BAS representation: the matrix to transform the MOs from Lowdin representation (orthonormalized SFOs) to the BAS representation 

``Eigen_Bas_A``
   mo expansion coefficients in the bas representation for all nmo_A orbitals. The coefficients run over all bas functions indicated by npart 

``Eigen_Bas_B``
   Similar for spin-B, if present 

``eps_A``
   The orbital energies for the nmo_A orbitals of spin-A When they result from a ZORA relativistic calculations, the non-scaled values are stored on file. (The scaled energies are printed in standard output. 

``eps_B``
   Similar for spin-B, if present 

``Eig-CoreSFO_A``
   MOs expressed in SFOs, for spin-A MOs 

``Eig-CoreSFO_B``
   Similar for spin-B 

**Sections Atyp n X**

Each such section contains the (core- and possibly also valence-) radial density and potential of one particular atom type. *X* is the atom type label and *n* is an index running over all atom types in the calculation. The list of all atom types is printed on standard output in the early geometry section. 

The radial densities and potentials may be represented as simple tables - a sequence of values for *r*, the distance to the nucleus, and the corresponding density or potential - or as a piecewise expansion in Chebyshev polynomials over a sequence of intervals (r1,r2). 

The core density and potential have been constructed from the Frozen Core orbitals, which are defined in the section Core. If a TAPE12 (corepotentials) file has been attached to the calculation the core data is read off from that TAPE12 and stored also. 

``rx val``
   Maximum r-value for which the valence density is non-negligible 

``nrint val``
   Number of intervals for piecewise expansion of the valence density in Chebyshev polynomials 

``rup val``
   Arrays (1..nrint) of upper bounds of the intervals. The lower bound of the first interval is zero 

``ncheb val``
   Array (1..nrint) with the number of expansion coefficients for each interval 

``ccheb val``
   Coefficients of the expansion. All coefficients, for all intervals, are stored contiguously in one linear array. The parts pertaining to a particular interval are determined by using the arrays ncheb() 

``nrad``
   Number of points used in the direct tabular representation of the atomic densities and potentials 

``rmin``
   The first r-value of the table: the radial grid is defined by a first value (rmin), a constant multiplication factor defining rk+1 w.r.t. rk (rfac, see next), and the total nr of points (nrad). 

``rfac``
   The multiplication factor of the radial grid 

``valence den``
   The valence density, in a table of nrad values. 

``valence pot``
   Similar for the Coulomb potential of the density, including a nuclear term Q/r, such that the long-range monopole term in the potential is zero 

``qval``
   The number of electrons contained in the valence density 

``rx core``
   Maximum r-value for which the core density is non-negligible 

``nrint core``
   Number of intervals for piecewise expansion of the core density in Chebyshev polynomials 

``rup core``
   Arrays (1..nrint) of upper bounds of the intervals. The lower bound of the first interval is zero 

``ncheb core``
   Array (1..nrint) with the number of expansion coefficients for each interval 

``ccheb core``
   Coefficients of the expansion. All coefficients, for all intervals, are stored contiguously in one linear array. The parts pertaining to a particular interval are determined by using the arrays ncheb() 

``qcore``
   The number of electrons contained in the core density 

``core den``
   The core density, in a table of nrad values. 

``core pot``
   Similar for the Coulomb potential of the density, including a nuclear term Q/r, such that the long-range monopole term in the potential is zero 

**Section LqbasxLqfitx_xyznuc**

This section will be removed again in the future. Temporarily it serves to transfer data from the calling program to the grid generator. 

``lqbasx``
   An array with for each atom type the maximum angular moment quantum number in the basis functions for that type 

``lqfitx``
   An array with for each atom type the maximum angular moment quantum number in the fit functions for that type 

``xyznuc``
   Cartesian coordinates of the non-dummy atoms 

**Section GenptData**

This section will be removed in the future. It serves, temporarily, to transfer data from the calling program to the numerical integration grid generator. Most of the entries here occur also in other sections but are packed together as replacement for previous common block structure. 

``numint``
   Integer code for the type of integration grid. Usual value: 2 (polyhedra method) 

``iexcit``
   Integer flag for excitations (response) calculation 

``lpolar``
   Integer flag for polarizability (response) calculation 

``ldim``
   Number of dimensions of periodicity 

``mdim``
   Dimensionality of the molecule, for instance a linear molecule has mdim=1 

``r0mult``
   A technical parameter that sets the radius outside which the multipole part of the fit coulomb potential functions is separated (from the exponentially decaying part), for separate treatment in the evaluation of the molecular coulomb potential. 

``avec``
   (3,3) matrix with lattice vectors. Only the (ldim,ldim) sub matrix is significant. 

``bvec``
   Inverse of avec (apart from a factor of 2 pi): lattice vectors in reciprocal space. 

``ngimax``
   Maximum number of geometry optimization iterations 

``llbloc``
   Block length determination parameter (maximum) 

``ipnbl``
   Number of integration blocks processed by the current process 

``nbleqv``
   The number of symmetry equivalent blocks to each symmetry unique block of points. This value is 1 if any equivalent blocks are not constructed and used. 

``ngmax``
   The number of integration points, accumulated over all parallel processes 

``nblock``
   The number of integration blocks 

``lblock``
   The block length 

``lblx``
   An upper bound of the block length applied during the computation of the block length 

``nmax``
   The number of integration points generated by this process 

``twopi``
   Value of the constant 2 :math:`\pi` 

``fourpi``
   Value of the constant 4 :math:`\pi` 

**Section Multipole matrix elements**

Information in a response calculation 

``dipole elements``
   The matrix elements of the 3 dipole operator components between occupied and virtual orbitals: outer loop over the operators (in order: y, z, x), loop over virtual MOs, inner loop over occupied MOs 

``quadrupole elements``
   Similar as for dipole. Order of operators: :math:`\sqrt{3}` \*xy :math:`\sqrt{3}` \*yz z2-(x2+y2)/2 :math:`\sqrt{3}` \*xz :math:`\sqrt{3}` \*(x2-y2)/2 

``octupole elements``
   Similar as for dipole and quadrupole. Order of operators: :math:`\sqrt{10}` \*y\*(3\*x2-y2)/4 :math:`\sqrt{15}` \*xyz :math:`\sqrt{6}` \*y\*(4\*z2-x2-y2)/4 z\*(z2-3(x2-y2)/2) :math:`\sqrt{6}` \*x\*(4\*z2-x2-y2)/4 :math:`\sqrt{15}` \*z\*(x2-y2)/2 :math:`\sqrt{10}` \*x\*(x2-3y2)/4 

``hexadecapole elements``
   Similar as for dipole and quadrupole. Order of operators: :math:`\sqrt{35}` \*xy\*(x2-y2)/2 :math:`\sqrt{70}` \*z\*(3x2y-y3)/4 :math:`\sqrt{5}` \*xy\*(6z2-x2-y2)/2 :math:`\sqrt{10}` \*(4yz3-3yz\*(x2+y2))/4 (8z4-24\*z2\*(x2+y2)+3(x4+2x2y2+y4))/8 :math:`\sqrt{10}` \*(4xz3-3xz\*(x2+y2))/4 :math:`\sqrt{5}` \*(x2-y2)\*(6z2-x2-y2)/4 :math:`\sqrt{70}` \*z\*(x3-3xy2)/4 :math:`\sqrt{35}` (x4-6x2y2+y4)/8 

**Section Irreducible matrix elements**

Information in a response calculation 

``irreducible dipole elements``
   The dipole matrix elements between occupied and virtual MOs, as in the section Multipole matrix elements. Here, however, the matrix elements are ordered by symmetry representations and 'symmetry zeros' are omitted. The stored arrays, however, have the same size as in the previous section. See the implementation for details about the storage of this data. (Directory $AMSHOME/adf/response/) 

``irreducible quadrupole elements``
   Similar as for the dipole elements 

``irreducible octupole elements``
   Similar as for the dipole elements 

``irreducible hexadecapole elements``
   Similar as for the dipole elements 

**Section ETS**

Technical data used in the ets procedure. 

``nff``
   Size of array ncspt (next) 

``ncspt``
   Pointer array to find, for each atom type, the first element corresponding to that atom type's section in the arrays ncsett, alfcst, and cfcset, see below 

``ncs``
   Size of the matrices ncsett, alfcst, and cfcset, see below 

``ncsett``
   Build a list of products of core orbital expansion functions, taking only the one-center products and looping over the atom types (not the atoms). ncsett stores the powers of the radial variable *r* for the products (from the main quantum numbers, one subtracted). A product of a 1s and a 2p yields ncsett()=1 

``alfcst``
   Similar as ncsett: the sum of the exponential decay factors of the factor functions 

``cfcset``
   The density matrix corresponding build from the frozen core orbitals (all atom types, but no copies for the distinct atoms of a type), in the representation of the core orbital expansion functions. Stored are, per atom and per *l*-value (0..3) the upper-triangles of the corresponding density matrices, one after the other, all in cfcset 

``nnuc``
   The number of (non-dummy) nuclei 

``qcore``
   For each atom the number of electrons summed over its core orbitals, resulting from analytical integration of the core orbital expansions in STO core expansion functions. 


Using Data from adf.rkf 
-----------------------

An ASCII dump of adf.rkf (complete or partial) can be obtained with the kf utility dmpkf, see the utilities document. Alternatively you may build your own small program to extract any required information, using the KF library routines in the ADF package. Consult the KFS documentation for a description of this software. 


Representation of functions and frozen cores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

adf uses the cartesian representation for the spherical harmonics part in functions: 

f(x,y,z)=xaybzcrde-ar 

The angular momentum quantum number *l* is then given by *l*\ =a+b+c, and the main quantum number *n* = *l* +d+1. 

There are (*l* + 1)(*l* + 2)/2 different combinations of (a, b, c) for a given *l* - value, rather than (2 *l* +1). The excess is caused by the presence of spurious non-*l* Functions in the set; a Cartesian d-set for instance consists of six functions, five of which are true d-functions while one linear combination is in fact an s-type function (x2+y2+z2). Only the five true d-combinations are actually used as degrees of freedom in the basis set, but lists of primitive basis functions (bas) for instance run over all Cartesian functions including the improper ones. 

A function *set* in ADF is characterized by the quantum numbers *l* and *n*, and by the exponential decay factor a. A set thus represents (*l* +1)(*l* +2)/2 Cartesian functions and (2 *l*\ +1) degrees of freedom. 

The atomic frozen core orbitals are described as expansions in Slater-type functions; these are not the functions of the normal basis set but another set of functions, defined on the data files you use in Create mode. 

Orthogonality of the valence space to the frozen core states is enforced as follows: for each frozen core shell (characterized by the quantum numbers *l* and *n*: all orbitals with *m* = - *l* ... + *l* are identical apart from rotation in space) the set of valence basis functions is augmented with a so-called core orthogonalization function set. You may conceptually interpret the core orthogonalization functions as single zeta expansions of the true frozen core states. Each of the normal valence basis functions is now transformed into a linear combination of that valence function with all core orthogonalization functions, where the coefficients are uniquely defined by the requirement that the resulting function is orthogonal to all true core functions. 

So the list of all Cartesian basis functions is much larger than the degree of freedom of the basis: it contains the spurious *non-l* combinations and it contains also the core orthogonalization functions. 


Evaluation of the charge density and molecular orbitals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

adf.rkf contains all the information you need to evaluate the charge density or a Molecular Orbital (MO) in any point in space. Most of the information is located in section Basis: 

A list of function characteristics (kx,ky,kz,kr,alf), including the core orthogonalization functions. This list does *not* run over *all* bas functions used in the molecule: if a particular function is used on the atoms of a given atomtype, the function occurs only once in the list, but in the molecule it occurs as many times as there are atoms of that type. 

With array nbptr you locate the subsections in the function list that correspond to the different types of atoms: for atom type i the functions nbptr(i)...nbptr(i+1)-1. The distinct atom types are listed in an early section of the standard output file. 

Array nqptr gives the number of atoms for type i: nqptr(i+1)-nqptr(i). With this information you construct the complete list of all functions. Repeat the subsection of type i as many times as there are atoms of that type: the complete list can be considered to be constructed as a double loop, the outer being over the atom types, the inner over the atoms that belong to that type. The total 'overall' list of functions you obtain in this way contains naos functions. Note that in this way we have implicitly also defined a list of all atoms, where all atoms that belong to a particular atom type are contiguous. This list is the so-called 'internal' atom ordering, which may not be identical to the order in which atoms were specified in input, under atoms. 

For a given symmetry representation (Sections S) the array npart gives the indices of the basis functions in the overall list that are used to describe orbitals in this representation. In case of an unrestricted run the array npart applies for either spin: the same basis functions are used; the expansion coefficients for the molecular orbitals are different of course. 

In the symmetry-representation sections Eigen_bas gives the expansion coefficients that describe the MOs. The expansion refer to the functions indicated by npart, and the function characteristics are given by the arrays kx,ky,kz,kr,alf, *and* bnorm, i.e. the expansion is in* normalized*functions. 

The value of an MO is now obtained as a summation of values of primitive basis functions. For the evaluation of any such basis function you have to take into account that its characteristics are defined in the local coordinate system of its atom. 

To obtain the charge density you sum all MOs, squared and multiplied by the respective occupation numbers (array froc in the appropriate irrep section). 

Note that the auxiliary program densf, which is provided with the ADF package, generates orbital and density values on a user-specified grid. See the utilities document. 

