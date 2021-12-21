.. _plams_tutorial:

Python Scripting With PLAMS
###########################

`PLAMS <../../plams/index.html>`__ (Python Library for Automating Molecular Simulation) is a collection of tools that provide powerful, flexible, and easily extendable Python interfaces to molecular modeling programs.
The library takes care of input preparation, job execution, file management and output processing as well as helps with building more advanced data workflows.

.. seealso::

    * The `Examples section <../../plams/examples/examples.html>`__ of the PLAMS manual contains several examples PLAMS scripts.
    * The `Cookbook section <../../plams/examples/examples.html>`__ of the PLAMS manual contains some useful code snippets.

**Notes before starting the tutorial**

These tutorials assume some familiarity with: Python (version 3.6), Unix command-line shells (like bash) and the `ADF`_ engine and `AMS`_ driver program of the Amsterdam Modeling Suite. 

On **Windows** and **MacOS** computers all tutorials can conveniently be run within the pre-configured AMS command line:

+ `Windows command line <../../Scripting/GettingStarted.html#windows>`__  
+ `MacOS command line <../../Scripting/GettingStarted.html#macos>`__

**Linux** users should make sure that the Amsterdam Modeling Suite is installed and that the ``AMSBIN`` environment variable is correctly set (``AMSBIN`` should contain the path to the Amsterdam Modeling Suite bin directory). You can test this by typing ``$AMSBIN/plams -h`` in a terminal: this should print PLAMS' help message. If this is not the case (e.g. ``No such file or directory``), you need to set up the environmental variable ``$AMSBIN`` (see the `Linux Quickstart guide <../../Installation/Linux_Quickstart_Guide.html>`__ for details).

PLAMS is an open source library, but in order to run the tutorials' example scripts you will need a license for the computational engines `ADF`_ and `AMS`_. Contact license@scm.com for further questions.

.. _first_steps_with_plams:

First steps with PLAMS
**********************

We will start with the simple example of a water molecule geometry optimization using `ADF <https://www.scm.com/product/adf/>`_ as computational engine.
In this script we will show how to:

* create a ``Molecule``
* specify the input for ADF through the ``Settings`` object
* create and run the ``AMSJob``
* read from the calculation's ``Results``

This is the full PLAMS script, which we will then explain step by step in this tutorial:

.. literalinclude:: /downloads/PythonScriptingWithPLAMS/H2O_opti.py
   :language: python


Running a PLAMS script
----------------------

Create a working directory ``plams_tutorial``, move into it, and save the script :download:`H2O_opti.py </downloads/PythonScriptingWithPLAMS/H2O_opti.py>`. To execute the script with PLAMS, type in a terminal::

  $AMSBIN/plams H2O_opti.py

The calculation should take just a few seconds and you should obtain the following result::

  [12:06:21] PLAMS working folder: /home/username/plams_tutorial/plams_workdir
  [12:06:21] JOB water_GO STARTED
  [12:06:21] JOB water_GO RUNNING
  [12:06:23] JOB water_GO FINISHED
  [12:06:23] JOB water_GO SUCCESSFUL
  == Water optimization Results ==
  Bonding energy:  -323.06 kcal/mol
  Bond angle:       103.54 degree
  Optimized coordinates:
    Atoms:
      1         O      0.047189      0.047189      0.000000
      2         H      1.021233     -0.068422      0.000000
      3         H     -0.068422      1.021233      0.000000

  [12:06:23] PLAMS run finished. Goodbye


Every time you run a PLAMS script, a new working directory is created (by default it is called ``plams_workdir``).
This folder will contain one subdirectory per job (in our case, one folder named ``water_GO``). Each job folder contains the job's input and results files.


Molecule
--------

You can initialize a `Molecule <../../plams/components/molecule.html>`__ object by:

* creating an *empty* molecule and manually adding the atoms

  .. code-block:: python

    mol = Molecule()
    mol.add_atom(Atom(symbol='O', coords=(0,0,0)))
    mol.add_atom(Atom(symbol='H', coords=(1,0,0)))
    mol.add_atom(Atom(symbol='H', coords=(0,1,0)))

* importing the atomic coordinates from an external file (supported formats: ``xyz``, ``mol``, ``mol2``, and ``pdb``):

  .. code-block:: python

    mol = Molecule('molecules/H2O.xyz')

* using the ``rdkit`` interface to generate the geometry from a SMILES string:

  .. code-block:: python

    mol = from_smiles('O')



The Molecule class provides several methods for basic molecular manipulations, such as `rotate <../../plams/components/molecule.html#scm.plams.basemol.Molecule.rotate>`__, `translate <../../plams/components/molecule.html#scm.plams.basemol.Molecule.translate>`__.
Furthermore, the list of `Atoms <../../plams/components/molecule.html#atom>`__ contained in the corresponding Molecule object can be directly accessed and manipulated.
See the `Molecule section <../../plams/components/molecule.html#molecule>`__ of the PLAMS documentation for the complete list of methods.


Settings class
--------------

The Settings class extends the regular `Python dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`__ by many useful features.
In the following we show how the ``Settings`` object is used to define the input for an ``AMSJob``. The reader is strongly encouraged to consult the `Settings section <../../plams/components/settings.html#settings>`__ of the PLAMS documentation for a detailed explanation of the Settings class.

One important aspect of the PLAMS library is that *PLAMS knows (almost) nothing about the input options of the various computational engines*.
In other words, you need to know the structure of the text input file of the computational engine in order to set up the corresponding ``Settings`` object.
Although input files for the various computational engines (ADF, BAND, and DFTB) use different sets of keywords, they share a similar structure – they consist of *blocks* and *subblocks* which in turn contain *keys* and *values*.

To give an example, the ``Settings`` object in ``H2O_opti.py``

.. code-block:: python

  # Initialize the settings for the ADF calculation:
  sett = Settings()
  sett.input.ams.Task = 'GeometryOptimization'
  sett.input.adf.Basis.Type = 'DZP'
  sett.input.adf.XC.GGA = 'PBE'

will translate into the following input file when supplied to an ``AMSJob`` class

.. code-block:: none

  Task GeometryOptimization

  Engine adf
    Basis
      Type DZP
    End
    XC
      GGA PBE
    End
  EndEngine

With the exception of the atomic coordinates (these will be picked up from the Molecule object; see above) all desired input options must be specified in the Settings object.

See the `Amsterdam Modeling Suite section <../../plams/interfaces/amssuite.html#preparing-input>`__ of the PLAMS documentation for a comprehensive description of how the settings object is converted into an ASCII input file.

You can get the computational engine's input file via the job's `get_input() <../../plams/interfaces/ams.html#scm.plams.interfaces.adfsuite.ams.AMSJob.get_input>`__ method. For example:

.. code-block:: python

  job = AMSJob(molecule=mol, settings=sett, name='water_GO')
  print(job.get_input())


Creating and running the Job
----------------------------

The ``Job`` class is the most important object in PLAMS as it takes care of the preparing, executing and collecting the results of a Job.
For a detailed description of the Job class, see the `Jobs section <../../plams/components/jobs.html#jobs>`__ of the PLAMS documentation.

PLAMS ships several ready-to-use Job subclasses. The ``AMSJob`` subclass is used to run jobs via the AMS driver program. The base class Job can readily be extended to be interfaced with other computational engines.

Creating and running the ``AMSJob`` of our example is straightforward:

.. code-block:: python

  # Create and run the job:
  job = AMSJob(molecule=mol, settings=sett, name='water_GO')
  job.run()


Each job has its own subdirectory (with the same name as the job) in the working folder.

Results
-------

After the successful completion of a job, the results can be accessed via the ``Results`` object associated with the ``job``.

There are three ways of retrieving data from the job results:

* For the most common results like the final energy or optimized geometry there are dedicated methods like in the example above.

  .. code-block:: python

    energy = job.results.get_energy()
    opt_mol = job.results.get_main_molecule()


* For all other data the recommended approach is to read the binary results file (in KF format) by using `readrkf <../../plams/interfaces/ams.html#scm.plams.interfaces.adfsuite.ams.AMSResults.readrkf>`__.
  The readrkf method will access the appropriate binary file and returns the requested data in a python built-in type (int, float, bool, ...).
  If the requested data is an array, it returns a python list.

  .. code-block:: python

    # Fetch and print some results:
    energy = job.results.readrkf('Energy', 'Bond Energy', file='adf')

  The two arguments are the respective "Section" and "Variable" names in the binary KF result file.

  .. tip::

    You can check the content of a binary KF file with the `kfbrowser <../../ADF/Appendices/KF_browser.html>`__ tool. Make sure to switch kfbrowser to expert mode in order to see the real section and variable structure of the KF file.


  Most results in the binary KF file are provided in atomic units.
  The `Units <../../plams/components/utils.html#units>`__ utility can be used to convert the results into the desired units:

  .. code-block:: python

    energy_in_kcal_mol = Units.convert(energy_in_au, 'au', 'kcal/mol')


* You can also extract data from the **standard output** using the `grep_output <../../plams/components/results.html#scm.plams.core.results.Results.grep_output>`__ and `awk_output <../../plams/components/results.html#scm.plams.core.results.Results.awk_output>`__ methods.
  They will return a list of strings containing the matches of the grep or awk commands. Alternatively, you can use `get_output_chunk <../../plams/components/results.html#scm.plams.core.results.Results.get_output_chunk>`__ to extract a continuous part of the output between two lines.

You can get the optimized geometry into a Molecule object via the `get_main_molecule <../../plams/interfaces/ams.html#scm.plams.interfaces.adfsuite.ams.AMSResults.get_main_molecule>`__ method:

.. code-block:: python

  opt_mol = job.results.get_main_molecule()



.. External links:
.. _ADF: https://www.scm.com/product/adf/
.. _AMS: https://www.scm.com/product/ams/
