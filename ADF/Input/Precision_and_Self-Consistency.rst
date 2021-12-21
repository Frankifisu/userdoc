.. index:: precision SCF 

Precision and Self-Consistency
******************************

The precision of a calculation is determined by 

+ The function sets (basis sets, levels of frozen core approximation, and fit sets for the computation of the Coulomb potential)

+ Numerical integration settings in real space

+ The accuracy of the density fitting procedure

+ Convergence criteria (for the SCF procedure and the geometry optimization)

+  A few more items that are rather technical and usually irrelevant (these are not discussed here).

The fragments you attach determine, through the fragment files, the function sets. Since each fragment traces back to one or more Create runs, the employed data base files in the Create runs determine the finally employed function sets. 

In this part we examine numerical integration, density fitting and the SCF procedure. 

.. _keyscheme NUMERICALQUALITY: 

**Numerical Quality**

With the key NUMERICALQUALITY one can set the density fitting quality (ZlmFit) and the numerical integration quality (BeckeGrid) simultaneously 

::

   NUMERICALQUALITY [basic|normal|good|verygood|excellent]


.. toctree::
   :maxdepth: 1

   SCF
   Numerical_integration
   Density_fitting
   Hartree-Fock_RI
   MBPT
   Dependency


