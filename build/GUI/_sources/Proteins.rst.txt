Proteins (from PDB or mol2 files)
*********************************

AMSinput can read a protein from a PDB file for from a mol2 file. 

The atom information is read (element type, coordinates, PDB name, residue to which the atom belongs, and chain information). 

The PDB atom names are also essential to properly add hydrogens, in case your PDB or mol2 file does not have any hydrogens. 

In the **Regions panel** for each chain detected in the PDB file, there will be a new line. This gives you a couple of visualization options (Ribbon, or all C, CA, N or O atoms connected). If you click on the triangle to the right you get a pop-up menu with some additional commands: 

+ **New Region From Chain**: make a new region, and put all atoms belonging to this chain into the new region

+ **Select Residue**: select all atoms in a given residue (which you select from the menu)

+ **Residue Protonation**: change the protonation state of some residues

+ **Add Hydrogen**: add hydrogen atoms to this chain

+ **Add Selection To Chain**: the selected atoms are marked as belonging to this chain

+ **Add Selection To Residue**: the selected atoms are added to the specified residue

Many of these features depend on the proper PDB names and residue information for the atoms. If they are not correct, or non-standard, AMSinput may for example add hydrogens to the wrong positions, or visualize things incorrectly. 

For the protonation state of some residues it is essential that their proper names are used: **LYN/LYS, ASP/ASH, GLU/GLH, HID/HIE/HIP**. 

You can use the **Atoms → Details (Color, Radius, Mass, ...)** command to check and change the PDB names of the atoms. 

Having the proper PDB atom names and residue types (including the proper protonation state) is essential.  The atom types generated for MM (Amber95) depend on them, as well as the algorithm that adds hydrogens (if needed). 

The hydrogens that are added by AMSinput do not use a very advanced algorithm. For the protein itself it should be correct in most cases, assuming you have made sure that you have the proper protonation state of the residues.  However, if you have solvent molecules in your PDB file the hydrogens will be added properly but the solvent molecules will be oriented randomly. So no hydrogen bond structure in water for example. 

To avoid problems with the primitive algorithm AMSinput uses to add hydrogens you can obviously use some other tool to first  make a proper PDB or mol2 file for your protein including hydrogens. 

Once read in, you can use in principle all tools within the GUI as you like. For example, perform MM, QMMM or QUILD calculations for the protein structure. 