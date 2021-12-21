.. This tutorial has been recorded: examples/tutorials/adf-vibexci
.. Keep the recording in sync so it may be used to generate the images!

.. _Vibrationally_resolved_electronic_spectra_with_ADF:

Vibrationally resolved electronic spectra with ADF
**************************************************

In this tutorial we use the vertical gradient Franck-Condon (VG-FC) `Vibronic-Structure Tracking (VST) method <../../AMS/Tasks/VibrationalAnalysis/Vibrationally_resolved_electronic_spectra.html>`__ to calculate the vibrationally resolved absorption spectrum of the first excited singlet state of naphthalene.

There are different methods to calculate a vibrationally resolved absorption spectrum.
Out of these methods VST is in principal the quickest method and can also be used for much larger sized molecules.
It is based on a mode-tracking algorithm and works by tracking those modes that are expected to have the largest impact on the vibronic-structure of the spectrum. More information on VST and related methods can be found in the AMS user manual:

* `Vibrationally resolved electronic spectra section of the AMS manual <../../AMS/Tasks/VibrationalAnalysis/Vibrationally_resolved_electronic_spectra.html>`__

Step 1: Geometry Optimization
=============================

Let us first obtain a naphthalene molecule, and `optimize its geometry <../../AMS/Tasks/Geometry_Optimization.html>`__  with `ADF <../../ADF/index.html>`__.

.. rst-class:: steps

  \
    | **1.** Start AMSinput.
    | **2.** In AMSinput, click the search icon |Search| and type "naphthalene" into the box.
    | **3.** Select the "Naphthalene (ADF)" entry from the molecules section.
    | **4.** Click the Symmetrize button |SymmTool| to check the symmetry (should be D(2H))
    | **5.** Select **Task → Geometry Optimization**.
    | **6.** Select **Frozen core → None**.
    | **7.** Click on **File → Save As...** and give it the name "naphthalene_GO".
    | **8.** Click on **File → Run**.
    | **9.** Wait for the calculation to finish.
    | **10.** When AMSinput asks if it should update the geometry to the optimized geometry, select **Yes**.

.. figure:: /Images/VibrationallyResolvedElectronicSpectraADF/VST_naphthalene.png
  :align: center


Step 2: Excited state gradient
==============================

Here we will look at the vibrationally resolved absorption spectra of the lowest electronically excited singlet state S1.
The VG-FC Vibronic-Structure Tracking method needs the excited state gradient of S1 at the ground state geometry.

.. seealso::

    ADF manual sections on `excitations <../../ADF/Input/Excitation_energies.html>`__ and `excited states gradients <../../ADF/Input/Excited_state_optimizations.html>`__


.. rst-class:: steps

  \
    | Select **Task → Single Point**.
    |
    | Panel bar **Properties → Gradients, Stress tensor**.
    | Check the **Nuclear gradients** checkbox.
    |
    | Panel bar **Properties → Excitations (UV/Vis), CD**.
    | Select **Type of excitations → SingletOnly**.
    | Enter '1' for **Number of excitations**.
    |
    | Panel bar **Properties → Excited State Geometry**.
    | Check the **All Gradients** checkbox.
    |
    | Click on **File → Save As...** and give it the name "naphthalene_ES".
    | Click on **File → Run**.
    | Wait for the calculation to finish.
    |
    | Click on **SCM → Spectra**.
    | **Axes → Horizontal Unit → eV**.
    | **Width → 0.01**.

.. image:: /Images/VibrationallyResolvedElectronicSpectraADF/VST_ES.png




Step 3: Vibronic-Structure Tracking
===================================

The calculated lowest excited singlet state is of B2.u symmetry.
For the VG-FC vibronic-structure tracking method we need a new input:

.. rst-class:: steps

  \
    | Click on **SCM → New Input**.
    | Click on **File → Import Coordinates...** and and select the "naphthalene_ES.ams" file.
    | Select **Task → Vibrational Analysis**.
    | Select **Frozen core → None**.
    |
    | Panel bar **Model → Vibrational Analysis**.
    | Select **Type → Vibronic Structure Tracking**.
    |
    | Panel bar **Details → Vibrational Analysis Excitation**.
    | Click on the folder next to **Excitation file:** and select the file **adf.rkf** in the **folder naphthalene_ES.results**
    | Enter 'B2.u 1' for **Singlet**.
    |
    | Panel bar **Details → Vibrational Analysis Spectrum**.
    | Enter '50' for **Line width** in cm\ :sup:`-1`.
    |
    | Click on **File → Save As...** and give it the name "naphthalene_VST".
    | Click on **File → Run**.
    | Wait for the calculation to finish (may take several minutes).
    | Click on **SCM → Spectra**.

.. image:: /Images/VibrationallyResolvedElectronicSpectraADF/VST.png

The spectrum is relative to the 0-0 excitation energy.
The default (artificial) broadening is relatively wide, therefore it was changed to 50 cm\ :sup:`-1`.
