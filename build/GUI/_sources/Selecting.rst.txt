Selecting
*********

In many modules there are menu commands to select atoms:

- Select All: select all atoms in your system.

- Invert Selection: all atoms in your system currently not selected will be the new selection.

- Select Molecule: extent the current selection so that all atoms connected (by bonds as visible) to it are included in the selection.

- Select Connected: extent the current selection so that all atoms directly connected (by bonds as visible) to it are included in the selection. Thus repeated use of this command will select all atoms in your molecule (same as Select Molecule).

- Select Atom Close To Origin: select one atom close to the origin. Often useful to select one atom in a crystal, and next selecting atoms in a sphere around it (with the next command).

- Select Within Radius: set the selection to all atoms in a sphere with specified radius around the center of the current selection.

- Make Selection Cappable: extent the current selection such that it is acceptable as a region for the Hybrid engine, were all bonds to other parts will be capped. A cappable region should not have bonds with an order > 1.25 to atoms not in the region, and atoms outside the region should have at most one bond to atoms inside the region. This command will extent the selection so that these requirements are handled.

- Select Atoms Of Same Type / PDBName: extent the selection with atoms with the same Type (element) or PDBName.

