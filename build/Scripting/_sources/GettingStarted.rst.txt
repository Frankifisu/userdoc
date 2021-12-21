

Getting Started
===============


To conveniently use the scripting tools of the Amsterdam Modeling Suite you need to set some shell `environment variables <../Installation/Appendix_A_Environment_Variables.html>`__ and add the ``AMSBIN`` folder to your ``PATH``. This can be done by sourcing file ``amsbashrc.sh``, which is located in the Amsterdam Modeling Suite installation directory.

Linux
-----

Note: if you followed the `Linux Quickstart installation Guide <../Installation/Linux_Quickstart_Guide.html>`__, the ``amsbashrc.sh`` should be automatically sourced when you start up a new terminal, and you can ignore the following steps.

* Start up a terminal
* Source the ``amsbashrc.sh`` with the following command (note: you should replace ``path_to_installation_directory`` with the actual path to your AMS installation directory::
   
   . path_to_installation_directory/amsbashrc.sh

* To test that you properly sourced the ``amsbashrc.sh`` file you can type the following command, which should yeld the help message for the  :ref:`amsprep <AMSPREP>` command line tool::

   amsprep -h


MacOS
-----

* From the AMSjobs GUI module, click on the **Help** dropdown menu and select **Terminal**. This will open a new terminal with all necessary environment variables already set and the ``AMSBIN`` folder already added to the ``PATH``.

Alternatively, you can follow the Linux steps.


Windows
-------

Every Windows installation of AMS2019 and newer, as well as older ADF versions, come with a pre-configured command line.
The easiest way to access the command line is via the Help menu of the graphical user interface:

.. rst-class:: steps

  \
    | Go to **Help → Command-line**
    | Inside the command line window, type ``bash`` and hit ENTER (alternative: type ``sh``)

.. image:: Images/windows_scripting.png


The advantage of calling the command line from the GUI is that you will find yourself in the current working directory right away.
In situations in which the GUI is not available, it is also possible to use the pre-configured command line directly:

.. rst-class:: steps

  \
    | Double click the file ``ams_command_line.bat`` in your AMS installation directory (e.g. C:/AMS2021.101)



Notes on Python
---------------

Python scripts should be executed using the python3 interpreter shipped with Amsterdam Modeling Suite::

   $AMSBIN/amspython scriptname.py

Further information can be found here: :ref:`Python_Stack`.
