.. _PESPointProperties:
.. index:: PES point properties

Gradients, Hessian, Stress tensor, Elasticity
#############################################

No matter what application the AMS driver is used for, in one way or another it
always explores the potential energy surface (PES) of the system. One can
furthermore ask AMS to calculate additional properties of the PES in the points
that are visited. These are mostly (but not exclusively) derivatives of the energy, e.g. we can ask
AMS to calculate the gradients or the Hessian in the visited points. In general
all these PES point properties are requested through the ``Properties`` block in
the AMS input:

.. scmautodoc:: ams Properties Gradients StressTensor Hessian SelectedRegionForHessian PESPointCharacter ElasticTensor
   :noref:
   :onlysummary:

This properties described on this page in the AMS manual are all related to derivatives of the energy.

Note that because these properties are tied to a particular point on the
potential energy surface, they are found on the :ref:`engine output
files<engine_output_files>`. Note also that the properties are not always
calculated in every PES point that the AMS driver visits during a calculation.
By default they are only calculated in *special* PES points, where the
definition of special depends on the :ref:`task<Tasks>` AMS is performing: For
a :ref:`geometry optimization<GeometryOptimization>` properties would for
example only be calculated at the final, converged geometry. This behavior can
often be modified by keywords special to the particular running task.


.. _NuclearGradients:
.. index:: Nuclear gradients
.. index:: Forces

Nuclear gradients
=================

The first derivative with respect to the nuclear coordinates can be requested as
follows:

.. scmautodoc:: ams Properties Gradients
   :noref:
   :skipblockdescription:

Note that these are gradients, not forces, the difference being the sign. The
gradients are printed in the output and written to the :ref:`engine result
file<engine_output_files>` belonging to the particular point on the PES in the
``AMSResults%Gradients`` variable as a :math:`3 \times n_\mathrm{atoms}` array
in atomic units (Hartree/Bohr).


.. _Hessian:
.. index:: Hessian

Hessian
=======

The calculation of the second derivative of the total energy with respect to the
nuclear coordinates is enabled by:

.. scmautodoc:: ams Properties Hessian SelectedRegionForHessian
   :noref:
   :skipblockdescription:

The Hessian is not printed to the text output, but is saved in the engine result
file as variable ``AMSResults%Hessian``. Note that this is just the plain
partial second derivatives (no mass-weighting) of the total energy. The
:math:`3 \times N_\mathrm{atoms}` columns/rows of the matrix are grouped by
atom: the first three rows/columns correspond to the first atom, etc..

Note that the AMS driver also supports the :ref:`Mobile Block Hessian<MBH>`
(MBH) method, which allows treating parts of the system as rigid blocks.

Often one is not interested in the Hessian matrix itself, but just in using it
for the calculation of IR frequencies or to characterize a PES point (as e.g. a
local minimum or a saddle point). For these application, see the following
pages in the manual:

* :ref:`IR frequencies<IRFrequencies>`
* :ref:`PES point character<PESPointCharacterization>`


.. index:: PES point characterization
.. _PESPointCharacterization:

PES point character
===================

A PES point can according to the slope and curvature of the PES at that point
be classified in the following categories:

* A local minimum on the PES with vanishing nuclear gradients and no negative
  frequencies.

* A transition state with vanishing nuclear gradients and exactly one negative
  frequency, i.e. a first order saddle point on the PES.

* A higher order saddle point, i.e. a stationary point on the PES with
  vanishing nuclear gradients but more than one imaginary frequency.

* A non-stationary point on the PES. Here the gradients are non-zero.

This classification can easily be done if both the gradients and the normal
modes have already been calculated. However, calculating the full Hessian needed
for the entire set of normal modes is very expensive and undesirable if one only
wants to know the character of a PES point. The AMS driver can quickly, and
without calculating the full Hessian, characterize a PES point into one of the
above categories. This can be used to confirm the success of e.g. a
:ref:`transition state search<TransitionStateSearch>` or :ref:`geometry
optimization<GeometryOptimization>`. A PES point can be characterized by
requesting ``PESPointCharacter`` as a property:

.. scmautodoc:: ams Properties PESPointCharacter
   :noref:
   :skipblockdescription:

This will calculate the few lowest normal modes using an iterative
diagonalization of the Hessian [#ref3]_ based on a Davidson algorithm
implemented in the PRIMME library [#ref4]_. The procedure has been optimized for
finding a small number of low-lying eigenvalues in as few matrix-vector
multiplications (and thus single point calculations) as possible. This is
facilitated by performing the iterative method using a pre-conditioning matrix
based on an approximation of the Hessian. The approximate Hessian is obtained
from the full Hessian at a lower level of theory. This calculation also provides
the initial guesses for the desired normal modes. What the lower level of
theory is depends on the main engine used in the calculation: DFTB with the
GFN1-xTB model is used as the lower level of theory for relatively slow
engines, e.g. DFT based engines. For semi-empirical engines like DFTB or MOPAC,
the lower level of theory is currently UFF. It is currently not possible to
change the engine used to obtain the preconditioning Hessian and the
approximate modes.

* Note that the iterative calculation of the normal modes is skipped when ...

  #. ... the nuclear gradients are so large that the PES point is considered
     non-stationary. The calculation of the modes is then just not necessary
     for classifying it.

  #. ... the full normal modes or Hessian have also been requested. The
     iterative calculation is then not necessary, as all modes are already
     known.

  #. ... the molecule is very small. (For small systems the iterative
     calculation of the few lowest normal modes is not faster than the full
     calculation of all modes, so all modes are calculated instead.)

* The classification as a stationary or non-stationary point uses the gradient
  convergence criterion from the geometry optimizer as the tolerance, see
  :ref:`geometry optimization<GeometryOptimization>`. This makes sure that the
  criterion for what is considered converged/stationary is always in sync
  between the optimizer and the PES point characterization.

* For periodic systems the PES point characterization does not take the lattice
  degrees of freedom into account. A PES point where the nuclear gradients are
  small enough would for example be classified as a stationary point, even if
  the system is under stress.

Details of the iterative procedure can be configured in the
``PESPointCharacter`` block:

.. scmautodoc:: ams PESPointCharacter

* Note that the residual tolerance that can be achieved is limited by the
  numerical differentiation that is performed. The default values should apply
  in most cases, but if convergence becomes a problem one may choose to
  increase the tolerance or to increase the step size (slightly). Note that the
  default residual tolerance is lower than for the other mode selective
  methods. This is because PRIMME uses a different convergence criteria than
  mode tracking/refinement. The higher value used as a default will therefore
  not result in decreased levels of accuracy. The method will bail if the
  number of iterations exceeds the number of normal modes as at this point
  still achieving convergence becomes unlikely, in part due to the next point.

* In order to avoid producing the known and irrelevant rigid modes, the method
  searches for normal modes orthogonal to six (or five) rigid modes.
  Imperfections due to the numerical differentiation may mean that the
  translational and rotational rigid modes are not exact eigenmodes of the
  Hessian that is constructed. As a result, some part of the lowest vibrational
  normal mode may lie in the span of the theoretical rigid modes and therefore
  be inaccessible to the Davidson method. This places a lower bound on the
  residual tolerance that can be achieved, which is directly related to the
  numerical differentiation accuracy. The take-away: do not set the tolerance
  too low, the default usually suffices.

* Behind the scenes, the method actually computes a few more modes than
  requested. In the case of multiplicities, eigenvalues may still converge out
  of order. These additional eigenvalues essentially guarantee that the obtained
  modes are indeed the lowest ones.

.. [#ref3] P\.  Deglmann and F. Furche, *Efficient characterization of stationary points on potential energy surfaces*, `J. Chem. Phys. 117, 9535 (2002) <https://doi.org/10.1063/1.1523393>`__

.. [#ref4] A\.  Stathopoulos and J. R. McCombs, *PRIMME: PReconditioned Iterative MultiMethod Eigensolver: Methods and software description*, `ACM Transactions on Mathematical Software, Vol. 37, No. 2, (2010), 21:1--21:30. <https://doi.org/10.1145/1731022.1731031>`__


Thermodynamics, gas phase Gibbs free energy
===========================================

At the end of a completed IR Frequencies (normal modes) calculation,
a survey is given of thermodynamic properties: entropy, internal energy, constant volume heat capacity, enthalpy and Gibbs free energy, see:

* :ref:`IR frequencies<IRFrequencies>`

  * :ref:`Thermodynamics<Thermodynamics>`
  * :ref:`Gibbs free energy change for a gas phase reaction<GasPhaseGibbsFree>`


.. _StressTensor:
.. index:: Stress tensor

Stress tensor
=============

For periodic systems (chains, slabs, bulk) one can also request the clamped-ion
stress tensor (note: the clamped-ion stress is only part of the *true* stress
tensor):

.. scmautodoc:: ams Properties StressTensor
   :noref:
   :skipblockdescription:

The clamped-ion stress tensor :math:`\sigma_\alpha` (Voigt notation) is
computed via numerical differentiation of the energy :math:`E` WRT a strain
deformations :math:`\epsilon_\alpha` keeping the atomic fractional coordinates
constant:

.. math::

   \sigma_\alpha= \frac{1}{V_0} \left. \frac{\partial E}{\partial \epsilon_\alpha} \right|_\text{constant atomic fractional coordinates}

where :math:`V_0` is the volume of the unit cell (for 2D periodic system
:math:`V_0` is the area of the unit cell, and for 1D periodic system
:math:`V_0` is the length of the unit cell).

The clamped-ion stress tensor (in Cartesian notation) is written to the engine
result file in ``AMSResults%StressTensor``.


.. index:: Elastic properties
.. index:: Elastic tensor
.. index:: Bulk modulus
.. index:: Young modulus
.. index:: Shear modulus
.. _ElasticTensor:

Elastic tensor
==============

The elastic tensor :math:`c_{\alpha, \beta}` (Voigt notation) is computed via second order numerical differentiation of the
energy :math:`E` WRT strain deformations :math:`\epsilon_\alpha` and :math:`\epsilon_\beta`:

.. math::

   c_{\alpha, \beta} = \frac{1}{V_0} \frac{\partial^2 E}{\partial \epsilon_\alpha \partial \epsilon_\beta}

where :math:`V_0` is the volume of the unit cell (for 2D periodic system :math:`V_0` is the area of the unit cell, and for 1D periodic system :math:`V_0` is the length of the unit cell).

For each strain deformation :math:`\epsilon_\alpha \epsilon_\beta`, the atomic positions will be optimized.
The elastic tensor can be computed for any periodicity, i.e. 1D, 2D and 3D.

.. seealso::

  :ref:`example ElasticTensor`

To compute the elastic tensor, request it in the ``Properties`` input block of
AMS:

.. scmautodoc:: ams Properties ElasticTensor
   :noref:
   :onlysummary:

.. note::

   The elastic tensor should be computed at the fully optimized geometry. One
   should therefore perform a geometry optimization of all degrees of freedom,
   **including the lattice vectors**. It is recommended to use a tight gradient
   convergence threshold for the geometry optimization (e.g. 1.0E-4). Note that
   all this can be done in one job by combining the :ref:`geometry optimization
   task<GeometryOptimization>` with the elastic tensor calculation.

The elastic tensor (in Voigt notation) is printed to the output file and stored
in the :ref:`engine result file<engine_output_files>` in the ``AMSResults``
section (for 3D system, the elastic tensor in Voigt notation is a 6x6 matrix;
for 2D systems is a 3x3 matrix; for 1D systems is just one number).

Options for the numerical differentiation procedure can be specified in the
``ElasticTensor`` input block:

.. scmautodoc:: ams ElasticTensor MaxGradientForGeoOpt StrainStepSize

:ref:`Pressure <pressure_addon>` or :ref:`non-isotropic external stress <external_stress_addon>` can be included in your simulation via the corresponding :ref:`engine addons <engineaddons>`.

The elastic tensor calculation supports AMS' :ref:`double parallelization <DriverLevelParallelism>`, which can perform the calculations for the individual displacements in parallel. This is configured automatically, but can be further tweaked using the keys in the ``NumericalDifferentiation%Parallel`` block:

.. scmautodoc:: ams ElasticTensor Parallel
   :noref:
   :skipblockdescription:


Numerical differentiation options
=================================

The following options apply whenever AMS computes gradients, Hessians or stress tensors via numerical differentiation.

.. scmautodoc:: ams NumericalDifferentiation NuclearStepSize StrainStepSize UseSymmetry

AMS may use symmetry (key ``NumericalDifferentiation%UseSymmetry``) in case of numerical differentiation calculations.
If symmetry is used only symmetry unique atoms are displaced.
Symmetry is only recognized if the starting geometry has symmetry.
Symmetry is only used for molecules if the molecule has a specific orientation in space, like that the z-axis is the main rotation axis.
If the GUI is used one can click the Symmetrize button (the star), such that the GUI will (try to) symmetrize and reorient the molecule.
There are some cases that even after such symmetrization, the orientation of the molecule is not what is needed for the symmetry to be used in case of numerical differentiation calculations. If that is the case or if key ``NumericalDifferentiation%UseSymmetry`` is set to 'False', then no symmetry will be used.

The numerical differentiation calculation supports AMS' :ref:`double parallelization <DriverLevelParallelism>`, which can perform the calculations for the individual displacements in parallel. This is configured automatically, but can be further tweaked using the keys in the ``NumericalDifferentiation%Parallel`` block:

.. scmautodoc:: ams NumericalDifferentiation Parallel
   :noref:
   :skipblockdescription:
