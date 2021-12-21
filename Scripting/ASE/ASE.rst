
.. _ASE:

ASE
###

The `Atomic Simulation Environment (ASE) <https://wiki.fysik.dtu.dk/ase/>`_ tool collection suite was designed as a flexible, easy-to-use, and customizable approach for the manipulation of quantum chemical models as well as for setting up and running the calculations required and for the analysis of the final results.

The development of ASE was originally started at the Technical University of Denmark but received also significant contributions from a large, international community.
While ASE is `available <https://gitlab.com/ase/ase/tree/3.13.0/>`_ under a GNU LGPL license, a modified version of this library is shipped together with the Amsterdam Modeling Suite.

This latter version of ASE provides the interfaces to `ADF <../../ADF/index.html>`__, `BAND <../../BAND/index.html>`__, `DFTB <../../DFTB/index.html>`__, `ReaxFF <../../ReaxFF/index.html>`__.
In addition, the shipped version was extended by several command line scripts that allow one to perform tasks such as geometry and  transition state searches in terms of single-line commands.

The interfaces of ASE to the Amsterdam Modeling Suite were written by Damien Coupry and Thomas M. Soini.

While the reader is encouraged to consult the very detailed `ASE manual <https://wiki.fysik.dtu.dk/ase/ase/ase.html>`__  for the clarification of technical details, an overview about the general concepts and mechanisms behind ASE is provided.
The rest of this section is then dedicated to a documentation and a demonstration of the usage of the extensions to ASE provided in the Amsterdam Modeling Suite.


.. only:: html
   
   **External ASE links:**

   * `ASE Manual <https://wiki.fysik.dtu.dk/ase/>`__

   * `ASE Tutorials <https://wiki.fysik.dtu.dk/ase/tutorials/tutorials.html#ase>`_

   * `ASE Download <https://wiki.fysik.dtu.dk/ase/install.html>`_ as an external library (mind to set the correct Python environment variables)


.. note::

   On Windows machines the developers of the ASE library provide only a partial support, see `the ASE website <https://wiki.fysik.dtu.dk/ase/download.html#installation-on-windows>`_ for further details.

.. toctree::
   :maxdepth: 1

   General_ASE_concepts
   SCM_ASE_Calculators

