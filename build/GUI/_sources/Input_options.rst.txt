Input: options
**************

Normal Options
==============

On the right side of the AMSinput window you have the panels with input options.

Most of the options presented in the different panels are generated automatically from configuration files that define the input for ADF, BAND etc.This ensures that all options are up-to-date, and that the descriptions in the help balloons (when your mouse pointer is over an option) are also up-to-date (and identical to the information in the user manuals).

The options are logically grouped together, the most important are on the Main panel.

Options regarding the physical Model are in the Model section, options that determine how and what properties are calculated are in the Properties section, and many other options that are details relating to the calculation are in the Details section.

If you cannot locate the option you are looking for, use the search field at the top right of the AMSinput window.

Expert Options
==============

Some options are either hardly ever used and have not been put explicitly on some panel.
And similar it might happen that the compute codes have some new options that have not yet been explicitly added to AMSinput.
All such options are added to the Expert Options panel in the Details section (again automatically generated).

Most users will not need to use these, but all options are available in this way.

The Expert Options panel is available for all SCM software, except for ADF (this will be fixed in a future release).

Again, if you cannot locate the option you are looking for, use the search field at the top right of the AMSinput window.


Units
=====

Often options have some unit associated with them. The units are clearly presented in the panels.

A hidden feature is that in most cases in AMSinput you can change the units.
Just click on the unit with your mouse, and a menu will pop up that you can use to select the units that you like.

The units that are selected without moving the mouse are the default units.

When you make a change, that change is saved when you quit AMSinput (in the $HOME/.scm_guirc file).
The next time you start AMSinput, that particular field will use the units you selected.
To revert everything to the default units, use the Preferences module, and select the 'Reset AMSinput units' command from the File menu.

Layout of Main panel
====================

Each of the modules has a Main panel. By default it contains the most important options that you need to consider.

You may change what options are present on the Main panel of each module. 

Start by making sure the Main panel is editable: click the icon at the top right in the panel.

Once editable, right-click on the label of any option in a panel (that is the left part) to get a popup menu with edit options. 

When doing this on options on the Main panel you get a menu that you can use to delete or move up/down an item. You can also add a new label (you will get the option to specify its text), or add a link to an option to some other page. Finally, you can either make the Main page empty, or reset it to the Default Main page.

When doing this on options on another panel, you get a menu that allows you to add that option to the Main panel (at the end), or to set the current panel as the target for a link that you want to make on the Main page.

The Default Main page is always available in the Model menu, with the name of the module you are using (thus named ADF, BAND, DFTB, etc). Thus, if you remove items from the Main page you can still find them on this Default Main page, so you can selectively add them back to the Main page.

The Main page layout that you define will be stored inside the .scm_gui folder in your home folder, as a file called amsinput.main with a version number. If you update the AMS package to a new main version, a new file will be made to be sure new Main options will be shown to you. Bug-fix releases (where the version number including one decimal will not change) will use the same layout configuration file.