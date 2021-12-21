
.. _enginevsstandalone:

ReaxFF Engine Features Vs. Old Standalone Program
=================================================

Introduction
************

Starting with AMS2018, ReaxFF is an engine for the AMS driver, thus sharing
many of the features and input syntax with the other engines in the Amsterdam
Modeling Suite.

Before AMS2018, ReaxFF was run as a standalone program.  The older standalone
program ("Old ReaxFF") can still be run from the command-line, also in AMS2020.
Some features are only available in this older program.

.. seealso::

   `Old Standalone ReaxFF manual <../OldReaxFF/index.html>`__

The engine shares all core routines with the standalone program, guaranteeing
identical energies and forces between these two codes. 

Feature comparison
********************

Some features of the old standalone ReaxFF program have been implemented into the AMS driver, others into the ReaxFF engine, and some are currently not available in the new implementation.
The table below indicates how certain features can be activated.

.. csv-table:: 
   :delim: ,
   :header: Feature, New implementation, Old implementation

   "0D, 1D, 2D periodicity", `AMS driver <../AMS/System.html#geometry-lattice>`__, not available
   ACKS2, :ref:`force field file <ACKS2>`, `old manual entry <../OldReaxFF/Miscellaneous.html#acks2-atom-condensed-kohn-sham-dft-approximated-to-second-order>`__
   Adsorption analysis, `AMS driver <../AMS/Properties.html#bond-orders-molecule-detection>`__, `old manual entry <../OldReaxFF/Properties.html#adsorption-analysis>`__
   Bond boost, `AMS driver <../AMS/Tasks/Molecular_Dynamics.html#bond-boost-method>`__, `old manual entry <../OldReaxFF/BondBoost.html>`__
   ChemTraYzer, `AMS utilities <../AMS/Utilities/ChemTraYzer.html>`__, `old manual entry <../OldReaxFF/ChemTraYzer.html>`__
   CMAES FF optimizer, `ParAMS  <../params/index.html>`__, `old manual entry <../OldReaxFF/CMAESFFOptimizer.html>`__
   CVHD, `AMS driver <../AMS/Tasks/Molecular_Dynamics.html#collective-variable-driven-hyperdynamics-cvhd>`__ , `old manual entry <../OldReaxFF/CVHD.html>`__
   Elastic wall restraint, not available, `old manual entry <../OldReaxFF/Miscellaneous.html#elastic-wall-restraint>`__
   eReaxFF, :ref:`force field file <eReaxFF>`, `old manual entry <../OldReaxFF/eReaxFF.html>`__
   External electric fields, `AMS driver <../AMS/System.html#homogeneous-electric-field-and-multipole-charges>`__,  `old manual entry <../OldReaxFF/Miscellaneous.html#external-electric-fields>`__
   Force-bias Monte Carlo, `AMS driver <../AMS/Tasks/Molecular_Dynamics.html#force-bias-monte-carlo-fbmc>`__, `old manual entry <../OldReaxFF/fbMC.html>`__
   Force field parametrization, `ParAMS <../params/index.html>`__, `old manual entry <../OldReaxFF/FFOptimizer.html>`__
   Grand-canonical Monte Carlo, `AMS driver <../AMS/Tasks/GCMC.html>`__, `old manual entry <../OldReaxFF/GCMC.html>`__
   Local atomic temperature, not available, `old manual entry <../OldReaxFF/Properties.html#local-atomic-temperature>`__
   LG dispersion, :ref:`force field file <LG_dispersion>`, `old manual entry <../OldReaxFF/Miscellaneous.html#lg-dispersion>`__
   Molecular charge constraints, :ref:`ReaxFF Engine <chargeconstraints>`, `old manual entry <../OldReaxFF/Miscellaneous.html#molecular-charges>`__
   Molecule gun, `AMS driver <../AMS/Tasks/Molecular_Dynamics.html#molecule-gun-adding-molecules-during-simulation>`__, `old manual entry <../OldReaxFF/molgun.html>`__
   NEMD (thermal conductivity), `AMS driver <../AMS/Tasks/Molecular_Dynamics.html#non-equilibrium-md-nemd>`__, `old manual entry <../OldReaxFF/Properties.html#nemd-methods-for-thermal-conductivity>`__
   Per-atom stress tensor, not available, `old manual entry <../OldReaxFF/Properties.html#atomicstresstensor>`__
   Tapered bond orders, :ref:`ReaxFF engine <smoothpes>`, `old manual entry <../OldReaxFF/Miscellaneous.html#correction-for-small-bond-orders>`__
   Temperature profile along axis, `AMS driver <../AMS/Tasks/Molecular_Dynamics.html#trajectory-sampling-and-output>`__, `old manual entry <../OldReaxFF/Properties.html#temperature-profile-along-coordinate-axis>`__
   Volume regimes, `AMS driver <../AMS/Tasks/Molecular_Dynamics.html#lattice-deformations-volume-regimes>`__, `vregime.in Training Course <../OldReaxFF/index.html#other-reax-ff-manuals>`__



Differences in execution
************************

**To run ReaxFF as an AMS engine** (recommended), run the ``ams`` executable and specify ``Engine ReaxFF``:

.. code-block:: none

   "$AMSBIN"/ams <<EOF
       # ams input
       Engine ReaxFF
          ForceField CHO.ff
       EndEngine
   EOF


**To run ReaxFF as a standalone program** (not recommended unless necessary), run the ``reaxff`` executable. The files ``control``, ``geo``, etc., must exist in the current working directory. For more information, see the `Old ReaxFF manual <../OldReaxFF/index.html>`__.

.. code-block:: none

   "$AMSBIN"/reaxff

.. The ReaxFF AMS engine enables efficient :ref:`parallel calculations <parallelization>` using this parametrized reactive molecular mechanics potential. 


