Introduction 
#############

This document describes the installation of the Amsterdam Modeling Suite (AMS) on the supported platforms. For optimal performance, some system specific tuning may be needed. Therefore, it is strongly recommended to also read the `additional information and known issues <Additional_Information_and_Known_Issues.html>`__ .

The Amsterdam Modeling Suite consists of the following main classes of programs: 

+ Computational engines: ADF, BAND, COSMO-RS, DFTB, UFF, ReaxFF and MOPAC. Each of the engines has its own (text-based) input and output and can be used from scripts and the command line. New in the AMS2019 release is the `AMS driver program <../AMS/General.html>`__, which houses the BAND, DFTB, UFF and ReaxFF engines. Within this manual we try to use the word *AMS* for all the computational engines, and *ADF* for the molecular DFT program.

+ Utilities and property programs. These are used primarily for pre- and post-processing data of the computational engines.

+ Graphical user interface (GUI), which is used to prepare input for computational engines and to visually present their results.

AMS is bundled as a complete package and all components are installed at once. Your license file determines which of the functionality will be available after installation.

The AMS package is written with a Unix-like environment in mind, but Unix/commandline knowledge is not needed install or use AMS from the GUI. Linux laptop and desktop users can follow the instructions in the :ref:`Linux Quickstart Guide <metatag LINUXQUICKSTART>` to install AMS. Windows users can follow the on-screen instructions after starting the installer, or take a look at the :ref:`Windows Quickstart Guide <metatag WINDOWSQUICKSTART>`. MacOS/OSX users can simply drag&drop the AMS application to install it, see the :ref:`MacOS Quickstart Guide <metatag MACOSQUICKSTART>` for more details. 

If you plan to do advanced scripting or run AMS from the command line, then you will need to know how to write shell scripts and have some knowledge of the environment variables. If you are the one who is going to install the package on a shared Unix-like system, such as Linux cluster environment, then you need to know how to modify shell resource files such as .bashrc. 

.. _metatag REQUIREMENTS: 

Requirements
************

Summary
-------

AMS2021 can be used on anything from a simple laptop to big Linux cluster environments, and is tested on a wide variety of hardware. 

Recommended minimum hardware specification:

+ Intel i5 or better 64bit CPU
+ 8GB RAM
+ 250GB SSD
+ OpenGL 3.2 graphics

Absolute minimum hardware specification:

+ 64bit CPU
+ 2GB RAM
+ 6GB storage for installation
+ OpenGL 1.4 graphics

Supported Operating Systems:

+ Windows 7/8/10
+ OSX 10.13 or newer
+ Linux with GLIBC v2.11 or higher: CentOS/RHEL 6 or 7, Debian 6 or newer, SUSE 11.3 or newer, Ubuntu 10.04 or newer, etc. AMS is regularly tested on CentOS 7, Ubuntu 18.04/20.04 and Arch Linux.

Specific hardware and software requirements for the AMS package depend on the platform. The list of supported platforms, including information on the operating system, parallel environment (MPI), and compilers used is available in the `Download section <http://www.scm.com/support/downloads/>`__ of our web site.

Detailed Hardware requirements
------------------------------

**CPU**

AMS2021 runs on any x86_64 CPU, but performs best on modern Intel CPUs with AVX or AVX-512 instruction sets and AMD Zen CPUs (Ryzen, Threadripper, EPYC). Especially the AMD Zen2/Zen3 processors give very good performance (Ryzen 3000/4000/5000, EPYC 7**2/7**3). We have also gotten reports of AMS2021 working correctly on the new Apple processors (M1), but we currently do not offer technical support for this platform.

**Memory**

In a parallel calculation, the total amount of memory used by the job is a sum of that used by each process. Starting from ADF2010, some large chunks of data are placed in the shared memory so the sum rule does not strictly hold. In principle, it is more correct to count memory per process but since AMS is an MPI program it runs most efficiently when the number of processes corresponds to the number of physical processors cores. Therefore, all memory amounts below are per processor core. 

The amount of RAM per core needed to run AMS depends greatly on the kind of calculation you perform. For small calculations, 256 MB will be sufficient, but if there is a lot of memory available AMS may run significantly faster. A large amount memory also reduces the load on the disks, which may speed up your calculation depending on the I/O sub-system and the operating system. 

The memory requirement increases with the system size. For example, for a molecule containing 100 atoms with a DZ basis set it may be sufficient to have 256 MB but for a molecule with 1000 atoms up to 8 gigabytes may be required. Also, if you are going to perform TDDFT, relativistic spin-orbit or analytical frequency calculations then the amount of memory should be larger. As an indication, an analytical vibrational frequency calculation of a organometallic complex containing 105 atoms with a TZP basis set uses up to 1GB of RAM per process but it can be done with less, even though not as efficiently. 

**Disk**

For installation of the package on Linux/Unix you need from about 5GB (without sources) to 8GB (with sources and compiled objects). The run-time (scratch) disk space requirements greatly depend on what type of calculation you perform. For the ADF engine, it may range from a few megabytes for a small molecule up to a hundred gigabytes for a large molecule with a large basis set, the amount scaling quadratically with the system size. Using a Solid State Drive (SSD) helps performance, especially for bigger calculations.

**Network**

First of all, a network card must be present in the computer as its hardware MAC address is used as the computer's ID for the licensing.

In order to enable MPI on a standalone Windows computer, one may need to create a dummy network connection by adding a network "card" called Microsoft Loopback Adapter. This interface will be assigned an IP address from a private range. 

**Multi-host parallel performance.** 

As far as performance concerned, a switched Gigabit Ethernet network is typically sufficient for good parallel performance on up to four nodes if the nodes do not have too many CPU cores per node. If you are going to use more nodes, or nodes with high core count (>16 cores per node), you may need faster communication hardware, such as Infiniband, to get good performance. Please note that multi-host execution is not supported on Windows.

**Graphics**

Starting with ADF2017, the GUI requires OpenGL 3.2 to run. For Linux and Windows users there is an OpenGL software mode available for older hardware, please read more about it in the `Remote GUI documentation <Remote_GUI.html>`__.

Software requirements
---------------------

**Operating System** 

The package runs on Windows and on the following Unix variants: Linux, Mac OS X. 

On the Apple systems the Mac OS X 10.13 and newer is supported. 

On linux both the compute engines, python scripting environment and GUI require a GLIBC version of 2.11 or higher. AMS is compiled on CentOS 6, the code gets tested daily on CentOS 6, Ubuntu 18.04, Ubuntu 20.04 and Arch.

The Windows version of AMS is supported on the desktop editions of Windows (7, 8, 8.1 and 10). The Windows Server is **not** supported.

**Additional libraries** 

Certain version of AMS will require different libraries to be installed on the system depending on the MPI library used.

**Graphics** 

In order to run the the graphical user interface (GUI) the computer needs to have an OpenGL-capable graphics subsystem (hardware, drivers and libraries). Besides that, on Linux the following (or equivalent) packages must be installed: 

::

   fontconfig
   freetype
   libdrm
   libICE
   libSM
   libstdc++
   libX11
   libXau
   libXdmcp
   libXext
   libXft
   libXrender
   libXScrnSaver (Ubuntu users may need to install libXss1)
   libXt
   libXxf86vm
   mesa-libGL
   mesa-libGLU

The GUI will not able to start without shared libraries provided by these packages. 

**NOTE:** If you receive an error about libXss (libXss.so.1: cannot open shared object file: No such file or directory), you need to install libXScrnSaver (redhat/centos: yum install libXScrnSaver) or libxss1 (ubuntu/debian: sudo apt install libxss1).

**Compiler** 

If you have a license for the source code, you can compile the source yourself, with or without your own modifications. 

The source consists mainly of Fortran95/2003 code, with some small parts written in C. Some of the Fortran2003 features are also used so a compiler supporting it is required. You must use object-compatible Fortran and C compilers to those we are using on the same platform, since some parts of the code are available only as object modules. For all x86 platforms it is currently Intel Fortran 19.1. It is very unlikely that other compilers, or even a different major version of the same compiler, will work with these object modules. We cannot support compilers different from what we are using ourselves. 

To check which compiler to use, check the `detailed machine information <https://www.scm.com/support/downloads/platform-specific-information/>`__ on the Download section of our web site. 

Important changes since AMS2021
*******************************

+ AMS now has a package manager for installing optional components. For more details see `Installing Optional Components <Optional_Components.html>`__

Important changes since AMS2020
*******************************

+ Linux binaires for AMD Zen processors now use MKL instead of OpenBLAS. These binaries are forced to run in AVX2 mode, and give better performance on AMD Zen-based processors.

Important changes since AMS2018
*******************************

No major technical changes have been made in AMS2019

Important changes since ADF2017
*******************************

Some of the technical changes made since ADF2017:

+ No more support for 32-bit Windows: almost all PCs nowadays run on 64-bit processors and 64-bit Operating Systems. If you need a 32-bit version, we advise you to use ADF2017 instead.
+ Automated OpenGL fallback mode for GUI on older graphics: available on 64-bit Windows and Linux.
+ No more support for CentOS 5 on Linux: The Intel ifort 18 compiler unfortunately introduces an unavoidable GLIBC 2.11 requirement, which means AMS2018/AMS2019 no longer works on older Linux systems.
+ Linux binaries for AMD Zen processors: AMS2018/AMS2019 is available with OpenBLAS instead of MKL, optimized for the AMD Zen architecture. These binaries should be used on AMD Ryzen / Threadripper and Eypc CPUs for better performance.
+ Updated Python stack: Our python stack is now based on the Enthought Python v3.6 stack, most included modules have also been updated.
+ AVX-512 support: AMS2018/AMS2019 is compiled with AVX-512 optimizations for the latest Intel Xeon Scalable Processors (Skylake SP).


