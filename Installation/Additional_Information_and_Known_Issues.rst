Additional Information and Known Issues
#######################################


Windows Subsystem for Linux (WSL) and Docker
********************************************

AMS does **NOT** run in parallel under WSL1, WSL2, or Docker on Windows, because the IntelMPI library does not support these configurations.

Shared memory and batch systems (SLURM)
***************************************

When discussing memory usage by a parallel job one should distinguish the private and shared memory. The private memory is, well, private to each process and to get the total job's memory usage one should add up the sizes of private memory segments from all processes. The shared memory is used by several processes on a shared-memory node, so for the job's total one should add each shared memory segment only once. However most batch systems ignore the fact that shared memory segments are shared and instead of adding it to the total on the per-node basis they add it per-process. This leads to the batch system greatly overestimating the memory consumption for jobs that use a lot of shared memory, for example, ADF calculations with hybrid functionals. This may lead to such jobs being killed and/or the users being over-charged or forced to use the more expensive hugemem queues. This would be totally unnecessary if the job accounting was properly configured. Luckily, SLURM has the JobAcctGatherParams=\ `UsePss <https://slurm.schedmd.com/slurm.conf.html>`__ option (off by default) that is supposed to take care of the private vs shared memory difference and ensure the correct accounting of ADF jobs. You can check the status of JobAcctGatherParams on your SLURM system with the following command:

::

   scontrol show config | grep JobAcctGatherParams

GPFS file system
****************

Starting with AMS2019, the KF sub-system (used for handling binary files such as ADF's TAPE* files) has been rewritten to use memory-mapped files. The mmap() system call implementation is file-system dependent and, unfortunately, it is not equally efficient in different file systems. The memory-mapped files implementation in GPFS is extremely inefficient. Therefore the users should avoid using a GPFS for scratch files. 


Running MPI jobs
****************

Most programs in the Amsterdam Modeling Suite (AMS) are MPI-enabled, and they are set up to run in parallel automatically, both from the GUI and the command line. For example, to run a parallel AMS calculation from the command line, simply do:

::

   $AMSBIN/ams < myinputfile

A common mistake by people who have worked with MPI programs before is to "mpirun" the programs manually, which results in a parallel mpirun call and usually a lot of errors. All MPI programs in the AMS suite are executed via *$AMSBIN/start* to set up the environment and call mpirun for you. If you need to modify the *mpirun* command, please edit the *$AMSBIN/start* script.

Technical explanation
---------------------

In the example above, AMS is started in parallel, which involves a couple of files:

+ $AMSBIN/ams: a symbolic link to the $AMSBIN/start script
+ $AMSBIN/start: this script sources $AMSBIN/setenv.sh to set up most of the environment, determines the name of the used symlink, and then starts the related binary (ams.exe in this case) via mpirun. On Linux clusters it also attempts to detect the scheduler to launch the MPI program with the allocated resources.
+ $AMSBIN/setenv.sh: when sourced, this script sets up the correct environment for locating libraries and runtimes such as MKL and IntelMPI
+ myinputfile: A valid input file. Some examples can be found in $AMSHOME/examples, and of course the input is also documented per program in the manual.

More on running MPI jobs
************************

MPI (Message Passing Interface) is a standard describing how to pass messages between programs running on the same or different machines.  

MPI is a formal standard and it is actively supported by all major vendors. Some vendors have highly-optimized MPI libraries available on their systems. There are also a couple of open-source implementations of the MPI standard, such as MPICH and OpenMPI. There are also numerous commercial MPI implementations that support a wide range of systems and interconnects, for example, HP-MPI (formerly known as Platform-MPI) and IntelMPI. 

Support for a particular MPI implementation in ADF can be considered at three levels: the source code, the configure script, and pre-compiled binaries. At each level different MPI implementations may be supported. 

The ADF source code is not implementation-specific and thus theoretically it supports any MPI library. Many popular MPI implementations are supported at the level of the configure script, but depending on your local setup you may need to make some modifications in the buildinfo file after running configure. For example on 64-bit Linux IntelMPI and OpenMPI should work directly, but using other MPI flavors will most likely require manual changes to the *buildinfo* file correct the include and linker paths to the MPI libraries of your system. The configure script will also try to generate an appropriate $AMSBIN/start script, but this might also need modification when using different MPI libraries. In general it is best to use the same MPI version used by SCM for the precompiled binaries.

When choosing an MPI implementation for pre-compiled binaries, SCM considers many factors including (but not limited to) the re-distribution policy, performance, and built-in support for modern interconnects. IntelMPI is currently the standard MPI implementation supported by SCM because it has the most favorable combination of these factors at this moment. For platforms where IntelMPI is supported its runtime is distributed with ADF (Windows, Linux). OpenMPI builds are also available for linux, but should only be used in case of problems with IntelMPI. A different MPI implementation will be standard on a platform where IntelMPI is not available. It may or may not be distributed with ADF. For example, SGI MPT is standard on SGI machines and OpenMPI is standard on Mac OS X platforms, but only the latter is distributed together with ADF.

When pre-compiled binaries do not work on your computer(s) due to incompatibility of the standard MPI library with your soft- and/or hardware, the SCM staff will be glad to assist you in compiling ADF with the MPI implementation supported on your machine(s). 

If you are going to use an MPI version of the ADF package, and it is not IntelMPI or OpenMPI, you will need to determine if the corresponding MPI run-time environment is already installed on your machine. If not, you will need to install it separately from ADF. As it has been already mentioned, IntelMPI and OpenMPI are bundled with the corresponding version of ADF so you don't need to worry about installing them separately. 

**Running with MPI on more than one node** 

When running on more than one machine (for example on a cluster **without** a batch system) you need to specify a list of hosts on which mpirun needs to spawn processes. In principle, this is implementation-specific and may be not required if the MPI is tightly integrated with your operating and/or batch system. For example for MPICH1 you can do this by preparing a file containing hostnames of the nodes (one per line) you will use in your parallel job. Then you set the SCM_MACHINEFILE environment variable pointing to the file. 

When you submit a parallel job to a batch system the job scheduler usually provides a list of nodes allocated to the job. The $AMSBIN/start shell script has some logic to extract this information from the batch system and pass it to the MPI's launcher command (typically mpirun). In some cases, depending on your cluster configuration, this logic may fail. If this happens, you should examine the $AMSBIN/start file and edit the relevant portion of it. For example, you may need to add commands that process the batch system-provided nodelist or change mpirun's command-line options or even replace the mpirun command altogether. 

IntelMPI and core-binding
*************************

IntelMPI by default uses core binding for the spawned processes (also known as process pinning). This can be disabled by setting the **I_MPI_PIN** environment variable to "off".

IntelMPI and SLURM
******************

To get IntelMPI work under SLURM one needs to edit the $AMSBIN/start script and change the value of the I_MPI_PMI_LIBRARY environment variable to point to a correct libpmi library from SLURM. If your SLURM system is configured to use PMI2, then it could also be sufficient to comment out the I_MPI_PMI_LIBRARY line in the $AMSBIN/start script. 

Depending on your SLURM version and configuration, it might be necessary to use the IntelMPI 2021 runtime (export SCM_USE_IMPI_2021=1), or use a local IntelMPI runtime from the modules system (export SCM_USE_LOCAL_IMPI=1, and make sure to load the local IntelMPI module). 

IntelMPI and SGE
****************

To get IntelMPI working with Sun Grid Engine, one has to define a parallel environment. How this can be done is described on the `intel website <https://software.intel.com/en-us/articles/integrating-intel-mpi-sge>`_. It is important for modern versions of IntelMPI (as used in AMS2021) and newer to make sure to set "job_is_first_task FALSE" in the parallel environment, otherwise jobs will fail to start.

IntelMPI and ABI compatibility
******************************

IntelMPI v5.0 or newer is ABI (Application Binary Interface) compatible with Cray MPT v7.0.0 or newer and MPICH v3.1 and newer. This means that binaries compiled with one of these libraries can use the other ones during run-time without problems. Our IntelMPI binaries should work out-of-the-box on Cray machines using the ABI compatibility, and can also be used in combination with MPICH 3.2. 

To run ADF with MPICH instead of IntelMPI, simply **export SCM_USE_LOCAL_IMPI=true**, and make sure the MPICH mpirun command is available in your PATH variable. Core binding (process pinning) is disabled by default for MPICH, to enable this add "-bind-to core" to the mpirun commands in the $AMSBIN/start file.

Multi-node issues
*****************

A common reason for multi-node jobs failing where single-node jobs work, is a missing scratch folder on the secondary nodes. Especially SLURM systems are known to sometimes only create the TMPDIR folder on the first node of the job. To solve this, make sure that the SCM_TMPDIR exists before starting the AMS/ADF calculation. For example, under SLURM you could try "srun --ntasks-per-node=1 mkdir -p $SCM_TMPDIR" from your submit script, or even incorporate it into the $AMSBIN/start script.

OpenMPI on Linux
****************

The OpenMPI 2.1.2 binaries supplied with AMS2021 should work on desktop, laptop and workstation machines out of the box (single-node usage). On cluster environments it might be necessary to compile an OpenMPI 2.1 library with support for the cluster queueing system and/or the infiniband solution. Make sure to **export SCM_USE_LOCAL_OMPI=true** before starting programs to enable your local OpenMPI version instead of the one shipped with ADF. Core binding (process pinning) is enabled by default for OpenMPI, to disable this add "--bind-to none" to the mpirun commands in the $AMSBIN/start file.

Corrupted License File
**********************

You may find that, after having installed the license file, the program still does not run and prints a message "LICENSE CORRUPT". There are a few possible causes. To explain how this error may come about, and how you overcome it, a few words on license files. 

Each license file consists of pairs of lines. The first of each pair is text that states in a human-readable format a couple of typical aspects: A 'feature' that you are allowed to use (for instance 'ADF'), the expiration date, a (maximum) release (version) number of the software and so on. The second line contains the same information in encrypted format: a long string of characters that appear to make little sense. The program reads the license file and checks, with its internal encrypting formulas, that the two lines match. If not, it stops and prints a "LICENSE CORRUPT" message. 

So, there are two common reasons why this may happen: 

You can use the **fixlic** utility to try to fix this automatically. Please be aware that the **fixlic** utility will try to fix the file pointed to by the $SCMLICENSE environment variable and replace it with the fixed copy. Thus, you need to make a backup of your license file first and you need to have write permissions for it. 

::

   cp $SCMLICENSE $SCMLICENSE.backup
   $AMSBIN/fixlic

Windows: running jobs from the command line
*******************************************

In order to run ADF or any other program from the package without the GUI, navigate to the ADF installation directory and double click the **adf_command_file.bat** file. It will start a Windows command interpreter and set up the environment specific for that installation of ADF. Once it has started, cd to your jobs directory by entering the following commands at the prompt:

::

   C:
   cd \ADF_DATA

Then, run your job as follows (assuming the job is called h2o):

::

   sh h2o.job

You can also prepare a job from a .ams file and run it using only two commands:

::

   sh amsprep -t h2o.ams -j h2o > h2o.job
   sh h2o.job

Please note that you do need to use *sh* in the commands above because both h2o.job and amsprep are shell scripts and, thus, they must be interpreted by a shell. 

If you are comfortable with a UNIX shell environment, you can also start a bash shell and enjoy a basic msys2 LINUX environment:

::

   bash
