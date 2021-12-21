
PyFrag: Activation Strain Model Analysis
========================================
The standalone script PyFrag allows one to analyse various quantities along a trajectory with ADF.
Usually such a trajectory results from either an internal reaction coordinate (IRC) or a linear transit (LT) calculation and is analyzed in the context of extended activation strain model (ASM).

.. seealso::
  
  :ref:`example pyfrag`

Requirements
------------
The trajectory can thereby either be a file containing concatenated molecular geometries in the xyz-format (see example below) or a T21 binary output file from a previous LT or IRC calculation with ADF.
ASM is based on the concept molecular fragments, which have to be defined by specifying the corresponding atomic indices for each fragment.
Furthermore, frequently used ADF input options can be imported from a separate input file (see :ref:`example <example pyfrag>`).

Running PyFrag
--------------
Running PyFrag is done by starting the corresponding Python script as follows:

::

  $AMSBIN/amspython $AMSHOME/scripting/standalone/pyfrag/PyFrag.py [options]

whereas the details of possible ``[options]`` are explained in the following

Specifying the Trajectory
-------------------------
The trajectory is specified by one of the following:

::

  --xyzpath <PATH>/trajectory.xyz
  --irct21 <PATH>/IRCtrajectory.T21
  --lt <PATH>/LTtrajectory.T21

Molecular Fragments
-------------------
The system can be split into an arbitrary number of disjoint subsystems, fragments.
Each fragment is defined by its own argument ``--fragment`` followed by the indices of atoms in that fragment: 

::

  --fragment 1 3 4 5 6 --fragment 2

ADF Options
-----------
The settings for the ADF calculations are retrieved from either a pyfrag-specific settings file ``adfsettings`` (see :ref:`example <example pyfrag>`).

::

  --adfinputfile adfsettings

or by individual command line arguments for each option, e.g.:

::

  --adfinput basis.type=TZ2P

Analysis Options
----------------
The following options control the quantities reported by PyFrag in the final results table:

Offsets for the strain energies in kcal/mol of the fragments (one argument for each fragment, corresponding to the order of the fragment definition above):

::

   --strain <StrainEnergy Fragment1> --strain <StrainEnergy Fragment2>

Bond length between selected pairs of atoms and equilibrium offset value in Angstrom

::

   --bondlength <AtomIndex1> <AtomIndex2> <offset value>

Angle length between selected triples of atoms and equilibrium offset value in degrees

::

   --angle <AtomIndex1> <AtomIndex2> <AtomIndex3> <offset value>

Hirshfeld charges of fragments

::

  --hirshfeld frag<FragmentNumber>

Atomic charges (Voronoi deformation density charges, VDD)

::

  --VDD  <AtomIndex1> [<AtomIndex2> [...]]

Orbital interaction energies for orbitals belonging to a point group symmetry irrep (specified by its symbol) of the whole system

::

  --irrepOI <IrrepSymbol>

Orbital energies within fragments can be either specified for a certain orbital in a given irrep specifically for HOMO and LUMO levels in each fragment

::

  --orbitalenergy <IrrepSymbol> <FragmentNumber> <OrbitalIndexWithinIrrep>
  --orbitalenergy frag<FragmentNumber> HOMO
  --orbitalenergy frag<FragmentNumber> LUMO

Orbital population numbers within fragments are again be either specified for a certain orbital in an irrep or for the HOMO or LUMO in each fragment 

::

  --population <IrrepSymbol> frag<FragmentNumber> <OrbitalIndexWithinIrrep>
  --population frag<FragmentNumber> HOMO
  --population frag<FragmentNumber> LUMO

Orbital overlaps between pairs of orbitals, e.g.

::

  --overlap frag<FragmentNumber> HOMO  frag<FragmentNumber> LUMO

or

::

  --overlap <IrrepSymbol> frag<FragmentNumber> <OrbitalIndexWithinIrrep> <IrrepSymbol> frag<FragmentNumber> <OrbitalIndexWithinIrrep>
