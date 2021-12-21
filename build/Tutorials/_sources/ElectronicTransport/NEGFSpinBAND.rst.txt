.. _BAND_NEGF_spin:

Spin transport in Chromium wire
===============================

.. seealso::
   
  `DFTB-NEGF manual <../../DFTB/NEGF.html>`__ and `BAND-NEGF manual <../../BAND/Electronic_Transport/NEGF.html>`__


To study spin-resolved transport is sufficient to activate the "unrestricted" option in the Band Main panel:

.. rst-class:: steps

  \
    | Start up **AMSinput**
    | **1.** Switch to **BAND**: |ADFPanel| **→** |BANDPanel|
    | **2.** Tick the **Unrestricted** check-box
    | **3.** Select **Task → NEGF**
    | **4.** Click on |MoreBtn| to go to the **NEGF** panel (or click on **Model → NEGF**)

.. image:: /Images/NEGFSpinBAND/negf_t4_main_panel.png

Now, download the lead file:

.. rst-class:: steps

  \
    | Click :download:`here <../downloads/Cr_lead.xyz>` to download the lead file **Cr_lead.xyz**


and create a 1D chromium chain: 

.. rst-class:: steps

  \
    | In the **NEGF panel**
    | Click on the folder icon next to **Lead**: this will prompt a file dialog window
    | Open **Cr_lead.xyz** (the .xyz file you just downloaded)
    | **Fill** the central region with **9 layers** of lead material

Your system should now look like this:

.. image:: /Images/NEGFSpinBAND/negf_t4_system_ready.png


We **run the calculation** and visualize the results with **AMSspectra**:

.. rst-class:: steps

  \
    | Click on **File → Save**
    | Run the calculation with **File → Run**
    | Wait for the calculation to finish
    | Click on **SCM → Spectra...**


.. image:: /Images/NEGFSpinBAND/negf_t4_transmission.png
