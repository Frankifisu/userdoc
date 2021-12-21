.. _density_fitting:

Density fitting
===============

**Zlm Fit: density fitting with radial spline functions and real spherical harmonics**

.. _ZLMFIT:

Note: In ADF2013 and previous versions, a different density-fitting scheme (pair-fit) was used. Include the key ``STOFIT`` if you want to use the old fitting scheme.

The basic ideas behind the so-called Zlm Fit can be described as follows. The total electron-density is split into atomic densities (in a similar way as the volume is partitioned for the Becke grid). These atomic densities are then approximated by a combination of radial spline functions and real spherical harmonics (Zlm). The implementation in ADF is described in Ref. [#ref2]_. The algorithm that is used in ADF is related to the procedures proposed by Becke [#ref3]_ and Delley [#ref1]_).

The Zlm Fit scheme (which is the default fitting scheme in ADF2016) offers certain advantages compared to the old pair-fit method, especially the possibility to calculate the Coulomb potential to very high precision.

.. _keyscheme ZLMFIT:

::

   ZLMFIT
    Quality {basic|normal|good|verygood|excellent}
    {QualityPerRegion
       Region myregion
       Quality {Basic|Normal|Good|VeryGood|Excellent}
    End}
   End

``Quality``
   The default quality of the Zlm Fit is normal. It can be changed with the subkey Quality.

``QualityPerRegion``
   One can overwrite the Zlm Fit quality for atoms in a particular region. :ref:`example Multiresolution_H2O` illustrates how to use this option.

The Zlm Fit method can be used for most features of the ADF program.
For the calculation of Hartree-Fock exchange integrals, ADF uses a different fitting method, see :ref:`the section on Hartree-Fock exchange<hartree-fock_RI>`.

**Pair fit: symmetric density fit**

.. _DENSITYFIT:

.. index:: density fitting

The non-default density fitting procedure in ADF, called pair fit method, is carried out separately for each pair of atoms. To use it one needs to include the keyword STOFIT.

::

   STOFIT

The implemented approach has several advantages in efficiency but it has a drawback in that it necessitates the use of all available fit functions rather than only the symmetric combinations although the final result of course needs only a symmetric fit because the total density is a symmetric (A1) function. For atoms far apart the density fitting is performed with only symmetric functions. Given the implemented algorithm this entails an approximation which can be tuned:

.. _keyscheme A1FIT:


::

   A1FIT atomicseparation

``atomicseparation``
   is the threshold distance between atoms, *in Angstrom*. The symmetric fit approximation is applied only for atoms farther apart. Default is 10.0 Angstrom

.. _keyscheme STOFIT:


**Pair fit: fit integrals**

::

   STOFIT

For the computation of the Coulomb potential with the pair fit method the program uses a large number of so-called *fit integrals*: the overlap integrals of a fit function with a *product* of two basis functions, where at least two of the involved three functions are centered on the same atom. In fact these are ordinary overlap integrals of STOs because the fit and basis functions are all STOs and a product of STOs on a center is itself also an STO. To use this STO fitting method, which was previously the default, use the key STOFIT in the input of adf (also include it in the create mode of an atom, if that is explicitly used).  For the bond energy a first order fit correction term is included, which makes the bond energy accurate to first order in the fit.

Obviously, when the two involved atoms are far enough apart, such overlap integrals become negligibly small. All fit integrals are ignored (and not computed) that are smaller - according to a rough but reasonable estimate - than a preset threshold.

The value of this threshold can be set via input, using the subkey CUTOFF_FIT of the  :ref:`LINEARSCALING<keyscheme LINEARSCALING>` block key word.

**True density in XC potential**

For the computation of the exchange-correlation potential (XC-potential) the program uses as default the fitted density. This is an approximation. For the XC potential the true density can be used if one includes the keyword EXACTDENSITY:

.. _keyscheme EXACTDENSITY:


::

   EXACTDENSITY

Using the EXACTDENSITY keyword makes the calculation more time-consuming but  more accurate in the following cases:

+ calculations that require accurate description of virtual orbitals, such as most of the TDDFT;

+ when studying systems where weak interaction, such Van der Waals forces and hydrogen bonds, are important.  For example, EXACTDENSITY should be switched on when performing geometry optimization of DNA pairs.


**Precision of density fitting on standard Output**

In the output file of the ADF calculation one can find at the end of the SCF concise information about the density-fit precision: the error integral for the SCF density.
The error integral is the integral of the difference between the exact density and the fit density, squared.
Such values have very little to do with numerical integration, rather they show whether or not the employed set of fit functions are adequate to describe the SCF density.
Error integral values that significantly exceed 1e-4 times the number of atoms are suspicious and may indicate some deficiency in the fit set for the actual calculation.
On the last geometry (in an optimization) the fit-error integrals are also printed for the initial (sum-of-fragments) density and the orthogonalized fragments.
In the bond energy analysis a 1st-order fit-correction term is given.

.. only:: html

  .. rubric:: References

.. [#ref1] B.\  Delley, *An all-electron numerical method for solving the local density functional for polyatomic molecules*, `Journal of Chemical Physics 92, 508 (1992) <https://doi.org/10.1063/1.458452>`__

.. [#ref2] M.\  Franchini, P.H.T. Philipsen, E. van Lenthe, L. Visscher, *Accurate Coulomb Potentials for Periodic and Molecular Systems through Density Fitting*, `Journal of Chemical Theory and Computation 10, 1994 (2014) <https://doi.org/10.1021/ct500172n>`__

.. [#ref3] A.D. Becke, R.M. Dickson, *Numerical solution of Poisson's equation in polyatomic molecules*, `Journal of Chemical Physics 89, 2993 (1988) <https://doi.org/10.1063/1.455005>`__
