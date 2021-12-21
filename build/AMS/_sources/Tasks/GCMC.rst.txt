
.. index:: GCMC
.. index:: Grand canonical Monte Carlo

.. _GCMC:

Grand Canonical Monte Carlo (GCMC)
**********************************


.. toctree::
   :maxdepth: 2

.. tip::
  Take a look at the `GCMC tutorial <../../Tutorials/MolecularDynamicsAndMonteCarlo/GCMCLiSBattery.html>`__ and learn how to setup a GCMC calculation.


General info
============

**About Monte Carlo / the Grand Canonical Ensemble**

It is best to read a bit about Monte Carlo and ensembles before working with the GCMC code. Almost every book or review text on molecular simulations will do, for example: Frenkel D, Smit B. Understanding molecular simulation: from algorithms to applications. Academic Press; 2002. 672 p.

Wikipedia also has some pages of interest:

+  `http://en.wikipedia.org/wiki/Monte_Carlo_method <http://en.wikipedia.org/wiki/Monte_Carlo_method>`__

+  `http://en.wikipedia.org/wiki/Grand_canonical_ensemble <http://en.wikipedia.org/wiki/Grand_canonical_ensemble>`__

It is important to note that this method heavily relies on random numbers, and simulations are thus non-repeatable in detail, but should converge to the same answer.

**About the AMS GCMC code**

The GCMC code was originally developed for standalone Reaxff by Thomas Senftle, working as a Graduate Student at Penn State University under the supervision of Dr. Adri van Duin [#ref1]_ [#ref2]_. The original version was a wrapper code that called an external executable to perform the reaxff minimization step and energy calculation, and relied on file modification and parsing to steer the reaxff code and get the results back.

The code was later rewritten by Hans van Schoot (SCM), in close collaboration with Thomas Senftle, to integrate it directly into the ADF-ReaxFF code. The current version is an AMS re-implementation so the method can be used with almost any engine supported by AMS (support for 3D periodic boundary conditions by the engine is currently a requirement).


Method Details
==============

**Overview**

The GCMC method will perform a number of Grand Canonical Monte Carlo trial moves (set by the ``Iterations`` option of the ``GCMC`` input block), and accept or reject them based on the energy produced by the geometry optimization of the trial geometry for the given engine. The Monte Carlo algorithm will always accept a step if it results in a decrease of the energy, and accept steps that go up in energy with a probability. This section will give some details about how the method works.

**MC Moves (Insert/Delete/Displace/ChangeVolume)**

The GCMC method currently supports 4 types of MC Moves: Insert, Delete, Displace (sometimes also called Move), and ChangeVolume. The first three MC moves are always available and the ChangeVolume becomes available only ``ChangeVolume`` option is set to True. The first three move types change coordinates of atoms in the system, while the ChangeVolume move changes the lattice only.

On every MC iteration, the method first selects one of the molecules defined by the ``Molecule`` input blocks at random and then selects an applicable MC move type. If there are no molecules of this type in the system then no Delete or Displace is attempted. If the selected molecule has the ``NoAddRemove`` option set then the Insert and Delete moves will not be attempted. If no MC move is possible with the selected molecule type then another one is selected or a VolumeChange is attempted, if allowed. If no moves with any of the provided molecules is possible (i.e. if all molecules have ``NoAddRemove`` set to True, there is nothing to displace and the volume is fixed) then the program will stop.

The Insert and Displace MC move will rotate the molecule randomly and put it at a random position, and then check if the minimum interatomic distance between the molecule and the rest of the system is within the ``MinDistance`` and ``MaxDistance`` boundaries. If the condition is not satisfied, a new set of coordinates is generated and the check is performed again. This is repeated up to ``NumAttempts`` times before stopping with an error.

The volume change is controlled by the ``VolumeChangeMax`` keyword. This sets the volume change limit, and it should be a value between between 0 and 1. The new volume will be calculated as: V\ :sub:`new` = exp(random(-1:1)*VolumeChangeMax)*V\ :sub:`old`.

**Calculating the chemical potential**

The chemical potential of the molecule (or atom) reservoir is used when calculating the Boltzmann accept/reject criteria after a MC move is executed. This value can be derived from first principles using statistical mechanics, or equivalently, it can be determined from thermochemical tables available in literature sources.

For example, the proper chemical potential for a GCMC simulation in which single oxygen atoms are exchanged with a reservoir of O2 gas, should be equal to 1/2 the chemical potential of O2 at the temperature and pressure of the reservoir [#ref1]_:

:math:`\mu^{MC}_{O}(T,P) = \frac {1} {2} \mu^{MC}_{O2}(T,P) = \frac {1} {2} \left [ \mu^{ref}_{O2}(T,P_{ref}) + kT ln \left ( \frac {P} {P_{ref}} \right ) - E^{diss}_{O2} \right ]`

where the reference chemical potential :math:`\mu^{ref}_{O2}(T,P_{ref})` is the experimentally determined chemical potential of O2 at T and P\ :sub:`ref`, :math:`kT ln \left ( \frac {P} {P_{ref}} \right )` is the pressure correction to the free energy, and :math:`E^{diss}_{O2}` is the dissociation energy of the O\ :sub:`2` molecule.


**Calculating energies**

Because the GCMC simulation adds and deletes atoms or molecules during the runtime, it cannot directly compare the AMS energies for the MC acceptance criteria: inserting a molecule will usually lower the total energy of the system, causing the MC to always accept it, and always reject a deletion. To compensate this, the GCMC method calculates a "corrected" MC energy to compare the trial energy with, consisting of the previously accepted AMS energy and a correction depending on the move:

:math:`E_{old}^{MC} = E_{old}^{AMS} + \mu^{MC}`  for an Insert move;

:math:`E_{old}^{MC} = E_{old}^{AMS} - \mu^{MC}`  for a Delete move;

:math:`E_{old}^{MC} = E_{old}^{AMS}`  for a Displace move;

:math:`E_{old}^{MC} = E_{old}^{AMS} - P (V_{new} - V_{old}) + N_{inserted} ln \left ( \frac {V_{new}^{avail}}{V_{old}^{avail}} \right ) kT` for a ChangeVolume move.

Here, :math:`\mu^{MC}` is the chemical potential of the inserted/deleted molecule, P is the pressure, V is the volume, and N\ :sub:`inserted` is the total number of MC molecules. The "new" and "old" subscripts refer to the current and the last accepted values. The V\ :sup:`avail` values are calculated from the MC-available volume as described below.

**Calculating volumes**

The available volume can be calculated in a few different ways, depending on the ``VolumeOption`` setting:

+ *Free*: volume = total volume - occupied volume - specified vacuum volume (``NonAccessibleVolume``)

+ *Total*: volume = total cell volume

+ *Accessible*: volume = specified accessible volume (``AccessibleVolume``)

+ *FreeAccessible*: volume = specified accessible volume (``AccessibleVolume``) - occupied volume

Here, the occupied volume is calculated as a sum of volumes of atoms that do not belong to the MC part of the system (i.e. that were not inserted during calculation and are not ``Removables``). The volume of an atom is calculated using the average of the covalent and the Van der Waals radii of the atom defined in the atominfo module used throughout AMS.

The ``AccessibleVolume`` and ``NonAccessibleVolume`` keywords can be used to get a more accurate available volume.

**Acceptance criteria**

An MC move is always accepted if the AMS energy is lower than the corrected MC energy of the last accepted MC move, or if the energy increase is small enough. If the new energy is higher, the code generates a random number between 0 and 1, and accepts the move if the random number is greater than:

::

   prob = preFactor * exp(-Beta*deltaE)

The prefactor is calculated (for insert and delete moves) using the deBroglie wavelength of the inserted molecules, the number of inserted molecules and the available MC volume of the system.





Input
=====

The GCMC functionality in AMS is triggered using the following Task key:

::

    Task GCMC

.. scmautodoc:: ams GCMC
   :onlysummary:

The following keys are common for all GCMC calculations and should always be specified. The ChemicalPotential value should correspond to the :math:`\mu^{MC}` expression above, and not to the experimental chemical potential :math:`\mu^{ref}`, which means it should include the (engine-dependent) free molecule's energy.

.. scmautodoc:: ams GCMC Molecule Iterations Temperature
   :nosummary:
   :noref:
   :skipblockdescription:

The following keys are related to Insert and Displace moves.

.. scmautodoc:: ams GCMC NumAttempts MinDistance MaxDistance
   :nosummary:
   :noref:
   :skipblockdescription:

The following keys influence computation of the acceptance probability and of the MC energy correction.

.. scmautodoc:: ams GCMC UseGCPreFactor VolumeOption AccessibleVolume NonAccessibleVolume
   :nosummary:
   :noref:
   :skipblockdescription:

The following keys apply to the ensemble choice and options for the Mu-PT ensemble.

.. scmautodoc:: ams GCMC Ensemble VolumeChangeMax Pressure
   :nosummary:
   :noref:
   :skipblockdescription:

The GCMC code can insert multiple atom/molecule types in a single simulation, so it needs to keep track of what atom belongs to which insert. This information is automatically stored and updated when insertion/deletion/moving of atoms or molecules during the simulation, but is by default unknown for the atoms of the starting geometry. The GCMC code will therefore by default not modify the atoms in the original input in the MC trial moves. The ``Restart`` key and the ``Removables`` block are two ways to provide information about Deletable/Movable atoms/molecules in the input structure. If the ``Restart`` key is present the ``Removables`` block will be ignored.

.. scmautodoc:: ams GCMC  Restart Removables
   :nosummary:
   :noref:
   :skipblockdescription:


An example of the Removables block:

::

  Removables
    Oatom 41
    O2  44 45
    Oatom 42
    Oatom 43
  End

This example specifies that 5 atoms belong to 4 different GCMC molecules of two different types, ``Oatom`` and ``O2``. Thus in addition to the main input ``System`` there should be at least two additional Systems defined, one called "Oatom" (containing one atom) and the other "O2" (containing two atoms). The first one was inserted three times (atoms 41, 42, and 43) and the second one was inserted once.

Finally there are more technical keywords:

.. scmautodoc:: ams GCMC MapAtomsToOriginalCell
   :nosummary:
   :noref:
   :skipblockdescription:

Note that the ``GeometryOptimization`` block is also read by the GCMC task, and the settings used for the individual optimizations. The documentation for these keywords can be found in the :ref:`Geometry Optimization<GeometryOptimization>` section of this manual.



Output
======

In addition to the standard KF variables in the "History" section on ``ams.rkf`` such as "Coords" and "Energy", the following GCMC-specific variables are also created for each accepted MC step:

* *MCMove* - integer index of the MC move.
* *MCMoveType* - string containing the type of the MC move.
* *MCMolecule* - string containing the name of the inserted/displaced/removed molecule.
* *Converged* - a Fortran logical value containing the convergence status of the given geometry.

Results of a GCMC calculation are stored in the GCMC section of the RKF file, in a number of variables. The following variables contain a summary of the MC statistics up to and including the latest step:

* *NIterMCtried* - the latest iteration number.
* *NIterMCaccept* - the number of accepted MC moves.
* *NIterMCreject* - the number of rejected MC moves.
* *NMCacceptAdd* - the number of accepted MC molecule insertions.
* *NMCacceptRemove* - the number of accepted MC molecule removals.
* *NMCacceptMove* - the number of accepted MC molecule moves.
* *NMCacceptVolume* - the number of accepted volume changes.
* *NMCrejectAdd* - the number of rejected MC molecule insertions.
* *NMCrejectRemove* - the number of rejected MC molecule removals.
* *NMCrejectMove* - the number of rejected MC molecule moves.
* *NMCrejectVolume* - the number of rejected volume changes.

The following variables (actually arrays of the size ``Iterations``) in the GCMC section contain the detailed information about all MC moves in the current simulation. Only the first *NIterMCtried* elements of each array contain valid data.

* *HistoryAccepted* - MC move status value (1 - accepted, 0 - rejected, -1 - not done yet).
* *HistoryAMSEnergy* - the AMS energy (the :math:`E^{AMS}` above).
* *HistoryMCEnergy* - the corrected MC energy (:math:`E^{MC} = E^{AMS} - \Sigma \mu^{MC}_i`, where :math:`\Sigma \mu^{MC}_i` is the total chemical potential of all inserted molecules).
* *HistoryVolume* - the simulation box volume.
* *HistoryMoveType* - the MC move type index (0 - insert, 1 - delete, 2 - displace, 3 - change volume). The name of the move type with index *i* can be found in the *MoveType(i)* variable.
* *HistoryMoleculeType* - the inserted/deleted/displaced molecule type index. The name of the molecule type with index *i* can be found in the *MoleculeName(i)* variable.
* *HistoryMoleculeIndex* - the inserted/deleted/displaced molecule index within its type.

.. only:: html

  .. rubric:: References

.. [#ref1] T.P. Senftle, R.J. Meyer, M.J. Janik, A.C.T. van Duin, *Development of a ReaxFF potential for Pd/O and application to palladium oxide formation*, `J. Chem. Phys. 139, 044109 (2013) <https://doi.org/10.1063/1.4815820>`__

.. [#ref2] T.P. Senftle, A.C.T. van Duin, M.J. Janik, *Determining in situ phases of a nanoparticle catalyst via grand canonical Monte Carlo simulations with the ReaxFF potential*, `Catalysis Communications 52, 72–77 <https://doi.org/10.1016/j.catcom.2013.12.001>`__
