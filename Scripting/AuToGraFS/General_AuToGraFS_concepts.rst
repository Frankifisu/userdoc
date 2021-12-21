General AuToGraFS Scripting concepts
####################################

AuToGraFS relies on the concept of underlying nets common to many structures. These nets, or topologies can be found in the `RCSR <http://rcsr.anu.edu.au/>`_ and `EPINET <http://epinet.anu.edu.au/>`_ databases. Once implemented, AuToGraFS will follow these blueprints to generate a framework from building units of compatible geometries. Since these geometries are ideal objects, and most chemical structures are distorted, an optimization step using `UFF <../../ForceField/index.html>`_ is necessary for the building units to "snap into place". Correct handling of bonding information and UFF atom types are crucial to the generation of correct structures.

Components of AuToGraFS
-----------------------

The Fragment class
``````````````````

This is a slightly modified version of the native ASE Atoms object, designed to hold essential data for UFF postprocessing. This englobes the uff atom types, and the bonding information.  

::

     from scm.autografs.fragment import Fragment
     from ase import Atoms

     line = Fragment(ase.Atoms("X2", positions=...),
                     mmtypes=["H_", "H_"], 
                     bonds = [[0,0,1],[0,0,1],[1,1,0]],
                     shape="linear",
                     unit=None,
                     name="a_line_has_no_name")

Where mmtypes is a list of the UFF atom types symbols, ordered as the corresponding atoms in the structure, and bonds is a symmetric 
`numpy array <https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.array.html>`_ of size equal to the number of atoms. The i,j elements in the bonds array are the bond order between atom i and atom j of the structure. These bond orders should follow the UFF conventions (1.5 for aromatic, 0.5 for coordination bonds, 0.001 for hydrogen bonds...).
The shape holds information for AuToGraFS about the connectivity of the fragment. Each dummy atom, with symbol "X" in ASE, represents a point of connection between two fragments. In the above example, the shape is clearly "linear". This is used to check compatibility between a fragment and a given topology.
The unit of a fragment is set internally by AuToGraFS and is of no interest here.
The name of a fragment is used only for logging purposes.
Individual building blocks of a framework are manipulated through the Fragment class.
It is possible to export a fragment from the GUI using edit -> framework -> export fragment. If the UFF atom types are not specified, an automatic typing script will take care of it.


The Model class
```````````````

This is a container class that holds in one place the topology of a framework and the correctly positioned fragments. Most of the postprocessing methods found in AuToGraFS are Model methods.

::

     from scm.autografs import *

     model = autografs.Model(...)

     # view the framework in adfinput. set clean to False to keep dummy atoms.
     model.view(clean=True, verbose=True)

     # write the name.ams and name.run files
     model.write(name="framework", clean=True, verbose=True)

     # returns a Fragment, with correct bonding information and mmtypes
     # if indices is True, it also returns the index of the corresponding fragment in the model for each atom
     atoms = model.get_atoms(self, clean=False, indices=False)

     # returns a supercell of the framework as a Fragment 
     supercell = model * (2,2,2)

     # deletes a fragment in the framework. if no index is given, the fragment will be chosen at random.
     # the defects will cap with hydrogen the empty spaces. returns a Fragment
     # here, a linker at random will be deleted
     model.insert_defect(indices=None, centers=0, linkers=1)

     # flip a linear object
     model.flip_fragment(index=the_fragment_index)

     # rotates a linear object around its axis by angle in degrees
     model.rotate_fragment(index=the_fragment_index, angle=85.0)

     # Will add a functional group to the selected fragment on a random hydrogen
     # if and only if the hydogen is connected to a carbon.
     # for more precise handling, use the GUI for now.
     model.functionalize_fragment(functional_group="NH2", index=the_fragment_index)

The Autografs class
```````````````````

This class is the builder in itself. Given a path to a database of building units in .inp format (exportable via the GUI), it will generate any valid framework from a topology name, a center and linker name or objects, and optionally a pillar name or object. The linkers, centers and pillars objects have to be passed as Fragment .

::

  from scm.autografs import *
  from random import choice

  # create the generator and update the database of building units
  mofgen = autografs.Autografs(refresh_database=True, verbose=True, path="path/to/my/fragments/")

  # choose a topology from the available one given no center or linkers
  topologies = mofgen.get_available_topologies(center=None, linker=None)
  topology = choice(topologies)

  # choose a center in the list of available centers for the topology
  centers = mofgen.get_available_centers(topology=topology, linker=None)
  center = choice(centers)

  # choose a linker in the list of available linkers for the topology and center
  linkers = mofgen.get_available_linkers(topology=topology,  center=center)
  linker = choice(linkers)

  # modify the linker by changing all hydrogens to fluorine 
  linker_structure = mofgen.database[linker]
  linker_symbols = linker_structure.get_chemical_symbols()
  linker_structure.set_chemical_symbols(["F" if l=="H" else l for l in linker_symbols])

  # generate the framework using multiprocessing tools and automatic scaling of unit cell
  framework = mofgen.make(lable="my_framework", topology=topology, center=center, linker=linker, pillar=None, form_factor=None, parallel=True)

  # visualize in adfinput
  framework.view()

do not forget to run a quick UFF optimization after generation to optimize lattice and fragment into an optimal configuration.


About the databases of building units
-------------------------------------

AuToGraFS uses both a binary database format, and structures in the DemonNano file format from which the binary is compiled.
To ask AuToGraFS to use a custom directory containing .inp files, simply pass the directory to the path argument when initializing the constructor.
The ".inp" file format should be formatted like the following example.

::

   Data: SBUtype = linker
   Data: shape = linear
   Data: name = benzene
   GEOMETRY CARTESIAN
   C       0.00000000     -1.39103633      0.00000000     MMTYPE=C_R   QMMM=MM BOND=2/1.5:6/1.5:12/1.0
   C      -1.20606758     -0.69440959      0.00000000     MMTYPE=C_R   QMMM=MM BOND=1/1.5:3/1.5:8/1.0
   C      -1.20606758      0.69440959     -0.00000000     MMTYPE=C_R   QMMM=MM BOND=2/1.5:4/1.5:10/1.0
   C      -0.00000000      1.39103633      0.00000000     MMTYPE=C_R   QMMM=MM BOND=3/1.5:5/1.5:11/1.0
   C       1.20606758      0.69440959      0.00000000     MMTYPE=C_R   QMMM=MM BOND=4/1.5:6/1.5:7/1.0
   C       1.20606758     -0.69440959     -0.00000000     MMTYPE=C_R   QMMM=MM BOND=1/1.5:5/1.5:9/1.0
   H       2.02806392      1.16933783      0.00000000     MMTYPE=H_    QMMM=MM BOND=5/1.0
   H      -2.02806392     -1.16933783      0.00000000     MMTYPE=H_    QMMM=MM BOND=2/1.0
   H       2.02806392     -1.16933783      0.00000000     MMTYPE=H_    QMMM=MM BOND=6/1.0
   H      -2.02806392      1.16933783      0.00000000     MMTYPE=H_    QMMM=MM BOND=3/1.0
   X       0.00000000      2.09099413      0.00000000     MMTYPE=H_    QMMM=MM BOND=4/1.0
   X       0.00000000     -2.09099413      0.00000000     MMTYPE=H_    QMMM=MM BOND=1/1.0
   END


Using the overhauled Atom Typer
-------------------------------

Both AuToGraFS and the GUI now use a new python library for the assignment of UFF types to atoms and generation of the bonding matrix. 
The process goes as follows:

::

   from scm.autografs import atomtyper

   # instantiate the typer on a readable molecule file (e.g: "mol.cif")
   typer = atomtyper.MolTyper("path/of/fileToType")

   # choose the UFF library. options are uff and uff4mof
   library = read_db("uff4mof")

   # actual typing is done here
   typer.type_mol(library)

   # prints the bond matrix as a numpy array
   # item i, j of matrix is the bond order between atoms i and j
   print typer.get_guibonds()

   # print a list of UFF types in order
   print typer.get_mmtypes()

   # write a SCM-UFF input file with correct info
   typer.structure.write(name="mytypedmol")
