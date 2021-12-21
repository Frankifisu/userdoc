Atom typing behavior
####################

To use a classical forcefield each atom should be given a type, and a partial charge. The power of the UFF forcefield is that this atomtyping is done automatically. 
For other force fields the atomtyping for most systems still has to be done by hand, possibly with the help of an external program. Unlike UFF parameters, the availabe parameters for the other available force fields typically cover only a fraction of all chemical elements. Nonetheless, experimental atomtyping options are available for small organic molecules (GAFF), and for biological systems (AMBER). 

UFF
***
Atom typing is the process of matching MM atom types to elements. For example, a Carbon atom becomes a C_1, C_2, C_3 or C_R, depending on the number (and type) of bonds it has to neighboring atoms. UFF is capable of finding a matching MM atom type on its own, but might not always succeed in doing so. When doing calculations with UFF, it is important to check the beginning of the output file, as the program will print the detected MM atom types there. You can also take matters into your own hands, and tell UFF what MM atom types you want it to use (see the section on Input and examples).

The atom typing in UFF is mostly controlled by the elements and mmatomtypes parameter files, however, some part of it is hidden in the code itself and is (at the moment) not accessible to users. This is done by UFF to differentiate between:

+ Carbon: double-bonded sp2 carbon (C_2) vs aromatic carbon (C_R), if any of the orders are close to 2, it's C_2.

+ Oxygen: having a bond to silicon gives O_3_z; otherwise, having bond order of 1.44 or higher gives O_R, provided that the partner is not a hydrogen. Otherwise, it's just an O_3.

+ Sulfur: having a bond order greater than 1.3 gives aromatic S_R.

By default, zero charges are used, unless a water molecule is detected.

Other forcefields
*****************

Automatic atomtyping via an experimental integration of the Antechamber toolkit is available for the Generalized AMBER Force Field (GAFF) for small organic molecules. This option was introduced in the 2020 release of AMS, and is still considered experimental and disabled by default. 

.. seealso::
   :ref:`Antechamber integration for GAFF forcefields <antechamber>`

Some atomtyping functionality for biological systems can be accessed via the GUI, using pdb files as input. A pdb file can be loaded into amsinput and then under the regions the residues can be found. Still, charges need to be set by hand.

Custom force field parameters can be provided as forcefield files. The two supported formats are ".ff" (originating from the ADF and QUILD programs) and the much more widely used amber ".dat" files.

