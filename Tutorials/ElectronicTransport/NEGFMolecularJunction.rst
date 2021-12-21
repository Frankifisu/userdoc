.. _DFTB_NEGF_bipyridine:

Au-(4,4'-bipyridine)-Au molecular junction
==========================================

.. seealso::
   
  `DFTB-NEGF manual <../../DFTB/NEGF.html>`__ and `BAND-NEGF manual <../../BAND/Electronic_Transport/NEGF.html>`__

In this tutorial we will use the **NEGF geometry building** tools to create a **Au-(4,4'-bipyridine)-Au** molecular junction:

.. image:: /Images/NEGFMolecularJunction/negf_t3_final_geo.png


Instructions
------------

.. rst-class:: steps

  \
    | Start up **AMSinput**
    | Switch to **DFTB**: |ADFPanel| **→** |DFTBPanel|
    | Select **Task → NEGF**
    | Select **Model → SCC-DFTB**
    | In the main DFTB panel click on **Parameter directory → QUASINANO2013.1**
    | Click on |MoreBtn| to go to the **NEGF** panel (or click on **Model → NEGF**)

Import the leads and fill the central region with 4 layers of lead material:

.. rst-class:: steps

  \
    | Click :download:`here <../downloads/Au3x3_lead.xyz>` to download the **lead** file **Au3x3_lead.xyz**
    | Import the **lead** file **Au3x3_lead.xyz** by clicking on the folder icon next to **Lead**
    | **Fill** the central region with **4 layers** of lead material

We now **carve** two tips out of the central gold wire:

.. rst-class:: steps

  \
    | Select the gold atoms as shown in the picture below
    | Delete the selected atoms by pressing **delete** on your keyboard


.. image:: /Images/NEGFMolecularJunction/negf_t3_carve_out.png


We need to *make space* in the central region for the 4,4'-bipyridine molecule;
to this aim we define a **left tip** and a **right tip**:

.. rst-class:: steps

  \
    | **1.** **Select** the gold atoms on the left-hand side
    | **2.** Click on **+** next to **Left Tip** in the **NEGF panel**
    | **Clear the selection** by clicking anywhere in the molecule-drawing area
    | **3.** **Select** the gold atoms on the right-hand side
    | **4.** Click on **+** next to **Right Tip** in the **NEGF panel**

.. image:: /Images/NEGFMolecularJunction/negf_t3_assign_tip.png

Your system should now look like this:

.. image:: /Images/NEGFMolecularJunction/negf_t3_tips_ready.png

.. tip::

  You can **remove atoms from a tip** by selecting them and clicking on **-** next to **Left/Right Tip** in the **NEGF panel**

The **tips** are now **anchored** to their respective leads.
If we move the two leads via the **Left/Right lead offset**, the tips will follow them.

*Make space* for 4,4'-bipyridine molecule:

.. rst-class:: steps

  \
    | Set the **Left lead offset** to **-10.0 Angstrom**
    | Set the **Right lead offset** to **10.0 Angstrom**

and import it:

.. rst-class:: steps

  \
    | Click :download:`here <../downloads/4_4_bipyridine.xyz>` to download the .xyz file **4_4_bipyridine.xyz**
    | Click on **File → Import Coordinates**
    | Open **4_4_bipyridine.xyz** (the .xyz file you just downloaded)

Your system should now look like this:

.. image:: /Images/NEGFMolecularJunction/negf_t3_mol_imported.png


.. tip::

  It is good practice to test the convergence of the results with respect to the **number of lead repetitions and** an amount of **buffer lead material in the central region**


We are now ready to run the calculation:

.. rst-class:: steps

  \
    | Click on **File → Save**, and name the job "zero_gate"
    | Run the calculation with **File → Run**
    | Wait for the calculation to finish


Gate potential
--------------

To include a **gate potential** for the 4,4'-bipyridine molecule:

.. rst-class:: steps

  \
    | In the **NEGF panel** in AMSinput
    | **1.** **Select** the **4,4'-bipyridine molecule**
    | **2.** Click on **+** next to **Gate potential region** in the **NEGF panel**
    | **3.** Set the Gate **Voltage** to **0.2 V**

.. image:: /Images/NEGFMolecularJunction/negf_t3_gate_potential.png

We will now run the job and visualize the results:

.. rst-class:: steps

  \
    | Click on **File → Save as...** and save it as **gate_0_2**
    | Run the calculation with **File → Run**
    | Wait for the calculation to finish
    | Click on **SCM → Spectra...**

To better see the effect of the bias potential on the transmission function, we can **add** the transmission functions at zero gate we computed earlier:

.. rst-class:: steps

  \
    | In **AMSspectra** click on **File → Add** and select **negf.rkf** in the **gate_zero.results** folder


.. image:: /Images/NEGFMolecularJunction/negf_t3_transmission.png

