.. This tutorial has been recorded: examples/tutorials/adf-uvvis-ethene
.. Keep the recording in sync so it may be used to generate the images!

.. _EXCITATION_ETHENE:

GUI tour: UV/Vis spectrum of ethene
***********************************

In this tutorial you will first construct an ethene molecule and optimize its geometry.

Next you will perform an excitation energies calculation using |ADF|.
The results will be examined using AMSlevels, AMSdos, AMSspectra and AMSview. The use of the KFbrowser is also shown.

Finally you will run an `excited state geometry optimization <../../ADF/Input/Excited_state_optimizations.html>`__ and check its results.


Create your ethene molecule
===========================

First we construct an ethene molecule, and pre-optimize its geometry:

.. rst-class:: steps

  \
    | **1.** Start AMSinput (**SCM → New Input**)
    | **2.** Select the C-tool by clicking on |CTool|
    | **3.** Select the Double bond mode |BondTool| **→ Double** (or use the shortcut: press the '2' - key)
    | **4.** Click somewhere in the drawing area to create a carbon atom
    | **5.** Click again to create a second carbon atom (with a double bond)
    | **6.** Click on the just created Carbon atom to stop bonding
    | **7.** Select the **Atoms → Add Hydrogen** command
    | **8.** Click on |PreOptimTool| to pre-optimize
    | **9.** Click on |SymmTool| to symmetrize the structure (it should be D(2H))

Your ethene molecule should look something like this:

.. figure:: /Images/ExcitationsAndUVVisOfEthene/t2-2-ethene.png
  :align: center


.. note::

  Starting from the 2020 release, ADF does not automatically symmetrize and re-orient the molecule.
  If your molecule is symmetric and you want to make sure that the highest possible symmetry is used, you should first symmetrize your system with |SymmTool|


Optimize the geometry
=====================

The next step is to `optimize the geometry <../../AMS/Tasks/Geometry_Optimization.html>`__ using ADF:

.. rst-class:: steps

  \
    | Select the **Geometry Optimization** task

.. figure:: /Images/ExcitationsAndUVVisOfEthene/t2-3-mainoptions.png
  :align: center

With the proper options selected, now run ADF:

.. rst-class:: steps

  \
    | **1.** Select the **File → Run** command
    | **2.** Click 'Yes' in the pop-up to save the current input
    | **3.** In the file select box, choose a name for your file (for example 'ethene')
    | **4.** Click 'Save'

Now ADF will start automatically, and you can follow the calculation using the logfile that is automatically shown.

.. rst-class:: steps

  \
    | Wait until the optimization is ready (should take very little time)
    | A dialog window should appear, asking whether you want to **Read new coordinates and bonds from "ethene.results/ams.rkf"**. Click 'Yes' to update the coordinates


Calculate the excitation energies
=================================

Select calculations options
---------------------------

To set up the calculation of the `excitation spectrum <../../ADF/Input/Excitation_energies.html>`__:

.. rst-class:: steps

  \
    | **1.** Select the **Single Point** task in the main panel
    | **2.** Use the panel bar **Properties → Excitations (UV/Vis), CD** command to go to the Excitations panel
    | **3.** For the 'Type of excitations' option, Select 'Singlet and Triplet'
    | **4.** Check the 'Calculate NTOs' check box

.. figure:: /Images/ExcitationsAndUVVisOfEthene/t2-4-exciopright.png
  :align: center

For the tutorial this set up is fine, normally you would also need to select an XC potential and Basis set that gives better results.

Run the calculation
-------------------

Now everything is ready to run the excitation energies calculation with ADF. Before running we will save the current input in a different file:

.. rst-class:: steps

  \
    | **1.** Select **File → Save As...**
    | **2.** Enter a filename (ethene-exci) and click 'Save'
    | **3.** Select **File → Run**
    | **4.** Wait for the calculation to finish

Results of your calculation
===========================

Logfile: AMStail
----------------

The logfile shows you that the calculation has finished, and that indeed the excitation code has been running:

.. rst-class:: steps

  \
    | Select **SCM → Logfile**

.. figure:: /Images/ExcitationsAndUVVisOfEthene/t2-5-logfile.png
  :align: center

Energy levels: level diagram and DOS
------------------------------------

.. rst-class:: steps

  \
    | Select **SCM → Levels**

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-levels.png

In this level diagram you can see that the HOMO and LUMO consist mainly of carbon p orbitals. It is also easy to see what orbitals the hydrogens take part in.

.. tip::

    You can drag the vertical columns around (the final MOs and the fragments) to get a clearer diagram if needed.
    Click and drag in the name (at the bottom) to do this.

Note that the carbon and hydrogen stacks show all carbon and hydrogen atoms at once: they show the fragment type.
AMSlevels can also show the individual fragments but when using atomic fragments you will get too many fragments.
In this particular case symmetry is used, and since there is only one symmetry unique carbon atom and only one symmetry unique hydrogen atom
you still would see only one stack per atom type.

.. rst-class:: steps

  \
    | Select **SCM → DOS**
    |
    | In the AMSdos window:
    | **View → Add Graph**
    | Select one hydrogen atom

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-dos.png

In these plots you can see that the partial DOS for the hydrogen atoms have no contribution to the HOMO.
By right clicking on an atom you can also show partial DOS graphs with contribution from selected atoms and selected L-values only.

Excitation spectrum: AMSspectra
-------------------------------

.. rst-class:: steps

  \
    | Select **SCM → Spectra**

AMSspectra will start and show the calculated excitation   spectrum.

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-spectra.png

In the window below the spectrum you will find a table with information.
You can get more information by selecting one of the entries
(or click on the peak in the spectrum):

.. rst-class:: steps

  \
    | In the table select the Singlet-Singlet1B3.u peak

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-spectrapopup.png

The composition of the excitation in terms of orbital transitions is listed on the right side.
In many cases you can visualize relevant orbitals or `NTOs <../../ADF/Input/Excitation_energies.html#nto-natural-transition-orbitals>`__  with AMSview by clicking on them in the window on the right.
The active items are visually marked.

.. rst-class:: steps

  \
    | Click on the the first major contribution line (with the highlighted orbitals)

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-spectraorbs.png

.. rst-class:: steps

  \
    | Close the two windows showing the orbitals using **File → Close** in both windows

Orbitals, orbital selection panel: AMSview
------------------------------------------

We will now use AMSview to examine the orbitals. Not just one, but have a look at many of them.
To do that AMSview has an 'orbital selection' panel.

.. rst-class:: steps

  \
    | Select **SCM → View**
    | Select **Properties → HOMO**
    | Click on the field selector pull-down in the control bar for the HOMO (reading SCF_B1.u 1: ...),
    | select **Orbitals (occupied)**

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-orbitalselector.png

In the 'Select Occupied Orbital' window you can select the orbital that you want to see.
Note that the currently visible orbital is highlighted using a dark green background.

.. rst-class:: steps

  \
    | Click on all of the orbitals in the window, one by one, and observe the orbitals
    | Click again on them

When you click the first time on an orbital, its values need to be calculated and then the orbital is shown.
When you click for a second time on an orbital in the list, it has already been  calculated (indicated by the light green background color).
And thus it shows immediately.

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-orbital1.png

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-orbital2.png

The Orbital select window allows you to reorder the orbitals by clicking on the headers of the columns.
Thus you can sort by Symmetry, Spin, etc. Clicking again on a header reverts the sort order.

.. rst-class:: steps

  \
    | Click on 'Symmetry' in the 'Select Occupied Orbital' window

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-orbitals-by-symmetry.png

.. rst-class:: steps

  \
    | Close AMSview: **File → Close**

Transition density: AMSview
---------------------------

You can use AMSview to view orbitals etc, but also to have a look at the transition density.

.. rst-class:: steps

  \
    | In AMSjobs with your ethene-exci job selected:
    | Select **SCM → View**
    |
    | In AMSview:
    | Select **Add → Isosurface: With Phase**

In the field pull-down menu (in the control line for the isosurface with phase) you will find an entry 'Transition (Fit) Density',
and if you select it an orbital select box will shown with all available transition densities:

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-transdenslist.png

In this case lets select the transition density that belongs to the largest peak: the Singlet-Singlet excitation at 0.3123 Hartree (which may have B1.u, B2.u or B3.u symmetry depending on the molecule orientation):

.. rst-class:: steps

  \
    | Click on the **Excitations_SS_B3.u_Fitdensity_1** field
    | Change the iso value to 0.003
    | Select **Fields → Grid → Medium**
    | Rotate the molecule a little

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-transdens.png


AMSoutput
----------

Using the output browser you can find all details about your   excitation calculation. Use the menu to jump to the relevant part of output:

.. rst-class:: steps

  \
    | Select **SCM → Output**
    | Select **Response Properties → All Singlet-Singlet Excitation Energies**

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-bob.png

KFBrowser: KF files, copy to Excel, graphs of results
-----------------------------------------------------

Most result of the calculation are saved to the KF result file (the **adf.rkf** file for an ADF calculation).
You can inspect the contents of KF files using the KFBrowser.

.. rst-class:: steps

  \
    | Select **SCM → KFBrowser**


The KFBrowser gets the raw data out of the result file, and presents a selection of that might be of interest for users.

By default, KFBrowser opens the **ams.rkf** binary file. The ADF-specific results (such as excitations energies) are on the **adf.rkf** file.

.. rst-class:: steps

  \
    | Click on  **File → Related files → adf.rkf**. This will open the **adf.rkf**, containing the ADF specific results.
    | Click on the arrow in front of Excitations
    | Click on the arrow in front of Energies (Hartree) (in the Excitations section)

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-kfbrowser1.png

If you click on the name of the property you can select it. Next   you can copy it, and paste it for example in Excel:

.. rst-class:: steps

  \
    | Click on "Energies (Hartree)"
    | Copy (from the Edit menu or the usual shortcut)
    | Open Excel or some text editor
    | Paste

After pasting you should have your results nicely formatted in Excel or in some text document.
Note that the values are tab-separated, so pasting into Excel will automatically put the data (energies) in cells.

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-excel.png

In a similar way you can copy/paste other results. Or even all results:

.. rst-class:: steps

  \
    | In the KFBrowser window:
    | **Edit → Select All**
    | **Edit → Copy**
    | In the Excel or text editor window:
    | Paste

All results should be nicely formatted in your text document or spreadsheet:

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-aolexcel3.png

Another feature of the KFBrowser is that it can show results in simple graphs:

.. rst-class:: steps

  \
    | Close the KFBrowser window
    | Open it again **SCM → KFBrowser**
    | Open the **adf.rkf** file: **File → Related files → adf.rkf**
    | Open the Charges section
    | Click on Mulliken (e)
    | Shift-click on MDC-Q (e)
    | Use the **Graph → Selection As Graph** command (or double click on the selection)

A window should appear that shows the selected results, charges   in this case:

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-5-graph.png

Finally two features that are intended for developers and expert users: the KFBrowser module can also show the raw data on the result file, and it can dump a KF file as a plain text file. To activate the expert mode, use the **File → Expert Mode** menu command. To save the contents of the result file as a text file using the **File → Save As ASCII...** command.

Excited state geometry optimization and excited state density
=============================================================

With ADF you can also `optimize the geometry of some selected excited state <../../ADF/Input/Excited_state_optimizations.html>`__. It depends on your application which state to optimize, in this tutorial we will pick the state corresponding to the largest peak in the UV/Vis spectrum.

.. rst-class:: steps

  \
    | Determine the name of the excited state corresponding with the largest peak in AMSspectra (1B1.u, 1B2.u or 1B3.u in this case, depending on the orientation)
    | If your molecule has a different symmetry the name may be different!
    |
    | In AMSjobs: click on the ADF button in front of the ethene-exci job

AMSinput should open with the ethene-exci job (or come to the   front if already open).

.. rst-class:: steps

  \
    | Select the **Geometry Optimization** task
    |
    | Select Frozen Core: None
    |
    | Open the Excited State Geometry panel in the Properties menu
    | Enter the excited state to optimize (1B1.u, 1B2.u or 1B3.u, depending on the orientation)
    |
    | **File → Save As...**
    | Save the file with a name like 'ethene-exci-1B3u'
    |
    | **File → Run**

With AMSmovie you can see how the excited state geometry is different from the ground state geometry:

.. rst-class:: steps

  \
    | Wait for the calculation to finish
    | **SCM → Movie**
    | Observe how the geometry changes

With AMSmovie you can see how the excited state density is different from the ground state density:

.. rst-class:: steps

  \
    | **SCM → View**
    |
    | **Add → Isosurface: With Phase**
    |
    | In the field select menu on the bottom: select **Excited State → Difference Density**
    | Change the isovalue to 0.001
    |
    | **Fields → Grid → Medium** to get a better quality

Now you see how the excited state density differs from the ground   state density (for this geometry)

.. image:: /Images/ExcitationsAndUVVisOfEthene/t2-ethene-difference-density.png

If you wish to see the excited state density, you can do this using a Calculated field (add the ground state density to the   difference density).

Closing the AMS-GUI modules
---------------------------

To close all modules for your excitations calculation at once, use the Quit command from the SCM menu:

.. rst-class:: steps

  \
    | Select **SCM → Quit**

Quit will close all open modules that have your current job loaded, except AMSjobs. The Close All command will close every   AMS-GUI module, including AMSjobs:

.. rst-class:: steps

  \
    | Select **SCM → Quit All**

All AMS-GUI modules will be closed.



.. |ADF| replace:: `ADF <../../ADF/index.html>`__
