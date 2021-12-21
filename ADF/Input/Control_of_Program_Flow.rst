
Control of Program Flow
***********************

Limited execution
=================

.. _keyscheme STOPAFTER: 


::

   STOPAFTER programpart

``programpart``
   Must be a predefined name associated with a (major) part of the program With this key you tell ADF to terminate the job after the named program part has been executed. 

A survey of the recognized names with a brief explanation follows below. The program parts are listed in order of execution: by taking a name further down the list you execute a larger part of the program. 

``init``
   initialization procedure, input reading and printing of the output header with the job identification. 

``input``
   input-reading module. 

``geomet``
   geometry section: organization of atoms in types of atoms and fragments, checks of the actual fragments against information on the attached fragment files. 

``config``
   electronic configuration (if not determined only by the SCF procedure), printout of symmetry subspecies. 

``mainsy``
   generation of symmetry information, representation matrices, etc. 

``symfit``
   construction of symmetry adapted fit functions. 

``cblock``
   generation of integration points and the distribution of them in the blocks that control the internally used segmented vectorization loops. 

``engrad``
   Relevant only in an optimization calculation. Engrad calculates energy gradients. The geometry is not yet updated and no printing of convergence tests and new coordinates is carried out. 

``geopt``
   This routine evaluates energy gradients and updates the geometry accordingly; it also prints the convergence tests and the computed new coordinates. Compare 'stopafter engrad'. 

``forcematrix``
   in a Frequencies run, terminate the calculation when all displacements have been done and before any further processing of the computed Hessian, such as the determination of normal modes, takes place. 


Skipping
========

With the following key you can restrict which parts of the program are actually executed: 

.. _keyscheme SKIP: 


::

   SKIP argumentlist

``argumentlist``
   A sequence of names, separated by blanks or commas. skip may occur any number of times in input. The names in the argument list refer to various items that are associated with parts of the program. With this key you tell ADF to skip the named program part(s) and to continue execution thereafter. The program does not check any consequences and may even crash when variables have not been initialized or have attained incorrect values due to the skipping. 

Use of this key should be contemplated only in debugging and testing sessions, in which you may skip the computation of certain data when before that data will be needed you'll halt the program to inspect something. 

Recognized and operational arguments are for instance (possibly not complete due to frequent extensions in this respect): atpair, ets, fitint, orthon, qmpot 


Ignore checks
=============

ADF performs several checks during a calculation, and stops with an error message when intermediate results are suspicious, when input-specified instructions are incompatible, etc. These controlled aborts can in some cases be overruled. Of course, the checks have been inserted for good reasons and one should realize that ignoring them probably produces incorrect results and/or may lead to a program-crash. 

.. _keyscheme ALLOW: 


::

   ALLOW argumentlist

``argumentlist``
   A sequence of names, separated by blanks or commas. allow may occur any number of times in input, see the list below for the names that can be used. 

``BadCoreInt``
   Numerical integration of the frozen core density should closely approximate the analytical value. If the deviation is large compared to the user-specified numerical integration precision the program aborts with an error message like 'BAD CORE INTEGRAL'. This control is overruled by using this ALLOW option. 

``BadIntegrals``
   Only applicable when the direct-SCF option is turned off for the basis functions. (This happens automatically for ZORA full-potential calculations). In that case, a sequence of elementary overlap integrals are evaluated with the numerical integration grid and the outcomes tested against the analytical value. If the deviation is too large a warning is issued. Above a certain threshold the program will abort, unless you override the exit with this Allow option. 

``BadSCF``
   If the SCF procedure hasn't converged, any geometry manipulations (optimization, linear transit ...) will be aborted because the energy gradients are not reliably computed in a non-self-consistent field. 

``CloseAtoms``
   Atom-atom distances should not be less than 0.2 Bohr. This is checked in the program section where the numerical integration grid is generated. 

``RelGeo``
   Geometry manipulation (optimization, linear transit...) is not supported for all of the relativistic options. See Relativistic 

``SmallBlocks``
   The list of numerical integration points is partitioned in blocks, so as to fit data arrays (for instance values of all basis functions in the points of a block) in available memory. The program computes the maximum block length from available memory and size parameters such as numbers of basis functions. A small block size implies a severe reduction in CPU efficiency. Therefore, the program aborts (by default, to override by this ALLOW option) if the block length turns out to be very small (less than 10). 

``xc``
   Certain combinations of the Density Functional options or application of them with some other features are not allowed. See XC. 

