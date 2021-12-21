Crystals and Slabs
******************

Periodicity
===========

Many GUI modules support periodicity. Some menu commands (like the **Edit → Crystal** command in AMSinput) will only by available when you have a periodic system. 

To set up periodicity you first need to switch to a method that supports periodicity. For example BAND, DFTB, Mopac, or UFF. Some of these, like UFF, are currently available without extra license. 

On the Main panel of a method that supports periodicity, you will find a 'Periodicity' pull-down menu. Use it to use periodicity in 1 (Chain), 2 (Slab) or 3 (Bulk) dimensions. Once periodicity is enabled,  menus like the Crystal menu will also be enabled. 

The tool bar below the molecule editor also changes when you have a periodic system. The structures tool gets replaced by the crystal tool (represented by a snowflake), followed by the Slice tool (which invokes the Generate Slab command). At the right side of the tool bar you find buttons to orient the camera, toggle perspective and toggle the display of periodic images. 

To set up the lattice vectors, press  the "...' details button next to periodicity, or go to the Lattice panel (in the Model section). 

When editing the lattice vectors: changing the 1,1 element also adjusts the 2,2 and 3,3 element.
Changing the 2,2 element also adjusts the 3,3 element (but leaves the 1,1 as it is).

Building crystals
=================

After setting the periodicity and lattice vectors, you can build your own crystal by adding atoms at the proper position. For many crystals this is a lot of work. 

You can also build crystals using the** Edit → Crystal** command. The first list of options (Cubic, Hexagonal and so on) have sub-menus for some common crystals. If your crystal is not in there, you can use the "From Space Group..." command in the same menu. This brings up a dialog that will help you build any crystal. 

The crystal tools are not only available from the Edit menu, you can also press the 'Snowflake' button in the molecule editor tool bar (next to the element button, if periodicity is enabled). It has the same options as the **Edit → Crystal** menu. 

Build slabs
===========

Building a slab is done most conveniently using the Generate Slab tool: first build a crystal, next use the "Generate Slab..." command from the Crystal menu to make a slab. Next you will need to enter the Miller indices of the plane that will define your slab. 

The Generate Slab tool is available from the **Edit → Crystal** menu, or in the periodic toolbar (the slice icon next to the snowflake). 

Crystal menu
=============

Generate Super Cell...
----------------------

In the dialog that appears when using this command you determine how the super cell should be created.

When editing the setup: changing the 1,1 element also adjusts the 2,2 and 3,3 element.
Changing the 2,2 element also adjusts the 3,3 element (but leaves the 1,1 as it is).

Map Atoms To (-0.5..0.5)
------------------------
**Edit → Crystal → Map Atoms To (-0.5..0.5)** 

Using the translational symmetry, the atoms are mapped to the cell centered around the origin.
Thus with fractional coordinates between -0.5 and 0.5 for each lattice direction.

Map Atoms To (0..1)
-------------------
**Edit → Crystal → Map Atoms To (0..1)** 

Using the translational symmetry, the atoms are mapped to the cell in the positive quadrant.
Thus with fractional coordinates between 0 and 1 for each lattice direction.

Set (0.5, 0.5, 0.5)
-------------------
**Edit → Crystal → Set (0.5, 0.5, 0.5)** 

The selected atoms define some point. This point will be translated to the point with fractional coordinates 0.5, 0.5, 0.5.
All atoms will be adjusted according to this translation.

Related, to shift the point defined by the selected atoms to the origin use the Set Origin command.

