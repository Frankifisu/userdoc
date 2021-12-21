
ForceField Engine Options
#########################

Details of the ForceField engine can be set via its input block. Some option are specific to UFF and others to other force fields.

Common options
**************

These options apply to any force field.

Type
====

There are a few predefined force field types, that, if used, require no other input.

.. scmautodoc:: forcefield Type


Non-bonded screening
====================

The long range interaction (dispersion and Coulomb) are the most expensive to evaluate. This gives you the option to screen the interaction more aggressively.

.. scmautodoc:: forcefield NonBondedCutoff

It is usually a good idea to add some "skin" to the cutoff above when it's used for computing a neighbor list for changing geometries 
(e.g. during molecular dynamics or geometry optimization). This way, the neighbor list will not need to be re-computed when atoms move a little. 
This may save some time because generating a neighbor list can be quite costly. The following option sets the thickness of the "skin":

.. scmautodoc:: forcefield NeighborListSkin

.. Note :: 

	This option also affects the cutoff used when generating a neighbor list in the real-space part of the Ewald summation but then it is added to the cutoff radius is used there.

Feedback
========

If you want to know more about the details of the force field you should crank up the verbosity.

.. scmautodoc:: forcefield Verbosity

Bonds usage
===========

Bonds can be specified in the input, still you may not want to use those. Here are some options to control this.

.. scmautodoc:: forcefield BondsUsage

Ewald summation
===============

For periodic systems the Ewald summation is performed for the Coulomb interaction. It has a couple of options:

.. scmautodoc:: forcefield EwaldSummation


Disabling energy terms
======================

By default all force field energy terms are calculated, however, you can disable each one of them individually.

.. scmautodoc:: forcefield EnergyTerms


Guessing or loading partial charges
===================================

The UFF forcefield has some very rudimentary partial charges guessing, only setting charges for atoms in water molecules. By default the partial charges in a force field calculation are zero. Essentially you will always need to specify atomic charges to make the results more realistic, either via the input or using one or the following options. 

See also example :ref:`LoadCharges <example LoadCharges>`, and :ref:`ChargedMolecules <example ChargedMolecules>`.

GuessCharges
------------

The simplest way is the use the GuessCharges key, that uses an engine that can calculate atomic charges. By default DFTB is used. DFTB is of course much more expensive than a forcefield, but if you run a MD calculation you can maybe afford a single DFTB calculation on the system.

.. scmautodoc:: forcefield GuessCharges

If you want to control the engine use the GuessChargesConfig key.

.. scmautodoc:: forcefield GuessChargesConfig


LoadCharges
-----------

You have more control over the charge guessing, by loading the charges of another calculation. This way you can set any engine specific detail, such as the basis set, or functional.

You can load charges form a previous calculation to be used as force field charges.

.. scmautodoc:: forcefield LoadCharges

.. _NONUFF:

Amber force field options
*************************

These options are relevant for the Amber and GAFF force fields:

.. scmautodoc:: forcefield AllowMissingParameters
.. scmautodoc:: forcefield CheckDuplicateRules
.. scmautodoc:: forcefield ForceFieldFile


.. _UFFBLOCK:

UFF options
***********

The following options are only relevant for the UFF force field:

.. scmautodoc:: forcefield UFF


.. _APPLENP:

APPLE&P force field options
***************************

The :ref:`ForceFieldFile <forcefield-key-ForceFieldFile>` key is mandatory and it should contain path to the APPLE&P forcefield file. This file is usually tailored for each system specifically.

Additionally, the following options are relevant for the APPLE&P force field.

.. scmautodoc:: forcefield DipoleConvergenceThreshold

The repulsion/dispersion and Coulomb interaction between atoms connected by a bond or by a valence angle are excluded in APPLE&P. 
Those between atoms connected by a diherdal (the so called 1-4 neighbors) may be scaled down 
and the scaling factors can be changed using the following options:

.. scmautodoc:: forcefield APPLE&P

