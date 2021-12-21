
.. index:: Density Fitting
.. index:: ZlmFit

Density Fitting
===============

The Coulomb potential in Band is computed using a method called density fitting. The density fitting scheme in BAND is called **Zlm Fit**, and it is described in reference [#ref1]_. The ZlmFit is also used to compute (when needed) the gradient and hessian of the electron density. 

Zlm Fit
-------

The idea behind Zlm Fit can be summarized as follows: the total electron density is split into localized atomic densities (in a similar way as the volume is partitioned in the Becke grid). These atomic densities are then approximated by a combination of radial spline functions and real spherical harmonics (Zlm), for which the Coulomb potential can be easily computed.

.. scmautodoc:: band ZlmFit Quality QualityPerRegion

:ref:`example Multiresolution_H2O` illustrates how to use the ``QualityPerRegion`` option.

Expert options
^^^^^^^^^^^^^^

.. scmautodoc:: band ZlmFit LMargin AllowBoost DensityThreshold PartitionFunThreshold FGaussianW FGridSpacing FKSpaceCutOff FirstTopoCell LastTopoCell OrderTopoTrick NumStarsPartitionFun
   :noref:

.. _STO fit:

STO Fit (Deprecated)
--------------------

In previous version of BAND (pre2014) this was the default option, which is now replaced by Zlm Fit. It is still used in the context of ``NMR`` and ``OldResponse`` calculations.



.. only:: html

  .. rubric:: References

.. [#ref1] M.\  Franchini, P.H.T. Philipsen, E. van Lenthe, L. Visscher, *Accurate Coulomb Potentials for Periodic and Molecular Systems through Density Fitting*,  `Journal of Chemical Theory and Computation 10, 1994 (2014) <https://doi.org/10.1021/ct500172n>`__.
