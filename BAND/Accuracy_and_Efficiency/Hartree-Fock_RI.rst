
.. index:: Resolution of the Identity 
.. index:: Hartree-Fock Exchange

.. _RIHARTREEFOCK:

Hartree–Fock RI
===============

The Hartree-Fock exchange matrix is calculated through a procedure known as Resolution of the Identity (RI). The implementation of the RI scheme in BAND is loosely based on work by Ren *et al.* [#ref1]_. For more information on hybrid functionals in BAND, see the :ref:`XC section <XC>`.

Technical aspects of the RI scheme can be tweaked in the ``RIHartreeFock`` block:

.. scmautodoc:: band RIHartreeFock Quality FitSetQuality DependencyThreshold QualityPerRegion

For efficiency and numerical stability reasons, it is advisable to include::

  SoftConfinement
    Quality Basic
  End

See the :ref:`basis confinement` section for more info.

**Notes:** for periodic systems it is only possible to use short-range hybrid functionals (*e.g.* HSE06) and all-electron basis sets.

.. note::

  * In AMS2019.3 the fit set for ``FitSetQuality Good`` has been improved.

.. only:: html

  .. rubric:: References

.. [#ref1] X.\  Ren, P. Rinke, V. Blum, J. Wieferink, A. Tkatchenko, A. Sanfilippo, K. Reuter and M. Scheffler, *Resolution-of-identity approach to Hartree–Fock, hybrid density functionals, RPA, MP2 and GW with numeric atom-centered orbital basis functions*, `New J. Phys. 14 053020 <https://doi.org/10.1088/1367-2630/14/5/053020>`__.
