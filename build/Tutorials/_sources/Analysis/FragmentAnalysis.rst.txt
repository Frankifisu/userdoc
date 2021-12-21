.. _FRAGMENT: 

Fragment Analysis
*****************

This tutorial will show you how to perform a Fragment Analysis using `ADF <../../ADF/index.html>`__ and visualize the results. The three examples used here are: 

Ni(CO)\ :sub:`4` 
    A fragment analysis with one Ni fragment and one CO fragment repeated four times.

PtCl\ :sub:`4` H\ :sub:`2` \ :sup:`2-`
    A fragment analysis with one PtCl\ :sub:`4` \ :sup:`2-` fragment and one H\ :sub:`2` fragment. This is a good example on how to specify the charges of the fragments. 

CH\ :sub:`3`\ I
     A fragment analysis with one CH\ :sub:`3` fragment and one I fragment). This is a good example to show how to use spin-unrestricted fragments.

.. tip::

   These tutorials can also be run from the command-line. See

   * `How to run examples from the command-line <../../ADF/Examples/Examples.html>`__
   * `Example: Compound Fragments: Ni(CO)4 <../../ADF/Examples/Frags_NiCO4.html>`__
   * `Example: Fragments: PtCl4H2 2- <../../ADF/Examples/Frags_PtCl4H2.html>`__
   * `Example: unrestricted fragments: CH3I <../../ADF/Examples/EDA_Unr_CH3I.html>`__


Ni(CO)\ :sub:`4` 
================

Build the Structure
-------------------


The structure is perfectly tetrahedral. You should be able to build the molecule yourself using the techniques described in earlier tutorials.

.. seealso::

    :ref:`Building structure tutorials <building_structures>`

One possible way: 

.. rst-class:: steps

  \ 
    | **1.** Start AMSinput
    | **2.** Build a tetrahedral metal complex: |StructTool| **→ Metal Complexes → ML4 tetrahedral**
    | **3.** Change the central atom into a Ni atom
    | **4.** Select one ligand
    | **5.** Select all ligands: **Select → Select Atoms Of Same Type** menu command
    | **6.** Change them in CO ligands: **Atoms → Replace By Structure → Ligands → CO**
    | **7.** Symmetrize the system by clicking on |SymmTool|
    | **8.** Choose the **Geometry Optimization** task
    | **9.** Save and Run
    | **10.** When the run has finished, click 'Yes, New Job' to import the optimized coordinates

Alternatively, copy-paste the following coordinates in AMSinput::

    Ni  0.0000000000000  0.0000000000000  0.0000000000000
    O  -1.7186781693251  1.7186781693251  1.7186781693251
    O   1.7186781693251 -1.7186781693251  1.7186781693251
    O  -1.7186781693251 -1.7186781693251 -1.7186781693251
    O   1.7186781693251  1.7186781693251 -1.7186781693251
    C   1.0473110733159  1.0473110733159 -1.0473110733159
    C  -1.0473110733159 -1.0473110733159 -1.0473110733159
    C   1.0473110733159 -1.0473110733159  1.0473110733159
    C  -1.0473110733159  1.0473110733159  1.0473110733159

Your molecule should look something like this: 

.. figure:: /Images/FragmentAnalysis/tut8-molecule.png
    :align: center

Define fragments
----------------

The fragments that ADF uses are based on the regions that you define. In this example we will generate four new regions: one for each of the CO ligands. 
The regions for the CO ligands will get special names to make sure that ADF recognizes them as one fragment repeated four times. 

The Ni atom will not be in a region. AMSinput will automatically create atomic fragments for all atoms not in a region. 

Repeated fragments are indicated with the fragment name followed by ``|n``, with ``n`` the number of the copy (see also the `ADF user manual on fragments <../../ADF/Input/Molecular_fragments.html>`__).
All copies must match such that one fragment can be positioned exactly over another fragment by rotation and translation. 
ADF checks for this, AMSinput does not. In this particular example all four CO fragments are obviously identical by symmetry. 

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Regions**
    | **2.** Select all atoms
    | **3.** Click the "+" button to add a new region (containing all atoms)
    | **4.** Select the Ni atom
    | **5.** Remove the Ni atom from Region_1: click the "-" button on the right side of the 'Region_1' 
    | **6.** Change the name of 'Region_1' into 'CO'

Now one new region has been defined: the CO region for the ligands. The next step is to split the ligand region into four repeated regions: 

.. rst-class:: steps

  \ 
    | **1.** Press the triangle on the right side of the CO region line
    | **2.** In the pop-up menu, use the **Split By Molecule** command

This should result in the following regions: 

.. figure:: /Images/FragmentAnalysis/nico4regions.png
    :align: center


Set up the fragment analysis run
--------------------------------

The next step is very easy: we will tell ADF to perform a Single Point calculation (fragment analysis in ADF only works with a single point calculation), and we tell AMSinput to use the regions that we just defined as fragments: 

.. rst-class:: steps

  \ 
    | **1.** Open the 'Main' panel
    | **2.** Select the **Single Point** task
    | **3.** Panel bar **MultiLevel → Fragments**
    | **4.** Check the 'Use fragments' check box

.. tip::

    The |MoreBtn| to the right of Task links to the Fragments panel if the task is "Single Point"

.. figure:: /Images/FragmentAnalysis/tut8-panel.png
    :align: center

In the Fragments panel you will see that one fragment is present, without charge: the repeated CO fragment. 
ADF will use basic atomic atoms for any atoms not put in another fragment. Thus, the Ni atom will be an atomic fragment. 

Run the fragment analysis and view the results
----------------------------------------------

Next you will Save and Run the calculation. When you do this, AMSinput will actually save two different calculations: 

+ The CO calculation (with matching .ams and .run file)   
+ The Ni(CO)\ :sub:`4`  fragment analysis calculation (with   matching .ams and .run file)   

You do not need to run the calculation for the CO fragment first, it will automatically be executed when needed.

.. rst-class:: steps

  \ 
    | **1.** Save
    | **2.** Run
    | **3.** Wait for the calculation to finish (note that first the fragment calculation (CO) is executed, followed by the final fragment analysis)

This calculation results in the normal .rkf and .out output files. 
You can view them with the **SCM → View** and   **SCM → Output** commands. 
More interesting in the case of a fragment analysis is the interaction diagram that you can view using AMSlevels: 

.. rst-class:: steps

  \ 
    | **SCM → Levels** 

.. figure:: /Images/FragmentAnalysis/tut8-levels.png
    :align: center


In the center you see the levels of the whole molecule, on the sides you see the CO fragment and the Ni-atom fragment. 

**The red interaction lines tell you which molecular orbitals come from which fragment orbitals**. 
The brightness of the line is directly related to the contribution %.

**The blue interaction lines together show the orbital interaction, and are drawn when a bonding and anti-bonding combination can be made.** 
The strength of this interaction is calculated by taking the geometric average of the 4 contributions. 
Compared to the normal average, the geometric average places more emphasis on equal contributions. 
This will give 50-50 contributions the strongest interaction, and 0-100 contributions no interaction at all. 
The strongest interaction is drawn, and weaker interactions can be drawn by using the menu or the shortcuts. 

In the output file you can find detailed information about the composition of the molecular levels in terms of the fragment   orbitals. 

PtCl\ :sub:`4` H\ :sub:`2` \ :sup:`2-` 
======================================

Build the structure
-------------------

We will now perform a similar fragment calculation for a PtCl\ :sub:`4` H\ :sub:`2` \ :sup:`2-` molecule.
The following is a picture of the PtCl\ :sub:`4` H\ :sub:`2` \ :sup:`2-` molecule, after optimization with ADF: 

.. figure:: /Images/FragmentAnalysis/tut8-mol2.png
    :align: center

To make this molecule, an easy way is to start with an octahedral complex to ensure symmetry. Next make changes to get this molecule, 
ending with a geometry optimization with ADF: 

.. rst-class:: steps

  \ 
    | **1.** Build an octahedral metal complex using the Structures button (|StructTool| **→ Metal Complexes → ML6 octahedral**)
    | **2.** Change the central atom into a Pt atom
    | **3.** Change four dummies in a plane into Cl atoms
    | **4.** Remove one of the remaining dummies
    | **5.** Change the remaining dummy in OH, via **Atoms → Replace by structure → Ligands → OH** (this will ensure the final two H's do not break symmetry)
    | **6.** Change the O atom into an H atom
    | **7.** Symmetrize the system by clicking on |SymmTool|

.. rst-class:: steps

  \ 
    | **1.** Choose the **Geometry Optimization** task
    | **2.** Set the **total charge** to **-2**
    | **3.** Run
    | **4.** When the run has finished, click 'Yes, New Job' to import the optimized coordinates

Note that pre-optimization using UFF will make the geometry worse, if you wish you can pre-optimize using Mopac. 
But the ADF geometry optimization will also converge without pre-optimization. 

Or, copy-paste the following coordinates and symmetrize the system by clicking on |SymmTool| (do not forget to set the **charge** to **-2**)::

    Pt  0.0         0.0         0.70977802 
    Cl  2.39841436  0.0         0.75420182 
    Cl  0.0         2.39841436  0.75420182 
    Cl -2.39841436  0.0         0.75420182 
    H   0.0         0.0        -2.26954689 
    Cl  0.0        -2.39841436  0.75420182 
    H   0.0         0.0        -1.45703842 


After copy-pasting the H atoms will not be bonded in the picture. That is no problem as ADF does only look at the atom positions.

Define fragments
----------------

Define the PtCl\ :sub:`4` \ :sup:`2-`  and H\ :sub:`2`    fragments in the Regions panel: 

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Regions**
    | **2.** Select the Pt and Cl atoms
    | **3.** Use the '+' button to add a new region, and name it 'PtCl4'
    | **4.** Select the two H atoms
    | **5.** Use the '+' button to add a new region, and name it 'H2'
    | **6.** Clear the atom selection (click in empty space)

.. figure:: /Images/FragmentAnalysis/tut8-frags.png
    :align: center


Now the fragments are defined. Next, we set up the fragment   analysis calculation: 

.. rst-class:: steps

  \ 
    | **1.** Select the **Main** panel
    | **2.** Select the **Single Point** task
    | **3.** Panel bar **MultiLevel → Fragments** (or click the |MoreBtn| button)
    | **4.** Check the **Use fragments** check box
    | **5.** Change the charge of the PtCl4 fragment to -2 
    | **6.** Save

**If you skipped the geometry optimization step and copy-pasted the coordinates, be sure to set the overall overall charge to -2 in the main panel!**

.. figure:: /Images/FragmentAnalysis/tut8-fragdetails.png
    :align: center


When you click on the Open button (the big dot) next to the PtCl4 fragment, you can inspect the PtCl4 fragment setup: 

.. rst-class:: steps

  \ 
    | **1.** Click on the Open button (the big dot next to the PtCl4 fragment) in the 'Fragments' panel
    | **2.** Check the charge of the fragment in the newly opened AMSinput (should be -2)
    | **3.** Close the PtCl4 fragment AMSinput window

For more complex calculations, you could make additional changes to your fragment runs. 

Run the fragment analysis and view the results
----------------------------------------------

Next you will Run the calculation: 

.. rst-class:: steps

  \ 
    | Run

After the calculation has finished, you can view the resulting   interaction diagram: 

.. rst-class:: steps

  \ 
    | **1.** Use the **SCM → Levels** command 
    | **2.** Use the mouse (drag with left mouse, scroll wheel, drag with right mouse)
    | **3.** zoom in on the interesting region (roughly from -0.5 to 0.4)
    | **4.** Select the PtCl4H2 column (by clicking on the name at the bottom
    | **5.** Use the **View → Interactions → Show** menu command 
    | **6.** Right-click in the H2 column, **Shift Stack...**, shift the H2 levels by +0.28

Only interactions between visible levels are shown. So, if you   zoom out no interactions will be visible for some of the levels.   
That is the reason that you will need to use the Show   Interactions menu command. 

We needed to shift the H2 levels to accommodate that in the final molecule the fragment experiences a -2 charge, which is absent from the H2 fragment calculation. 
The interaction diagram should look something like the following: 

.. figure:: /Images/FragmentAnalysis/tut8-levels2.png
    :align: center


In the output file you can find detailed information about the composition of the molecular levels in terms of the fragment orbitals. 

CH\ :sub:`3`\ I
===============

We will now perform an unrestricted fragment analysis for a CH\ :sub:`3`\ I molecule.

Here we will use real spin-unrestricted fragments.
An alternative approach is to use spin-restricted fragments in combination with the `FRAGOCCUPATIONS key <../../ADF/Input/Electronic_Configuration.html#simulated-unrestricted-fragments-with-key-fragoccupations>`__  in which the spin-unrestricted occupations are defined.

Set up the calculation
----------------------

Copy-paste the following coordinates::

    C       0.000000000   0.000000000  -0.23931600
    H      -0.521322100  -0.902956364  -0.56271600
    H      -0.521322100   0.902956364  -0.56271600
    H       1.042644200  -0.000000000  -0.56271600
    I       0.000000000   0.000000000   1.92746400

.. rst-class:: steps

  \ 
    | In the **Main** panel:
    | **1.** **Task → Single Point**
    | **2.** **XC functional → GGA:BP86**
    | **3.** **Basis set → TZ2P**
    | **4.** **Frozen core → Small**
    | **5.** **Numerical quality → Good**

.. figure:: /Images/FragmentAnalysis/tut8-settings3.png
    :align: center


Define the CH\ :sub:`3` and I fragments in the Regions panel: 

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Regions**
    | **2.** Select the I atom
    | **3.** Use the '+' button to add a new region, and name it 'I'
    | **4.** Invert the selection: **Select → Invert Selection** menu command
    | **5.** Use the '+' button to add a new region, and name it 'Methyl'
    | **6.** Clear the atom selection (click in empty space)

.. figure:: /Images/FragmentAnalysis/tut8-frags3.png
    :align: center


Now the fragments are defined.
Next, we set up the unrestricted fragment analysis calculation.

Prepared for bonding
--------------------

The electron configuration of the fragments will be chosen such that the valence I p\ :sub:`z` orbital
has 1 alpha electron, and the highest occupied Methyl orbital has 1 beta electron.
Note that this electron configuration of the fragments means that they
are so called 'prepared for bonding' in order to minimize the Pauli repulsion in
the electron pair bond, which in this case is a sigma-bond in the z-direction.


.. rst-class:: steps

  \ 
    | **1.** Panel bar **MultiLevel → Fragments**
    | **2.** Check the 'Use fragments' check box
    | **3.** Change the spin polarization of the I fragment to 1
    | **4.** Change the spin polarization of the Methyl fragment to -1

.. figure:: /Images/FragmentAnalysis/tut8-fragdetails3.png
    :align: center


Note that the GUI shows a label 'Spin' which in fact should be 'Spin polarization'.
If fragments are used symmetry has been set by the GUI to NOSYM. In this case, however, we would like to use symmetry.
If one uses real spin-unrestricted fragments the calculation on the full complex must also be calculated spin-unrestricted.

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Details → Symmetry**
    | **2.** **Symmetry → AUTO**
    | **3.** **File → Save**

In the electron configuration of the I atomic fragment we want the p\ :sub:`z` alpha orbital to be occupied,
and the p\ :sub:`z` beta orbital to be unoccupied.
In order to make such an electron configuration the I atomic fragment is not calculated in atomic symmetry but calculated in a subsymmetry, in this case D∞h (D(LIN)),
in which p\ :sub:`z` is in a different irrep (SIGMA.u) than p\ :sub:`x` and p\ :sub:`y` (PI.u).
The symmetry requirements in ADF for calculating an atom in D∞h symmetry are such that the atom should be in the origin.
For convenience the I atomic fragment is precalculated in D∞h symmetry without specifying the electronic configuration.
Next the electronic configuration of this calculation is adjusted to the desired electronic configuration.

.. rst-class:: steps

  \ 
    | **1.** Panel bar **MultiLevel → Fragments**
    | **2.** Click on the Open button (the big dot next to the I fragment) in the 'Fragments' panel
    | **3.** In the newly opened AMSinput window:
    | **4.** Put the I atom in the origin (select the I atom, then **Edit → Set Origin**)
    | **5.** Panel bar **Details → Symmetry** Molecular symmetry **Symbol → D(LIN)**
    | **6.** Run the I fragment calculation
    | **7.** After the calculation has finished (still for the I fragment calculation):
    | **8.** Panel bar **Model → Spin and Occupation**
    | **9.** Change the electron configuration from 4/3 to 2 beta electrons in PI.u
    | **10.** Change the electron configuration from 2/3 to 0 beta electrons in SIGMA.u
    | **11.** Close and save the I fragment AMSinput window

.. figure:: /Images/FragmentAnalysis/tut8-spinocc3.png
    :align: center


Run the calculation
-------------------

Next you will Run the calculation: 

.. rst-class:: steps

  \ 
    | Open the CH3I AMSinput window
    | Run

After the calculation has finished, you can view the resulting interaction diagram: 

.. rst-class:: steps

  \ 
    | **1.** Use the **SCM → Levels** command 
    | **2.** **Axes → Unit → eV**
    | **3.** Use the mouse (drag with left mouse, scroll wheel, drag with right mouse)
    | **4.** zoom in on the interesting region (roughly from -9 to -2 eV)
    | **5.** **View → Labels → Show**

.. figure:: /Images/FragmentAnalysis/tut8-levels3.png
    :align: center


If you move the mouse over a molecular orbital (MO) level one can find out more detailed information about the composition of the MO level in terms of the symmetrized fragment orbitals (SFOs).
The most important contributions are given including an overlap S(sfo) of the SFOs that participate the most.
A '+' or '-' sign directly after an overlap value between two different SFOs indicates whether the contributions of these two SFOs form a bonding combination ('+') or anti-bonding combination ('-') in the MO.

.. figure:: /Images/FragmentAnalysis/tut8-molevels3.png
    :align: center


The 4A1 MO is (mostly) a bonding combination of a I p\ :sub:`z` fragment orbital (a p\ :sub:`z` orbital has irrep label SIGMA.u in symmetry D(LIN)) and a Methyl 2A1 fragment orbital.
Although the 4A1 alpha MO and the 4A1 beta MO are spatially the same, the decomposition in terms of SFOs is (slightly) different, since the spin alpha and spin beta SFOs are not spatially the same.
