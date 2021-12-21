Appendix A. Environment Variables
#################################

If you start the MacOSX ADF-GUI application the environment defined by your shell startup scripts is ignored.
Instead the bundled ADF is used, and environment variables may be defined in a file $HOME/.scmenv .

The following environment varables must always be set for all ADF versions.

**AMSHOME**: full path of the ADF installation directory, for example, $HOME/ams2021.101 .

**AMSBIN**: full path ADF directory with binaries, typically set to $AMSHOME/bin .

**AMSRESOURCES**: full path of the directory with the ADF database (basis sets and so on), typically set to $AMSHOME/atomicdata

**SCMLICENSE**: full path-name of the license file, for example $AMSHOME/license.txt.

**SCM_DOMAINCHECK**: set to yes if you have a license based on your domain info (DNS). If it is defined but no proper DNS sever is available, delays will often occur.

**SCM_TMPDIR**: full path of the directory where all processes will create their temporary files. See also the `Installation manual <Installation.html#set-up-the-scratch-space>`__ and the special section on SCM_TMPDIR below.

The following environment variable may be required at run-time by a parallel version.

**NSCM**: The number of processes to be used in a particular calculation. This variable should only be set per job. Do **not** add any NSCM definitions to your shell resource files. Please note that the NSCM value is typically ignored in job submitted through a batch system because then the number of processors is determined by the batch job's properties.

**SCM_MACHINEFILE** full path-name of the file containing a list nodes to use for a job; **Important:** this variable should **only** be set if multiple computers are used without any batch system and then it should be set on the per-job basis. The file pointed to by the variable must already exist and it must contain a list of nodes on which a particular job is about to be executed, possibly with their processor count.

**SCM_USE_LOCAL_IMPI** this applies only to IntelMPI distributions. Setting this environment variable to not be empty will disable the IntelMPI runtime environment shipped with the AMS distribution, allowing the use of a local IntelMPI installation, or any other ABI-compatible local MPI installation (MPICH v3.1 or newer for example). The environment must be properly set up on the machine, meaning I_MPI_ROOT must be set, and mpirun should be in the PATH, and the libraries must be in LD_LIBRARY_PATH.

**SCM_USE_IMPI_2021** this applies only to IntelMPI distributions of AMS2021 and newer. Setting this environment variable to not be empty will load the IntelMPI 2021 runtime shipped with the AMS distribution instead of the 2018 version. This can solve problems on certain linux distributions, cluster environments and/or AMD Zen processors. 

**SCM_USE_LOCAL_OMPI** this applies only to OpenMPI distributions. Setting this environment variable to not be empty will disable the OpenMPI runtime environment shipped with the adf distribution, allowing the use of a local OpenMPI 2.0 installation. The environment must be properly set up on the machine, meaning OPAL_PREFIX must be set, and mpirun should be in the PATH, and the libraries must be in LD_LIBRARY_PATH.

**SCM_PYTHONDIR**: This environment variable specifies where the AMS python distribution will search for a python virtual environment to use. If no suitable virtual environment exists in this directory, it will be created. To not use a virtual environment, set SCM_PYTHONDIR to an empty string.

**SCM_PYTHONPATH**: The contents of this environment variable gets prepended to the PYTHONPATH variable when using the AMS python distribution. You can add the paths to other python modules that you wish to use in combination with the shipped python distribution to this variable to make them available.

**The following environment variables are relevant for the GUI modules.**
For a full list, see the `GUI Environment Variables <../GUI/GUI_Environment_Variables.html>`_ page.

**SCM_ERROR_MAIL**: e-mail address for error reports

**SCM_GUIRC**: location of the preferences file, by default $HOME/.scm_guirc

**SCM_GUIPREFSDIR**: location of the preferences folder, by default $HOME/.scm_gui/ (available since ADF2013.01b)

**SCM_TPLDIR**: location of the templates directory, by default no extra templates are loaded

**SCM_STRUCTURES**: location of the structures directory, by default no extra structures are loaded

**SCM_RESULTDIR**: location of the results directory, by default the current directory used

**DISPLAY**: specifies the X-window display to use and is required for all X11 programs on Linux/Unix and Mac OS X. On MaC OS X you should typically not set it as it will be set automatically. Setting it will break this.

**SCM_QUEUES**: path to the dynamic queues directory, by default AMSjobs will search the remote $HOME/.scmgui file

**SCM_OPENGL_SOFTWARE**: Linux and Windows (available since AMS2020). If set to be non-empty, the GUI will use a software OpenGL implementation. See `Using the GUI on a remote machine <Remote_GUI.html>`__ for more information.

**SCM_OPENGL1_FALLBACK**: No longer used since AMS2019.305 (applies from ADF2017 until AMS2019.304), see SCM_OPENGL_SOFTWARE and `Using the GUI on a remote machine <Remote_GUI.html>`__ for more information.

**The AMS driver environment variables can be found in the** `AMS Documentation <../AMS/Input_Output.html#ams-environment-variables>`__

**The following environment variables are relevant for source distributions only, and only at the configure time.**

**MPIDIR and MATHDIR**: see `Compiling ADF from Sources <Compiling_ADF_from_Sources.html>`_

**The following environment variables may be set to modify other aspects of ADF execution. All of them are optional and some are used for debugging only.**

**SCM_GPUENABLED**: Environment flag to turn GPU acceleration on or off. Only works for the CUDA-enabled binaries. Setting this variable to TRUE turns GPU acceleration on, setting it to FALSE turns it off. If the input contains a GPU%Enabled input key then this environment variable will be ignored.

**SCM_MAXCOMMLENGTH**: when performing collective MPI communications ADF breaks them into pieces of at most SCM_MAXCOMMLENGTH elements, each element being 4 or 8 bytes long. So in practice the largest collective MPI operation should not exceed SCM_MAXCOMMLENGTH*8 bytes in size. By default, SCM_MAXCOMMLENGTH is set to 268435455 on Linux and 4194304 on Windows and macOS. When the SCM_MAXCOMMLENGTH environment variable is set its value is used instead. 

**SCM_VECTORLENGTH**: all DFT programs within the ADF package use numerical integration, and this is normally the most time-consuming part of the code. Numerical integration involves summing together results for each 'integration point'. The best performance is achieved when handling a number of points at the same time. The number of integration points handled together is called the block length or the vector length. If the block length is too small, you will have a significant overhead and the programs may become very slow. If the block length is too large, lots of data will not fit in the processor cache and again the program will not run at the maximum speed. The optimal block length is somewhere in between, ranging from 32 to 4096 depending on your hardware. Sometimes it pays off to set the block length explicitly NOT to a power of 2 to avoid memory bank conflicts. Again, try it yourself with your typical calculation on your production machine to find out the optimal value for your situation. On most machines, the default 128 is a good value.

**SCM_SHAR_NCORES**: setting this variable to a number forces AMS to split each physical node into sub-nodes when allocating shared memory. Each sub-node will contain up to the specified number of processes. This will work only if ranks are assigned to physical and NUMA nodes sequentially. The result is unpredictable if a round-robin rank distribution is used.

**SCM_SHAR_PER_SOCKET**: setting this variable to any non-empty string forces AMS for Linux to ignore NUMA nodes and use one node per CPU socket instead. This may be helpful when the NUMA granularity is too fine, for example on  AMD Zen and other architectures using chiplet design. This variable has no effect when no CPU affinity (or CPU binding) is used.

**SCM_SHAR_NONUMA**: setting this variable to any non-empty string forces AMS for Linux to ignore NUMA nodes and use the whole shared memory machine as one node. This may be helpful when the job uses too much shared memory otherwise.

**SCM_SHAR_EXCEPTIONS**: setting this variable to "*" disables the use of shared arrays.

**SCM_SHAR_LIMIT**: sets the limit on the total size of shared arrays in megabytes. The default is a bit less than half of the node's total RAM. If a new shared array would cause the total amount of shared memory to go over the limit, then instead of placing the array into shared memory it is created as a shared file in the scratch directory of the node-master. The file is then memory-mapped into the address space of all processes on the node. The effect will be the same as when the array is placed into shared memory except that there may be a delay due to disk I/O when the array is destroyed (because on some systems it may have to be written to the disk first). 

**SCM_DEBUG**: setting this to a non-empty string will cause each MPI rank to print values of relevant environment variables and some messages about copying files to/from SCM_TMPDIR.

**SCM_NOMEMCHECK**: setting this to a non-empty string disables checks on memory allocation failures. The usefulness of this variable is questionable.

**SCM_NODOMAINCHECK**: setting this to a non-empty string disables DNS requests when verifying the license. Use this variable if you experience long delays at the start of each calculation.

**SCM_TRACETIMER**: setting this to a non-empty string will produce additional output on entry/exit to/from internal timers.

**SCM_DEBUG_ALL**: setting this to yes is equivalent to specifying DEBUG $ALL in the input

More on the SCM_TMPDIR variable
*******************************

Below we will explain in more detail how does the SCM_TMPDIR environment work. Every parallel job consists of one master and one or more slave tasks. Master and slaves behave a bit differently with respect to their scratch directories.

**Slave processes**

Slave processes will always create a directory for their scratch files in $SCM_TMPDIR and *chdir* to it to avoid any risk that shared files are updated by more that one process at the same time. For efficiency reasons, that directory should reside on a local disk unless you are using very, very fast shared file system for large files. You need write access to that directory, and the file system should have enough free space. Please note that the SCM_TMPDIR environment variable will be passed from the master to slaves. After the job is finished, slave processes will delete their scratch directories. This can disabled by setting the SCM_DEBUG environment variable to any text, for example, to "yes". In this case the scratch directory and all its contents will be left intact. This directory will also be left behind when a job has crashed or has been killed. Each slave writes its text output to a file called KidOutput located in its scratch directory. In case of an error this file will likely contain some sensible error message. If an error occurs and a slave process exits in a controllable way then in order to avoid losing the file ADF will copy the file to the directory, from which the job was started, as KidOutput__#, where # is the process' rank.

**Master process or serial runs**

The master process (which is the only process in a serial run) will also create its temporary files in its own sub-directory of $SCM_TMPDIR. There are some exceptions. Some files, such as logfile and TAPE13, will be created in the directory where ADF was started because they are not performance-critical but are convenient to have in the current directory for different reasons. For example, logfile is nice to have in the current directory in order to follow the calculation progress and the TAPE13 is an emergency restart file that can be used if ADF crashes or is killed. At the end of a calculation, the master will copy all result files from its scratch directory to the directory where it was started.


**Using multiple scratch disks**

It is possible to use multiple physical scratch disks in a parallel calculation. See the `Installation manual <Installation.html#set-up-the-scratch-space>`__ for more information about this.
