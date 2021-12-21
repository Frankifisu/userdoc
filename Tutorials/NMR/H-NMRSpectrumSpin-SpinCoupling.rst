.. This tutorial has been recorded: examples/tutorials/h-nmr-spin-spin
.. Keep the recording in sync so it may be used to generate the images!

.. _ADF_NMR_H:

H-NMR spectrum with spin-spin coupling
**************************************

Learn how to use the GUI to setup the calculation of NMR chemical shifts and nuclear spin-spin coupling constants (NSSCCs). 
Use the AMSspectra module to inspect the results and compare the simulated and experimental NMR spectra directly.

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-title.png

.. seealso:: 

   + Don't miss this **must-read** `FAQ entry <https://www.scm.com/faq/adf-faq/#what-settings-are-recommended-for-nmr-calculations>`__  on NMR settings based on the work done by the group of `Jochen Autschbach <http://ja01.chem.buffalo.edu/~jochena/>`__  
   + The `NMR part of the ADF manual <../../ADF/Input/NMR.html>`__  contains a neat summary of the science behind `spin-spin coupling calculations <../../ADF/Input/NMR_spin-spin_coupling.html>`__ as well as some additional advice. 
   + The advanced tutorial on `relativistic NMR calculations <https://www.scm.com/adf-modeling-suite/wizard/spectroscopy/nmr-shifts-with-relativistic-dft/>`__ .


Start AMSinput and copy the molecule
====================================

.. rst-class:: steps

  \
    | **1.** Start **AMSinput**
    | **2.** Obtain a pre-optimized ethyl acetate structure by copy-pasting the following coordinates into AMSinput:

::

     O       1.48603879      -1.49561627       0.00000000
     C       1.29751002      -0.30552432       0.00000000
     O       0.07403584       0.25228979       0.00000000
     C      -1.02449892      -0.67494471       0.00000000
     C      -2.30056502       0.12358769       0.00000000
     C       2.36905363       0.74347075       0.00000000
     H      -0.94187587      -1.31519741       0.88039373
     H      -0.94187587      -1.31519741      -0.88039373
     H      -2.36617127       0.75820872       0.88525259
     H      -3.15628689      -0.55419212       0.00000000
     H      -2.36617127       0.75820872      -0.88525259
     H       3.34355252       0.26293272       0.00000000
     H       2.26362714       1.38098693       0.87932777
     H       2.26362714       1.38098693      -0.87932777


.. rst-class:: steps

The above structure was optimized with the following settings:

+ `Hybrid XC  <../../ADF/Input/Density_Functional.html#hybrid>`__: PBE0
+ `Basis <../../ADF/Input/Basis_sets_and_atomic_fragments.html>`__: TZP
+ `Frozen core <../../ADF/Input/Basis_sets_and_atomic_fragments.html>`__: None
+ `Numerical Quality <../../ADF/Input/Precision_and_Self-Consistency.html>`__: Good

In case you want to run the geometry optimization yourself, take a look at the :ref:`GUI tutorial on geometry optimizations. <GO_ETHANOL>`


Setting up the NMR calculation
==============================

Select the following settings in AMSinput

.. rst-class:: steps

  \ 
    | XC functional: **GGA → OPBE**
    | Relativity: **None**
    | Basis set: **J → TZ2P-J** 
    | Frozen core: **None**
    | Numerical quality: **Good**

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-settings-1.png

.. Note::

	The basis sets in ``J``, including TZ2P-J, have been especially designed for ESR hyperfine and NMR spin-spin coupling calculations. 

Next, instruct the program to calculate the shieldings for all hydrogen atoms.

.. rst-class:: steps

  \ 
    | **1.** In the panel bar, select **Properties → NMR**
    | **2.** Click checkbox **H atoms** next to **Shielding for all**
    | **3.** Click checkbox **H atoms** next to **Perturbing / responding all** 
 
.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-settings-2.png

.. Note::

   In some cases, e.g. when dealing with alcohol groups, you might want to exclude atoms from the list of perturbing and responding atoms. 
   To do so, just select the atoms you want to calculate the splittings for, and use the **+** button to add to the list of perturbing and responding atoms manually.

You have now finished the setup of the calculation and are ready to run it. 

.. rst-class:: steps

  \ 
    | **1.** Select **File → Save As** and give it an appropriate name (e.g. 'Ethyl_acetate_NMR')
    | **2.** Select **File → Run**
    | **3.** Wait for the calculation to finish (this can take 5 minutes up to several hours, that highly depends on your hardware)


Results of your calculations
============================

Logfile: AMStail
----------------

You can follow the progress of the calculation by clicking **SCM → Logfile** (AMStail).
The chemical shifts will be calculated first, followed by the couplings constants for the perturbing and responding atoms. 

When the calculation has finished the end of your logfile will look something like this: 

.. figure:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-logfile.png
  :align: center


View the :sup:`1` H-NMR spectrum
--------------------------------

Use AMSspectra to visualize the calculated spectrum

.. rst-class:: steps

  \ 
    | Select **SCM → Spectra**
    | In AMSspectra, set the "Width" to 0.01

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-spectrum-1.png

By default only the chemical shifts are visualized using plain singlets.
To switch on the visualization of couplings:

.. rst-class:: steps

  \
    | Click on the **coupling** checkbox

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-spectrum-2.png

This switches on the spin-spin coupling (default machine frequency at 200 Mhz). 
An additional section in the table will appear which displays additional information for any selected atom or peak in the spectrum. 
For example: 

.. rst-class:: steps

  \
    | Click on the quartet in the spectrum  

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-spectrum-3.png

Average chemical shifts and couplings for equivalent atoms
----------------------------------------------------------

As you may have noticed, there are a lot of splittings in the simulated spectrum. 
This is because all the chemical shifts and coupling constants are calculated at fixed geometry, 
which  means that there is no rotation which would create magnetically equivalent groups.

You can resolve this issue by either flagging chemically equivalent atoms manually or have AMSspectra guess them for you.
To manually supply the information: 

Select groups of chemically equivalent atoms and

.. rst-class:: steps

  \
    | Hold down the **SHIFT** key on your keyboard
    | Use the **left key** of the mouse to select several atoms
    | Press **CTRL+G** or go to **Regions  →  New Region From Selected Atoms** 

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-assign-chem-equivalents.png


The atoms should now be surrounded by a colored sphere. 
Continue with all remaining atoms.  
Your spectrum should look as follows now:

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-regions-assigned.png


**Alternatively**, to have AMSspectra guess chemically equivalent regions for you, go to 

.. rst-class:: steps

  \
    | Click on **NMR** → Chemical Equivalent Regions**

.. tip::

  In the **NMR** menu you can adjust the thresholds that are used by the algorithm to identify equivalent regions.
  
Comparison of calculated and experimental spectrum
--------------------------------------------------

A good source for experimental spectra is the SDBS database: http://sdbs.db.aist.go.jp/sdbs/cgi-bin/direct_frame_top.cgi

These are the peak data for the :sup:`1` H-NMR spectrum of ethyl acetate (CAS = 141-78-6) from the SDBS database (the three columns are **Hz**, **ppm** and **Intensity**)::

      379.88   4.242     52
      372.75   4.163    171
      365.56   4.082    180
      358.50   4.003     62
      182.56   2.039   1000
      119.69   1.337    245
      112.63   1.258    560
      105.38   1.177    214


.. rst-class:: steps

  \
    | Select the peak data above (three columns, all lines with peaks) and copy it ot clipboard (ctrl+c)


Now we switch back to AMSspectra where we can paste the contents from the clipboard directly:

.. rst-class:: steps

  \
    | Activate the AMSspectra window showing the calculated ethanol spectrum
    | **Edit → Paste**

AMSspectra will ask which columns to use for X and Y, and offer to rescale the data:

.. rst-class:: steps

  \
    | Enter ``2`` to use the second column as X values (that column contains the chemical shift in ppm) and click **OK** 
    | Enter ``3`` to use the third columns as Y vales and click **OK**

You now should see both the experimental and the calculated spectrum in one graph.
The experimental spectrum (at least the one used to create this tutorial) was measured at 89.56 MHz.
So adjust the frequency (default at 200 MHz) of the calculated spectrum:

.. rst-class:: steps

  \
    | Change the frequency (next to the Coupling check box)  from 200 MHz to  ``89.56`` MHz

This should give you something like this:

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-comparison.png


Sometimes it makes sense to change one of the spectra to a stick spectrum, showing only sticks for the calculated positions and heights, not applying the broadening.
As an example lets do that here for the calculated peak positions:

.. rst-class:: steps

  \
    | Double click below the X-axes to show the Graph options dialog
    | Click on the Curves tab
    | Select the NMR curve (not the Clipboard one) in the menu on the left
    | For this curve, on the right side: Show the Sticks, and do NOT show the Curve itself
    | Click OK

Now you should get the experimental spectrum as a broadened curve, with sticks for the calculated positions:

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-results-comparison-with-sticks.png

Spectrum overlap
================

If you have an (experimental) spectrum in xy format with the same units as your calculated spectrum, you can calculate and optimize the overlap.
The method used to calculate the overlap is SimIR/VCD from J. Shen et al. Spectrochimica Acta Part A 76 (2010) 418-422.
First, we start with a clean AMSspectra window with our NMR calculation and apply the previous NMR options:

.. rst-class:: steps

  \
    | **1.** Open a **new** AMSspectra window: Select **SCM → Spectra**
    | **2.** In AMSspectra, set the "Width" to 0.01
    | **3.** Tick the Coupling checkbox
    | **4.** Change the frequency from 200 MHz to  ``89.56`` MHz
    | **5.** Click on **Chemical Equivalent Regions** in the **NMR** menu
     
Now we will add an experimental spectrum that has the same units as our calculated spectrum:
 
.. rst-class:: steps

  \
    | **1.** Click :download:`here <../downloads/Ethyl_acetate.xy>` to download the .xy file **Ethyl_acetate.xy**
    | **2.** Add the spectrum: **File →  Add**
    | **3.** Answer 'Yes' when asked to put the spectrum on the left axis

If your spectrum has different units you will want to put it on the right axis, so you can scale it separately. In that case you cannot calculate or optimize the overlap. 
We will now optimize the overlap. The peak width, standard reference (or offset in general), and scaling will be optimized to maximize the overlap between the spectra.
Important to note is that only the current horizontal range is used to optimize the overlap. Specific areas of the spectrum can be optimized this way by limiting the range. The results are immediately applied to the calculated spectrum.

.. rst-class:: steps

  \
    | Optimize the overlap: **Tools →  Optimize SimIR Spectra Overlap**

.. image:: /Images/H-NMRSpectrumSpin-SpinCoupling/nmr-spin-spin-overlap.png

Instead of optimizing the overlap, just the overlap can be shown and updated on the fly when the width, offset, scale or horizontal range are changed.

.. rst-class:: steps

  \
    | Show the overlap: **Tools →  Show SimIR Spectra Overlap**

