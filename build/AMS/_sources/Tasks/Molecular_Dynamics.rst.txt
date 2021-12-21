.. index:: Molecular dynamics
.. index:: MD

.. _MolecularDynamics:

Molecular dynamics
##################

Molecular dynamics (MD) can be used to simulate the evolution of a system in
time.

.. seealso::

  * :ref:`Examples`
  * `AMS GUI Tutorial <../../Tutorials/MolecularDynamicsAndMonteCarlo/index.html>`__
  * :ref:`MD trajectory analysis tool <trajectory_analysis>`

To perform a MD simulation, first select the corresponding ``Task``::

   Task MolecularDynamics

All aspects of the simulation can then be configured using the
``MolecularDynamics`` block.

.. scmautodoc:: ams MolecularDynamics
   :onlysummary:

General
=======

The time evolution of the system is simulated by numerically integrating the
equations of motion. A velocity Verlet integrator is used with a time step set
by the ``TimeStep`` key. The MD driver will perform ``NSteps`` timesteps in
total.

Because the overall computational cost depends on ``NSteps`` but not on
``TimeStep``, it is desirable to set the timestep as large as possible to
maximize the sampled timescale with a given computational budget. However,
numerical integration errors grow rapidly as the timestep increases. These
errors will cause a loss of energy conservation, crashes, and other artifacts.
It is thus important to set the ``TimeStep`` value carefully, as its optimal
value strongly depends on the studied system and simulated conditions.

As a rule of thumb, reasonable timesteps for systems not undergoing chemical
reactions are 10-20 times lower than the period of the fastest vibration mode.
Systems containing hydrogen atoms at room temperature can thus be accurately
simulated using a 1 fs timestep. Longer timesteps can be safely used for systems
containing only heavy atoms (vibration periods scale with the square root of the
atomic mass). Conversely, the timestep needs to be made shorter for
high-temperature simulations. The same also applies to simulations of chemical
reactions, which are usually accompanied by significant transient local heating.
The default timestep of 0.25 fs should work for most of these cases.

.. scmautodoc:: ams MolecularDynamics NSteps TimeStep
   :nosummary:
   :noref:
   :skipblockdescription:

During a long simulation, numerical integration errors will cause some
system-wide quantities to drift from their exact values. For example, the system
may develop a nonzero net linear velocity, causing an overall translation or
flow. Non-periodic (molecular) and 1D-periodic systems may also develop nonzero angular momentum
(overall rotation) and a Brownian motion of their center of mass through space.
These problems are corrected by periodically removing any accumulated drift.
This feature can be controlled using the ``Preserve`` key.

.. scmautodoc:: ams MolecularDynamics Preserve
   :nosummary:
   :noref:
   :skipblockdescription:


.. _ConstrainedMD:

Constrained molecular dynamics
==============================

There are two types of constraint available for MD: frozen atoms and Shake/Rattle.
Atoms can be kept frozen using the ``Atom`` or ``AtomList`` keys of the ``Constraints`` top-level input block.

.. scmautodoc:: ams Constraints Atom AtomList
   :nosummary:
   :noref:
   :skipblockdescription:

.. note::

   During simulations with a changing simulation box (NpT, NpH), the absolute Cartesian coordinates of the frozen atoms cannot be kept fixed. In this case, their fractional cell coordinates are maintained at the original values.

The Shake/Rattle constraints are specified using the Shake input block:

.. scmautodoc:: ams MolecularDynamics Shake
   :nosummary:
   :noref:
   :skipblockdescription:

.. note::

   Currently it's only possible to constrain bonds that are part of the System. This means that bonds not specified in the System block or not found by the engine will not be constrained.


.. index:: Restart (molecular dynamics)

(Re-)Starting a simulation
==========================

The state of a system at the beginning of a simulation is defined by the
positions and momenta of all atoms. The positions can be set in the input or
loaded from a file as described under :ref:`SystemDefinition`. Initial
velocities are then supplied using the ``InitialVelocities`` block.

Probably the most common way to start up a simulation is to draw the initial
velocities from a Maxwell-Boltzmann distribution by setting ``Type=Random`` and
``Temperature`` to a suitable value. Alternatively, velocities can be loaded
from an ``ams.rkf`` file produced by an earlier simulation using
``Type=FromFile`` and ``File``. This is the recommended way to start a
production simulation from the results of a short preparation/equilibration run.

Velocities of all atoms in units of Å/fs can also be explicitly defined in the
``Values`` block after setting ``Type=Input``. This is mainly useful to repeat
or extend simulations done by other programs. For example, velocities can be
extracted from the ``vels`` or ``moldyn.vel`` files used by the `standalone
ReaxFF <../../ReaxFF/index.html>`__ program. A simple AWK script is supplied in
``scripting/standalone/reaxff-ams/vels2ams.awk`` to help with the conversion.

.. scmautodoc:: ams MolecularDynamics InitialVelocities
   :nosummary:
   :noref:
   :skipblockdescription:

The MD module also supports exact restarts of interrupted simulations by
pointing the ``Restart`` key to an ``ams.rkf`` file. This will restore the
entire state of the MD module from the last available checkpoint (if the
previous simulation was interrupted) or from the final state (if the previous
simulation ended after ``NSteps``). An earlier trajectory can thus be seamlessly
extended by increasing ``NSteps`` and using ``Restart``.

.. note::

   ``Restart`` should be combined with ``LoadSystem`` from the same ``ams.rkf``
   to restore the atomic positions.

.. warning::

   The ``Restart`` feature is only intended for exact restarts, so the rest of
   the ``MolecularDynamics`` settings should be the same as in the original run.
   Only ``NSteps`` and engine settings (contents of the ``Engine`` block) can
   always be changed safely across restarts.

Although some MD settings (such as the trajectory sampling options) can in
practice be changed without problems, changing others (such as thermostat or
barostat settings) will cause the restart to fail or produce physically
incorrect results. It is thus strongly recommended to only use ``Restart`` for
exact continuation and ``InitialVelocities Type=FromFile`` together with
``LoadSystem`` otherwise.

.. scmautodoc:: ams MolecularDynamics Restart
   :nosummary:
   :noref:
   :skipblockdescription:


Thermostats and barostats
=========================

By default, the MD simulation samples the microcanonical (NVE) ensemble.
Although this is useful to check energy conservation and other basic physical
properties, it does not directly map to common experimental conditions. The
canonical (NVT) ensemble can be sampled instead by applying a ``Thermostat``,
which serves as a simulated heat bath around the system, keeping its average
temperature at a set value.

.. index:: Thermostat

AMS offers two thermostats with drastically different properties, mode of
operation, and applicability, selected using the ``Type`` key:

Berendsen
   The Berendsen friction thermostat drives the system to a particular target
   temperature by rescaling the velocities of all atoms in each step. This
   ensures rapid (exponential) convergence of the temperature with a time
   constant ``Tau``. However, this thermostat produces an incorrect velocity
   distribution and should thus be avoided in all situations where correct
   energy fluctuations are important. Additionally, using a too short time
   constant ``Tau`` tends to cause incorrect equipartition of energy between
   different degrees of freedom in the system, leading to the "flying ice cube"
   phenomenon. The time constant ``Tau`` should thus be set as large as possible
   to limit these artifacts while still providing sufficient temperature
   control. Common values of ``Tau`` for condensed-phase systems lie between 100
   fs (strong damping, rapid convergence) and 10 ps (weak coupling with minimal
   artifacts).

   This thermostat is mainly useful for systems far from equilibrium, for
   example during the initial preparation and equilibration phase of a
   simulation. The ``NHC`` thermostat should be preferred where possible.

NHC
   This enables a chain of coupled Nosé-Hoover thermostats. This method
   introduces artificial degrees of freedom representing the heat bath and
   ensures correct sampling of the canonical ensemble. The combined total energy
   of the system and the heat bath is conserved and shown in the GUI as
   ``Conserved Energy``. Checking this quantity for drift and artifacts thus
   offers a valuable test of the correctness of the simulation. This thermostat
   exhibits oscillatory relaxation with a period of ``Tau``. It is thus not well
   suited for systems starting far from equilibrium, because the oscillations
   may take long to settle. The time constant ``Tau`` should be at least
   comparable to the period of some natural oscillation of the system to ensure
   efficient energy transfer. It is commonly on the order of hundreds of
   femtoseconds, although higher values may be used if weak coupling is desired.

Multiple independent thermostats can be used to separately control different
non-overlapping regions of the system at the same time. This is done by first defining appropriate
:ref:`Regions` in the ``System`` block and then specifying the ``Thermostat`` block
multiple times with the ``Region`` key of each thermostat set to an appropriate region expression.

.. scmautodoc:: ams MolecularDynamics Thermostat
   :nosummary:
   :noref:
   :skipblockdescription:

Just like using a ``Thermostat`` to control the temperature of the system, a
``Barostat`` can be applied to keep the pressure constant by adjusting the
volume. This enables sampling the isenthalpic-isobaric (NpH) ensemble by using
only a barostat or the isothermal-isobaric (NpT) ensemble by combining a
barostat and a thermostat. Unlike thermostats, a barostat always applies to the
entire system and there can thus be at most one barostat defined.

.. index:: Barostats

AMS offers two barostats with similar properties to the related thermostats:

Berendsen
   The Berendsen friction-like isobaric ensemble method rescales the system in
   each step to drive the pressure towards a target value. Similarly to the
   ``Berendsen`` thermostat, the relaxation is exponential with a time constant
   ``Tau``. Similar considerations for the choice of ``Tau`` apply as in the
   case of the thermostat, but the value of ``Tau`` for the barostat is
   usually at least several times higher than the corresponding ``Tau`` used for
   the thermostat. This barostat does not have any conserved quantity.

MTK
   This enables the Martyna-Tobias-Klein extended Lagrangian barostat, which
   generates a true isobaric ensemble by integrating the cell parameters as
   additional degrees of freedom. This barostat is derived from the
   Andersen-Hoover isotropic barostat and the Parrinello-Rahman-Hoover
   anisotropic barostat. Like the ``NHC`` thermostat, it exhibits oscillatory
   relaxation unsuitable for systems far from equilibrium. This barostat must
   always be combined with a ``NHC`` thermostat. One instance of such thermostat
   coupled to the atoms as usual, while a second instance is created internally
   and coupled to the cell degrees of freedom.

.. scmautodoc:: ams MolecularDynamics Barostat
   :nosummary:
   :noref:
   :skipblockdescription:

.. index:: Temperature (molecular dynamics)
.. index:: Pressure (molecular dynamics)

Temperature and pressure regimes
--------------------------------

Arbitrary temperature and pressure regimes can be generated by setting
``Temperature`` or ``Pressure`` to a list of values, corresponding to the
successive set points. This needs to be accompanied by a ``Duration`` key
specifying the length of each regime segment in steps::

   Thermostat
      Temperature 0     300     300     500     500     300
      Duration      100     200     100     200     100
   End

Note that there is always N-1 ``Duration`` values for N ``Temperature`` values.
The target temperature of the thermostat in this example will evolve as follows:

1. Increase linearly from 0 to 300 K over 100 steps.
2. Stay constant at 300 K for 200 steps.
3. Increase linearly from 300 to 500 K over 100 steps.
4. Stay constant at 500 K for 200 steps.
5. Decrease linearly from 500 to 300 K over 100 steps.
6. Stay constant at 300 K for the rest of the simulation.

.. index:: Trajectory sampling
.. _Trajectory_sampling:

Trajectory sampling and output
==============================

A basic principle of the numerical integration of motion in MD is that the
changes in the state of the system between successive time steps are small. This
means that storing the results of every step is not useful, because all the data
is strongly correlated. Instead, a snapshot of the system is taken every N steps,
where N is set low enough to still capture the fastest motion of interest but
high enough to avoid wasting space due to correlations. The resulting sequence
of snapshots is then commonly called the trajectory.

AMS writes the trajectory to the ``History`` and ``MDHistory`` sections of
``ams.rkf``, according to the settings in the ``Trajectory`` block. A snapshot
of the system and various MD variables is stored every ``SamplingFreq``
timesteps. By default, this frequency is also used to print basic thermodynamic
parameters of the simulation to the output and log file. Set ``PrintFreq``
to override this.

Frequently sampling a long trajectory can generate large volumes of data.
If the space usage becomes a concern, one can selectively disable storing
some parts of the trajectory to save space using the ``Write*`` keys. Note
however that this will make it impossible to use some analysis methods on the
resulting trajectory:

- ``WriteBonds`` is necessary for reaction network analysis (ChemTraYzer).
  Disabling ``WriteBonds`` also makes AMSmovie show only guessed bonds instead
  of those calculated by the engine.
- ``WriteMolecules`` is required by the Molecule Fractions panel in AMSmovie.
- ``WriteVelocities`` is required to calculate the velocity autocorrelation
  functions needed for diffusivity and IR spectra.

The trajectory itself contains only the data needed for subsequent analysis of
the dynamics of the system. However, much more data is usually generated on
every integration step. This includes, for example, the internal data used by an
engine when evaluating the energies and forces. This information is normally
discarded after each step, because it is often very large. However, a
``Checkpoint`` containing the complete internal state of the MD driver together
with a result file generated by the engine is stored every ``Frequency`` steps.
An interrupted simulation can then be restarted from this checkpoint using the
``Restart`` keyword. Additionally, the engine result files called
``MDStep*.rkf`` can also be used to extract various engine-specific details
about the system, such as the orbitals for QM engines.

.. index:: Molecular dynamics checkpoint
.. scmautodoc:: ams MolecularDynamics Trajectory Checkpoint CalcPressure Print
   :nosummary:
   :noref:
   :skipblockdescription:

.. _MDDeformation:
.. index:: Lattice deformations
.. index:: Volume regimes

Lattice deformations (volume regimes)
=====================================

The ``Deformation`` block can be used to gradually deform the periodic lattice of
the system during a MD simulation. This block can be repeated to define multiple
deformations, which will be applied on every MD step in the order in which they
are listed in the input.

.. seealso::

  :ref:`Example demonstrating various lattice deformations<example MD_Deformation>`

.. warning::

   While a ``Deformation`` and a ``Barostat`` can be used at the same time, remember
   to set the ``Scale`` parameter of the barostat so that no dimension is simultaneously
   being deformed and barostatted.

Each ``Deformation`` block will be active on MD steps between ``StartStep`` and ``StopStep``.

The time dependence of the lattice parameters is defined by the ``Type`` key:

Linear
   This deformation type adds the same constant amount to the selected lattice parameters
   on every simulation step. When used with ``TargetLattice``, ``LatticeVelocity``, or ``StrainRate``,
   the lattice matrix :math:`H` evolves as :math:`H(t) = H_0 + \Delta H \cdot t`,
   where :math:`H_0` is the lattice at ``StartStep``.

Exponential
   When used with ``StrainRate``, this type strains the lattice by the given strain matrix ``\epsilon``
   on every step, so that the lattice matrix :math:`H` evolves as :math:`H(t) = H_0 (1 + \epsilon)^t`.
   When used with ``LengthRate``, the length of each lattice vector evolves as
   :math:`l(t) = l_0 (1 + r)^t`.

Sine
   This is a periodic deformation going from the starting value of the selected lattice
   parameters to a set target, and then with the same amplitude to the opposite direction
   from the starting lattice.

Cosine
   This periodic deformation oscillates between the starting lattice and a defined target.

The period of the oscillation for the ``Sine`` and ``Cosine`` types must be set using
the ``Period`` key.

The extent of the deformation is defined by setting one of the six mutually exclusive input
keys. These belong to two groups, depending on whether they operate on the lattice matrix
as a whole, or just on the lengths of the individual lattice vectors:

TargetLattice, Velocity, and Rate
   These input keys expect a "lattice-like" matrix of numbers, consisting of up to three rows
   containing up to three values each. Each row contains the components of a single lattice vector
   and corresponds to a row of the :ref:`Lattice block <Lattice_vectors>`. For systems with 1D or
   2D periodicity the matrix may be padded to 3x3 with zeros.

TargetLength, LengthVelocity, and LengthRate
   These input keys expect a list of up to three values, defining the desired length of each lattice
   vector or the (absolute or relative) rate of its change.

.. scmautodoc:: ams MolecularDynamics Deformation
   :nosummary:
   :noref:
   :skipblockdescription:


Example: Transition from the initial lattice to a 10 Å cube over 1000 steps::

   MolecularDynamics
      Deformation
         StopStep 1000
         TargetLattice
            10.0  0.0  0.0
             0.0 10.0  0.0
             0.0  0.0 10.0
         End
      End
   End

Example: Oscillate the length of the *c* lattice vector between the initial value and 20 Å, leaving the *a* and *b* vectors unchanged::

   MolecularDynamics
      Deformation
         Type Cosine
         Period 100
         TargetLength 0 0 20
      End
   End

Example: Stretch the box in the "z" direction by a true exponential strain of 10 ppm per timestep while barostatting the remaining dimensions::

   MolecularDynamics
      Barostat Type=MTK Pressure=1e5 Tau=1000 Scale=XY
      Deformation
         Type Exponential
         StrainRate
             0.0  0.0  0.0
             0.0  0.0  0.0
             0.0  0.0 1e-5
         End
      End
   End

.. _MDAddMolecules:

.. index:: Molecule gun (molecular dynamics)
.. index:: Add molecules (molecular dynamics)

Molecule Gun: adding molecules during simulation
================================================

The molecule gun allows you to "shoot" (add with velocity) a molecule into the simulation box.

.. seealso::

   The `GUI tutorial <../../Tutorials/MolecularDynamicsAndMonteCarlo/MoleculeGun.html>`__ on the molecule gun.

Molecules can be continuously added to the simulation or only once. The initial position
can be pre-set or be random within the simulation box or a part thereof. It can be defined either in the
Cartesian or fractional coordinates. The initial velocity can be specified either directly (in Angstrom per femtosecond)
or as translational temperature or kinetic energy.
Possible applications of the molecule gun include e.g. the simulation of enforced collisions or deposition
processes on surfaces.

.. scmautodoc:: ams MolecularDynamics AddMolecules
   :nosummary:
   :noref:
   :skipblockdescription:


.. _MDRemoveMolecules:

.. index:: Remove molecules (molecular dynamics)

Removing molecules during simulation
====================================

Molecules :ref:`detected<BondOrders>` by the AMS driver can also be removed from
the system. This feature can, for example, be used to remove reaction products.

.. scmautodoc:: ams MolecularDynamics RemoveMolecules
   :nosummary:
   :noref:
   :skipblockdescription:

.. Warning::

   When there is a Molecules%AdsorptionSupportRegion defined, the molecule formulas depend on whether the molecule is adsorbed or not.


Accelerated dynamics
====================

.. _MDPLUMEDLibrary:

.. index:: PLUMED library

The PLUMED library support in AMS
---------------------------------

`PLUMED <http://www.plumed.org/>`__ is a plugin that works with various MD programs and is also available in AMS. It can be used for on-the-fly analysis of the dynamics, or to perform a wide variety of free energy methods. The interface with the plugin is really simple: you just need to specify the PLUMED input in the MolecularDynamics%Plumed%Input block and it will be passed to the library "as is". At each MD step, the current state of the system will be passed to the plugin to be updated according to the PLUMED input.

.. scmautodoc:: ams MolecularDynamics Plumed
   :nosummary:
   :noref:
   :skipblockdescription:


.. _CRESTmetadynamics:

.. index:: CREST metadynamics

Metadynamics for Conformer-Rotamer Ensemble Sampling (CREST-MTD)
----------------------------------------------------------------

This is a very specific implementation of metadynamics that is only meant for exploration of conformer space,
as used in the Conformer-Rotamer Ensemble Sampling (CREST) approach.
It is an RMSD-based metadynamics that places a new 1-dimensional Gaussian on the potential energy surface every ``NSteps`` steps.
The Gaussian is a function of the RMSD from the current geometry,
which will  always be zero at the moment of placement.
All Gaussians have the same maximum height (``Height``) and the same width (``Width``).
There is an upper limit of ``NGaussiansMax`` to the number of Gaussians present in the system,
and when this is exceeded the oldest Gaussian is removed.
By default the Gaussians are gradually introduced, using a scaling function that increases from 0 to 1
with the  simulation time. The keyword ``ScalingSlope`` in the inputblock ``GaussianScaling`` determines the
slope of the scaling function with respect to time. The default value of 0.03 :math:`steps^{-1}` yields a scaling factor of
nearly 1 after 100 steps.
The keyword ``ScaleGaussians`` in the inputblock ``GaussianScaling`` determines whether the Gaussians are scaled at all.

.. scmautodoc:: ams MolecularDynamics CRESTMTD
   :nosummary:
   :noref:
   :skipblockdescription:

By default the gradients of the Gaussians with respect to the atom coordinates are added to the state gradients,
but the value of the Gaussians is not added to the energy,
which is common in metadynamics.
For testing purposes it can be useful to add the Gaussian value to the energy, and this can be done with the
keyword ``AddEnergy``.
Irrespective of this choice, the energy value of the Gaussian at each geometry is printed in the ams.rkf file
in the section CrestMTDHistory.
It is also possible to use Gaussians from an earlier CREST-MTD simulation,
using the keyword ``RestartFile``.

.. _CVHD:

.. index:: CVHD

Collective Variable-driven HyperDynamics (CVHD)
-----------------------------------------------

The Collective Variable-driven HyperDynamics is a molecular dynamics acceleration method that allows observation of rare events by filling energy minima with a bias potential. In this sense it is similar to metadynamics. The difference of the hyperdynamics is that it ensures that the bias disappears in the transition state region. This difference allows hyperdynamics to calculate the rate of slow processes, for example the ignition phase of combustion.

.. seealso::

   The `GUI tutorial <../../Tutorials/MolecularDynamicsAndMonteCarlo/CVHD.html>`__ on CVHD.

The CVHD implementation in AMS follows the algorithm described in `K.M. Bal, E.C. Neyts, JCTC, 11 (2015) <https://doi.org/10.1021/acs.jctc.5b00597>`__

The StartStep, Frequency, StopStep, and WaitSteps keys define when and how often the bias potential is added, and when it is removed. The Bias block defines parameters of the bias potential peaks and the ColVarBB block describes parameters of the bond-breaking collective variable.

.. scmautodoc:: ams MolecularDynamics CVHD
   :nosummary:
   :noref:
   :skipblockdescription:

During a CVHD calculation, the following variables are saved to the MDHistory section of the RKF file, in addition to other MD properties:

* *BiasEnergy* - value the bias energy at the current MD step, in Hartree.
* *MaxBiasEnergy* - max BiasEnergy since the last sampling step.
* *BoostFactor* - the boost factor at the given MD step. The boost factor is calculated at each MD step as :math:`boost = e^{E_{bias}/kT}`, where T is the MD ensemble temperature.
* *MaxBoostFactor* - max BoostFactor value since the last sampling step.
* *HyperTime* - boosted MD time, in femtoseconds, which is a sum of the hyper-time steps calculated from the current boost factor and the MD time step as :math:`\Delta t_{boost} = boost * \Delta t`. In hyperdynamics, the hyper-time value is directly related to the rate of the process boosted by the corresponding collective variable.


Temperature Replica Exchange
----------------------------

Sampling of rare events can be accelerated using the Replica Exchange Molecular Dynamics (REMD) method, also known as Parallel Tempering.
This method runs multiple replicas (copies) of the simulated system in parallel, each in a different ensemble.
In the case of Temperature REMD, these ensembles are all NVT or NpT, each at a different temperature.
Periodically, Monte Carlo swaps are attempted between neighboring ensembles.
If the current configuration of replica A has a sufficient Boltzmann probability in the ensemble of replica B (and vice versa), the two configurations will be swapped.
This causes high-energy configuration to migrate into the high-temperature replicas while low-energy configurations eventually end up in the coldest ensemble.
This facilitates the crossing of energy barriers in the high-temperature ensembles while keeping the coldest replica at a given temperature of interest.
Because each replica always samples an unbiased ensemble, any property can be calculated using standard MD analysis methods without special preparation.

The method is controlled using the ReplicaExchange block:

.. scmautodoc:: ams MolecularDynamics ReplicaExchange
   :nosummary:
   :noref:
   :skipblockdescription:

The number of replicas set by ``nReplicas`` must never exceed the total number of processors used for the simulation.
If possible, the total number of processors should be an integer multiple of ``nReplicas`` to ensure good load balancing.

The temperature of the base (coldest) replica is determined by the ``Thermostat`` input block, just like in an ordinary MD simulation.
There are two ways to set the temperatures of the remaining replicas, either using ``Temperatures`` or ``TemperatureFactors``.
The latter is typically more convenient, as it makes it easy to set up the optimal geometric progression of temperatures.
In the simplest case, it is enough to supply just a single value in ``TemperatureFactors``, setting the common ratio of temperatures of any two adjacent replicas.

``SwapFrequency`` should be set as low as practical for maximum efficiency.
The value of this parameter isn't critical because it doesn't affect the validity of the results.
However, setting it too high will decrease overall acceleration by missing some opportunities to exchange.
Conversely, using a value that is too low will increase the communication overhead and lead to useless back-and-forth swaps between adjacent replicas.
Ideally, ``SwapFrequency`` should be comparable to the correlation time of the system to ensure that individual exchange attempts are uncorrelated.

The trajectory of each replica is written to a separate RKF file: *ams.rkf* for the base replica and *replicaX.rkf* for the other replicas.
One can easily switch between these files in the GUI using *File → Related Files*.
In addition to data present in any MD trajectory, these files also contain an extra section *ReplicaExchangeHistory* with the following data items written every ``SwapFrequency`` steps:

* *AvgSwapProbability* – Average swap acceptance for each pair of replicas, smoothed using an exponentially weighted moving average with a mixing factor equal to the inverse of ``EWMALength``.
* *{Min,Max,Mean,StdDev}PotentialEnergy* – Statistics of the potential energy for each ensemble over the last ``SwapFrequency`` steps.
* *SystemInEnsemble i* – Identifies the system (continuous trajectory) currently running in ensemble (replica) *i*.
* *EnsembleOfSystem i* – Inverse mapping of *SystemInEnsemble*, giving the current replica number in which the system number *i* runs.
* *TemperatureOfSystem i* – Equivalent to *EnsembleOfSystem* using temperatures instead of integer numbers to identify ensembles.

These data items can be plotted using the ``MD Replica Exchange`` menu in AMSmovie.
For example, plotting *TemperatureOfSystem* or *EnsembleOfSystem* is useful to visualize the migration of each system through the space of ensembles, where each curve represents one continuous trajectory.
Plotting potential energy statistics or average acceptances facilitates tuning the number of replicas and their temperatures to achieve efficient acceleration.
The replica exchange method can only work when the potential energy distributions of adjacent ensembles have a sufficient overlap.
This can be easily seen by comparing *MaxPotentialEnergy* of ensemble *i* with *MinPotentialEnergy* of ensemble *i+1*.
The optimal degree of overlap is such that leads to approximately 20 % of swap attempts getting accepted.
The acceptance of swaps can be monitored by plotting *AvgSwapProbability* and the corresponding ``TemperatureFactors`` can then be adjusted to keep it near the optimal value.


.. _MDBondBoost:
.. index:: Bond Boost method

Bond Boost Method
-----------------

The bond boost method implemented here is described in [#ref3]_. In this method, the distances between atoms that are relevant to the reaction of interest are calculated to determine the orientation of the reactant molecules. If a suitable initial configuration is recognized, an additional restraint energy (possibly consisting of more than one term) is added to the system that is intended to stretch or compress bonds at a pre-defined rate such that this additional energy can help achieve the energy to cross the reaction barrier. A single term of the restraint energy is depends on the restraints type and its parameters, see :ref:`restraint definitions <restraints_addon>` for details. If more than one suitable configuration is found then the one with the smallest sum of distances is used to create the restraints.


.. seealso::

   The `GUI tutorial <../../Tutorials/MolecularDynamicsAndMonteCarlo/PolymersBondBoost.html>`__ on the Bond Boost Method.


.. scmautodoc:: ams MolecularDynamics BondBoost
   :nosummary:
   :noref:
   :skipblockdescription:

For example::

   MolecularDynamics
      BondBoost
         NSteps 10000
         Chain
            AtomNames     N.1   C.t    O     H     @1
            MinDistances     3.0   1.2   1.5   0.8
            MaxDistances     3.8   3.0   2.5   1.5
         End
   #     Restraints         i  j   R_0    FC
         DistanceRestraint  1  2   1.5   0.05   Hyperbolic   0.7
         DistanceRestraint  2  3   3.5   0.03   Hyperbolic   0.5
         DistanceRestraint  3  4   1.0   0.03   Hyperbolic   0.5
      End
   End

The ``AtomNames``, ``MinDistances``, and ``MaxDistances`` keys constitute the atom chain definitions for the initial configuration. Thus, the example above defines a chain of atoms N.1-C.t-O-H-N.1 with R(N.1-C) in the (3.0,3.8) range, R(C.t-O) in the (1.2,3.0) range, etc.. In this example, the last atoms in the chain is required to be the same as the fist one, thus defining a ring. The specified restraints will push pairs of atoms C-N and O-H close together, which will hopefully let them form a bond, and pull atoms C.t and O away from each other, thus breaking the C-O bond. The restraint type is set to ``Hyperbolic`` to avoid very large forces that would otherwise result from a harmonic potential at a large deviation.

.. Note::

   When detecting coordinates, the program uses the full atom name and not just the element name. An atom name consists of the element name optionally followed by a period and a suffix, just like ``N.1`` and ``C.t`` in the example above. Using extended names for some atoms one may allow only a subset of bonds to be boosted.

.. _fbMC:
.. index:: Force bias Monte Carlo
.. index:: fbMC

Force bias Monte Carlo (fbMC)
-----------------------------

Configurational sampling and structural relaxation can be accelerated by the Force bias Monte Carlo method.
Unlike molecular dynamics, this approach does not use the equations of motion or atomic velocities.
Instead, all atoms are randomly displaced in each fbMC steps.
AMS uses an uniform-acceptance force bias Monte Carlo flavour of fbMC called tfMC, as published by Mees et al. [#ref4]_
Unlike other well-known Monte Carlo methods such as the Metropolis algorithm, fbMC does not generate completely random moves and then test whether these should be accepted or rejected.
Instead, the atomic displacements are generated so that atoms preferably move in the direction of the forces acting on them.
This special biasing enables fbMC to accept every move, sampling the correct canonical ensemble with high efficiency.

In AMS the fbMC method is implemented as an add-on to molecular dynamics, enabling mixed MC-MD simulations.
After every ``Frequency`` MD steps, the MD procedure is stopped and fbMC takes over, executing ``NSteps`` Monte Carlo steps.
Once the fbMC procedure completes, the MD simulation continues from the new geometry generated by fbMC while reusing atomic velocities from before the start of fbMC.

The fbMC module requires three main input settings.
Apart from the ``NSteps`` and ``Frequency`` defining the mix of molecular dynamics and Monte Carlo, ``Temperature`` needs to be set as desired to sample a particular canonical (NVT) ensemble.
Although the fbMC procedure always runs in constant temperature mode, the rest of the MD simulation can in principle use any ensemble (with or without a thermostat or barostat).

.. Note::

   To run a pure fbMC simulation with no molecular dynamics component, leave ``Frequency`` set to 1 (the default), set the MD ``TimeStep`` and ``InitialVelocities`` to zero, and do not use other MD features such as a thermostat or a barostat.

.. Note::

   AMS currently cannot write sampled geometries to the trajectory during the fbMC procedure. To see the evolution of the system during a long fbMC run, split it into multiple shorter fbMC passes to let the MD driver sample the current state between them. To do this, set the ``NSteps`` for fbMC to the desired trajectory sampling interval, keep ``Frequency`` set to 1 and set ``Trajectory SamplingFreq`` to 1.

The amount of acceleration provided by fbMC depends on the ``StepLength`` parameter, which defines the maximum displacement of the lightest atom in the system.
The default value of 0.1 Å is relatively conservative.
Increasing ``StepLength`` leads to faster evolution of the system, but setting it too high can lead to inaccurate sampling or cause crashes by generating geometries that are too distorted.

An estimate of the timescale associated with fbMC (tfMC) steps will be printed to the output.

.. scmautodoc:: ams MolecularDynamics fbMC
   :nosummary:
   :noref:
   :skipblockdescription:


.. index:: NEMD

Non-equilibrium MD (NEMD)
=========================

.. index:: Heat exchange (molecular dynamics)
.. index:: T-NEMD
.. index:: HEX method (NEMD)
.. index:: eHEX method (NEMD)

T-NEMD for thermoconductivity: heat exchange
--------------------------------------------

There are different methods to study thermal conductivity using non-equilibrium molecular dynamics (NEMD). A common feature of these methods is that they require the system to be divided into three or more zones, each with its own thermostat and other properties. One method maintains the temperature of the heat source and the heat sink zones at the given temperature using two different thermostats and measures the amount of heat transferred. These method does not require any special features besides a standard thermostat and a possibility to calculate the amount of heat accumulated by the thermostat per unit of time. The accumulated thermostat energies are available in the MDHistory section of ams.rkf file, in variables called 'XXXXstat#Energy', where XXXX is a 4-letter abbreviation of the thermo-/barostat ('BerT' for a Berendset thermostat, 'NHCT' for an NHC thermostat, 'NHTB' for an MTK barostat, etc.) and '#' is a 1-digit index of the thermo-/barostat.

In the other method, the heat flow is constant and the induced temperature gradient is measured. This method is implemented in AMS in three variants: a simple heat exchange, HEX [#ref1]_ and eHEX [#ref2]_. In the simple heat exchange method the atom velocities are scaled up (or down) by a factor corresponding to the amount of heat deposited to the heat source (or withdrawn from the heat sink) without paying attention to the conservation of the total momentum of the heat source (or sink). In the HEX method the velocities are scaled in such a way that the total momentum is conserved. This, however, introduces a small but measurable drift in the total energy. The eHEX algorithm improves upon the HEX by adding a third-order time-integration correction to remove the drift.

This method is controlled by the HeatExchange sub-block of the MolecularDynamics block:

.. scmautodoc:: ams MolecularDynamics HeatExchange
   :nosummary:
   :noref:
   :skipblockdescription:

One should be careful when choosing a value for the HeatingRate because a too large value may lead to pyrolysis of the heat source or to an abnormal termination when all the kinetic energy of the heat sink has been drained. The optimal value depends on the size of the system, its heat conductivity and the desired temperature gradient value. The thermal conductivity *k* can be calculated by dividing the heat flow rate *W* by the temperature gradient *grad(T)* and by the flow cross-section area *S*: :math:`k = W/(S \cdot grad(T))`. See the :ref:`trajectory sampling <Trajectory_sampling>` section above on how to obtain the temperature profile from which the *grad(T)* can be computed.


.. only:: html

  .. rubric:: References

.. [#ref1] T.\  Ikeshoji and B. Hafskjold, *Non-equilibrium molecular dynamics calculation of heat conduction in liquid and through liquid-gas interface* `Molecular Physics 81, 251-261 (1994) <https://doi.org/10.1080/00268979400100171>`__

.. [#ref2] P.\  Wirnsberger, D. Frenkel, and C. Dellago, *An enhanced version of the heat exchange algorithm with excellent energy conservation properties* `Journal of Chemical Physics 143, 124104 (2015) <http://dx.doi.org/10.1063/1.4931597>`__

.. [#ref3] A.\  Vashisth, C. Ashraf, W. Zhang, C.E. Bakis, and A.C.T. van Duin, *Accelerated ReaxFF simulations for describing the reactive cross-linking of polymers*, `J. Phys. Chem.  A, 122, 6633-6642 (2018) <https://doi.org/10.1021/acs.jpca.8b03826>`__

.. [#ref4] M.\ J. Mees, G. Pourtois, E. C. Neyts, B. J. Thijsse, and André Stesmans, *Uniform-acceptance force-bias Monte Carlo method with time scale to study solid-state diffusion*, `Phys. Rev. B 85, 134301 (2012) <https://doi.org/10.1103/PhysRevB.85.134301>`__
