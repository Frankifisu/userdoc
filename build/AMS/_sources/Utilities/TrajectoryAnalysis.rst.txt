.. index:: MD trajectory analysis 

.. _trajectory_analysis:

Trajectory Analysis
===================

``analysis`` is a standalone program that performs analysis of molecular dynamics trajectories created with AMS. It can produce histograms and radial distribution functions. It is also used under the hood in `AMSmovie <../../GUI/AMSmovie.html>`__ (**MD Properties** menu bar).

This is an example showing how to compute the oxygen-oxygen radial distribution function of a MD simulation using the analysis utility program:

.. code-block:: bash

   $AMSBIN/analysis <<eor

   Task RadialDistribution

   TrajectoryInfo
       Trajectory
           KFFilename ams.results/ams.rkf
           Range 1 1000 2
       End
   End

   RadialDistribution
       NBins 1000
       AtomsFrom
           Element O
       End
       AtomsTo
           Element O
       End
   End
   eor

The analysis program reads one or more trajectory files (filename.rkf) from an AMS molecular dynamics (MD) or a Grand Canonical Monte Carlo (GCMC) simulation.
The file information is supplied in the ``TrajectoryInfo`` input block. 
In this block, a separate ``Trajectory`` subblock needs to be supplied for each trajectory file.
The ``Trajectory`` subblock contains a mandatory keyword ``KFFilename``, and an optional keyword ``Range``.
The latter contains the initial frame to be read, the final frame to be read, and optionally the stepsize.
By default all frames on the trajectory file are read.

.. scmautodoc:: analysis TrajectoryInfo

All tools in the analysis program provide an option to obtain information on the equilibration of the simulation. 
If the optional keyword ``NBlocksToCompare`` in the ``TrajectoryInfo`` block
is set to a value :math:`N` higher than 1, the trajectory is divided into :math:`N` blocks, and the analysis results for each block are compared.
The variation in the analysis result is provided as a standard deviation.

.. index:: Radial distribution function
.. index:: RDF

Radial Distribution Function (RDF)
##################################

The Analysis tool computes radial distribution functions :math:`g(r)` if the ``Task`` keyword is set to RadialDistribution. 

.. scmautodoc:: analysis Task

Further details on the radial distribution functions are then set in the ``RadialDistribution`` block. 
If more than one ``RadialDistribution`` block is present in the input, more than one radial distribution function will be computed. 
The result is printed to output as text, as well as stored in a binary file (analysis.kf).

Description
***********

A radial distribution function :math:`g(r)`, or pair correlation function,
is a density of distances between particles,
relative to the average distance density.
The *x*-axis variable represents a distance :math:`r`, while the *y*-axis represents the relative density of that distance.
For a complete homogeneous system of particles the :math:`g(r)` values for 
the distances between all particles equals 1 everywhere.

Two sets of atoms :math:`\mathbb{S}_{\textrm{from}}` and :math:`\mathbb{S}_{\textrm{to}}`, of length :math:`n_{\textrm{from}}` and :math:`n_{\textrm{to}}` respectively,
are specified with the keywords ``AtomsFrom`` and ``AtomsTo`` in the ``RadialDistribution`` block.
As a result the program computes :math:`n_{\textrm{from}}*n_{\textrm{to}}` distances :math:`r_{ij}^s` between atom :math:`i`
in :math:`\mathbb{S}_{\textrm{from}}` and atom :math:`j` in :math:`\mathbb{S}_{\textrm{to}}` for each trajectory frame :math:`s` 
out of a total of :math:`n_{\textrm{frames}}` frames.

A normalized histogram is then computed from these distances, resulting in a function :math:`N(r)`.

:math:`N(r)=\frac{1}{n_{\textrm{frames}}} \sum_{s=1}^{n_{\textrm{frames}}} \sum_{i=1}^{n_{\textrm{from}}}\sum_{j=1}^{n_{\textrm{to}}} \delta(r_{ij}^s-r)`.

This histogram is converted to a density, by dividing all values :math:`N(r)` with the volume :math:`V(r)= 4 \pi r^2 dr` 
of a sphere-slice at radius :math:`r` with thickness :math:`dr`.

The density is further converted to a relative density by dividing with the total density of the system 
:math:`\rho_{\textrm{tot}} = \frac{n_{\textrm{from}}*n_{\textrm{to}}}{V_{\textrm{tot}}}`, yielding the final radial distribution function :math:`g(r)`.

:math:`g(r) = \frac{N(r)}{V(r)*\rho_{\textrm{tot}}}`

Options
*******

**Non-periodic systems**
The above equation assumes that the volume :math:`V_{\textrm{tot}}` of the system is a well-defined quantity.
This assumption is correct for systems with 3D periodicity, where the :math:`V_{\textrm{tot}}` is defined as the volume
of the periodic cell. 
In such a system the value of :math:`r` can be no larger than :math:`r_{\textrm{max}}`, the radius of the largest sphere that
can be placed inside the periodic cell.

If a system is non-periodic in one or more direction, then the program still computes a :math:`g(r)`, only if
the radius :math:`r_{max}` is supplied by the user with the ``Range`` keyword in the ``RadialDistribution`` block.
The radius is the second value supplied.

.. scmautodoc:: analysis RadialDistribution Range

In this case the volume :math:`V_{\textrm{tot}}` is assumed to be the volume of a sphere with radius :math:`r_{\textrm{max}}`.

**NPT simulations**
The above equation further assumes that the volume :math:`V_{\textrm{tot}}` is constant throughout the simulation.
The :math:`g(r)` of the trajectory from an NPT simulation can still be computed, and in this case :math:`V_{\textrm{tot}}`
is the average value of the volume of the periodic cell.

**Simulations with varying numbers of atoms**
The above equation also assumes that :math:`n_{\textrm{from}}` and :math:`n_{\textrm{to}}` remain constant throughout the simulation.
However, in a Molecular Gun simulation particles can be added to the system, and in a GCMC simulation particles can be
both added and removed from the system.
Nonetheless, the program still computes a :math:`g(r)` in these situations.

If the ``AtomsFrom`` and ``AtomsTo`` blocks contain element names (supplied with the recurring ``Element`` keyword),
then every time atoms are added to or removed from the system, the sets of atoms 
:math:`\mathbb{S}_{\textrm{from}}` and :math:`\mathbb{S}_{\textrm{to}}`
are re-evaluated. 

If the ``AtomsFrom`` and ``AtomsTo`` blocks contain atom numbers (supplied with the recurring ``Atom`` keyword),
these numbers are updated in the sets :math:`\mathbb{S}_{from}` and :math:`\mathbb{S}_{to}`
every time atoms are added to or removed from the system.
If one of the atoms from the set disappears, the number of distances contributing to the :math:`g(r)` decreases.

*Note:* 
Currently, the values of :math:`n_{from}` and :math:`n_{to}` in the normalization factor are taken from the last frame of the simulation.

*Warning:* 
If multiple trajectories are supplied, and the number of atoms changes between the end of one trajectory
and the beginning of another, this may result in an error in the atom numbers used by the program internally.

.. index:: Histogram (molecular dynamics)

Histogram
#########

The Analysis program computes histograms if the ``Task`` keyword is set to Histogram. 

.. scmautodoc:: analysis Task
   :noref:

Further details on the histogram need to be specified in the ``Histogram`` block. 
If more than one ``Histogram`` block is present in the input, more than one histogram will be computed. 
The result is printed to output as text, as well as stored in a binary file (analysis.kf).
By default the histogram contains the number of occurrences of a certain value, 
but the normalized occurrence is provided if the keyword
``Normalized`` in the ``Histogram`` block is specified.

.. scmautodoc:: analysis Histogram Normalized
   :skipblockdescription:

Histograms can be computed for every quantity stored on the molecular dynamics
trajectory file (ams.rkf) in the section History.  Example quantities are
``PotentialEnergy``, ``KineticEnergy``, ``TotalEnergy``, ``Temperature``. In
the histogram block, this quantity is selected with the keyword ``Variable`` in
the ``Axis`` subblock.  If more than one ``Axis`` subblock is present, the
dimensionality of the histogram is increased: Three ``Axis`` subblocks result
in a 3D histogram.

For each histogram axis, the number of bins can be selected with the ``NBins`` keyword in the ``Axis block``,
in which case the range of values along each axis is automatically determined.
The default ``NBins`` value is 100.

Alternatively, a range and a stepsize can be selected with the keyword ``Range`` in the ``Axis`` subblock.
The keyword ``Range`` can contain one, two, or three values:
1: Only a stepsize.
2: A smallest value and a largest value.
3: A smallest value, a largest value, and the stepsize.

.. scmautodoc:: analysis Histogram Axes
   :noref:


.. _AnalysisAutocorrelationFunction:

.. index:: Autocorrelation function

Autocorrelation Functions
#########################

The Analysis program computes autocorrelation functions (ACF) if the ``Task`` keyword is set to AutoCorrelation.

.. scmautodoc:: analysis Task
   :noref:

Further details need to be specified in the ``AutoCorrelation`` block.
If more than one ``AutoCorrelation`` block is present in the input, more than one ACF will be computed.
The result is printed to output as text, as well as stored in a binary file (analysis.kf).

.. scmautodoc:: analysis AutoCorrelation
   :skipblockdescription:

Description
***********

An autocorrelation function :math:`C(t)` describes the average correlation (overlap) of a (vector) property :math:`\textbf{A}` with itself as a function of time.

:math:`C(t) = \langle \textbf{A}(0) \cdot \textbf{A}(t)) \rangle`

The average runs over all time-intervals :math:`\left( t_{0}, t_{0}+t \right),\left( t_{1}, t_{1}+t \right),...,\left( t_{N}, t_{N}+t \right)`, 
with :math:`t_{N} = t_{n} - t_{m}`. Here :math:`n` is the total number of simulation steps in the trajectory, and :math:`m` is the number of discrete :math:`t` values
for which :math:`C(t)` is computed. The value :math:`m` can be set with the keyword ``MaxStep``, and defaults to half the total number
of simulation steps.
If applicable, the average also runs over all possible contributions to :math:`\textbf{A}` at each simulation timestep.
The normalized autocorrelation function :math:`c(t)` describes the decorrelation of the property with time, and always starts at 1.0 at :math:`t=0`.

:math:`c(t) = \frac{\langle \textbf{A}(0) \cdot \textbf{A}(t)) \rangle}{\langle \textbf{A}(0) \cdot \textbf{A}(0)) \rangle}`

In most cases short timescale fluctuations are important, so frequent storage of the desired property is required 
(when preparing the molecular dynamics simulation,
set the ``Frequency`` keyword in the ``Trajectory`` block of the ``MolecularDynanimcs`` settings low, preferably to 1).

A power spectrum is automatically computed
by Fourier transform of the autocorrelation function,
and provides information on the frequencies of the signal.
When the selected property is the dipole moment, the power spectrum matches the IR spectrum.

Options
*******

Autocorrelation functions can be computed for different simulation properties:
1) Dipole moments from atomic charges
2) Velocities
3) User provided values.

.. scmautodoc:: analysis AutoCorrelation Property
   :noref:

With the keyword ``Normalized`` a normalized ACF is computed, 
and with the keyword ``MaxStep`` the number of values :math:`n` in the autocorrelation function 
(:math:`t = [0,t_{1},t_{2},....,t_{n}]`) can be set. 
The default value is half of the total number of simulation steps used.

A subset of atoms for which the property :math:`\textbf{A}` should be selected/computed can be provided in the block ``Atoms``. 
The block can contain element names (recurring keyword ``Element``), or individual atom numbers (recurring keyword ``Atom``).

.. scmautodoc:: analysis AutoCorrelation Atoms
   :noref:

.. _AnalysisDiffusionCoefficient:

.. index:: Diffusion coefficient

Diffusion Coefficient
#####################

The diffusion coefficient can be computed as the integral over the velocity autocorrelation function. 

:math:`D = \frac{1}{3} \int_{t=0}^{t=t_{max}} \langle \textbf{v}(0) \cdot \textbf{v}(t)) \rangle dt`

The factor :math:`\frac{1}{3}` corrects for the dimension of the system, which we assume to be always 3.

The diffusion coefficient is computed if the task ``AutoCorrelation`` is selected, 
and if in the ``AutoCorrelation`` block `DiffusionCoefficient` is selected as the ``Property``.

.. code-block:: bash

   $AMSBIN/analysis <<eor
      Task AutoCorrelation
      AutoCorrelation
         Property DiffusionCoefficient
      End
   eor

.. scmautodoc:: analysis AutoCorrelation Property
   :noref:
   :nosummary:

Again, a subset of atoms can be selected with the sublock ``Atoms``.

The value of the diffusion coefficient is written to the output, as well as to the KF file.

