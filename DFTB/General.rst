General
#######

.. |AMSdriver| replace:: `AMS driver <../AMS/index.html>`__

Introduction
************

The DFTB engine implements density functional based tight-binding methods, which can be viewed as computationally very efficient approximations to density functional theory (DFT). As such it is a good engine for cheap calculations that still include quantum effects. DFTB is a computational engine that runs through the |AMSdriver|. It can be used directly from the command line, from Python, and through our graphical interface.

What's new in DFTB?
*******************

New in DFTB2022.1
=================

* Visualization of orbitals in AMSview now also works for calculations with (most) DFTB.org parameter sets.
* :ref:`Fragment orbital analysis <FRAGMENTS>`
* :ref:`Charge transport (transfer integrals) <TRANSFERINTEGRALS>`

New in DFTB2021.1
=================

* The D4 :ref:`dispersion correction <DispersionCorrection>` has been added. It can be used with the Slater-Koster based model Hamiltonians and the DFTB.org parameter sets.

New in DFTB2020
===============

* Calculations with the :ref:`GFN1-xTB model <ModelHamiltonians>` and many k-points are significantly faster.
* The default model has been changed from SCC-DFTB to GFN1-xTB, as the latter supports all elements.
* Various `new applications <../AMS/General.html#new-in-ams2020-1>`__ in the |AMSdriver|.

New in DFTB2019.3
=================

* The internals of the DFTB engine have been restructured, making it faster, more scalable and more accurate for periodic systems, while at the same time enabling previously locked combinations of features:

  - The default for the accuracy of :ref:`k-space integration<KSpace>` has been changed: DFTB used to sample only the Γ-point by default. As of this release the default k-points depend on the system size, using the same logic as in BAND. See the `page on k-space integration in the BAND manual <../BAND/Accuracy_and_Efficiency/K-Space_Integration.html>`__.
  - Calculations with :ref:`k-space integration<KSpace>` are generally faster and scale much better on parallel machines.
  - The :ref:`GFN1-xTB model <ModelHamiltonians>` can now be used together with :ref:`k-space integration<KSpace>`.
  - :ref:`Unrestricted calculations <SCCDetails>` can now also be performed in conjunction with :ref:`k-space integration<KSpace>`.
  - The orbital dependent (l-dependent) :ref:`SCC cycle<SCCDetails>` is now compatible with :ref:`k-space integration<KSpace>`.
  - The `stress tensor <../AMS/Properties.html#nuclear-gradients-and-stress-tensor>`__ is now calculated analytically, making its calculation faster and the result more accurate.

* An :ref:`implicit solvation model<Solvation>` (GBSA: Generalized Born (GB) model augmented with the solvent accessible surface area (SA) term) has been added to DFTB, allowing simulations of molecules in solution.
* Various `new applications <../AMS/General.html#new-in-ams2019-3>`__ in the |AMSdriver|.

New in DFTB2019.1
=================

* Grimme's GFN1-xTB has been added as a new :ref:`model Hamiltonian <ModelHamiltonians>`. It supports molecular as well es periodic calculations for systems including elements up to Radon. Visualization of the results (e.g. molecular orbitals) in AMSview is also supported.
* Various `new applications <../AMS/General.html#new-in-ams2019-1>`__ in the |AMSdriver|.
* More robust and easier to set up :ref:`k-space integration<KSpace>`.
* More robust SCC convergence:

  - :ref:`Adaptive mixing<SCCDetails>`: The charge mixing parameter is automatically decreased if the energy increases during the SCC cycle.
  - The default electronic temperature has been increased to 300K, making SCC convergence more robust for systems with small HOMO-LUMO gaps.

New in DFTB2018
===============

New features
^^^^^^^^^^^^

* Elastic tensor and related properties (e.g. Bulk modulus) (via |AMSdriver|)
* Linear transit and PES scan (via |AMSdriver|)
* Geometry optimization under pressure (via |AMSdriver|)
* ...

AMS: a new driver program
^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   In the 2018 release of the Amsterdam Modeling Suite we introduced a new driver program call **AMS**.
   We recommend you to first read the `General section of the AMS Manual <../AMS/General.html>`__

If you use DFTB exclusively via the Graphical User Interface (GUI), this change should not create any issues. If, on the other hand, you create input files *by hand* (or you use DFTB via `PLAMS <../plams/index.html>`__), then you should be aware that **shell scripts for DFTB2017 and previous versions are not compatible with DFTB2019 and have to be adjusted to the new setup.**

The example below shows how a shell script for DFTB2017 is converted to DFTB2019.

**DFTB2017 shell script (obsolete):**

.. code-block:: none

   #!/bin/sh

   # This is a shell script for DFTB2017 which will not work for DFTB2019

   $AMSBIN/dftb << EOF

   Task
      RunType GO
   End

   System
      Atoms
         H 0.0 0.0 0.0
         H 0.9 0.0 0.0
      End
   End

   DFTB
      ResourcesDir Dresden
   End

   Geometry
      iterations 100
   End

   EOF


**DFTB2019 shell script:**

.. code-block:: none

   #!/bin/sh

   # This is a shell script for DFTB2019

   # The executable '$AMSBIN/dftb' is no longer present.
   # You should use '$AMSBIN/ams' instead.

   $AMSBIN/ams << EOF
      # Input options for the AMS driver:

      System
         Atoms
            H 0.0 0.0 0.0
            H 0.9 0.0 0.0
         End
      End

      Task GeometryOptimization

      GeometryOptimization
         MaxIterations 100
      End

      # The input options for DFTB, which are described in this manual,
      # should be specified in the 'Engine DFTB' block:

      Engine DFTB
         ResourcesDir Dresden
      EndEngine
   EOF
