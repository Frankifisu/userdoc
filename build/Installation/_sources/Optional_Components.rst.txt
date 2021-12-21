******************************
Installing Optional Components
******************************

This guide describes how to install optional components of the Amsterdam Modeling Suite.
To reduce the initial download size, the Amsterdam Modeling Suite does not include all components by default. 
This includes features such as 

- the `Ligand Field DFT atomic database <../ADF/Input/LFDFT.html>`__
- the `COSMO-RS compound Database <../COSMO-RS/COSMO-RS_Databases.html>`__
- `Quantum ESPRESSO <../GUI/Set_up.html#quantum-espresso>`__
- `Machine Learning potential engines <../MLPotential/general.html>`__

If the appropriate license is present these modules can be installed though the GUI, or the command-line.
The easiest way requires an active internet connection, but it is also possible to to use a local copy of our repository downloaded ahead of time. 
These instructions assume that you have already successfully `installed AMS <./Installation.html>`__.

Introducing AMSpackages
#######################

Starting with AMS2021.1, several optional components will be provided through a unified program called AMSpackages.
AMSpackages helps you maintain the installation of optional components of the Amsterdam Modeling Suite. 
Features installed through AMSpackages integrate with both the GUI as well as command line programs,
and can be managed through either as well.
Users will be able to download and install packages, without the need for a password or writing permissions to the 
main installation directory of AMS.
All that is required is a valid license.

Users of the graphical interface will be prompted with a suggestion to install them when components are selected in AMSinput.
Alternatively, the package manager can be opened using SCM -> Packages to install components ahead of time, and to update or remove installed components.  
You can find more usage instructions at the `AMSpackages GUI <../GUI/AMSpackages.html>`__ section of the documentation. 

Managing packages from the command line
#######################################

On the command line, users can use :code:`"${AMSBIN}/amspackages"` to access the package manager interface. 
There are several subcommands that can be used to access several features such as installing, updating, or removing packages.
Below the most commonly used options are explained.
To see a full list of options you can use :code:`"${AMSBIN}/amspackages" --help`. 
Options marked as "Experts only" typically should not be used.
Any of the subcommands may also have specific options, which can be seen when using :code:`--help` behind the subcommand.
For instance, for :code:`"${AMSBIN}/amspackages" install --help`.

Finding available packages
--------------------------

The :code:`display` command will show available packages.

.. code-block:: sh
    
    "${AMSBIN}/amspackages" display | less -R

If you wish to refer to a package, you can use the :code:`ID` to install, remove it, or check if it is installed.
By default, display provides a long list of packages, but a wide view is also available.
For example::

  > "${AMSBIN}/amspackages" display --format wide
  AMSpackages Overview
  Date: Tue May 11 12:07:01 2021
  Repository: https://downloads.scm.com/Downloads/packages/
  Package directory: /home/user/.scm/packages/AMS2021.1.packages
  Name                                                [id]|     Instl. Version     |   Disk usage   |     Avail. Version     | Licensed? | Req. licenses
  ========================================================|========================|================|========================|===========|================
  ADFCRS-2018 Database                            [adfcrs]|                        |                |     2018: build 1      |    YES    | CRS 2021.1
  LFDFT atomic database                            [lfdft]|      1.0: build 0      |    1.42 GiB    |      1.0: build 0      |    YES    | ADF 2021.1
  All ML Potential backends                 [mlpotentials]|                        |                |     1.0.0: build 0     |    YES    | MLPOT 2021.1
  PiNN ML backend                                   [pinn]|                        |                |     0.3.1: build 0     |    YES    | MLPOT 2021.1
  Quantum ESPRESSO                                    [qe]|                        |                |      6.3: build 1      |    YES    | 
  SchNetPack ML backend                       [schnetpack]|                        |                |     0.3.1: build 0     |    YES    | MLPOT 2021.1
  sGDML ML backend                                 [sgdml]|                        |                |     0.4.4: build 0     |    YES    | MLPOT 2021.1
  TorchANI ML backend                           [torchani]|                        |                |     2.2.0: build 0     |    YES    | MLPOT 2021.1
   

.. _install-cmd:

Installing a package
--------------------

To install a package, use the :code:`install` command and specify the ID of the package. 

.. code-block:: sh
    
    "${AMSBIN}/amspackages" install lfdft

If you wish to install all available packages, `all` can be used as a shortcut.

.. code-block:: sh
    
    "${AMSBIN}/amspackages" install all

Some packages such as the Machine Learning potentials are installed into your `amspython environment <../Scripting/Python_Stack/Python_Stack.html#python-virtual-environment>`__.
Others are installed into a default directory.

- for Linux users this typically is :code:`$HOME/.scm/packages`
- for MacOS users :code:`$HOME/Library/Application Support/SCM/packages`
- for Windows users: :code:`%LOCALAPPDATA%/SCM/packages`


Check if a package is installed
-------------------------------

If you want to make sure that a package is installed, you can use the :code:`check` command. 

.. code-block:: sh
    
    "${AMSBIN}/amspackages" check lfdft

The exit status will be 0 if a package is installed, and non-zero otherwise.
For detailed information, you can pass the verbose (:code:`-v`) flag. This will tell you what version is installed. 

.. code-block:: sh
    
   > amspackages -v check lfdft
   04-20 17:26:28 lfdft is installed: Ligand Field DFT v[1.0] - build:0 [974661607e9f46c78b6d875e12edfb7a]

.. _remove-cmd:

Removing a package
------------------

Sometimes, you may wish to remove a package.
Removing a package is done by using the :code:`remove` command. 
This command can take a list of packages as arguments. 
For example, to remove the Ligand Field DFT package use:

.. code-block:: sh

    "${AMSBIN}/amspackages" remove lfdft

While we advise against it, there may be times when a user has accidentally or intentionally made changes or saved new files inside the directories
of one of the packages.
When trying to remove such a package, to prevent data loss you will be warned that a package is modified. 
In order to remove packages despite modifications, use the :code:`--force` flag.

.. code-block:: sh

    "${AMSBIN}/amspackages" remove --force lfdft


Updating a package
------------------

At times a newer version or build of a package may be available.
To install an update, use the :code:`update` command. 

.. code-block:: sh

    "${AMSBIN}/amspackages" update lfdft

.. note::

  The update mechanism usually removes user modifications.
  Therefore just like the remove command, you will have to specify the :code:`--force` flag to update such packages.

Reinstalling packages from a previous version of AMS
----------------------------------------------------

.. versionadded:: AMS2022.101
    
    Compatible components from a previous installation of AMS can be copied over, so redownloading and reinstalling is not necessary for some packages.

The ``copy`` command can be used to reuse packages from your previous installation by copying them to the new installation directory.
You can either use the package ID of packages you wish to copy over, or simply type ``all`` and the package manager will copy all compatible packages.
Not all packages will be compatible by default, and the exact list of compatible packages will depend on the version of AMS.
Python packages such as the ML potentials are not compatible with the copy functionality, so they will need to be reinstalled using the :ref:`install <install-cmd>` command.

.. code-block:: none

    $ "${AMSBIN}/amspackages" copy all
    Going to copy packages:  
    Quantum ESPRESSO v[6.3] - build:1
    ADFCRS-2018 Database v[2018] - build:1
    LFDFT atomic database v[1.0] - build:0
    Proceed with copying packages? [y/N
    copied: 100%|##########| 3/3 [00:09<00:00,  3.27s/pkg]

.. rubric:: Please note

AMSpackages will not delete the contents of the previous installation.
If you wish to remove packages from the old installation, please use the :ref:`remove <remove-cmd>` command within the old installation.

.. _local-copy:

Using the package manager offline
#################################

In some cases, it may be difficult to directly download packages on the system where one wishes to install them.
It is possible to instead use a local copy of the package repository downloaded on a different machine.
Below you will find instructions to generate a copy of our repository.

You can find a listing of the repository contents at 

.. code-block:: sh

  https://downloads.scm.com/Downloads/packages/listings/


Be sure to use the listing that matches your version of AMS, or you may have unexpected issues with installed packages.
You will need to download these files and preserve their directory structure. 

.. warning:: 

    Never install packages from an untrusted source. Only use a copy directly downloaded from our website.

MacOS and Linux
---------------

Method 1: wget
^^^^^^^^^^^^^^

.. note::

  On MacOS, you will need to install wget first. You can use `brew <https://brew.sh/>`__, or `macports <https://www.macports.org>`__ to install it. 

On Unix systems, wget can be used to achieve this from the command line.
To download the repository for AMS2021.1 you would use the following from the command line:

.. code-block:: sh
   
    wget --user scmuser --password scmpasswd -xi https://downloads.scm.com/Downloads/packages/listings/AMS2021.1.txt

This will create the ``downloads.scm.com`` folder in your current working directory, containing just the path to the repository.

Method 2: python
^^^^^^^^^^^^^^^^

You can download the following :download:`python script <./download/download_repository.py>` to download a copy of the repository.
If you have a local installation of AMS, then you can run it with amspython.
The script can resume after interuption, and update files that have changed in size.

It uses the following command line options

.. code-block:: none
    
    usage: download_repository.py [-h] [--strict-authentication] [--no-ssl] LISTING_URL DOWNLOAD_FOLDER USER PASSWORD

    positional arguments:
    LISTING_URL           Url pointing to the file listings for the repository.
    DOWNLOAD_FOLDER       A local directory for storing your download.
    USER                  Username for downloading from the website.
    PASSWORD              Password for downloading from the website.

    optional arguments:
    -h, --help            show this help message and exit
    --strict-authentication
                            If supplied this script will exit on 401 errors. By
                            default, this script will skip files on 401 errors.
    --no-ssl              Don't use SSL verification.

    All positional arguments are REQUIRED.

For example, you can run it as

.. code-block:: sh

  amspython download_repository.py https://downloads.scm.com/Downloads/packages/listings/AMS2021.1.txt ~/Downloads/my/repo scmuser scmpassword

If you want to use your own version of python, you need to install tqdm, and requests.
Note that the script requires python 3.6 or greater. 

.. code-block:: sh

  python -m pip install tqdm requests
  python download_repository.py --help


Windows
-------

For Windows users, we provide this :download:`powershell script <./download/download_repository.ps1>`.

Download this script, along with the listing file. 
You can right-click the script file in the file browser and select ``Run with Powershell`` to start it.

It will open a blue window displaying the progress, as well as some interactive prompts that will require you to 
provide the listing file, the location to store the download, and your SCM user account and password.

.. warning:: 

   Don't close the blue powershell window while the program is running.

The script will automatically start downloading the files to the folder of your choosing.
It may take a while to download all the files.
When it is done, the blue window will display a message saying that it is safe to close.

.. note::

    Your computer may not allow you to run powershell scripts by default. 
    If you receive a warning about not being allowed to run scripts, first open a open a ``powershell`` window using ``win + R`` on your keyboard, and typing powershell.
    In the powershell window that opens type ``powershell -ep Bypass C:\Path\To\Script``. Fill in the correct path to the script you downloaded.
    
Below, you can see a demonstration of how you can download and use the local copy on Windows.

.. raw:: html

    <center>
      <video width="480" height="320" muted="true" controls src="https://downloads.scm.com/distr/package_manager_offline.mp4"></video>
    </center>

You will need an internet connection to see the video.

Using the downloaded copy
-------------------------

On the command line you can point the package manager to the downloaded repository as follows

.. code-block:: sh

    amspackages --repository "/full/path/to/Downloads/packages/AMS2021.1.yml" display 

Or, you can set the :code:`SCM_AMSPKGS_REPO` environment variable in your shell, or in the :ref:`configuration file <persistent-configuration>`.

This will allow other programs that use the package manager to use the same repository for checking and installing packages.

In your shell (e.g. in `.bashrc`):

.. code-block:: sh

    export SCM_AMSPKGS_REPO="/full/path/to/Downloads/packages/AMS2021.1.yml"
    
In the configuration file:

.. code-block:: yaml
    
    SCM_AMSPKGS_REPO: /full/path/to/Downloads/packages/AMS2021.1.yml


Instructions for administrators
###############################

It is typical for several users to access and use the same installation of AMS. 
On shared systems, such as a compute cluster, it may therefore be desirable to share installed optional components. 
This will prevent redundant installations of the same feature.
If you are an administrator of such a shared installation, you may use the --admin flag to indicate that you wish to 
provide a shared package. For instance to install a shared package, use 

.. code-block:: sh
    
    "${AMSBIN}/amspackages" --admin install lfdft

Instead of in the user directory, packages will be installed in a shared path.
Users will not be able to modify shared packages themselves unless they have write permissions to the shared installation directory.

.. note::

    Shared installations can not be used for the Machine Learning potential engines, because these are installed inside the user's python environment.
    
Default paths for the shared installation are operating system dependent, and can be configured to point elsewhere.

- for linux users this typically is :code:`/opt/SCM/packages`
- for MacOS users :code:`/Library/Application Support/SCM/packages`
- for Windows users: :code:`C:\ProgramData\SCM\packages`

AMSpackages supports a set of environment variables that can be set to override default options. 
These paths can be overridden using the ``SCM_AMSPKGS_SHAREDDIR`` environment variable. 
You should add this to the persistent configurations, so that users can find the installation path that you used for 
installing.


.. _persistent-configuration:

Persistent configurations
#########################

.. sidebar:: Configuration file
  :subtitle: YAML syntax
   
  The configuration file uses YAML syntax. Environment variables can be specified using the variable name, followed by :code:`:`, a space, and then the value. 

The ``amspackages`` command has a lot of different options that users or admins may need to change to suit their particular system.
The full list of configuration options can always be seen when running ``${AMSBIN}/amspackages --help``.

The usage text contains the name of the environment variables that AMSpackages looks for between ``[]`` brackets.
A user can export these in their shell environment, or an administrator can add them to the configuration file to make them persistent throughout the usage of the package manager.
These options will also affect the operation of the package manager gui.
The configuration file will make settings persistent for all users of the installation of AMS.
The file is located inside AMSBIN, under

.. code-block:: sh
   
   "${AMSBIN}/amspackageslib/config.yml"

You can open this file in a plain text editor to make changes.
Inside you can find several variables that are set by default.
Please take care not to accidentally remove the pre-existing variables, as they are necessary for the package manager to function.
You can add your own variables to the file, and edit variables such as the repository, for instance to use a :ref:`local copy <local-copy>`.

Some example variables you may wish to set

.. code-block:: yaml
    
    SCM_AMSPKGS_REPO: /downloads/SCM/packages/AMS2021.1.yml # A local copy of the package repository
    SCM_AMSPKGS_SHAREDDIR: /shared/SCM/packages/ # Admin provided packages will be installed here
    SCM_AMSPKGS_USERDIR: ~/.scm/packages # User packages will be installed here.

Note that using variables (for example ``$HOME``) inside the names of paths is not supported, but you can use a ``~`` as a shortcut for home in path names.
If you require a different configuration per user, it is recommended to set an environment variable inside the user environment instead of using the configuration file.


F.A.Q. & Troubleshooting
########################

.. note::

    If you face problems with the package manager, please include the log file in your support ticket. 
    The log file is called "amspackages.log" and is located under

    - for Linux :code:`$HOME/.scm/packages/amspackages.log`
    - for MacOS users :code:`$HOME/Library/Application Support/SCM/packages/amspackages.log`
    - for Windows users: :code:`%LOCALAPPDATA%/SCM/packages/amspackages.log`


Where are packages are installed ?   
----------------------------------

AMSpackages uses the following default locations for the installation of packages:

- Linux: ``$HOME/.scm/packages``
- MacOS: ``$HOME/Library/Application Support/SCM/packages``
- Windows: ``%LOCALAPPDATA%/SCM/packages``

Every version of AMS has its own dedicated folder inside the ``packages`` directory, to allow different installations
to appear side-by-side.
Packages themselves will be located in a uniquely named subdirectory. 
It is typically not recommended to make manual changes to installed packages. 
If you do need to know the location of a specific package, the ``loc`` command on the command line can help you find them.

.. code:: sh

    $ amspackages loc lfdft
    /home/user/.scm/packages/AMS2021.1.packages/kfh27hvj/content

The default location can be changed using the ``SCM_AMSPKGS_USERDIR`` environment variable. 


The package manager exits saying "Unhandled exception..."
---------------------------------------------------------

It appears that the package manager has run into an unexpected error. 
More information about the error will be in the log file, see also the top of this F.A.Q.

To see more information, the command line version of AMSPackages has a ``--verbose`` option. 
Using this flag twice will result in large amounts of debug information (short-cut ``-vv``), 
which may include more information about the error.

Some errors may disappear after running ``amspackages clean`` on the command line. 

If these errors persist, please contact SCM support and include the log file.


I want to use my own version of package 'X'
-------------------------------------------

There is usually an environment variable that the user can set that points towards their own
version of the package.
Please check out the documentation of the specific package for instructions.


COSMO-RS Database 2018
^^^^^^^^^^^^^^^^^^^^^^

You can point the environment variable ``SCM_ADFCRSDIR`` to the location of the ``ADFCRS-2018`` folder.
Please see the `COSMO-RS Database Tutorial <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html>`__ for details.


QuantumESPRESSO
^^^^^^^^^^^^^^^

Please consult the `Quantum ESPRESSO GUI documentation <../GUI/Set_up.html#quantum-espresso>`__ for details.


Machine Learning potentials
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For python packages such as the ML potential backends, you can use pip to install alternate versions.
See the `ML potential documentation <../MLPotential/general.html>`__ for details.


I am having trouble downloading packages
----------------------------------------

If you have an unstable or slow connection, you can try to download a copy of our repository elsewhere and use that.
You can find instructions :ref:`here <local-copy>`.

Alternatively, you can `follow the instructions <./Optional_Components.html#i-want-to-use-my-own-version-of-package-x>`__ for using your own version of a package.


My problem isn't listed here
----------------------------

You can find more information about getting support for your problem on our `support page <https://www.scm.com/support/>`__.




