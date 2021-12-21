Relativistic Effects and Spin
=============================

.. index:: Unrestricted calculation

Spin polarization
-----------------

By default Band calculations are spin-restricted. You can instruct Band to perform a  spin-unrestricted via the ``Unrestricted`` key:

.. scmautodoc:: band Unrestricted

The orbitals are occupied according to the aufbau principle. 

If you want to enforce a specific spin-polarization (instead of occupying according to the aufbau principle) you can use the ``EnforcedSpinPolarization`` key:

.. scmautodoc:: band EnforcedSpinPolarization


.. index:: ZORA
.. index:: Relativistic Effects
.. index:: Spin-orbit

.. _spin_orbit:
.. _relativistic_effects:

Relativistic Effects
--------------------

Relativistic effects are treated with the accurate and efficient ZORA approach [#ref1]_ [#ref2]_, controlled by the ``Relativity`` keyword. Relativistic effects are negligible for light atoms, but grow to dramatic changes for heavy elements. A rule of thumb is: Relativistic effects are quite small for elements of row 4, but very large for row 6 elements (and later). 

.. scmautodoc:: band Relativity

See also the :ref:`SpinOrbitMagnetization <SpinOrbitMagnetization>` key.

.. only:: html

  .. rubric:: References

.. [#ref1] P.H.T. Philipsen, E. van Lenthe, J.G. Snijders and E.J. Baerends,  *Relativistic calculations on the adsorption of CO on the (111) surfaces of Ni, Pd, and Pt within the zeroth-order regular approximation.*  `Physical Review B 56, 13556 (1997) <https://doi.org/10.1103/PhysRevB.56.13556>`__.

.. [#ref2] P.H.T. Philipsen, and E.J. Baerends,  *Relativistic calculations to assess the ability of the generalized gradient approximation to reproduce trends in cohesive properties of solids.*  `Physical Review B 61, 1773 (2000) <https://doi.org/10.1103/PhysRevB.61.1773>`__.
