.. This tutorial has been recorded: examples/tutorials/band-td-cdft-slab
.. Keep the recording in sync so it may be used to generate the images!

.. _band_TDCDFT_MoS2Monolayer: 

TD-CDFT Response properties for a 2D periodic system (NewResponse)
******************************************************************

`BAND <../../BAND/index.html>`__ can calculate response properties such as the frequency-dependent dielectric function within the theoretical framework of `time-dependent current density function theory (TD-CDFT) <../../BAND/Spectroscopy_and_Properties/Time_Dependent_Current_DFT.html>`__.

This introductory tutorial will show you how to: 

+ Set up and run a **BAND** single point calculation (using **AMSjobs** and **AMSinput**) for an |MoS2| monolayer
+ Set up and run a **BAND** TD-CDFT, linear response calculation (using **AMSjobs** and **AMSinput**) with the ``NewResponse`` method for an |MoS2| monolayer
+ Visualize the dielectric function using **AMSspectra**

If you are not at all familiar with our Graphical User Interface (GUI), check out the :ref:`Introductory tutorial <GO_ETHANOL>` first.

.. _TDCDFT_MoS2Monolayer_CreateSystem: 

Step 1: Create the system
=========================

We now want to **create a** |MoS2| **monolayer**. Let us import the geometry from our database of structures

.. |MoS2| replace:: MoS\ :subscript:`2`\

.. rst-class:: steps

  \ 
    | 1. Open **AMSinput**. 
    | 2. Switch to **BAND**: |ADFPanel| **→** |BANDPanel|
    | 3. Search for **MoS2** in the **search box** |Search|.
    | 4. Select **Crystals → MoS2_Monolayer**. (you have to click on the **triangle** to the right of **Crystals** to expand the list)
    | 5. click on **View → Periodic → Repeat Unit Cells**

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step1_Int0.png
   :figwidth: 90 %
   :align: center

If you succeed, your GUI should resemble the following picture:

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step1.png
   :figwidth: 90 %
   :align: center

Step 2: Run a Singlepoint Calculations (LDA)
============================================

To get an idea regarding the performance of the LDA XC functional for the |MoS2| monolayer, we first run a single-point calculation with the aim of analyzing the resulting band structure. We will already chose the calculation settings to be the same as for the following linear-response calculation with TD-CDFT: e.g. the `basis set <../../BAND/Accuracy_and_Efficiency/Basis_Set.html>`__, the `numerical quality <../../BAND/Accuracy_and_Efficiency/TOC.html>`__, use of `symmetry <../../BAND/Expert_Options/Symmetry.html>`__ and the sampling of `k-space <../../BAND/Accuracy_and_Efficiency/K-Space_Integration.html>`__.

.. rst-class:: steps

  \ 
    | 1. Select the 'BAND Main' panel
    | 2. Change **Basis set** to **DZP**
    | 3. Change **Numerical Quality** to **Basic**
    | 4. Tick the **Calculate band structure** and **Calculate DOS** check-boxes

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step2_Int1.png
   :figwidth: 90 %
   :align: center

.. rst-class:: steps

  \ 
    | 6. Go to **Details → K-Space Integration** and set **Number of points** to '**11 11**'.

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step2_Int2.png
   :figwidth: 90 %
   :align: center

.. rst-class:: steps

  \ 
    | 7. Go to **Details → Symmetry** and de-select the check box **Use of symmetry**

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step2_Int3.png
   :figwidth: 90 %
   :align: center

Now, everything is prepared for the single-point calculation.

.. rst-class:: steps

  \ 
    | 8. **File → Save As...**, use name LDA_SP.ams
    | 9. **File → Run**

With the help of the bandstructure we can validate that basic electronic properties are reproduced by this k-space sampling using only LDA as XC functional. Unlike the multilayered |MoS2|, which has an indirect band gap, the |MoS2| monolayer has a direct band-gap. (see also `Ref <https://doi.org/10.1016/j.ssc.2012.02.005>`__)

.. rst-class:: steps

  \ 
    | 10. **SCM → Logfile**
    | 11. **SCM → Band Structure**

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step2_Int4.png
   :figwidth: 90 %
   :align: center

Step 3: Run an NewResponse Calculation (ALDA)
=============================================

We can now start the calculation of the frequency-dependent, dielectric function using linear response TD-CDFT. As a reasonable frequency range we shall sample from 1.0 eV to 3.0 eV with a step size of 0.1 eV.

.. rst-class:: steps

  \ 
    | 1. Go to the 'BAND Main' panel and uncheck the **Calculate band structure** and **Calculate DOS** boxes.
    | 2. Go to **Properties → Dielectric Function (TD-CDFT)**.
    | 3. Change **Method** to **NewResponse**.
    | 4. Change **Number of frequencies** to **21**.
    | 5. Change **Starting frequency** to **1.0**.
    | 6. Change **End frequency** to **3.0**.
    | 7. Change **Criterion** to **0.1**.
    | 8. Uncheck the 'z'-box regarding **Components**.

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step3_Int1.png
   :figwidth: 90 %
   :align: center

Since we have already calculated the SCF results in the previous run, we can restart the SCF from the band.rkf file (this will save some time during the SCF procedure)

.. rst-class:: steps

  \ 
    | 8. Go to **Details → Restart Details**.
    | 9. Select the band.rkf file located in the folder **LDA_SP.results**
    | 10. Tick the checkbox **SCF** next to **Restart**

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step3_Int2.png
   :figwidth: 90 %
   :align: center

.. tip::
     
  This allows us to split the frequency range into smaller parts without too much of an overhead due to the SCF convergence for the ground state properties. One could even think about restarting from a hybrid DFT calculation with e.g. HSE06.

We are set to run the calculation now:

.. rst-class:: steps

  \
    | 11. **File → Save As...**, use name ALDA_TDCDFT.ams
    | 12. **File → Run**

After the calculation finished, we can analyze the calculated dielectric function by plotting it with **AMSspectra**.

.. rst-class:: steps

  \ 
    | 13. **SCM → Spectra**
    | 14. **Spectra → TD-CDFT → Dielectric Function → XX** (you can move the legend with the mouse by drag and drop it to the desired location)

.. figure:: /Images/TDCDFTMoS2Monolaye/TDCDFT_MoS2Mono_Step3_Int3.png
   :figwidth: 90 %
   :align: center

With respect to the accuracy of our calculation we can reproduce the main features of the dielectric function for this system. We cannot expect the spin-orbit splitting of the first transition at around 1.9 eV to 2.1 eV, since we don't use **Spin-Orbit Relativistic ZORA**. Furthermore, the absolute values of the dielectric function depends on the assumed two-dimensional volume for the surface. Since this definition is arbitrary, we can change the value for the **Volume cutoff**, so that the static dielectric function is reproduced.
