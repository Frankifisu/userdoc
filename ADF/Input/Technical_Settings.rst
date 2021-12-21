
Technical Settings
******************

.. index:: memory usage 

Memory usage
============

The amount of memory used by the program during a calculation is determined by three quantities: 

+ The size of the program itself (executable statements, static arrays). This quantity depends on the program version and is currently around 20 MB.

+ Buffer space used by ADF for more efficient I/O handling. This quantity is set at installation. See the Installation Manual.

+ Dynamically allocated arrays. The program allocates memory dynamically during the run conform the requirements of the actual calculation.

.. index:: shared arrays 

Starting from ADF2010 in case of parallel calculations some of the data arrays that are used  within ADF will be shared by processes on the same node, provided the operating system  allows shared memory. This will reduce the total amount of memory used by all ADF processes  on each node because only one copy of certain large arrays per node will be present.  Note that shared arrays is not the same as distributed arrays.  To disable the use of shared memory one can specify the following keyword: 

.. _keyscheme NOSHAREDARRAYS: 


::

   NoSharedArrays

Direct SCF: recalculation of data
=================================

The program's performance can be defined in terms of the amounts of time (CPU and I/O seconds) and disk space used in a calculation. Also important for the human user is the turn-around time. On multi-user machines CPU-cheap jobs may take a lot of real time to execute due to I/O scheduling.
Therefore ADF recomputes some items, like basis functions and fit functions in the integration points, rather than store them on disk. This will increase the amount of CPU time but reduce disk access and it may also improve the turn-around.

The direct SCF method is default and can not be changed. The keys DISK or DIRECTSCF are therefore obsolete and can not be used.

Vector length
=============

Numerical integration is applied in ADF to evaluate Fock matrix elements and many other quantities that are defined as integrals over basis functions, the charge density, the potential, etc. As a consequence a large part of the CPU time is spent in simple do-loops over the integration points. The total number of points depends on the required precision and on the number of atoms, the geometry and symmetry. All such numerical integration loops are segmented into loops over *blocks* of points, each block consisting of a certain number of points. This latter defines the most inner do-loop and hence determines vectorization aspects. 

Depending on the computer, c.f. the compiler, vector operations may be executed more efficiently using longer vectors. Long vectors increase the demand on Central Memory however because the program may sometimes have to access large numbers of such vectors in combination (for instance all basis functions) so that they must be available in memory simultaneously. The optimum vector length depends therefore on the balance between vectorization efficiency and memory usage. The maximum vector length that you allow the program to use can be set via input. 

.. _keyscheme VECTORLENGTH: 


::

   VECTORLENGTH vectorlength

The default is set at the installation of ADF on your platform, see the Installation manual. For organizational reasons the true vector length actually used in the computation may be smaller than the value defined with this key, but will not exceed it (except in a Create run, but in that case performance and memory usage are no hot topics). 


Tails and old gradients
=======================

The key TAILS is currently obsolescent because of the introduction of the LINEARSCALING block and may be removed in future versions. 

Each block of points (see above) covers (more or less) a certain region in space and can hence be assigned a distance value with respect to a particular atom. These distances are used to control whether or not to evaluate functions centered on that atom in that particular block of points. 

.. _keyscheme TAILS: 


::

   TAILS {bas=tailbas} {fit=tailfit}

``tailbas, tailfit``
   Accuracy levels, similar to the integration parameter: a higher value implies higher precision: in this case, basis functions and fit functions respectively are assumed zero in blocks of points that are at a sufficiently large distance from the atom at which the function is centered. Sufficiently large is defined by comparing the integral of the (radial part of the) function beyond that distance with the total integral. By default tailbas and tailfit both depend on the numerical integration parameter 

Note: in contrast with some of the older versions, supplying only the keyword without parameters does not switch off the use of function cutoffs. To effectively switch off the distance effects in gradients evaluation one should specify large values for the BAS and FIT parameters. The value of 100 should be more than enough, thus, for example: 

::

   TAILS bas=100 fit=100

Improved performance in geometry optimizations and frequency runs is achieved by a new implementation of the calculation of the gradients that now uses linear scaling techniques. 

The key TAILS is not used in geometry optimizations anymore. For controlling the use of distance effects in normal SCF calculations, and for calculations with the RESPONSE or EXCITATIONS keywords, please check the LINEARSCALING block.  

.. _LINEARSCALING: 
.. index:: linear scaling techniques 

Linearscaling
=============

The LINEARSCALING block has a very similar function to the TAILS keyword described above. In addition to defining the precision of operations related to operations in the numerical integration grid, it also defines the precision for the calculation of the overlap matrix, the fit integrals, and the density fit procedure. Default values have been chosen which result in negligible differences in the results for our test calculations, so that these defaults can be considered safe. They have been chosen similarly to the defaults for the TAILS keyword.  

However, it may be advisable to modify the settings for the linear scaling parameters in two cases. First, if a very accurate result is needed, and numerical noise is to be completely eliminated, strict values can be specified. Especially for small molecules, where timings are not so large anyway, this may be of interest. Second, for large molecules, in which the calculations are very time-consuming, one can experiment with less strict values for the LINEARSCALING block keyword. In such a case one should be aware of the reduced accuracy and preferably test the influence of the changes on the results. 

In the simplest application of the LINEARSCALING block, only one parameter is provided. All the subkeys described below will then be given this value. A very large value implies a calculation where no distance cut-offs are used. A normal value (almost default situation) would be 8 for linscal, 6 gives a faster but somewhat sloppier result. Whether this is acceptable is strongly case-dependent. A value of 10 or 12 is already quite strict and, unless there are some sort of numerical problems, there should not be much influence on the results by choosing a stricter value than that. A value of 99 for linscal virtually excludes the possibility that something will be neglected.  

.. _keyscheme LINEARSCALING: 


::

   LINEARSCALING linscal
   End

More refined control is possible by using the full block key 

::

   LINEARSCALING
     CUTOFF_FIT epsfit
     OVERLAP_INT ovint
     PROGCONV progconv
     CUTOFF_COULOMB epsvc
     CUTOFF_MULTIPOLES epsmp
   END

``CUTOFF_FIT``
   determines how many atom pairs are taken into account in the calculation of the fit integrals and the density fit procedure. If the value is too low, charge will not be conserved and the density fitting procedure will become unreliable. This parameter is relevant for the timings of the FITINT and RHOFIH routines of ADF. 

``OVERLAP_INT``
   determines the overlap criterion for pairs of AO's in the calculation of the Fock-matrix in a block of points. Indirectly it determines what the cut-off radii for AO's should be. The value of ovint has a strong influence on the timing for the evaluation of the Fock matrix, which is very important for the overall timings. The default value for ovint is accint + 2 (typically 6). Again, a higher value implies a safer but slower calculation. 

``PROGCONV``
   determines how the overall accuracy changes during the SCF procedure ('progressive convergence'). The idea is that one might get away with a lower accuracy during the initial SCF cycles, as long as the last cycle(s) is/are sufficiently accurate. The current default is that progconv has the value 0, which means that the accuracy in the beginning of the SCF is the same as in the rest of the SCF. This keyword is currently still in the testing phase, so we do not recommend changing its default value. The value of progconv determines how much lower the other parameters in the LINEARSCALING input block are at the beginning of the SCF than at the end. 

``CUTOFF_COULOMB``
   determines the radii for the fit functions in the evaluation of the (short-range part of) the Coulomb potential. As the Coulomb potential may take a sizable amount of time, the value chosen for epsvc may influence the total ADF timing significantly as well. The default value for epsvc is accint + 4 (typically 8). 

``CUTOFF_MULTIPOLES``
   determines the cut-offs in the multipole (long-range) part of the Coulomb potential. This term scales quadratically with system size, but has a small prefactor. In most cases, change in the epsmp value will not affect the CPU time significantly. The default value for epsmp is accint + 4 (typically 8). 


All Points
==========

ADF makes use of symmetry in the numerical integrations. Points are generated for the *irreducible wedge,* a symmetry unique sub region of space. Optionally the symmetry equivalent points are also used. This is achieved by setting the key 

.. _keyscheme ALLPOINTS: 


::

   ALLPOINTS

The key has no argument. The CPU time increases roughly by a factor equal to the number of symmetry operators, and the results should be the same. This key is available only as a debugging feature, to check the correctness of certain symmetry related algorithms. 


Full Fock
=========

At every cycle in the SCF procedure the Fock operator is computed in all integration points. By default the *difference* with the values of the previous cycle are used to compute *changes* in the Fock matrix elements. This leads in general to better computational efficiency in two ways: 1) when all such difference values in a block of integration points are very small such a block is skipped in the calculation. 2) if the values are not negligible but still rather small, the contribution from such a block to matrix elements between basis functions with small overlaps are neglected. 

With the key 

.. _keyscheme FULLFOCK: 


::

   FULLFOCK

this is turned off, so that the complete matrix elements are computed, no blocks are skipped and the neglect of matrix elements between functions with small overlaps (see also the key TAILS) is controlled solely by the function characteristics and precision requirements, not by the development of the SCF. 


Save info
=========

Several types of information, gathered during the run, are lost on exit. The SAVE key allows you to prevent the removal of such information. 

.. _keyscheme SAVE: 


::

   SAVE info

``info``
   A sequence of names separated by blanks or commas. save may occur any number of times in the input file. save turns save-info options on. Possible ``info``:

   TAPE10
      File with numerical integration data: points and weights, values of functions (depends on direct-SCF options) and core densities and potentials.

   TAPE13
      Check point file. This file is lost (by default) only upon normal program exit, i.e. a program-controlled termination (including a program-detected error condition leading to controlled exit). In all such cases all info on TAPE13 is also present on adf.rkf. TAPE13 exists when the program crashes into a core dump for instance, in which case it is uncertain what the contents of adf.rkf will be. The save feature allows you to specify that TAPE13 is kept *also* upon normal exit.

   TAPE14
      Scratch file with numerical integration data, mainly pertaining to individual fragments.

   Timing 
      During
      an ADF calculation the program
      gathers a large amount of timing information about the performance of
      different program parts. It can be printed, at various levels of detail, on
      standard output (key PRINT). It can
      also be stored on adf.rkf, for later inspection, in a section
      Timing."
   
