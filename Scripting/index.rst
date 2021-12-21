.. Scripting documentation master file, created by
   sphinx-quickstart on Sun Sep 27 18:43:21 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Scripting |release|
===================

The Amsterdam Modeling Suite includes several scripting environments, each with a specific scope and purpose.

Most elemental are amsprepare, amsreport, and similar tools meant to be called from a console shell such as bash. 
Through various command line options these tools allow for the automatized preparation of series of input files.

More advanced scripting environments are based on the `Python <http://www.python.org/>`_ programming language.
As a consistently object oriented language Python can be employed for flexible and rapid scripting solutions for the quantum chemical problem at hand.

To this end, the quantum chemistry programs `ADF <../ADF/index.html>`_, `BAND <../BAND/index.html>`_, `DFTB <../DFTB/index.html>`_, and `ReaxFF <../ReaxFF/index.html>`_ were interfaced to the popular, external Python scripting library `Atomic Simulation Environment (ASE) <https://wiki.fysik.dtu.dk/ase/>`_.
ASE can be used for the automatized manipulation of chemical systems and quantum chemical calculation prescriptions to compute a large variety of different chemical and physical properties.

FlexMD is a python library that is specifically intended for scripting solutions in the field of molecular dynamics simulations.
Indeed, FlexMD features implementations of a variety of approaches to multi-scale simulations and especially adaptive QM/MM methods, which are interfaced to the aforementioned ASE library.

The Python Library for Automating Molecular Simulations (PLAMS) represents another flexible and extendable Python interface to several quantum chemical programs.
In contrast to the other scripting environments mentioned above, PLAMS focuses on easing the input preparation, job execution, file management, and output processing.
It thereby allows one to automatize even very advanced data workflows.

Also the PyADF library pursues the concept of automatizing the workflows required for multiscale simulations.
PyADF is currently not part of the Amsterdam Modeling Suite but can be readily retrieved from an `external source <https://www.tu-braunschweig.de/pci/research/theorie/software/pyadf>`_.

.. toctree::
   :maxdepth: 1

   GettingStarted
   Commandline_Tools/Commandline_Tools
   Python_Stack/Python_Stack
   ASE/ASE
   FlexMD/FlexMD
   PLAMS/PLAMS
   AuToGraFS/AuToGraFS

.. only:: html
   
*  :download:`(PDF) Scripting<download/Scripting.pdf>`

