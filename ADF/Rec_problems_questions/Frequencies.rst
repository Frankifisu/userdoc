
Frequencies
===========

Imaginary Frequencies
---------------------

.. index:: imaginary frequencies 

**Problem**: totally unexpected significant imaginary frequencies are obtained (in a Frequencies run) where you are pretty convinced that all frequencies should be real. 

**Possible cause 1**: problems with the electronic configuration. If there are competing configurations, the electronic *states* in the different displaced geometries may be different, resulting in energies and gradients belonging to different potential energy surfaces to be compared and combined into force constants (frequencies). 

**Check**: orbital occupations and SCF convergence behavior: if the SCFs in the displaced geometries start with large errors and/or converge very slowly you are likely to have stumbled into different configurations, so that the results from the displaced geometries are incompatible. 

**Cure**: This is a difficult situation that may require some experimenting and judicious manipulation of the various SCF options. The bottom line is that you should try anything you can to ensure that all involved geometries have the same electronic configuration. As long as you fail to achieve this, the results are meaningless. 

**Possible cause 2**: flat potential energy surface  (think about almost free rotation modes) coupled with relatively high noise  level in gradients caused by numerical integration errors or not sufficiently converged geometry optimization. 

**Check**: visualize the imaginary frequencies in AMSspectra and  check that their respective normal modes correspond to movements that are expected to  be have (nearly) flat energy profile. 

**Cure** 
: 

+ restart geometry optimization with more strict convergence criteria.  The default criterion on gradients 0.001 Hartree/Angstrom may be not strict enough for  some systems. In such cases a value of 0.0001 is recommended, and for accuracy reasons use "good" numerical quality, and EXACTDENSITY (important for GGA's). 

After the AMSification numerical frequencies or analytical frequencies can be computed immediately after a geometry optimization.
Example input with strict settings using analytical frequencies, and a TZ2P basis set.

::

   $ADFBIN/ams <<eor
      Task GeometryOptimization
      GeometryOptimization
         Convergence gradients=1e-4
      End
      Properties
         NormalModes True
      End
      NormalMode
         Hessian Analytical
      End

      Engine ADF
         NumericalQuality Good
         Basis
           Type TZ2P
           Core None
         End
         ExactDensity
      EndEngine
   eor
      

Geometry-displacement numbers in the logfile are not contiguous
---------------------------------------------------------------

**Problem**: successive displaced geometries in the logfile are numbered, but in your case these numbers make sudden jumps, like '0, 1, 2, 5, 6, 13...' 

**Cause**: you're using Cartesian displacements in a system that has some symmetry in its equilibrium geometry. The program skips the displacements of symmetry-equivalent atomic coordinates to save time. The displacement counts in the logfile do not run over the actually performed displacements but over all atomic coordinates that could be displaced if no use were made of symmetry properties. 

**Cure:** there is no error, don't worry. 

