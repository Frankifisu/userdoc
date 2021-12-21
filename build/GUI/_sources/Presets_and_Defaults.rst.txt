Presets and Defaults
********************

All input options have default values. AMSinput presets are simply a collection of input values to be used. 

A preset may set all or just a few input options. After you have selected a preset, fields that are set by the selected preset will be show with a green color. 

If you next use another preset, only the input options included in the preset will be changed. Other input options will remain as they are.
Thus the order in which you apply presets is important.

Using a preset
==============

AMSinput always first uses the Defaults preset as included by SCM. 
Next the Defaults preset defined by the user (if any).
Finally, a preset matching the current task will be loaded (either from SCM or defined by the user).

When you switch the Task, AMSinput will try to load a matching preset. 

If you have saved matching presets yourself these will be used instead of the standard presets, thus allowing you to set your own defaults as you like them. A matching preset is a preset that has the same name as the Task selected, user-defined presets are searched first. If no matching preset is found, AMSinput will load a preset matching the Single Point task (which is always available). For presets to match, spaces and minus signs are ignored.

You can also load any preset you like using the Preset command from the File menu.
This preset will be applied just as the other presets, so it does make a difference when you load the preset.

Color Code
==========

The input fields use a color coding to warn you they have been modified: 

+ No special color: the field has its original default value.

+ Yellow: the field has been changed by the user (only).

+ Green: the field has been changed by the preset (only).

+ Red: the field has been changed by the preset, and next by the user.

The pull-down menus in the panel bar use a similar color-coding to point you to fields that have been changed: 

+ No special color: all fields in the panel have their original default value.

+ Yellow: some fields have been changed by the user.

+ Green: some fields has been changed by the preset.

+ Red: some fields has been changed by the preset, and some (possibly also) by the user.

Make your own presets
=====================

It is very easy to make your own presets, collecting all or a few default values for the typical jobs you like to perform. 

By default presets are saved in the $HOME/.scmgui/Tpl directory. This can be changed by setting the SCM_TPLDIR environment variable.

To make your own preset, follow these steps (in AMSinput): 

+ edit all the fields as you would like them to be stored in a preset.

+ select 'Save as preset...' from the Preset menu, or 'Save as full preset...'

+ specify a name

+ click on Save

If you now check your Preset menu you will find a new entry.  

The name of the preset is the file name you have chosen, but without the .tpl extension. 

The difference between a Full Preset and a 'normal' Preset is that a Full Preset will save all input options, and a 'normal' preset will save only the yellow, green or red fields (options that have been changed by the user or by the active template). 

If you wish to store only fields that you have changed yourself in the preset, make sure you start with the None preset.

If you save a preset with the same name as one of the default presets, it will effectively replace that preset. 
One exception: the SCM supplied Defaults are always read first, and thus cannot be replaced.

Some presets are only available for specific methods. For example, the Fragment Analysis preset is only available for ADF. You can get this behavior for your own presets by pre-pending the name of your preset by the name of the method for which it should be available. For example "ADF_My_Defaults", or "BAND_My_band_Defaults". 

To delete your own preset(s), use the 'Delete Preset' command from the Preset menu. 

Multiple presets are used
=========================

The default values that are used when you start AMSinput are generated as follows: 

+ Use the Defaults preset supplied by SCM

+ Use the Defaults preset that the user has defined, if any

+ Use the 'Single Point' preset, either supplied by SCM or one that is defined by the user (if any)

+ Any user selected preset, directly or implicitly (by changing the Task).


Input options remarks
=====================

Empty fields
------------

Some input fields do not have a value from the default Preset. In those cases AMSinput does not specify the value, but leaves the value to be determined by the ADF program. 

You can use the 'Explicit Defaults' preset to see the typical values. However, depending on details of your calculation the actual default used by ADF may be different. 

Spin and Occupation
-------------------

The spin and occupation panel allows you to specify the occupations of the orbitals per symmetry. In case of an unrestricted calculation you can also specify the occupations per spin type. 

To show the available symmetries, AMSinput needs the result of an ADF calculation. If a previous calculation is available (without specifying the occupations), it will use the information from that calculation to generate the proper options in this panel. If such results are not available, AMSinput will suggest to run a short guess calculation: a preliminary run with an inaccurate grid, only a few SCF cycles and stopping immediately after the SCF. Hopefully this guess calculation will allow you to generate sensible occupation. 

The energy levels of the guess calculation (or previous calculation if available) will be shown using AMSlevels. Be aware that it is the result of the guess calculation, and not your proper results! 

User Input
----------

You can use the User Input field to specify any kind of text. The text will be put without any change at the beginning of the ADF input. This way, you may access some keys that are not (yet) available in AMSinput.  

Alternatively, and more flexible, you can obviously edit the .run file after saving it with AMSinput. 
