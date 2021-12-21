.. _engines:
.. index:: Engines

Engines
#######

The engines are the core of the Amsterdam Modeling Suite: While the AMS driver
steers the calculation over the potential energy surface in e.g. a
:ref:`geometry optimization<GeometryOptimization>` or :ref:`molecular
dynamics<MolecularDynamics>` calculation, the engines calculate energies and
gradients and in this way *define* the PES on which the driver works.

.. index:: Engine input

.. scmautodoc:: ams Engine

The engine used for an AMS calculation is selected and configured with the special
``Engine`` block in the AMS input:

.. code-block:: none

   Engine DFTB
      ... input for the DFTB engine ...
   EndEngine

Here the type of engine, e.g. ``DFTB`` as in the example above, is specified on
the line that opens the block. Note that the ``Engine`` block ends with
``EndEngine``, and is in this way different from all the other blocks in the AMS
input, which close just with ``End``. The content of the engine block is what we
call the "engine input". Generally the engine input consists of a series of
blocks and keywords, and looks just like the AMS driver input. However, many
engines have a lot of options and keywords, which are documented in a separate
engine manual. In other words: This AMS driver manual documents all the keywords
outside of the ``Engine`` block, while the individual engine manuals document
the contents of the engine block.


.. _available_engines:
.. index:: Available engines

Available engines
=================

The following engines are available in the |release| release of the Amsterdam
Modeling Suite:

.. index:: ADF
.. index:: BAND
.. index:: DFTB
.. index:: ReaxFF
.. index:: MLPotential
.. index:: UFF
.. index:: MOPAC

* `ADF <../ADF/index.html>`__
   A DFT engine particularly strong in understanding and predicting structure, reactivity, and spectra of molecules.

* `BAND <../BAND/index.html>`__
   An atomic-orbital based DFT engine aimed at periodic systems (crystals, slabs, chains) but supporting also molecular systems.

* `DFTB <../DFTB/index.html>`__
   An engine implementing Density Functional based Tight-Binding, a fast approximation to DFT.

* `ReaxFF <../ReaxFF/index.html>`__
   An engine for modeling chemical reactions with atomistic potentials based on the reactive force field approach.

* `MLPotential <../MLPotential/index.html>`__
   Machine learning potentials (machine learning force fields).

* `ForceField <../ForceField/index.html>`__
   An engine implementing classical non-reactive force fields such as UFF (a non-reactive force field covering the entire periodic table).

* `GFNFF <../GFNFF/index.html>`__
   The GFNFF force field

* `Hybrid <../Hybrid/index.html>`__
   Hybrid engine, for embedding and QM/MM calculations that combine multiple engines.

* `MOPAC <../MOPAC/index.html>`__
   An engine wrapping the MOPAC code, a general-purpose semiempirical molecular orbital package for the study of solid state and molecular structures and reactions.

* :ref:`External<ExternalEngines>`
   A flexible scripting interface that allows advanced users to use external modeling programs as engines in AMS.

* :ref:`LennardJones<LennardJones>`
   A simple toy engine implementing a Lennard-Jones potential.


Summary of engine capabilities
===============================

Some options/properties can only be computed in combination with some of the engines (i.e., not all engines support all features). These tables summarize the capabilities of the engines of the Amsterdam Modeling Suite:

.. csv-table:: Engine support for AMS driver options
   :header: "Feature", "ADF", "BAND", "DFTB", "ReaxFF", "MLPot.", "ForceField", "MOPAC", "GFNFF"

   All elements available                         ,✓,✓, ✓ [#dftb_all_el]_, , ,✓ [#ff_all_el]_,✓,✓
   :ref:`Non-periodic systems <SystemDefinition>` ,✓,✓,✓,✓,✓ [#mlpotential_periodicity]_,✓,✓,✓
   :ref:`1D periodic systems <SystemDefinition>`  , ,✓,✓,✓, ,✓,✓, 
   :ref:`2D periodic systems <SystemDefinition>`  , ,✓,✓,✓, ,✓,✓, 
   :ref:`3D periodic systems <SystemDefinition>`  , ,✓,✓,✓,✓ [#mlpotential_periodicity]_,✓,✓,✓
   Charged molecular systems                      ,✓,✓,✓,✓, ,✓,✓, 
   External electric field                        ,✓,✓,✓, , , ,✓, 
   External point charges                         ,✓,✓,✓, , , , , 

.. csv-table:: Engine support for AMS driver properties
   :header: "Feature", "ADF", "BAND", "DFTB", "ReaxFF", "MLPot.", "ForceField", "MOPAC", "GFNFF"

   :ref:`Atomic charges <Charges>`                       ,✓,✓,✓,✓, ,✓,✓,✔
   :ref:`Bond orders <BondOrders>`                       ,✓, ,✓,✓, ,✓,✓,✔
   :ref:`Dipole gradients <DipoleGradients>`             ,✓,✓,✓, , , ,✓,✔
   :ref:`Dipole moment <DipoleMoment>`                   ,✓,✓,✓, , , ,✓,✔
   :ref:`Elastic tensor <ElasticTensor>`                 , ,✓,✓,✓,✓,✓,✓,✔
   :ref:`Gradients / Forces <NuclearGradients>`          ,✓,✓,✓,✓,✓,✓,✓,✔
   :ref:`Hessian <Hessian>`                              ,✓,✓,✓,✓,✓,✓,✓,✔
   :ref:`Infrared spectra <IRFrequencies>`               ,✓,✓,✓, , , ,✓,✔
   Molecule detection                                    ,✓, ,✓,✓, ,✓,✓,✔
   :ref:`Normal modes     <IRFrequencies>`               ,✓,✓,✓,✓,✓,✓,✓,✔
   :ref:`PES point character <PESPointCharacterization>` ,✓,✓,✓,✓,✓,✓,✓,✔
   :ref:`Phonons <Phonons>`                              , ,✓,✓,✓,✓,✓,✓,✔
   :ref:`Polarizability <Polarizability>`                ,✓, , , , , , ,
   :ref:`Raman <raman>`                                  ,✓, , , , , , ,
   :ref:`Stress tensor <StressTensor>`                   , ,✓,✓,✓,✓,✓,✓,✔
   :ref:`Thermodynamic properties <Thermodynamics>`      ,✓,✓,✓,✓,✓,✓,✓,✔
   :ref:`VCD <VCD>`                                      ,✓,✓,✓, , , ,✓, 
   :ref:`VROA <VROA>`                                    ,✓, , , , , , ,


.. note::

   The features/options in the following tables are **engine-specific**, and are described in the corresponding engine's manual. The input for these options should be specified in the :ref:`Engine block <InputOutput>` section of the input file.

.. csv-table:: Engine-specific capabilities
   :header: "Feature", "ADF ", "BAND", "DFTB", "ReaxFF", "MLPot.", "ForceField", "MOPAC", "GFNFF"

   EFG, ✓ `(doc) <../ADF/Input/EFG.html>`__ , ✓ `(doc) <../BAND/Spectroscopy_and_Properties/EFG.html>`__
   Electronic transport, ✓ `(doc) <../ADF/Input/Transport.html>`__ , ✓ `(doc) <../BAND/Electronic_Transport/NEGF.html>`__ , ✓ `(doc) <../DFTB/NEGF.html>`__
   Energy decomposition analysis, ✓ `(doc) <../ADF/Input/Bond_energy_analysis.html>`__, ✓ `(doc) <../BAND/Analysis/Energy_Decomposition_Analysis.html>`__
   ESR/EPR, ✓ `(doc) <../ADF/Input/ESREPR.html>`__
   Hyperpolarizabilities, ✓ `(doc) <../ADF/Input/Polarizabilities.html>`__
   NMR, ✓ `(doc) <../ADF/Input/NMR.html>`__ ,
   Orbital energies, ✓, ✓, ✓, , , , ✓
   pKa, , , , , , , ✓ `(doc) <../MOPAC/Input.html#properties>`__
   Solvation models, ✓ `(doc) <../ADF/Input/Solvents_and_other_environments.html>`__ , ✓ `(doc) <../BAND/Model_Hamiltonians/Solvation.html>`__ , ✓ `(doc) <../DFTB/DFTB_Model_Hamiltonian.html#solvation-gbsa>`__ , , , , ✓ `(doc) <../MOPAC/Input.html#solvation>`__
   Spin-polarization, ✓ `(doc) <../ADF/Input/Electronic_Configuration.html>`__ , ✓ `(doc) <../BAND/Model_Hamiltonians/Relativistic_Effects_and_Spin.html>`__ ,  ✓ `(doc) <../DFTB/DFTB_Model_Hamiltonian.html#scc-details-and-spin-polarization>`__, , , , ✓ `(doc) <../MOPAC/Input.html#model-hamiltonian>`__
   UV-VIS optical spectra, ✓ `(doc) <../ADF/Input/Spectroscopic_properties.html>`__, , ✓ `(doc) <../DFTB/Spectroscopy_and_Properties.html#excited-states-with-time-dependent-dftb>`__


.. csv-table:: Engine-specific capabilities for periodic systems
   :header: "Feature", "ADF ", "BAND", "DFTB", "ReaxFF", "MLPot.", "ForceField", "MOPAC"

   Density of states (DOS), , ✓ `(doc) <../BAND/Analysis/DOS.html>`__ , ✓ `(doc) <../DFTB/Spectroscopy_and_Properties.html#electronic-structure-of-periodic-systems>`__, , , ,
   Dielectric function, , ✓ `(doc) <../BAND/Spectroscopy_and_Properties/Time_Dependent_Current_DFT.html>`__ , , , , ,
   Effective mass , , ✓ `(doc) <../BAND/Spectroscopy_and_Properties/Effective_Mass.html>`__ , ✓ `(doc) <../DFTB/Spectroscopy_and_Properties.html#electronic-structure-of-periodic-systems>`__, , , ,
   Electronic band structures , , ✓ `(doc) <../BAND/Analysis/Band_Structure.html>`__ , ✓ `(doc) <../DFTB/Spectroscopy_and_Properties.html#electronic-structure-of-periodic-systems>`__, , , ,
   k-space sampling, , ✓ `(doc) <../BAND/Accuracy_and_Efficiency/K-Space_Integration.html>`__ , ✓ `(doc) <../DFTB/DFTB_Model_Hamiltonian.html#k-space-integration>`__, , , ,
   X-ray form factors, , ✓ `(doc) <../BAND/Spectroscopy_and_Properties/X-Ray_Form_Factors.html>`__ , , , , ,

.. [#dftb_all_el] All elements are available for the GFN1-xTB model, but other DFTB parameter sets are not parametrized for all elements.

.. [#ff_all_el] All elements are available with UFF (universal force field), but other force fields are not parametrized for all elements.

.. [#mlpotential_periodicity] MLPotential backends may support non-periodic and/or 3D-periodic calculations.


.. _ExternalEngines:
.. index:: External engines
.. index:: Interface to external programs

External programs as engines
============================

The AMS driver allows running external programs as an engine. In this way users
can combine the functionality in the AMS driver (tasks and PES point properties)
with the energies and gradients of any molecular modeling program they have
access to.  For example, the graphical
user interface supports setting up `VASP as an external engine to the AMS driver <../GUI/VASP_via_AMS.html>`__.

In general, the interfacing between the AMS driver and the external program has to be done
by the user in form of a small script, which allows users to hook up any
external program without access to the source code of AMS.
The graphical user interface of the Amsterdam Modeling Suite
can then be used to analyze the results of these calculations.

An external engine is specified with ``Engine External``. The keyword
``Execute`` is used to specify the command that is run to execute the external program::

   Engine External
       Execute /path/to/my_interface_script.sh
   EndEngine

The command can in principle be anything, as it will just be executed as is by
the system shell. However, it should not use relative paths (e.g. to files in
the directory where the input file is). We recommend writing the interfacing
script in Python and using the Python interpreter that ships with AMS::

   Engine External
       Execute "$AMSBIN"/amspython /path/to/my_python_interface_script.py
   EndEngine

AMS then starts running and for every geometry prepares a folder in which the
external engine is supposed to run. This is the folder in which the interface
script specified with the ``Execute`` key is executed (so any relative paths
are relative to that folder). AMS puts two files into this folder::

   system.xyz
   request.json

The ``system.xyz`` just contains the geometry AMS wants the external engine to
calculate. It is an :ref:`extended format XYZ file<ExtendedXYZ>` with the
``VEC1``, ``VEC2``, ``VEC3`` extension at the end for periodic systems, e.g.
diamond would look like this::

   2

   C       -0.51292147    -0.51292147    -0.51292147
   C        0.51292147     0.51292147     0.51292147
   VEC1     0.00000000     2.05168587     2.05168587
   VEC2     2.05168587    -0.00000000     2.05168587
   VEC3     2.05168587     2.05168587     0.00000000

The ``request.json`` file is just a small JSON file that specifies what exactly
AMS wants the external engine to calculate::

   {
      "title": "GOStep28",
      "quiet": false,
      "gradients": true,
      "stressTensor": false,
      "hessian": true,
      "dipoleMoment": false,
      "properties": true,
      "prevResults": "GOStep27"
   }

The job of the interfacing script is now to read these files, run the external
program and convert its output into a format understood by AMS. Generally these
are simple text files with the name of the property and the extension ``.txt``.
The bare minimum the interfacing script needs to produce is the file
``energy.txt`` containing a single number, i.e. the total energy in atomic
units (Hartree). Other properties are optional, and it is easiest to go through
the ``request.json`` entries one by one to see what AMS might request and what
the interfacing script could produce in response.

``title``
   Just a title for this particular engine run. It can be passed on to the
   external program if desired, or can just be ignored.

``quiet``
   Whether AMS wants the external engine to write to standard output. This can
   be ignored in principle, but that might lead to really incomprehensible text
   output files of AMS if the external engine has to be called many times, e.g.
   for numerical derivatives.

``gradients``
   Whether or not to calculate nuclear gradients. The interface script should
   put the gradients in a file called ``gradients.txt`` with nAtoms lines of 3
   real numbers each, in atomic units, i.e. Hartree/Bohr. Note that AMS wants
   the gradients, not forces (beware the - sign!).

``stressTensor``
   Whether to calculate the stressTensor for periodic systems. Should be written
   to ``stresstensor.txt`` in atomic units.

``hessian``
   Whether to calculate the Hessian, that is just the second derivative of the
   energy with respect to the nuclear coordinates, *without* applying any mass
   weighing to it. If the Hessian has been calculated, it should be put in
   ``hessian.txt`` as a 3 nAtoms x 3 nAtoms matrix in atomic units.

``dipoleMoment``
   If true, calculate the dipole moment and put it in ``dipolemoment.txt`` in
   atomic units, in one line with three numbers.

``properties``
   This is set to true if AMS considers this "geometry" important and wants the
   engine to calculate further properties that the user might be interested in.
   In practice this is set to "true" for e.g.  the final converged step in a
   geometry optimization, so that the user can then let the engine calculate
   e.g. the band structure, which one would not want to do at all the steps
   *during* the optimization. AMS can't do anything with the properties that the
   engine might calculate, but the files will remain on disk for people to
   inspect them.

``prevResults``
   This is the title of a previous similar calculation that the engine has
   already performed. These results can be accessed in ``../$prevResults/``, so
   for the example above ``GOStep28`` can access the results from the previous
   step in the geometry optimization in ``../GOStep27/``. This is just the
   directory in which the interfacing script was run when the ``title`` field
   was set to ``GOStep27``, so files that were written back then are still
   accessible. They can in principle be used to restart for example the SCF of
   the engine from step to step. Of course all of that has to be done by the
   interfacing script. The AMS driver does not know anything about how to
   restart the external program and can only point the interfacing script to the
   right location.

That is really all there is to the external engine: AMS prepares a folder with
``system.xyz`` and ``request.json`` and runs the user's interfacing script in
there, which has to take care of preparing the input for the external engine,
running it, and putting the results in the text files that AMS expects, e.g.
``gradients.txt``.

Note for properties that are in one way or another derivatives of the energy, it
is generally ok if the external engine does not calculate what was requested by
the AMS driver in ``request.json``. If AMS requests, for example, the gradients
from the external engine, but then does not find the ``gradients.txt`` in the
directory after the interfacing script has run, it will just assume that the
engine was not capable of calculating the gradient analytically. AMS will then
just do the gradient numerically by rerunning the external engine for displaced
geometries, reading only the energy from ``energy.txt``. In this sense it is
only absolutely required for the external engine to produce the energy, the rest
can be done numerically by AMS if required. It is of course best to let the
engine do as much as possible, especially if it implements analytical
derivatives. Note that currently AMS can not calculate the Hessian numerically
for engines that do not provide gradients. This is just a technical limitation,
as it is of course possible to do a second derivative numerically, but it is
just not implemented in AMS yet. (And it would also be a very slow way to
calculate a Hessian.)

In addition to the ``Execute`` keyword that specifies the interfacing script,
it is also possible to use the ``ExecuteAtEnd`` keyword to specify another
command to be run at the end of the calculation, for example after the last
step of a geometry optimization or molecular dynamics simulation. This command
is run in the results directory.

Moreover, the ``Engine External`` block can also contain some information about the
capabilities of the external engines::

   Engine External
      Execute {...}
      ExecuteAtEnd {...}
      Supports
         DipoleMoment     {true|false}
         PeriodicityNone  {true|false}
         PeriodicityChain {true|false}
         PeriodicitySlab  {true|false}
         PeriodicityBulk  {true|false}
      End
   EndEngine

The normal engines that come with AMS (e.g. DFTB and BAND) produce the engine
output files with extension ``.rkf`` in the results directory, see
:ref:`here<engine_output_files>`. These files are also produced when an external
engine is used and the information on them (anything related to the shape of the
PES at that point, e.g. normal modes, phonons, ...) can be visualized normally
with the graphical interface. In addition to each engine output ``.rkf`` file,
external engines will also produce a correspondingly named folder per engine
file, which is just the working directory of the interfacing script for that
particular invocation of the external program. These folders just contain the
full output of the external program and anything that the interfacing script
might have produced. In this way users still have access to all results from the
external program, even if these results were not communicated back to the AMS
driver.

This last point is probably best illustrated with a simple example. Consider the
following job that uses an external engine to do a linear transit calculation of
ethane, going from the staggered to the eclipsed configuration, calculating
normal modes at all converged points along the path::

   AMS_JOBNAME=ethane_torsion $AMSBIN/ams << EOF

   Task PESScan

   System
      Atoms
         C       0.00000000       0.00000000       0.76576000
         C       0.00000000       0.00000000      -0.76576000
         H      -0.88668938       0.51193036       1.16677000
         H       0.88668938       0.51193036       1.16677000
         H       0.00000000      -1.02386071       1.16677000
         H       0.00000000       1.02386071      -1.16677000
         H      -0.88668938      -0.51193036      -1.16677000
         H       0.88668938      -0.51193036      -1.16677000
      End
   End

   PESScan
      CalcPropertiesAtPESPoints True
      ScanCoordinate
         nPoints 5
         Dihedral  3 1 2 6   60.0  0.0
      End
   End

   Properties
      NormalModes True
   End

   Engine External
      ...
   EndEngine

   EOF

If we run this job and look into the results folder, we will find the standard
``ams.log`` and ``ams.rkf`` as well as the usual engine result files
``PESPoint(1).rkf`` to ``PESPoint(5).rkf``. Just as if we had used one of the
native AMS engines, like DFTB. Each of these files can be opened in AMSspectra
to visualize the normal modes for this particular point. For an external engine
we additionally have one folder per engine file, so for this example we would
have ``PESPoint(1)/`` to ``PESPoint(5)/``. These are the folders in which the
interfacing script ran for these particular points, so they contain all the
native output files of the external program.


Toy engines
===========

.. _LennardJones:
.. index:: Lennard-Jones potential

The AMS driver comes with a simple built-in toy engine that implements a
Lennard-Jones potential. This can sometimes be useful for testing, as many
properties of the Lennard-Jones gas/liquid/solid can be calculated analytically
and compared to the results from AMS. Note that the potential is exactly the
same for all elements, i.e. the N-N bond has exactly the same strength as the
He-He bond.

The Lennard-Jones engine only has three keywords, which define the shape of the
potential:

::

   Engine LennardJones
      RMin   float
      Eps    float
      Cutoff float
   EndEngine

.. scmautodoclist:: lennardjones


.. _engineaddons:
.. index:: Engine add-ons
.. index:: Add-ons

Engine add-ons
==============

Engine add-ons can be used to augment the results returned from an engine.


Dispersion corrections
----------------------

For engines that do not natively support Grimme's D3 and D4 dispersion
corrections, the ``D3Dispersion`` and ``D4Dispersion`` engine add-ons can be
used to add such corrections.

.. _D4Dispersion:
.. index:: D3 dispersion add-on
.. index:: D4 dispersion add-on
.. index:: D5 dispersion add-on

.. scmautodoc:: ams EngineAddons D3Dispersion D4Dispersion
   :skipblockdescription:
   :noref:
   :collapselongchoicesinsummary:


.. index:: Pressure
.. _pressure_addon:

Pressure
--------

**Pressure** can be included using the following keyword (this can only be used for **3D periodic systems**):

.. scmautodoc:: ams EngineAddons Pressure
   :skipblockdescription:
   :noref:

The engine's energy will include the following extra term: :math:`P \cdot V`, where :math:`V` is the volume of the unit cell. The engine's stress tensor will include the following extra term: :math:`P \cdot \mathbb{1}`, where :math:`\mathbb{1}` is the identity matrix. This can only be used for 3D periodic boundary conditions (i.e. bulk).
The energy and stress tensor printed in output and written to the ``.rkf`` binary file will include these extra terms (i.e. the printed stress tensor is the sum of the internal stress and the external stress do to pressure).

When studying the effect that pressure has on the structure and properties of your system, one should generally start by :ref:`optimizing the structure <GeometryOptimization>` **including the lattice vectors** under pressure. Properties such as :ref:`phonons <Phonons>` or :ref:`elastic tensor <ElasticTensor>` can then be computed at the relaxed geometry.
If you are investigating phase transitions under pressure (or if you simply expect some symmetry breaking) you should disable symmetry and/or perturb the initial geometry of your system.

.. seealso::

   :ref:`example Diamond_under_pressure`

.. warning::

   If you want to include pressure in :ref:`molecular dynamics <MolecularDynamics>` calculations, you should not use this engine addon, but use the MD-specific pressure option.



.. index:: Non-isotropic stress
.. _external_stress_addon:

Non-isotropic external stress
-----------------------------

An **non-isotropic external stress tensor** can be included by using the following keywords:

.. scmautodoc:: ams EngineAddons ExternalStress
   :skipblockdescription:
   :noref:


The energy and stress tensor printed in output and written to the ``.rkf`` binary file already include the corresponding extra terms, i.e. the printed stress tensor is the sum of the internal stress and the input-specified external stress.

When studying the effect that an external stress has on the structure and properties of your system, one should generally start by :ref:`optimizing the structure <GeometryOptimization>` **including the lattice vectors** under the external stress (depending on the magnitute of the applied external stress, you might have to adjust the :ref:`stress energy per atom convergence threshold <GO_convergence>`). If your system is symmetric, you should **disable symmetry** when optimizing structures under external stress. Be aware that the geometry optimization might go completely astray (e.g. the material will break apart) if you apply a) too large shear stress or b) too large tension stress (too large negative stresses for the diagonal values).

Following this paper [#ref1]_ from Parrinello and Rahman, the extra energy term due to a non-isotropic external stress [#nonisotropic_energy]_ is defined with respect to a *reference unit cell*, which in our case is the unit cell at the beginning of the simulation.
If, during the simulation, large deformations of the unit cell occur, the above mentioned energy expression is only approximately consistent with the stress tensor. This affects the calculation differently depending on whether the stress tensor is computed by the engine or by AMS via numerical differentiation: a) If the stress tensor is computed directly by the engine, for large unit-cell deformations the energy might increase during the optimization; b) If the stress tensor is computed by AMS via numerical differentiation, the actual final value of the stress tensor might not match perfectly the external stress specified in the input (for large cell deformations, this error can be in the order of 10%).

After the optimization under external stress is converged, it is therefore good practice to validate the results. To do this, you should compute the :ref:`stress tensor <StressTensor>` at the optimized geometry by performing a :ref:`single point calculation <SinglePoint>`  **without** applying the external stress. The values in the computed stress tensor should have opposite sign compare to the external stress applied during the optimization.
If the values differ too much, then you can run a second geometry optimization under external stress starting from the optimized geometry.

.. seealso::

   :ref:`example ExternalStress_BN`

An alternative option is to set the key ``ExternalStress%UpdateReferenceCell`` to ``True``; this will update the reference unit cell at every optimization step, effectively changing the definition of the energy expression at every geometry optimization step. The energy might not consistently go down during the optimization, but the resulting internal stress will match much better the applied external stress. This option should only be used during geometry optimizations (i.e. it should not be used when computing properties such as the elastic tensor).

.. seealso::

   :ref:`example ExternalStress_graphene`


.. [#ref1] \M. Parrinello, and A. Rahman, *Polymorphic transitions in single crystals: A new molecular dynamics method*, `Journal of Applied Physics 52, 7182 (1981) <https://doi.org/10.1063/1.328693>`__


.. [#nonisotropic_energy] The energy term due to a non-isotropic external stress is:

   .. math::

      E_\text{stress} = p_h (V - V_0) + \frac{1}{2} V_0 Tr[(\sigma- p_h \mathbb{1}) (h_0^{T-1} h^T h h_0^{-1} - \mathbb{1})]

   where: :math:`\sigma` is the external stress tensor, :math:`p_h` is the hydrostatic pressure associated with :math:`\sigma` (i.e. the average of the diagonal elements of :math:`\sigma`), :math:`V` is the volume of the unit cell (for 2D periodic systems this is the area of the cell, and for 1D periodic systems is the length of the cell), :math:`V_0` is the volume of the *reference unit cell*, :math:`h` are the lattice vectors in matrix form, :math:`h_0` are the lattice vectors of the reference unit cell in matrix form and :math:`\mathbb{1}` is the identity matrix.



.. index:: Atom energies
.. _atom_energies_addon:

Atom energies
-------------

This add-on adds an element-dependent energy for each atom in a system,
effectively applying an energy shift. It does not affect any other property.

.. scmautodoc:: ams EngineAddons AtomEnergies

The below example will add -0.5 Hartree for every H atom and -5.0 Hartree for every C atom in the system to the total energy. The add-on will ignore any atoms of other elements::

   EngineAddons
      AtomEnergies
         H -0.5
         C -5.0
      End
   End

.. index:: Restraints
.. _restraints_addon:

Restraints
----------

A restraint is potential energy function (a spring) attached to a certain coordinate, for example, an interatomic distance, the minimum of the potential energy being at the specified optimal value. A restraint can have one or two parameters: a ForceConstant and, for some types, a F(Inf) value. The ForceConstant parameter corresponds to second derivative of the restraint potential energy :math:`\frac {d^{2}V(x)}{dx^2}` for any :math:`x` (harmonic restraints) or only at :math:`x = 0` (other restraints). Here, :math:`x` is a deviation from the restraint's optimal value.

Geometry restraints can be added using the following input block:

.. code-block:: none

   Restraints
      Profile [Harmonic | Hyperbolic | Erf]
      fInfinity float
      Distance atomIdx1 atomIdx2 OptValue {Profile} {fInfinity}
      Angle
      Dihedral
      SumDist
      DifDist
   End


The shape of the restraint potential function is defined by its profile type (``Harmonic``, ``Hyperbolic``, or ``Erf``) and the appropriate parameter(s). The ``Harmonic`` profile is most suitable for geometry optimizations but may result is very large forces that can be problematic in molecular dynamics. For MD simulations the ``Hyperbolic`` or ``Erf`` may be more suitable because the restraint force is bounded by a user-defined value. A ``Harmonic`` restraint is defined as :math:`V(x)=C \frac {x^2}{2}`. A ``Hyperbolic`` restraint is defined as :math:`V(x) = a (\sqrt{1+(b x)^2}-1)`. An ``Erf`` restraint is defined as :math:`V(x) = a (b x \cdot erf(b x) + \frac {e^{-(b x)^2}-1}{\sqrt{\pi}})`, which corresponds to an indefinite integral of the error function :math:`\frac {dV(x)}{dx} = a b \cdot erf(b x)`. The :math:`a` and :math:`b` parameters are calculated from the ``FInfinity`` and ForceConstant values. The ``Erf`` profile is very similar to ``Hyperbolic`` however its derivative converges to F(Inf) much faster.

The following keys define global parameters for all restraints.

.. scmautodoc:: ams Restraints Profile FInfinity
   :skipblockdescription:
   :noref:
   :nosummary:


The following keys define individual restraints. The force constant, profile type and the F(Inf) value can be set for each restraint individually.

.. scmautodoc:: ams Restraints Distance Angle Dihedral DifDist SumDist
   :skipblockdescription:
   :nosummary:

A default value for the force constant depends on the restraint type: 1.0 Hartree/Bohr for Distance, SumDist and DifDist, 0.3 Hartree/radian for Angle and 0.1 Hartree/radian for Dihedral.

Below is an example if the Restraints block.

::

   Restraints
      Profile Hyperbolic     # Change the default profile type
      fInfinity 10.0         # Change the asymptotic value for the restraint force away from optimum
   #  Type     Atoms    OptValue  FC   Profile  F(Inf)
      Distance 1 2        5.0     1.0  Erf      1.0
      Angle    1 2 3     90.0
      Dihedral 4 1 2 3  180.0     0.1
   #  The next two together are equivalent to imposing two distance restraints: R(23) to 0.85 Angstrom and R(14) to 0.65 Angstrom
      SumDist  1 4 2 3    1.5     # Keep R(14)+R(23) as close to 1.5 Angstrom as possible
      DifDist  1 4 2 3    0.2     # Keep R(14)-R(23) as close to 0.2 Angstrom as possible
   End


.. index:: Wall potential
.. _wall_potential_addon:

Wall potential
--------------

This add-on adds an inward repulsive potential around the origin of the form

.. math::

   E_\text{wall}(r) = k\log(1+\exp(-b(R-r)))

where the prefactor k, the radius R, and the gradient b are parameters, and r is the distance to the origin. The potential is time-independent and spherical. Inside the radius R, values for potential and forces are near zero. Outside of R, the potential exerts a nearly constant inward pointing force of :math:`k \cdot b` on each mass point [#ref_wall_potential]_.

.. scmautodoc:: ams EngineAddons WallPotential
   :noref:

.. [#ref_wall_potential] \S. Grimme, *Exploration of Chemical Compound, Conformer, and Reaction Space with Meta-Dynamics Simulations Based on Tight-Binding Quantum Chemical Calculations*, `Journal of Chemical Theory and Computation 15, 2847-2862 (2019) <https://doi.org/10.1021/acs.jctc.9b00143>`__

