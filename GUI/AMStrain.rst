.. _metatag ADFTRAIN: 

AMStrain
########

General
*******

Overview
========

AMStrain is a graphical user interface (GUI) to handle Training sets and ReaxFF force field files.

When optimizing a a force field, one has to define a training set and initial force field file, and decide on what parameters to optimize (and in what range).

AMStrain shows you the training set and force field, and allows you to make adjustments:

- adjust the training set (new systems, remove systems, define what to include in the objective function, weights, etc.)
- adjust the force field (add or remove terms, initial values for parameters, optimization details)

After saving, you will have a trainset.in and geo file. These define the training set.
You will also have a ffield and params file. These define the force field and how to optimize it.

The next step would be to actually optimize the ffield, using all these files as input.
That is currently not handled by AMStrain.

Finally, the results of the training (new ffield and fort.99) can be shown with AMStrain.
The fort.99 contains the contributions to the objective function, and they will be shown together with the training set.

Based on the results, one can adjust the optimization: improve the training set, or focus on other parameters of the ffield to optimize.


File handling
=============

Open
----

Use the Open command in the File menu to open a specific file. Alternatively, one can start AMStrain via the command line and specify the file to open as argument.

The current setup will be cleared (that is, the New command is automatically used).

AMStrain will try to determine what kind of file you have selected to open. Possible options are a trainset.in file (must be named trainset.in), a geo file (either named geo or with the .bgf extension), a force field file (named ffield or with the .ff extension), or a params file (must be named params).

The names of the other files to open are the default names (trainset.in, geo, ffield, params and fort.99) in the same directory as the file you selected to open.

Add
---

When using the Add command in the File menu, the selected file will be added to the current AMStrain window.
Only the selected file will be imported, and you can add only trainset.in, geo or ffield files.

Save
----

First it will be suggested to save with the same names as has been used while opening.

If you do not like that (probably you want to save your original files), click 'No'.
You will be asked to select a directory in which to save the files. All files will have their default names.

Tables
======

Both the training set and force field are shown as a table.

Header menus: sort and filter
-----------------------------

On top of the tables is an header. 
All the items in the header are pull-down menus, you can use them to sort the table (by the values in the corresponding column).

The left-most item in the headers are 'Type' menus. They offer the same sorting options, but you can also filter by specific types.
You can select which types of data to show, one or more types, or all.

Search
------

Both tables have a Search field on the bottom. Use cmd/ctrl-F to go there, or click in the field. 
While you type, the data shown in the corresponding table will automatically be filtered by whatever you type.
The spaces in your search string will automatically be replaced by wild-cards.

Selection
---------

To make selections in the tables use your mouse. 

In the training set table you may click anywhere, in the force field table click somewhere in the left two columns to make a selection.

|  Left click: set the selection to the clicked line,
|  Shift-left click: extent the selection up to and including the clicked line,
|  Control-left or right click: toggle the clicked line in/out the selection.
|  
|  The backspace key: delete the selected lines.
|  The Escape key: clear the selection.

All lines in the training set correspond to one or more systems (molecules). If only one system is selected (or multiple lines with the same system) it is displayed on the left. When a single line with an Energy term is selected, all systems in that energy expression are shown on the left. Use your arrow keys (left and right) to go through the different systems in the energy expression.

You can move the selected line in the tables using up and down arrow keys. 

Training set
************

Systems
=======

A training set needs one or more systems. A system is a molecule or a crystal, together with details on how to run a calculation with it.
So it might be a single point calculation, a geometry optimization, with extra details (like constraints, maximum number of geometry iterations, ...).

If you select a System line, and if it is the only selected system, the molecule will be shown on the left.

You can use the commands in the View menu to change details of what is shown on the left, just as in other ADF-GUI modules.
Of course you can use the mouse to rotate, zoom, and select atoms.

Systems cannot be created inside AMStrain, they are imported from various sources:

- AMStrain: select a file to import, all formats that the ADF-GUI can read are supported (for example .ams, .xyz, .bgf, .sdf, .pdb, but also result files like .t21, .rkf etc)
- AMSinput: use the 'Add Coordinates To AMStrain' menu command (in the File menu)
- AMSmovie: use the 'Add Coordinates To AMStrain' menu command (in the File menu) to add the current frame to AMStrain. Note you can do this repeatedly, for any frame you like to use as a test system
- AMSjobs: select one or more jobs, and use the 'Add To AMStrain' menu command (in the File menu). In this case the selected job(s) is (are) added, not just the coordinates. AMStrain will try to handle the job as best as it can. For example:

  - when adding a Linear Transit or PES Scan job AMStrain will convert it into a series of geometry optimizations with constraints, and will also add Energy entries to match the corresponding LT/PES.,
  - jobs using SDF files will be added using all entries of the SDF file as a separate system.

Shortcut: cmd/ctrl-T  (in AMStrain, AMSinput, AMSmovie and AMSjobs).

In a system line in the training set table you can see the details of the system:

- SystemID,
- Runtype (with possible extra details),
- File from which the current system is used.

More information can be seen by moving your mouse over the line, and keep it there without moving. A balloon will popup with details.

When saving your setup, the systems are saved in BGF format, in a file called geo or in a .bgf file selected by you (via the Open command).

Currently ReaxFF has a restriction that SystemIDs may have at most 20 characters.
To make renaming your SystemIDs easier, there is a menu command 'Change SystemIDs' in the 'Training Set' menu.
Use this command to replace some text in all of your selected Systems (or all systems if none are selected) at once with some other text.
You will be asked for a string to search for, and for a string to replace it with. 

The 'Smart System Status' will adjust the status of all systems: if a system is used, the status will be active, if a system is not used the status is disabled.

Training set
============

A training set also defines the objective function that will be minimized with the parameter optimization.
The objective function consists of many terms, each line in the table is one term (with the exception of comment lines and system lines).

To add terms to your training set, use the Add menu. Typically the selected systems and the selected atoms are used when adding terms.

As an example, to add a distance terms to your training set:

1. select the system for which you want to add a distance term,
2. select two atoms in the system,
3. use the Bonds command from the Add menu.

One distance term will be created in your training set. Obviously, when you are going to use a distance term your system will need to be a geometry optimization. If it would be a single point calculation, the distances will always remain the same so this term would just be a constant (probably zero).

The atom selection determines what distance terms are added:

- If no atoms are selected (thus step 2 is skipped), all bonds found in the system will be added.
- If two atoms are selected (as in the example): the distance between those atoms will be added (even if they are not bonded directly).
- If more than two atoms are selected: all selected bonds in the system will be added (thus existing bonds between selected atoms).

If more than one system is selected, the above is repeated for all selected systems.
The atom selection criterion will still be used, note that this makes no sense if the systems do not have the same atoms in the same order.
This way of handling the atom selection is used for all geometric tests.

In the distance term line you can see:

- the Type ('Geometry: distance'),
- the systemID (some name, identical to the name of the selected system),
- the Accuracy (inverse of weight factor, to set the relative contribution of this term to the objective function),
- the Details (the atom numbers and atom types involved in this particular distance),
- the Value (the reference value, calculated using the current system),
- the Error (when opening a training set after optimizing, the actual contribution to the objective function of this term).

The Error column will be filled with results from the training (read from a fort.99 file). 
It shows the contribution to the objective function for each term in the training set. It is especially convenient if you sort by this column.

Term types that can be added are evident from the Add menu:

- distances (Bonds)
- angles
- dihedrals (Torsions)
- several types of charges
- energy expression
- energy curve
- force
- heat of formation
- cell parameters

An energy curve is special: select two or more systems, and use the Energy Curve command.
This will add a set of energy records, one for each system, that test the energy differences between the selected systems.
All differences will be with respect to the system with the lowest energy.

You can also add Comments, which are added just before the selected line. 
They are attached to that selected line, which is important when you are sorting the training set table.

When saving your setup, the systems are saved in a file called 'trainset.in'.


Mouse interaction
=================

In addition to the general mouse interactions for selection (already mentioned):

- Double click item to edit
- Right click on system
- Mouse over to see details, error info etc (you will get a popup if you do not move the mouse).

Editing
=======

To edit something, double click on it (or single click on a selected item).
Next you can edit it in place, or in a window that appears.

Depending on what you are editing, the changes you make will be applied to the full selection!
So when selecting multiple terms and editing the Accuracy, that field will be set for all your selected items.
Similar, when changing runtype options, like runtype or maximum number of iterations, it applies to all selected systems. 
Constraints are not propagated as they depend on a particular system.

When editing SystemIDs, you can use the tab key to cycle through all SystemIDs matching what you have been typing.
Add a space to use the current suggestion, or type more letters to narrow the search down.
This works when changing SystemIDs as well as when editing energy expressions.

When you edit the runtype (double click on the Details field of a system), a window will appear that enables you to select the runtype and a couple of options. You can also add or remove constraints in this window. If you have made changes that are not visible in the Details field (like constraints), this will be graphically indicated. 

Show
====

In the Show menu you can choose if you want to show comments, active or disabled items.
With the Activate and Disable commands in the Training Set menu you can make an item active or disabled.

A disabled item will still be saved to the trainset.in file, but it will be commented out (with a special comment to distinguish it from a comment line).

In the table the lines can have different colors:

- Yellow background: selected
- Light red background: warning or error
- Red background: warning or error AND selected
- Gray foreground and background: disabled
- Gray foreground, light yellow background: disabled AND selected

This should be intuitive, if you remember yellow for selected, and red for warnings/errors.


Warnings and errors
===================

If you hover with your mouse over a red line you will get extra information on why it is red, what kind of error.

For example, checking a distance for a system which is not optimized is useless, or having systems that are not used in any term.
For energy expressions there is a check that the stoichiometry is correct (thus the net amount of all atom types should be zero).

Disabling an item makes it unavailable, thus for error testing this is the same as the item not being present at all.

You can also detect duplicate lines using the Duplicates command in the Show menu. 
They will also be marked as warning/error. This option is not on by default as it may be slow for big training sets.

You can use the 'Select All Not In Force Field' command in the Training Set menu to select all items in the training set that have specific atoms mentioned (geometry tests, charges, etc), and where the corresponding explicit term is not present in the Force Field.
So when you select a C-H distance in the training set, and the Force Field does not have any C-H bond records, that line will be marked in the training set. It is up to you to consider if extra entries in the Force field are required.

In the Force Field menu there is a similar command to select force field entries that are not in the training set.

Reference data
==============

Generating reference jobs
-------------------------

Use the 'Generate Ref Jobs...' command from the 'Training Set' menu to generate reference jobs for your selected systems.

You will first be asked to select an example job. This is an .ams file created with AMSinput, which has the calculation setup you want to use.
That may be using ADF, DFTB, etc., with basis, parameters and all other options as you like.

Next you need to select a directory in which the reference jobs are created.

Once they are created they are also added to AMSjobs (visible if you have AMSjobs open).

Running reference jobs
----------------------

To run the reference jobs, use AMSjobs (just select the jobs and use the Run menu command).
With AMSjobs you can also decide to run these jobs on some other computer system.

Importing results from reference jobs
-------------------------------------

Use the 'Get Data From Ref Jobs' menu command from the 'Training Set' menu to update all selected items in the training set with data from the reference jobs (if they are available). If you have no selection, all items in the training set will be updated.

Force field
***********

Type: lgDispersion, ACKS2 or eReaxFF
=====================================

If your force field uses lgDispersion, ACKS2 or eReaxFF you need to specify this.
To do this, use the Type command in the Force Field menu. 

You can turn on or off each of these options as you like. When using eReaxFF, ACKS2 will always be turned on automatically.

The type of force field (especially lgDisperion) determines how many parameters are saved to the force field file.

Force field parameters
======================

For a description of the records in the force field file, please check the ReaxFF documentation.
They should be self-explaining as presented in AMStrain.

Note that when you hover with your mouse over a parameter value, a balloon will appear with the long name of that parameter, and with statistical information collected from all force fields in the force field directory.


Adding records
--------------

In the Force Field menu you will find many commands like 

- Add xxx (Training Set)

These will add an xxx record (Atom, Bond, Angle etc) for each matching item in the Training Set.
Thus, if the Training set has a 'Geo: distance' term for atoms C-H, a Bond C-H record will be added to the force field.
Records already in the force field will not be added again.

Only the selected lines in the training set will be considered, if no selection the full training set will be considered.

- Add xxx (All)

These commands will add all possible Atoms, Bonds etc that can be made by combining the atoms types found in the training set.
The selection in the training set is ignored.
Records already in the force field will not be added again.

- Add Any...

This command will show a window where you can select what to add.
You need to specify a type, and an atom string (something like H-C-H).
You have the option to explicitly allow duplicate records (sometimes needed for angles or torsions).

The atom string may use some special characters: 

- a '*' to match anything (will also be a wildcard in the force field file)
- a '#' to loop over atom types in the force field file
- a '@' to loop over atom types in the training set

So:

1. Add Any Torsion H-C-O-N
2. Add Any Bond #-#
3. Add Any Angle #-#-#
4. Add Any Torsion #-#-#-#

will result in a force field file with many records, all combinations of H, C, O and N.
This will be too much for a good force field, and also the Off-diagonal an Hydrogen bond records need to be considered.


The Force Field menu also has a command 'Select All Not In Training Set'.
For each line in the force field file, the corresponding geometric tests are searched for in the training set.
Thus is you have a Bond C-H line in the force field, this command will check if some Distance C-H occurs in the training set.
If not, the line in the force field is selected.
This is just a convenience feature, it is possible that lines are used for example in energy expressions and not in geometric tests.
It is up to you to consider to add extra terms to the training set, or to remove lines from the force field, or leave things as they are.

Editing parameters and optimization details
-------------------------------------------

When adding record to the force field file, values need to be specified for all parameters.
The values used by AMStrain are the values reported by rxffutils. These are the average values of a specific parameter in all force fields in the force field directory. For reasonable values you probably need to set up your own force field library (the default is the collection of all ReaxFF force fields distributed with our software).


With the 'RXFFUtil Options...' command in the Force Field menu you can set the options to use with the RXFFUtil program, especially the force field directory. For more info about rxffutil see the ReaxFF documentation.

For the force field optimization not only the parameters need a value, you also need details like the allowed range for a parameter, a delta per parameter, and a flag to indicate if a specific parameter needs to be optimized.

Select one or more parameters using Left Click and Shift Left Click. 
The first selected parameter will be shown with a black outline, the other selected parameters will be shown with a tiny outline.
The Shift Left Click action will extent the set of selected parameters with all parameters inside a rectangle with respect to the first selected parameter (the one with the black outline).
Click on a selected parameter to edit these values (thus if no selection double click on a parameter). 
If you leave a value empty, the value suggested by RXFFutil will be used.

A very common editing operation is to change the optimize flag. 
A convenient shortcut for this is to Control-left-click or Right-click on the parameter.
When using the shortcut, the optimize status will propagate to all selected parameters if it is changed for a selected parameter.

The optimize flag is indicated with a color (orange when optimized, no special color otherwise).

When you make changes to other optimization values for a parameter, this will be indicated graphically.

When saving the force field with parameter values will be saved to the ffield file, and the details regarding optimization will be saved to the params file.


Use the following menu commands to reset the changes you made to the values calculated by the rxffutil:

1. Reset Param Values in the Force Field menu: reset the parameter values used in the ffield file (the values that are visible)
2. Reset Param Ranges in the Force Field menu: reset the optimization ranges, as set by double clicking on a parameter

Mouse interaction
=================

In addition to the general mouse interactions for selection (already mentioned):

- Mouse over to see distribution of values, defaults etc (info from rxffutil)
- Control-left or right click on a parameter: toggle optimize flag, propagate to all selected parameters
- Click a selected parameter to edit it
- Left click on a parameter: set anchor (shown with an outline)
- Shift left click on a parameter: select a block of parameters (wrt the anchor) (selected parameters are visually marked))
- Left click on a selected parameter (or double click on a non-selected parameter): select and edit it
- Control-left or right click on atoms field: filter the training set with these atoms



