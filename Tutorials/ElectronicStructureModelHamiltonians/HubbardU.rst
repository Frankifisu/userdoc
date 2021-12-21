.. This tutorial has been recorded: examples/tutorials/band-dftu
.. Keep the recording in sync so it may be used to generate the images!

.. _band_Hubbard: 

NiO and DFT+U
*************

This tutorial will show you how to perform a single point calculation with the `DFT+U <../../BAND/Model_Hamiltonians/Density_Functional.html#gga-u>`__ formalism using the `BAND engine <../../BAND/index.html>`__.

Step 1: amsinput
================

.. rst-class:: steps

  \ 
    | **1.** Start AMSinput
    | **2.** Switch to **BAND**: |ADFPanel| **→** |BANDPanel|

.. image:: /Images/HubbardU/amsinput_BAND_Main.png

Step 2: Setup the system - NiO
==============================

You can copy-paste the following information into the AMSinput directly.

::

	2
	 
	Ni    0.000  0.000  0.000
	O     2.085  2.085  2.085
	VEC1  0.000  2.085  2.085
	VEC2  2.085  0.000  2.085
	VEC3  2.085  2.085  0.000

By default, only the central unit cell is shown. To see a few unit-cell repetitions:

.. rst-class:: steps

  \ 
    | Click on **View → Periodic → Repeat Unit Cells** 


Step 3: BP86 without Hubbard
============================

Change the calculation setup (`Unrestricted <../../BAND/Model_Hamiltonians/Relativistic_Effects_and_Spin.html#spin-polarization>`__, `XC functional <../../BAND/Model_Hamiltonians/Density_Functional.html>`__, `basis set <../../BAND/Accuracy_and_Efficiency/Basis_Set.html>`__) as follows:

.. rst-class:: steps

  \ 
    | 1. Check the **Unrestricted** box.
    | 2. Set **XC functional** to **GGA:BP86**.
    | 3. Set **Basis Set** to **TZP**
    | 4. Tick the checkbox **DOS**

.. image:: /Images/HubbardU/Hubbard_2.png

Step 3a: Run the calculation
----------------------------

Now you can save and run the calculation.

.. rst-class:: steps
  
  \ 
    | **File → Save**, give it a name and press Save.
    | **File → Run**

Step 3b: Checking the results
-----------------------------

After the calculation finished, you can check the Output for the 'Band Gap Info'.

.. rst-class:: steps

  \ 
    | **SCM → Output**
    | **Properties → Band Gap Info**

One can see that there is no band gap at all. This contradicts experimental studies, which predict values between 3.7 to 4.3 eV.

.. image:: /Images/HubbardU/BP_Output_BandGapInfo.png

Plotting and examining the partial density of states (pDOS) for this calculation reveals that the d-orbital contributions of Ni are crossing the Fermi level.

.. rst-class:: steps

  \ 
    | **SCM → DOS**
    | Select the **Ni atom**.
    | Choose **Partial → Ni(1) → D-DOS**

.. image:: /Images/HubbardU/Ni_D_DOS_BP.png

Step 4: Run the calculation - BP86+U
====================================

Go back to the Main menu of amsinput, change to HubbardU menu, and apply an U value of 0.6 a.u. to the d-orbitals of the Ni atom.

.. rst-class:: steps

  \ 
    | Go to **Model → HubbardU**.
    | Set for Ni the **l-value** to **d** and the **U** value to **0.6**.


.. image:: /Images/HubbardU/Hubbard_4.png

This will influence the Hamiltonian and results in a state which tries to omit partial occupation or degeneracy w.r.t. the d-orbitals.

Step 4a: Run the calculation
----------------------------

Now you can save and run the calculation. 

.. rst-class:: steps

  \ 
    | **File → Save**, give it a name and press Save.
    | **File → Run**

Step 4b: Checking the results
-----------------------------

After the calculation finished, you can check the Output for the 'Band Gap Info'.

.. rst-class:: steps

  \ 
    | **SCM → Output**
    | **Properties → Band Gap Info**

One can see that there is now a band gap of around 2 eV. This is still less than the experimental values. That can be traced back to the neglection of the correct magnetic behavior of NiO.

.. image:: /Images/HubbardU/BP+U_Output_BandGapInfo.png

Plotting and examining the partial density of states (pDOS) for this calculation reveals that the d-orbital contributions of Ni are no longer crossing the Fermi level. 

.. rst-class:: steps

  \ 
    | **SCM → DOS**
    | Select the **Ni atom**.
    | Choose **Partial → Ni(1) → D-DOS**

.. image:: /Images/HubbardU/Ni_D_DOS_BP+U.png
