.. _PESPointExtraProperties:
.. index:: Dipole moment
.. index:: Atomic charges
.. index:: Polarizability

Dipole moment, Polarizability, Bond orders
##########################################

This page in the AMS manual describes the calculation of the dipole moment, the
polarizability, and bond orders.

.. scmautodoc:: ams Properties DipoleMoment Polarizability BondOrders
   :noref:
   :onlysummary:

Note that because these properties are tied to a particular point on the
potential energy surface, they are found on the :ref:`engine output
files<engine_output_files>`. Note also that the properties are not always
calculated in every PES point that the AMS driver visits during a calculation.
By default they are only calculated in *special* PES points, where the
definition of special depends on the :ref:`task<Tasks>` AMS is performing: For
a :ref:`geometry optimization<GeometryOptimization>` properties would for
example only be calculated at the final, converged geometry. This behavior can
often be modified by keywords special to the particular running task.


.. _Charges:
.. _DipoleMoment:
.. _Polarizability:
.. _DipoleGradients:

Charges, Dipole Moment, Polarizability
======================================

.. scmautodoc:: ams Properties Charges DipoleMoment DipoleGradients Polarizability
   :noref:
   :skipblockdescription:


.. _BondOrders:
.. _MoleculeDetection:
.. index:: Bond orders
.. index:: Molecule detection

Bond orders & Molecule detection
================================

Many engines can determine bond orders between atoms. For engines based on
force fields, these might just be the bond orders used internally by the force
field, while for quantum mechanical engines the bond orders are usually
determined by analyzing the results of the quantum mechanical calculation, e.g.
the electronic density. We refer users to the manuals of the respective engine
for details.

.. scmautodoc:: ams Properties BondOrders
   :noref:
   :skipblockdescription:

Based on the bond orders, the AMS driver can analyze the atomic connectivity
graph in order to determine which sets of atoms together constitute molecules.
This allows for example to monitor the changes in molecular composition during
a reactive molecular dynamics calculation. For :ref:`molecular
dynamics<MolecularDynamics>` calculations this option is enabled by default.
For other :ref:`tasks<Tasks>` the molecular analysis can explicitly be
requested in the ``Properties`` block.

.. scmautodoc:: ams Properties Molecules
   :noref:
   :skipblockdescription:

Details of the molecule detection are configured in a dedicated block:

.. scmautodoc:: ams Molecules
