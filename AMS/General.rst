General
#######


Overview
========

AMS is the new driver program introduced in the 2018 release of the Amsterdam
Modeling Suite. The job of AMS is to handle all changes in the simulated
system's geometry, e.g.  during a geometry optimization or molecular dynamics
calculation, using the so-called "engines" like ADF, BAND or DFTB for the
calculation of energies and forces. In summary, one might say that the AMS
driver steers the engines across the potential energy surface.

Prior to the 2018 release of the Amsterdam Modeling Suite, what we now call
engines used to be separate programs, each with their own input and output files
and formats. Starting with the 2018 release, the engines are only accessible
through the AMS driver program, that provides a unified interface to all of
them.


What's new in the AMS driver?
=============================

New in AMS2022.1
^^^^^^^^^^^^^^^^

- The MD driver now supports Rattle/Shake methods for :ref:`constrained molecular dynamics simulations <ConstrainedMD>`.
- The :ref:`PES scan <PESScan>` task now allows the :ref:`scanning of lattice degrees of freedom <LatticePESScan>`.
- The :ref:`molecule gun <MDAddMolecules>` now supports the generation of molecule mixtures through the ``MoleFrac`` keyword.
- The :ref:`Replay task<TrajectoryReplay>` for recomputing properties for trajectory frames with a different engine.
- A new option allows :ref:`Geometry optimizations<GeometryOptimization>` with :ref:`PES point characterization <PESPointCharacterization>` and no :ref:`symmetry<Symmetry>` to converge more reliably to minima instead of transition states or higher order saddle points: in case a geometry optimization converges to a TS, it can will now :ref:`automatically restart <GO_RestartFromTS>` after displacing all atoms along the imaginary mode.
- The calculation of Franck-Condon factors with the :ref:`FCF program<FCF>` has been improved regarding precision, speed, and memory requirements.

New in AMS2021.1
^^^^^^^^^^^^^^^^

- :ref:`PES exploration <EON>` tasks for the automated discovery of stationary points on the potential energy surface.

  #. :ref:`Process Search <ProcessSearch>`: a composite method for finding escape mechanisms from a state. This will find both local minima and their connecting saddle points.
  #. :ref:`Basin Hopping <BasinHopping>`: a Monte Carlo method for finding local minima.
  #. :ref:`Saddle Search <SaddleSearch>`: a single-ended method for finding nearby saddle points.

- :ref:`Force bias Monte Carlo <fbMC>` is now available in AMS, enabling pure MC or mixed MD/MC simulations with any engine.
- The :ref:`molecule gun <MDAddMolecules>` can now generate random shooting directions in a given cone.
- A new :ref:`wall potential <wall_potential_addon>` engine add-on can be used to simulate spherical nanoreactors.
- The :ref:`D4 dispersion add-on <D4Dispersion>` can now also be used for calculations on periodic systems.
- Graceful interactive termination of running jobs through the :ref:`interactive input file <interactive_input_file>`.
- :ref:`Geometry optimizations<GeometryOptimization>` write the optimized geometry to the results directory as an :ref:`extended XYZ file<ExtendedXYZ>`.

New in AMS2020.1
^^^^^^^^^^^^^^^^

- `ADF <../ADF/index.html>`__ has been fully integrated as an AMS engine.
- New engines: `MLPotential <../MLPotential/index.html>`__ implementing several different type of machine learning (ML) potentials. A `Hybrid engine <../Hybrid/index.html>`__ for combining other engines in QM/MM calculations. Enhanced `ForceField <../ForceField/index.html>`__ engine (formerly UFF).
- Improvements to the :ref:`Quasi-Newton geometry optimizer <QuasiNewton>`: Periodic systems can now be optimized in delocalized coordinates. Better performance for systems made up of disconnected fragments.
- Geometry optimization can now be performed with :ref:`frozen and equal strain constraints <LatticeConstraints>` for the lattice degrees of freedom. This option is currently only available with the :ref:`FIRE optimizer <FIRE>`.
- Support for :ref:`external electric fields <ExternalFields>`: Homogeneous as well as multipole charges.
- Enhanced support for :ref:`vibrational spectroscopy <PESVibrations>`: (resonance) Raman, (resonance) vibrational Raman optical activity, vibrational circular dichroism.
- The MD driver now supports time-dependent :ref:`lattice deformations <MDDeformation>` as well as a method for accelerating bonding reactions (:ref:`Bond Boost method <MDBondBoost>`).
- Reactive MD calculations with the AMS driver can now be analyzed with :ref:`ChemTraYzer <chemtrayzer>`.
- It is now possible to selectively disable writing some parts of a :ref:`MD trajectory <Trajectory_sampling>` to save space.
- More :ref:`trajectory analysis <trajectory_analysis>` options: :ref:`autocorrelation functions <AnalysisAutocorrelationFunction>` and :ref:`diffusion coefficient <AnalysisDiffusionCoefficient>`
- The :ref:`molecular composition analysis <MoleculeDetection>` can now be done with respect to an adsorption support region.
- The :ref:`transition state search <TransitionStateSearch>` task now allows the users to specify an approximate reaction coordinate (TSRC).
- For the calculation of normal modes, the :ref:`Mobile Block Hessian<MBH>` method now allows to treat parts of the system as rigid blocks.
- New coordinates for :ref:`constrained geometry optimizations <Constraints>` and :ref:`PES scans <PESScan>`: Sum of distances and difference of distances.
- Added the ability to include additional potential terms (i.e. springs) through the :ref:`Restraints engine add-on <restraints_addon>`.
- A running AMS driver process can be used from Python through the new `AMSWorker class <../plams/interfaces/amsworker.html>`__ in the `PLAMS <../plams/index.html>`__ library. The communication between PLAMS and the AMS driver happens via the new :ref:`AMSPipe` protocol.
- Introduced :ref:`Regions <Regions>` to simplify the input syntax for options that apply to a subset of atoms only.
- Symmetrization of systems from the input and the option to input a Z-matrix.
- Low frequencies contribution to :ref:`thermodynamics properties <Thermodynamics>` can be corrected using a free rotor interpolation method.

New in AMS2019.3
^^^^^^^^^^^^^^^^

- The :ref:`Nudged elastic band method (NEB)<NEB>` for finding minimum energy paths of transitions has been added.
- The new :ref:`PES point character property<PESPointCharacterization>` can be used to quickly calculate a few of the lowest vibrational modes of a system and to verify the success of a geometry optimization or transitions state search.
- :ref:`Driver level parallelism<DriverLevelParallelism>` is now enabled and managed automatically, improving the performance and scalability of many applications.
- A :ref:`Mode Scanning<ModeScanning>` calculation can now be :ref:`started automatically<AutomaticModeScanning>` for all modes within a specific frequency range.
- Methods for the quick calculation of the :ref:`vibrationally resolved electronic spectra<VibrationallyResolvedElectronicSpectra>`: :ref:`Vibronic-Structure Refinement<VibronicStructureRefinement>` and :ref:`Vibronic-Structure Tracking <VibronicStructureTracking>`.
- New geometry optimizer available: :ref:`Limited-memory BFGS <L-BFGS>`
- Input keywords that expect lists of numbers can now be specified as :ref:`ranges using a Python slice-like notation <ranges_in_input>`. Input keywords that expect a single real number now also accept fractions (of integers).
- New option to include a :ref:`non-isotropic external stress <external_stress_addon>` for 1D,2D and 3D periodic systems. This can be used to study structural deformation and mechanical properties of materials under non-isotropic stress.
- New :ref:`add-on system <engineaddons>` for manipulating and augmenting the results returned from the :ref:`engines <engines>`:

  #. Grimme's D4 and D3 dispersion corrections can be used with any engine through the :ref:`D4Dispersion and D3Dispersion add-ons <D4Dispersion>`.

New in AMS2019.1
^^^^^^^^^^^^^^^^
- :ref:`Intrinsic Reaction Coordinate (IRC) Scan <IRC>` in now available in the AMS driver for molecular and periodic systems.
- Support for the :ref:`Grand Canonical Monte Carlo (GCMC) <GCMC>` method has been added in the AMS driver.
- Molecular composition analysis for molecular dynamics simulations (see `tutorial <../Tutorials/MolecularDynamicsAndMonteCarlo/BurningIsooctane.html>`__)
- :ref:`Collective Variable-driven Hyperdynamics (CVHD) <CVHD>`
- :ref:`Molecule gun <MDAddMolecules>` and :ref:`molecule sink <MDRemoveMolecules>`  for molecular dynamics
- :ref:`PLUMED library support <MDPLUMEDLibrary>` for MD analysis and a wide variety of free energy methods
- The initial symmetry of a system is enforced during geometry optimizations with the Quasi-Newton optimizer.
- :ref:`Thermodynamic properties <Thermodynamics>` (assuming an ideal gas) are automatically computed after normal modes calculations.
- :ref:`Partial vibrational density of states (PVDOS) <PVDOS>` for normal modes.
- The system's symmetry is used to accelerate numerical nuclear derivatives and to provide symmetry labels for normal modes.
- The AMS driver starts up much faster, significantly speeding up scripting applications that launch AMS many times.
- New tools for mode selective vibrational analysis:

  #. :ref:`Mode Scanning<ModeScanning>` (aka ADF's ScanFreq)
  #. :ref:`Mode Refinement<ModeRefinement>` (aka "Frequency range selection")
  #. :ref:`Mode Tracking<ModeTracking>`

Motivation and progress
=======================

The Amsterdam Modeling Suite has grown substantially over the last decade, and
in the 2017 release included programs implementing methods all the way from
accurate density functional theory, through semi-empirical methods, to fast
reactive force fields. Many of these programs have originally been developed by
academic groups and are now maintained and expanded by SCM in collaboration with
the original authors.

This rapid growth of the Amsterdam Modeling Suite had, however, led to a certain
degree of unnecessary inhomogeneity within the suite: The input for the same
task, e.g. a geometry optimization, differed quite a lot between the different
programs in the suite. While this problem was mostly hidden for users of the
graphical interface, it constituted a barrier for users of the new scripting
frameworks such as PLAMS. Furthermore, the different programs produced rather
different output files for the same task, making the automated extraction of
results unnecessarily difficult. Finally, and most importantly, the rapid growth
of the AMS suite had also led to a certain level of feature fragmentation, where
some features were available in one program but not the other: ADF, for example,
was able to do a linear transit calculation, while BAND was not. Constrained
geometry optimization was supported in DFTB, but not in UFF. ReaxFF could be
used for Grand Canonical Monte Carlo simulations, but DFTB could not.

In order to overcome these issues and make the Amsterdam Modeling Suite more
powerful and user friendly, we introduced the AMS driver program with the 2018
release of the suite. The idea of this reorganization is to have only a single
program called the AMS driver that under the hood uses the so-called "engines"
like ADF, BAND and DFTB for the calculation of energies and gradients, where
the engines are technically no longer separate programs but just libraries used
by the AMS driver. In this way much of the input and output of AMS is the same,
no matter which particular engine is used for a calculation. It also avoids the
feature fragmentation, since any new feature in the AMS driver can immediately
be used with all engines in the suite. Furthermore, the AMS driver also allows
running :ref:`external programs as an engine<ExternalEngines>` providing
energies and gradients, allowing end-users to perform all calculations
supported by AMS with virtually any atomistic modeling program they have access
to and to visualize the results in the graphical user interface of the
Amsterdam Modeling Suite.

Converting all the programs of the Amsterdam Modeling Suite into engine
libraries that are used by the AMS driver was a big reorganization of the
entire suite, which was spread out over multiple releases between 2018 and 2020.
As of the AMS2020 release, ADF itself has been integrated into the AMS driver,
making the integration of all engines into the AMS driver finally complete.
(The only exception is QuantumEspresso, which is integrated into the GUI, but
has no connection to the AMS driver in the 2020 release.)

As with any large reorganization, it is unavoidable that some things change. For
GUI users this should not create any issues, but users familiar with the
existing command line and scripting interfaces will notice these changes and
their existing workflows might need to be adjusted to the new setup. We know
that these kind of changes can be disrupting for existing users, and where
possible we try to keep backwards compatibility with previous versions, but
unfortunately this is not always possible. However, overall AMS provides a much
more consistent and convenient interface to command line and scripting users,
and we believe that the new simplicity and expanded feature set of AMS make
transitioning to the new framework well worth the effort.


Input, execution and output
===========================

With the introduction of AMS in the 2018 release of the Amsterdam Modeling
Suite, there were some changes in the input and output files and formats used by
our software. Users of the graphical interface should not notice these changes,
but people using the software from the command line or through the scripting
frameworks need to be aware of them.

This section contains the main changes. For a more complete description see:

* The extended :ref:`Input, execution and output section<InputOutput>`.

Generally the input for AMS has the block and keyword structure that most
programs in the Amsterdam Modeling Suite have already been using. See the
:ref:`input_syntax` section for more details.  The only new construct in the
AMS input is a special ``Engine`` block, that selects which engine is used for
the simulation and also contains all the details of its configuration. This is
probably best illustrated by an example. Let us look at the following AMS
input, which optimizes the geometry of the methane molecule and calculates its
normal modes of vibration at the optimized geometry:

.. code-block:: shell

   $AMSBIN/ams << EOF
      Task GeometryOptimization

      GeometryOptimization
         Convergence
            Gradients 1.0e-4
         End
      End

      Properties
         NormalModes true
      End

      System
         Atoms
            C       0.00000000       0.00000000       0.00000000
            H       0.63294000      -0.63294000      -0.63294000
            H      -0.63294000       0.63294000      -0.63294000
            H       0.63294000       0.63294000       0.63294000
            H      -0.63294000      -0.63294000       0.63294000
         End
      End

      Engine DFTB
         Model DFTB3
         ResourcesDir DFTB.org/3ob-3-1
      EndEngine
   EOF

Note how DFTB is selected as the engine in the ``Engine DFTB`` line that opens
the ``Engine`` block. All DFTB specific configuration is contained within this
engine block, which is terminated by ``EndEngine``. The fact that we want to run
a geometry optimization with normal modes for methane and things like
convergence criteria for the optimization are of course completely independent
from which engine is actually used to perform this calculation. Therefore they
are all found *outside* of the ``Engine`` block. In this sense, the AMS input is
split up into the driver level input (everything outside of the engine block)
and the engine input, which is just a single ``Engine`` block. This separation
makes it easy to perform the same calculation at a different level of theory, by
simply switching out the ``Engine`` block in the input. We could, for example,
repeat the same calculation at the DFT-GGA level using the Band engine:

.. code-block:: none

   Engine BAND
       XC
          GGA PBE
       End
   EndEngine

Engines like ADF and BAND that have many options and can calculate many properties,
consequently also have a large number of possible keywords in their input. In
order to have a better structured documentation we have split off the description
of the engine inputs into separate :ref:`engine specific manuals<engines>`,
while this AMS manual only documents the driver level keywords outside of the
``Engine`` block. All the engine specific options are found in the respective
engine's manual, which documents the keywords in its ``Engine`` block. In
general all engines can be used with all tasks in AMS. There are only a few
rather obvious restrictions, for example that only engines which can handle
periodic systems can be used for the calculation of phonons.

The introduction of the ``Engine`` block is the only real change AMS brings to
the input side of things. On the output side there are a few more changes.

The first change to the output is that AMS does not put any of its output files
into the present working directory, as virtually all of the standalone programs
in the suite did. Instead AMS creates a ``*.results`` directory, which collects
all result file associated with a job. Here ``*`` is replaced by the jobname,
which is set with the ``AMS_JOBNAME`` environment variable:

.. code-block:: shell

    AMS_JOBNAME=methane $AMSBIN/ams << EOF

    ... see above ...

    EOF

This would put all results related to our geometry optimization of methane into
the newly created folder ``methane.results``. (The default name of the results
folder is ``ams.results`` if ``AMS_JOBNAME`` is not set, see the
:ref:`environment variables<EnvironmentVariables>` section of this manual for
documentation of all environment variables used by AMS.) In this way users can
easily run multiple jobs in the same directory without danger of clashing output
files, which was a common problem before the introduction of AMS. This new setup
is also more consistent with the graphical user interface, which already
collected all files associated with a specific job into a dedicated results
directory. Note that AMS will by default **not overwrite** results directories if a
job is rerun or another job is run with the same jobname.

Inside of the results directory users will always find the logfile ``ams.log``,
which is written during a running calculation and can be used to monitor its
progress. Furthermore the results directory contains binary result files in the
KF format, which can be opened and inspected with the KFBrowser GUI component.

* The main ``ams.rkf`` written by the AMS driver. It contains high level
  information about the trajectory that the AMS driver took over the potential
  energy surface. For example, for a molecular dynamics simulation it would
  contain the full trajectory. The format in which this information is written
  is independent from which engine was used for a calculation.

* The engine specific main binary output file written by the engine (and partly by the AMS driver).
  This file is kept for only one special point, e.g. the final geometry in a geometry optimization.
  For example, for ADF this engine file is called ``adf.rkf`` (instead of ``TAPE21`` in ADF<=2019),
  for BAND ``band.rkf``, for DFTB ``dftb.rkf``.
  If a property, like vibrational modes, is tied to the special point on the potential energy surface,
  it is stored in this file.  Also all engine specific properties are written to this file, like orbitals
  in case of a quantum mechanical engine.

* Additionally there might be a binary output file for every point on the
  potential energy surface that was visited during the calculation.

* Other engine specific binary (and ASCII) output files written by the engine.

Having multiple different binary output files could be confusing for people that
are used to the single result file that was written by the standalone programs
in ADF<=2017. After all, it brings up the question in which file the desired
property is stored. The general rule is: if the property is tied to a particular
point on the potential energy surface, it is stored in the engine output file
belonging to that particular point.
If the information depends on the entire trajectory over the PES, it is found in
the main ``ams.rkf`` written by the AMS driver.
