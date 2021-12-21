.. This tutorial has been recorded: examples/tutorials/bsse-double-hybrids
.. Keep the recording in sync so it may be used to generate the images!

.. _BSSE_double_hybrids: 

Basis set superposition error (BSSE)
************************************

This tutorial will show you how to calculate a `basis set superposition error (BSSE) <../../ADF/Input/BSSE.html>`__ using `ADF <../../ADF/index.html>`__ for a formamide dimer.
The first method uses `atomic fragments <../../ADF/Input/Basis_sets_and_atomic_fragments.html>`__, the second method uses `molecular fragments <../../ADF/Input/Molecular_fragments.html>`__.

In this example `double-hybrids <../../ADF/Input/Density_Functional.html#post-scf-correlation-methods>`__ are used.
Note that this example is not a typical example in which double-hybrids improve much over dispersion-corrected hybrid functionals.
However, this example is relevant for double hybrids, since the BSSE is typically larger for double-hybrids than for standard GGA or hybrid functionals.
Thus for double-hybrids it is especially relevant to correct for a BSSE.

An all electron `TZ2P basis set <../../ADF/Input/Basis_sets_and_atomic_fragments.html>`__ is used since that is the recommended choice in ADF for double hybrids.
For reasons of numerical stability, it is also highly recommended not to use larger or more diffuse basis sets.
The use of triple-zeta quality basis sets is usually necessary for accurate double-hybrid energies.


Method 1: atomic fragments
==========================

.. rst-class:: steps

  \ 
    | **1.** Start a new AMSinput
    | **2.** Copy-paste the following coordinates of a formamide dimer in the molecule-drawing area of AMSinput:

::

  C       2.01911735      -0.03015376       0.00000000
  C      -2.01911735       0.03015376       0.00000000
  N       1.39482051       1.15825415       0.00000000
  N      -1.39482051      -1.15825415       0.00000000
  H       0.37362012       1.21206244       0.00000000
  H       3.11670830       0.04878624       0.00000000
  H       1.94222103       1.99902922       0.00000000
  H      -1.94222103      -1.99902922       0.00000000
  H      -0.37362012      -1.21206244       0.00000000
  H      -3.11670830      -0.04878624       0.00000000
  O       1.46498124      -1.12721089       0.00000000
  O      -1.46498124       1.12721089       0.00000000

.. rst-class:: steps

  \ 
    | Calculation settings:
    | **1.**  XC functional: **Double Hybrids → B2PLYP-D3BJ**.
    | **2.** Basis set: **TZ2P**.
    | **3.** Frozen core: **None**.

Save and run the calculation:

.. rst-class:: steps

  \ 
    | **1.** Click on **File → Save As...** and give it the name "Formamide_dimer".
    | **2.** Click on **File → Run**.
    | Wait for the calculation to finish.

We will now use `Ghost atoms <../../ADF/Input/Basis_sets_and_atomic_fragments.html#ghost-atoms-non-standard-chemical-elements>`__ for one of the two formamide molecules:

.. rst-class:: steps

  \ 
    | In AMSinput:
    | **1.** Select all atoms of one of the formamide monomers (holding shift)
    | **2.** Select **Atoms → Ghosts → Change Atoms to Ghosts**
    | **3.** Click on **File → Save As...** and give it the name "Formamide_BSSE".
    | **4.** Click on **File → Run**.
    | Wait for the calculation to finish.

.. image:: /Images/BSSEDoubleHybrid/BSSE_formamide.png

Note that the geometry of the two monomers is exactly the same apart from a
rotranslation.  The BSSE-corrected (counterpoise-corrected) energy of the
Formamide dimer with respect to its monomer fragments can now be calculated as
the bond energy printed in Formamide_dimer.logfile minus two times the bond
energy printed in Formamide_BSSE.logfile. The result is approximately -15.6
kcal/mol.

Method 2: molecular fragments
=============================

.. rst-class:: steps

  \ 
    | **1.** Start a new AMSinput
    | **2.** Copy-paste the coordinates of the formamide dimer of method 1
    | **3.** XC functional: **Double Hybrids → B2PLYP-D3BJ**.
    | **4.** Basis set: **TZ2P**.
    | **5.** Frozen core: **None**.


.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Regions**
    | **2.** Select all atoms of one of the formamide monomers (holding shift)
    | **3.** Click the '+' button to add a new region (containing the atoms of 1 monomer)
    | **4.** Change the name of 'Region_1' into 'monomer'
    | **5.** Select **Select → Invert Selection**
    | **6.** Select **Atoms → Ghosts → Change Atoms to Ghosts**

.. image:: /Images/BSSEDoubleHybrid/BSSE_formamide_Regions.png

.. rst-class:: steps

  \ 
    | **1.** Panel bar **MultiLevel → Fragments**
    | **2.** Check the **Use fragments** check box
    | **3.** Click on **File → Save As...** and give it the name "Formamide".
    | **4.** Click on **File → Run**.
    | Wait for the two calculations to finish.

The BSSE for the formamide monomer (which is the energy of the monomer calculated in the dimer basis set minus the the energy of the monomer calculated in its own monomer basis) set is printed as bond energy in Formamide.logfile, which is approximately -0.88 kcal/mol.

Next we calculate the formamide dimer using the formamide monomer as fragment.
Note that the geometry of the two monomers is exactly the same apart from a rotranslation, which means that the same monomer fragment can be used.

.. rst-class:: steps

  \ 
    | **1.** Start a new AMSinput
    | **2.** Copy-paste the coordinates of the formamide dimer of method 1
    | **3.** XC functional: **Double Hybrids → B2PLYP-D3BJ**.
    | **4.** Basis set: **TZ2P**.
    | **5.** Frozen core: **None**.

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Regions**
    | **2.** Select all atoms of one of the formamide monomers (holding shift)
    | **3.** Click the '+' button to add a new region (containing the atoms of 1 monomer)
    | **4.** Select **Select → Invert Selection**
    | **5.** Click the '+' button to add a new region (containing the atoms of the other monomer)

.. rst-class:: steps

  \ 
    | **1.** Panel bar **MultiLevel → Fragments**
    | **2.** Check the 'Use fragments' check box
    | **3.** Click on the folder next to **Region_1:** and select Formamide.monomer.results/adf.rkf
    | **4.** Click on the folder next to **Region_2:** and select Formamide.monomer.results/adf.rkf

.. image:: /Images/BSSEDoubleHybrid/BSSE_MultiLevel.png

.. rst-class:: steps

  \ 
    | **1.** Click on **File → Save As...** and give it the name "Formamide_dimer_EDA".
    | **2.** Click on **File → Run**.
    | Wait for the calculation to finish.

The uncorrected energy of the Formamide dimer with respect to its monomer fragments can now be read from the
Formamide_dimer_EDA.logfile and is approximately -17.39 kcal/mol.
After correction this energy for BSSE this makes -17.39 - 2*(-0.88) = -15.6 kcal/mol as was found in method 1.

Note that in the energy decomposition analysis (EDA) in case of double-hybrids is incomplete.
The bonding energy with respect to the individual fragments is calculated and printed out.
However, all terms which rely on the orthogonal fragment density (e.g. Pauli repulsion terms) do not include the MP2 part of the double-hybrid.
