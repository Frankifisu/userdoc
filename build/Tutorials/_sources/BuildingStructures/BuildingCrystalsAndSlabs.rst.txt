.. This tutorial has been recorded: examples/tutorials/building-crystals
.. Keep the recording in sync so it may be used to generate the images!

.. _CRYSTALBUILDING: 

Building Crystals and Slabs
***************************

In this tutorial we demonstrate the working of several tools that combined give you great flexibility to build periodic structures. 

If you are not interested in periodic structures (for example, if you only use ADF), you can skip this tutorial. 

The instruments at your disposal are: 

+ The crystal structures tool |CrystalTool|.

+ The predefined crystal structures in the database (via the search field).

+ CIF file importer.

+ Crystal builder from space group information.

+ Super cell tool to enlarge the unit cell.

+ Slice tool to cut out slabs from any crystal.

To use these tools you need to use AMSinput in periodic mode. For example, by switching to the BAND mode, or by switching to DFTB or Mopac and next changing the periodicity. 

.. seealso::

   More information about modeling crystals and slabs in AMS: see the :ref:`Crystals_Surfaces` tutorial.

The Crystal Structures Tool
===========================

If you are lucky your crystal structure is already included in AMSinput. Most of the common structures are there. NaCl is one of them. 

.. rst-class:: steps

  \ 
    | Start AMSinput and switch to BAND (or to DFTB, and switch the periodicity to 'Bulk')
    | Click on the snowflake-like pictogram |CrystalTool| on the toolbar.
    | Select a "Cubic" lattice and then NaCl

.. figure:: /Images/BuildingCrystalsAndSlabs/StructureTool_SelectNaCl.png
   :align: center

Next a dialog pops up where you can change the parameters of the structure, such as lattice constants 

.. figure:: /Images/BuildingCrystalsAndSlabs/NaClDialog.png
   :align: center

In this case there is no need to change anything. 

.. rst-class:: steps

  \ 
    | Click OK
    | **View → Periodic → Repeat Unit Cells**


You can adjust the details like lattice constants by hand. For example LiF: it has the same crystal structure as NaCl, but other elements and a different lattice constant, namely 4.02: 

.. figure:: /Images/BuildingCrystalsAndSlabs/LiFDialog.png
   :align: center

.. rst-class:: steps

  \ 
    | Open again the NaCl dialog
    | Change the lattice constant and the elements as shown
    | Click OK

The NaCl crystal structure will be replaced by the new LiF crystal structure. 

Some crystal structures have more parameters. 

.. rst-class:: steps

  \ 
    | Select "Tetragonal" and then "Rutile" from the snowflake tool
    | Click OK

.. figure:: /Images/BuildingCrystalsAndSlabs/RutileDialog.png
   :align: center

As you can see, it has two lattice parameters that need to be specified. But now also the positions of the oxygens have a parameter "x" 

After clicking 'Ok' your screen will look like this 

.. figure:: /Images/BuildingCrystalsAndSlabs/TiO2Rutile.png
   :align: center

The Crystal Structures Database
===============================

All crystal structures known to the crystal structures tool are also available via the search tool. 

Just as you can search for a molecule, you can search for a crystal. So lets make NaCl again: 

.. rst-class:: steps

  \ 
    | **File → New**
    | Click on the search icon, or press control or command - F
    | Type 'NaCl' (without the quotes)

You should get a couple of matches: 

.. figure:: /Images/BuildingCrystalsAndSlabs/SearchNaCl.png
   :align: center

Select the NaCl crystal result (not the molecule!): 

.. rst-class:: steps

  \ 
    | Click on the 'NaCl' search result (in the Crystals section)

You now should have a NaCl crystal again. 

.. figure:: /Images/BuildingCrystalsAndSlabs/NaClFromSearch.png
   :align: center

Currently the structures of many simple crystals are included, as well as a few complex structure (optimized by MOPAC). The zeolite frameworks are also included as a starting point to make your zeolite structure. 

Crystal builder (from space group information)
==============================================

.. _BUILDER: 

The structure database is very convenient but by necessity incomplete. A more powerful approach is to build 3D crystals from the space group information. Here we give an example on how to build TiO2 (Rutile) again, now from its space group. 

.. rst-class:: steps

  \ 
    | Open the crystal builder:
    | Click on the snowflake tool and select "From Space Group"

.. figure:: /Images/BuildingCrystalsAndSlabs/FromSpaceGroup.png
   :align: center

And the following window pops up 

.. figure:: /Images/BuildingCrystalsAndSlabs/CrystalBuilder.png
   :align: center

Rutile has the symmetry of space group 136 

.. rst-class:: steps

  \ 
    | Enter 136 in the space group "Number" field, and press return (enter key on Windows).

.. figure:: /Images/BuildingCrystalsAndSlabs/SpaceGroup136.png
   :align: center

Note how the Browser reflects the change and also how the "Name" and "Lattice" values change 

Now set the two lattice parameters as below 

.. figure:: /Images/BuildingCrystalsAndSlabs/CrystalDialogLatticeConstants.png
   :align: center

We still need to define the atomic coordinates. For starters click on the plus below "Coordinates" 

.. figure:: /Images/BuildingCrystalsAndSlabs/Coords136_first.png
   :align: center

In a book on crystal structures you can find that Rutile has two sites occupied. The Ti atom is on the "a" site 

.. rst-class:: steps

  \ 
    | Select the Ti atom and select the "a" site

.. figure:: /Images/BuildingCrystalsAndSlabs/Coords136_Ti.png
   :align: center

The oxygens occupy the "f" site. 

.. rst-class:: steps

  \ 
    | Click on the plus to add a site
    | Change the atom type to "O" and the site to "f"

.. figure:: /Images/BuildingCrystalsAndSlabs/Coords136_O_initial.png
   :align: center

As you can see in the "Coords" column and the "Parameters" column, this site has an undetermined parameter "x". (It represents a symmetry line for this space group.) In the book you can find that for TiO2 "x=0.3". 

.. rst-class:: steps

  \ 
    | Set "x" to 0.3

The final dialog looks like 

.. figure:: /Images/BuildingCrystalsAndSlabs/RutileFinalDialog.png
   :align: center

.. rst-class:: steps

  \ 
    | Press "Apply" and if that looks any good press "Close"

.. figure:: /Images/BuildingCrystalsAndSlabs/RutileFinal.png
   :align: center

In the toolbar there is another tool that may be of use: the star button.
Just like the similar button for molecules this button will try to detect the symmetry of your system and make small changes to adjust to perfect symmetry.
It does this via spglib, see the help balloon for details.

.. rst-class:: steps

  \
    | Click the Symmetrize button (the star in the toolbar)

You already had perfect symmetry, so nothing much changes.
The detected symmetry should be reported:

.. figure:: /Images/BuildingCrystalsAndSlabs/RutileSpglib.png
   :align: center

You can view a larger part of the crystal and still see the unit cell clearly:

.. rst-class:: steps

  \
    | Right-click on the periodic display button (the 4 dots)
    | In the dialog that pops up type 2 in the top-left cell (other elements will follow)
    | Click OK
    | Use ctrl/cmd-J and ctrl/cmd-K to make neighbor cells more or less transparent (or use the menu commands in the View menu)

This will give you a view like this:

.. figure:: /Images/BuildingCrystalsAndSlabs/RutileTransparent.png
   :align: center


Slicer: building slabs, transform primitive to conventional cell
================================================================

The slicer is a very easy, yet powerful tool to make slabs from any crystal structure. 
In this example we build a three layer slab of the Cu(111) surface.

.. rst-class:: steps

  \ 
    | Select fcc from the "Cubic" crystals

The element and lattice constant are already correct for Cu. 

.. figure:: /Images/BuildingCrystalsAndSlabs/FccDialog.png
   :align: center

.. rst-class:: steps

  \ 
    | Press "OK" to generate the Cu lattice
    | **View → Periodic → Repeat Unit Cells** if needed

.. figure:: /Images/BuildingCrystalsAndSlabs/CuLattice.png
   :align: center

Let us invoke the slicer tool to cut out the slab. 

.. rst-class:: steps

  \  
    | Click on the |SliceTool| slice tool, *or* select |CrystalTool| **→ Generate Slab**.

The right side of the AMSinput window will show the Generate Slab options.

If you hold your mouse over the Miller indices fields, you should get a balloon
that explains how to set the proper Miller indices.  In this particular example
we have the primitive unit cell of Cu, so first **we need to convert to conventional unit cell**. 

.. rst-class:: steps

  \ 
    | Click on the **Convert to Conventional Cell** button.
    | Set the Miller indices to ``1``, ``1``, ``1``
    | Set the number of layers to 3

.. figure:: /Images/BuildingCrystalsAndSlabs/Dialog111Cu.png
   :align: center

.. rst-class:: steps

  \ 
    | Press **Generate Slab**

The generated surface unit cell is in this case not the primitive surface unit cell, but a (2×2) surface supercell.

.. rst-class:: steps

  \ 
    | |CrystalTool| → Convert To Primitive Cell

You will see (from the top), if the |PeriodicViewTool| periodic view tool is activated,

.. figure:: /Images/BuildingCrystalsAndSlabs/Cu111Top.png
   :align: center

You may want to rotate it or select **View → View Direction → Along X-axis** to
convince yourself that it is a three layer slab. 

.. figure:: /Images/BuildingCrystalsAndSlabs/Cu111Side.png
   :align: center


.. seealso::

   More about :ref:`primitive and conventional cells <unit_cells>`, and :ref:`surface_unit_cells`.

.. _supercell:

Creating a supercell
====================

Quite often you want to use a larger unit cell. You can do this for chains, slabs, and crystals, but we will demonstrate how it works for a slab. 

We will continue to work with the 3-layer Cu slab: 

.. rst-class:: steps

  \ 
    | Select the **Edit → Crystal → Generate Super Cell...** command

Thus invoking the Super Cell Tool 

.. figure:: /Images/BuildingCrystalsAndSlabs/SuperCellTool.png
   :align: center

Here you see how new lattice vectors are expressed in terms of old ones. Because we have a slab this is a 2x2 matrix. 

.. rst-class:: steps

  \ 
    | Use the default (2 on the diagonal)
    | Press OK

and you get a bigger unit cell with three atoms per layer: 

.. figure:: /Images/BuildingCrystalsAndSlabs/Cu111S3.png
   :align: center

.. rst-class:: steps

  \ 
    | Close AMSinput
 

.. seealso::

   :ref:`surface_unit_cells`
