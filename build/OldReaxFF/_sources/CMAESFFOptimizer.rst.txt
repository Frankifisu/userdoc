
.. _cmaes:

CMA-ES Force-field Optimizer
****************************

The CMA-ES FFOptimizer uses the Covariance Matrix Adaptation Evolution Strategy to find the best fit force field for the given training set. The current implementation is using the `c-cmaes library <https://github.com/CMA-ES/c-cmaes>`__ by Nikolaus Hansen. In the following sections, the input and output of the CMA-ES FFOptimizer are described. 

See also: The `advanced tutorial on ReaxFF reparametrization <../Tutorials/Parametrization/ReaxFFParametrizationHandsOn.html>`__ . 

Input files
===========

In addition to files specified in the FF Optimizer section the following files must be present in the directory where the reaxff program is executed. 

+ *iopt* - file containing a single text line with 7 on it. This will instruct reaxff to perform a CMA-ES force-field optimization.

The following files are optional:

+ *cmaes_restart.txt* - a restart file. It should be a copy of the cmaes_resume.txt file from another calculation. If this file is present the optimization procedure will be restarted where it was left off.

+ *params* - If this file is present, it will define the variable reaxff parameters, one line per parameters, as follows:

::

  # i j k   sigma   min   max
    1 1 0    0.1   -1.0  1.0   # The 1st general parameter
    2 3 4    0.1   -1.0  1.0   # The 4th parameter of the 3rd atoms block
  ...

The first three number on a line specify the parameter coordinates (the i,j,k indices). The fourth number is the initial sigma value (the step size) for the given parameter. The fifth and sixth numbers define the range of allowed values for this parameter. 

If sigma is less than or equal to zero then it is determined by dividing the range between *min* and *max* by the *mcrxdd* parameter as described below.

Whenever the CMA-ES algorithm makes a trial step outside the given interval, a very large number for the fitness function is returned without performing the calculation. This should "teach" the CMA-ES algorithm to avoid the forbidden part of the parameter space. If at some point the CMA-ES procedure leads to a mean value (the center of the distribution) outside the allowed interval then the optimization stops.


Control parameters
==================

For compatibility with the MCFFOptimizer the following control parameters are also applicable to the CMA-ES Optimizer. The default value for each parameter is given in parentheses. 

+ *ffotol* - CMA-ES convergence parameter (1.0e-6). The optimization is stopped when the step-size becomes smaller than ffotol for every parameter.

+ *mcffit* - max number of iterations (10000). An optimization is stopped when it has converged or after mcffit iterations.

+ *mcrxdd* - number of steps to divide the parameter range between ffield_min and ffield_max into if the params file is not present (100).

+ *replic* - the CMA-ES sample size. The CMA-ES algorithm is designed to use multiple fitness function values at once, called a sample. The sample size should be at least as large as the default calculated as :math:`M = 4 + 3*ln(N)`, where :math:`N` is the number of variables.

**Relation between mcrxdd and the step size sigma**. When the parameter ranges are given via ffield_max and ffield_min files, the initial sigma parameter for CMA-ES is calculated as :math:`\sigma = (Xmax-Xmin)/mcrxdd`. Here,  Xmax and Xmin are values of this parameter from ffield_max and ffield_min, respectively. When the parameter range is given via a params file then :math:`\sigma` corresponds the first real number in the params file. 



Results
=======

Main results of the CMA-ES Force-Field Optimizer are saved in the following files: 

+ ffield_best - force-field file corresponding to the lowest error value

+ cmaes_progress.txt - a progress file written by the c-cmaes library containing some useful information about the current state of the CMA-ES model.

+ fort.73 - a log file containing some general output from the ReaxCMAESFFOptimizer module.

+ cmaes_resume.txt - a file containing the complete set of CMA-ES model parameters needed to restart the optimization. This file is updated only when a new best-fit force-field is found.

+ fort.99 - the error function breakdown for the latest step

