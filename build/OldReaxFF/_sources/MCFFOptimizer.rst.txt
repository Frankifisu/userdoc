
MCFF Optimizer: Monte Carlo force field parameter optimizer
***********************************************************

The MCFF Optimizer uses a Monte Carlo approach to finding the best fit force field for the given training set.  It is based on the paper by  `E. Iype et. al. <https://doi.org/10.1002/jcc.23246>`__  In the following sections, the input and output of the MCFF Optimizer are described. 

A worked out example on building a training set and optimizing a ReaxFF force field with MCFF is on our `workshop pages <https://www.scm.com/adf-modeling-suite/adf-hands-on-workshops/advanced-2-day-reaxff-workshop/>`__.


Input files
===========

In addition to files specified in the FF Optimizer section the following files must be present in the directory where the reaxff program is executed. 

+ *iopt* - file containing a single text line with 4 on it. This will instruct reaxff to perform a Monte-Carlo force-field optimization.

The mcffopt_water example in the examples/reaxff directory demonstrates the use of the MCFFOptimizer.  Note however that this example is not physically meaningful. For example, many atomic force-field  parameters are allowed to vary in a very broad range, which is the same for all elements. In practice,  you will want to set the range for each element separately. 


Control parameters
==================

The following control parameters are related to MCFFOptimizer. The default value for each parameter  is given in parentheses. 

+ *mcffit* - number of MC iterations (10000). Since the Monte-Carlo method does not have any notion of convergence the optimization is stopped after mcffit iterations.

+ *mcbeta* - initial MC beta parameter in the acceptance probability calculation :math:`P=exp(-\beta \Delta E)` (0.0). Here, :math:`\Delta E` is a difference in the error function between the current and the best step so far. If the current step is the best, it is always accepted. Otherwise, the acceptance probability is calculated using the formula above and it is calculated with a random number from the (0,1) range. The optimal value of beta depends on values of the error function. If absent or set to 0, it will be calculated after the first step as :math:`\beta_0 = \sqrt{\frac{N_{par}}{2}} \frac{1}{E_0})`, where :math:`N_{par}` and :math:`E_0` are the number of variable parameters and the initial error function value, respectively.

+ *mcdbet* - simulated annealing: increase the beta parameter by this value at each step (0.0). A positive mcdbet value means that the probability to take a step that increases the error function will decrease over time. This has the same effect as decreasing the temperature in the classical molecular Monte-Carlo method.

+ *mcbsca* - simulated annealing: divide the beta parameter by this value at each step (1.0). A value of mcbsca less than 1.0 has an effect similar to positive mcdbet. If mcbsca is set to 0, it will be calculated after the first step as :math:`\frac{\beta_n}{\beta_{n+1}} = \sqrt[N_{step}]{\frac{5}{E_0}}`, where :math:`N_{step}` and :math:`E_0` are the number of steps and the initial error function value, respectively.

+ *mcacpf* - probability to vary a variable at each step (0.2). To avoid taking very large steps only some of the variables are varied at each step (selected randomly).

+ *mcrxdd* - number of intervals to divide the parameter range between ffield_min and ffield_max into (100).

+ *mcstep* - initial max step size in units of range/mcrxdd, where range = difference between ffield_max and ffield_min values (1.0).

+ *mcmxst* - maximum allowed value of max step size (100);

+ *mcscps* - factor to scale max step size to satisfy acceptance tolerance (1.1);

+ *mctart* - target acceptance rate, percent (30.0);

+ *mcmart* - max acceptance rate, percent (70.0);

+ *mcmini* - if not 0, minimize the best force-field parameter set after so many iterations (0). The optimization is performed only if the best set has changed since the previous minimization. The minimization employed here is gradient-free and relatively slow so it should not be used too frequently.

+ *replic* - number of replicas to try at each step (1). At each step, replic Monte-Carlo steps are done and the one with the lowest error is selected for the next iteration.

**Relation between mcrxdd, mcstep, mcmxst, and mcscps**. When the parameter ranges are given via ffield_max and ffield_min files, the range for each parameter is divided into mcrxdd intervals. The step taken is a uniformly distributed random value in the range :math:`(-\Delta x, \Delta x)`, where :math:`\Delta x = mcstep*(Xmax-Xmin)/mcrxdd`. Here,  Xmax and Xmin are values of this parameter from ffield_max and ffield_min, respectively. When the parameter range is given via a params file then :math:`\Delta x = mcstep*delta`, where *delta* corresponds the first real number in the params file. When performing optimization, the program keeps track of the average acceptance rate and adjusts  mcstep up or down by the mcscps factor to keep the acceptance rate close to mctart. If the acceptance rate is too low the step size is decreased to allow searching for a smaller  parameter space. The mcstep value can never be larger than mcmxst.  

It should be noted that the value of the MC step size (and thus all the parameters discussed  in this section) applies to all force-field parameters to the same extent, which means that it is very important to select the min and max parameter values very carefully. The rule of thumb  here is that the range should be as small as possible covering only the physically meaningful values. 


Results
=======

Main results of the MCFFOptimizer are saved in the following files: 

+ ffield_best - force-field file corresponding to the lowest error value

+ ffield_last - the most recent accepted force-filed

+ MCFFOptimizer.log - summary of iterations including the error function value, number of changed and  bounded force-field parameters, cumulative number of accepted and rejected steps at each step. Also the  current MC parameters such as the :math:`\beta` value and the acceptance rate, are shown, as well as the elapsed  time in seconds.

+ fort.99 - the error function breakdown for the latest step

+ fort.90 - if fort90 is set in the control file, geo file with optimized geometries corresponding to the current best parameter set


Run-time control
================

The progress of the force-field optimization can be controlled by changing parameters in the  *istop* file present in the calculation directory. The file is read every 10 iterations. The parameters are explained below: 

+ StopKey - replace 0 with 1 to stop the calculation

+ Beta - the current :math:`\beta` value corresponding to the *mcbeta* control parameter

+ Command - one of: NONE, WALK, JUMPWALK, MINIMIZE, JUMPMINI: 
  
+ NONE - no change in the procedure

+ WALK - switch to Monte-Carlo steps (the default);

+ MINIMIZE - switch to gradient-free minimization of the latest accepted force-field;

+ JUMPWALK - take the best force-field so far and start the Monte-Carlo procedure from there;

+ JUMPMINI - take the best force-field so far and minimize it.

+ ScaleFactor - change the current step size corresponding to the *mcstep* control parameter

+ ActiveParameterFraction - set the fraction of force-field parameters changed at each step (*mcacpf*)

+ deltaBeta - change the current value of the *mcdbet* control parameter

+ BetaScaling - change the current value of the *mcbsca* control parameter

+ ScaleParSpace - change the current value of the *mcscps* control parameter

