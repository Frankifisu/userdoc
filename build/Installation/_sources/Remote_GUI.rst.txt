Using the GUI on a remote machine
#################################

Running the ADF GUI (amsinput) on a remote machine (X forwarding over SSH) can be tricky sometimes. This page will try to explain why and might contain some hints into how to get a remote GUI working. If your remote GUI worked fine with ADF2016 but stopped working with ADF2017, you can probably skip most of this page and read the last section about `ADF2017 and VTK7`_. 

X11 over SSH
************
When connecting to a remote system (let's call it RemoteBox) from your local machine (LocalBox) over SSH, there is the option to enable X forwarding:

::

   ssh -X -Y user@RemoteBox

This allows you to run X11 GUI programs on RemoteBox while the window shows on LocalBox. You can try some simple X11 programs now:

::

   xterm
   xclock

If you got a terminal and a clock popping up in separate windows, you have working X11 forwarding over SSH.

If you got any errors and no window, most likely something fundamental is broken. Check if the RemoteBox allows X11 Forwarding (/etc/ssh/sshd_config should contain "X11Forwarding yes"), and try both the -X and -Y flag on the ssh command. Another thing to check is "xhost", which might also get in the way.


**sidenote on ssh -X and -Y:** There are two ways of enabling X forwarding with SSH, -X and -Y. The default -X flag enables X11 forwarding, but with extended security restrictions to protect LocalBox from malicious behavior of people on the RemoteBox. The -Y flag enables trusted X11 forwarding, which does not enable the additional security extensions. The security extensions are there for good reason, but they can break so many things that some distros (Debian for example) disable them by default, even if you use -X and not -Y. Which mode you decide to use is up to you of course, but if something doesn't work always try using -X -Y (or -XY) before asking for help.

.. attention::

    If you did not succeed in getting an xterm or xclock window to show, then you MUST solve that problem before trying to use 3D graphics. The rest of this text assumes you have a working X11 setup.

X11 with OpenGL over SSH (3D graphics)
**************************************

X11 over SSH can also support OpenGL 3D graphics, using the GLX extensions. To test this run:

::

   glxgears

It should pop up a window with 3 gears, which may or may not be spinning. To get more info about the 3D driver stack, run:

::

   glxinfo |  grep -E " version| string| rendering|display"

If the above two commands produce errors (For example: ``Error: couldn't find RGB GLX visual or fbconfig`` or ``X Error of failed request:``) something fundamental is broken with the 3D setup on RemoteBox or LocalBox. You should check the 3D driver stack on **both** machines, and pay special attention to the libGL.so and libGLX*.so libraries. Make sure you can run ``glxgears`` and ``glxinfo`` on LocalBox before investigating the remote machine.

Intel Graphics (mesa)
=====================

If LocalBox has intel graphics, you might run into problems if RemoteBox uses proprietary hardware & drivers.
First check which libGL.so is used on RemoteBox by logging in via SSH and running:

::

   ldd `which glxinfo`

The output will contain a line similar to:

::

   libGL.so.1 => /usr/lib/x86_64-linux-gnu/libGL.so.1 (0x00007f76cdcaf000)

/usr/lib/x86_64-linux-gnu/libGL.so.1 is most likely a symlink, so use ``ls -l`` to find its true destination:

::

   ls -l /usr/lib/x86_64-linux-gnu/libGL.so.1

if this points to a proprietary graphics library (for example: ``lrwxrwxrwx 1 root root 30 aug 22 13:24 /usr/lib/x86_64-linux-gnu/libGL.so.1 -> /usr/lib/nvidia-361/libGL.so.1``), you can try pre-loading the mesa version of the library on the remote machine. Try to locate the mesa libGL.so:

::

   find /usr -iname "*libGL.so*" -exec ls -l {} \;

If we are lucky we spot the mesa libGL.so in the output. It may look something like this:

::

   /usr/lib/x86_64-linux-gnu/mesa/libGL.so

If you found the mesa libGL.so, try to put it in LD_PRELOAD:

::

   export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/mesa/libGL.so
   glxinfo

If the system was already using the mesa libGL.so, you can try to use indirect rendering by setting the following environment variable:

::

   export LIBGL_ALWAYS_INDIRECT=1

Other useful environment variables can be:

::

   export LIBGL_DEBUG=verbose
   export LIBGL_ALWAYS_SOFTWARE=1

NVidia Graphics
===============

There are probably two libGL implementations on LocalBox if it uses the NVidia proprietary drivers (or 4 if you also have 32bit libraries installed): the opensource "mesa" library (``libGL.so.1.2.0``, most likely in a "mesa" subdirectory) and the proprietary NVidia library that comes with the NVidia drivers. Run the following command to find the libGL libraries on your system:

::

   find /usr -iname "*libGL.so*" -exec ls -l {} \;

Make sure that the ``libGL.so`` and ``libGL.so.1`` symlinks in the generic folders (/usr/lib/, /usr/lib64, /usr/lib/x86_64_linux_gnu) eventually point towards the proprietary library. You will need to have root permissions to change the symlinks.

.. warning::

  Never run any commands as root (or with sudo) to change your system setup if you do not understand them. It is not hard to break a Linux installation when making mistakes as root, so make backups before you change something and double-check what you type when using sudo or the root account!

Another important library when running OpenGL over SSH with NVidia hardware is ``libGLX.so``. Locate it on your system with the following command:

::

   find /usr -iname "*libGLX*.so*" -exec ls -l {} \;

Make sure that there are symlinks to the proprietary library in a generic location (/usr/lib on ubuntu).

You can check if the correct ``libGL.so`` is being used by checking the dynamic library dependencies of glxinfo:

::

   ldd `which glxinfo`

The reported ``libGL.so`` dependency is most likely a symlink, so use ``ls -l`` on it to find out where it points to.

libGL.so examples
-----------------
A correct setup on CentOS 6 with NVidia drivers for example should look something like this:

::

   # first 3 lines are the NVidia lib
   # second set of 3 lines are the mesa lib
   # last two lines are the generic symlinks that point towards the NVidia lib
   -rwxr-xr-x 1 root root 1220472 apr  6 02:51 /usr/lib64/nvidia/libGL.so.352.93
   lrwxrwxrwx 1 root root 15 aug 19 13:33 /usr/lib64/nvidia/libGL.so.1 -> libGL.so.352.93
   lrwxrwxrwx 1 root root 15 aug 19 13:33 /usr/lib64/nvidia/libGL.so -> libGL.so.352.93
   -rwxr-xr-x 1 root root 561640 mei 11 06:38 /usr/lib64/mesa/libGL.so.1.2.0
   lrwxrwxrwx 1 root root 14 jun  6 13:40 /usr/lib64/mesa/libGL.so.1 -> libGL.so.1.2.0
   lrwxrwxrwx 1 root root 14 jun  6 13:40 /usr/lib64/mesa/libGL.so -> libGL.so.1.2.0
   lrwxrwxrwx 1 root root 15 aug 19 13:48 /usr/lib64/libGL.so -> nvidia/libGL.so
   lrwxrwxrwx 1 root root 17 aug 19 13:48 /usr/lib64/libGL.so.1 -> nvidia/libGL.so.1

Another example of an 64bit ubuntu installation with NVidia drivers and 32bit libraries available:

::

   -rw-r--r-- 1 root root 439972 jul 18 05:47 /usr/lib32/nvidia-361/libGL.so.1.0.0 # 32bit nvidia lib
   lrwxrwxrwx 1 root root 10 aug  3 06:14 /usr/lib32/nvidia-361/libGL.so -> libGL.so.1
   lrwxrwxrwx 1 root root 14 aug  3 06:14 /usr/lib32/nvidia-361/libGL.so.1 -> libGL.so.1.0.0
   lrwxrwxrwx 1 root root 10 jun 13  2013 /usr/lib32/libGL.so -> libGL.so.1 #generic 32bit symlink, points to the next line
   lrwxrwxrwx 1 root root 21 aug 22 13:23 /usr/lib32/libGL.so.1 -> nvidia-361/libGL.so.1 # generic 32bit symlink, points to nvidia
   -rw-r--r-- 1 root root 448200 jul 22 09:53 /usr/lib/i386-linux-gnu/mesa/libGL.so.1.2.0 # 32bit mesa lib
   lrwxrwxrwx 1 root root 14 jul 22 09:53 /usr/lib/i386-linux-gnu/mesa/libGL.so.1 -> libGL.so.1.2.0
   -rw-r--r-- 1 root root 579760 jul 18 05:50 /usr/lib/nvidia-361/libGL.so.1.0.0 # 64bit nvidia lib
   lrwxrwxrwx 1 root root 10 aug  3 06:14 /usr/lib/nvidia-361/libGL.so -> libGL.so.1
   lrwxrwxrwx 1 root root 14 aug  3 06:14 /usr/lib/nvidia-361/libGL.so.1 -> libGL.so.1.0.0
   -rw-r--r-- 1 root root 459392 jul 22 09:52 /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1.2.0 # 64 bit mesa lib
   lrwxrwxrwx 1 root root 14 jul 22 09:52 /usr/lib/x86_64-linux-gnu/mesa/libGL.so -> libGL.so.1.2.0
   lrwxrwxrwx 1 root root 14 jul 22 09:52 /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1 -> libGL.so.1.2.0
   lrwxrwxrwx 1 root root 10 aug 22 13:25 /usr/lib/x86_64-linux-gnu/libGL.so -> libGL.so.1 # generic 64bit symlink, points to next line
   lrwxrwxrwx 1 root root 30 aug 22 13:24 /usr/lib/x86_64-linux-gnu/libGL.so.1 -> /usr/lib/nvidia-361/libGL.so.1 # generic 64bit symlink, points to nvidia

AMD Graphics
============

AMD GPUs are reasonably well supported by the latest versions of mesa (ubuntu 16.04), and installing the proprietary Catalyst driver is not always a good idea. If you have an older distro (CentOS 6) you can install the fglrx Catalyst drivers. As a rule of thumb run the following command first:

::

   glxinfo |  grep -E " version| string| rendering|display"

If this reports an OpenGL core profile version string of 4.x, do not install Catalyst. If the OpenGL core profile version string says 3.0, then check on google if fglrx is safe to install for your distribution.

libGL.so examples
-----------------
An example of a CentOS 6 setup with AMD drivers should look a bit like this:

::

   # first 4 lines are the 32bit AMD lib and symlinks
   # next 4 lines are the 64bit AMD lib and symlinks
   # last line is the renamed 64bit mesa library (renamed by the AMD driver installation)
   -rwxr-xr-x. 1 root root 612220 Dec 18  2015 /usr/lib/fglrx/fglrx-libGL.so.1.2
   lrwxrwxrwx. 1 root root 19 Aug 30 08:53 /usr/lib/libGL.so -> /usr/lib/libGL.so.1
   lrwxrwxrwx. 1 root root 21 Aug 30 08:53 /usr/lib/libGL.so.1 -> /usr/lib/libGL.so.1.2
   lrwxrwxrwx. 1 root root 33 Aug 30 08:53 /usr/lib/libGL.so.1.2 -> /usr/lib/fglrx/fglrx-libGL.so.1.2
   -rwxr-xr-x. 1 root root 921928 Dec 18  2015 /usr/lib64/fglrx/fglrx-libGL.so.1.2
   lrwxrwxrwx. 1 root root 21 Aug 30 08:53 /usr/lib64/libGL.so -> /usr/lib64/libGL.so.1
   lrwxrwxrwx. 1 root root 23 Aug 30 08:53 /usr/lib64/libGL.so.1 -> /usr/lib64/libGL.so.1.2
   lrwxrwxrwx. 1 root root 35 Aug 30 08:53 /usr/lib64/libGL.so.1.2 -> /usr/lib64/fglrx/fglrx-libGL.so.1.2
   -rwxr-xr-x. 1 root root 561640 May 11 06:38 /usr/lib64/FGL.renamed.libGL.so.1.2.0

OpenGL direct or indirect rendering
***********************************

OpenGL with X11 can run in two different modes: direct rendering and indirect rendering. The difference between them is that indirect rendering uses the GLX protocol to relay the OpenGL commands from the program to the hardware, which limits OpenGL capabilities to OpenGL 1.4.

When using OpenGL over X11 with SSH, quite often direct rendering is not available and you have to use indirect rendering. Unfortunately indirect rendering is not always secure, so it got disabled by default on many recent Linux Distros. If you are using the mesa ``libGL.so``, you can run the following commands to test if indirect rendering is working on LocalBox:

::

   glxinfo
   export LIBGL_ALWAYS_INDIRECT=1
   glxinfo

If glxinfo crashes with something like:

::

   name of display: :0
   X Error of failed request:  GLXBadContext
     Major opcode of failed request:  154 (GLX)
     Minor opcode of failed request:  6 (X_GLXIsDirect)
     Serial number of failed request:  34
     Current serial number in output stream:  33

after setting LIBGL_ALWAYS_INDIRECT=1, then you might need to enable indirect rendering on LocalBox.

enabling indirect rendering on Xorg 1.17 and newer
==================================================

X 1.17 disables indirect rendering by default. Enabling it can be a bit tricky, because the xorg.conf flag is only available in 1.19 and newer, so you need to use the **+iglx** command line flag when starting the X server.

.. warning::

  Be careful when making changes as root! Running these commands is at your own risk, and you should not execute them if you do not understand what they do.

CentOS 6
--------

The X server call is hardcoded in gdm, so we need to create a wrapper script around Xorg. Log in as root on a console (Ctrl+Alt+F1) or via SSH and do:

::

   cd /usr/bin/
   mv Xorg Xorg.bin
   echo -e '#!/bin/sh\nexec /usr/bin/Xorg.bin +iglx "$@"' > Xorg
   chmod +x Xorg
   init 3 # this stops the X server
   init 5 # this starts the X server again

Ubuntu 16.04
------------

::

   sudo nano /usr/share/lightdm/lightdm.conf.d/50-xserver-command.conf

change the last line from ``xserver-command=X -core`` to ``xserver-command=X -core +iglx``
restart the machine, or restart the X server with:

::

   sudo service lightdm restart

OSX / MacOS
-----------

Mac OS X users who update to XQuartz 2.7.9 will discover that they cannot use GLX applications remotely any more.
This includes the ADF-GUI. To solve, at this point in time: stick to the older version of XQuartz (2.7.8), or install the 2.17.10 beta version: https://www.xquartz.org/releases/XQuartz-2.7.10_beta2.html. After installing they should run this command to enable GLX:

::

   defaults write org.macosforge.xquartz.X11 enable_iglx -bool true

OpenGL2+ with X11 over SSH
**************************

If you need OpenGL2+ features, there are two options: use direct rendering (this usually only works if both LocalBox and RemoteBox use a recent mesa libGL.so), or use ``VirtualGL``.
The VirtualGL tool ( http://www.virtualgl.org/ ) intercepts the OpenGL calls, does the 3D rendering on RemoteBox and then transports the resulting image to LocalBox. For more details on how this is achieved see `their documentation <https://cdn.rawgit.com/VirtualGL/virtualgl/2.5/doc/index.html>`_.

Install VirtualGL on LocalBox and RemoteBox, and configure (run ``vglserver_config`` as root, see the `VirtualGL documentation <https://cdn.rawgit.com/VirtualGL/virtualgl/2.5/doc/index.html#hd006%20to%20setup%20RemoteBox>`_) RemoteBox to operate as a VirtualGL server. RemoteBox should of course also have proper 3D hardware and drivers (intel integrated graphics with recent mesa drivers, or a dedicated AMD/NVidia GPU), and be capable of indirect rendering (see above). 

Once virtualGL is installed and set up on RemoteBox and installed on LocalBox, open a terminal window on LocalBox and connect to RemoteBox with:

::

   vglconnect -s username@RemoteBox

This will start a VirtualGL client on LocalBox and set up two encrypted tunnels to RemoteBox. On RemoteBox you can now run OpenGL programs by starting them through ``vglrun``:

::

   vglrun glxinfo
   vglrun glxgears

If you look at the output of the glxinfo command when running through vglrun, you will see that both the server and client glx vendor string changed into "VirtualGL", and the OpenGL renderer & version string should now say something about the hardware of RemoteBox.

ADF2017 and VTK7
****************

ADF2017 uses VTK7 and newer OpenGL features to dramatically speed up the visualization of large systems. This comes with a higher requirement for the OpenGL version supported by the system: OpenGL 3.2. If your machine does not support this, you might get the following error message when starting the GUI:

::

   Warning: In /home/builder/jenkins/workspace/trunk/label/centos6_impi_lxc/VTK/Rendering/OpenGL2/vtkOpenGLRenderWindow.cxx, line 647
   vtkXOpenGLRenderWindow (0x7b93c40): VTK is designed to work with OpenGL version 3.2 but it appears it has been given a context that does not support 3.2. VTK will run in a compatibility mode designed to work with earlier versions of OpenGL but some features may not work.

In such cases, a fallback mode is available that lowers the OpenGL requirement to version 1.4, but this fallback mode of course does not have the performance benefits of the newer OpenGL features. To enable the fallback mode, set the ``SCM_OPENGL1_FALLBACK`` environment variable to something non-zero:

::

   export SCM_OPENGL1_FALLBACK=1
   amsinput &

The OpenGL 3.2 requirement should not present any problems, unless your hardware or OS is really old. Known problematic cases are:

* CentOS 6 with intel graphics has OpenGL 2.1 (possible solutions: get an NVidia or AMD GPU with closed-source drivers, or use the fallback mode)
* OpenGL with X11 over SSH (possible solutions: use VirtualGL (see `OpenGL2+ with X11 over SSH`_) or the fallback mode)
* Remote Desktop on Windows: The 32bit Windows version of ADF2017.107+ has been made OpenGL 1.4 compatible to deal with older hardware and Remote Desktop problems. You can try to install the 32bit version of ADF2017 on your Windows machine if you have problems with starting the GUI on Windows.

AMS2019/AMS2018 and VTK7
************************

AMS2019 uses the same VTK7 as AMS2018 and ADF2017, and thus also requires OpenGL 3.2 or newer. However, the OpenGL 1.4 fallback mode is now available on 64bit Windows and Linux, and should trigger automatically when it detects an OpenGL version on the system that is too old for the normal mode. The ``SCM_OPENGL1_FALLBACK`` environment variable can also still be used, for example when the detection is not working. Setting this on Windows can be done with the following steps: ``Winkey+R``, ``sysdm.cpl``, Advanced, Environment Variables... Here you can either add the ``SCM_OPENGL1_FALLBACK`` key with value 1 to the current user, or as admin for everyone on the system.

AMS2020/AMS2021 and VTK7
************************

AMS2020/AMS2021 ships a software implementation of OpenGL on Linux and Windows. On Windows this is automatically enabled if the system has no support for OpenGL 3.2 or newer. The ``SCM_OPENGL_SOFTWARE`` environment variable can be set to use this on Linux, or force it on Windows. The ``SCM_OPENGL1_FALLBACK`` environment variable is no longer available.

Sources
*******

The information on this page is a mashup of local knowledge, a lot of testing and reading on the web. The following pages contained some useful information:

* https://www.phoronix.com/scan.php?page=news_item&px=Xorg-IGLX-Potential-Bye-Bye
* https://wiki.archlinux.org/index.php/VirtualGL
* https://cdn.rawgit.com/VirtualGL/virtualgl/2.5/doc/index.html
* https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure
* https://unix.stackexchange.com/a/1441

