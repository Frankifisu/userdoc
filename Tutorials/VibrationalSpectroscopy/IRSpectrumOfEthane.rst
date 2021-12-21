.. _FREQ_ETHANE: 

Vibrational frequencies and IR spectrum of ethane
*************************************************

Create an ethane molecule
=========================

.. rst-class:: steps

  \ 
    | **1.** Open AMSinput

Next we create an ethane molecule: 

.. rst-class:: steps

  \ 
    | **1.** Select the C-tool (|CTool|)
    | **2.** Click once in the molecule drawing area to make a carbon atom
    | **3.** Click again to make a second carbon atom
    | **4.** Select **Atoms → Add Hydrogens**
    | **5.** And do it again: **Atoms → Add Hydrogens**
    | **6.** Pre-optimize by clicking on |PreOptimTool|
    | **7.** Click the Symmetrize button |SymmTool|

.. figure:: /Images/IRSpectrumOfEthane/t3-3-ethane.png
    :align: center

You need to add hydrogen twice: the first time one carbon atom was selected. 
Thus, the 'Add Hydrogen' command added the hydrogen to that selected atom only. 
By repeating the 'Add Hydrogen' command the hydrogens are added in all possible places. 

The symmetrization should have enforced perfect D(3D) symmetry, using the Symmol program (see the help balloon on that button for details). 

Geometry optimization and vibrational frequencies calculation
=============================================================

We will now set up a `geometry optimization <../../AMS/Tasks/Geometry_Optimization.html>`__ followed by a `frequency <../../AMS/Vibrational_Spectroscopy.html>`__ calculation:

.. rst-class:: steps

  \ 
    | In the main ADF panel:
    | **1.** Select **Task → Geometry Optimization**
    | **2.** Check the **Frequencies** check-box 

.. figure:: /Images/IRSpectrumOfEthane/t3-4-main.png
    :align: center

Now run the calculation:

.. rst-class:: steps

  \ 
    | In AMSinput
    | **1.** In the **menu bar**, select **File → Run** (give your calculation a nice name, e.g.  'ethane')
    | Wait for the calculation to finish (check the logfile)...
    | **2.** In the dialog that appears when the calculation is finished, click 'Yes' to import the optimized geometry


Visualize the IR-spectrum, normal modes
=======================================

The IR spectrum can be visualized using the AMSspectra module.

.. rst-class:: steps

  \ 
    | In AMSinput
    | **1.** In the **menu bar** Select **SCM → Spectra**

.. image:: /Images/IRSpectrumOfEthane/t3-5-spectra.png

On the left side of the window the molecule (Ethane) is shown. 

On the right side the IR spectrum is shown. 

.. tip::

  - save a picture (of the IR spectrum) as an image: **File → Save Image...** (PNG by default)
  - export the xy coordinates of the spectrum to a plain text file: **File → Export XY Values...**.
  - export the peak positions and intensities to a plain text file: **File → Export XY Peaks...**.  

Below the spectrum window a table is shown with details about the peaks.

You can click on a peak in the spectrum, or select a line in the table: 

.. rst-class:: steps

  \
    | **1.** Click on the mode with the intensity (approximately 58 km/mol) in the table


.. image:: /Images/IRSpectrumOfEthane/t3-5-normalmode.png

The atoms of the molecule should be animated according to the selected normal mode (see also the options in the **Play** menu in the menu bar).

To view another normal mode, you can use the left and right arrow keys to move through them.

You can make the displacements larger or smaller via menu commands, or via the up and down arrow keys on the keyboard 
(after clicking in the graph or molecule window).

To show the normal mode as vectors: 

.. rst-class:: steps

  \ 
    | **1.** Click in the molecule window to make sure it has input focus
    | **2.** Click on **Play → Displacement Vectors** to visualize the normal mode with vectors

.. image:: /Images/IRSpectrumOfEthane/t3-5-normalmodevecs.png

You can make the vectors larger or smaller using the same ctrl/cmd-L/K, or arrow up and down. 

You can also visualize the normal mode in AMSmovie (which offers some extra options, e.g. you can make an mpg movie showing the mode)

.. rst-class:: steps

  \ 
    | In the menu bar, select **Play → Open Mode In AMSmovie** 

In AMSmovie you have some extra advanced options, for example you can make an mpg movie showing the mode. 


.. seealso::

  `Partial Vibrational Spectra (PVDOS) <../../AMS/Vibrational_Spectroscopy.html#partial-vibrational-spectra-pvdos>`__

You can close all open AMS-GUI windows by selecting in the menu bar  **SCM → Quit All**,
