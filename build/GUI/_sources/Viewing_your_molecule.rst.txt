Viewing your molecule
#####################

Molecule style: Balls and Sticks, Sticks, or Wireframe
******************************************************

The molecule style can be selected via the View menu (**View → Molecule → ...**). You can select Balls and Sticks, Sticks, Wireframe or Hidden. This choice will affect the whole molecule. Note that if you use anything else then Balls and Sticks it will become much more difficult to select an atom (as there is no ball representing it). 

You can also use different styles at the same time, for different regions. To do that, go to the Regions panel, make regions as you like, and set the molecule style from the  pop-up menu per region in the Regions panel (the downward pointing triangle at the end of each region line). 

Camera position: view direction
*******************************

You can use the mouse to view your molecule from a different position. 

In some situations you may want to view your molecule from some very specific angle. There are a couple of ways to do this: 

+ **View → View Directions → Along X-axes**

+ **View → View Directions → Along Y-axes**

+ **View → View Directions → Along Z-axes**

These commands need no further explanation. 

+ **View → Align Screen**

Using this command, you can align the screen parallel to some plane in your molecule. You need to select three atoms first which will define the plane to align to. 

+ **View → Camera → Save... / Load...**

First view your molecule from your favorite position (or use one of the just mentioned commands). Next, you can store the camera position by selecting one of the Save 1-5 commands. That will store the current view in the selected slot. To switch to one of the stored views, use one of the Load 1-5 commands. 

The camera positions are saved for all GUI modules to use.  Thus, if you start AMSinput (or any other GUI module with a View menu) the stored camera positions are available everywhere. This makes it possible to force the use of the same camera position in different GUI modules. 

The Camera menu can be torn off, which is very convenient if you have several views that you wish to switch between frequently. To tear off the menu, select the dashed line in the Camerae menu. 

3D
**

The GUI modules do have support for real 3D viewing. Use the **View → 3D** menu to select what kind of stereoscopic display you have. The simplest version is having none, but using colored glasses (like the Red-Cyan). The other options are for special hardware. Just try out what works for you. This is a rather new and not completely stable feature, so it may not work for you. 

One known but at the moment this is written unsolved problem is that the 3D view does not work on Mac OS X using Lion (it does work with Snow Leopard). 

Fly to selection
****************

When you have a big system, it often make sense to zoom in to some particular region. To do this, use the **View → Fly To Selection** menu command. 

Not only will this zoom in to the selected atoms, but the center of the selected atoms will also become the new center of rotation when you use the mouse to get a different view. 

Reset View
**********

You can reset the view using the **View → Reset View** menu command. This is especially useful after flying to the selection. Or when the view gets distorted  for some reason. 

