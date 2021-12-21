.. _BAND_NEGF_gate_bias:

Gate and Bias potentials
========================

.. seealso::
   
  `DFTB-NEGF manual <../../DFTB/NEGF.html>`__ and `BAND-NEGF manual <../../BAND/Electronic_Transport/NEGF.html>`__

In this tutorial we will show how to include a **Gate** and **Bias** potentials in NEGF calculations.

.. rst-class:: steps

  \
    | Start up **AMSinput**
    | Switch to **BAND**: |ADFPanel| **→** |BANDPanel|
    | Select **Task → NEGF**
    | Click on |MoreBtn| to go to the **NEGF** panel (or click on **Model → NEGF**)


Download the lead and molecules .xyz files:

.. rst-class:: steps

  \
    | Click :download:`here <../downloads/Li_lead.xyz>` to download the **lead** file **Li_lead.xyz**
    | Click :download:`here <../downloads/CuAg.xyz>` to download the molecule **CuAg.xyz**

.. note::

  The system studied in this tutorial is just a toy system.

Set up the system:

.. rst-class:: steps

  \
    | **1.** Select the file **Li_lead.xyz** as **Lead**
    | **2.** Fill the central region with 4 layers of lead material
    | **3.** Set the **tips** as shown in the figure. (Select left two atoms and click the + after Left tip, similarly for the right tip.)
    | **4.** Set the right and left **lead offsets** to -8.5 and 8.5 respectively
    | **5.** Select **Method → self-consistent**
    | Import the file **CuAg.xyz** by clicking on **File → Import Coordinates...**

.. image:: /Images/NEGFGateBiasBAND/negf_t5_system_set_up.png



To apply a **gate potential** of 0.1 Volts for the CuAg molecule:

.. rst-class:: steps

  \
    | **1.** Select the CuAg molecule
    | **2.** Click on the **+** next to **Potential region**
    | **3.** Set the gate potential to 0.1 V

.. image:: /Images/NEGFGateBiasBAND/negf_t5_gate.png


.. tip:: 

  You can check the regions in the **Model → Regions** panel. You will see there the right_tip, left_tip and gate_potential regions. Use the checkboxes to see them individually.

We will now apply a **bias potential** of 0.1 Volt, with a **ramp-potential** from -3.0 to 3.0 Angstrom (see picture below), do not forget to change the unit to Angstrom, the choices shown by clicking on the unit:

.. image:: /Images/NEGFGateBiasBAND/negf_t5_biassettings.png
   :scale: 50 %
   :align: center


.. note:: 

  You can only apply a bias potential for the **self-consistent** and **self-consistent + align** NEGF methods


.. rst-class:: steps

  \
    | **1.** Set the bias potential **Voltage** to 0.1
    | **2.** Set the bias potential range to -3.0 and 3.0 respectively


.. image:: /Images/NEGFGateBiasBAND/negf_t5_bias.png

we are now ready to run the calculation:

.. rst-class:: steps

  \
    | Click on **File → Save**
    | Run the calculation with **File → Run**
    | Wait for the calculation to finish


The current (in atomic units) is saved on the binary **.rkf** file.

.. rst-class:: steps

  \
    | Click on **SCM → KFBrowser**
    | Activate **Expert mode** by clicking on **File → Expert mode**
    | Click on **File → Related Files → band.rkf**  
    | Look for the **NEGF** section 
    | Click on the small arrow next to the NEGF section
    | The **current** should be "-0.00289"


.. image:: /Images/NEGFGateBiasBAND/negf_t5_kfbrowser.png


.. tip::

  You can also extract this information using `amsreport <../../Scripting/Commandline_Tools/AMSreport.html>`__:
  ``amsreport band.rkf "NEGF%current"``


.. warning::

  The *Current vs Bias* plot you can visualize with AMSspectra is computed **from a the transmission function at fixed bias**, and it is therefore **just an approximation** of the *real* *Current vs Bias* characteristic. If you want to compute the actual *Current vs Bias* characteristic you have to run multiple calculations using different bias potentials.



