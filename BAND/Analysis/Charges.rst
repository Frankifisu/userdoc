.. index:: Atomic Charges
.. index:: Charges
.. index:: Mulliken Analysis
.. index:: Hirshfeld Charges
.. index:: Voronoi Charges (VDD)
.. index:: CM5 (charge model 5)

.. _AtomicCharges:

Charges
=======

Default Atomic Charge Analysis
------------------------------

By default BAND computes the following atomic charge analyses:

* **Hirshfeld Charges** [#ref1]_ [#ref2]_
* **Voronoi Deformation Charges** (VDD, Voronoi Deformation Density)
* **Mulliken Charges** (note: not calculated for :ref:`Spin-Orbit <spin_orbit>` calculations)
* **CM5** (Charge Model 5) [#ref3]_ [#ref4]_

These atomic charges are printed to the output file and can be visualized using the AMSview GUI module.

A more detailed output of the atomic charges can be printed by specifying following print option (note: in Band 2017 and previous versions this detailed output was printed by default)::

  Print AtomicChargesDetails


.. index:: Bader Analysis
.. index:: QTAIM

.. _QTAIM:

Bader Analysis (AIM)
--------------------

The QTAIM (Quantum Theory of Atoms in Molecules), also known as Bader Analysis can be enabled in the GridBasedAIM input block:

.. scmautodoc:: band GridBasedAIM

.. scmautodoc:: band AIMCriticalPoints

.. note::
  
  The Bader (AIM) analysis is performed on the fitted density (see :ref:`ZlmFit <band-key-ZlmFit>`). We advise to use a Good (or better) ZlmFit quality.


.. only:: html

  .. rubric:: References

.. [#ref1] F.L. Hirshfeld, *Bonded-atom fragments for describing molecular charge densities*, `Theoretica Chimica Acta 44, 129 (1977) <https://doi.org/10.1007/BF00549096>`__

.. [#ref2] K.B. Wiberg and P.R. Rablen, *Comparison of atomic charges derived via different procedures*, `Journal of Computational Chemistry 14, 1504 (1993) <https://doi.org/10.1002/jcc.540141213>`__

.. [#ref3] A.V. Marenich, S.V. Jerome, C.J. Cramer, D.G. Truhlar, *Charge Model 5: An Extension of Hirshfeld Population Analysis for the Accurate Description of Molecular Interactions in Gaseous and Condensed Phases*, `Journal of Chemical Theory and Computation 8, 527 (2012) <https://doi.org/10.1021/ct200866d>`__

.. [#ref4] C.A.\  Peeples and G. Schreckenbach, *Implementation of the SM12 Solvation Model into ADF and Comparison with COSMO*, `Journal of Chemical Theory and Computation 12, 4033 (2016) <https://doi.org/10.1021/acs.jctc.6b00410>`__
