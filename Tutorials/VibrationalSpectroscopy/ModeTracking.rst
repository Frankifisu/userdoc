.. This tutorial has been recorded: examples/tutorials/mode-tracking
.. Keep the recording in sync so it may be used to generate the images!

.. _AMS_mode_tracking:

Mode Tracking
*************

In this tutorial we use the `Mode Tracking method <../../AMS/Vibrational_Spectroscopy.html#mode-tracking>`__ to calculate a specific mode with C=O stretch character in the dydrogesterone molecule. More information on this features can be found in the AMS user manual:

* `Vibrational spectroscopy section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html>`__
* `Mode Tracking section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html#mode-tracking>`__

Let us first obtain a dydrogesterone molecule.

.. rst-class:: steps

  \
    | **1.** Start AMSjobs.
    | **2.** Click on **SCM → New Input**. This will open AMSinput.
    | **3.** In AMSinput, insert the dydrogesterone molecule by clicking the search icon |Search| and typing "dydrogesterone" into the box. Select the "C21H28O2: Prodel" entry from the molecules section.

.. image:: /Images/ModeTracking/ModeTracking1.png

The Mode Tracking method requires an initial guess for a mode, which will then be iteratively improved until it is a real normal mode. In this tutorial we want to calculate the normal mode associated with stretching of the C=O bond marked in green in the image above. The pure C=O stretch will not be a real normal mode of the system, but we can use it as an initial guess that we iteratively improve using Mode Tracking in order to get the real mode.

The easiest way to obtain the pure C=O stretch mode as the initial guess, is to let AMS perform a frequency calculation, but restrict it to only the two involved atoms. This can be easily done at the end of a geometry optimization of the system, which we need to perform anyway.

.. rst-class:: steps

  \
    | **1.** Select the DFTB panel: |ADFPanel| **→** |DFTBPanel|
    | **5.** Select **Model → DFTB3**, and **Parameter directory → DFTB.org/3ob-freq-1-2**.
    | **2.** Make sure **Task** is set to **Geometry Optimization** and tick the **Frequencies** check-box below.
    | **3.** Select the carbon and oxygen atom we are interested in the viewport on the left, and convince yourself that these are the atoms with the indices 24 and 25. (The atom index is shown on the bottom right of the viewport when an atom is selected.)
    | **4.** Go to the panel **Properties → IR (frequencies)**, and select "Hessian only for" and then "New region". This creates a new region for the selected CO atoms.

.. image:: /Images/ModeTracking/ModeTracking2.png

We are now ready to run the calculation:

.. rst-class:: steps

  \
    | **1.** Click on **File → Save As...** and give it the name "GO_PFREQ".
    | **2.** Click on **File → Run** . This will bring the **AMSjobs** window to the front.
    | **3.** Wait for the calculation to finish. It should finish almost instantaneous.
    | **4.** When AMSinput asks if it should update the geometry to the optimized geometry, select **Yes**.

Let us look at the modes we obtained in AMSspectra.

.. rst-class:: steps

  \
    | **1.** Click on **SCM → Spectra**.

.. image:: /Images/ModeTracking/ModeTracking3.png

Note that we only have 6 modes with a non-zero frequency in our spectrum, as we have ignored all but the 6 degrees of freedom associated with the two C and O atoms. By clicking the mode at 1678cm^-1 you can convince yourself, that this is indeed the pure stretch of the C=O bond we were interested in. We will now use this mode as the initial guess for a Mode Tracking calculation. Note that this is mode number 153. We will need this number later.

.. rst-class:: steps

  \
    | **1.** Return to the AMSinput window that has the optimized geometry of dydrogesterone.
    | **2.** Go to the **Main** panel.
    | **3.** Select **Task → Vibrational Analysis** and disable the **Frequencies** checkbox.
    | **4.** Go to the panel **Model → Vibrational Analysis**.
    | **5.** Select **Type → Mode Tracking**.
    | **6.** Select the modes from our partial frequencies calculation, by setting **Mode file** to **GO_PFREQ.results/dftb.rkf**.
    | **7.** Type the mode number **153** of the pure C=O stretch into the **Mode numbers** field.

.. image:: /Images/ModeTracking/ModeTracking4.png

We are now ready to run the calculation:

.. rst-class:: steps

  \
    | **1.** Click on **File → Save As...** and give it the name "ModeTracking".
    | **2.** Click on **File → Run** . This will bring the **AMSjobs** window to the front.
    | **3.** Wait for the calculation to finish. It should finish almost instantaneous.
    | **4.** Click on **SCM → Spectra**.

Looking at the resulting mode in AMSspectra, it is easy to see, that it is no longer the pure C=O stretch we originally started with. The C=O stretch character of the mode is still strong, but we now have a real normal mode of the system, just as if we had performed the much more expensive full frequency analysis.

.. image:: /Images/ModeTracking/ModeTracking5.png

We leave it to the user to do a full frequency analysis and confirm that this is indeed a true normal mode, and that frequency and IR intensity are correct. This concludes the tutorial on Mode Tracking in AMS.
