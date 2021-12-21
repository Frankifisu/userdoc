.. _Python_Stack: 


Python Stack in Amsterdam Modeling Suite
****************************************

General
=================================

The Amsterdam Modeling Suite includes a python stack based on the `Enthought Python Distribution <https://www.enthought.com/products/epd/>`_.
In the AMS2020 release, the python version is 3.6.9.

This python stack is completely separate from any other python installations on the system.

All programs within the Amsterdam Modeling Suite launch python via a special command, ``amspython``.
In previous versions of the Amsterdam Modeling Suite, the command was called ``startpython``, but starting with AMS2020, the python launcher is called ``amspython``.

Included modules
================================

Some of the included modules are:

+ numpy (1.11.3) and scipy (0.18.1): Big modules with a lot of functionality for math and science, more information on the `SciPy website <https://www.scipy.org/>`_.

+ ipython4 (5.1.0): An improved interactive python shell, more information can be found on the `iPython website <https://ipython.org/>`_. Can be started with::

   $AMSBIN/amsipython

+ ase (3.19.0): ASE (Atomic Simulation Environment) is a python module for atomistic simulations, more information in the :ref:`ASE documentation <ASE>`.

+ matplotlib (1.5.1): A library for plotting data in 2D, more information on the Matplotlib `website <https://matplotlib.org/>`_. We do not ship an interactive backend for matplotlib, so make sure to set a `non-interactive backend <https://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear>`_ when using it. For example the Agg backend for PNGs::

   import matplotlib
   matplotlib.use('Agg')

+ pip (20.0.2): The recommended tool for installing packages from the Python Package Index (PyPI). The `pip documentation <https://pip.pypa.io/en/stable/>`_ explains in detail how to use this tool, but for the Python stack shipped with the Amsterdam Modeling Suite all **pip** commands need to be prefixed with **$AMSBIN/amspython -m**::

   $AMSBIN/amspython -m pip list
   $AMSBIN/amspython -m pip show scipy
   $AMSBIN/amspython -m pip search rotate-backups
   $AMSBIN/amspython -m pip install rotate-backups

+ flexmd: A module for running MD simulations with adaptive QM/MM regions. Details can be found in the :ref:`FlexMD documentation <FlexMD>`. 

+ plams: PLAMS (Python Library for Automating Molecular Simulation) is a collection of tools that aim at providing powerful, flexible and easily extendable Python interface to molecular modeling programs. It takes care of input preparation, job execution, file management and output processing as well as helps with building more advanced data workflows. See the `PLAMS tutorials <../../Tutorials/WorkflowsAndAutomation/PythonScriptingWithPLAMS.html>`_ and `PLAMS documentation <../../plams/index.html>`_ for more information.

+ autografs: AuToGraFS stands for Automatic Topological Generator for Framework Structures. Information and examples can be found in the :ref:`AuToGraFS documentation <AuToGraFS>`.

Using other modules with the AMS Python Stack
=============================================

You can extend the the AMS Python Stack with other modules. You can use **pip** (see above) to install additional modules if they are available on the Python Package Index (`PyPI <https://pypi.python.org/pypi>`_). This is the recommended way of installing packages::

   $AMSBIN/amspython -m pip install name_of_package

You can also do this for your own packages that you develop, for example::

   $AMSBIN/amspython -m pip install -e .

Alternatively, you can add the location of the source to the ``SCM_PYTHONPATH`` variable to make the module available in the AMS Python Stack. To avoid collisions with other python installations on the system, we unload ``PYTHONPATH`` and ``PYTHONHOME`` from the environment when launching the ADF Python Stack and put the content of ``SCM_PYTHONPATH`` into ``PYTHONPATH``.

.. hint:: If you for some reason have to use the PYTHONPATH variable and are unable to use SCM_PYTHONPATH, you can modify $AMSBIN/amspython and $AMSBIN/amsipython to not have it cleared when starting python.


Python virtual environment
=================================

Default python virtual environment
-----------------------------------------
Starting with AMS2020, the ``amspython`` command by default checks for a python virtual environment inside the user's home directory. If it does not find a virtual environment, it will create one in the following location (these are the default values for the ``SCM_PYTHONDIR`` environment variable):

+ Windows: ``$USERPROFILE/.scm/python``

+ Mac: ``$HOME/Library/Application Support/SCM/python``

+ Linux: ``$HOME/.scm/python``

``amspython`` then launches the python binary located inside the virtual environment.

If you install additional packages via pip (see above), they will be installed into the virtual
environment's ``site-packages``.


Virtual environments for different AMS versions
----------------------------------------------------
The virtual environment is tied to the major release version of AMS, which is
reflected in the name of the virtual environment directory (e.g.
AMS2020.1.venv).

Thus, upgrading from AMS2020.101 to AMS2020.102 will automatically let you use
all python packages that you installed into the AMS2020.101 virtual
environment.

To use previously installed python packages when upgrading from AMS2020.101 to
e.g. AMS2020.301 or AMS2021.101, simply copy or rename AMS2020.1.venv to
AMS2020.3.venv or AMS2021.1.venv in the same directory.

If you have several installations of different major releases of the Amsterdam
Modeling Suite on the same computer, multiple virtual environments will also be
created, one for each installation.



Changing the location of the python virtual environment
--------------------------------------------------------

Set the ``SCM_PYTHONDIR`` environment variable to a directory in which the
virtual environment will be installed. If you use the graphical user interface
(GUI), this environment variable can be changed in the GUI preferences. If you
use the command line, set it in your ``amsbashrc.sh``.  If you use both the GUI
and the command line, you should change it in both places.

Disabling the virtual environment
------------------------------------
Follow the steps for changing the location of the python virtual environment, but set ``SCM_PYTHONDIR`` to be empty.

Uninstalling the virtual environment
-------------------------------------
Just delete the directory containing the virtual environment. This will also delete any packages that you have installed into it.

Reinstalling the virtual environment
------------------------------------
To force a reinstallation of the virtual environment, even if it already
exists, run ``$AMSBIN/amspython --install_venv``. This will not remove any
packages inside the virtual environment.

Useful commands
=================================

+ Start a python shell::

   $AMSBIN/amspython

+ Install new packages via pip::

   $AMSBIN/amspython -m pip install name_of_package

+ Find out the location of an installed package (e.g. numpy)::

   $AMSBIN/amspython -c 'import numpy; print(numpy.__file__)'

+ Find out which python binary is launched by amspython::

   $AMSBIN/amspython -c 'import sys; print(sys.executable)'

+ Disable the virtual environment (one-time)::

   SCM_PYTHONDIR='' $AMSBIN/amspython



