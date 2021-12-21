Run Jobs from the Command Line 
***********************************************

.. important::

   This tutorial explains how to run AMS calculations from the command line.
   This is sometimes convenient, but usually not necessary. You can always set up
   calculations using the :ref:`graphical user interface <GO_ETHANOL>` (GUI) instead.

.. contents::
   :local: 
   :depth: 1

An example shell script
===============================

If you followed the :ref:`GO_ETHANOL` or :ref:`EXCITATION_ETHENE` tutorial, you
will have created a file called ``jobname.run``, that contains something
similar to this:

.. code::

   #!/bin/sh
   
   "$AMSBIN/ams" << eor
   
   Task GeometryOptimization
   System
       Atoms
           C 0.01247 0.02254 1.08262 
           C -0.00894 -0.01624 -0.43421 
           H -0.49334 0.93505 1.44716 
           H 1.05522 0.04512 1.44808 
           H -0.64695 -1.12346 2.54219 
           H 0.50112 -0.9164 -0.8044 
           H 0.49999 0.86726 -0.8448099999999999 
           H -1.0431 -0.02739 -0.80544 
           O -0.66442 -1.15471 1.56909 
       End
   End
   
   Engine ADF
       Basis
           Type SZ
       End
   EndEngine
   eor


This file is a **shell script**. With a shell script, you can run an AMS
calculation without the graphical user interface (GUI). Such a shell script is
also called a **run script** or a **run file**. You will still be able to
visualize the results with the GUI.


.. _cmdline_tutorial_run:

Run the job
==========================

.. note::

   This tutorial assumes that you have basic familiarity with a command-line,
   for example that you are familiar with the ``cd`` and ``ls`` commands.

.. rst-class:: steps

  \
    | Create a new **empty** directory 
    | Save the above script with the filename ``jobname.run`` in the new directory

To run the job, you first need to open up a terminal or command-line.

* `Windows <../../Scripting/GettingStarted.html#windows>`__: **Help → Command-line**, type ``bash`` and hit Enter.
* `MacOS <../../Scripting/GettingStarted.html#macos>`__: **Help → Terminal**.
* `Linux <../../Installation/Linux_Quickstart_Guide.html>`__ : Open a terminal and run: ``source /path/to/ams/amsbashrc.sh``

.. figure:: /Images/10WaysToGetTheEnergy/6_1.png
  :align: center

.. rst-class:: steps

  \
   | In the terminal, go to the directory containing the ``jobname.run`` file (and no other file)
   | Run the job with this command: ``sh jobname.run > jobname.out``
   | After the job has finished, list all files with ``ls -R``

The following should appear:

* the original ``jobname.run`` file

* the ``jobname.out`` file containing the **standard output** from ams

* the ``ams.results`` directory, containing the **logfile** ``ams.log``, the **optimized geometry in xyz format** ``output.xyz``, the **binary output files** ``ams.rkf`` and ``adf.rkf``, as well as a few more files.

Visualize the results in the GUI
---------------------------------

GUI modules can also be started from the command line. For example, to open the geometry optimization trajectory in AMSmovie, run

.. code::

   $AMSBIN/amsmovie ams.results

.. figure:: /Images/RunJobsFromTheCommandLine/2.png
  :align: center


Meaning of the run command
=================================

The command ``sh jobname.run > jobname.out`` executes the ``jobname.run`` file via the ``sh`` shell interpreter, and places the output in a file called ``jobname.out``.

Customize the run command
-------------------------------

.. note::

   Before running the job again, you must remove the ``ams.results`` directory. ``ams`` will never overwrite results if they already exist. 

* To view the output on the screen, as well as save it to a file, instead run ``sh jobname.run | tee jobname.out``

* You can also make the jobname.run file executable, if you prefer:

.. code::

   chmod +x jobname.run
   ./jobname.run > jobname.out


Meaning of the shell script contents
=======================================

#!/bin/sh
------------

This line indicates how the file should be executed. In this case, it means to
use the ``sh`` shell interpreter. If you run the file using 

* ``sh jobname.run > jobname.out``, this line is optional, but using

* ``./jobname.run > jobname.out``, it is required.

"$AMSBIN/ams" << eor
------------------------

This line executes the ``ams`` program. ``AMSBIN`` is an `environment
variable <../../Installation/Appendix_A_Environment_Variables.html>`__, and points to the directory containing the ``ams`` file.
When you :ref:`open a terminal following these instructions <cmdline_tutorial_run>`,
the ``AMSBIN`` variable will be set to the correct value.

.. rst-class:: steps

  \
   | Check what ``AMSBIN`` contains with this command: ``echo $AMSBIN``


``<< eor`` means that all the following lines, until there is a line exactly
equal to ``eor``, will be used as input for ``ams``. The input to ``ams`` thus becomes

.. _runscript_input_to_ams:

.. code::

   Task GeometryOptimization
   System
       Atoms
           C 0.01247 0.02254 1.08262
           C -0.00894 -0.01624 -0.43421
           H -0.49334 0.93505 1.44716
           H 1.05522 0.04512 1.44808
           H -0.64695 -1.12346 2.54219
           H 0.50112 -0.9164 -0.8044
           H 0.49999 0.86726 -0.8448099999999999
           H -1.0431 -0.02739 -0.80544
           O -0.66442 -1.15471 1.56909
       End
   End
   
   Engine ADF
       Basis
           Type SZ
       End
   EndEngine


Task and System block
----------------------------

When ``ams`` reads the ``Task GeometryOptimization`` line, it knows to perform a geometry optimization.

Similarly, the ``System`` block tells ``ams`` for which molecule to run the
calculation. Each line contains an atomic element and the atomic coordinates in
angstrom.

Technically, the ``Task`` and ``System`` block are input options to the `AMS
Driver <../../AMS/Input_Output.html>`__.  All allowed keywords are described in
the `AMS Driver manual <../../AMS/index.html>`__.

Engine ADF block
-----------------------

The lines between ``Engine ADF`` and ``EndEngine`` are passed on to the
`ADF engine <../../ADF/index.html>`__. In this case, the ``Basis`` block is used
to specify a single-ζ (SZ) basis set.

All keywords within the ``Engine ADF`` block are described in the `ADF manual <../../ADF/index.html>`__.

.. seealso::

   More information about the `AMS Driver <../../AMS/index.html>`__ and `Engines <../../AMS/Engines.html>`__.



Customize the shell script
====================================

Set the job name
-----------------------

``ams`` will place all its output files in a **results directory**. By default, this directory is called ``ams.results``. You can change it by replacing the ``"$AMSBIN/ams" << eor`` line with:

.. code::

   AMS_JOBNAME=my_jobname "$AMSBIN/ams" << eor

This will create the directory ``my_jobname.results`` instead.

Overwrite old results
----------------------------

If you want to overwrite the results if they already exist, add the ``--delete-old-results`` flag:

.. code::

   "$AMSBIN/ams" --delete-old-results << eor
       # ams input
   eor

Run in serial/parallel
-----------------------------

To set the number of processes used by ``ams``, specify the ``-n`` flag. To run in serial (using only 1 core):

.. code::

   "$AMSBIN/ams" -n 1 << eor
       # ams input
   eor

Alternatively, you can set the `environment variable <../../Installation/Appendix_A_Environment_Variables.html>`__ ``NSCM``:

.. code::

   export NSCM=1
   "$AMSBIN/ams" << eor
       # ams input
   eor

.. note::

   If you run ``ams`` on a batch system (compute cluster), it will automatically use the right number of cores.

Place the input to ams in its own file
------------------------------------------

Save the :ref:`input to ams <runscript_input_to_ams>` (all lines starting from ``Task`` to ``EndEngine``) in its own file ``jobname.in``.

Then the run script ``jobname.run`` can be simplified to become:

.. code:: 

   #!/bin/sh

   "$AMSBIN/ams" < jobname.in > jobname.out

Because this script is now really only 1 line, you could also run this command directly in the terminal: ``"$AMSBIN/ams" < jobname.in > jobname.out``


Specify a .xyz file for the geometry
-------------------------------------

When editing shell scripts manually, it is often more convenient to read the
atomic coordinates from an external file. You can read the coordinates from
``.xyz`` files, for example, the ``output.xyz`` file from a previous
calculation.  You can also create or open the structure in AMSinput GUI and
choose File → Export coordinates → xyz.

Then, in your shell script change the System block to become:

.. code::

   System
       GeometryFile my_xyz_file.xyz
   End


Tips for creating the input
================================

AMSinput is a very convenient tool for creating .run files. 

Whenever you use AMSinput, make a habit of checking the .run file before
running the job. You can also preview it, or even edit it, before saving, by
selecting **Details → Run Script**.

.. warning::

   On the **Details → Run Script** panel, clicking inside the text area will
   disable the "auto-update". Any other changes you make in AMSinput will then
   **not be added to the run file**! Check that "Auto update" is enabled,
   unless you manually want to edit the run script.

The run script lets you at a glance see if all the input options that you
(think you) have specified are actually present in the input to the job.
Inspecting the run script can help you to prevent mistakes.
