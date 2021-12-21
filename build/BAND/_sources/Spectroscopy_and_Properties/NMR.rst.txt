.. index:: NMR
.. index:: Shielding Tensor

.. _NMR:

NMR
===

.. warning::
   
   The calculations of NMR shielding with BAND has not been thoroughly tested and the results might be unreliable. One should be extra careful when running NMR calculation, and validate the results by using different super-cells and different technical parameters.


With the NMR option the *shielding tensor* is calculated. There are two methods implemented: the super cell method and the single-dipole method. 

I) The super cell method is according to the implementation by Skachkov *et al.* [#ref1]_ The symmetry will be automatically disabled. The unit cell should not be chosen too small. 

II) The other method is the single-dipole method. In principle one can now use the primitive cell [#ref2]_. In practice also this method needs to be converged with super cell size. However, depending on the system the required super cell may be much smaller. At a given super cell size this method is more expensive than the super cell method. 

.. scmautodoc:: band NMR Enabled SuperCell

This option honors the ``SelectedAtoms`` key, in which case only the NMR properties will be calculated for the selected atoms only. 


.. only:: html

  .. rubric:: References

.. [#ref1] D.\  Skachkov, M. Krykunov, E. Kadantsev, and T. Ziegler,  *The Calculation of NMR Chemical Shifts in Periodic Systems Based on Gauge Including Atomic Orbitals and Density Functional Theory.*  `Journal of Chemical Theory and Computation  6, 1650 (2010) <https://doi.org/10.1021/ct100046a>`__.

.. [#ref2] D.\  Skachkov, M. Krykunov, and T. Ziegler,  *An improved scheme for the calculation of NMR chemical shifts in periodic systems based on gauge including atomic orbitals and density functional theory*,  `Canadian Journal of Chemistry 89, 1150 (2011) <https://doi.org/10.1139/V11-050>`__.
