Mouse Interaction
#################

.. _metatag ROTATE: 

Rotate, Translate and Zoom
**************************


In the modules that provide a 3D view of your molecule (like AMSinput, AMSview and AMSmovie) you can rotate, translate and zoom using the mouse. 

Drag with the mouse: press a mouse button, and move it while holding it down.  A one-button mouse button is the same as a Left mouse button. Which mouse button, and which modifier key you press at the same time, determines what will happen: 

.. csv-table:: 

   "Rotate",Left mouse button
   Rotate in-plane,Ctrl with Left mouse button
   Translate,Right mouse button
   Zoom,"Use the scroll wheel on your mouse, or Middle mouse button, or (not on windows) Alt with Left mouse button"
   
The rotate, translate and zoom operations change how you look at the molecule. They do not change the coordinates. 

In AMSinput operating with the mouse on the selection will move the selection only. In that case the geometry of your molecule (and thus the coordinates) will change. Zooming the selection will move it perpendicular to the screen, unless you are using the mouse-wheel. You operate on the selection by starting the drag operation with the mouse above a selected object. 

In the View menu you can select either 'Mouse as trackball' or 'Mouse as joystick'. If 'Mouse as trackball' is selected, you need to drag with the mouse (move the mouse with a button pressed down). If 'Mouse as joystick' is selected you just need to press and keep the button pressed down. The direction of movement etc will depend on the position of the mouse with respect to the center of the 3D view area. 

The mouse handling has changed in the 2013 release: the middle and right buttons have been switched. The right mouse button was used for zooming, now by default it is for translating (and zooming is much more convenient using the scroll wheel). Via the **SCM → Preferences** you can switch the mouse handling back to the previous style (use the "Right mouse button" option). 

Selecting
*********

.. _metatag SELECT: 

.. _mouseselect: 

In the modules that provide a 3D view of your molecule (like AMSinput, AMSview and AMSmovie) you can make selections using the mouse.  

::

   Click on an object: make a new selection with it

   Click in space: clear selection

   Shift-Click on object: add or remove it from the selection

   Shift-Drag in space: add all objects within the rectangle to the selection

In some modules there are additional ways to select objects using menu commands. Furthermore, in AMSinput one can select atoms from the list in the coordinates window. 

