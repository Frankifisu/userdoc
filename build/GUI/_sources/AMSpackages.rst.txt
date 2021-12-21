###########
AMSpackages
###########

General
*******

AMSpackages is a GUI module that can be used to install optional software components.
Users of the graphical user interface will automatically be prompted to install an optional component when the option is selected in AMSInput.
Alternatively they can use SCMMenu **→** Packages to install packages at any time.
The graphical interface can also be started using :code:`"${AMSBIN}/AMSpackages" gui` on the command line. 


.. figure:: images/amspackages_gui1.png
  :width: 80%
  :align: center

  The main window of the AMSpackages gui.

Command line features of AMSpackages are documented in the `installation <../Installation/Optional_Components.html>`__ 
chapter of the manual.


Installing packages
-------------------

Select the packages that you wish to install and click install.
Some information will be printed to the screen regarding progress. 

If you wish to abort an operation, you can click the abort button.


Removing packages
-----------------

Select the packages that you wish to remove and click remove.


Reinstalling packages from a previous version of AMS
----------------------------------------------------

.. versionadded:: AMS2022.101
    
    Compatible components from a previous installation of AMS can be copied over, so redownloading and reinstalling is not necessary for some packages.

If compatible packages are detected, you will see the *reuse* button appear.

.. figure:: images/amspackages_gui4.png
  :width: 80%
  :align: center

Clicking it will provide you with a new dialog, where you can select your choice from the list of compatible packages.

.. figure:: images/amspackages_gui3.png
  :width: 50%
  :align: center

After clicking confirm, copying of selected packages will proceed.


Selecting an alterative package source
--------------------------------------

If you are on a computer with a slow connection or behind a firewall, you can select a local copy of our repository
using the **local mirror** button. 
Navigate to your copy and and select the ``AMS2021.1.yml`` file inside the ``packages`` directory.

.. warning::

  Never install packages from an untrusted source. Only use a copy directly downloaded from our website.

.. figure:: images/amspackages_gui2.png
  :width: 80%
  :align: center

Instructions on how to obtain a copy can be found in the `installation section <../Installation/Optional_Components.html#using-a-local-package-source>`__.

