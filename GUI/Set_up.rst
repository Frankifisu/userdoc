Set up
######

.. _metatag SETUP: 

Mouse
*****

A three-button mouse is also very convenient for using the ADF-GUI, and on a Mac you can use a Magic mouse for this purpose. To get three buttons (instead of the standard one or two), download and install one of the free utilities  BetterTouchTool or MagicPrefs, and configure it to add a middle click. 

Running Remotely
****************

To use AMSjobs with remote machines, you need to set up ssh first. You should take care to configure things such that you do not need to type a password when you access your remote machine. To do this you need to: 

+ create **keys**,
+ run an **ssh agent**,
+ add your public key to the **authorized_keys** file on the remote machine.
+ set up a ssh config file, if needed. This allows you to automatically set options, like the user name to use on the remote machine. 

Thus, users (and AMSjobs) should be able to use ssh to log in to the remote machine without ever needing to enter a password. 

If you are using OpenSSH (typically on Linux machine or MacOSX) you can make the communication with the remote machine much more  efficient by setting the SCM_SSH_MULTIPLEXING environment variable to yes (in the GUI Preferences module). 

AMSjobs does not store passwords, it always uses the ssh command to communicate with remote systems. 

For more information, consult your ssh documentation or one of the many guides on the internet. 

OpenGL3.2+, fallback mode
*************************

The GUI needs OpenGL 3.2 or later. Using it results in a much better performance, especially for bigger systems. Also some new graphical features depend on it.
That OpenGL version may not be available when you are running on old hardware or OS, or when you are running remotely via X11 with GLX or some remote desktop solutions.

When the GUI detects a problem with the OpenGL version it will automatically activate a fallback option. That will normally just run, but it will be significantly
slower, and of course the features depending on OpenGl 3.2 will be missing. We advise that you try to update your system to solve this issue.
For remote use of a linux machine a solution could be the use of VirtualGL.

For more details please see the `Installation manual <../Installation/Remote_GUI.html#opengl2-with-x11-over-ssh>`__.

Font issues
***********

The GUI used unicode characters in many places. For example, the proper characters for Angstrom, degrees Celcius, and many more.
You can see examples by starting AMSinput, selecting a Geometry Optimization, and then going to the details page (by clicking the ... button).
There you should see a couple of Angstrom symbols if everything is working as intended.

On most machines this will just work out of the box. If not, the issue might be that the default font on the machine does not support such characters.
Try installing a font line DejaVU Sans and Monospace DejaVu. On Centos you can do this (as root) with the command:::

      yum install dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-serif-fonts


AMSjobs Queues
**************

Defining proper queues in AMSjobs will making the GUI much easier. For example, you can run as easily on a remote compute cluster that you have access to as on your local desktop. AMSjobs will handle all the details like transferring input and output files, and you can even monitor the progress of running jobs as if they were running on your local machine. 

So you should take some time to set up the queues correctly. It is possible that there are predefined queues on your remote machine.  Then you can configure AMSjobs to automatically use those queues. You can find a description of the AMSjobs queues and how to set them up later in :ref:`this manual <metatag ADFJOBS>`.


Quantum ESPRESSO
****************
.. _metatag QESETUP: 

Quantum ESPRESSO is an open source package that can perform plane wave SCF calculations, among other things. 
See `www.quantum-espresso.org <http://www.quantum-espresso.org>`__ for details.

Quantum ESPRESSO is *not* included in the ADF distribution.
The GUI works with the standard Quantum ESPRESSO distribution (version 6.3), no changes have been made. 

Installing using AMSpackages
----------------------------

The easiest way to install it is just to open AMSinput and go to the Quantum ESPRESSO section.
This will use AMSpackages to check if QE has already been installed, and if not it will install it using AMSpackages.
An environment variable ``SCM_PKG_QE`` will be set pointing to the install location.

To force installation of Quantum ESPRESSO (for example to re-install it to make sure you have a clean version), use the  **SCM → Packages** command, and use the AMSpackages module to remove and reinstall Quantum ESPRESSO.

Alternatively, the precompiled Quantum ESPRESSO binaries are `available <https://www.scm.com/support/downloads/quantum-espresso-binaries/>`__ from the SCM web site.

The search path for Quantum ESPRESSO by the GUI and by the run scripts made by the GUI is:

#. ``$SCM_QEDIR`` (this allows you to override which Quantum ESPRESSO to use even if installed via AMSpackages)
#. ``$SCM_PKG_QE`` (this is where AMSpackages installs QE and pseudo potentials, do not change SCM_PKG_QE yourself)
#. ``$AMSBIN`` (and ``$AMSHOME/atomicdata`` for the pseudo potentials)

For an example of how to override the Quantum ESPRESSO installation using ``$SCM_QEDIR`` on windows, or on a remote Linux machine
please see the videos below.
These assume that you have downloaded the binaries, and pseudopotential files to the computer already.

Using SCM_QEDIR on Windows
--------------------------

This video demonstrates how to extract the binaries and pseudopotential files from the website, and set the SCM_QEDIR variable
on a windows machine. This will allow both the GUI and run scripts to make use of of Quantum ESPRESSO. 
This is recommended only if you don't wish to use the build installed by the package manager.

.. raw:: html     

  <center>
    <video width="480" height="320" muted="true" controls src="https://downloads.scm.com/distr/qe_windows_qedir.mp4"></video>
  </center>

You will need an internet connection to see the video.

Make sure that the binaries are inside the folder ``$SCM_QEDIR/qe-6.3/bin``,
and the pseudopotential files are inside ``$SCM_QEDIR/upf_files-6.2.1``.
The example video uses the binaries from the website, which automatically contain the right paths.
Alternatively you can provide these yourself.


Using SCM_QEDIR on Linux
------------------------

This video demonstrates how to extract the binaries and pseudopotential files from the website, and set the SCM_QEDIR variable
on a remote Linux command line. This is recommended only if you don't wish to use the build installed by the package manager.

.. raw:: html     

  <center>
    <video width="480" height="320" muted="true" controls src="https://downloads.scm.com/distr/qe_remote_linux.mp4"></video>
  </center>

You will need an internet connection to see the video.

Make sure that the binaries are inside the folder ``$SCM_QEDIR/qe-6.3/bin``,
and the pseudopotential files are inside ``$SCM_QEDIR/upf_files-6.2.1``.
The example video uses the binaries from the website, which automatically contain the right paths.
Alternatively you can provide these yourself. 

This video assumes AMSBIN has been added to your PATH variable. If this is not the case,
qerc.sh can be found using ``$AMSBIN/qerc.sh`` instead.