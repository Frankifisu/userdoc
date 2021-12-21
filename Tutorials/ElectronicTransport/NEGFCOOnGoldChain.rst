.. _NEGFCOOnGoldChain:

Electronic transport in a 1D gold chain
=======================================

Introduction
------------

The system studied in this tutorial is discussed in **Electronic and Transport Properties of Artificial Gold Chains** `PhysRevLett.93.096404 <https://doi.org/10.1103/PhysRevLett.93.096404>`__ and **Benchmark density functional theory calculations for nano-scale conductance** `The Journal of Chemical Physics 128, 114714 (2016) <https://doi.org/10.1063/1.2839275>`__.

We will simulate the electronic transport through an atomic gold chain, and study the effect that an adsorbed CO molecule has on the conductance.

.. image:: /Images/NEGFCOOnGoldChain/negf_t2_system_cartoon.png

According to `PhysRevLett.93.096404 <https://doi.org/10.1103/PhysRevLett.93.096404>`__ "a single CO group [...] modulates the electronic wave functions, acting as a ‘‘chemical scissor’’ along the gold chain, to strongly modify the coherent transport properties of the system".

.. seealso::
   
  `DFTB-NEGF manual <../../DFTB/NEGF.html>`__ and `BAND-NEGF manual <../../BAND/Electronic_Transport/NEGF.html>`__


Creating the lead file
----------------------

Let's begin by **creating a lead file**. A lead file is a simple .xyz file with an extra lattice vector. 

.. tip::

  The folder **$AMSHOME/atomicdata/Molecules/NEGF/Leads** contains some pre-defined lead files

For this tutorial the lead will be a single gold atom with a lattice of 2.9 Å (in the x-direction).
Let us create this with AMSinput:

.. rst-class:: steps

  \
    | Start up **AMSinput**
    | **1.** Switch to **BAND**: |ADFPanel| **→** |BANDPanel|
    | **2.** From the main BAND-panel, select **Periodicity → Chain**
    | **3.** Click Click on |MoreBtn| to switch the **Lattice** panel


.. image:: /Images/NEGFCOOnGoldChain/negf_t2_create_lead_1.png

In the lattice panel we can specify the lattice vector:

.. rst-class:: steps

  \
    | Set the lattice vector to 2.9

.. image:: /Images/NEGFCOOnGoldChain/negf_t2_create_lead_2.png

We now add the gold atom

.. rst-class:: steps

  \
    | **1.** Click on 'X'
    | **2.** Select 'Au'
    | **3.** Click anywhere in the drawing area to add the gold atom


.. image:: /Images/NEGFCOOnGoldChain/negf_t2_create_lead_3.png

and set the coordinates of the gold atom to **(0,0,0)**:

.. rst-class:: steps

  \
    | **1.** Click on **Model → Coordinates**
    | **2.** Set the xyz coordinates on the Au atom to (0,0,0)


.. image:: /Images/NEGFCOOnGoldChain/negf_t2_create_lead_4.png

We now export this 1D gold chain as an .xyz file:

.. rst-class:: steps

  \
    | **1.** Click on **File → Export Coordinates...**
    | **2.** Save the file as "Au_lead.xyz"
    | **3.** Close AMSinput  **File → Close**


The .xyz file, defining our lead, should look like this::

  1

  Au       0.00000000       0.00000000       0.00000000
  VEC1     2.90000000       0.00000000       0.00000000 



Gold chain transport calculation
--------------------------------

We are now ready to set up the NEGF calculation for the gold chain. The simulation in this tutorial can be performed with either the `DFTB engine <../../DFTB/index.html>`__ or the `BAND engine <../../BAND/index.html>`__. DFTB is computationally faster than BAND, but the results will generally be less accurate.


.. tabs::

  .. tab:: DFTB

    .. rst-class:: steps

      \
        | Start up a new **AMSinput**
        | **1.** Switch to **DFTB**: |ADFPanel| **→** |DFTBPanel|
        | **2.** Select **Task → NEGF**
        | **3.** Select **Model → SCC-DFTB** 
        | **4.** Select **Parameter directory → QUASINANO2013.1**
        | **5.** Click on |MoreBtn| next to **Task: NEGF** to switch to the NEGF panel (or click on **Model → NEGF**)

  .. tab:: BAND

    .. rst-class:: steps

      \
        | Start up a new **AMSinput**
        | **1.** Switch to **BAND**: |ADFPanel| **→** |BANDPanel|
        | **2.** Select **Task → NEGF**
        | **3.** Click on |MoreBtn| next to **Task: NEGF** to switch to the NEGF panel (or click on **Model → NEGF**)


In the **NEGF panel**, import the lead file we just created ('Au_lead.xyz'):

.. rst-class:: steps

  \
    | Click on the folder icon next to **Lead**: this will prompt a file dialog window
    | Open **Au_lead.xyz** (the .xyz file you just created)

**Fill the central region** with 9 gold atoms using the "Fill central region" option:

.. rst-class:: steps

  \
    | Click on **Fill**
    | Enter **9** in the prompted dialog window and click on **OK**


Let us also change the range for the Transmission energy grid to **[-3.5,3.0]**, to match the energy range of `PhysRevLett.93.096404 <https://doi.org/10.1103/PhysRevLett.93.096404>`__:

.. rst-class:: steps
 
  \
    | Set the **Transmission energy grid** to **-3.5 ... 3.0**

This is what your set-up should look like:

.. image:: /Images/NEGFCOOnGoldChain/negf_t2_Au_chain_ready.png

We are now ready to **run the calculation** and visualize the results with **AMSspectra**:

.. rst-class:: steps

  \
    | Click on **File → Save as...**
    | Run the calculation with **File → Run**
    | Wait for the calculation to finish
    | Click on **SCM → Spectra...**


This is the computed transmission function through a 1D gold chain:

.. tabs::

  .. tab:: DFTB

    .. image:: /Images/NEGFCOOnGoldChain/dftb_au_transmission.png

  .. tab:: BAND

    .. image:: /Images/NEGFCOOnGoldChain/band_au_transmission.png



CO on gold chain transport calculation
--------------------------------------

We now modify our previous system by adding a CO molecule in the central region:

.. rst-class:: steps

  \
    | Select the AMSinput window: **SCM → Input**
    | Add the **CO** molecule by **copy-pasting** the following coordinates into AMSinput (**CTRL+V** in molecule drawing area)


::

  O     0.0   0.0   3.12
  C     0.0   0.0   1.96

The gold atom on which CO is adsorbed is "pulled" towards the CO molecule by 0.2 Angstrom:

.. rst-class:: steps

  \
    | In the **Coordinates panel** adjust the position of the central gold atom to **(0.0, 0.0, 0.2)** 
    | Change the View Direction to Along Y-axis either via the View Menu or via pressing CTRL+2.

Your system should look like this:

.. image:: /Images/NEGFCOOnGoldChain/negf_t2_CO-Au_chain_ready.png

.. tip::

  It is good practice to include some *buffer* lead material in the **central region**, and test the convergence of the results WRT the *buffer* size (in this tutorial we have 4 *buffer* gold atoms on each side of the central Au-CO).  


**Run the calculation** and visualize the results with **AMSspectra**:

.. rst-class:: steps

  \
    | Click on **File → Save**
    | Run the calculation with **File → Run**
    | Wait for the calculation to finish
    | Click on **SCM → Spectra...**


This is the computed transmission function when CO is adsorbed on a gold chain. 

.. tabs::

  .. tab:: DFTB

    .. image:: /Images/NEGFCOOnGoldChain/dftb_au_with_co_transmission.png

  .. tab:: BAND

    .. image:: /Images/NEGFCOOnGoldChain/band_au_with_co_transmission.png


As expected, the conductivity around the Fermi energy is suppressed by the adsorbed CO molecule.
