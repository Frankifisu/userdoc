AMSpreferences
##############

.. _metatag PREFERENCES: 

The GUI preferences module of the GUI (started via the Preferences command in the SCM or Application  menu) allows you to set many preferences.

General
*******

In the preferences module you can change things as you would like them to be. To test them use the Preview button. This will instruct all currently open modules to use the 
selected preferences. If you then quit the preferences module your changes (to the preferences) will not be saved, and all open modules will revert to the previous preferences.
Click the Save button to save the changes you made.

The preferences are save (by default) in a file called .scm_guirc in your home folder. Typically this is a hidden file, you need to use the terminal to see it.
If you remove (or move) this file and start a GUI module a new clean .scm_guirc file will be made. 

Restore defaults
****************

In the file menu of the Preferences application you will find commands to restore the preferences to their default values.
This is equivalent to deleting the .scm_guirc file.

You can also only reset the units as used by AMSinput to the default units.

Panels
******

On the top you will see tabs: Options, Colors, Module and Environment.

Click on any of those tab titles to get a menu that allows you to go to a panel belonging to that category.

General
-------

The General panel allow you to set some general options, like mouse handling and font size.

Atoms and Bonds
---------------

This panel (click on the Options title of the Options tab to get to it)  allows you to set some preferences for the visualization of atoms and bonds.

Colors
------

In the colors panel you can set details of the background color (for all modules), and the default colors for fields visualized by AMSview.

Atom Colors
-----------

This panel allows you to set the color range when coloring atoms by scalars.
It also allows you to change the default color per element (click the + button to select for which element you want to change the color).

Bond Colors
-----------

Allows you to color the bonds by atom types or not.

AMSview
-------

Set AMSview specific preferences (see also the Colors panel).

AMSjobs
-------

Set AMSjobs specific preferences.

AMSlevels
---------

Set AMSlevels specific preferences (which lines to show for contributions etc, you can change for what contribution/interaction range to show them, the width and the color).

Environment
-----------

Allows you to set environment variables to be used by GUI modules. They are saved in the GUI preferences, and have no effect on environment variables set by default in your shell.

