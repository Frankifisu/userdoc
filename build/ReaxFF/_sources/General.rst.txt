General
#######

ReaxFF is an engine for modeling chemical reactions with atomistic
potentials based on the reactive force field approach developed by Prof.
Adri van Duin and coworkers. SCM has modernized, parallelized and greatly
optimized the original ReaxFF program. 

.. only:: html

   .. seealso::

      * `GUI overview tutorials <../Tutorials/GettingStarted/GeometryOptimizationOfEthanol.html>`_

      * `ReaxFF-GUI tutorials <../Tutorials/IndexByEngine.html#reaxff>`_

What's new in ReaxFF 2020
*************************


ReaxFF is available in the `AMS driver <../AMS/index.html>`__ as one of
the engines, which means that all :ref:`tasks that can be performed with the AMS
driver <ams_tasks>` are also available for ReaxFF. However, not all tasks from the
classic ReaxFF standalone program are available in the ReaxFF AMS engine, so in the
2020 release of the Amsterdam Modeling Suite, the standalone ReaxFF program and
the ReaxFF engine coexist. **The graphical user interface program AMSinput only
sets up ReaxFF jobs as an engine to the AMS driver**.

For more information, see :ref:`enginevsstandalone`.

**Other new features:** 

* `0D, 1D, and 2D periodicity <../AMS/System.html#geometry-lattice>`__

* :ref:`Tapered bond orders <smoothpes>`

* :ref:`chargeconstraints`


.. note::

   Development of the `old standalone ReaxFF program <../OldReaxFF/index.html>`__
   has stopped.

