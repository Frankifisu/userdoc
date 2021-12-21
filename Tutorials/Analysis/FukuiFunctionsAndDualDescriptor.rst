.. _Fukui: 

Fukui Functions and the Dual Descriptor 
***************************************

Chemical reactivity can be analyzed using `Fukui Functions and the Dual Descriptor <../../GUI/Fukui.html>`__. ADF provides the tools to perform this analysis. 
The local chemical reactivity can be described per atom via a condensed Fukui Function. Subsequently, the local softness can be determined as well.
The Fukui Functions and the Dual Descriptor can be visualized in the GUI with AMSview.

Step 1: Setting up the calculation 
==================================
.. rst-class:: steps

  \ 
    | Start AMSinput with the |ADFPanel| panel active.
    | Build the carbon monoxide molecule using the search function |Search|
    | Set the **XC** functional to **GGA BP86**
    | Set **Relativity → None** (QTAIM analysis cannot be performed in combination with relativistic effects)
    | Open the Conceptual DFT tab in **Properties → Conceptual DFT** 
    | Check both Fukui options at the bottom of the panel (nucleophilic and electrophilic attack)
   
Here you can specify which Fukui functions you want to calculate. Both can be calculated at the same time, and is also required for the Dual Descriptor.
The default way to calculate the Fukui functions is to add or subtract a whole electron. However, it is possible to use fractional charges by modifying the Charge change parameter.

.. image:: /Images/FukuiFunctionsAndDualDescriptor/t16-fukuisettings.png

.. rst-class:: steps

  \
    | Open the Bader tab in **Properties → QTAIM**  
    | Check the **Perform QTAIM analysis** button
    | Set the **Analysis** level to **Full**
   
The condensed Fukui Functions and local softness are calculated using atomic charges. By default the Hirshfeld, Voronoi and Mulliken charges are used. The Bader charges can be used as well if they are calculated.

.. rst-class:: steps

  \
    | Use **File → Save As** to save the file as 'CO_Fukui'
    | Run the calculation

Step 2: The output
==================

The condensed Fukui Functions and the local softness can be found in the output file of the main calculation.

.. rst-class:: steps

  \ 
    | Open the output file with AMSoutput: **SCM → Output**
    | Go to the Condensed Fukui section by **Properties → Condensed Fukui**

.. image:: /Images/FukuiFunctionsAndDualDescriptor/t16-output.png


The condensed Fukui functions are given per atom, with the various atomic charge methods. The same applies for the local softness.

Step 3: Visualizing the Fukui functions and Dual Descriptor 
===========================================================

The Fukui functions can be visualized in AMSview, using the electron density. 

.. rst-class:: steps

  \
    | **SCM → View**
    | Set the grid size to medium **Fields → Grid → Medium**
    | Add an isosurface with phase **Add → Isosurface: With Phase**
    | At the bottom of the screen (in Select Field...) choose the Properties → Fukui Plus
    | The instruction on the screen asks for the result file of the Fukui Plus calculation
    | Choose adf.plus.rkf
    | Enable the second checkbox for the field to use the wireframe model

.. image:: /Images/FukuiFunctionsAndDualDescriptor/t16-fukuiplus.png

AMSview will create some calculated fields to combine the spin densities for the unrestricted calculations, and calculates the Fukui plus function. The wireframe model allows us to see any hidden isosurface. Another way to do this is by lowering the opacity in the field details.

.. rst-class:: steps

  \
    | Disable the field by unchecking the first checkbox at the bottom
    | Create a new isosurface with phase
    | At the bottom of the screen (in "Select Field...") choose Properties → Dual Descriptor (FDL)
    | The fukui plus function is already loaded, the instruction now asks for the missing Fukui Minus calculation
    | Choose adf.minus.rkf
    | Enable the second checkbox for the field to use the wireframe model

.. image:: /Images/FukuiFunctionsAndDualDescriptor/t16-dualdescriptor.png
