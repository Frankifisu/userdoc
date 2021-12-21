.. _band_PEDA_Restricted: 

Periodic Energy Decomposition Analysis - PEDA
*********************************************

This tutorial will teach you how to perform a `Periodic Energy Decomposition Analysis (PEDA) <../../BAND/Analysis/Energy_Decomposition_Analysis.html>`__ for periodic systems with `BAND <../../BAND/index.html>`__.


Set up the system - CO@MgO(100) (√2×√2)-R45°
============================================

Start AMSinput in a clean directory and switch to Band:

.. rst-class:: steps

  \ 
    | **1.** Switch to the **BAND panel**: |ADFPanel| **→** |BANDPanel|
    | **2.** Copy-paste the following coordinates directly into AMSinput

:: 

	Mg       0.59538358       0.59538226       0.20750000
	Mg       2.08384335      -0.89307752      -1.89750000
	Mg      -2.38153597       0.59538226       0.20750000
	Mg      -0.89307620      -0.89307752      -1.89750000
	O        2.08384335      -0.89307752       0.20750000
	O       -0.89307620      -0.89307752       0.20750000
	O        0.59538358       0.59538226      -1.89750000
	O       -2.38153597       0.59538226      -1.89750000
	O        0.59538553       0.59539200       3.95250000
	C        0.59538493       0.59538903       2.80750000
	VEC1     2.97691955      -2.97691955       0.00000000
	VEC2     2.97691955       2.97691955       0.00000000


.. rst-class:: steps

  \ 
    | **3.** Set View to Along Y-axis (CTRL+2)

.. image:: /Images/PEDARestricted/amsinput_BAND_Main_MgO+CO1.png


Set up the PEDA calculation
===========================

To run the PEDA for the adsorption of CO on MgO, you have to define the fragments. Therefore switch to Regions menu.

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Regions**
    | **2.** Select the CO fragment and add a new region by clicking on the '+' button (or Ctrl+G)
    | **3.** De-select the currently selected atoms by clicking in an empty space of the molecule drawing area
    | **4.** Select the MgO fragment and add a new region by clicking on the '+' button (or Ctrl+G)
    | **5.** You may want to rename "Region_1" to CO and "Region_2" to MgO. (optional)

.. image:: /Images/PEDARestricted/amsinput_BAND_Model_Regions_MgO+CO4.png


We now enable the PEDA calculation:

.. rst-class:: steps

  \ 
    | **1.** Panel bar **MultiLevel → Fragments**
    | **2.** check the "Use fragments" box. This will trigger the PEDA.

.. figure:: /Images/PEDARestricted/amsinput_BAND_MultiLevel_Fragments_MgO+CO2.png 
  :align: center

Go back to the main panel set some calculation options for BAND:

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Main**
    | **2.** **XC Functional → GGA → PBE**
    | **3.** **Basis set → DZP**
    | **4.** **Frozen core → Small**
    | **5.** **Numerical quality → Basic** (this is just to make the calculation run faster! For production results, don't use "basic" numerical quality)


.. image:: /Images/PEDARestricted/amsinput_BAND_Main_MgO+CO3.png


Run the calculation check the results
=====================================

Now you can save and run the calculation:

.. rst-class:: steps

  \ 
    | **File → Save**, give it a name and press Save.
    | **File → Run**


After the calculations of the fragments and the PEDA finished you can look for the PEDA results. Open the "Output" using the SCM dropdown menu:

.. rst-class:: steps

  \ 
    | **SCM → Output**

You can jump to the 'PEDA Energy Terms' via the corresponding button in the 'Properties' drop-down menu.


.. rst-class:: steps

  \ 
    | **Properties → PEDA Energy Terms**

Reference results:

.. image:: /Images/PEDARestricted/Output_MgO+CO2.png

In addition to these energy terms the summed preparation energies of the fragments and the (negative) bond dissociation energy are usually given. Therefore you have to calculate the energy difference between the electronically and structurally relaxed fragments (which can be accessed by a geometry optimization of the separated fragments) and the promoted fragments (which are already calculated and used for the PEDA). Adding this energy difference, which is equal to the preparation energy, to the interaction energy will give you the negative bond dissociation energy.


Plot the deformation density with respect to the fragments
==========================================================

Fire up amsview

.. rst-class:: steps

  \ 
    | **SCM → View**

and select add -> Isosurface: With Phase. At the bottom you can now open the selector, and this shows an extra item "Fragment related densities". Select "Deformation density w.r.t. sum-of-fragments". You should see

.. image:: /Images/PEDARestricted/DeformationDensity.png

Make sure that you select the view along the x-axis and change the isovalue from 0.03 to 0.001. As you can see, more is happening on the CO than on the MgO surface.

You can also visualize the same, but obtained with via the fitted density. This is faster, but is an approximation. In this case they look pretty much the same.
