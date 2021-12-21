.. _metatag LINUXQUICKSTART: 

Linux Quickstart Guide
######################

This quickstart guide is for installing AMS on a Linux desktop/laptop machine. For cluster installations please read the :ref:`generic Installation manual <metatag INSTRUCTIONS>`

**NOTE:** The following steps should be taken under a normal user account. Do not use the root account or superuser!

**Start with downloading AMS2021 for Linux** from the `main download page <http://www.scm.com/support/downloads/>`__ (click the orange *Download* button below the penguin), and save it in your Downloads folder. You do not need to open the file. If you have an AMD Zen processor (Ryzen/EPYC), then download the "Linux Intel MPI, optimized for AMD-Zen" binary instead.

Now **open a terminal** (Ctrl+Alt+T usually works, otherwise browse your application menus), and run the commands below to **extract the download into your homefolder**. Make sure to replace the ams2021.101.pc64_linux.intelmpi part to match the name of the file you downloaded (in case of a newer version, or if you downloaded a snapshot or development version). Try to use copy and paste (right-click with your mouse in the terminal screen to paste) to avoid mistyping the commands.

::

   cd $HOME
   tar -xf $HOME/Downloads/ams2021.101.pc64_linux.intelmpi.bin.tgz

Run the following command to **source the amsbashrc.sh file**, do not forget the dot and space at the beginning of the line! Also make sure to replace 2021.101 with the version you downloaded.

::

   . $HOME/ams2021.101/amsbashrc.sh

**Start up the GUI** with this command:

::

   amsjobs &

If this fails to launch a GUI window, then you can try to run our GUI in software mode:

::

   export SCM_OPENGL_SOFTWARE=1
   amsjobs &

If this still does not open a GUI, then use your mouse to select all the text in the terminal window, copy it (right-click and select copy), and send us an email at support@scm.com with the text. DO NOT PROCEED WITH THE NEXT STEP!

If the AMS GUI started without problems, go back to the terminal window and run the following command to **create a desktop icon** for AMS:

::

   $AMSBIN/create_linux_icon.sh


Finally we can set up our terminal to automatically source the amsbashrc.sh file when starting. **Add the source command to the .bashrc file** with the following command in the terminal window:

::

   echo '. $HOME/ams2021.101/amsbashrc.sh' >> $HOME/.bashrc

You can also open the .bashrc file in a text editor, and manually paste the part between the quotes on a new line at the end of the file.

