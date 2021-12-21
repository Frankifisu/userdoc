.. This tutorial has been recorded: examples/tutorials/band-peda-nocv-unr
.. Keep the recording in sync so it may be used to generate the images!

.. _band_PEDANOCV_Unrestricted: 

PEDA-NOCV for Spin Unrestricted Calculations
********************************************

This tutorial will teach you how to: 

+ perform an `Periodic Energy Decomposition Analysis (PEDA) <../../BAND/Analysis/Energy_Decomposition_Analysis.html>`__ combined with the natural orbitals for chemical valency (NOCV) method (`pEDA-NOCV <../../BAND/Analysis/Energy_Decomposition_Analysis.html#periodic-energy-decomposition-analysis-and-natural-orbitals-of-chemical-valency-peda-nocv>`__) for extended and/or molecular systems with BAND, where the bond is described by open-shell, **spin unrestricted** fragments
+ where to look for the results


Step 1: Start AMSinput
======================

Start AMSinput in a clean directory.

.. rst-class:: steps

  \ 
    | Switch to the **BAND** panel: |ADFPanel| **→** |BANDPanel|
    | Chose **Periodicity**: *None*.

.. image:: /Images/PEDAWithNOCVUnrestricted/amsinput_BAND_Main_0D.png

Step 2: Set up the system - Ethane
==================================

An easy and non-timeconsuming test system is the C-C bond analysis in an ethane molecule. Here, two methyl radicals with opposite spin-polarization do interact to form the shared electron C-C bond. Hence, the fragments and the PEDA-NOCV calculation have to be carried out as `unrestricted <../../BAND/Model_Hamiltonians/Relativistic_Effects_and_Spin.html#spin-polarization>`__ DFT calculations.

You can copy-paste the following geometry information into the GUI directly.

::

   C          1.54081631       0.00000000       0.00000000
   H          1.90061013       0.71448558       0.72714386
   H          1.90061011      -0.98692880       0.25534173
   H          1.90084793       0.27238885      -0.98228957
   C          0.00000000       0.00000000       0.00000000
   H         -0.35953041      -0.27213306       0.98136715
   H         -0.36080772       0.98640196      -0.25411759
   H         -0.36080775      -0.71466441      -0.72582318


.. image:: /Images/PEDAWithNOCVUnrestricted/amsinput_BAND_MainA_Tut4b.png


Step 3: Running the PEDA-NOCV calculation
=========================================

Step 3a: Setting up the fragments
---------------------------------

To run the PEDA and PEDA-NOCV you have to define fragments. Therefore switch to Regions menu.

.. rst-class:: steps

  \ 
    | Panel bar **Model → Regions**

* Select one methyl fragment and add a new region by clicking on the '+' button (or Ctrl+G).
* Then select the other methyl fragment and add a new region by clicking on the '+' button (or Ctrl+G).
* You may want to rename "Region_1" to "H3C_A" and "Region_2" to "H3C_B". (optional)

.. image:: /Images/PEDAWithNOCVUnrestricted/amsinput_BAND_Model_RegionsB_Tut4b.png

Step 3b: Details for the calculation
------------------------------------

Go to the Main menu,

.. rst-class:: steps

  \ 
    | Panel bar **Main**

and change the calculation setup (XC functional, basis set, frozen core, numerical quality and unrestricted calculation) according to the following picture.

.. image:: /Images/PEDAWithNOCVUnrestricted/amsinput_BAND_MainB_Tut4b.png

Step 3c: Enabling the PEDA-NOCV
-------------------------------

Go to the Fragments menu,

.. rst-class:: steps

  \ 
    | Panel bar **MultiLevel → Fragments**
    | Check the "Use fragments" box. This will trigger the PEDA.
    | Define the **spin** polarization of the fragments. One shall be **+1** (excess of 1 electron with spin up) and the other **-1** (excess of 1 electron with spin down).

.. image:: /Images/PEDAWithNOCVUnrestricted/amsinput_BAND_MultiLevel_FragmentsC_Tut4b.png

Furthermore, enable the PEDA-NOCV calculation as follows:

.. rst-class:: steps

  \ 
    | Panel bar **Properties → PEDA-NOCV**
    | Check the **Perform PEDA-NOCV analysis** box
    | Set **Use NOCVs with eV larger than:** to 0.001

.. image:: /Images/PEDAWithNOCVUnrestricted/PEDANOCV_Unrest_Properties.png

Step 3d: Save and run the calculation
-------------------------------------

Now you can save and run the calculation. 

.. rst-class:: steps

  \ 
    | **File → Save**, give it a name and press Save. 
    | **File → Run**

Step 4: Checking the results
============================

After the calculations of the fragments and the PEDA-NOCV finished you can look for the PEDA results. Therefore, open the "Output" using the SCM dropdown menu.

.. rst-class:: steps

  \ 
    | **SCM → Output**

You can jump to the 'PEDA Energy Terms' via the corresponding button in the 'Properties' dropdown menu.

.. rst-class:: steps

  \ 
    | **Properties → PEDA Energy Terms**

Reference results:

.. image:: /Images/PEDAWithNOCVUnrestricted/OutputB_Tut4b.png

In addition to these energy terms the summed preparation energies of the fragments and the (negative) bond dissociation energy are usually given. Therefore you have to calculate the energy difference between the electronically and structurally relaxed fragments (which can be accessed by a geometry optimization of the separated fragments) and the promoted fragments (which are already calculated and used for the PEDA). Adding this energy differences, which are equal to the preparation energy, to the interaction energy will give you the negative bond dissociation energy.


You can jump to the 'PEDA-NOCV Energy Terms' via the corresponding button in the 'Properties' dropdown menu.

.. rst-class:: steps

  \ 
    | **Properties → PEDA-NOCV Energy Terms**

Reference results:

.. image:: /Images/PEDAWithNOCVUnrestricted/PEDANOCV_Unrest_Results.png

Step 5: Plotting NOCV orbitals and deformation densities
========================================================

You can visualize the charge NOCV deformation densities which describe the charge flow between the fragments. Therefore, open the "View" using the SCM dropdown menu.

.. rst-class:: steps

  \ 
    | **SCM → View**
    | **Fields → Grid → Medium**


You can now add an isosurface with phase via the dropdown menu 'Add', or via 'Ctrl+B'.

.. rst-class:: steps

  \ 
    | **Add → Isosurface: With Phase**

.. image:: /Images/PEDAWithNOCVUnrestricted/PEDANOCV_Unrest_amsview1.png

Step 5a: Plotting NOCV deformation densities
--------------------------------------------

To get an overview of the NOCV deformation densities click on 'Select Field ...' and then on 'NOCV deformation densities'. The following window should appear.

.. image:: /Images/PEDAWithNOCVUnrestricted/PEDANOCV_Unrest_amsview2.png

You can see that there are NOCV deformation densities for electron spin A and B. You can visualize the first NOCV deformation density of spin A. (Be aware of the small isovalue of 0.001 in the following picture!) 

.. image:: /Images/PEDAWithNOCVUnrestricted/PEDANOCV_Unrest_amsview4.png

You see the transfer of charge density from red to blue lobes from one methylradical (with spin A excess) to the other (with spin B excess). The first NOCV deformation density for spin B is giving the same picture but the other way around. So, transfer of charge density from the methylradical with spin B excess to the methylradical with spin A excess.

.. image:: /Images/PEDAWithNOCVUnrestricted/PEDANOCV_Unrest_amsview3.png

