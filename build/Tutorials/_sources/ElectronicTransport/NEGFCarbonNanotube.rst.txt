.. _NEGFCarbonNanotube:

Electronic transport in a carbon nanotube
=========================================

.. seealso::
   
  `DFTB-NEGF manual <../../DFTB/NEGF.html>`__ and `BAND-NEGF manual <../../BAND/Electronic_Transport/NEGF.html>`__

In this tutorial we will be modeling the electronic transport through a carbon nanotube using the NEGF formalism.

.. figure:: /Images/NEGFCarbonNanotube/negf_t1_system_setup.png
  :width: 85%
  :align: center


Setting up the calculation
--------------------------

The simulation in this tutorial can be performed with either the `DFTB engine <../../DFTB/index.html>`__ or the `BAND engine <../../BAND/index.html>`__. DFTB is computationally faster than BAND, but the results will generally be less accurate.

.. tabs::

  .. tab:: DFTB

    .. rst-class:: steps

      \
        | Start up **AMSinput**
        | **1.** Switch to **DFTB**: |ADFPanel| **→** |DFTBPanel|
        | **2.** Select **Task → NEGF**
        | **3.** Select **Model → SCC-DFTB** 
        | **4.** Click on the **parameter directory folder** and select  **DFTB.org/3ob-3-1**

      .. figure:: /Images/NEGFCarbonNanotube/dftb_main_panel.png

  .. tab:: BAND

    .. rst-class:: steps

      \
        | Start up **AMSinput**
        | **1.** Switch to **BAND**: |ADFPanel| **→** |BANDPanel|
        | **2.** Select **Task → NEGF**

      .. figure:: /Images/NEGFCarbonNanotube/band_main_panel.png

    .. note:: 

      In this tutorial we use the **Non self consistent** NEGF method of BAND. 
      This method represents a computationally cheap alternative to the more sophisticated **self consistent method**, but it can only be used for zero-bias calculations.
      See the `BAND-NEGF Documentation <../../BAND/Electronic_Transport/NEGF.html>`__ for more details.


Next, we switch to the **NEGF panel** where we can set up the geometry of our system and specify various NEGF calculation parameters:

.. rst-class:: steps

  \
    | Click on |MoreBtn| next to **Task: NEGF** to switch to the NEGF panel (or click on **Model → NEGF**)


We first need an **.xyz file defining our lead**, that is, a carbon nanotube:

.. rst-class:: steps

  \
    | Click :download:`here <../downloads/carbon_nano_tube_4-4.xyz>` to download the .xyz file **carbon_nano_tube_4-4.xyz**

Now import the lead:

.. rst-class:: steps

  \
    | **1.** Click on the folder icon next to **Lead**: this will prompt a file dialog window
    | **2.** Open **carbon_nano_tube_4-4.xyz** (the .xyz file you just downloaded)
    | **3.** Set **Lead Repetitions** to **2**

.. image:: /Images/NEGFCarbonNanotube/negf_t1_select_lead.png

.. note:: 

  The leads cannot be directly modified in the molecule-editing area. In the next tutorial we will show how to create a leads.


We now need to define our **central region**. In this tutorial, the central region consist of a nanotube (same as in the lead). We can easily **fill in the central region** with lead-material with the **Fill central region** option:

.. rst-class:: steps

  \
    | **1.** Click on **Fill**
    | **2.** Enter **2** in the prompted dialog window and click on **OK**

.. image:: /Images/NEGFCarbonNanotube/negf_t1_fill_with_bulk.png

This concludes the geometry-building part of a NEGF calculation. Your system should look like this:

.. image:: /Images/NEGFCarbonNanotube/negf_t1_geo_ready.png


From the NEGF panel we can change other parameters of the NEGF calculation, but in this tutorial we will use the default values.


Run the calculation and visualize the results
---------------------------------------------

We are ready to **run the calculation**:

.. rst-class:: steps

  \
    | Click on **File → Save as...**
    | Run the calculation with **File → Run**
    | Wait for the calculation to finish


The results can be visualized with **AMSspectra**. To start up AMSspectra:

.. rst-class:: steps

  \
    | Click on **SCM → Spectra...**

Here you can visualize:

* **Transmission function** :math:`T(E)`
* **NEGF-DOS** (density of states)
* **Current v.s. Bias Potential** (computed from the the zero-bias Transmission function)

.. rst-class:: steps

  \
    | In AMSspectra, click on **Spectra → Transmission / Transmission+DOS / Current**

.. note::
  
  Energies are relative to the **Fermi energy of the lead**, 
  *i.e* in the picture below, 0 eV corresponds to the Fermi energy of the nanotube (first simulation in `Simulations work flow <../../DFTB/NEGF.html>`__)

This is the computed **transmission function** of our nanotube:


.. tabs::

  .. tab:: DFTB

    .. image:: /Images/NEGFCarbonNanotube/dftb_transmission.png

  .. tab:: BAND

    .. image:: /Images/NEGFCarbonNanotube/band_transmission.png

