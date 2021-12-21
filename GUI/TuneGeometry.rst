Tuning Geometry: translation, rotation, position with respect to plane
**********************************************************************

The  **Edit → Tune Geometry...** menu command gives you a panel with some options to fine-tune the geometry of your system.

You can use it for example to:

* precisely translate or rotate part of your system
* scale your system
* orient part of your system, for example an adsorbate
* move adsorbates around on surfaces

Typically you will have to set up some details first, like which atoms to move, or in which direction.
The ⬭ button will use the currently selected atoms to set the details in front of the button.

Atoms to move
=============

To tune the geometry of your system some atoms will have to be moved. This may be a single atom or many atoms.
If you do not use this option, the selected atoms will be adjusted.

Often it is convenient to fix the set of atoms that will be adjusted.

To do that, use the ⬭ button: it will set the atoms to be moved to the currently selected atoms.

That allows you to change the selected atoms (for example to set other options) without having to re-select the atoms to move.

Click the button that lists the atoms (or shows the text 'Selected Atoms') to show which atoms have been set (they will be selected).

Translate atoms, direction
==========================

This option will translate atoms in a specified direction.

1. First specify a direction, this is a vector in x, y, z coordinates. 

You can use the ⬭ button to set this vector using the currently selected atoms:

* from the first selected atom towards the second selected atom,
* perpendicular to the plane of three selected atoms.

2. Next you need to set the step size, the default is 0.1 Angstrom. 

This step is in the direction specified (the direction vector will be normalized).

3. Click the left ◀ or right ▶ arrow to translate the atoms.

The atoms will be translated in the specified direction, with the specified step size.

4. After the first click you may use the space bar to repeat the action.

Translate atoms, target
=======================

This option will translate atoms towards a specified point (target).

1. First specify a target, this is a point in x, y, z coordinates. 

You can use the ⬭ button to set the target to the geometrical center of the selected atoms.

2. If you check the "As a group" option, all atoms move in the same direction (from the center of the atoms towards the specified point).
Otherwise, each atom moves towards the specified point.

3. Next you need to set the step as a fraction of the distance to the target, the default is 0.01.

4. Click the left ◀ or right ▶ arrow to translate the atoms.

The atoms will be translated in the direction of the target, with the specified step.

5. After the first click you may use the space bar to repeat the action.

Note: as the step is a fraction of the distance of the atoms to the target this option can also be used to scale all coordinates 
(use a target at 0 0 0, and be sure not to move the atoms as a group).

Rotate atoms
============

This option will rotate atoms around some axes, around some point with a specified angle.

1. First specify an angle in degrees.

2. Next specify the direction of the axes around which will be rotated.

You can use the ⬭ button to set this vector using the currently selected atoms:

* from the first selected atom towards the second selected atom,
* perpendicular to the plane of three selected atoms.

3. Specify the center around which will be rotated.

You can use the ⬭ button to set the target to the geometrical center of the selected atoms. Obviously the rotation axes will run through this center.

* If no atoms are selected, that button will clear the fields.
* If no center is specified, the center of the rotation will be the geometrical center of the atoms that will be rotated.

4. Click the left ◀ or right ▶ arrow to rotate the atoms.

5. After the first click you may use the space bar to repeat the action.

Position atoms with respect to a plane
======================================

This option will position atoms with respect to a plane.

1. First define the plane. 

This is done by selecting three atoms, and using the ⬭ button. 

The plane through the three selected atoms will be used.
The default is the XY plane through the origin.

Click the button that shows the atoms defining the plane to show these atoms by selecting them.

2. Next, optionally, define 'Above atoms', which is a set of atoms above which your atoms should be located. 
The geometrical center of this set of atoms will be used as reference point.

Click the button that shows the 'Above atoms' to show these atoms by selecting them.

3. You need to specify the distance to the plane (default 2.5 Angstrom), and how this distance is measured: 

* to the geometrical center of the atoms that will be adjusted, 
* to the closest atom of the atoms that will be adjusted,
* to the first atom selected that will be adjusted.

4. Click **Move** to move (translate) the atoms to be adjusted with respect to the plane and the 'Above atoms'.

The atoms will be translated such that:

* the distance of the reference position to the plane is the specified distance,
* if 'Above atoms' have been set: the reference position will be above the 'Above atoms' when looking perpendicular to the plane,
* ff multiple atoms have the same distance to the plane, the geometrical average of these atoms will be used.

5. Click **Orient Perpendicular** to position the atoms perpendicular to the surface:

The atoms will be adjusted such that:

* the line through the first and second atom of the atoms will be perpendicular to the plane,
* the first atom will be kept in place,
* if already perpendicular, clicking this button will rotate the selection 180 degrees.

6. Click **Orient Parallel** to position the atoms parallel to the surface:

The atoms will be adjusted such that:

* the first atom of the set of atoms to move will be kept in place,
* the line through the first and second atom of the atoms will be parallel to the plane,
* it will also be parallel to the line through two 'Above atoms', or to the line through the first two atoms defining the plane, or the X-axes,
* if already parallel, clicking this button will rotate the selection 180 degrees.

