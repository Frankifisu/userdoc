Regions
*******

A Region in AMSinput is defined as a collection of atoms. Atoms may be present in one or more region. 

Within the GUI they are used for many purposes. For example to change the visualization style for part of the molecule, to set up fragment calculations, or to set up other multilevel calculations like QUILD, QMMM or FDE. 

When using the slider to change distances or angles you can use regions to group atoms (so they move as one). 

When you select the Regions panel (in the panel bar Model section) you will find that one region has already been defined: All.  This region consists of all atoms of your molecule, and is always present. 

To add a new region, click the + button. If any atoms are selected when you press this button, they will automatically be added to this new region. With this new region you can do a couple of things: 

+ Click the - button: delete the region. Note that only the region is deleted, not the atoms in it.

+ The check box: this selects all atoms currently in the region. In your molecule display you can easily see what atoms are in it, and it will also tell you how many atoms are contained in this region.

+ Click in the region name to change the name

+ Click the check box (the V-like shape) to show the region graphically

+ The + button (on the right hand side): add the currently selected atoms to this region

+ The - button (on the right hand side): remove the currently selected atoms from this region

+ Click the triangle to get access to a pop-up menu with a number of commands that apply to that region.

The pop-up menu per region has the following options: 

+ **Split By Molecule**: split the region in many regions, based on the connectivity. Thus parts that are not bonded together will all be put in a separate region. The typical use is for solvents: first add a solvent with explicit molecules. The solvent molecules will automatically be put in their own region. Next, use the Split By Molecule command to split this into many small regions. If all your solvent molecules are identical, this leads to a very big time saving with fragment or FDE calculations. As the typical use is for replicated fragments, the naming of the newly generated regions will use the /n name, with n a number. Currently AMSinput does not check if the fragments are really identical!

+ **Invert Selection Within Region**: perform an invert selection command, but just within the atoms part of this region.

+ **Region Color**: set the color used to visualize the region

+ **Balls And Sticks**: show the atoms and bonds in this region using Balls and Sticks

+ **Sticks**: show the atoms and bonds in this region using Sticks only (that is, atoms not visible)

+ **Wireframe**: show the atoms and bonds in this region using a wire frame only (again, no atoms visible)

+ **Hidden**: do not show the atoms and bonds in this region

Regions can also be used in the Numerical Quality and Basis panel: you can change the basis per atom type per region. For example, give all carbon atoms in an outer region a smaller basis. Or you can set the Quality per region (the Becke / Zlm fit options and/or Basis and Core). 

A quick and easy way to make a new region containing the current selection is to use the **Atoms → New Region From Selected Atoms** menu command (cmd/ctrl-G). 
