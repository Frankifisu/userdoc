Introduction
############

MOPAC [:ref:`1<reference 1>`] is a general-purpose semiempirical quantum chemistry engine for the study of molecular and periodic structures. A good trade-off between speed and accuracy is achieved through a minimal basis and parameterization against experimental data, with parameters for most elements.

As of the |release| release of the Amsterdam Modeling Suite, MOPAC has become an
`engine <../AMS/Engines.html>`__ in the new `AMS driver setup
<../AMS/General.html>`__. If you have not done so yet, we highly recommend you
to first read the `General section of the AMS Manual <../AMS/General.html>`__.
In practice the inclusion of MOPAC into AMS means that MOPAC can now be used for
many applications that were previously not supported:

* Linear transit and PES scan
* Constrained geometry optimizations
* Molecular dynamics simulations
* Lattice optimization (also under pressure)
* Elastic tensor and related properties (e.g. Bulk modulus)
* Phonon calculations
* ...

Please refer to the `AMS manual <../AMS/index.html>`__ for a complete overview.


What's new in MOPAC 2019
========================

* MOPAC has been fully integrated as an Engine in the Amsterdam Modeling Suite; this significantly speeds up the execution of MOPAC via AMS.
* Parallel binaries.

New input options (also available via the Graphical User Interface):

* Calculation of :ref:`pKa <mopac-key-Properties>`
* :ref:`COSMO <mopac-key-Solvation>`: all solvents available in ADF/Band are now also available in MOPAC.
* :ref:`Static polarizability tensor <mopac-key-Properties>`
* Localized orbitals (Natural Bond Orbitals)
* :ref:`SCF options <mopac-key-SCF>`: Camp-King converger, ...
