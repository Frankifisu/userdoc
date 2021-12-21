
.. _parallelization:

Parallelization (MPI and OpenMP)
################################

ReaxFF, both as a program and as an AMS engine, has been parallelized using both MPI and OpenMP. MPI uses multiple processes to share the work, while OpenMP uses multiple threads within the same process. Each parallelization methods has its pluses and minuses. The OpenMP usually has a lower overhead than MPI but MPI can be used on a distributed-memory machine (compute cluster). It is possible to combine both methods in a single job, which may lead to a lower performance because of the double overhead. For small systems pure OpenMP can be much faster than hybrid OpenMP+MPI or pure MPI because of the relatively high cost of MPI communication.

**Number of OpenMP threads**

The number of OpenMP threads is controlled by the OMP_NUM_THREADS environment variable. If OMP_NUM_THREADS is not defined the program will set the number of threads to the minimum of the default number of threads from the OpenMP library and the number of physical processor cores in the machine divided by the number of MPI processes running on it. The default number of threads returned by the OpenMP library depends on different factors: the number of the machine's virtual processors, the MPI and the OpenMP library used and the batch system, if any. For example, when running ReaxFF on a quad-core desktop computer with hyperthreading (8 virtual processors) with IntelMPI using 4 MPI processes, the default number returned by the Intel OpenMP library will usually be 2 because the library is aware of the fact that it is running under MPI. The same OpenMP library running under a different MPI run-time, for example OpenMPI, will probably set the default number of threads to 8. In both cases, ReaxFF will use one OpenMP thread per process because it counts only physical cores and is aware of the job's MPI configuration. 

When running under a batch system the default number of OpenMP threads will depend on the quality of integration of the batch system with the MPI runtime and the OpenMP library. For example, when running an IntelMPI version under SLURM, the number of threads should be set using the --cpus-per-task option to set the number of threads. 

The OMP_NUM_THREADS environment variable's value overrides any defaults or heuristics when present.

**Recommendations**

For single-node calculations we recommend using pure OpenMP. To this end, set the NSCM environment variable to 1 and set OMP_NUM_THREADS to the number of processors to use or leave it undefined to use all cores. 

When running on multiple nodes we recommend using pure MPI. To this end, set the OMP_NUM_THREADS environment variable to 1 and set other MPI-related options as you would do for any other AMS job. This is especially important if you are using an MPI runtime environment loosely integrated with the cluster's batch system. 

