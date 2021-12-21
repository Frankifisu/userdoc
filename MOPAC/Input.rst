Input keywords
##############

This manual documents the input for the MOPAC `engine <../AMS/Engines.html>`__
used together with the AMS driver. If you are not yet familiar with the AMS
driver setup, we highly recommend reading the `introductory section in the AMS
manual <../AMS/General.html>`__.

The MOPAC engine is selected and configured in the AMS input with

.. code-block:: none

   Engine MOPAC
      ... keywords documented in this manual ...
   EndEngine

This page documents all keywords of the MOPAC engine input, basically the
contents of the ``Engine MOPAC`` block in the AMS input file.

General remarks on the input syntax can be found in the `AMS manual <../AMS/Input_Output.html>`__.

.. seealso::

   The :ref:`examples` section of this manual contains several example calculations

Model Hamiltonian
=================

The most important keyword in the MOPAC engine input is the model selection:

.. scmautodoc:: mopac Model
   :nosummary:

The default PM7 model [:ref:`2<reference 2>`] is the latest parametrization for
MOPAC and should be the most accurate for most calculations.

.. scmautodoc:: mopac Sparkles
   :nosummary:

.. scmautodoc:: mopac UnpairedElectrons
   :nosummary:

Solvation
=========

Solvation effects can be included via the COSMO model.

.. scmautodoc:: mopac Solvation
  :collapselongchoicesinsummary:


Properties
==========

.. scmautodoc:: mopac Properties

The calculation of Natural Bond Orbitals can be requested with the following keyword:

.. scmautodoc:: mopac CalcLocalOrbitals

The calculation of bond orders can be requested in the `AMS Properties block <../AMS/Properties.html>`__. 

Technical settings
==================

.. scmautodoc:: mopac SCF

With the MOZYME method the standard SCF procedure is replaced with a localized molecular orbital (LMO) method. This can speed-up the calculation of large molecules. Although a job that uses the MOZYME technique should give results that are the same as conventional SCF calculations, in practice there are differences.  Most of these differences are small, but in some jobs the differences between MOZYME and conventional SCF calculations can be significant. Use with care.

.. scmautodoc:: mopac Mozyme
   :nosummary:


Extra keywords
==============

Finally it is possible to pass any other keywords directly to the MOPAC program
[:ref:`1<reference 1>`]. The full list of keywords can be found on the
`standalone MOPAC manual <http://openmopac.net/manual/index.html>`__.

.. scmautodoc:: mopac Keywords

These keywords are just literally passed through to MOPAC program which the AMS
MOPAC engine wraps, without any checking in AMS. One should therefore be very
careful with this, as it is very easy to set up completely non-sensical
calculations in this way. 

**Note:** The following keywords have been either removed or renamed in our version of MOPAC and they should not be used in the ``Keywords`` key: 0SCF, 1SCF, A0, ADD, AIDER, AIGIN, AIGOUT, ALT_A, ALT_R, ANGSTROMS, AUTOSYM, BANANA, BAR, BCC, BFGS, BIGCYCLES, BIRADICAL, CHAINS, COMPARE, CVB, DDMAX, DDMIN, DFORCE, DFP, DMAX, DRC, ECHO, EF, FLEPO, FORCE, FREQCY, GNORM, H, HTML, INT, IONIZE, IRC, ISOTOPE, KINETIC, LBFGS, LET, LOCATE, MODE, NOCOMMENTS, NOOPT, NORESEQ, NOSWAP, NOTER, NOTHIEL, NOTXT, OPT, P, PDB, PDBOUT, POINT, POINT1, POINT2, RABBIT, RECALC, RMAX, RMIN, SIGMA, SLOG, SMOOTH, SNAP, START_RES, STEP, STEP1, STEP2, SYBYL, T, THERMO, THREADS, TIMES, TRANS, TS, VELOCITY, X, XENO, XYZ,, AM1, LOCAL, BONDS, CHARGE, UHF, CAMP, KING, ITRY, EPS, FIELD, pKa, STATIC, CYCLES, PRESSURE, SPARKLE.
