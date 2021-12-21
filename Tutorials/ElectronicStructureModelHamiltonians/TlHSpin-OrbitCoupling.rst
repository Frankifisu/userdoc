.. This tutorial has been recorded: examples/tutorials/adf-tlh-spinorbit
.. Keep the recording in sync so it may be used to generate the images!

.. _SPINORBIT_TLH: 

TlH (thallium hydride) Spin-Orbit Coupling
******************************************

This `ADF <../../ADF/index.html>`__ tutorial consists of several steps: 

+ TlH `spin-orbit <../../ADF/Input/Relativistic_effects.html>`__ fragment analysis

+ Separate calculations for Tl and H

+ Visualization of the energy diagram

+ Visualization of spinors

+ Calculate the atomization energy

Prepare the molecule
====================

First create a TlH (thallium hydride) molecule with a bond length of 1.87 Angstrom (the experimental bond length): 

.. rst-class:: steps

  \ 
    | **1.** Open AMSinput and draw a TlH molecule.
    | **2.** Select the Tl and H atoms
    | **3.** Set the bond distance between the atoms to 1.87 Angstrom (i.e. 187 pm)
    | **4.** Click on the Symmetrize tool |SymmTool| (the system should have ``C(LIN)`` symmetry)

.. figure:: /Images/TlHSpin-OrbitCoupling/tlhdistance.png
  :align: center

Set calculation options
=======================

Next we will set up the calculation. The following details need to be set: 

.. rst-class:: steps

  \ 
    | **1.** Clear the selection (click in empty drawing space)
    | **2.** Select the **GGA → BP86** as **XC functional**
    | **3.** Select the **Relativity → Spin-Orbit**
    | **4.** Select the **Basis set  → TZ2P** 
    | **5.** Set **Frozen core → None**

The Main panel will now look like: 

.. figure:: /Images/TlHSpin-OrbitCoupling/tlhoptionsmenu.png
  :align: center

We are going to perform a fragment analysis as a trick to get a diagram that makes it very easy to compare scalar and  spin-orbit relativistic results. 

Fragment calculations are based on regions, which are just collections of atoms. So we start by making a region: 

.. rst-class:: steps

  \ 
    | **1.** Select both atoms
    | **2.** In the **panel bar** select **Model → Regions**
    | **3.** Click the '+' button to add a new region
    | **4.** Change the name of the new region (Region 1) to TlH_SR

.. image:: /Images/TlHSpin-OrbitCoupling/tlh-regions.png

You have now defined a region containing all atoms, with name TlH_SR. 

.. rst-class:: steps

  \ 
    | **1.** In the **panel bar** select **Multilevel → Fragments**
    | **2.** Click the **Use fragments** check box

.. figure:: /Images/TlHSpin-OrbitCoupling/tlh-fragments.png
  :align: center

Run your calculation
====================

.. rst-class:: steps

  \ 
    | **1.** Use the **File → Save** menu command
    | **2.** Enter the name 'TlH_SO' in the 'Filename' field
    | **3.** Click 'Save'

Now you have saved your current options and molecule information. 

As we have set up a fragment calculation, also the .ams and .run files for the fragment have been saved. Lets study what options are used for the fragment in AMSinput: 

.. rst-class:: steps

  \ 
    | **1.** Make sure the **Fragments** panel is still the current panel
    | **2.** Click on the 'Open' button (the dot) for the TlH_SR fragment

A new AMSinput window will also appear with the name 'AMSinput: TlH_SO.TlH_SR.ams'. This is the name of the molecule, a dot, and the name of the fragment. The fragment should have the 'Scalar' relativistic option selected, as that is required when the results will be  used as a fragment. The other options are identical to what you set for the main molecule. 

Now close this AMSinput window: 

.. rst-class:: steps

  \ 
    | **1.** Select the AMSinput window with the name 'AMSinput: TlH_SO.TlH_SR.ams'
    | **2.** Select **File → Close**

We are now ready to run the calculation: 

.. rst-class:: steps

  \ 
    | **1.** Select the AMSinput window with the name 'TlH_SO.ams.
    | **2.** Select **File → Run**

Now two calculations will run: first the building fragment (using the scalar relativistic option), and next the version including spin-orbit coupling. You will see the two logfiles.

.. rst-class:: steps

  \ 
    | Wait until both calculations have finished.


Results of the calculation
==========================

TlH energy diagram
------------------

To see the effect of the spin-orbit coupling we will first look at the energy level diagram: 

.. rst-class:: steps

  \ 
    | **1.** Select the AMSinput window with the name 'TlH_SO.ams.
    | **2.** **SCM → Levels**
    | **3.** Select **View → Labels → Show**
    | 
    | **4.** In AMSlevels, **right-click on the right stack** and select **Zoom HOMO-4 .. LUMO+4**.
    | **5.** You can move the levels vertically by dragging with the left mouse button and you can zoom using using the scroll wheel.

.. image:: /Images/TlHSpin-OrbitCoupling/tlhsolevels.png

You can see that the spin-orbit coupling is important to split energy levels. 

Especially for the Tl core levels the spin-orbit coupling is more important than the ligand field splitting. Compare the 8pi, 13sigma, 4delta orbitals (close to 5d atomic Tl orbitals) with the 11j3/2, 20j1/2 spinors (close to 5d3/2 atomic Tl spinors) and 5j5/2, 12j3/2, and 21j1/2 spinors (close to 5d5/2 atomic Tl spinors). 

If you press and hold the right mouse button on one of the levels, you can select a spinor. That spinor will be shown. You can also show all spinors (in the case of a degenerate level) at once. 

The energy diagram of the scalar relativistic fragment calculation shows the atomic contributions to the scalar relativistic levels.  

.. rst-class:: steps

  \ 
    | **1.** Bring AMSjobs to the front
    | **2.** Select the TlH_SO.TlH_SR job (the scalar relativistic fragment)
    | **3.** Use the **SCM → levels** command
    | **4.** Select **View → Labels → Show**
    | **5.** **Right-click on the central stack** and select **Zoom HOMO-4 .. LUMO+4**.
    | **6.** Next zoom and move the levels using a right mouse drag and or scroll wheel.

.. image:: /Images/TlHSpin-OrbitCoupling/tlhsrlevels.png

Visualization of spinors
------------------------

Visualization of spinors is conceptually  more difficult than visualization of orbitals. 

A spinor :math:`\Psi` is a two-component complex wave function, which can be described with four real functions :math:`\phi`: real part :math:`\alpha` :math:`\phi_\alpha^R` , imaginary part :math:`\alpha` :math:`\phi_\alpha^I` , real part :math:`\beta` :math:`\phi_\beta^R` , imaginary part :math:`\beta` :math:`\phi_\beta^I`: 

.. math::

   \Psi = \binom{\phi_\alpha^R + i \phi_\alpha^I}{\phi_\beta^R + i \phi_\beta^I}
   
The density :math:`\rho` is: 

.. math::

   \rho = \Psi^\dagger \Psi

The spin magnetization density :math:`m` is: 

.. math::

   m = \Psi^\dagger \sigma \Psi

where :math:`\sigma` is the vector of the Pauli spin matrices :math:`\sigma_x`, :math:`\sigma_y`, and :math:`\sigma_z`. A spinor is fully determined by the spin magnetization density and a phase factor :math:`e^{i \theta}`, which both are functions of spatial coordinates. 

In AMSview one can visualize the (square root of the) density and spin magnetization density, however, the phase factor :math:`e^{i \theta}`  is summarized only with a plus or minus sign. 

For this tutorial we have a small molecule, and a fine grid is chosen for better visualization. 

.. rst-class:: steps

  \ 
    | **1.** Select the AMSinput window with the name 'TlH_SO.ams.
    | **2.** Select **SCM → View**
    | **3.** Rotate the molecule, such that one can see both atoms.
    | **4.** Select **Fields → Grid → Fine**
    | **5.** Select **Add → Spinor: Spin Magnetization Density**
    | **6.** In the new control line at the bottom, use the field select pull-down menu and
    | **7.** Select **Orbitals (occupied) ...**.
    | **8.** Select the **J1/2:1 number 22** spinor.

.. image:: /Images/TlHSpin-OrbitCoupling/tlh22j1.png

The arrows in this picture are in the direction of the spin magnetization density **m**. All arrows are approximately in the same direction, which means that this spinor is an eigenfunction of spin in this direction of the arrows. In fact this 22 j1/2 spinor is almost a pure :math:`\alpha` orbital. The arrows are drawn starting from points in space where the square root of the density is 0.03. The color of the arrows is red or blue by default, indicating minus or plus for the phase factor :math:`e^{i \theta}` . 

The (square root of the) density and the approximate phase vector :math:`e^{i \theta}`  can also be viewed separately: 

.. rst-class:: steps

  \ 
    | **1.** Select **Add → Isosurface: With Phase**
    | **2.** Select **Orbitals (occupied)...**
    | **3.** Select the **SCF_J1/2:1  number 18** spinor.
    | **4.** Hide the spinor (uncheck the check box at the left of the Spinor label)

.. image:: /Images/TlHSpin-OrbitCoupling/tlh18j1.png

This spinor 18j1/2 is almost a pure 5p1/2 Tl spinor. A p1/2 atomic orbital has a spherical atomic density, but a spin magnetization density which is not the same in each point in space. 

.. rst-class:: steps

  \ 
    | **1.** In the control line with 'Spinor', press on the pull-down menu and
    | **2.** Select **Orbitals (occupied)**
    | **3.** Select the SCF_J1/2:1  number 18 spinor
    | **4.** Show the 'Spinor' (check the left check box for the spinor line)
    | **5.** Hide the 'isosurface with phase' (uncheck the left check box for the isosurface with phase line)
    | **6.** Hide the atoms: **View → Molecule → Sticks**

.. image:: /Images/TlHSpin-OrbitCoupling/tlh18j1vec.png

Calculate the atomization energy including spin-orbit coupling
==============================================================

The calculation of the atomization energy is not a simple problem in DFT. Spin-orbit coupling is an extra complication. In this paragraph a way is presented how to calculate the atomization energy using spin-polarized calculations in the non-collinear approximation. 

If you wish, you can skip the rest of this tutorial. 

The Tl atom
-----------

To calculate an atomization energy we need to calculate the atoms also including spin-orbit coupling. The easiest way is to start with the TlH_SO.ams file and change this to an atomic file. 

Since the Tl atom is an open shell atom for an (accurate) atomization energy we need to do an unrestricted calculation. The best theoretical method is the non-collinear method. Note that the 'Spin polarization' field is not used in the non-collinear method. 

.. rst-class:: steps

  \ 
    | Select the AMSinput window with the name 'TlH_SO.ams
    | Use the panel bar **Multilevel → Fragments** command
    | Uncheck the 'Use fragments' option
    | Delete the H atom (select it and press the backspace key)
    | Use the panel bar **Model → Regions** command
    | Remove the TlH_SR region (click on the - button in front of it)
    | Select 'Main' panel
    | Check the 'Unrestricted:' box
    |  
    | Select the Relativity panel (search for 'relativity' in the search box |Search|)
    | Select 'NonCollinear' from the 'Spin polarization' options
    | Select **File → Save As**
    | Enter the name 'Tl_SO' in the 'FileName' field
    | Click on 'Save'

.. figure:: /Images/TlHSpin-OrbitCoupling/noncollinearmenu.png
  :align: center

Now we want to actually perform the calculation for the Tl atom 

.. rst-class:: steps

  \ 
    | Run the calculation: **File → Run**
    | Wait until the calculation is finished

The H atom
----------

Basically we can follow the same steps as for the Tl atom, but in this case we will start with Tl_SO.ams file and change this. 

.. rst-class:: steps

  \ 
    | Select the AMSinput window with the name 'Tl_SO.ams
    | Select the 'Main' panel
    | Select the Tl atom
    | Use the **Atoms → Change Atom Type → H**
    | Select **File → Save As...**
    | Enter the name 'H_SO' in the 'Filename' field
    | Click on 'Save'
    | Select **File → Run**
    | Wait until the calculation is finished

TlH atomization energy
----------------------

The atomization energy including spin-orbit coupling is a combination of several terms. 

.. rst-class:: steps

  \ 
    | Select the AMSinput window with the name 'TlH_SO.ams'.
    | Select **SCM → Logfile**
    | Write down the value of the bonding energy printed at the end of the calculation
    | in the AMStail window.  (should be around -1038.62 eV)
    | Select **File → Open**
    | Select the file 'TlH_SO.TlH_SR.logfile'
    | Write down the value of the bonding energy printed at the end of the calculation
    | in the AMStail window.  (should be around -3.84 eV)
    | Select **File → Open**
    | Select the file 'Tl_SO.logfile'
    | Write down the value of the bonding energy printed at the end of the calculation
    | in the AMStail window.  (should be around -1039.32 eV)
    | Select **File → Open**
    | Select the file 'H_SO.logfile'
    | Write down the value of the bonding energy printed at the end of the calculation
    | in the AMStail window.  (should be around -0.95 eV)

The atomization energy including spin-orbit coupling is in this case, the bond energy printed in the TlH_SO.logfile plus the the bond energy printed in the TlH_SO.TlH_SR.logfile minus the bond energy printed in the Tl_SO.logfile minus the the bond energy printed in the H_SO.logfile. (approximately -1038.62 - 3.84 + 1039.32 + 0.95 = -2.19 eV, experimental number is close to -2.06 eV.) 

