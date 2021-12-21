Building molecules
******************

Building molecules with AMSinput is very simple, just draw them with the appropriate tools. Please check the tutorials for extensive description of this. 

Here we will just note some details that may not be obvious. 

Bonding mode
============

After creating an atom, it will be selected (the 'bond atom'). When you still have an atom tool and one atom is selected, you are in bonding mode. This is indicated by a line from the bond atom to the mouse cursor. If you next click to create a new atom, it will automatically be bonded to the bond atom. 

To stop bonding mode, click once on the bond atom. This will switch to the select tool, and as a result you are no longer in bonding mode. 

Atom Details: Connectors (valency) and Lone Pairs, Atom mass
============================================================

Each atom you make has the possibility to connect to other atoms. The number of connections depends on the atom type. Some of the 'connectors' may be used by lone pairs and not be available for bonding to other atoms. 

For example, carbon has 4 connectors and no lone pairs, oxygen has 4 connectors and 2 lone pairs. 

When you use the Add Hydrogen menu command, all unsaturated connectors will be saturated with hydrogen atoms. The number of connectors will determine the geometry (2 linear, 3 flat, 4 tetrahedral). So if you plan to use this command it is essential that the number of connectors and the number of lone pairs is correct. 

You can view and change these via the **Atoms → Details (Color, Radius, Mass...)** menu command. It will activate the Atom Details panel, in which you an change the number of connectors and lone pairs for each atom. Note that only selected atoms will be visible in the Atom Details panel. 

You can also see and change other atom properties like the type, screen radius, nuclear charge, mass, color, Amber and Tripos atom types and more. 

Right click on one of the fields to propagate that value to all selected atoms (for example to change the color of all selected atoms).

Pre-optimization
================

After drawing a molecule you will typically run a pre-optimization. 

On the right end of the molecule editor tools you will see a cog wheel. If you click it your system will be optimized using the UFF method. 

If you right-click the cog wheel you will get a pop-up menu that allows you to specify which method to use as a pre-optimizer: UFF, Mopac, DFTB or SimpleMM. UFF, Mopac and DFTB are identical to these methods within AMSinput, SimpleMM is a very primitive force field like method that used to be the only available pre-optimizer. It is mainly included for compatibility. 

Alternatively you can just switch AMSinput into UFF, Mopac or DFTB mode (by using the orange method menu in the panel bar). For each of these you will find a 'Run' button on the Main panel. If you press it, it will run the current set up interactively, updating the coordinates and possibly the bonds on screen automatically. This is very similar to clicking the cog wheel, but it allows you to set details of the calculation. For example, for DFTB you can select what parameter set to use. 

Geometry adjustments
====================

Sliders
-------

Select two, three, four or five atoms. 

Below the molecule, a horizontal slider will appear, just above the toolbar. 

You can drag the thumb inside the slider to change the distance, angle, dihedral, or plane angles. 

The order in which you select the atoms determines what atoms will move. The selection order is shown in the molecule editing window.
The last atoms selected will move (together with things connected to those atoms).  However, if you press the control key and then move the slider, the smallest group will move.
You can force this behavior (so you do not need to press the control key)  by setting the SCM_GEOMODSBYSIZE environment variable (via the Preferences or via the command line). 
Note in the 2017 version the default was the reverse (smallest group moving, by order with control key).

You can use regions to group atoms. Atom in a region will move together when using a slider to change distance or angle. 

Edit box
--------

Select two, three, four or five atoms. 

Above the slider on the right side you will get an text entry box next to the atom labels. For example, after selecting two atoms it might look like H(8)-C91) (pm): 149. The 149 in this example is editable. Instead of using the slider, you can type some specific number in this box instead. 


Centroids
---------

A centroid in AMSinput is defined as a dummy which is (and will stay) in the geometrical center of the atoms to which it is bonded.
They are useful to control the geometry for molecules like ferrocene, as you can easily set the distance between the central atom and the center of a ring.

To make a centroid, select the atoms that should define the center, and use the **Edit → Add Centroid** menu command.

As an example, to change the distance between a ring and the Fe atom in Ferrocene:

1. Use the structure tool to load Ferrocene.
2. Select the carbons in one ring.
3. Add a centroid.
4. Delete the bonds between Fe and the carbons belonging to the centroid (otherwise you will not be able to change the distance)
5. Select the centroid and the Fe
6. Use the slider to set whatever distance you want (or set it in the input field).

Thus the centroid functions as a fixed manipulation point.

Another example, to change the angle ring - Fe - ring in Ferrocene, adjusting the planes of the rings as well:

7. Make a similar centroid in the second ring (also with Fe - C bonds removed).
8. select centroid - Fe - centroid.
9. Change the angle using the slider.

Another way to manipulate your geometry is selecting the centroid (as the only selected item). Dragging the centroid will drag everything to which it is bonded.


Move an atom (possibly perpendicular to the screen)
---------------------------------------------------

First select the atom that you want to move. 

Next, translate (middle mouse button, or alt left mouse button), but start with the mouse on the atom that you want to move. 

If you wish to move the atom perpendicular to the screen: use the right mouse button (or command left mouse button) and move the mouse up or down). This is equivalent to zooming. 

Rotate or translate the selection
---------------------------------

First make your selection. 

Next rotate, translate or zoom as usual, but start with the mouse in the selection. So if you click and drag the selection, ONLY the selection will be rotated or translated. If you click and drag anywhere else the whole molecule will be rotated or translated (actually, only your viewpoint). 

If you 'zoom' the selection you are really moving the selected objects perpendicular to the screen (in or out the screen). 

Coordinates
-----------

In some situations you want to set the coordinates of the atoms exactly to some value. You can do this via the Coordinates panel (in the Model part of the panel bar). 

If you first select the atoms of interest, they will be highlighted in the Coordinates panel. The coordinates in that panel can be edited, and the molecule on the left side will immediately reflect the changes. 

Z-Matrix
--------

In some situations you want to set the coordinates of the atoms via a Z-Matrix. You can do this via the Z-matrix panel (in the Details part of the panel bar). 

If you first select the atoms of interest, they will be highlighted in the Z-Matrix panel. The values for the distances and angles in that panel can be edited, and the molecule on the left side will immediately reflect the changes. 

The connectivity can not be edited, but you can effectively do this by reordering the atoms. That way you normally can create the Z-Matrix coordinate that you are after. 

Set Center Of Mass
------------------

The **Edit →Set Center Of Mass** command translates all atoms so that the mass-weighted center  of the selection will be the new origin. If nothing is selected, the center of mass of the whole molecule will be  the new origin. 

The atoms are really translated, thus the coordinates are changed. It is not a change of the camera. 

When symmetry is used, the origin will also be the origin of symmetry. 

Set Origin
----------

The **Edit →Set Origin** command translates all atoms so that the center of the selection will be the new origin. If nothing is selected, the center of all atoms will be the new origin. 

The atoms are really translated, thus the coordinates are changed. It is not a change of the camera. 

When symmetry is used, the origin will also be the origin of symmetry. 

Symmetry
--------

To symmetrize your molecule, clock on the **star tool** in the tool bar below the molecule editor. This is equivalent of the **Edit → Symmetry → Symmetrize Using Symmol** menu command. In most cases this just works, and is the preferred method of symmetrizing your molecule. 

The **Edit → Symmetry** menu gives access to a less automatic but more power-full symmetry code. Using it is somewhat complicated, and sometimes it does not work as expected. 

To use it, follow this procedure: 

+ Select the symmetry group

+ Set the (symmetry) origin of your molecule via the SetOrigin menu command

+ Define one or two operators for the selected group. In the symmetry menu you can see what operators you need to define.        

+ Use one of the symmetry commands:     

Rotate 90
---------

The **Edit → Rotate 90** commands (select an axes via the submenu) will rotate your system around some axes. 

Not only the coordinates of the atoms, but also the lattice vectors (if any) will be rotated. 

Thus, for example, if you get some .cif file with a nanotube structure and want to treat  it with BAND as a one-dimensional periodic structure (a chain), you must ensure it is oriented along the x axes.  If the structure in the .cif file is oriented along another main axes, these commands make it very easy to fix that. 

Align
-----

The **Edit → Align** command contains commands to align your molecule to the indicated axes or plane. 

If you are aligning to an axes, you need to select which atoms to align. If you select one atom, the molecule is rotated around the origin such that the selected atom is on the specified axes. If you select two atoms, first the molecule is translated such that one of the selected atoms is on the origin. Next, the molecule will be rotated such that the other selected atom is on the specified axes. 

If you are aligning to a plane, you need to select a plane to align. If you select two atoms, these will define the normal of the plane to be aligned. If you select three atoms, these define the plane to be aligned. 

This Align command does change the coordinates of your atoms, unlike the Align Screen command in the View menu. 

Not only the coordinates of the atoms, but also the lattice vectors (if any) will be rotated. 

Typically the Align command will change your origin. You can always set the origin as you like after-wards. 

Mirror
------

The **Edit → Mirror** command contains commands to mirror the selected atoms (or all atoms if no atoms selected) in a plane parallel to the indicated plane, through the center of the selected atom(s),  or through the center of the molecule if no atoms selected. 

The Mirror command does change the coordinates of your atoms. Also the lattice vectors (if any) will be mirrored. 

Update coordinates via AMSmovie
-------------------------------

If you have performed a calculation that saves multiple geometries, for example a geometry optimization or a linear transit run, you can use AMSmovie to see how the geometry changes. You can go to a particular geometry, and then use the '**File → Update Geometry in Input** menu command in the Movie window to adjust the geometry in the matching AMSinput window. 

Bonds
=====

Bonds are normally made while drawing the molecule. There are several other options to handle bonds: 

+ Make a bond via an atom tool: Take one of the atom tools.   Next click once on the first atom you want to connect. You will enter the bonding mode (the line to the mouse  position from the atom you just clicked on will be your visual cue for the bonding mode).   Next click on the atom you want to make the bond to.   The bond will be created, and you will revert to the normal select mode.   

+ Make a bond using the Add Bond command: Select the two atoms that you wish to be bonded together, and then use the **Bonds → Add Bond** command.   

+ Via Guess Bonds Use the **Bonds → Guess Bonds** menu command.   This command uses an algorithm that looks at bond distances to guess the bonds and bond orders. The bond orders are adjusted based on the known number of connectors and lone pairs.   
