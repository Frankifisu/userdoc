.. index:: BerryPhase
.. index:: Dipole Moment

.. _BerryPhase:

Dipole moment and Berry Phase
=============================

By default, Band computes (and prints to the output) only the components of the dipole moment orthogonal to the periodic direction(s).

Since the position operator is ill-defined in periodic systems, computing the longitudinal components of the dipole moment (i.e. the components along periodic directions) is not completely trivial. To obtain the longitudinal components of the dipole moment, you can perform a Berry Phase calculation:

.. scmautodoc:: band BerryPhase

In the graphical user interface (AMSinput) you can find the Berry Phase checkbox in the **Details → Expert BAND** panel.

In a Berry phase calculation, the dipole moment of a unit cell is calculated with the help of the geometric phase within the unit cell. The theoretical framework of the calculations originates from the *'Modern theory of polarization'*  that was come up with in the early 1990s by King-Smith, Vanderbilt and Resta. [#ref1]_ [#ref2]_ The implementation in BAND is a generalization of the one-dimensional Berry phase approach for quantum chemistry codes with local basis sets devised by Kudin and Car. [#ref3]_

.. warning::

   The Berry phase implementation in BAND has been thoroughly for 1D systems. Nonetheless, the implementation seems to break down for 2D and 3D systems, thus requiring careful testing and validation of the calculations for such systems.  

.. warning::

   * Berry phase calculations require orthorhombic unit cells, differently shaped unit cells are not currently supported.
   * For Berry Phase calculations you should use an all :ref:`electron basis set <basis set>` (i.e. Set the ``core`` to ``none``)
   * Using a good k-space sampling is recommended for Berry Phase calculations

An option that can be useful when validating the Berry Phase calculation is ``ShiftCoordinates`` in the AMS System block:

.. scmautodoc:: ams System ShiftCoordinates
    :skipblockdescription:

.. only:: html

  .. rubric:: References

.. [#ref1] R.\  King-Smith, D. Vanderbilt, *Theory of polarization of crystalline solids.* `Physical Review B 47, 1651 (1993) <https://doi.org/10.1103/PhysRevB.47.1651>`__.

.. [#ref2] R.\  Resta, *Macroscopic polarization in crystalline dielectrics: the geometric phase approach.* `Reviews of Modern Physics 66, 899 (1994) <https://doi.org/10.1103/RevModPhys.66.899>`__.

.. [#ref3] K.\  Kuding, R. Car, *Berry phase approach to longitudinal dipole moments of infinite chains in electronic-structure methods with local basis sets* `Journal of Chemical Physics 126, 234101 (2007) <https://doi.org/10.1063/1.2743018>`__.
