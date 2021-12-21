Appendix B. Directory Structure of the AMS Package
##################################################

Below is the list of major parts of the AMS package.

The bin directory
*****************

When the package is installed, the executable files are placed in $AMSHOME/bin.  The binary executable file is usually called 'ams.exe', 'reaxff.exe', and so on. On Windows  it is ams.3.exe, reaxff.3.exe, etc. There will also be files called just 'ams' or 'reaxff'. The latter are shell scripts that execute the corresponding binaries.

You should use the script files, rather than the executables directly. The script files provide a correct environment, and if needed prepare for running in parallel and then launch the binary using the correct mpirun command. See also the sample run scripts and the Examples document.

The $AMSBIN/setenv.sh and $AMSBIN/start scripts take care of setting up the environment and starting the binaries. If necessary, it parses the information provided by a batch system and sets up a machinefile (or an appfile) and runs tasks in parallel. Edit the file if you need to customize the way MPI programs are started.

The atomicdata directory
************************

The directory atomicdata/ contains a large amount of data needed by programs from the AMS package at run time. For example, it contains basis sets for all atoms. Generally you should  **not** modify any of the files in this directory.

The basis sets are described in detail in the `ADF manual <../ADF/Input/Coordinates_basis_fragments.html>`__ and `BAND manual <../BAND/Accuracy_and_Efficiency/Basis_Set.html>`__ 

The data directory
******************

The directory data/ contains files needed for running the programs and GUI from the AMS package. No modifications should be made to the files in this directory.

The examples directory
**********************

The directory examples/ contains sample script and output files. The files with extension .run are shell scripts that also contain embedded input. Thus, these files should be executed, and not given as input to AMS.

The example calculations are documented in the `ADF Examples documentation <../ADF/Examples/Examples.html>`__, and `BAND Examples documentation <../BAND/Examples/TOC.html>`__. 

The src directory
*****************

The source files are only visible if you have a copy of the source code distribution. The source code files found in the program and library directories and subdirectories thereof have extensions .f, .f90, .c or .cu and contain FORTAN or C/CUDA code. Other source files are include files (files with extension .fh or .h). When compiling, the object files are generated in the folder $AMSHOME/build, and archived into libraries.

Compilation is done by $AMSBIN/foray, and the configure options are located in $AMSHOME/Install/-machinetype-/Forayflags.

The Install directory contains a configure script, some data files which provide generic input for configure (start,  starttcl, and some more), a portable preprocessor cpp (based on  Mouse cpp) and machine-specific files that are unpacked into the bin folder (precompiled packages), or the build folder (precompiled libraries). The machine-specific folders start with x86 or x86_64.

The Utils directory
*******************

The Utils/ directory contains the "run_test" script and two "rc" scripts. The run_test script can be used to run examples from the examples/ folder and validate their output. The amsrc.sh and amsrc.csh can be used instead of the amsbashrc.sh script in case one uses a C/TC/Z-shell (amsrc.csh), or if bash needs to be avoided (amsrc.sh).

The Doc directory
*****************

All the user documentation for AMS is present in html format in $AMSBIN/Doc.  Documentation is also available on the  `SCM website <http://www.scm.com/support>`__ 

The scripting directory
***********************

This directory contains some useful scripts that are part of the AMS package.

