.. index:: basis set file format

.. _basis_set_file_format:


Basis set file format
*********************

In ``$AMSHOME/atomicdata/ADF`` you can find standard basis sets (including fit sets and frozen core orbitals) for all chemical elements of the periodic table at different levels of accuracy. 
The database is partitioned in subdirectories. Some of these are special: for example, the subdirectory Dirac contains input files for the program *dirac* (computation of relativistic potentials and charge densities). 
Most subdirectories contain files for the create runs: for example, the subdirectories SZ through TZ2P.  
:ref:`The section about the STO basis sets<STO basis sets>` describes all subdirectories in more details. 

The names of the basis set files consist of two parts: the standard symbol for the chemical element and the level of frozen core approximation; e.g. Mn.2p is a basis set file for Manganese with a frozen core up to and including the 2p shell. 

Many all-electron basis can be found in the data base, especially for the elements H-Kr. All electron basis sets for the heavier elements can be found in the ZORA subdirectory. Fit functions for the all-electron basis sets must include more, in particular more contracted functions than the standard fit sets that are provided in the frozen core basis set files. If you would combine a basis set with an inadequate fit set the results are unreliable and absolutely inadequate, in the same fashion as when you would have used a highly inadequate basis set. 


Sections
========

The basis set file supplied to ADF in Create mode contains the following sections: 

::

   Title
   Basis Functions
   Core Expansion Functions
   Core Description
   Fit Functions

Each of these items is discussed below. The basis set file does *not* define the applied density functional, the electronic configuration, precision parameters (numerical integration, SCF convergence criterion...), etc etc. These items can be set in the normal input file if the default is not satisfactory. 


Title
  The title is the first record of the file. It may contain any text. 
  Only the first 60 characters are actually used. This title is (by default) printed in the output; it is also used to stamp an identification on the result file (adf.rkf). 
  The file stamp will be printed whenever you use it as a fragment file in another calculation. 


Basis functions
  A list of Slater type basis function characteristics. This part has the following format (example): 

  ::

     BASIS
       1s 5.4
       2s 1.24
       ...
       (etc.)
       ...
     end

  The words basis and end signal the beginning and the end of this section in the data file. The records in-between list the basis functions; each record contains the main quantum number, the angular quantum number, and the exponential decay factor for a *set* of Slater type basis functions.

  The order of specification of the basis functions is not free. First must come the Core Functions used for core-orthogonalization. The CFs must be in order: s-functions first, then p-functions, then d-functions, and finally f-functions (as far as applicable). In the valence basis set there must be exactly one core-orthogonalization function for each frozen core shell (1s, 2s, 2p, ...). 

  Here as well as in all other function definitions below, the unit of length, implicit in the exponential decay factor, is bohr (atomic units), irrespective of the unit of length used in input for geometric items such as atomic positions (see units). 


Core expansion functions
  This part has the form 

  ::

     CORE ns, np, nd, nf
       1s 7.68
       ...
       (etc.)
       ...
     end

  It looks very much like the *basis functions*: a list of Slater type function descriptions, closed by end. The header record however (core...) contains in addition four integers ns, np, nd, nf. They are the numbers respectively of s-, p-, d-, and f- frozen core shells in the atom. If you create for instance a Ruthenium atom with a frozen core up to the 4p shell, these numbers would be ``4 3 1 0`` : four frozen s-shells (1s,2s,3s,4s), three frozen p-shells (2p,3p,4p), one frozen d-shell (3d), and no frozen f-shells. 

  The core expansion sets defined in this section are used to describe the frozen core orbitals; they are not included in the valence basis set. In the list of core expansion sets all s-type functions must come first, then the p-type functions, then the d-functions, and then the f-functions (as far as applicable). 


Core description
  Describes the frozen core shells as linear combinations of the core expansion functions. This section has the form 

  ::

     COREDESCRIPTION
       coefficients for the first frozen s-shell
       for the second s-shell
       for the n-th shell
       coefficients for the first frozen p-shell
       for the second p-shell
       for the d-shells
       for the f-shells
       pseudopotential parameters
     end

  For each of the angular momentum quantum numbers *l=s, p, d, f* all n *l* frozen shells are described by giving expansion coefficients. There are as many coefficients as there are function *sets* with the pertaining *l* value in the list of expansion functions. There are no separate coefficients for all *m* values: all *m* values are equivalent in a spherically symmetric model atom. See the Ca example below. 

  At the end of the (core) description section there is a record with pseudopotential parameters. The pseudopotential option, as an alternative to the frozen core approximation, is currently not supported, all values in this record must be zero, one for each frozen core shell. Equivalently you can put one zero, followed by a slash (/). 


Fit functions
  is again a list of Slater type functions. These are used for an expansion of the density. The Coulomb potential due to the electronic charge distribution is computed from this expansion. 

  The format of this section is similar to the *basis functions*: 

  ::

     FIT
       1s 10.8
       ...
       (etc.)
       ...
     end

  The program cannot handle fit functions with *l*\ -value higher than 4, i.e. not higher than *g*-type functions. Bear this in mind if you construct alternative fit sets. 


Example of a basis set file: Calcium
====================================

An example may serve to illustrate the format of a Create data file for DZ/Ca.2p (empty records inside and between the various sections are meaningless and ignored): 

::

  Calcium (DZ, 2p frozen)
   
  BASIS
   1S  15.8
   2S   6.9
   2P   8.1
   
   3S   2.6
   3S   3.9
   3P   2.1
   3P   3.4
   4S   0.8
   4S   1.35
   4P   1.06
   
   3D   2.000
  END
   
  CORE    2  1  0  0
   1S  24.40
   1S  18.25
   2S   7.40
   2S   4.85
   3S   4.00
   3S   2.55
   4S   0.70
   4S   1.05
   4S   1.65
   2P  10.85
   2P   6.45
   3P   1.85
   3P   2.70
   3P   4.00
  END
  
  DESCRIPTION
    0.2076143E+00  0.7975138E+00 -0.7426673E-04  0.1302616E-03 -0.6095738E-04
    0.1508446E-04  0.1549420E-06 -0.2503155E-07 -0.1843317E-05
    0.8487466E-01 -0.4505954E+00  0.1009184E+01  0.9627952E-01 -0.3093986E-01
    0.1678301E-01 -0.2381843E-02  0.6270439E-02 -0.8899688E-02
    0.3454503E+00  0.6922138E+00 -0.1610756E-02  0.5640782E-02 -0.5674517E-02
   
  0/
  END
   
  FIT
   1S  31.80
   2S  29.37
   3S  25.15
   4S  21.06
   4S  13.99
   5S  11.64
   5S   8.05
   6S   6.69
   6S   4.76
   6S   3.39
   7S   2.82
   7S   2.06
   7S   1.50
   2P  24.10
   3P  14.78
   4P   9.29
   5P   5.98
   6P   3.94
   6P   2.24
   7P   1.50
   3D  16.20
   4D  10.47
   5D   6.91
   6D   4.65
   6D   2.70
   7D   1.85
   4F   7.00
   5F   4.00
   5G   3.50
  END


Extending a basis set
=====================

Polarization functions are provided for most elements. We strongly recommend to use one of the default basis sets described :ref:`here<STO basis sets>`. 

If you are considering making your own basis set by including one or more polarization functions, a good rule of thumb to choose the function characteristics is the following: take the next higher *l*-value that does not yet occur in the function set (however, do not go beyond *f*-functions: the program cannot (yet) handle *g*-type basis functions), select the minimum value for the main quantum number :math:`n` that is compatible with the *l*-value (i.e.: 2p, 3d, 4f), and determine the exponential decay factor :math:`\zeta`, such that the function attains its maximum value at somewhere between 1/3 and 1/2 times the bond length. 
The functional maximum for a Slater-type function is at :math:`R = (n-1) / \zeta`. The maximum for :math:`r^2` times the square of a Slater-type function is at :math:`R = n / \zeta`. 

