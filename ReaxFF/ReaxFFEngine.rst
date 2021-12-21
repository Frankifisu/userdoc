
.. _ReaxFFEngine:

ReaxFF input 
=========================

This section describes the input keywords to the ReaxFF AMS engine.

.. The ReaxFF AMS engine enables efficient :ref:`parallel calculations <parallelization>` using this parametrized reactive molecular mechanics potential. 

.. The engine shares all core routines with the  guaranteeing identical energies and forces between these two codes. 

.. seealso::

  - :ref:`ams_tasks`

..  - :ref:`reaxff_new_vs_old`

..  - `The standalone old ReaxFF program <../OldReaxFF/index.html>`__

Force field specification
-------------------------

The only input key required by the engine is ``ForceField``, used to select the :ref:`force field file <ffield>`. Force fields :ref:`included in the Amsterdam Modeling Suite <forcefields>` can be easily accessed using their file name, such as ``CHO.ff``.

.. scmautodoc:: reaxff ForceField
   :nosummary:



Recommended lattice convention
------------------------------

The ReaxFF engine supports molecular (free boundary), 1D-, 2D-, and 3D-periodic systems. Non-orthorhombic lattices are supported in an arbitrary orientation. However, the engine is slightly more computationally efficient when the cell is oriented according to the convention used in standalone ReaxFF, i.e. lattice vector ``c`` aligned with the ``z`` axis and vector ``b`` in the ``yz`` plane (zero ``x`` component). The ``Lattice`` block in the `system definition <../AMS/System.html>`__ then looks like this::

   System
      Lattice
        xx xy xz
         0 yy yz
         0  0 zz
      End
   End


.. _smoothpes:

Smoothened potential energy surface
-----------------------------------

The keywords below can be used to enable the **tapered bond orders**  and/or **improved torsion angle potentials**. Although the original ReaxFF torsion potential is the default to preserve backward compatibility, the corrected potentials eliminate energy discontinuities and work well with existing force fields. 

Using the tapered bond order (the ``TaperBO`` key) does not change the potential form at the chemically relevant distances so it can be used with any force-field. It may improve the energy conservation during MD and make geometry optimizations with ReaxFF converge to much tighter criteria.  The discontinuity and the correction for it are described in detail in `J. Phys. Chem. Lett. 10 (2019) 7215 <https://doi.org/10.1021/acs.jpclett.9b02810>`__.

.. scmautodoc:: reaxff TaperBO
   :nosummary:


The discontinuity at small bond orders in the expression for torsion angles and conjugation contributions can alternatively be corrected for using the ``Torsions 2013`` correction. 
The corresponding terms are given by f\ :sub:`10` (eq. 10b) and f\ :sub:`12` (eq. 11b) in the `original ReaxFF paper <https://doi.org/10.1021/jp004368u>`__. 
The new expression for each term in f\ :sub:`10` is :math:`\left(1 - e^{-2 \lambda_{23} \text{BO}^2} \right)` and in f\ :sub:`12` the new expression is :math:`\sin(\frac{\pi}{3} \text{BO})^4`. 
The new expressions ensure correct asymptotic behavior for the :math:`\frac{dE}{d\text{BO}}` for BO :math:`\rightarrow` 0. 

Another discontinuity in the torsion angle term is when one or both valence angles approach 180 degrees. It is described in detail in `J. Chem. Phys. 153 (2020) 021102 <https://doi.org/10.1063/5.0013906>`__, and can be enabled with ``FurmanTorsions Yes``.

.. seealso::

   :ref:`troubleshooting_geoopt`

.. scmautodoc:: reaxff Torsions
   :nosummary:

.. scmautodoc:: reaxff FurmanTorsions
   :nosummary:

Bond order and distance cutoffs
-------------------------------

.. scmautodoc:: reaxff BondDistanceCutoff 
   :nosummary:

.. scmautodoc:: reaxff BondOrderCutoff 
   :nosummary:

.. scmautodoc:: reaxff StrongBondCutoff
   :nosummary:

Non-reactive mode
-----------------

The engine can also be switched to a special non-reactive mode useful mainly for initial preparation of molecular dynamics simulations. This mode greatly reduces the occurrence of unwanted reactions when starting from an unrelaxed geometry. In these situations, we recommend running a short simulation with the ``NonReactive`` key to relieve the initial conformational strain and then restarting the MD run without this key.

Note that if you want to resume or extend an interrupted ``NonReactive`` run, it is recommended to also use the ``EngineRestart`` AMS key to supply the last ReaxFF ``.rkf`` file from the previous run. This enables the engine to load the bonding topology used during the previous run and ensure that the simulation is seamlessly restarted. If the ``EngineRestart`` key is not used, bonds will be re-detected in the first step and then preserved during the rest of the simulation.

.. scmautodoc:: reaxff NonReactive
   :nosummary:


.. _chargeequilibration:

Charge equilibration
--------------------

Details of the charge equilibration (electronegativity equalization method, EEM) procedure can be adjusted using the ``Charges`` block.

.. scmautodoc:: reaxff Charges

.. _chargeconstraints:

Charge constraints
^^^^^^^^^^^^^^^^^^

The net charge of an arbitrary group of atoms can be constrained to a particular value using the ``Constraint`` block.
This block can be repeated as needed to constrain multiple non-overlapping parts of the system.
To define charge constraints, first define appropriate `regions <../AMS/System.html#regions>`__, in the ``System`` block and then
set the ``Region`` key inside each ``Constraint`` block accordingly.

.. note::
   Unlike the similar MOLCHARGE constraints in standalone ReaxFF, it is not necessary for the constrained regions to span a consecutive range of atoms.
   It is also not necessary to define constraints for all atoms in the system. The necessary sum of charges of any unconstrained atoms will be determined from
   the overall net charge of the entire system, as set by the ``Charge`` key in the ``System`` block.

In the following example, we constrain the net charge of one water molecule in a dimer while the other molecule automatically assumes the opposite charge
to keep the whole system neutral::

   System
       Charge 0.0
       Atoms
           O -0.0509 -0.2754  0.6371 region=donor
           H  0.0157  0.5063  0.0531 region=donor
           H -0.0055 -1.0411  0.0658 region=donor
           O  0.0981  1.7960 -1.2550 region=acceptor
           H -0.6686  2.2908 -1.5343 region=acceptor
           H  0.8128  2.3488 -1.5619 region=acceptor
       End
   End

   Engine ReaxFF
       ForceField Water2017.ff
       Charges
           Constraint Region=donor Charge=0.1
           # The following constraint is implied and need not be specified explicitly.
           # It is only shown here as an example of multiple constraints in a single system.
           Constraint Region=acceptor Charge=-0.1
       End
   EndEngine

Sometimes it may be useful to disable the charge equilibration altogether and set the charges from input. This can be done using the ``reaxff.charge`` atom property, as shown in the example below::

   System
       Atoms
           O -0.0509 -0.2754  0.6371 reaxff.charge=-0.8
           H  0.0157  0.5063  0.0531 reaxff.charge=0.4
           H -0.0055 -1.0411  0.0658 reaxff.charge=0.4
           O  0.0981  1.7960 -1.2550 reaxff.charge=-0.8
           H -0.6686  2.2908 -1.5343 reaxff.charge=0.4
           H  0.8128  2.3488 -1.5619 reaxff.charge=0.4
       End
   End

