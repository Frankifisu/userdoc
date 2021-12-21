.. index:: MBPT

.. _MBPT:

MBPT scheme
-----------

.. note::
  This page describes technical aspects of the MBPT (Many-Body Perturbation Theory) module which is used in double-hybrid and MP2, RPA and GW calculations. In order to use double-hybrids, MP2 or RPA in your calculation you should request it in the :ref:`XC input block <keyscheme XC>`. In order to perform a GW calculation, you should request it in the :ref:`GW input block <keyscheme GW>`.

ADF implements RPA, GW, and SOS-MP2 (spin-opposite-scaled) using a newly designed algorithm which in all cases scales quadratically with system size [#ref1]_ [#ref3]_. Full MP2 is at the moment only implemented using the canonical RI-algorithm which scales to the fifth power with system size. Thus, we strongly discourage using full MP2 or double-hybrids employing full MP2 for system larger than 1000-1500 basis functions. At the moment ADF features a large number of double-hybrids using SOS-MP2 only (For a list of implemented functionals see :ref:`XC input block <keyscheme XC>`) which are significantly faster than conventional double-hybrids while offering the same level of accuracy [#ref2]_. 

GW, MP2, RPA and double-hybrid functionals can be used icw scalar relativistic effects within the ``ZORA``, ``X2C``, or ``RA-X2C`` formalism.
In ADF2022 and later MP2 and double-hybrid functionals can be used icw spin-orbit coupling. Note that in case of spin-orbit coupling approximate SS and OS contributions are calculated.
GW and RPA can not be used icw spin-orbit coupling.
In ADF2022 in case of ZORA by default the so called scaled ZORA orbital energies are used in the MBPT expressions.

The Formalism used in the double-hybrid calculation can be changed using the Formalism key. By default, ADF selects the most appropriate algorithm for your system and functional.

The calculation of the independent-particle polarizability or Kohn-Sham density response function in imaginary time is the key step in SOS-MP2, RPA and |G0W0|. The equations are solved in the atomic orbital basis exploiting sparsity via advanced density fitting techniques (so-called pair-atomic resolution of the identity or pair-atomic density fitting) [#ref1]_. In case of a SOS-MP2 or RPA calculation, the polarizability is than contracted with the Coulomb potential. For SOS-MP2, the correlation energy is then immediately evaluated in imaginary time while in a RPA calculation the product of Coulomb potential and polarizability is Fourier transformed to the imaginary frequency axis where the correlation energy is evaluated using a matrix logarithm. In a |G0W0| calculation, the polarizability is Fourier transformed to the imaginary frequency axis as well where the so-called screened interaction is calculated. The QP states are then evaluated along the real-frequency axis using analytical continuation techniques. 

Recommended numerical settings
++++++++++++++++++++++++++++++

For all calculations using the MBPT scheme (which includes GW, RPA, MP2, and double hybrids), we recommend to consider the following points:

**Dependency**


In ADF2022 a similar method was implemented as was used in the RIHARTREEFOCK scheme to improve stability of the results with the subkey DEPENDENCY of the key MBPT:

.. scmautodoc:: adf MBPT Dependency
   :noref:
   :skipblockdescription:

In addition one may remove linear dependencies in the basis set, by using the ``Dependency`` key. For example

::

  DEPENDENCY
     BAS 5e-04
  END


| **Augmented basis sets:** Set the dependency key to values between 1e-3 and 5e-3
| **Non-augmented basis sets:** Set the dependency key to values between 5e-4 and 5e-3
| **quasiparticle selfconsistent GW:** A value of 5e-3 is usually a good choice

**Numerical Quality**

| **Augmented basis sets:** Numerical quality should be ``VeryGood``
| **Non-augmented basis sets, TZ:** Numerical quality should range from ``Normal`` to  ``VeryGood``
| **Non-augmented basis sets, QZ:** Numerical quality should range from ``Good`` to  ``VeryGood``

There is also the option to choose a different numerical quality for the MBPT and the preceding DFT calculation: 

::

  MBPT
     NumericalQuality Good
  END

sets the numerical quality to Good only for the MBPT calculation. More info can be found in the :ref:`MBPT input block <keyscheme MBPT>` section.

**The sizes of the imaginary time and imaginary frequency grids** can be controlled with the ``nTime`` and ``nFrequency`` keys. For example:           

::

  MBPT
     nTime 32
     nFrequency 32
  END

In case of SOS-MP2, ``nFrequency`` is ignored. For SOS-MP2, the default is 9 points. The numerical quality automatically sets the number of grid points for imaginary time and frequency integration in case of a GW or RPA calculation:

.. csv-table:: 
   :widths: 100,100

  **"Numerical quality"**, **"Number of points"**
  VERYBASIC ,  8
  BASIC     , 12
  NORMAL    , 16
  GOOD      , 20
  VERYGOOD  , 24
  EXCELLENT , 32

For a MP2 or double hybrid calculation, see default is always 9 points, independently of the numerical quality. Note, that the requirements for this parameter are in general lower than for a GW or RPA calculation. 


**Note** the following: The number of points actually used in a calculation can differ. At runtime, the MBPT algorithm decides what is the maximum number of integration points which is reasonable to use. So the actual number of points which has been used will be equal or smaller. In case the number of points is set by hand, some info is printed in the output. In case of a GW calculation, the numbers of points can also be found in adf.log file in the ``GW`` section under the names ``nTime`` and ``nFrequency``.

**Changing the defaults** can be necessary in case your system contains 4th row elements or heavier and/or your basis set is very large and/or your system has a very small HOMO-LUMO gap. For a GW calculation, 24 points should be sufficient for 5th row elements. 32 points might be required for 6th row elements. The maximum number of points which can be used is 42. For a MP2 calculation, 16 points will usually be sufficient if your systems contains 4th row elements, and 20 points will usually suffice in case of 5th row elements. Note, that also a very small HOMO-LUMO.


.. _keyscheme MBPT: 

.. scmautodoc:: adf MBPT Formalism nTime nFrequency FitSetQuality IntegrationQuality ThresholdQuality Dependency UseScaledZORA

.. only:: html

  .. rubric:: References

.. [#ref1] A.\  Förster, M. Franchini, E. van Lenthe, L. Visscher, *A Quadratic Pair Atomic Resolution of the Identity Based SOS-AO-MP2 Algorithm Using Slater Type Orbitals*, `Journal of Chemical Theory and Computation 16 875-891 (2020) <https://doi.org/10.1021/acs.jctc.9b00854>`__ 

.. [#ref2] A.\  Förster, L. Visscher, *Double hybrid DFT calculations with Slater type orbitals*, `Journal of Computational Chemistry 41 1660-1684 (2020) <https://doi.org/10.1002/jcc.26209>`__

.. [#ref3] A.\  Förster, L. Visscher, *Low-order scaling |G0W0| by pair atomic density fitting*, `Journal of Chemical Theory and Computation 16 (12), 7381 (2020) <https://doi.org/10.1021/acs.jctc.0c00693>`__ 

.. |G0W0| replace:: G\ :sub:`0`\ W\ :sub:`0`
