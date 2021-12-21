
FF Optimizer: framework for force field parameter optimization
##############################################################

The FF Optimizer is a base module that can be extended with other modules that implement specific optimization methods. The base FFOptimizer module offers methods to compute the cost function (also known as the error or the fitness function) and its first and second derivatives with respect to the force-field parameter values. Besides that, there are two extensions available that implement global optimization methods: Monte-Carlo (MCFF) and Covariance Matrix Adaptation Evolution Strategy (CMA-ES).


.. toctree::
   :maxdepth: 1

   ffopt_Input_files
   ffopt_Control_parameters
   MCFFOptimizer
   CMAESFFOptimizer

.. tip::

   See also: The `advanced tutorial on ReaxFF reparametrization <../Tutorials/Parametrization/ReaxFFParametrizationHandsOn.html>`__ .

.. note::

   With the 2020 release of the Amsterdam Modeling Suite, we have introduced `ParAMS <../params/index.html>`__, a Python based toolkit integrated with the `AMS driver <../AMS/index.html>`__ and `PLAMS <../plams/index.html>`__ for the optimization of parameterized engines, such as `ReaxFF <../ReaxFF/index.html>`__ and `DFTB <../DFTB/index.html>`__. ParAMS provides similar functionality to the parameter optimizers included in the standalone ReaxFF program, which are documented in this manual. We encourage users interested in parameterization to consider using ParAMS. It is currently in an alpha state, but will be developed further in the future and will at some point become the default parameterization tool in the Amsterdam Modeling Suite.
