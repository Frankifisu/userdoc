Compiling AMS from Sources
##########################

**THIS INFO IS ONLY RELEVANT FOR PEOPLE WITH A SOURCE CODE LICENSE! If you are unsure what this means, you can most likely skip reading this page!**

Compiling AMS from sources by end users is not supported on Windows. The following instructions apply to Linux/Unix and Mac OS X only. Compiling AMS2021 from sources is supported for ifort version 19.1.1 with MKL and IntelMPI on linux. For more details on the recommended compilers and libraries, see the `Platform Specific Information <https://www.scm.com/support/downloads/platform-specific-information/>`__.

Unpacking the distribution
**************************

Installing AMS with recompilation in mind is somewhat different from the binary-only installation. The downloaded source and binary tarballs must be unpacked in the following order (using IntelMPI on x86_64-linux in this example):

::

   # First sources
   tar xzf ams2021.102.src.tgz
   # Then binaries
   tar xzf ams2021.102.pc64_linux.intelmpi.bin.tgz

The result will be a ams2021.101 directory containing both binaries (for your platform) and sources.

Note that for Mac OS X, the downloading of the binaries is different. Follow the instructions for downloading and installation of the binaries. Copy the binaries from the downloaded disk image to the directory ams2021.101 that was created from the source code. Depending on where you have put the binaries it could be something like:

::

    cp -r /Applications/AMS2021.102.app/Contents/Resources/amshome/* ams2021.102

Setting up environment
**********************

This document assumes you are using a bash shell. If you are using a different shell, some commands might need to be modified. The following environment variables should be set: 

+ I_MPI_ROOT: this variable must be set if compiling with IntelMPI on linux (the default)

+ MPIDIR: may be needed in the case of compiling AMS with non-default MPI, for example OpenMPI on linux.

+ MATHDIR/MKLROOT: this should be set to the the MKL root folder. If MKLROOT is defined and MATHDIR is not, then MKLROOT will be used.

+ AMSHOME/AMSBIN/AMSRESOURCES/...: the standard environment variables discussed in the `Installation manual <Installation.html#Set-up-the-environment>`__, also needed for running AMS. The easiest way to set the mis to source the amsbashrc.sh script:

::

   cd ams2021.102
   . amsbashrc.sh

Running Install/configure
*************************

After unpacking everything and setting up your environment properly, you need to run the *configure* script. This script is located in the $AMSHOME/Install directory, and it must be executed from the $AMSHOME directory. The script replaces some files in the bin directory with versions specifically targeted for your system. Further, *configure* creates the buildinfo file that you will need to compile AMS.

To see what options the configure script supports, use configure -h:

Example:

::

   cd $AMSHOME
   Install/configure -h

Configure can set up multiple build targets with different configuration options using the -b flag. The options regarding your build target should be wrapped in quotes following a -b flag, starting with the build name. The -b flag can be used multiple times to create different build targets. For example, to create a target with all current release build options: 

::

   Install/configure -b "release -p intelmpi -meadshared -dynamicmkl -plumed"

If a different MPI version is needed (for example OpenMPI) it can be selected with the -p flag: 

::

   Install/configure -b "mydefaulttarget" -b "myompitarget -p openmpi"

Compiling AMS
*************

Next, you need to compile the sources by executing foray located in $AMSBIN. Foray supports parallel compilation to make things faster, use -j N to tell foray you want it to use N processes (for example: -j 4 on a quadcore machine): 

::

   cd $AMSHOME
   bin/foray -j 4

After a while, depending on the speed of your computer, everything should be  ready to use, just as if you had installed the precompiled executables but now with your  modifications included. Use *bin/foray -h* to get a list of all foray options.

