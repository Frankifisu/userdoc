What's new in ADF 2022.1
************************

New features
============

* Model Hamiltonians

  + :ref:`QM/FQ Quantum Mechanics/Fluctuating Charges <FQQM>`

    - extended to fluctuating dipoles (QM/FQFμ) 
    - can be combined with Frozen Density Embedding (FDE)

  + :ref:`3D-RISM <3D-RISM>` revised implementation and additional functionality
  + :ref:`IQA Interacting Quantum Atoms <IQA>`

    - intra-atomic terms
    - parallelization

  + :ref:`MP2<MP2>` and :ref:`double hybrid<DoubleHybrid>` in combination with spin-orbit coupling

    - in case of spin-orbit coupling approximate SS and OS contributions

* :ref:`Many-Body Perturbation Theory<MBPT>`

  + :ref:`quasiparticle self-consistent GW: qsGW<GWscheme>`
  + :ref:`second-order self-energy GW: G3W2<GWscheme>`
  + improvements in stability of the MBPT results especially for larger basis sets

* New |AMS| features can be used in combination with ADF

  + `what's new in the AMS driver <../../AMS/General.html#what-s-new-in-the-ams-driver>`__
  + `FCF module <../../AMS/Utilities/FCF_module.html#fcf-module-franck-condon-factors>`__ for the calculation of vibronic progressions and bandshapes improved

What's new in ADF 2021.1
************************


New features
============

* Model Hamiltonians

  + :ref:`QM/FQ Quantum Mechanics/Fluctuating Charges <FQQM>`
  + :ref:`r2SCAN-D4 <LIBXC>` XC functional

* :ref:`Many-Body Perturbation Theory<MBPT>`

  + :ref:`eigenvalue-only self-consistent GW: evGW<GWscheme>`
  + :ref:`Basis sets<STO basis sets>` for use in :ref:`MBPT<MBPT>`

    - Corr/TZ3P
    - Corr/QZ6P

* Spectroscopy

  + :ref:`LFDFT ESR (EPR) g-tensor doublets <LFDFT_gtensor>`
  + :ref:`LFDFT MCD <LFDFT_MCD>`
  + :ref:`POLTDDFT: reduced fit sets for most elements for DZ, DZP, TZP basis sets<POLTDDFT>`
  + :ref:`unrelaxed dipole moment excited states<UV_VIS>`
  + :ref:`transition dipole moment between excited states<ESESTDM>`


* New |AMS| features can be used in combination with ADF. See the page `What's new in the AMS driver <../../AMS/General.html#what-s-new-in-the-ams-driver>`__  for more details.

New Defaults
============

* :ref:`Perturbative inclusion of spin-orbit coupling for excitation energies <excitations SOPERT>`

  + singlet ground state is included by default, keyword GSCORR now subkey of SOPERT
  + improved way to calculated transition dipole moment


ADF is an AMS Engine
********************

Starting from AMS2020 ADF is only accessible via the AMS driver program.
The standalone program 'adf' does not exist anymore.
The job of the AMS driver is to handle all changes in the geometry, e.g. during a geometry optimization, using so-called engines like ADF for the calculation of energies and forces.

.. important::

   In the AMS2020 release ADF is an AMS engine.
   We recommend you to first read the `General section of the AMS Manual <../../AMS/General.html>`__

If you use ADF exclusively via the Graphical User Interface (GUI), this change should not create any issues.
If, on the other hand, you create input files by hand (or you use ADF via `PLAMS <../../plams/index.html>`__),
then you should be aware that shell scripts for ADF2019 and previous versions
are not compatible with ADF2020 and have to be adjusted to the new setup (see also :ref:`automatic_conversion`).

Some of the changes:

* environment variables AMSHOME, AMSBIN (instead of ADFHOME, ADFBIN)
* ams (instead of adf)
* major restructuring of input and input keys
* output files in separate directory
* ams.rkf new binary output file, contains mainly geometry related data
* adf.rkf binary output file (instead of TAPE21), contains mainly single point related data
* AMS does not symmetrize coordinates by default, which ADF used to do. See also `AMS driver system definition <../../AMS/System.html>`__ and :ref:`symmetry section of ADF <appendix symmetry>`.
* `QM/MM, QM/QM, Quild with the Hybrid engine <../../Hybrid/index.html>`__
* $AMSHOME/atomicdata/ADF directory with ADF basis sets (instead of $ADFHOME/atomicdata)
* scalar relativistic ZORA is the default (instead of non-relativistic)

.. seealso::
  
  More details this can be found in the section :ref:`AMSification of ADF<AMSIFICATION>`

.. |AMS| replace:: `AMS driver <../../AMS/index.html>`__
