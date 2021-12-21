Builder (packmol)
*****************

To build systems consisting of many different molecules, randomly put together, the GUI includes the Builder. This is a graphical interface to the packmol program, using only a few possibilities of it. The most common use will be to set up a big system for  Molecular Dynamics with ReaxFF or DFTB. 

If you find using the Builder (and thus packmol)  useful, please give proper credit via the following reference

L.\  Martínez, R. Andrade, E. G. Birgin, J. M. Martínez. Packmol: A package for building initial configurations for molecular dynamics simulations. Journal of Computational Chemistry, 30(13):2157-2164, 2009.

The Builder allows you to compose your system of many replicas of some predefined molecules. These molecules are replicated as often as you want, giving a simulation box full with these molecules. Thus it is very easy to generate a liquid or a gas. 

To activate the Builder, use the **Edit → Builder** menu command. 

First you need to define the box into which the molecules will be generated. In the Builder panel you define the lattice vectors that define the unit cell. 

Next you define what molecules to add to your system. Press the + button to add more molecules, or press the - button in front of a line to remove that particular molecule. 

The 'Current' option will include whatever you have manually created on the left side. For example, some molecules to be solvated. Or some slab imported from BANDinput. 

The 'Fill box with' option allows you to select what molecule to use for filling. The geometry of the molecule must be available in a file with .xyz extension, and it should contain the coordinates and atom types of your molecule in XYZ format. Many typical molecules are included with AMSinput. When you press the folder button at the right side you will be able to select your molecule via a file-select browser. Or you can start typing a text in the field, and below it matching molecules will be shown (similar to the  molecule search).

As you may have more then one kind of molecule, you can also make mixtures of different molecules. 

Once you press the 'Generate Molecules' button, the actual packing of the molecules is done using  `Packmol <http://www.ime.unicamp.br/~martinez/packmol/>`__. 
