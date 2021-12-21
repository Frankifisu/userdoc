Creating a molecule object
==========================

FlexMD can be run trough the interactive python interpreter in the ADF package. To start it, run: $AMSBIN/amspython in a terminal, followed by: 

::

    from scm import flexmd

Note that it is also possible, and usually more convenient, to write your FlexMD code in a file and then to execute this file. To do this, type all the commands you would use in the interactive interpreter in a file, and then enter $AMSBIN/amspython myFlexMDjob.py in a terminal (after changing to the directory where the file was stored of course). 

Most FlexMD jobs will start with importing FlexMD and creating an MDMolecule object. This can be done by starting from a geometry in xyz or pdb format, or by manually adding the atoms in the FlexMDjob.py file. Geometries can be generated in the ADF GUI, and then be exported to xyz file. For more details on the MDMolecule object, run $AMSBIN/amspython, import flexmd and call help(flexmd.mdmolecule). 

::

    from scm import flexmd
    myMol = flexmd.MDMolecule('myGeometryFile.xyz')

Some ForceJobs require the system to be periodic. If we create an MDMolecule object from a pdb file that includes periodic information, the periodic boundary conditions are automaticcaly imported. If the information is not there, we can add it to the MDMolecule object: 

::

    myMol = flexmd.pdb.set_box([50.0,25.0,100.0])

Info on set_box (and other functions, such as set_cellvectors, and write_pdb) can be found using help(flexmd.pdbmolecule). 

It is also possible to write the info in the MDMolecule object to a pdb file. to do so, call pdb.write_pdb('mypdbfile.pdb') on the myMol object: 

::

    myMol.pdb.write_pdb('mypdbfile.pdb', box=True)

