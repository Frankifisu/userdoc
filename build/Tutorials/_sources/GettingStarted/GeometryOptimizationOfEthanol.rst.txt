.. This tutorial has been recorded: examples/tutorials/getting-started-ethanol
.. Keep the recording in sync so it may be used to generate the images!

.. _GO_ETHANOL:


Getting started: Geometry optimization of ethanol
*************************************************

This tutorial will help you to:

+ create a simple molecule
+ view the molecule from all sides and save a picture
+ make a couple of changes to the molecule with different tools
+ set up your ADF calculation
+ perform the actual ADF calculation
+ visualize some results: energy levels, geometry, electron density, orbitals, ...


.. seealso::

  More detailed information on the features presented in this tutorial can be found in the `AMS driver manual <../../AMS/index.html>`__ and `ADF manual <../../ADF/index.html>`__.


Step 1: Preparations
====================

Start AMSjobs
-------------

On a Unix-like system, enter the following command:

.. rst-class:: steps

  \
    | cd
    | amsjobs &

On Windows, one can start AMSjobs by double-clicking on the AMS-GUI icon on the Desktop:

.. rst-class:: steps

  \
    | Double click the AMS-GUI icon on the Desktop

On Macintosh, use the AMS2021.xxx program to start AMSjobs:

.. rst-class:: steps

  \
    | Double click on the AMS2021.xxx icon

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-1-startamsjobs.png
  :align: center

Note that the directory in which AMSjobs depends on how you start AMSjobs, so your screen might look different.

Make a directory for the tutorial
---------------------------------

We prefer to run the tutorial in a new, clean, directory. That way we will not interfere with other projects. AMSjobs not only manages your jobs, but also has some file management options. In this case we use AMSjobs to make the new directory:

.. rst-class:: steps

  \
    | Select the **File → New Directory** command (the New Directory command from the File menu)
    | Rename the new directory by typing 'Tutorial' and a Return

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-1-newdir.png
  :align: center

.. rst-class:: steps

  \
    | Change into that directory by clicking once on the folder icon in front of it

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-1-emptydir.png
  :align: center

Start AMSinput
--------------

Now we will start AMSinput in this directory using the SCM menu:

.. rst-class:: steps

  \
    | Select the **SCM → New Input** menu command

The AMSinput module should start:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-1-startup.png
  :align: center

The AMSinput window consists of the following main parts:

+ the menu bar with the menu commands (SCM, File, Edit, ..., on a Mac the menu bar is at the top of the screen)
+ the drawing area of the molecule editor (the dark area on the middle left side)
+ the status field (lower part of the dark area, blank when the AMSinput is empty as shown above)
+ the molecule editor tools
+ many panels with several kinds of options (currently the 'ADF Main' panel is visible)
+ panel bar with menu commands to activate the panel of choice
+ a search tool |Search|

Undo
----

AMSinput has an Undo command (**Edit → Undo**), which works on your molecule (thus not on your input options).

If you make a mistake while making changes to your molecule, just use the **Edit → Undo** menu command to go back in time. You can Undo more than one step, or Redo a step (with **Edit → Redo**) if you wish to do so.

Step 2: Create your molecule
============================

Create a molecule
-----------------

The molecule we are going to create is ethanol.

First we will draw the two carbon atoms, next the oxygen atom, and after that we will add all hydrogen atoms at once. Finally, we will pre-optimize the geometry within AMSinput.

Create the first carbon atom
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create an atom, you need to select an atom tool.

.. rst-class:: steps

  \
    | Select the C-tool by clicking on the button with the 'C'

Back glow is added to the 'C' button to indicate that you are using the C-tool. Also, the status field in the left bottom corner shows 'C tool' to indicate that you are using the C-tool.

Now create the first carbon atom:

.. rst-class:: steps

  \
    | Click somewhere in the drawing area

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-onecarbon.png
  :align: center

One carbon atom has been created.

Note that:

+ If you move the mouse you will see a white line from that carbon atom to the current mouse pointer position: this shows you are in 'bonding' mode, and that the bond will be made to the atom just created.
+ The 'C' button has a different color, indicating you are still using the C-tool.
+ The carbon atom is selected (the green glow), which indicates that the carbon atom is the current selection.
+ The status field contains information about the current selection: it is a Carbon, number 1, with 4 'connectors'
+ The status field also shows the current tool (C), and that a single bond will be made.

Create the second carbon atom
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rst-class:: steps

  \
    | Click somewhere in the drawing area to create the second carbon atom

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-twocarbons.png
  :align: center

A second carbon atom has been created, bonded to the first atom.

The atom will be created along the 'bonding line', at a distance that corresponds to a normal C-C single bond distance. That is, the bond length is constrained while drawing.

The newly created atom becomes the new selection, and you are still in bonding mode. The next bond will be created to the carbon atom just created. And you are still using the C-tool.

Create the oxygen atom
^^^^^^^^^^^^^^^^^^^^^^

To create the oxygen atom you need to switch to the O-tool:

.. rst-class:: steps

  \
    | Select the O-tool by clicking on the button with the 'O'

With the O-tool, create an oxygen atom bonded to the second carbon;

.. rst-class:: steps

  \
    | Click somewhere in the drawing area

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ethanolnoh.png
  :align: center

The oxygen atom has been added.

For now, we are done using atom tools, so go back to the select tool:

.. rst-class:: steps

  \
    | Select the select-tool by clicking on the button with the arrow (or press the Esc key)

Add the hydrogens
^^^^^^^^^^^^^^^^^

Now many hydrogen atoms need to be added. You can do this using the H-tool, but a much easier method is to use the **Atoms → Add Hydrogen** menu command:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-atomsmenu-addh.png
  :align: center

The 'Add Hydrogen' menu command works on the selection only, when present. Thus, only one hydrogen atom would be added to the oxygen atom. This is not what you want. So first we make sure that nothing is selected by clicking in empty space.

.. rst-class:: steps

  \
    | Click in empty (drawing) space

Now no atoms are selected any more.

.. rst-class:: steps

  \
    | Select the **Atoms → Add Hydrogen** command

Many menu commands have shortcuts. In this case you can also use the shortcut (ctrl-E or cmd-E, depending on your platform) as an alternative. The shortcuts are indicated in the menu commands.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ethanol-raw.png
  :align: center

All atoms will be saturated with hydrogen atoms. And you have created an ethanol molecule, though the geometry is still far from perfect.

Pre-optimize the geometry
^^^^^^^^^^^^^^^^^^^^^^^^^

Now use the optimizer that comes with AMSinput to pre-optimize the geometry.

.. rst-class:: steps

  \
    | Click on the pre-optimizer button |PreOptimTool|

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ethanol.png
  :align: center

The geometry of the molecule will be pre-optimized, using UFF by default.

.. tip::

    You can select another pre-optimizer via the Preferences, or use a different pre-optimizer by right-clicking on the cog wheel and selecting the method to use from the pop-up menu.

In the status field below the drawing area you can follow the pre-optimization iteration number and the energy relatively to the starting configuration.

Viewing the molecule
--------------------

Rotate, translate, or zoom
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can rotate, translate, and zoom your molecule using the mouse.

You need to drag with the mouse: press a mouse button, and while holding it down move it. Which mouse button, and which modifier key you press at the same time, determines what will happen:

.. csv-table::

   "Rotate",Left
   Rotate in-plane,ctrl-Left
   Translate,Right
   Zoom,"Mouse wheel, or (not on windows) alt-Left (drag up or down)"

The rotate, translate, and zoom operations change how you look at the molecule, they do not change the coordinates.

This behavior is the default behavior, you can change what the right mouse button does using the Preferences.

.. rst-class:: steps

  \
    | Click once somewhere in empty space to make sure nothing is selected
    |
    | Click with the left mouse button, and drag:
    | your molecule will rotate
    |
    | Click with the left mouse button with the ctrl-key, and drag:
    | your molecule will rotate in-plane
    |
    | Click with the right mouse button, and drag:
    | your molecule will be translated
    |
    | Click with the right Middle button (if available), and drag up and down:
    | you will zoom closer to or away from your molecule
    |
    | (not on windows) Click with the left mouse button with the alt-key, and drag:
    | (not on windows) you will zoom closer to or away from your molecule
    |
    | Use the mouse wheel, if you have one:
    | you will zoom closer to or away from your molecule
    |
    | Using all these options, try to position the ethanol as in the following figure:


.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ethanol-top.png
  :align: center

Save picture
^^^^^^^^^^^^

You can save a picture of your molecule using the  'Save Picture ...' command from the File menu.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-SavePicture.png
  :align: center

The format used is the PNG format. You can change this using the **File → Picture Format** menu command. You can also change the resolution. A smaller resolution will result in a smaller file, but will reduce the quality.

Via the Preferences command it is possible to save your preferred format.

.. rst-class:: steps

  \
    | Select the **File → Save Picture ...** command
    | Enter the name for your picture: ethanol
    | Click the 'Save' button

A picture will be saved to disk containing the figure of your molecule. Only the  drawing area is saved in the picture, not all the input.


.. tip::

    The format used is the PNG format.
    You can change the resolution. A smaller resolution will result in a smaller file, but will reduce the quality.

    Via the Preferences command it is possible to save your preferred format (PNG, JPEG, TIFF, BMP or PostScript)

Molecular conformation
----------------------

Rotate such that you look along the C-C axis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rst-class:: steps

  \
    | Rotate your molecule into the following position:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ethanol-top.png
  :align: center

Select the top CH3 group
^^^^^^^^^^^^^^^^^^^^^^^^

.. rst-class:: steps

  \
    | Click once on the top carbon atom
    | Use the **Select → Select Connected** menu command

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-top-selected.png
  :align: center

As you will notice, all atoms directly connected to the selected atom are added to the selection. Alternatively, you can also make a selection by shift-clicking on the elements you want to select.

.. rst-class:: steps

  \
    | Click in empty space
    | Click on the top carbon atom
    | Shift-Click once (without moving) on each of the top hydrogen atoms

This has almost the same effect (in this case you have not selected the second carbon atom).

Rotate the selection
^^^^^^^^^^^^^^^^^^^^

We are now trying to make an eclipsed geometry.

.. rst-class:: steps

  \
    | ctrl-Click with the left mouse button **in one of the selected hydrogens**,and drag around to rotate the selection in-plane
    | Rotate the hydrogen atoms in an almost eclipsed position

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-top-eclipsed.png
  :align: center

You can move the selection by clicking in a selected object, and dragging with  the mouse. All usual operations are possible: rotate, rotate in-plane, translate  and zoom. Zoom in this case means moving the selection perpendicular to the screen.

In the status field you see the current rotation angle.

You have to click and start dragging at a selected item. If you click and drag in space you will move the entire molecule.

Back to Staggered Geometry
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rst-class:: steps

  \
    | Click in empty space to clear the selection
    | Click on the pre-optimize button |PreOptimTool|

The optimizer will bring the structure back to the original staggered geometry. If it does not complete, repeat this step until it does.

Getting and setting geometry parameters
---------------------------------------

Bond length
^^^^^^^^^^^

First select the oxygen atom and the connected hydrogen atom.

This time we make the selection by dragging a rectangle around all objects that we want to select.

.. rst-class:: steps

  \
    | Using the left mouse button together with the shift key, drag a rectangle around the oxygen and hydrogen atom

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-top-rectoh.png
  :align: center

.. rst-class:: steps

  \
    | Release the mouse button (and the shift key)

The oxygen atom and the hydrogen atom are selected.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-top-ohsel.png
  :align: center

In the status area you see the distance between the selected atoms, information about the bond, and a slider.

You can set the distance to any value you wish by editing it, or (most conveniently) by using the slider.

.. rst-class:: steps

  \
    | Use the slider to move the H atom

.. tip::

    The order in which you have selected the atoms is shown with numbers.
    By default, the last atom selected will will be in the group of atoms to move.

    Press the **control key while using the slider**, and the **smallest group of atoms** will move.

Bond angle
^^^^^^^^^^

.. rst-class:: steps

  \
    | Select first one of the top hydrogens by clicking on it
    | Next, extend the selection (shift key) by clicking on the top carbon atom
    | Finally, extend the selection (shift key) by clicking on another top hydrogen atom

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-top-hch-sel.png
  :align: center

In the status area information about the bond angle of the selected three atoms is given, and the slider is again visible. You can change this value to a value you like, most conveniently using the slider.

Dihedral angle
^^^^^^^^^^^^^^

By selecting four atoms we get information about the dihedral angle. And of course you can also change it, again most conveniently using the slider.

.. rst-class:: steps

  \
    | Move the molecule such that you can see all atoms
    | Select first one of the top hydrogens by clicking on it
    | Next, extend the selection (shift key) by clicking on the top carbon atom
    | Next, extend the selection (shift key) by clicking on the next carbon atom
    | Finally, extend the selection (shift key) by clicking on the oxygen atom

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-top-occh-sel.png
  :align: center

Coordinates
^^^^^^^^^^^

To view the coordinates we have to go to a different input panel. The input panels can be selected using the panel bar on the top of the input panels, the right half of the window.

.. rst-class:: steps

  \
    | In the right side of the AMSinput window:
    | Click on the **Model** tab in the panel bar
    | Select the **Coordinates** command

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-coords.png
  :align: center

You get a list of all Cartesian coordinates. They will be updated in real time when you make changes to the molecule, and you can also edit the values yourself. In that case, the picture of the molecule will be updated automatically.

Note that some atoms are highlighted. These are the currently selected atoms.

The Move Atom(s) buttons (the arrows) will move the selected atoms up or down. In this way you can re-order the atoms.


Extending and changing your molecule
------------------------------------

Before making some changes, let's re-optimize. We first select the 'Main' panel so the coordinates will not be visible during the pre-optimization. Otherwise this may slow down the pre-optimization.

.. rst-class:: steps

  \
    | Click on the "Main" tab
    | Click in empty space to make sure nothing is selected
    | Click on the pre-optimize button |PreOptimTool|

Let's try to change the CH2OH group in a COOH group.

Thus, we need to:

+ remove one hydrogen
+ change one hydrogen into an oxygen
+ change a single bond into a double bond

After this, we will revert to the ethanol molecule.

Delete an atom
^^^^^^^^^^^^^^

First: delete one hydrogen

.. rst-class:: steps

  \
    | Click in empty space to clear the selection
    | Click once on the hydrogen to delete, it will be selected

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ch3ch2oh-hsel.png
  :align: center

.. rst-class:: steps

  \
    | Press the backspace key

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ch3choh.png
  :align: center

The selected atom is removed.

Change the type of an atom
^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, we will change a hydrogen into an oxygen atom

.. tip::

    You can quickly select a tool using the C, O, H, N, S, P, or F keys.

    Or use X, type one or two letters, and Return, for any element.

.. rst-class:: steps

  \
    | Select the O-tool (or press the 'O' key)
    | Double-click on the hydrogen that should change into an oxygen

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ch3co-oh.png
  :align: center

Change the bond type of an existing bond
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now the oxygen atom is singly bonded to the carbon, we need to change this into a double bond.

.. rst-class:: steps

  \
    | Click on the bond between the carbon and the new oxygen
    | Use the **Bonds → Bond Order → Double** menu command (or just press the '2' key)

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-single-to-double.png
  :align: center

The single bond has changed into a double bond.

Another way to modify a bond type is to click on the bond once which will select this bond.  Then click on the bond tool in the menu bar ('ball and stick' logo to the right of the start), and select the proper bond type.

.. tip::

    Use the keyboard shortcuts: select a bond, press 1 for a single bond, 2 for a double bond, 3 for a triple bond and 4 for an aromatic bond.

To get a reasonable geometry optimize the structure:

.. rst-class:: steps

  \
    | Click in empty space to deselect the bond
    | Click on the pre-optimize button |PreOptimTool|
    | If not converged, press pre-optimize again

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ch3cooh.png
  :align: center

Add new (bonded) atoms
^^^^^^^^^^^^^^^^^^^^^^

Now, to revert to the ethanol molecule, we first remove the new doubly-bonded oxygen atom, and then add one hydrogen atom.

.. rst-class:: steps

  \
    | Click once on the doubly-bonded oxygen atom to select it
    | Press the backspace key to delete it
    |
    | Select the H-tool (or press the 'H' key)
    | Click once on the carbon atom connected to the oxygen

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ch3coh.png
  :align: center

Note that this way you started bonding mode again, as indicated by the bond to the mouse position.

.. rst-class:: steps

  \
    | Click once in empty space to make a hydrogen atom (connected to the carbon!)
    | Click once **on the just created** atom to stop bonding
    |
    | Repeat this to add a second hydrogen to the carbon atom
    |
    | Pre-optimize the molecule

For the next step, we want to find the optimal geometry of a local minimum, for this

.. rst-class:: steps

  \
    | While holding shift select the top carbon, next carbon, oxygen, and its hydrogen in that order
    |
    | Use the slider at the bottom to set the dihedral to 180.
    |
    | Deselect all atoms.
    |
    | Pre-optimize with the gear button

Make sure the O-H bond remains parallel to the C-C bond, or repeat this process.

.. warning::

    The results in the next section may look slightly different for other energy minima.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-2-ethanol.png
  :align: center

Once again you have created an ethanol molecule.

.. tip::

    The pre-optimizer will optimize the positions of the selected atoms only, if any.


.. warning::

    Make sure you have no or all atoms selected if you wish to pre-optimize all atoms in your system.


Step 3: Select calculation options
==================================

Task
----

ADF has many different modes of operation.

.. seealso::

  `Tasks section <../../AMS/Tasks/TOC.html>`__  of the AMS driver manual.


So to optimize the geometry of the ethanol molecule we choose the geometry optimization task:

.. rst-class:: steps

  \
    | Select **Geometry Optimization** from the 'Task' menu

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-3-GeOpt.png
  :align: center

After selecting a task the AMS-GUI loads a preset that adjusts input fields needed for this particular task.
You can easily see what fields have been updated by a preset: they are colored green.

Check the `GUI presets <../../GUI/Presets_and_Defaults.html>`__ documentation for more information about presets.

XC functional
-------------

An important input option is the `XC functional <../../ADF/Input/Density_Functional.html>`__ to use.

For this tutorial the default functional during the SCF is sufficient. So just leave this at the default value.

.. tip::

    You really should select a good XC functional (and basis set) to get accurate results.

Basis set
---------

With the Basis Set pull-down menu you select the basis set you want to use.

The menu gives access to the `Basis Sets <../../ADF/Input/Basis_sets_and_atomic_fragments.html>`__ regularly used.

For this tutorial we will choose a very small basis set. This will yield less accurate results, but the calculation runs much faster. Obviously, if you want more accurate results you should use a better quality basis set. Thus:

.. rst-class:: steps

  \
    | Select 'SZ' from the 'Basis Set' pull-down menu

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-3-basisset.png
  :align: center

.. tip::

    Colors of input field: changed by preset (green), by user (yellow), by both (red)


Numerical quality
-----------------

The ADF program uses a numerical integration scheme for virtually everything it may calculate. A numerical integration scheme generates some kind of grid (and corresponding weights). The default integration method in ADF (and BAND) is the so called Becke Grid.

Another technical detail is that a density fitting method is used, for computational efficiency. The spline Zlm fit is the default fit method (the old slater type fit is still available).

With the Numerical quality option you can select the quality of both the Becke integration and the spline Zlm fit at the same time.

Increasing the quality makes the results more accurate, but will require substantially more computation time.

Similarly, decreasing the quality will result in less accurate results, but you may get results faster.

The default value will in most cases be fine, certainly for this tutorial. If you go to the Details section (click on the ...) you can set details of the integration scheme and fit method. However, the Numerical quality option in the main panel is the most convenient way to select the quality.


Geometry Convergence
--------------------

.. rst-class:: steps

  \
    | Click on the |MoreBtn| button next to the Task

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-3-GeometryConvergence.png
  :align: center

In this panel you can see the details of the geometry optimization, like the maximum number of iterations and the convergence thresholds.

.. tip::

    Click on a unit to change the unit, your choice will be remembered.

    Use the GUI Preferences to reset all units to the default values.

As the current set up is fine, go back to the main panel:

.. rst-class:: steps

  \
    | Click the 'Main' button in the panel bar


Other input options
-------------------

The panels on the right side contain many more input options. You select a panel with the menus in the panel bar, or by searching for a particular option. When searching for an option, any text in the panels will match, as well as from the help balloons. Also the corresponding ADF input keys will match.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-3-panelmenu.png
  :align: center

The menu items use a color coding to show you which panels have been affected by a preset (green), by the user (yellow), or both (red).

As we will not do anything special right now, you do not need to change anything in other panels.


Step 4: Run your calculation
============================

Save your input and create a job script
---------------------------------------

Finally you will want to save your input.

.. rst-class:: steps

  \
    | Select the **File → Save** command
    | Make sure you select the Tutorial directory that we made
    | Enter the name 'ethanol' in the Filename field

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-4-save.png
  :align: center

.. rst-class:: steps

  \
    | Click on Save

Now you have saved your current options and molecule information. The file will automatically get the extension '.ams'.

AMSinput has also created a corresponding script file. This script file has the same name, but with an extension '.run' instead of '.ams'.

In the AMSjobs module you can see what files have been created:

.. rst-class:: steps

  \
    | Click once in the AMSjobs window to activate it
    | Click once on the triangle in front of the name of the job (ethanol)

You will see the .ams and .run files, and a .pid file that AMSjobs uses to store information. You might also see the picture that you saved, if you used the name 'ethanol' for it. Only the extensions are listed, so the real filenames are ethanol.ams, ethanol.run and ethanol.pid. Notice the job status icon (the open circle on the right) that AMSjobs uses to indicate a new job.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-4-ethanolfiles.png
  :align: center

Run your calculation
--------------------

To actually perform the calculation (the geometry optimization of the ethanol molecule), use the **Job → Run** menu command in AMSjobs:

.. rst-class:: steps

  \
    | Make sure the ethanol job is selected in AMSjobs (it is if you followed the tutorial)
    | Select the **Job → Run** command

This will execute the run script that has just been created. If you have never made changes in the AMSjobs setup, the default behavior is to run the job in the background on your local computer, using the Sequential queue. This queue will make sure that if you try to run more then one job at the same time, they will be run one after another.

Once your job starts running, AMSjobs will show the progress of the calculation: the last few lines of the logfile:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-4-statusrunning.png
  :align: center

Note that while running, the job status symbol in AMSjobs changes.

If you wish to see the full logfile while the calculation is running, just click on the logfile lines displayed in the AMSjobs window:

.. rst-class:: steps

  \
    | Click on the logfile lines in the AMSjobs window

Now the logfile is showing in the AMStail window:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-4-amstail.png
  :align: center

Step 5: Results of your calculation
===================================

Logfile: AMStail
----------------

The logfile is saved and extended by ADF as it is running. Normally it is most convenient to view it only in the AMSjobs window to prevent screen clutter.

Right now it is already showing in the AMStail window, and in the AMSjobs window, but you could have used any text editor.

Wait for the calculation to finish:

.. rst-class:: steps

  \
    | Wait until AMStail shows 'Job ... has finished' as last line
    | In the `dialog that pops up <../../GUI/Update_geometry_results_from_finished_calculation.html>`__, click 'Yes' to update the geometry

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-updcoords.png
  :align: center
  :width: 60%

Now close AMStail by using the **File → Close** menu command:

.. rst-class:: steps

  \
    | In the window showing the logfile (the AMStail window):
    | Select the **File → Close** command

In the AMSjobs window, note that the job status icon has changed to indicate that the job is ready:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-statusready.png
  :align: center

Files
-----

ADF has created a couple of data files and a couple of text files.  You can check this in the AMSjobs window:

.. rst-class:: steps

  \
    | Click on the AMSjobs window

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-statusready.png
  :align: center

Note that the Local files are visible because earlier in the tutorial you already clicked on the triangle opening the details for this job.

The .ams file is the input as saved by AMSinput.

The .run file is the run script, also saved by AMSinput.

.. tip::

    To change the .run file (if your really must ...), use the 'Run Script' panel in AMSinput (in the Details section). Your changes will be saved in the .ams file.
    If you make changes to the .run file itself they will be overwritten next time you save the job with AMSinput.

The .pid file is a file that contains your job status and configuration. It is used by AMSjobs.

The other files are produced by ADF. The .err file contains error messages, the .logfile shows the progress of the calculation, the .out file is the main (text) output file, and the other files are binary files that store results of the calculation.

Geometry changes: AMSmovie
--------------------------

ADF has optimized the geometry, and we can use the AMSmovie module to visualize the progress of the optimization. So let's start AMSmovie using the SCM menu in your AMSinput window:

.. figure:: /Images/GeometryOptimizationOfEthanol/SCM-menu.png
  :align: center

.. rst-class:: steps

  \
    | Select the **SCM → Movie** command in AMSinput
    | Press the Play button (the right pointing arrow)

.. tip::

    Press the space bar to start/stop playing in AMSmovie

The AMSmovie module will display a movie of the geometry optimization.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsmoviegraph.png
  :align: center

.. tip::

    Use the slider to quickly move through the frames.

    Use the left and right arrow keys to single step through the frames.

You control playing with the buttons. When your mouse pointer is above any of the buttons, and not moving, a balloon will pop up showing what that particular button will do.

The graph on the right-hand side shows the energy as function of the geometry step.

You can show several graphs for different properties at the same time:

.. rst-class:: steps

  \
    | Use the **Graph → Add Graph** menu command
    | Select two carbon atoms by shift-clicking on them
    | Use the **Graph → Distance, Angle, Dihedral** menu command

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsmoviegraph2.png
  :align: center

Now you have two graphs. One of them is the 'active' graph. When you make a new graph it will always be the active graph. You can also make a graph active by clicking on it.

When you select a property from the Graph menu (Energy, Distance and so on) that property will be plotted in the active graph.

You can also have multiple curves in one graph, if possible: one property per Y-axis. You may have several curves on the same Y axes if they are using the same unit (all Angstroms for example):

.. rst-class:: steps

  \
    | Select two carbon atoms and one oxygen atom by shift-clicking on them
    | Use the **Graph → Distance, Angle, Dihedral** menu command

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsmoviegraph3.png
  :align: center

Another feature is that you can click on a point in one of the graphs. It will be marked, the movie will jump to that particular step, and if you have more then one graph the corresponding point(s) will also be marked in the other graphs.

To rotate, translate, or zoom the picture, use your mouse, just as in AMSinput.

.. rst-class:: steps

  \
    | Use the slider to go to a frame in the middle of the optimization

Selecting atoms provides information about atoms, bonds, etc. in the information field below the molecule editor pane.
The information will be updated when you go to another point in the movie (a different geometry). You can see examples of these in the pictures above.

You can also show this information in the 3D window:

.. rst-class:: steps

  \
    | Use the **View → Geometric Info → Angle** menu command

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsmovie-angle-3D-menu.png
  :align: center

The angle will be visually added to your molecule :

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsmovie-angle-3D.png
  :align: center

.. rst-class:: steps

  \
    | In the AMSmovie window: select **File → Close**

Orbital energy levels: AMSlevels
--------------------------------

.. rst-class:: steps

  \
    | Select your job in the AMSjobs window by clicking on the job name
    | Select the **SCM → Levels** command

.. tip::

    In AMSjobs right-click on a job name to go quickly select it **and** show the SCM menu

AMSlevels will start and show a diagram of the energy levels of the ethanol molecule.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amslevels-inter.png
  :align: center

In the diagram you can see from what fragment types the molecular levels are composed.

.. rst-class:: steps

  \
    | Move the mouse around, above different levels, without clicking

Balloons will pop up with information about the level at the mouse position: The MO number, eigenvalue, occupation, and how it is composed of SFOs (fragment orbitals).

.. rst-class:: steps

  \
    | Click and hold on the HOMO level of the molecule

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amslevels-popup.png
  :align: center

.. rst-class:: steps

  \
    | In the pop-up that appears, select 'Show Labels'
    | Click and hold on the HOMO of the O fragment type
    | In the pop-up, select 'Show Labels'

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amslevels-labels.png
  :align: center

The labels of the orbitals may be different as they depend on the symmetry of your molecule.

To actually see the orbital, select the orbital from the top of the pop-up menu:

.. rst-class:: steps

  \
    | Click and hold on the HOMO level of ethanol
    | Select the '10A' command (or similar depending on the symmetry)

A window with a picture of the orbital should appear.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amslevels-orbital.png
  :align: center

You can move (rotate, translate and zoom) the orbital with your mouse.

.. rst-class:: steps

  \
    | Close the window showing the orbital: **File → Close** (in the window displaying the orbital)

Electron density, potential and orbitals: AMSview
-------------------------------------------------

.. rst-class:: steps

  \
    | Select **SCM → View**

AMSview will start up and show a picture of your molecule:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsview-startup.png
  :align: center

You can use AMSview to visualize all kinds of 'field' related properties: densities, orbitals, potentials, etc. You actually have already used it before: the picture of the orbital that was created using AMSlevels was shown by AMSview.

Use the mouse to rotate, translate or zoom, as in AMSinput.

In the Properties menu there are some pre-defined things to visualize: density, spin-density, HOMO, LUMO and more. If you select one of these, you will see the corresponding item immediately. However, AMSview can do much more and gives you lots of control.

For example, lets show a density isosurface, colored by the electrostatic potential:

.. rst-class:: steps

  \
    | Select the **Add → Isosurface: Colored** command

Below the picture a control line will be created. AMSview creates one such line for all visual items and special fields (surfaces, cut planes, calculated fields, etc.) that you add.

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsview-control.png
  :align: center

In this particular case the control line contains two pull-down menus that you use to select the fields that you want to visualize.

.. rst-class:: steps

  \
    | From the first pull-down menu in the control line, select **Density → Density SCF**

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsview-pulldown.png
  :align: center

.. rst-class:: steps

  \
    | From the second pull-down menu in the control line, select **Potential → Coulomb Potential SCF**

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsview-denspot.png
  :align: center

To demonstrate some other possibilities of AMSview, do the following:

.. rst-class:: steps

  \
    | Select the **Properties → HOMO** command
    | Click on the leftmost check box in the FIRST control line to hide the density
    | Rotate the molecule to get a good view

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsview-orbital.png
  :align: center

.. rst-class:: steps

  \
    | Select the **Add → Cut Plane: Colored** command
    | In the new control line, press on the pull-down menu and select **Density → Density SCF**
    | Click the check box in front of the 'Isosurface: With Phase' line to hide the HOMO
    | Select the Carbon and Oxygen atoms (three atoms)
    | Click the 'with atoms' button next to the 'Position plane' option (thus the button, not the check box)
    | Click the check box in front of the 'Isosurface: With Phase' line to show the HOMO
    | Select the **Fields → Grid → Medium** command
    | Click Yes to recalculate the fields
    | Rotate your molecule to get a good view

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-amsview-colcut.png
  :align: center

You can save the picture you create using the Save Picture menu command:

.. rst-class:: steps

  \
    | Select **File → Save Picture ...**
    | Enter the name (without extension) of the file you want to create
    | Click Save

A picture with the (file)name you specified has been created.

You might want to explore some more of the possibilities of AMSview on your own. Many different properties can be visualized as you probably have noticed in the pull-down menus.

Browsing the Output: AMSoutput
------------------------------

The output file (tutorial.out) is a plain text file. You can view it with your favorite text editor (or text viewer). You can also use the AMSoutput GUI module which provides a convenient way to check the results:

.. rst-class:: steps

  \
    | Select the **SCM → Output** command
    | Select the **Properties → Bonding Energy Decomposition** command

The AMSoutput program will start showing the results of your calculation, and via the menu you jumped to the first section with geometry details:

.. figure:: /Images/GeometryOptimizationOfEthanol/t1-5-bob.png
  :align: center

You can use the menus to go to different parts of the output file, or you can just use the scroll bar. If a menu option is shaded, this means that no corresponding section of the output is available.

.. tip::

    Click text highlighted in blue to jump to the next section with the same title, if present.

.. tip::

    Use the search box at the bottom of the AMSoutput window (cmd/ctrl-F)

Convert results to spreadsheet (.xlsx)
--------------------------------------------

..
   the spreadsheet steps are not recorded

You can also export the results of a finished calculation to spreadsheet
(.xlsx) format, that you can open in e.g., Microsoft Excel or LibreOffice Calc.

.. rst-class:: steps

  \
    | In AMSjobs select your job and choose **Tools → Build Spreadsheet**.

Only the most common types of results are exported to the spreadsheet. For
example, general information about the system, the orbital energies, and the atomic
positions and atomic charges. For a full list, the `spreadsheets documentation <../../GUI/Spreadsheets_xlsx.html>`__.

.. figure:: /Images/GeometryOptimizationOfEthanol/ethanol_general_sheet.png
   :align: center

.. figure:: /Images/GeometryOptimizationOfEthanol/ethanol_orbitals_sheet.png
   :align: center



Close all open GUI windows
------------------------------------------

As we are now done with tutorial 1, close all windows that belong to this tutorial:

.. rst-class:: steps

  \
    | Select the **SCM → Quit All** command in any AMS-GUI window

All open windows from the AMS-GUI will be closed.

