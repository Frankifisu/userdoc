
Control parameters common for all optimizers
============================================

The following control parameters are related to the FFOptimizer. The default value for each parameter is given in parentheses. 

+ *ffoact* - the task ID to be performed by the base FFOptimizer module (i.e. when the iopt file contains 6):
    * 1 - calculate gradient of the error function with respect to the variable FF parameters by finite differences. This option requires 2*N + 1 error function evaluations, where N is the number of variable force-field parameters.
    * 2 - calculate the second derivatives (Hessian) matrix of the error function with respect to the variable FF parameters by finite differences. The eigenvalues and eigenvectors of the obtained Hessian matrix will also be computed. In this case, N^2 + N + 1 function evaluations will be done. Note: a calculation of derivatives can be very slow so make sure you run it on as many processors as possible. 
    * 3 - calculate an error function value for each column-vector of parameters specified in the *params* file. If the params file does not contain any column-vectors (i.e. there are no real numbers at all in the file) then the error function for the current ffield file is calculated. This feature can be used, for example, by external force-field optimizers. The result per trainset.in entry is written to the fort.99 file.
    * 4 - find *replic* random vectors of parameter values that result in a valid (non-NaN) error function value. The random values are distributed uniformly in the allowed parameter space.

+ *ffostp* - the delta used for calculating first and second derivatives by finite differences (0.01). 

The following options may apply to any FF optimization type.

+ *ffdedi* - If running in parallel and *ffdedi* is set to 1 then the master process will run as a dedicated dispatcher and will not perform any computations. The default value depends on the number shared-memory nodes used in the calculation (0 for single-node calculation, 1 otherwise). 

+ *replic* - number of parameter sets to calculate at once for *ffoact* = 4 (1 by default). This control parameter may have different meaning and defaults for other force-field optimizers.

+ *fort99* - if this parameters is set to 0 then the fort.99 files will not be written. By default, every fitness function evaluation produces a fort.99.xxx.yyy file, where xxx is an iteration number and yyy is a replica index at the iteration. This may potentially lead to a large number of fort.99.* files so setting fort99 to 0 can be useful for saving space in long production runs.

+ *fort90* - MCFFOptimizer will create a geo file with optimized geometries corresponding to the current best parameter set.

