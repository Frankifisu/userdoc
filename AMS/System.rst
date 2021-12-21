.. _SystemDefinition:

Geometry, System definition
###########################

The definition of the system to simulate, i.e. the positions and types of the
nuclei, the total charge, and potentially lattice vectors, is enclosed in the
``System`` block:

.. scmautodoc:: ams System Atoms Lattice FractionalCoords AllowCloseAtoms GeometryFile Symmetrize LatticeStrain SuperCell Charge BondOrders
   :onlysummary:

.. index:: Geometry
.. index:: Lattice

Geometry, Lattice
-----------------

The geometry of the system is specified with the ``Atoms`` and ``Lattice``
blocks.

.. scmautodoc:: ams System Atoms Lattice FractionalCoords
   :noref:
   :nosummary:

The ``Atoms`` block contains one line per atoms, similar to the lines found in
an ``.xyz`` file: First the name of the element, then three real numbers
representing the coordinates of that atom in Angstrom. The following ``Atoms``
block shows how one would define a water molecule::

   System
      Atoms
         O   0.0   0.0       0.59372
         H   0.0   0.76544  -0.00836
         H   0.0  -0.76544  -0.00836
      End
   End

Note that it is possible to specify a different unit of length in the header of
the block (that is in the line after the keyword opening the block) by putting
the name of the unit in ``[`` and ``]`` brackets. So the same water molecule
could also be specified as follows::

   System
      Atoms [Bohr]
         O   0.0   0.0       1.12197
         H   0.0   1.44647  -0.01580
         H   0.0  -1.44647  -0.01580
      End
   End

.. index:: Z-matrix

It is also possible to specify the input geometry as a Z-Matrix, by putting the
string ``Z-Matrix`` in the header of the block::

   System
      Atoms Z-Matrix
         C
         H   1 1.089000
         H   1 1.089000  2  109.4710
         H   1 1.089000  2  109.4710  3  120.0000
         H   1 1.089000  2  109.4710  3 -120.0000
      End
   End

.. _Lattice_vectors:
.. index:: Lattice vectors

Periodic systems require the specification of 1 (for chains), 2 (for slabs) or 3
(for bulk) lattice vectors in addition to the nuclear coordinates. Every lattice
vector is specified on a separate line of three numbers, representing the
vectors x,y and z-component. Note that for chain systems, the single lattice
vector **must** point along the x-axis, while for slab systems the two lattice
vectors **must** be in the xy-plane. Consider the following input for graphene::

   System
      Atoms
         C   0.0   0.0      0.0
         C   1.23  0.71014  0.0
      End
      Lattice
         2.46  0.0      0.0
         1.23  2.13042  0.0
      End
   End

.. index:: Fractional coordinates

As with the ``Atoms`` block, the length unit in which the lattice vectors are
given can be changed by specifying the desired unit in the header of the block
(enclosed in ``[`` and ``]``). It is also possible to define a system given the
fractional coordinates of the atoms using the ``FractionalCoords`` keyword.
The numbers in the ``Atoms`` block are then interpreted as fractional
coordinates according to the lattice vectors in the ``Lattice`` block. Note
that for chain and slab systems, the coordinates perpendicular to the periodic
direction (z and y for chains, z for slabs) are of course still in Angstrom (or
alternatively the unit set in the header of the ``Atoms`` block).  Using the
``FractionalCoords`` keyword we could specify the geometry of table salt
(NaCl) as follows::

   System
      Lattice
         0.0   2.75  2.75
         2.75  0.0   2.75
         2.75  2.75  0.0
      End
      FractionalCoords True
      Atoms
         Na  0.0  0.0  0.0
         Cl  0.5  0.5  0.5
      End
   End

Instead of specifying the geometry of the system directly in the input file it
can also be read from an external file.

.. scmautodoc:: ams System GeometryFile
   :noref:
   :nosummary:
   :skipblockdescription:

Note that the ``GeometryFile`` key replaces both the ``Atoms`` and the
``Lattice`` blocks in the input. So if you specify the ``GeometryFile`` keyword
in the input, the ``Atoms`` and ``Lattice`` blocks must not appear there. At the
moment only the :ref:`extended XYZ file format<ExtendedXYZ>` is supported.


Modifying the geometry
======================

Finally there are a number of keywords that *modify* the system geometry:

.. index:: Super cell
.. scmautodoc:: ams System Symmetrize LatticeStrain SuperCell SuperCellTrafo PerturbCoordinates PerturbLattice MapAtomsToUnitCell
   :noref:
   :nosummary:
   :skipblockdescription:

These modifications are applied immediately after the system block is read. To
the rest of AMS (and the input) it looks exactly as if the modified system was
specified explicitly in the ``System`` block input. That means that the
``SuperCell`` keyword is not easily usable with input options that require the
specification of atom indices, e.g. the :ref:`constraints<Constraints>` block.
Note that the randomization of the coordinates is applied after a potential
supercell creation.

.. index:: Symmetrization
.. index:: Symmetry

.. _Symmetry:

Symmetry
--------

Symmetry can be used in AMS optimizations of molecules and of periodic structures.

In case of molecules at the start of an AMS calculation one can symmetrize an almost symmetric structure.
In the :ref:`Appendix Symmetry<orientation requirements>` one can find molecular orientation requirements that AMS needs such that AMS can use the (sub)symmetry of a molecule.
If the system is symmetrized (and no symmetry is given in the System block key) the molecular structure is rotranslated into this standard orientation.
In the :ref:`Appendix Symmetry<SCHOENFLIES>` one can also find Schönfliess symbols for molecular point groups and symmetry labels that are used in AMS for molecules to label normal modes.

.. scmautodoc:: ams System Symmetrize Symmetry
   :onlysummary:
   :noref:
   :collapselongchoicesinsummary:

.. scmautodoc:: ams Symmetry
   :onlysummary:
   :noref:

.. scmautodoc:: ams UseSymmetry
   :onlysummary:
   :noref:


.. scmautodoc:: ams System Symmetrize Symmetry
   :noref:
   :nosummary:
   :skipblockdescription:

.. scmautodoc:: ams Symmetry
   :nosummary:
   :skipblockdescription:

.. scmautodoc:: ams UseSymmetry
   :nosummary:



.. _Regions:

Regions
-------

.. index:: Regions

Some options of the AMS driver and its engines require specifying a subset of a
system's atoms. For example one might want to freeze part of the system in a
molecular dynamics calculation. We refer to these subsets of atoms as
"regions". Atoms are assigned to regions by specifying the region names behind
the atomic coordinates in the ``Atoms`` block of the input::

   System
      Atoms
         C       1.22110608      -0.00000000       1.65928963     region=ring_1
         C       0.37734253      -1.16134090       1.65928963     region=ring_1
         C       0.37734253       1.16134090       1.65928963     region=ring_1
         C      -0.98789557      -0.71774815       1.65928963     region=ring_1
         C      -0.98789557       0.71774815       1.65928963     region=ring_1
         H       2.30849293      -0.00000000       1.64874914     region=ring_1
         H       0.71336355      -2.19550724       1.64874914     region=ring_1
         H       0.71336355       2.19550724       1.64874914     region=ring_1
         H      -1.86761001      -1.35689810       1.64874914     region=ring_1
         H      -1.86761001       1.35689810       1.64874914     region=ring_1
         Fe      0.00000000       0.00000000       0.00000000
         H       0.71336355       2.19550724      -1.64874914     region=ring_2
         H       0.71336355      -2.19550724      -1.64874914     region=ring_2
         C       1.22110608      -0.00000000      -1.65928963     region=ring_2
         C       0.37734253       1.16134090      -1.65928963     region=ring_2
         C       0.37734253      -1.16134090      -1.65928963     region=ring_2
         C      -0.98789557       0.71774815      -1.65928963     region=ring_2
         C      -0.98789557      -0.71774815      -1.65928963     region=ring_2
         H       2.30849293      -0.00000000      -1.64874914     region=ring_2
         H      -1.86761001       1.35689810      -1.64874914     region=ring_2
         H      -1.86761001      -1.35689810      -1.64874914     region=ring_2
      End
   End

In the above example of a ferrocene molecule, we have created two separate
regions for the two cyclopentadienyl rings. The region names (``ring_1`` and
``ring_2`` in the example above) can be freely chosen by the user. Note that an
atom can be in more than one region, in which case the region names should be
separated by commas::

   System
      Atoms
         ...
         Mg  0.0  0.0  0.0    region=metal_centers,mol_1
         ...
      End
   End

The region names given by the user can then be referred to for input keywords
requiring the specification of a region.

Technically the region is handled as an :ref:`atomic attribute <AtomAttributes>`.

Charge, atomic masses, input bond orders
----------------------------------------

.. index:: Atomic masses
.. index:: Isotopes

AMS allows to set user-defined masses for particular atoms. This can be used to
simulate isotopes of different atoms. Masses are specified by adding the
desired mass (in Dalton) at the end of the atom's line.  The following input
shows the system specification for a heavy water molecule::

   System
      Atoms
         O   0.0   0.0       0.59372
         H   0.0   0.76544  -0.00836    mass=2.014
         H   0.0  -0.76544  -0.00836    mass=2.014
      End
   End

(Observe that the mass specified this way is an example of the :ref:`atomic attributes <AtomAttributes>` system.)

Finally the ``System`` block also contains the specification of the system's
total charge as well as optionally defined bond orders, which might be needed by
engines implementing force fields.

.. index:: Charge
.. scmautodoc:: ams System Charge BondOrders
   :noref:
   :nosummary:
   :skipblockdescription:

Note that the specified bond orders are currently only used by the ForceField engine.


.. _ExternalFields:
.. index:: Electric field
.. index:: Point charges

Homogeneous electric field and multipole charges
------------------------------------------------

A homogeneous electric field and multipole charges can be requested at the AMS level. Currently this option is supported by the engines ADF, BAND, DFTB, and MOPAC.

**Homogeneous electric field:**

::

   System
      ElectrostaticEmbedding
         ElectricField ex ey ez
      End
   End

.. scmautodoc:: ams System%ElectrostaticEmbedding ElectricField
   :nosummary:
   :skipblockdescription:


**Point and multipole charges:**

::

   System
      ElectrostaticEmbedding
         MultipolePotential
            Coordinates
               x y z   q   py pz px
               x y z   q   py pz px
               ...
            End
         End
      End
   End

.. scmautodoc:: ams System%ElectrostaticEmbedding MultipolePotential
   :noref:
   :nosummary:
   :skipblockdescription:


.. note::

   When running geometry optimizations (or other similar tasks) in combination with point charges, you should be aware that the system might end up on top of the point charge(s), resulting in non-physical situations. You should consider using :ref:`constraints <Constraints>`, :ref:`restraints <restraints_addon>` or explicitly setting :ref:`rigid motions <scmautodoclist-ams-RigidMotions>` options.


.. _LoadSystem:

Load a System from file
-----------------------

.. index:: Restart (geometry)

Instead of specifying the system to simulate in the ``System`` block of the
input, it is also possible to read the system used in a previous calculation
from the binary ``.rkf`` result files of AMS. This is done with the
``LoadSystem`` block in the input:

.. scmautodoc:: ams LoadSystem

Note that the ``LoadSystem`` block is mutually exclusive with the ``System``
block: The system *either* needs to be specified in the input, *or* loaded from
a previous results file.

Any ``.rkf`` file written by AMS should be suitable to load a system from. For
:ref:`engine output files<engine_output_files>` the loaded geometry is just the
one for which the engine was invoked when it wrote this file. For the :ref:`main
result file<main_output_file>` ``ams.rkf`` written by the AMS driver, which
geometry is loaded depends on the :ref:`task <Tasks>` that AMS was performing
when this file was written. Generally the ``ams.rkf`` file contains two systems:

* The input system corresponding just to the ``System`` block that was read in
  by AMS. This system is written to the ``InputMolecule`` section on the
  ``ams.rkf``, and can be loaded from there using the ``LoadSystem%Section``
  keyword. This can be useful in order to repeat a previous AMS calculation
  for the same system, but with different settings, e.g. a different engine.

* The system which was the result of a previous AMS calculation, e.g. a geometry
  optimization or transition state search. This system is written to the
  ``Molecule`` section on the ``ams.rkf``. What exactly is considered the
  resulting geometry of a calculation depends in the :ref:`task <Tasks>` of the
  previous calculation. (For tasks that do not change the geometry (like a single
  point calculation) or where no configuration is particularly special (e.g. a
  PES scan), the result system is normally just the same as the input system.)


Atom attributes
---------------

.. _AtomAttributes:

There is in general the possibility to add text after the coordinates of an atom, we call these atomic attributes. The text should be of the form key=value, separated by spaces::


   System
      Atoms
         O   0.0   0.0       0.59372   key1=1 key2=y
         H   0.0   0.76544  -0.00836   file=ams.rkf
         H   0.0  -0.76544  -0.00836
      End
   End

You can enter any arbitrary key/value list, but that will have no effect in general. Although there is one important effect that atoms with different atomic attributes (even unrecognized ones) are considered different elements during the symmetry detection.

The order in which keys are specified has no effect.

Examples of atomic attributes are the region, and mass.


Force field related extensions
------------------------------

For forcefield there are two dedicated :ref:`atomic attributes <AtomAttributes>`, the ForceField.Type and ForceField.Charge. Obviously these attributes are ignored by all other engines, although it can reduce the symmetry of the system::

   System
      Atoms
         O   0.0   0.0       0.59372   ForceField.Type=O ForceField.Charge=-0.1
         H   0.0   0.76544  -0.00836   ForceField.Type=H ForceField.Charge=+0.05
         H   0.0  -0.76544  -0.00836   ForceField.Type=H ForceField.Charge=+0.05
      End
   End


Load charges for a forcefield into regions
==========================================

When you want to use a forcefield, the charges obtained by a previous calculation can be loaded into a specific region (with the same molecule). Currently the order of the atoms has to be the same for this to work.

Once loaded, it is as if the user had typed in the ForceField.Charge attributes.

.. scmautodoc:: ams System LoadForceFieldCharges
   :noref:
   :nosummary:
   :skipblockdescription:


Load forcefield atom types
==========================

After you have done a forcefield calculation the atom types are stored. You can load those for a next calculation. 

Once loaded, it is as if the user had typed in the ForceField.Type atom attributes.

.. scmautodoc:: ams System LoadForceFieldAtomTypes
   :noref:
   :nosummary:
   :skipblockdescription:
