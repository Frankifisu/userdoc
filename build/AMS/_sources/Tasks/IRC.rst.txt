.. index:: IRC
.. index:: Intrinsic reaction coordinate
.. index:: MEP
.. index:: Minimum energy profile

.. _IRC:

Intrinsic Reaction Coordinate (IRC)
***********************************

The path of a chemical reaction can be traced from the transition state (TS) to the products and/or reactants using the Intrinsic Reaction Coordinate (IRC) method [#ref1]_ [#ref2]_. **The method assumes that the starting geometry is a fair approximation of the TS**. A minimum energy profile (MEP) is defined as the steepest-descent path on the potential energy surface from the transition state down towards a local minimum. An IRC path is defined similarly but in the mass-weighted coordinates [#ref3]_, which means that instead of the steepest descent direction it follows that of the maximum instantaneous acceleration. This makes IRC somewhat related to the Molecular Dynamics method. The energy profile is obtained as well as the length and curvature properties of the path, providing the basic quantities for an analysis of the reaction path.

.. image:: ../images/irc.png
   :width: 100%
   :align: center

.. seealso::

  :ref:`Examples` and the `PES exploration for hydrohalogenation tutorial <../../Tutorials/StructureAndReactivity/PESExpHydrohalogenation.html#obtaining-the-reaction-path-with-the-irc-intrinsic-reaction-coordinate-method>`__


Method details
==============

Calculation of an IRC path consists of two nested loops, the so-called outer and inner loops. The outer loop runs over IRC points and the inner loop is over geometry optimization steps for the given IRC point. The first IRC point starts from the transition state geometry, which is a saddle point, in one of the two possible downhill directions. Each IRC point after that starts from the optimized geometry of the previous point. At the start of every step, the pivot point is determined, which is a point at the Step/2 distance in the direction opposite to the gradient. When working in the mass-weighted coordinates, this direction corresponds to the acceleration of the corresponding atom. The final point of the given IRC step corresponds to the energy minimum point at the same distance (Step/2) from the pivot point further downhill. More precisely, the coordinates of the target point are optimized during the inner loop to minimize projection of the gradient on the hypersphere of radius Step/2 around the pivot point.
The angle between the (pivot-start) and (pivot-final) vectors determines the curvature of the reaction path. If this angle becomes smaller than 90 degrees then the IRC scan is considered to have reached vicinity of an endpoint and the program switches to energy minimization (options for this energy minimization can be specified in the :ref:`Geometry Optimization <ams-key-geometryoptimization>` block.). If the angle is between 90 and 120 degrees then the current IRC step is canceled and a new one is started from the same starting point with half the initial Step parameter. In all other cases the optimized geometry becomes a starting point for the next IRC step. By default, when the forward path is completed the backward one is started from the same TS geometry. When both forward and backward paths are complete, a summary of the whole reaction path is printed to the output.

Input
=====

The IRC scan in AMS is triggered by setting the ``Task`` to ``IRC``:

::

    Task IRC

All IRC-related options are specified in the IRC input block:

.. scmautodoc:: ams IRC
   :onlysummary:

All keys of the IRC block have reasonable defaults or are optional. Thus, in principle, the IRC block can be omitted altogether. These are some of the main options:

.. scmautodoc:: ams IRC Direction Step InitialHessian
   :nosummary:
   :noref:
   :skipblockdescription:

The following keys set limits on the number of steps for the inner and outer IRC loops and, related to that, the geometry optimization criteria. Note that tighter criteria may require a greater MaxIterations limit. Please also note that the outer loop limits are valid for each half of the path (forward and backward) separately. That is, if all settings are left at their defaults then up to 200 IRC points may be calculated, each of them may require up to 300 energy evaluations.

.. scmautodoc:: ams IRC MaxIRCSteps MaxPoints MaxIterations Convergence MinPathLength
   :nosummary:
   :noref:
   :skipblockdescription:

The following keys modify other aspects of the IRC scan:

.. scmautodoc:: ams IRC CoordinateType MinEnergyProfile KeepConvergedResults
   :nosummary:
   :noref:
   :skipblockdescription:

It is possible to restart an IRC calculation that crashed, has been killed or exceeded the MaxPoints limit, or to re-compute the path starting from a certain point, using the Restart key:

.. scmautodoc:: ams IRC  Restart
   :nosummary:
   :noref:
   :skipblockdescription:





Output
======

A summary of reaction path is printed to the output file at the end of the IRC calculation.

The IRC reaction path can be visualized using the AMSmovie GUI module.

Results of an IRC calculation are also stored in the History section of the 'ams.rkf' file, just like in a normal geometry optimization. In addition to the standard KF variables such as "Coords" and "Energy", the following IRC-specific variables are also created:

* *IRCDirection* - IRC direction to which this point belongs: 1 - forward, 2 - backward.
* *IRCIteration* - the IRC (a.k.a. the outer loop) iteration number.
* *OptIteration* - the geometry optimization (a.k.a. the inner loop) iteration number (0 means the results correspond to the converged geometry at this IRC step).
* *IRCGradMax* - value of the max component of the IRC gradient that determines convergence of the inner loop.
* *IRCGradRms* - the RMS value of the IRC gradient that determines convergence of the inner loop. Both the ircGradRms and the ircGradMax are given in the mass-weighted atomic units for IRC steps and in the atomic units for the final minimization loop.
* *ArcLength* - length, in Angstrom, of the arc that connects the initial and the final point of this IRC step. The corresponding pivot point is located near the the middle point of the arc.
* *Angle* - value of the angle (in degrees) between lines connecting the pivot point with the initial and final points. A value of 180 degrees means the path is passing straight through the pivot point, while a smaller value means the path makes a bend at this point.
* *PathLength* - sum of the *ArcLength* values from the transition state up to this point, in Angstrom.
* *Converged* - a Fortran logical value containing the convergence status of the given geometry.

The IRC section of the RKF file contains all the data needed for a successful restart procedure.

.. only:: html

  .. rubric:: References

.. [#ref1] L.\  Deng, T. Ziegler and L. Fan, *A combined density functional and intrinsic reaction coordinate study on the ground state energy surface of H*\ :sub:`2` *CO*, `Journal of Chemical Physics 99, 3823 (1993) <https://doi.org/10.1063/1.466129>`__

.. [#ref2] L.\  Deng and T. Ziegler, *The determination of Intrinsic Reaction Coordinates by density functional theory*, `International Journal of Quantum Chemistry 52, 731 (1994) <https://doi.org/10.1002/qua.560520406>`__

.. [#ref3] C.\  Gonzalez and H.B. Schlegel, *Reaction Path Following In Mass-Weighted Internal Coordinates* `J. Phys. Chem. 94, 5523-5527 (1990) <https://doi.org/10.1021/j100377a021>`__
