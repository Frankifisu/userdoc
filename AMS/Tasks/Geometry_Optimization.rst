.. index:: Geometry optimization
.. index:: Structure relaxation
.. index:: Geometry relaxation

.. _GeometryOptimization:

Geometry optimization
=====================

A geometry optimization is the process of changing the system's geometry (the
nuclear coordinates and potentially the lattice vectors) to minimize the total
energy of the systems. This is typically a local optimization, i.e. the
optimization converges to the next local minimum on the potential energy surface
(PES), given the initial system geometry specified in the ``System`` block. In
other words: The geometry optimizer moves "downhill" on the PES into the local
minimum.

.. seealso::

  :ref:`Examples` and `diamond lattice optimization and phonons tutorial <../../Tutorials/StructureAndReactivity/DiamondOptimizationAndPhonons.html>`__

Geometry optimizations are performed by selecting them as the ``Task``. The
details of the optimization can be configured in the corresponding block::

   Task GeometryOptimization

.. scmautodoc:: ams GeometryOptimization Convergence MaxIterations CalcPropertiesOnlyIfConverged OptimizeLattice KeepIntermediateResults PretendConverged MaxRestarts RestartDisplacement
   :onlysummary:

.. _GO_convergence:

.. scmautodoc:: ams GeometryOptimization Convergence
   :noref:
   :nosummary:

.. index:: Geometry convergence

A geometry optimization is considered converged when all the following criteria
are met:

1. The difference between the bond energy at the current geometry and at the
   previous geometry step is smaller than ``Convergence%Energy`` times the
   number of atoms in the system.

2. The maximum Cartesian nuclear gradient is smaller than
   ``Convergence%Gradient``.

3. The root mean square (RMS) of the Cartesian nuclear gradients is smaller than
   2/3 ``Convergence%Gradient``.

4. The maximum Cartesian step is smaller than ``Convergence%Step``.

5. The root mean square (RMS) of the Cartesian steps is smaller than 2/3
   ``Convergence%Step``.

**Note**: If the maximum and RMS gradients are 10 times smaller than the
convergence criterion, then criteria 4 and 5 are ignored.

Some remarks on the choice of the convergence thresholds:

* Molecules may differ very much in the stiffness around the energy minimum.
  Using the standard convergence thresholds without second thought is therefore
  not recommended. Strict criteria may require a large number of steps, while a
  loose threshold may yield geometries that are far from the minimum (with
  respect to atom-atom distances, bond-angles etc...) even when the total
  energy of the molecule might be very close to the value at the minimum. It is
  good practice to consider first what the objectives of the calculation are.
  The default settings in AMS are intended to be reasonable for most
  applications, but inevitably situations may arise where they are inadequate.

* The convergence threshold for the coordinates (``Convergence%Step``) is not a
  reliable measure for the precision of the final coordinates. Usually it yields
  a reasonable estimate (order of magnitude), but to get accurate results one
  should tighten the criterion on the gradients, rather than on the steps
  (coordinates). (The reason for this is that with the Quasi-Newton based
  optimizers the estimated uncertainty in the coordinates is related to the used
  Hessian, which is updated during the optimization. Quite often it stays rather
  far from an accurate representation of the true Hessian. This does usually
  not prevent the program from converging nicely, but it does imply a possibly
  incorrect calculation of the uncertainty in the coordinates.)

* Note that tight convergence criteria for the geometry optimization require
  accurate and noise-free gradients from the engine. For some engines this might
  mean that their numerical accuracy has to be increased for geometry
  optimization with tight convergence criteria, see e.g. the
  ``NumericalQuality`` keyword in the BAND manual.

The maximum number of geometry iterations allowed to locate the desired
structure is specified with the ``MaxIterations`` keyword:

.. scmautodoc:: ams GeometryOptimization MaxIterations CalcPropertiesOnlyIfConverged PretendConverged
   :noref:
   :skipblockdescription:
   :nosummary:

If the geometry optimization does not converge within this many steps it is
considered failed and the iteration aborted, i.e. :ref:`PES point
properties<PESPointProperties>` block will not be calculated at the last
geometry. The default maximum number of steps is chosen automatically based on
the used optimizer and the number of degrees of freedom to be optimized. The
default is a fairly large number already, so if the geometry has not converged
(at least to a reasonable extent) within that many iterations you should step
back and consider the underlying cause rather than simply increase the allowed
number of iterations and try again.

.. index:: Lattice optimization
.. index:: Cell optimization

.. _GO_RestartFromTS:

While a geometry optimization aims to find a (local) PES minimum, it may occur
that it ends up finding a saddle point instead. The ``PESPointCharacter``
property keyword can be used to quickly calculate the lowest few Hessian
eigenvalues to determine what kind of stationary PES point the optimization
found. More information on this feature can be found on its :ref:`Documentation
Page<PESPointCharacterization>`. Since AMS2022.1, geometry optimizations with
enabled PES point characterization can automatically restart when a transition
state (or higher order saddle point) is found: the geometry is distorted along
the lowest frequency mode and the optimizer run again. The applied distortion
is often symmetry breaking in this case, so this automatic restarting is only
enabled if the system does not have any symmetry operators or the use of
symmetry is explicitly disabled using the ``UseSymmetry`` keyword. Furthermore
the automatic restarting must be explicitly enabled by setting the
``MaxRestarts`` option to a value >0. Of course the PES point characterization
needs to be enabled too::

   GeometryOptimization
      MaxRestarts 5
   End

   UseSymmetry False

   Properties
      PESPointCharacter True
   End

Details of the automatic restarting can configured with the following keywords:

.. scmautodoc:: ams GeometryOptimization MaxRestarts RestartDisplacement
   :noref:
   :skipblockdescription:
   :nosummary:

For periodic systems the lattice degrees of freedom can be optimized in addition
to the nuclear positions.

.. scmautodoc:: ams GeometryOptimization OptimizeLattice
   :noref:
   :skipblockdescription:
   :nosummary:

Finally the ``GeometryOptimization`` block also contains some technical options:

.. scmautodoc:: ams GeometryOptimization KeepIntermediateResults
   :noref:
   :skipblockdescription:
   :nosummary:


.. _Constraints:
.. index:: Constraints
.. index:: Constrained optimization
.. index:: Geometry constraints

Constrained optimization
------------------------

The AMS driver also allows to perform constrained optimizations, where a number
of specified degrees of freedom are fixed to particular values.

.. seealso::

  :ref:`Example demonstrating all supported constraints<example constraints>`

The desired constraints are specified in the ``Constraints`` block at the root
level of the AMS input file::

   Constraints
      Atom integer
      AtomList integer_list
      FixedRegion string
      Coordinate integer [x|y|z] float?
      Distance (integer){2} float
      Angle (integer){3} float
      Dihedral (integer){4} float
      SumDist (integer){4} float
      DifDist (integer){4} float
      BlockAtoms integer_list
      Block string
      FreezeStrain [xx] [xy] [xz] [yy] [yz] [zz]
      EqualStrain  [xx] [xy] [xz] [yy] [yz] [zz]
   End

.. scmautodoc:: ams Constraints
   :nosummary:
   :notrecursive:

.. _FixedAtomConstraint:
.. index:: Fixed atoms

``Atom atomIdx``
   Fix the atom with index ``atomIdx`` at the initial position, as given in the
   ``System%Atoms`` block.

``AtomList [atomIdx1 .. atomIdxN]``
   Fix all atoms in the list at the initial position, as given in the
   ``System%Atoms`` block.

``FixedRegion regionName``
   Fix all atoms in a :ref:`region <Regions>` to their initial positions.

.. _CoordinateConstraint:

``Coordinate atomIdx [x|y|z] coordValue?``
   Constrain the atom with index ``atomIdx`` (following the order in the
   ``System%Atoms`` block) to have a cartesian coordinate (``x``, ``y`` or
   ``z``) of ``coordValue`` (given in Angstrom). If the ``coordValue`` is
   missing, the coordinate will be fixed to its initial value.

``Distance atomIdx1 atomIdx2 distValue``
   Constrain the distance between the atoms with index ``atomIdx1`` and
   ``atomIdx2`` (following the order in the ``System%Atoms`` block) to
   ``distValue``, given in Angstrom.

``Angle atomIdx1 atomIdx2 atomIdx3 angleValue``
   Constrain the angle (1)--(2)--(3) between the atoms with indices
   ``atomIdx1-3`` (as given by their order in the ``System%Atoms`` block) to
   ``angleValue``, given in degrees.

``Dihedral atomIdx1 atomIdx2 atomIdx3 atomIdx4 dihedValue``
   Constrain the dihedral angle (1)--(2)--(3)--(4) between the atoms with
   indices ``atomIdx1-4`` (as given by their order in the ``System%Atoms``
   block) to ``dihedValue``, given in degrees.

``SumDist atomIdx1 atomIdx2 atomIdx3 atomIdx4 sumDistValue``
   Constrain the sum of the distances R(1,2)+R(3,4) between the atoms with
   indices ``atomIdx1-4`` (as given by their order in the ``System%Atoms``
   block) to ``sumDistValue``, given in Angstrom.

``DifDist atomIdx1 atomIdx2 atomIdx3 atomIdx4 difDistValue``
   Constrain the difference between the distances R(1,2)-R(3,4) of the atoms
   with indices ``atomIdx1-4`` (as given by their order in the ``System%Atoms``
   block) to ``difDistValue``, given in Angstrom.

Note that the above constraints do **not** need to be satisfied at the
beginning of the optimization.

.. index:: Block constraints

``BlockAtoms [atomIdx1 ... atomIdxN]``
   Creates a block constraint (freezes all internal degrees of freedom) for a
   set of atoms identified by the list of integers ``[atomIdx1 ...  atomIdxN]``.
   These atom indices refer to the order of the atoms in the ``System%Atoms``
   block.

``Block regionName``
   Creates a block constraint (freezes all internal degrees of freedom) for a
   all atoms in a :ref:`region <Regions>` defined in the ``System%Atoms`` block.
   Example::

      System
         Atoms
            C  0.0  0.0  0.0    region=myblock
            C  0.0  0.0  1.0    region=myblock
            C  0.0  1.0  0.0
         End
      End
      Constraints
         Block myblock
      End

.. _LatticeConstraints:
.. index:: Lattice constraints
.. index:: Strain constraints

For lattice optimizations, the following constraints can be used on the lattice
degrees of freedom:

``FreezeStrain [xx] [xy] [xz] [yy] [yz] [zz]``
   Exclusively for lattice optimizations: Freezes any lattice deformation
   corresponding to a particular component of the strain tensor. Accepts a set
   of strain components [xx, xy, xz, yy, yz, zz] to be frozen.

``EqualStrain  [xx] [xy] [xz] [yy] [yz] [zz]``
   Exclusively for lattice optimizations: Accepts a set of strain components
   [xx, xy, xz, yy, yz, zz] which are to be kept equal. The applied strain will
   be determined by the average of the corresponding stress tensors
   components.

Note that in principle an arbitrary number of constraints can be specified and
thus combined. However, it is the user's responsibility to ensure that the
specified constraints are actually *compatible with each other*, meaning that it
is theoretically possible to satisfy all of them at the same time. The AMS
driver does **not** detect this kind of problems, but the optimization will
show very unexpected results. Furthermore, for calculations involving block
constraints the following restrictions apply:

+ There should be no other constrained coordinates used together with block
  constraints although this may work in many situation.

+ The user should absolutely avoid specifying other constraints that include
  atoms of a frozen block.


Restraints
**********
Not all optimizers support constraints. An alternative is to use so-called restraints. These are not exact constraints, but rather a number of springs that pull the system towards the preferred constraints, see :ref:`Restraints <restraints_addon>`.

Optimization under pressure / external stress
---------------------------------------------

:ref:`Pressure <pressure_addon>` or :ref:`non-isotropic external stress <external_stress_addon>` can be included in your simulation via the corresponding :ref:`engine addons <engineaddons>`.


.. _GeometryOptimizationMethods:
.. index:: Geometry optimization methods

Optimization methods
--------------------

The AMS driver implements a few different geometry optimization algorithms. It
also allows to choose the coordinate space in which the optimization is
performed:

.. scmautodoc:: ams GeometryOptimization Method CoordinateType
   :noref:
   :skipblockdescription:

We **strongly** advise leaving both the ``Method`` as well as the ``Coordinate``
type on the ``Auto`` setting. There are many restrictions as to which optimizer
and coordinate type can be used together with which kind of optimization. The
following (roughly) sketches the compatibility of the different optimizers and
options:

+---------------------+---------------------------------------+--------------+----------------------+
|     Optimizer       |              Constraints              | Lattice opt. |   Coordinate types   |
+=====================+=======================================+==============+======================+
|    Quasi-Newton     |    All, except strain constraints     |      Yes     |          All         |
+---------------------+---------------------------------------+--------------+----------------------+
|       FIRE          | Fixed coordinates, strain constraints |      Yes     |       Cartesian      |
+---------------------+---------------------------------------+--------------+----------------------+
|       SCMGO         |                   No                  |      Yes     |      Delocalized     |
+---------------------+---------------------------------------+--------------+----------------------+
|      L-BFGS         |                   No                  |      Yes     |       Cartesian      |
+---------------------+---------------------------------------+--------------+----------------------+
| Conjugate gradients |                   No                  |      No      |       Cartesian      |
+---------------------+---------------------------------------+--------------+----------------------+

Furthermore for optimal performance the optimizer should be chosen with the
speed of the engine: a faster engine in combination should use an optimizer with little
overhead (FIRE), while slower engines should use optimizers that strictly
minimize the number of steps (Quasi-Newton, SCMGO). This is all handled
automatically by default, and we recommend changing ``Method`` and
``Coordinate`` only in case there are problems with the automatic choice.

The following subsections list the strengths and weaknesses of the individual
optimizers in some more detail, motivating why which optimizer is chosen
automatically under which circumstances.

.. _QuasiNewton:
.. index:: Quasi-Newton (geometry optimizer)

Quasi-Newton
************

This optimizer implements a quasi Newton approach [#ref1]_ [#ref2]_ [#ref3]_,
using the Hessian for computing changes in the geometry so as to reach a local
minimum. The Hessian itself is typically :ref:`approximated<InitialHessian>` in
the beginning and updated in the process of optimization. It uses delocalized
coordinates by default both for molecules and periodic systems. The molecular
part is based mainly on the work by Marcel Swart [#ref4]_. Cartesian coordinates
are used in the presence of an external electric field and/or frozen atom constraints.

The Quasi-Newton (QN) optimizer supports all types of constraints and can be
used for both molecular and periodic systems, including lattice optimizations.
For cases where the optimization can be performed in delocalized coordinates,
the number of steps taken to reach the local minimum is usually smaller than
when optimizing in Cartesian ones.  For fast compute :ref:`engines<Engines>`,
the overhead of the QN optimizer can become a bottleneck of the calculation,
thus a more light-weight optimizer such as :ref:`FIRE` may give an better
overall performance. In principle, a QN optimization in delocalized coordinates
may run out of memory for a very large system (say over 1000 atoms) because of
the SVD step. However, since it is going to be used for a moderate-to-slow
engine we still recommend sticking to it for the benefit of fewer steps.
Because of these properties the QN optimizer is the default in AMS for all
kinds of optimizations with moderate and slow engines, such DFTB and ADF.  It
is also used as the optimizer back-end for the :ref:`PES scan task<PESScan>`,
the :ref:`transition state search<TransitionStateSearch>` as well as the
calculation of the :ref:`elastic tensor<ElasticTensor>`.

Details of the Quasi-Newton optimizer are configured in a dedicated block:

.. scmautodoc:: ams GeometryOptimization Quasi-Newton
   :noref:
   :skipblockdescription:

.. _InitialHessian:
.. index:: Initial Hessian

The Quasi-Newton optimizer uses the Hessian to compute the step of the
geometry optimization. The Hessian is typically approximated in the beginning
and then updated during the optimization. A very good initial Hessian can
therefore increase the performance of the optimizer and lead to faster and more
stable convergence. The choice of the initial Hessian can be configured in a
dedicated block:

.. scmautodoc:: ams GeometryOptimization InitialHessian
   :noref:
   :skipblockdescription:

While there are some options for the construction of approximate model
Hessians, the best initial Hessians are often those calculated explicitly at a
lower level of theory, e.g. the real DFTB Hessian can be used the initial
Hessian for an optimization with the more accurate BAND engine. Using the
``CalculateWithFasterEngine`` keyword can be used to automatically chose a fast
engine at a lower level of theory.  What the lower level of theory is depends
on the main engine used in the calculation: DFTB with the GFN1-xTB model is
used as the lower level of theory for relatively slow engines, e.g. DFT based
engines. For semi-empirical engines like DFTB or MOPAC, the lower level of
theory is currently UFF. If more control over the lower level engine is needed,
the initial Hessian can be calculated with a user defined engine and then
loaded from file, see :ref:`this example<example 2StepGO>`.

.. index:: FIRE (geometry optimizer)
.. _FIRE:

FIRE
****

The Fast Inertial Relaxation Engine [#ref5]_ based optimizer has
basically no overhead per step, so that the speed of the optimization purely
depends on the performance of the used compute :ref:`engine<Engines>`. As such
it is a good option for large systems or fast compute engines, where the
overhead of the Quasi-Newton optimizer would be significant. Note that is also
supports :ref:`fixed atom constraints<FixedAtomConstraint>` and :ref:`coordinate
constraints<CoordinateConstraint>` (as long as the value of the constrained
coordinate is already satisfied in the input geometry), as well as lattice
optimizations (with strain constraints).

FIRE is selected as the default optimizer for fast compute engines if it is
compatible with all other settings of the optimization (i.e. no unsupported
constraints or coordinate types).

.. Note::

   FIRE is a very robust optimizer. In case of convergence problems with the
   other methods, it is a good idea to see if the optimization converges with
   FIRE. If it does not, it is very likely that the problem is not the optimizer
   but the shape of the potential energy surface ...

The details of the FIRE optimizer are configured in a dedicated block. It is
quite easy to make the optimization numerically unstable when tweaking these
settings, so we strongly recommend leaving everything at the default values.

.. scmautodoc:: ams GeometryOptimization FIRE
   :noref:
   :skipblockdescription:

.. _SCMGO:
.. index:: SCMGO (geometry optimizer)

SCMGO
*****

The SCMGO optimizer is a new implementation of a Quasi-Newton style optimizer
working in delocalized coordinates. In the 2020 release of the Amsterdam
Modeling Suite it is still considered experimental and therefore never selected
automatically. However, for molecules and fully connected periodic systems it
already shows a quite good performance, and could be a reasonable alternative to
the classic :ref:`Quasi-Newton<QuasiNewton>` optimizer.

.. scmautodoc:: ams GeometryOptimization SCMGO
   :noref:
   :skipblockdescription:

Note that SCMGO also supports different initial Hessians, and uses the same
options for the initial Hessian as the Quasi-Newton optimizer, see
:ref:`above<InitialHessian>`.

.. index:: L-BFGS (geometry optimizer)

.. _L-BFGS:

Limited-memory BFGS
*******************

AMS also offers an L-BFGS based geometry optimizer. It usually converges faster
than :ref:`FIRE`, but does not support constrained optimizations.
For periodic systems it can be quite good for lattice optimizations.
The new implementation has not been thoroughly tested yet, therefore never
selected automatically. For large systems and fast engines you may want to disable symmetry:
simply the detection of (non-existing) symmetry may be a huge overhead.

.. scmautodoc:: ams GeometryOptimization HessianFree
   :noref:
   :skipblockdescription:

.. index:: Conjugate gradients (geometry optimizer)

Conjugate gradients
*******************

AMS also offers a conjugate gradients based geometry optimizer, as it was also
implemented in the pre-2018 releases of the DFTB program. However, it is
usually slightly slower than :ref:`FIRE`, and supports neither lattice nor
constrained optimizations. It is therefore never selected automatically, and we
do not recommend using it. Like L-BFGS, the conjugate gradients optimizer is
also configured in the ``HessianFree`` block, see L-BFGS section above for
details.


Troubleshooting
---------------

Failure to converge
*******************

First of all one should look how the energy changed during the latest ten or so
iterations. If the energy is decreasing more or less consistently, possibly
with occasional jumps, then there is probably nothing wrong with the
optimization. This behavior is typical in the cases when the starting geometry
was far away from the minimum and the optimization has a long way to go. Just
increase the allowed number of iterations, restart from the latest geometry and
see if the optimization converges.

If the energy oscillates around some value and the energy gradient hardly
changes then you may need to look at the calculation setup.

The success of geometry optimization depends on the accuracy of the calculated
forces. The default accuracy settings are sufficient in most cases. There are,
however, cases when one has to increase the accuracy in order to get geometry
optimization converged. First of all, this may be necessary if you tighten the
optimization convergence criteria. In some cases it may be necessary to increase
the accuracy also for the default criteria. Please refer to the :ref:`engine
manuals<Engines>` for instructions on how to increase the accuracy of an
engine's energies and gradients. Often this is done with the
``NumericalQuality`` keyword in the engine input.

A geometry optimization can also fail to converge because the underlying
potential energy surface is problematic, e.g. it might be discontinuous or not
have a minimum at which the gradients vanish. This often indicates real problems
in the calculation setup, e.g. an electronic structure that changes
fundamentally between subsequent steps in the optimization. In these cases it is
advisable to run a single point calculation at the problematic geometries and
carefully check if the results are physically actually sensible.

Finally it can also be a technical problem with the specific :ref:`optimization
method<GeometryOptimizationMethods>` used. In these cases switching to another
method could help with convergence problems. We recommend first trying the
:ref:`FIRE` optimizer, as it is internally relatively simple and stable.

Restarting a geometry optimization
**********************************

During a running optimization the system's geometry is written out to the AMS
driver's output file ``ams.rkf`` after every step (in the ``Molecule`` section).
This means that crashed or otherwise canceled geometry optimizations can be
restarted by simply loading the last frame from there using the ``LoadSystem``
keyword, see :ref:`its documentation<LoadSystem>` in the system definition
section of this manual::

   LoadSystem File=my_crashed_GO.results/ams.rkf

This can of course also be used to continue an optimization but e.g. with
tighter convergence criteria or a different optimizer, as it essentially starts
a new geometry optimization from the previous geometry, and does not propagate
any information internal to the optimizer (e.g.  the approximate Hessian for the
Quasi-Newton optimizer or the FIRE velocities) to the new job. As such it might
take a few more steps to convergence than if the original job had continued, but
allows for additional flexibility.

.. only:: html

  .. rubric:: References

.. [#ref1] L.\  Versluis and T. Ziegler, *The determination of Molecular Structure by Density Functional Theory*, `Journal of Chemical Physics 88, 322 (1988) <https://doi.org/10.1063/1.454603>`__

.. [#ref2] L.\  Versluis, The determination of molecular structures by the HFS method, PhD thesis, University of Calgary, 1989

.. [#ref3] L.\  Fan and T. Ziegler, *Optimization of molecular structures by self consistent and non-local density functional theory*, `Journal of Chemical Physics 95, 7401 (1991) <https://doi.org/10.1063/1.461366>`__

.. [#ref4] M.\  Swart and F.M. Bickelhaupt, *Optimization of strong and weak coordinates*, `International Journal of Quantum Chemistry 106, 2536 (2006) <https://doi.org/10.1002/qua.21049>`__

.. [#ref5] E.\  Bitzek, P.\  Koskinen, F.\  Gähler, M.\  Moseler and P.\  Gumbsch, *Structural Relaxation Made Simple*, `Physical Review Letters 97, 170201 (2006) <https://doi.org/10.1103/PhysRevLett.97.170201>`__
