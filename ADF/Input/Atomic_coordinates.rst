.. index:: atomic coordinates 
.. index:: Z-matrix coordinates 
.. index:: internal coordinates 

.. _keyscheme ATOMS: 
.. _keyscheme SYSTEM: 


Atomic coordinates
******************

See also

* `Geometry, System definition section of the AMS manual <../../AMS/System.html>`__

Cartesian
=========

You can define the input atomic coordinates in the ``Atoms`` sub block key of the ``System`` key in AMS.
Note that in AMS one can not add an integer by which the atoms are numbered.

::

   System
      Atoms
         AtomType Coords {adf.F=Fragment}
         ...
      End
   End

``AtomType``
   The name of an *atom type*. It must begin with the standard one- or two-character symbol for the chemical element (*e.g.* H, He, Li,...). Optionally it may be appended by .text, where text is any string (not containing delimiters). Examples: ``H``, ``Mn.3``, ``Cu.dz-new``.

   **Note**: *Atom type* is not identical to *chemical element*. An atom type is defined by all characteristics of the basic atom to which it in fact refers: the nuclear charge, the basis functions, the frozen core, the density functional and any other features that were applied in generating that basic atom.  

``Coords``
   The xyz coordinates of the atom Example::

      ATOMS
         O  0.000000  0.000000   0.000000 
         H  0.758602  0.000000   0.504284 
         H  0.758602  0.000000  -0.504284 
      END

``adf.F=Fragment``
   Specifies that the atom belongs to a particular fragment. The fragment name must be of the form ``fragtype|n``, where fragtype is the name of one of the types of fragments in the molecule. The integer n, after the pipe ``|``, counts the individual fragments of that type. The numbering suffix ``|n`` is not required if there is only one fragment of that type. 

   When ``adf.f=fragment`` is omitted altogether, the fragment type is taken to be the *atom type* that was specified earlier on the same line. (The numbering ``|n`` is then added automatically by the program, by counting the number of times that this single-atom fragment type occurs in the list of atoms). 

   **note**: Input items are generally case insensitive. Exceptions are the names of files and directories. Since (to be discussed below) the name of the fragment type as it is defined under atoms (explicitly with the ``adf.f=option``, or implicitly as the name of the atom type) might also directly indicate the fragment file, the specification of fragment types is in principle case-sensitive. Errors may occur if you are sloppy in this respect.
   However, you must not give different fragment types names that differ only by case: at various places in the program fragment type names are compared in a case-insensitive way


.. index:: dummy atom

Z-Matrix
========

It is possible to specify the input geometry as a Z-Matrix.

::

   System
      Atoms Z-Matrix
         C
         H   1 1.089000
         H   1 1.089000  2  109.4710
         H   1 1.089000  2  109.4710  3  120.0000
         H   1 1.089000  2  109.4710  3 -120.0000
      End
   End

Only the first atom may be a dummy atom in case of a Z-matrix, use as chemical symbol XX for the dummy atom.


Orientation of Local Atomic Coordinates
=======================================

As discussed before the atomic positions are input with the key ATOMS. One option has thus far not been mentioned: the possibility to redefine the local coordinate frame of an atom. 

::

   ATOMS {type of coordinates}
      AtomType coordinates {adf.F=fragment} {Z="xx yy zz"} {X="xx yy zz"}
      ...
   end

Except for the z= option all aspects have been examined already before. 

``z="xx yy zz"``
   defines a reorientation of the local atomic z-axis; it is interpreted as a direction vector with components (xx,yy,zz) pointing away from the atom. In the local, reoriented frame the local atomic x-axis will be rotated to the plane defined by the directions of the molecular z-axis and the local atomic z-axis.  This feature can be used only for single-atom fragments (otherwise it is ignored). Its purpose is to give more flexibility in the analysis of the final molecular orbitals in terms of the atomic orbitals. In such a case it may be very helpful to redefine the orientation of say the p-orbitals of an atom. For instance, you may orient all p-orbitals towards the origin by specifying for each atom z= -x -y -z (with x,y,z the coordinates of that atom). By default the local and molecular z-axes are identical. 

``x="xx yy zz"``
   defines a reorientation of the local atomic x-axis; it is interpreted as a direction vector with components (xx,yy,zz) pointing away from the atom. Together with the z vector this defines the xz plane. The y axis is then given by the vector product :math:`\vec{z}  \times \vec{x}`.  This is used for analysis (see orientation of the z-axis). 


Symmetry Key
============

Note that this is a specification of the ``Symmetry`` key in the Engine ADF part of the input.
You can use the System%Symmetrize key in the AMS part of the input, such that AMS will symmetrize the coordinates.
ADF will not adjust coordinates.
Thus input atomic coordinates that are off from their correct positions, even if they are only slightly off, are not adjusted by ADF.
There exist a System%Symmetry key in the AMS part of the input, which can be used icw the System%Symmetrize key to symmetrize coordinates.
Note that the the symmetry used in AMS does not have to be the same as is used in ADF.

The point group symmetry and symmetry tolerance can be supplied. 

.. scmautodoc:: adf Symmetry

.. scmautodoc:: adf SymmetryTolerance


The point group symmetry specified in input with a Schönfliess type symbol puts restrictions on the orientation of the atomic system.
If symmetry is specified the user must take care of supplying the *Cartesian* coordinates in the appropriate orientation.
