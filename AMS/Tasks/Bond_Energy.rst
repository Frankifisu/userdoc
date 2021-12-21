.. index:: Bond energy calculation

.. _Bond energy:

Bond energy calculations
========================

The way to calculate bonding energies is always the same, regardless of the engine. It is about combining ground state energies for several systems.

.. _Ground state energy:

Ground state energy
-------------------

Let system A have a ground state energy E(A)

The ground state energy of a system is obtained by a full relaxation with respect to the geometry coordinates and (if relevant) to the electronic degrees of freedom.
In case of periodic materials the lattice vectors need relaxation as well.

Electronic degrees of freedom are specific for the method underpinning the engine. A simple force field may have a charge equilibration scheme , whereas more advanced engines such DFT- and DFTB-based ones have orbitals. The electronic relaxation can become a non-trivial problem in case of :ref:`open shell <Open shell systems>` systems.

Formation energy
----------------

Say we have a reaction of two molecules (A and B) forming a new one (C).

A + B -> C

The interaction energy follows from three :ref:`ground state <Ground state energy>` calculations

E(bond) = E(C) - E(A) - E(B)

Let us look at a slightly more complicated reaction. The (metastable) material Octanitrocubane with the formula C\ :sub:`8` ( NO \ :sub:`2`  )\ :sub:`8` can be formed from 8 CO\ :sub:`2` molecules and four N\ :sub:`2` molecules. The formation energy is

E(bond) = E(Octanitrocubane) - 8 E(CO\ :sub:`2`) - 4 E(N\ :sub:`2`)

the result being positive as this reaction is highly endothermic.

Atomization energies
--------------------

Let us now look at atomization energies. For instance, the cohesive energy the NaCl crystal is

E(cohesive energy) = E(NaCl-crystal) - E(Na-atom) - E(Cl-atom)

(Atomization energies can also be calculated for molecules.)

For engines with electronic degrees of freedom, the tricky part here is how to calculate the atomic energies, in particular E(Cl-atom), because they are open shell systems. See the notes on a :ref:`atomic corrections <Atomic corrections>`.

Of course you need to weigh the atomic energies by how often they occur in the system (molecule or crystal).

Chemisorption energies
----------------------

What is the adsorption energy of a molecule on a surface?

The main thing here is whether the "real" system has translational symmetry. For instance in an experiment this may be the case and correspond to a certain coverage. This can be perfectly modeled in a periodic calculation

E(chemisorption) = E(mol\@surface) - E(mol) - E(bare surface)

You need to choose the right super cell to get the correct coverage (how many adsorbed atoms per unit cell).

If the experiment is about the adsorption of a single molecule you need to try to converge the result with progressively larger super cells.

The other main issue is that almost always in the experimental setup the surface is macroscopically thick. Therefore the slab thickness is an issue to be tested. Fortunately, often less than 10 layers are needed.


.. _Atomic corrections:

Atomic corrections
------------------

Sometimes we need to calculate the ground state energy of a single atom. As there are no geometric variables, the only degrees of freedom are electronic. In general atoms are :ref:`open shell <Open shell systems>` systems.
The idea is to let the engine run without any restrictions imposed on the spin-polarization, or the symmetry of the orbitals. 

One possible trick is to run two atoms quite far away (10-20 angstrom), thus reducing the exact spherical symmetry. 

Calculating atomic corrections can be very tricky, as there may be many nearly degenerate orbitals near the fermi level. Also SCF convergence can be very difficult. There is not a single solution for all atoms.

.. _Open shell systems:

Open shell systems
------------------

The idea is to let the engine run without any restrictions imposed on the spin-polarization, or the symmetry of the orbitals. 

Calculating open shell systems can be very tricky, as there may be many close lying states (of which the lowest is searched for). Also SCF convergence can be very difficult.

From a theoretical point of view these states should ultimately be described by multi-determinantal wave functions, lacking from methods such as DFT.

There may be no automatic way to find the absolute minimum. If possible try to avoid the need to do such calculations.


Impurities
----------

Let's say that we want to introduce a single impurity in a crystal. Currently we do not support such a method.  But using periodic boundary conditions (PBCs) we can approximate this.

Say we want to introduce a single Li atom in an Al crystal. This can be done by considering progressively larger super cells.

First we make a 2x2x2 super cell, with 8 Al atoms, then we insert one Li, thus modeling an "impurity", with a  1/8  Li/Al ratio, rather than a 1/infinity. With bigger super cells this approximation becomes better.

The insertion energy is then

E(8Al+Li) - E(8Al) - E(Li-atom)

See also the comments for Atomization energies.
