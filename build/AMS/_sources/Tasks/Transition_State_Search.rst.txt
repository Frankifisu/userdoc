.. index:: Transition state search

.. _TransitionStateSearch:

Transition state search
=======================

A transition state (TS) search is very much like a :ref:`geometry
optimization<GeometryOptimization>`: the purpose is to find a stationary point
on the potential energy surface, primarily by monitoring the energy gradients,
which should vanish. The difference between a transition state and a minimum is
that at the transition state the Hessian has a negative eigenvalue: We are at a
saddle point, not a minimum, with the "negative" mode connecting the two basins
on the potential energy surface.

.. seealso::

  * :ref:`Examples`
  * Tutorial `Transition state search and characterization of a Ziegler Natta Catalyst <../../Tutorials/StructureAndReactivity/ZN-PES-Scan_TST.html>`__
  * Tutorial `Tips and Tricks for Transition State Searches for Click Reactions <../../Tutorials/StructureAndReactivity/TipsAndTricksForTS.html>`__


A transition state search in AMS is performed by selecting the corresponding
task::

   Task TransitionStateSearch

Due to the similarities between energy minimization and transition state search,
the ``TransitionStateSearch`` task in AMS is actually implemented as a special
kind of geometry optimization using the :ref:`quasi-Newton<QuasiNewton>`
optimizer. As such all the settings and keywords described on the :ref:`geometry
optimization manual page<GeometryOptimization>` also apply to transition state
searches.

In a geometry optimization with a quasi-Newton based optimizer the Hessian is
used to make a reasonably sized step in the "downhill" direction on the
potential energy surface, as the goal is simply to minimize the energy. A
transition state search is a bit different: In the first step a normal mode is
picked along which the energy is to be *maximized*, while it is *minimized*
along all other directions. Normally the mode with the lowest eigenvalue is
picked, since we know that there should be exactly one negative eigenvalue at
the TS geometry, but one can also choose an approximate reaction coordinate, see ``ReactionCoordinate``.
If the initial geometry is sufficiently close to the transition
state, i.e. we are close to the saddle, the lowest mode is normally the correct
one to follow in order to get to the ridge of the saddle. Alternatively a
different mode can also be selected manually.

.. scmautodoc:: ams TransitionStateSearch

This selection happens only in the first step. Subsequent steps will attempt to
maximize along the mode that resembles most (by overlap) the previous
maximization direction.

Practice shows that transition states are much harder to find than a minimum.
For a large part this is due to the much stronger anharmonicities that usually
occur near the TS, which threaten to invalidate the quasi-Newton methods to find
the stationary point. For this reason it is good advice to be more cautious in
the optimization strategy when approaching a transition state:

* We recommend starting the transition state search with an intial geometry that
  is already close to the transition state. One can use a :ref:`potential energy
  surface scan<PESScan>` along something resembling the reaction coordinate to
  get a rough idea where the transition state is. This geometry can then be used
  as an initial geometry for the transitions state search.

* It is strongly recommended to manually supply a good initial Hessian for the
  transition state search. Otherwise the first step of the search might not be
  taken in the correct direction and subsequent steps will attempt to keep
  steering in the wrong direction. In AMS this is easily possible by loading a
  Hessian from a previous calculation, see the :ref:`initial Hessian
  section<InitialHessian>` of this manual. A good way to obtain a reasonable
  Hessian is to compute it explicitly with one of the fast engines (i.e. at a
  lower lever of theory) and read that Hessian as the initial Hessian for the
  transition state search at a higher level of theory.

* When no accurate initial Hessian is available, it may be a good idea to specify an approximate
  normal mode vector using the ``ReactionCoordinate`` input block. A reaction coordinate
  is a linear combination of distances and/or valence and dihedral angles::

    TransitionStateSearch
      ReactionCoordinate
        Distance  i j     fac
        Distance  i j     fac
        Angle     i j k   fac
        Dihedral  i j k l fac
      End
    End

  Here, ``i``, ``j``, ``k``, and ``l`` are atom indices, and the ``fac``
  is the factor with which the internal coordinate enters the linear combination.

  One should be careful when specifying more than one bond or angle as a transition
  state reaction coordinate (TSRC). For example, suppose atom 2 is located between
  atoms 1 and 3. Then the following ReactionCoordinate block::

    TransitionStateSearch
      ReactionCoordinate
        Distance 1 2  1.0
        Distance 2 3 -1.0
      End
    End

  means that the TSRC consists of two distances: R(1-2) and R(2-3). The positive
  direction of the TSRC is defined as an increase of the R(1-2) and a decrease
  of the R(2-3). In other words, this TSRC corresponds to atom 2
  moving along the R(1-3) axis.

* When the method converges it is usually a good idea to verify that the found
  geometry is indeed a transition state. This can be done by performing a
  frequency analysis and checking whether the Hessian has exactly one negative
  eigenvalue (represented by a mode with a negative frequency). Doing so is
  expensive however. Since we are really only interested in the lowest two
  normal modes calculating the full Hessian is however not necessary and one can
  use the faster PES point characterization instead. This uses a Davidson-type
  algorithm to obtain the lowest few normal modes without constructing the full
  Hessian. The user is referred to the :ref:`PES point
  characterization<PESPointCharacterization>` documentation page for further
  details.
