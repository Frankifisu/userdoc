.. index:: Numerical Integration

.. _numerical_integration:

Numerical Integration
=====================

Many of the integrals needed by Band are computed via numerical integration. See also: `Wikipedia page on Numerical Integration <https://en.wikipedia.org/wiki/Numerical_integration>`_.

.. index:: Becke Grid

Becke Grid
----------

The numerical integration grid is a refined version of the fuzzy cells integration scheme developed by Becke [#ref1]_. The implementation in BAND is described in Ref. [#ref2]_. 

The quality of the Becke integration grid can be changed within the ``BeckeGrid`` block:

.. scmautodoc:: band BeckeGrid Quality RadialGridBoost QualityPerRegion

:ref:`example Multiresolution_H2O` illustrates how to use the ``QualityPerRegion`` option.

**Notes:**

+ The space-partition function used in BAND differs from the one described in Ref. [#ref2]_. The unnormalized partition function used in the program is defined as (:math:`\Omega_I` is an element-dependent parameter: 0.1 Bohr for H, 0.3 Bohr for He-Xe and 0.6 Bohr for Cs-Ubn): 

.. math::

  \mathcal{P}_{i,U} = \begin{cases}
                        1 & \text{if  $r_{i,U}<\Omega_I$} \\
                        0 & \text{if  $\exists j : r_{j,U}<\Omega_J$ } \\
                        \eta_i \frac{e^{-2 (r_{i,U}-\Omega_I) / a_0}}{(r_{i,U}-\Omega_I)^2} &  \text{elsewhere}               
                \end{cases}
    

+  The Becke grid is not very well suited to calculate Voronoi deformation density (VDD) charges. For accurate calculation of VDD charges the Voronoi integration scheme is recommended.

.. index:: Radial Grid

Radial grid of NAOs
-------------------

.. scmautodoc:: band RadialDefaults


.. index:: Voronoi Grid

Voronoi grid (deprecated)
-------------------------

It is possible to use an alternative numerical integration scheme to the Becke Grid, namely the Voronoi Grid.


.. scmautodoc:: band IntegrationMethod 

The options for the Voronoi Grid are specified in the ``Integration`` block:

.. scmautodoc:: band Integration

.. only:: html

  .. rubric:: References

.. [#ref1] A.D. Becke, *A multicenter numerical integration scheme for polyatomic molecules*,  `Journal of Chemical Physics 88, 2547 (1988) <https://doi.org/10.1063/1.454033>`__.

.. [#ref2] M.\  Franchini, P.H.T. Philipsen, L. Visscher, *The Becke Fuzzy Cells Integration Scheme in the Amsterdam Density Functional Program Suite*,  `Journal of Computational Chemistry 34, 1818 (2013) <https://doi.org/10.1002/jcc.23323>`__.
