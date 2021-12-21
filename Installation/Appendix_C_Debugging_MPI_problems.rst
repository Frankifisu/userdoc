Appendix C. Debugging MPI Problems
##################################

The Amsterdam Modelling Suite (AMS) is designed to work out of the box on as many platforms as possible, but it could be that you are experiencing problems with running our programs in parallel. This mostly happens on linux cluster environments, but the information below could also be useful for Windows or MacOS users. However, anything that mentions cluster environment or batch system is linux specific!


Technical introduction into AMS
*******************************

Most of our compute programs use Message Passing Interface (MPI) communication for parallel operation. To make AMS as easy to use as possible we ship the MPI runtime libraries within the AMS package, and take care of launching of the MPI programs in parallel in our start script. Because of this setup it is not needed to "mpirun" our programs yourself, so **never do something like "mpirun $AMSBIN/ams"** !


Execution order
===============

When starting one of our programs, for example *$AMSBIN/ams*, you actually call our start script via a symbolic link. This start script then:

* checks which program it should launch, based on the name it was called from or the value of the -x flag
* detects how many cores should be used: -n or the NSCM environment variable are read, when both are empty we detect the cpu core count (see below for cluster environments!)
* sources the *$AMSBIN/setenv.sh* script to set up environment variables
* Write the given input to a temporary file
* detect if and which batch system it is running on
* do the correct parallel MPI launch of the program

``Old pre-AMS2020 info:`` When running *$AMSBIN/adf*, this sequence is preceded by a program that first sets up and runs the "atomic create runs" in serial.


The $AMSBIN/start script
========================

As described above, the start script takes care of selecting the number of cores to use for the calculation, sourcing the setenv.sh script, and launching the selected program in parallel. You might need to edit it if your AMS program fails to start, or does not run on the correct number of cores.

The start script tries to detect if it is running on a cluster environment with a batch system such as PBS/Torque, SLURM, SGE or LSB. If it detects one of the environment variables associated with these batch systems, it will leave figuring out the MPI job configuration (cores and nodes) to the MPI library. The MPI library should get the number of cores to run on, and which compute nodes to use (in case of a multi-node calculation) from the batch system. the **NSCM** environment variable and the **-n** flag are ignored in this case!

If no batch system is detected, and both **NSCM** and **-n** are not used to explicitly set the number of cores to use for running the AMS program, then the start script attempts to detect the number of cores on the machine, and uses all available cores. We only count real CPU cores (no hyperthreading or modules with shared FPUs such as AMD Bulldozer), because the AMS programs do not benefit from hyperthreading.

Finally the start script launches the AMS program using the correct mpi commands for the situation.


The $AMSBIN/setenv.sh script
============================

The *$AMSBIN/setenv.sh* script takes care of setting up environment variables needed for running the AMS programs. This includes among others:

* the LD_LIBRARY_PATH variable with locations to the required libraries (and DYLD_LIBRARY_PATH)
* the PYTHONPATH variable

The setenv script also responds to a couple of environment variables, such as **SCM_USE_LOCAL_IMPI**, **SCM_USE_IMPI_2021**, and **SCM_USE_LOCAL_OMPI**. See `Appendix A on Environment Variables <Appendix_A_Environment_Variables.html>`__ for details.


MPI runtimes
============

The Amsterdam Modelling Suite ships with the required MPI runtime inside the package. For MacOS this is OpenMPI, for Windows this is IntelMPI, and for Linux both IntelMPI and OpenMPI flavors exist. When working on Linux we advise to use the IntelMPI library, as this provides the best out-of-the-box experience. The OpenMPI runtime has no batch system integration build into it, so it will most likely not work under a batch system. The runtimes can be found in *$AMSBIN/IntelMPI* or *$AMSBIN/openmpi*, and are loaded into the environment by the setenv.sh script. See the `Additional information section <Additional_Information_and_Known_Issues.html#running-mpi-jobs>`__ for more details.


Debugging MPI issues
********************

For non-batch system (desktop/laptop usage) related MPI issues, please contact support@scm.com as these should almost never happen. However, linux users might want to try using a newer IntelMPI runtime by setting **export SCM_USE_IMPI_2021=1** in their environment.

For cluster usage we always advise to use the IntelMPI version. AMS ships with the IntelMPI runtime inside the package, you do not need to install this separately. IntelMPI can be used on Cray systems as well via the ABI compatibility, see the `Additional information section <Additional_Information_and_Known_Issues.html#running-mpi-jobs>`__ for more details. If you for whatever reason need to use OpenMPI instead, make sure to compile and use your own OpenMPI version that matches the version used to build AMS (currently 2.1.2), and set SCM_USE_LOCAL_OMPI=true in the environment.
Make sure to to read the `Additional information and known issues document <Additional_Information_and_Known_Issues.html>`__ before you dive into debugging MPI!

The generic scheme for debugging IntelMPI / batch system issues consists of the following steps:

#. Start by setting up the IntelMPI runtime libaries in the environment: load it from a module, or load your AMS environment and execute ". $AMSBIN/setenv.sh" without the quotes. Keep in mind that in order to test the IntelMPI 2021 runtime shipped with AMS2021, you will need to execute "export SCM_USE_IMPI_2021=1" before sourcing the setenv.sh script.
#. get the intel mpirun to work. Environment variables that are useful for this are I_MPI_DEBUG=100 (or higher), I_MPI_OFI_PROVIDER_DUMP=1 (for information about the interconnects detected by IntelMPI), the I_MPI_FABRICS (for selecting a specific fabric, options depend on the IntelMPI runtime version) and I_MPI_HYDRA_TOPOLIB. See the `IntelMPI 2018u3 developer reference manual <https://software.intel.com/en-us/download/intel-mpi-library-for-linux-os-developer-reference-2018-update-3>`__ for details on these variables for the default IntelMPI runtime. If you are using the IntelMPI 2021 runtime, see `IntelMPI current developer reference manual <https://software.intel.com/content/www/us/en/develop/documentation/mpi-developer-reference-linux/top/environment-variable-reference.html>`__
#. get a small mpi test program that's compiled with IntelMPI and a Fortran compiler. To make things a bit easier you can download an example with `both binary and source code here <https://downloads.scm.com/distr/MPItest.tgz>`__.
#. try to mpirun the test program (mpirun ./mpitest) on a single node via the batch system. This usually respects the batch system reservation. In case it doesn't you will need to dive into the manuals to see what kind of environment variables you need to set, or arguments you need to give to get it to integrate with the batch system. `IntelMPI developer references and guides <https://software.intel.com/en-us/articles/intel-mpi-library-documentation-overview>`__ help out with this, but make sure to get the manual matching your IntelMPI version! The manual of your batch system might also hold some clues.
#. once single node jobs work, then it is time to see what needs to be done for multi-node jobs. Usually this can be set up via integration with the batch system, but if that fails you could always write a bit of code that generates a "machine file", and tell IntelMPI to use this file with the -machinefile flag (see `this <https://software.intel.com/en-us/mpi-developer-guide-linux-controlling-process-placement>`__ for how a machine file should look)

It might be that the default IntelMPI runtime shipped with AMS (currently 2018 update 3) needs to be updated for a better integration with your batch system. In such a case you can try the IntelMPI 2021 runtime (also shipped with AMS) by setting "export SCM_USE_IMPI_2021=1" in your environment. Or you can download and install a newer IntelMPI runtime package (those are free to use), and repeat the previous steps. If the downloaded IntelMPI works better than the 2018 or 2021 runtime shipped with AMS, then you can set the "export SCM_USE_LOCAL_IMPI=true" environment variable. This tells AMS not to load the distributed IntelMPI into the environment, but instead use the one already available. (You do not need to recompile AMS for this!)

Finally: when requesting support for MPI issues via support@scm.com, make sure to include as much information as possible. For example: which batch system are you using, what version is it, do you have a special interconnect such as Infiniband, and of course always send us all the input and output files produced by the failed job, including the sdtout and stderr of the batch system. From our experience the fastest way to resolve such issues is if somebody from SCM can work directly on the machine. Therefore you might want to consider setting up a form of temporary remote access for an SCM employee to help you out.
