.. _metatag WINDOWSQUICKSTART: 

Windows Quickstart Guide
########################

This quickstart guide is for installing AMS on a Windows desktop/laptop machine. Please also read the :ref:`generic Installation manual <metatag INSTRUCTIONS>` if you encounter problems.

**Start with downloading AMS2021 for Windows** from the `main download page <http://www.scm.com/support/downloads/>`__ (click the orange *Download* button below the blue Windows logo), and save it in your Downloads folder. Open ams2021.101.pc64_windows.intelmpi.exe after the download is complete, for example by opening your Downloads folder in the Windows explorer and double-clicking it. Newer versions of AMS will have a different number in the file name.

**Follow the on-screen instructions** to install AMS2021 to your computer. The InstallShield Wizard asks where to install the program (C:\\AMS2021.101 by default), where to save your AMS files (C:\\ADF_DATA by default), and where to store temporary data (C:\\SCMTMP by default). All these paths can be changed, but should **NOT** contain any spaces!

During installation a text console window will open to extract a few more files needed for using AMS, do NOT close this window! If you do, the installation has to be started all over again.

Once the installation is complete, **double-click the "AMSjobs" shortcut** on the desktop to start AMS2021.

AMS2021 also includes a **bash/python** scripting environment, which can be started by starting *ams_command_line.bat* from the AMS2021 installation folder. This will open a windows shell with the correct environment set up for running AMS/ADF. The scripting environment also provides a *bash* shell (simply type **bash** and hit enter) and a `python stack <../Scripting/Python_Stack/Python_Stack.html>`__.

