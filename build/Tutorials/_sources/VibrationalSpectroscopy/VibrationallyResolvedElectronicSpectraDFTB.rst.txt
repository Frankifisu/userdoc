.. This tutorial has been recorded: examples/tutorials/dftb-vibexci
.. Keep the recording in sync so it may be used to generate the images!

.. _Vibrationally_resolved_electronic_spectra_with_DFTB:

Vibrationally resolved electronic spectra with DFTB
***************************************************

In this tutorial we use the vertical gradient Franck-Condon (VG-FC) `Vibronic-Structure Tracking (VST) method <../../AMS/Tasks/VibrationalAnalysis/Vibrationally_resolved_electronic_spectra.html>`__ to calculate the vibrationally resolved absorption spectrum of the first excited singlet state of pyrene.

There are different methods to calculate a vibrationally resolved absorption spectrum.
Out of these methods VST is the quickest method and can also be used for much larger sized molecules.
It is based on a mode-tracking algorithm and works by tracking those modes that are expected to have the largest impact on the vibronic-structure of the spectrum.
More information on VST and related methods can be found in the AMS user manual:

* `Vibrational resolved electronic spectra section of the AMS manual <../../AMS/Tasks/VibrationalAnalysis/Vibrationally_resolved_electronic_spectra.html>`__


Step 1: Geometry Optimization
=============================

Let us first obtain a pyrene molecule, and `optimize its geometry <../../AMS/Tasks/Geometry_Optimization.html>`__  with `DFTB <../../DFTB/index.html>`__.

.. rst-class:: steps

  \
    | **1.** Start AMSinput.
    | **2.** In AMSinput, click the search icon |Search| and type "pyrene" into the box.
    | **3.** Select the "Pyrene (ADF)" entry from the molecules section.
    | **4.** Click the Symmetrize button |SymmTool| to check the symmetry (should be D2h)
    | **5.** Select the DFTB panel: |ADFPanel| **→** |DFTBPanel|
    | **6.** Select **Model → DFTB3**.
    | **7.** Select **Parameter directory → DFTB.org/3ob-3-1**.
    | **8.** Click on the 'Pre-optimize' button.

.. image:: /Images/VibrationallyResolvedElectronicSpectraDFTB/VST_pyrene.png


Step 2: Excited state gradient
==============================

Here we will look at the vibrationally resolved absorption spectra of the lowest electronically excited singlet state S1.
The VG-FC Vibronic-Structure Tracking method needs the excited state gradient of S1 at the ground state geometry.

.. seealso::

    DFTB manual section on `excitations <../../DFTB/Spectroscopy_and_Properties.html#excited-states-with-time-dependent-dftb>`__


.. rst-class:: steps

  \
    | **1.** Select **Task → Single Point**.
    |
    | **2.** Panel bar **Properties → Gradients, Stress Tensor**.
    | **3.** Check the **Nuclear gradients** checkbox.
    |
    | **4.** Panel bar **Properties → Excitations (UV/Vis)**.
    | **5.** Select **Type of excitations → Singlet**.
    | **6.** Enter '1' for **Number of excitations**.
    | **7.** Enter '1' for **Calculate excited state gradients for Excitation number**.
    |
    | **8.** Click on **File → Save As...** and give it the name "pyrene_ES".
    | **9.** Click on **File → Run**.
    | **10.** Wait for the calculation to finish.
    | **11.** Click on **SCM → Spectra**.
    | **12.** **Axes → Horizontal Unit → eV**.
    | **13.** **Width → 0.01**.

.. image:: /Images/VibrationallyResolvedElectronicSpectraDFTB/VST_ES.png


Step 3: Vibronic-Structure Tracking
===================================

For the VG-FC vibronic-structure tracking method we need a new input:

.. rst-class:: steps

  \
    | **1.** Click on **SCM → New Input**.
    | **2.** Click on **File → Import Coordinates...** and and select the "pyrene_ES.ams" file.
    | **3.** Select the DFTB panel: |ADFPanel| **→** |DFTBPanel|.
    | **4.** Select **Task → Vibrational Analysis**.
    | **5.** Select **Model → DFTB3**.
    | **6.** Select **Parameter directory → DFTB.org/3ob-3-1**.
    |
    | **7.** Panel bar **Model → Vibrational Analysis**.
    | **8.** Select **Type → Vibronic Structure Tracking**.
    |
    | **9.** Panel bar **Details → Vibrational Analysis Excitation**.
    | **10.** Click on the folder next to **Excitation file:** and select pyrene_ES.results/dftb.rkf.
    | **11.** Enter 'A 1' for **Singlet**.
    |
    | **12.** Click on **File → Save As...** and give it the name "pyrene_VST".
    | **13.** Click on **File → Run**.
    | **14.** Wait for the calculation to finish.
    | **15.** Click on **SCM → Spectra**.

.. image:: /Images/VibrationallyResolvedElectronicSpectraDFTB/VST.png

The spectrum is relative to the 0-0 excitation energy.
The default (artificial) broadening is relatively wide.


Step 4: Increase spectral resolution
====================================

If we want to change the broadening of the vibronic spectrum we can change the **Line width** in
**Details → Vibrational Analysis Spectrum** and run the calculation again.
Here we will also restart the VST calculation, which saves computation time, for which we need a new input:

.. rst-class:: steps

  \
    | **1.** Click on **File → Save As...** and give it the name "pyrene_VST_restart".
    |
    | **2.** Panel bar **Details → Vibrational Analysis Spectrum**.
    | **3.** Enter '50' for **Line width** in cm\ :sup:`-1`.
    |
    | **4.** Panel bar **Details → Vibrational Analysis Mode Tracking**.
    | **5.** Click on the folder next to **VSTrestart file:** and select ``pyrene_VST.results/ams.rkf``.
    |
    | **6.** Click on **File → Run**.
    | **7.** Wait for the calculation to finish.
    | **8.** Click on **SCM → Spectra**.

.. image:: /Images/VibrationallyResolvedElectronicSpectraDFTB/VST2.png

