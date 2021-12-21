.. _band_PEDANOCV: 

PEDA-NOCV - decomposing the orbital relaxation term
***************************************************

This tutorial will teach you how to perform a `Periodic Energy Decomposition Analysis (PEDA) <../../BAND/Analysis/Energy_Decomposition_Analysis.html>`__ combined with the Natural Orbitals for Chemical Valency (`NOCV <../../BAND/Analysis/Energy_Decomposition_Analysis.html#periodic-energy-decomposition-analysis-and-natural-orbitals-of-chemical-valency-peda-nocv>`__) method for periodic systems with `BAND <../../BAND/index.html>`__. It will also show how to visualize NOCV orbitals and NOCV deformation densities.

Setting up the System and the Calculation
=========================================

.. rst-class:: steps

  \ 
    | Follow the instructions in the sections "Set up the system" and "Set up the PEDA calculation" of the first :ref:`PEDA Tutorial<band_PEDA_Restricted>`.

Preparations for the PEDA-NOCV calculation
------------------------------------------

Now the PEDA-NOCV has to be switched on. Go to the PEDA-NOCV menu,

.. rst-class:: steps

  \ 
    | Panel bar **Properties → PEDA-NOCV**
    | Check the **Perform PEDA-NOCV analysis** checkbox

You may want to define a NOCV eigenvalue threshold (default: 0.001) which handles the amount of output.

.. image:: /Images/PEDAWithNOCV/amsinput_BAND_Properties_PEDA-NOCVB_Tut5.png

Then you have to keep in mind that the PEDA-NOCV is implemented for :math:`\Gamma`-only case. So, go to the 'Integration K-Space' menu,

.. rst-class:: steps

  \ 
    | Panel bar **Details → K-Space Integration**
    | Set the 'K-Space' to 'Gamma only'


.. image:: /Images/PEDAWithNOCV/amsinput_BAND_Details_KspaceB_Tut5.png


Save and run the calculation
----------------------------

Now you can save and run the calculation. 

.. rst-class:: steps

  \ 
    | **File → Save**, give it a name and press Save. 
    | **File → Run**

Step 2: Checking the results
============================

After the calculations of the fragments and the PEDA finished you can look for the PEDA results. Therefore, open the "Output" using the SCM dropdown menu.

.. rst-class:: steps

  \ 
    | **SCM → Output**

You can jump to the 'PEDA-NOCV Energy Terms' via the corresponding button in the 'Properties' drop-down menu.

.. rst-class:: steps

  \ 
    | **Properties → PEDA-NOCV Energy Terms**

Reference results:

.. image:: /Images/PEDAWithNOCV/amsoutput_B_Tut5.png

Step 3: Plotting NOCV orbitals and deformation densities
========================================================

You can visualize the charge NOCV deformation densities which describe the charge flow between the fragments. Therefore, open the "View" using the SCM drop-down menu.

.. rst-class:: steps

  \ 
    | **SCM → View**
    | Press CTRL+2 to view along the Y-axis
    | **Fields → Grid → Medium**

Depending on your preferences (w.r.t. showing atoms of neighboring cells) you will end up with the following representation of AMSview.

.. image:: /Images/PEDAWithNOCV/amsview_A_Tut5.png

You can now add an isosurface with phase via the drop-down menu 'Add', or via 'Ctrl+B'.

.. rst-class:: steps

  \ 
    | **Add → Isosurface: With Phase**

.. image:: /Images/PEDAWithNOCV/amsview_B_Tut5.png

Step 3a: Plotting NOCV deformation densities
--------------------------------------------

To get an overview of the NOCV deformation densities click on 'Select Field ...' and then on 'NOCV Def Densities...'. The following window should appear.

.. image:: /Images/PEDAWithNOCV/amsview_NOCVDefDens_MenuA_Tut5.png

For example you can now visualize the first NOCV deformation density. (Be aware of the small isovalue of 0.000025 in the following picture!)

.. image:: /Images/PEDAWithNOCV/amsview_NOCVDefDens_3_Tut5.png

(For further tweaking you can click on "Isosurface: With Phase" and select "Show Details")

This deformation density visualizes the charge flow from red to blue lobes. Here, the charge transfer from the CO to the MgO surface is shown.

According to the information in  the 'Select NOCV Deformation Density' window the first NOCV deformation density is a combination of the NOCV orbitals 1 (the small number denotes the donor/occupied NOCV) and 150 (the large number denotes the acceptor/unoccupied NOCV).

.. image:: /Images/PEDAWithNOCV/amsview_NOCVDefDens_MenuB_Tut5.png

Step 3b: Plotting NOCV orbitals
-------------------------------

These NOCV orbitals can visualized by changing the field to 'NOCV Orbitals'. The following window should appear.

.. image:: /Images/PEDAWithNOCV/amsview_NOCVOrbs_Menu_Tut5.png

By selecting the 1st and 150th NOCV orbital these are calculated and can then be visualized one at a time.

NOCV orbital 1 does show predominantly a lone-pair localized at the CO fragment.

.. image:: /Images/PEDAWithNOCV/amsview_NOCVOrbs_3_Tut5.png

NOCV orbital 150 does show predominantly a lobe connecting the CO fragment and a Mg atom of the surface.

.. image:: /Images/PEDAWithNOCV/amsview_NOCVOrbs_150_Tut5.png

**Remark**: The calculated fields for the NOCV properties does represent not only the central unit cell but partially the neighboring cells. So, it can be tough to only show what is needed and not confuse additional lobes of the neighboring cells with something in the unit cell! You can hide parts of the field using the **Clip Plane** in BANDGUI.

.. rst-class:: steps

  \ 
    | **Isosurface: With Phase → Details**
    | Check **Use Clip Plane**

To optimize the resulting plot one can visualize (temporarily) and modify the position of the **Clip Plane** by checking **Interactive Plane**.

.. rst-class:: steps

  \
    | Check **Interactive Plane**

.. image:: /Images/PEDAWithNOCV/amsview_NOCV_interactive.png
