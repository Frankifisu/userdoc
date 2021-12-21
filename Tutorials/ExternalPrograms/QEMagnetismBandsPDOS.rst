.. _qe_Magnetism_bandstructures_pdos:

Magnetism, Band Structure and pDOS
**********************************

This tutorial will teach you how to:

+ set up unrestricted calculations (Magnetism) with the Quantum ESPRESSO GUI
+ assign different initial spins
+ calculate the band structure and dos in the same job
+ observe spin results using AMSview, the KFbrowser and AMSoutput
+ view band structure and pDOS using AMSbandstructure


Step 1: Start AMSinput
======================

.. rst-class:: steps

  \
    | Start AMSinput
    | Switch to **Quantum ESPRESSO**: |ADFPanel| **→** |QuantumESPRESSOPanel|

If you have not yet installed Quantum ESPRESSO a dialog will pop up suggesting to install Quantum ESPRESSO by downloading it from the SCM web site.
This is required for this tutorial to work. Downloading may take a while as it is a big package.

.. image:: /Images/QEMagnetismBandsPDOS/QE-main.png


Step 2: Set up the system - Iron supercell
==========================================

First make an Iron crystal:

.. rst-class:: steps

  \
    | Press cmd-F or ctrl-F to activate the search box |Search|
    | Type 'Fe' in the search box
    | Click on 'Fe' in the list of found Crystals

The unit cell has 1 atom. Rotate the system to get a good view.
As we want to assign different spins in this tutorial we need a super cell:

.. rst-class:: steps

  \
    | Start the supercell tool **Edit → Crystal → Generate Super Cell**
    | Click OK (the default 2x2x2 is fine in this case)
    | Move / rotate / zoom to get a good view

.. image:: /Images/QEMagnetismBandsPDOS/iron-supercell.png


Step 3: Set up the anti-ferromagnetic iron calculation
======================================================

Let's first set up the slightly more complex anti-ferromagnetic system calculation.

We need to assign initial spins up to some atoms, and initial spin down to other atoms.
For that reason we need different types of iron atoms. This can be done using Regions.

.. rst-class:: steps

  \
    | Select four iron atoms by shift clicking, two per side (never the ones closes to each other)
    | Make a new region from these atoms **Atoms → New Region From Selected Atoms**
    | Repeat this to make a region from the four other atoms

.. image:: /Images/QEMagnetismBandsPDOS/iron-regions.png

Next set up the magnetism details:

.. rst-class:: steps

  \
    | Select 'Collinear' from the Magnetization option in the panel
    | Click the |MoreBtn| button next to Collinear to go to the Magnetization panel

In this panel you set the starting magnetization for the different atoms.
As you can see there are two iron atom types, let's assign them a starting magnetization of -1 and 1 so we get an anti-ferromagnetic state:

.. rst-class:: steps

  \
    | Enter -1 and 1 as starting magnetization for the different iron atoms.

.. image:: /Images/QEMagnetismBandsPDOS/iron-antiferromagnetic.png

Note that this is a starting magnetization, it is possible that the final SCF calculation ends up in a different state!

The magnetism options have now been taken care of, next the other calculation options need to be set.
As iron is a metal we will have to use the smearing option.
To speed up the calculation, lets reduce the K grid to 5x5x5 (for real application you need to test convergence with the K grid).
In this tutorial we will also calculate the pDOS and band structure of the system.

.. rst-class:: steps

  \
    | Go to the Main panel
    | Select 'Gaussian' from the Occupation menu
    | Enter '0.01' as smearing width
    |
    | Enter 5 5 5 as the number of K points to be used
    |
    | Select 'PBE' from the pseudopotential XC menu
    | Select 'van' from the pseudopotential type menu
    |
    | Click the 'DOS' check box
    | Click the 'Bandstructure' check box

.. image:: /Images/QEMagnetismBandsPDOS/iron-setup.png

Again, the choice of pseudopotential in this example is just an example and not an advise!

Save your set up as 'iron-antiferromagnetic'

.. rst-class:: steps

  \
    | Save: **File → Save**
    | Enter 'iron-antiferromagnetic' as name and click the Save button


Step 4: Set up the ferromagnetic iron calculation
=================================================

Before running, lets also setup the ferromagnetic version as we already have AMSinput open.
The changes are minimal, only the starting magnetization needs to be set differently.

.. rst-class:: steps

  \
    | Click the |MoreBtn| button next to Collinear to go to the Magnetization panel
    | Specify 1 as starting magnetization for both iron types
    | Save with a different name: Save: **File → Save As**
    | Enter 'iron-ferromagnetic' as name and click the Save button

.. image:: /Images/QEMagnetismBandsPDOS/iron-ferromagnetic.png

Again, note that this is a starting magnetization, it is possible that the final SCF calculation ends up in a different state!


Step 5: Run the calculations
============================

The easy step: use AMSjobs to run your jobs:

.. rst-class:: steps

  \
    | In AMSjobs select your two jobs (via shift-click or control-click)
    | Run them: **Job → Run**

You should see the two jobs running, one after the other, and you can follow their progress.


Step 6: Examine the results
===========================

KFBrowser
---------
When the calculations are ready (as is visible in AMSjobs) the first thing is to make sure that the spin is as expected.
One way to see that is via the KFBrowser:

.. rst-class:: steps

  \
    | In AMSjobs select the ferromagnetic job
    | Start the KFBrowser **SCM → KF Browser**
    | open the 'Charges and Spins' section (click on the triangle in front of it)
    | open the 'Atomic Spin' variable
    |
    | Repeat this for the antiferromagnetic job (without closing the first KFBrowser window)

Now you can compare the spin results:

.. image:: /Images/QEMagnetismBandsPDOS/iron-kfbrowser-spins.png

As you can see the ferromagnetic calculation resulted in all iron atoms having the same spin, and thus a total spin.
For the anti-ferromagnetic calculations the iron atoms have alternating spins, and an almost zero total spin.

The KFBrowser gives access to many other properties, in particular you can have a look at the energies if you wish
.

Output
------
In the output file you can also find Lowdin Charges, breaking up the spin in different components.
These results are generated by activating the pDOS calculation (which is the default when you check the DOS check button):

.. rst-class:: steps

  \
    | Select the ferromagnetic job in AMSjobs
    | Open the output (**SCM → Output**)
    | Search (at the bottom) for Lowdin

The text in the output window should scroll immediately to the section with Lowdin charges:

.. image:: /Images/QEMagnetismBandsPDOS/iron-ferro-lowdin.png

AMSbandstructure
----------------
With the AMSbandstructure module you can inspect the band structure of your system (if calculated of course),
as well as the DOS or partial DOS (again if calculated).
In this case all are available. So lets have a look:

.. rst-class:: steps

  \
    | In AMSjobs select the ferromagnetic job
    | Start the AMSbandstructure module (**SCM → Band Structure**)

.. image:: /Images/QEMagnetismBandsPDOS/iron-ferro-bandstructure.png

You can easily see the different structure for the alpha and beta electrons in the band structure (solid and dotted lines).
The partial DOS display shows you the composition of the bands in terms of atomic shells (s, p, d) for both the alpha and beta spins.
In the DOS menu you can switch what to see.

Do the same for the antiferromagnetic job:

.. rst-class:: steps

  \
    | In AMSjobs select the antiferromagnetic job
    | Start the AMSbandstructure module (**SCM → Band Structure**)

.. image:: /Images/QEMagnetismBandsPDOS/iron-antiferro-bandstructure.png

In this case due to symmetry the alpha and beta curves are on top of each other.

You can also see the partial DOS for a particular atom:

.. rst-class:: steps

  \
    | In the AMSbandstructure window for the antiferromagnetic job:
    | Select the **Atoms** tab in the bottom left
    | Disable the repeated unit cell view:  **View → Periodic → Repeat Unit Cells**
    | **View → Atom Info → Name → Show**
    | Select the Fe(1) atom
    | Right-click on it, and in the menu that pops-up select **DOS → Total (s+p+d+f)**
    | Select the Fe(5) neighboring atom
    | Right-click on it, and in the menu that pops-up select **DOS → Total (s+p+d+f)**

.. tip::
   In AMSbandstructure you can change the relative size of the three panels by clicking-and-dragging the gray line between the panels.
   You can also zoom the x and y axis independently by positioning the mouse cursor on an axis and then use the mouse scroll wheel to zoom in/out

.. image:: /Images/QEMagnetismBandsPDOS/iron-anti-totaldos.png

If you look carefully you can see in the DOS section that the spin alpha and beta have been switched for atoms Fe1 and Fe5.

AMSview
-------

With AMSview we can examine fields and atomic properties.

.. rst-class:: steps

  \
    | In AMSjobs select the antiferromagnetic job
    | Open AMSview **SCM → View**
    |
    | **In AMSview:**
    | Show the atomic spins: **Properties → Atom Info → Atomic: Spin (quantum espresso) → Show**

Now the atomic spins will be show as a label next the atoms. Even more visual is to color the atoms by the spin:

.. rst-class:: steps

  \
    | Color the atoms by the spin: **Properties → Color Atoms By → Atomic: Spin (quantum espresso)**

.. image:: /Images/QEMagnetismBandsPDOS/iron-anti-view-spin.png

To view the spin polarization density:

.. rst-class:: steps

  \
    | Add an isosurface with phase **Add → Isosurface: With Phase**
    | In the control line at the bottom of the window select spin polarization: **Select Field... → Density → Spin Polarization**

.. image:: /Images/QEMagnetismBandsPDOS/iron-anti-view-spinpolarization.png

You can compare these images to similar images for the ferromagnetic iron results.

Note that in AMSview you can also visualize other field, like the (valence) density and deformation density.
Just play with it or check the Advanced AMSview tutorial.

For example, using a multi-iso surface with clip plane and transparency, atoms reduced in size, using a fine grid, you can create the following picture of the deformation density:

.. image:: /Images/QEMagnetismBandsPDOS/iron-anti-view-deformation.png

In this tutorial you did run the Quantum ESPRESSO calculations on your local machine.
With AMSjobs you can also run jobs on remote machines. In such cases when using AMSview to visualize Quantum ESPRESSO results
the calculation of fields will automatically happen on the remote machine (with AMSview running on your local machine).

You do need to transfer your files to your local machine first!
