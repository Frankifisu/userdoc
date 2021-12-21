10 Ways to Get the Energy and Other Properties
***********************************************

Most AMS calculations produce several `output files <../../AMS/Input_Output.html#output>`__:

* the **standard output** (``jobname.out`` file)
* the **logfile** (``jobname.logfile``, or ``ams.log``)
* the **binary ams.rkf file** inside the ``jobname.results`` directory
* the **binary "engine.rkf" file** inside the ``jobname.results`` directory. The name of the file `depends on the calculation <../../AMS/Input_Output.html#binary-output-files>`__, and can be ``adf.rkf``, ``band.rkf``, ``dftb.rkf``, ``reaxff.rkf``, etc.

One important result from an AMS geometry optimization or single-point calculation is the **final potential energy**. AMS
will print this number in **hartree** to the standard output, logfile, and
engine.rkf file.

This tutorial shows you how to get this number with the

* :ref:`GUIWays` (:ref:`Output <OutputWay>`, :ref:`Logfile <LogfileWay>`, :ref:`KFbrowser <KFbrowserWay>`, :ref:`Spreadsheet (Excel) <SpreadsheetWay>`, :ref:`AMSjobs <AMSjobsWay>`) 
* :ref:`Command-line <CommandLineWays>` (:ref:`amsreport <amsreportWay>`, :ref:`dmpkf <dmpkfWay>`, :ref:`grep <grepOutputWay>`)
* :ref:`PythonWays` (:ref:`AMSJob <AMSJobWay>`, :ref:`KFReader <KFReaderWay>`)

Most of these tools can also be used to extract **many other properties**, such as atom coordinates, bond lengths, orbital energies, excitation energies, density of states, etc.

.. note::

   ADF and BAND give the energy with respect to fragments. The fragments are
   spherically symmetric nonspinpolarized atoms, by default. See also the `FAQ <https://www.scm.com/faq/adf-faq/#where-can-i-find-the-total-energy-in-the-output>`__.

This tutorial uses results from :ref:`GO_ETHANOL`.



.. _GUIWays:

Graphical User Interface
==============================

.. _OutputWay:

1. Standard output 
---------------------------------------------------------

* Select the job in AMSjobs (SCM → Jobs)

.. figure:: /Images/10WaysToGetTheEnergy/1_1.png
  :align: center

* SCM → Output

* Scroll down towards the end, or search for "CALCULATION RESULTS" with the search box at the bottom of the window. 

.. figure:: /Images/10WaysToGetTheEnergy/1_3.png
  :align: center

* Under "CALCULATION RESULTS" is a line with the energy.

.. _LogfileWay:

2. Logfile 
----------------------------------

* Select the job in AMSjobs (SCM → Jobs)
* SCM → Logfile
* Scroll down towards the end. Depending on the engine and task, the energy is sometimes printed as "Bond Energy", "ENERGY OF FORMATION", "current energy", etc.

.. figure:: /Images/10WaysToGetTheEnergy/2_1.png
  :align: center

.. _KFbrowserWay:

3. KF browser
----------------------------------------------------------

KF browser is a program for viewing the binary ams.rkf and engine.rkf files.

* Select the job in AMSjobs (SCM → Jobs)
* SCM → KF browser. This will show you the contents on the **ams.rkf** file.
* **File → Related files -> engine.rkf**

.. figure:: /Images/10WaysToGetTheEnergy/3_1.png
  :align: center

* AMS results, Energy

.. figure:: /Images/10WaysToGetTheEnergy/3_2.png
  :align: center

To start kfbrowser from the :ref:`command line <CommandLineWays>`, run ``$AMSBIN/kfbrowser engine.rkf``.

See also: `The difference between ams.rkf and engine.rkf  <../../AMS/Input_Output.html#binary-output-files>`__.

.. tip::

   If you select File → Expert Mode, you will see the raw structure of the binary file.



.. _SpreadsheetWay:

4. Spreadsheet (Excel) summary
----------------------------------------------------
* Select the job in AMSJobs (SCM → Jobs)
* **Tools → Build spreadsheet summary**

.. figure:: /Images/10WaysToGetTheEnergy/4_1.png
  :align: center

* Choose your preferred units

.. figure:: /Images/10WaysToGetTheEnergy/4_2.png
   :align: center

* Click "Do It"

This places a spreadsheet .xlsx file in the job.results folder and opens it in your default spreadsheet viewer. The energy is given under "Main results".

.. figure:: /Images/10WaysToGetTheEnergy/4_3.png
  :align: center

See also: `Documentation for spreadsheet export <../../GUI/Spreadsheets_xlsx.html>`__.


.. _AMSjobsWay:

5. AMSjobs
------------------------------------------

* Select the job in AMSJobs (SCM → Jobs)
* **Job → Edit Comments**
* In the Results dropdown menu choose **Energy**
* Click **Set as Default**
* Click **Save** 
* In the main AMSjobs window, select **View → Comments**.


.. _CommandLineWays:

Command-line (bash, terminal)
==============================

Start a terminal window as follows:

* `Windows <../../Scripting/GettingStarted.html#windows>`__: **Help → Command-line**, type ``bash`` and hit Enter.
* `MacOS <../../Scripting/GettingStarted.html#macos>`__: **Help → Terminal**.
* `Linux <../../Installation/Linux_Quickstart_Guide.html>`__ : Open a terminal and run: ``source /path/to/ams/amsbashrc.sh``

.. figure:: /Images/10WaysToGetTheEnergy/6_1.png
  :align: center

In the examples, replace ``/path/to/engine.rkf`` with the actual path to the file (the path can be absolute or relative).

.. _amsreportWay:

6. Command-line: amsreport
---------------------------

.. code::
   
   $AMSBIN/amsreport /path/to/engine.rkf energy

Some engines calculate the energy by summing up contributions. See the contributions with

.. code::

   $AMSBIN/amsreport /path/to/engine.rkf energies

You can also read key-value pairs from engine.rkf directly.  To find out which entry to read, first inspect the file with :ref:`kfbrowser <KFbrowserWay>` in **Expert Mode** (File → Expert Mode).

.. code::

   $AMSBIN/amsreport /path/to/engine.rkf "AMSResults%Energy" -r


``amsreport`` can also extract many other properties. See the `amsreport documentation <../../Scripting/Commandline_Tools/AMSreport.html>`__.


.. _dmpkfWay:

7. Command-line: dmpkf
--------------------------

.. code::

   $AMSBIN/dmpkf /path/to/engine.rkf "AMSResults%Energy"

.. _grepOutputWay:

8. Command-line: grep (not recommended)
-------------------------------------------

We do not recommend to ``grep`` the output file, as the output file format may change in future versions.

.. code::

   grep "^Energy (hartree)" jobname.out 


.. _PythonWays:

Python
======================

To run an example: 

* Save the contents into a file ``filename.py`` 

* Run it from the :ref:`command-line <CommandLineWays>` with: ``$AMSBIN/amspython filename.py``.

``amspython`` is the `python interpreter included with the Amsterdam Modeling Suite <../../Scripting/Python_Stack/Python_Stack.html>`__. It gives you access to the `PLAMS python library <../../plams/index.html>`__.

.. _AMSJobWay:

9. Python: Load an AMSJob
--------------------------

To get the final energy:

.. code:: python

   from scm.plams import *
   job = AMSJob.load_external('/path/to/jobname.results')
   energy = job.results.get_energy()
   print(energy)


To get all the energies from for example a geometry optimization:

.. code:: python

   from scm.plams import *
   job = AMSJob.load_external('/path/to/jobname.results')
   energies_list = job.results.get_history_property('Energy')
   print(energies_list)

PLAMS has many different functions for extracting results. See the `AMSResults API <../../plams/interfaces/ams.html#amsresults-api>`__.

.. _KFReaderWay:

10. Python: Direct access to .rkf file
---------------------------------------

To find out which entry to read from a binary file, first inspect the file with :ref:`kfbrowser <KFbrowserWay>` in **Expert Mode** (File → Expert Mode).

To get the final energy with `KFReader <../../plams/interfaces/kffiles.html#scm.plams.tools.kftools.KFReader>`__:

.. code:: python

   from scm.plams import *
   kf = KFReader('/path/to/jobname.results/engine.rkf')
   energy = kf.read('AMSResults', 'Energy')
   print(energy)


Alternatively, load an `AMSJob <../../plams/interfaces/ams.html#amsjob-api>`__ and call the ``readrkf`` method on its `results <../../plams/interfaces/ams.html#amsresults-api>`__:

.. code:: python

   from scm.plams import *
   job = AMSJob.load_external('/path/to/jobname.results')
   energy = job.results.readrkf('AMSResults', 'Energy', file='engine')
   print(energy)



