Importing and exporting your molecule
*************************************

Importing your molecule
=======================

**Importing from file: .ams, .t21, .xyz, .mol, .mol2, .pdb, .runkf, .adf, .band, .cif, .dmol, .rkf, .rxi, .rxkf ...**

You can also import your molecule from a file using the **File → Import Coordinates...** command. 

Many formats are handled explicitly. They are typically recognized by the file extension: 

``.ams, .band, .rxi``
   These files have been saved by AMSinput, BANDinput or ReaxFFinput.  Every detail belonging to atoms or bonds will be imported: not only the coordinates and bonds, but also things like atom properties (for example the color, the force field atom type, number of connectors, bond orders, and so on). 

``.t21, .runkf, .rxkf, .rkf``
   These are all results files produced by the ADF package. The coordinates and bond information will be read, if present. The files are binary, and will be recognized even if having a different extension. 

``.pdb, .mol2``
   Importing from a .pdb or .mol2 file will get the coordinates and the protein information (residues, PDB atom names and so on). For PDB files, only the ATOM information is read, thus no bond information. For MOL2 files, also the bond information is read. 

``.mol``
   Importing from a .mol file will get the coordinates and bond information. 

``.cif``
   Importing from a .cif file (Crystallographic Information File) will import the proper crystal structure. No bonds will be read. 

``.dmol``
   Files from the DMol program can also be read, and atom positions and periodic information is properly handled. No bond information will be read. 

``.xyz, any file type not recognized``
   Importing from an unknown text file, or a file with .xyz extension is rather flexible:  AMSinput needs three real numbers next to each other. These will be interpreted as x, y and z coordinate.  One additional integer or the abbreviation of an element is also needed to identify the kind of atom. 

   To be recognized as real, the real number must contain a '.' (dot), and at least one digit before or after the dot. Real numbers with exponents (E or D) are **not** recognized. 

   If an integer is used to specify the element (the nuclear charge), it may **not** contain a '.' (dot). 

   No bond information is read. 

If no bond information has been read, AMSinput tries to guess the bonds between the imported atoms. Guessed bonds might be completely wrong, or have the wrong bond order. 

Z-matrix import (internal coordinates) is not available. 

After using the 'Import Coordinates...' command the newly imported atoms are selected. This makes it easy to reposition them with respect to other atoms that may already be present, remove the automatically guessed bonds, or use other operations on the newly imported atoms and bonds. 

If you are importing many atoms, the molecule visualization will switch to wire-frame for the newly imported atoms. By default this happens when importing 50 atoms or more. You can change this limit via the **SCM → Preferences**. 

Copy/Paste between GUI modules, XYZ coordinates, SMILES or InChI strings
========================================================================

When Copying or Pasting with AMSinput, you need to make sure that the molecule editor has focus. Otherwise you will be copying or pasting one of the text input fields. To be sure, just click once in the drawing area before pasting. 

You can copy an XYZ-formatted geometry (for example from an ADF output file), and use the **Edit → Paste** command to import coordinates. Pasted text will be handled as when it had been import as .xyz or .cif file via the Import Coordinates command. 

Copy/Paste also works between the GUI modules, for example if you have several AMSinput windows. This will copy all information about your molecule: xyz, bonds, but also things like color of atoms or number of connectors. Only selected atoms will be copied. 

If you have the SMILES or InChI string of your molecule on your clipboard (for example, from wikipedia) you can just paste it in AMSinput. It will automatically be converted to a 3D structure (via OpenBabel). It works often, not always, so be sure to check your structure. 

Exporting your molecule
=======================

**Exporting to file: .xyz, .mol, .cif or .bgf**

Use the **File → Export Coordinates...** to export your current system.

In the file select box you will have the option to select the format. Currently supported are .xyz (default), .mol, .bgf and .cif (for periodic systems).

You can also Copy your system via the Copy menu. The contents of the clipboard will be identical to the .xyz file that would have been exported.
For periodic systems, the lattice vectors are included as special atoms VEC1, VEC2 and VEC3.
