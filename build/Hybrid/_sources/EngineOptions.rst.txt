
Hybrid Engine Options
#####################


.. _subengines:
.. _engineid:

Sub-engines and EngineIDs
*************************

Inside the Hybrid engine input block one or more sub-engine blocks can be defined. 
These have exactly the same format as regular engine blocks.
There is, however, one extra feature: the ``EngineId``. 
Optionally, a unique name can be added to the engine definition as an extra string, serving as an identifier. 
By default the identifier is simply the engine name. 
The extra string allows the user to select the same engine multiple times, each time  with different settings. 

This is an example, where we use the same engine (ADF) with two different basis sets, 
computing the average result.

::

    Engine Hybrid
        Energy # we want the average energy obtained with the DZ and TZP basis sets
           Term EngineId=adf-tzp factor=0.5
           Term EngineId=adf-dz factor=0.5
        End

        Engine ADF adf-tzp   # here afd-tzp is the EngineID
          Basis Type=TZP
        End

        Engine ADF adf-dz
          Basis Type=DZ
        End

    EndEngine


EngineIDs are for instance used in the technical example :ref:`QUILD <example QUILD>`, 
which tests that EngineIDs are case-insensitive.

.. scmautodoc:: hybrid Engine

Linear Combination of Energy Terms
*******************************************

The block ``Energy`` triggers a QUILD-like setup,
allowing the energy to be defined as a linear combination of energy terms.
Each energy term can be computed with a different engine.


See the :ref:`basic QUILD example<basicQUILDExample>`. 
As you can see capping can be enabled per energy term, and the user can set a charge per term 
(for the corresponding region).

.. scmautodoc:: hybrid Energy

QM/MM
*****
The alternative to the ``Energy`` block is the ``QMMM`` block,
which triggers a two-layer computation.
The embedding type can be selected with the ``Embedding`` key,
for which mechanical or electrostatic can be selected.
The former option triggers a specific linear combination of three energy terms,
and can therefore also be set up using the ``Energy`` block
(see :ref:`basic QUILD example<basicQUILDExample>`).

See the :ref:`basic electrostatic embedding example<basicQMMMExample>`. 
Capping can be disabled, and charges can be set for the QM and MM regions.


.. scmautodoc:: hybrid QMMM

Capping
*******

Whether of not capping is enabled is set inside the ``Energy`` and ``QMMM`` blocks. 
If enabled then the user can influence the position and type of the capping atom with
the ``Capping`` sub-block.

.. scmautodoc:: hybrid Capping

For a specific application of QM/MM with capping atoms 
see this :ref:`example <example AtomicInfoForCappingAtom>`.

Restarts
********

In a molecular dynamics run or geometry optimization, the geometries at subsequent steps are often very similar.
Generally, efficiency can be gained by providing the engines with information from the previous step ("restart"), 
as this might speed up the SCF or charge equilibration procedure, if applicable. 
To the forcefield engine, this might avoid re-loading of the database, guessing bonds, etc. at every step.
By default all sub-engines are provided with restart information.
It can be switched off with the ``RestartSubEngines`` key.

.. scmautodoc:: hybrid RestartSubEngines



Charges per region
******************

The user can specify charges per region associated with each energy term. 

Depending on the setup the charges can be set with the 
``Energy%Term%Charge`` or the ``QMMM%mmCharge`` and ``QMMM%mmCharge`` keys.

For a QM engine the charge for a region determines the number of electrons in the region defined in the energy term.  
For the ForceField engine, charges are specified per atom, and they should add up to the charge specified for the region.

Linear Combination of Energy Terms
==================================

When the Linear Combination of Energy Terms feature is selected, but using the ``Energy`` block, 
the energy is a linear combination of independent calculations. 
It is in this spirit that the total charge is considered to be

.. math::

  Q = \sum_i^N w_i \; Q^\text{engine(i)}\big(region(i)\big)

In the QMMM setup the total charge is the sum of the charge of the mm region and the qm region.


Electrostatic Embedding
=======================

In general, the charges for sub-regions should be consistent with the charge specified for the total system.
However, in the case of an electrostatic embedding computation with capping atoms,
the sum of charges of the subsystems used in the computation of the five energy terms
is allowed to deviate from the total system charge.

.. math::

   E = E^{MM}(E) + E^{QM}\big(\text{A}_C(V^\text{E})\big) + E^\text{MM}_\text{nonelstat}(\text{A+E}) - E^\text{MM}_\text{nonelstat}(\text{A}_C) - E^\text{MM}_\text{nonelstat}(\text{E})

The MM region that will be passed to the MM engine (term 1) will often have a fractional charge,
due to un-capped dangling bonds.
The fractional charge of the QM-region however (term 2), should be corrected by the capping atom charges,
to yield a chemical system that optimally resembles the full system.
As a result, the sub-region charges do not need to add up to the total charge of the system.

