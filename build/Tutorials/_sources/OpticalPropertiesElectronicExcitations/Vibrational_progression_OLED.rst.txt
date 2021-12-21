.. _ADF_vibrational_progression_OLED:

Vibrational progression of an OLED phosphorescent emitter
*********************************************************

Triplet harvesting in OLEDs by transition metal complexes increases the maximum efficiency from 25% to 100%. Singlet excitons are rapidly converted to triplet excited states and fast phosphorescence can be achieved by strong spin-orbit coupling.
In this example we calculate the frequencies of the T\ :sub:`1` and S\ :sub:`0` state of Pt(4,6-dFppy)(acac) in the gas phase to determine the vibronic fine structure from the Franck-Condon factors. We compare these with the experimental results from the Yersin group, who studied Pt(4,6-dFppy)(acac) in n-octane. [#ref1]_
The sample command line input files can be downloaded :download:`here<../downloads/VibrProg_Pt_OLED_emitter.zip>`.

To calculate the overlap of the vibronic wave functions, we first need to calculate the frequencies of the two electronic states involved, followed by the Franck-Condon calculation. So we have three steps:

#. Optimize the lowest singlet state (S\ :sub:`0`) and calculate frequencies
#. Optimize the lowest triplet state (T\ :sub:`1`) and calculate frequencies
#. Calculation of the Franck-Condon Spectrum

You can start straight away with the :download:`example input<../downloads/VibrProg_Pt_OLED_emitter.zip>`  files or read further to learn how to set up these three calculations in the GUI for your own complexes.

1. Optimize lowest singlet state (S\ :sub:`0`)
==============================================
First, the geometry of the complex (in its lowest singlet state) must be optimized by performing the following steps. (Another basis set and functional can be used as well.)

Remark: Pt(4,6-dFppy)(acac) has C\ :sub:`s`-symmetry. The use of symmetry may speed up the calculation and may improve the analysis of the results.

.. rst-class:: steps

 \
  | **1.** **SCM** → **New Input**
  | **2.** In AMSinput make the complex by copying the :download:`xyz coordinates <../downloads/Pt_OLED_emitter.xyz>`
  | **3.** Click the Symmetrize button |SymmTool|
  | **4.** Select the Task **Geometry Optimization**
  | **5.** Tick the **Frequencies** box
  | **6.** Set the **XC functional** to **GGA:BP86**
  | **7.** Set the **Basis Set** to **TZP**
  | **8.** Set the **Frozen core** to **Small** and the **Numerical quality** to **Good**
  | **9.** Run the calculation (**File** → **Run**)

.. image:: /Images/VibrationalPprogressionOLED/GO_S0.png
  :width: 100%

2. Optimize lowest triplet state (T\ :sub:`1`)
==============================================
For calculating the complex in its T\ :sub:`1` state, the same DFT settings should be applied as for S\ :sub:`0`, but an unrestricted calculation needs to be performed.

Remark: An open shell electronic configuration may break symmetry.
In this case Pt(4,6-dFppy)(acac) also has C\ :sub:`s`-symmetry in the lowest triplet state, as one may check if one looks at the results of the frequency calculation.
In general, however, one may have to break symmetry in the starting geometry, in order to get a non-symmetric optimized geometry.

.. rst-class:: steps

 \
  | **1.** **SCM** → **New Input**
  | **2.** In AMSinput make the complex by copying the :download:`xyz coordinates <../downloads/Pt_OLED_emitter.xyz>`
  | **3.** Click the Symmetrize button |SymmTool|
  | **4.** Select the Task **Geometry Optimization**
  | **5.** Tick the **Frequencies** box
  | **6.** Tick the **Unrestricted** box
  | **7.** Change the **Spin Polarization** to ``2``
  | **8.** Set the **XC functional** to **GGA:BP86**
  | **9.** Set the **Basis Set** to **TZP**
  | **10.** Set the **Frozen core** to **Small** and the **Numerical quality** to **Good**
  | **11.** Run the calculation

.. image:: /Images/VibrationalPprogressionOLED/GO_T1.png
  :width: 60%

.. rst-class:: steps

 \
  | The energy of the T\ :sub:`1` state can be found at the bottom of the logfile or in the output
  | The difference in energy of the  T\ :sub:`1` state with respect to the  S\ :sub:`0` state can be calculated now

This difference in energy should be about 2.5 eV which is in reasonable agreement with the experimental result for the 0-0 transition, which is 21461 cm-1 (2.66 eV) for Pt(4,6-dFppy)(acac) in n-octane. [#ref1]_.

3. Calculation of the Franck-Condon Spectrum
============================================
Next the Franck-Condon spectrum will be calculated. Important is to make a new AMSinput file.

.. rst-class:: steps

 \
  | **1.** **SCM** → **New Input**
  | **2.** On the main panel choose **Properties Only** as the **Task**
  | **3.** Make sure that the **Frequencies** box is ticked
  | **4.** In the panel bar, select **Details** → **Files (Restart)**
  | **5.** Choose in **Properties only for** the results folder of the T\ :sub:`1` calculation (for instance ``T1_GeoFreq.results``)
  | **6.** In the panel bar, select **Properties** → **Franck-Condon Spectrum**
  | **7.** Tick the **Calculate Franck-Condon spectrum** box
  | **8.** Select as the **Reference state** the ``adf.rkf`` file from the S\ :sub:`0` calculation (e.g. in the ``S1_GeoFreq.results`` folder)
  | **9.** In **Quanta reference state** enter ``5`` and in **Quanta current state** enter ``0``
  | **10.** Fill in the **Frequencies** range: from ``-10000``... ``0`` cm\ :sup:`-1`
  | **11.** Run the calculation

.. image:: /Images/VibrationalPprogressionOLED/FCF_settings.png
  :width: 60%

In this example we do not consider vibrational excitations in the T\ :sub:`1` state (i.e. "hot states").
We therefore set the number of quanta for the T\ :sub:`1` state to zero and only allow quanta in the S\ :sub:`0` state.
(The number of 5 quanta in S\ :sub:`0` should be enough the get a converged spectrum, but you can try fewer/more to see if the spectrum changes.)
More information about the calculation of Franck-Condon spectra can be found in the `AH-FC: Adiabetic Hessian Franck-Condon section. <../../AMS/Utilities/FCF_module.html>`__

The output will list the spectral intensity from -10000 cm\ :sup:`-1` to 0 cm\ :sup:`-1` (relative to the 0-0 transition) by taking into account the overlap of the vibronic wavefunction (Franck-Condon factors). The FCF spectrum can be visualized at **SCM** → **Spectra**.
The lines can be Gaussian-broadened to take into account thermal broadening.

.. rst-class:: steps

 \
  | **1.** **SCM** → **Spectra**
  | **2.** **|Axis|** → **Flip Horizontal**
  | **3.** Enter ``300`` for the **Width**
  | **4.** Enter ``21461`` (experimental 0-0 transition) for the **Offset** (makes the spectrum unvisible)
  | **5.** Double-click on the x-axis to open the Graph options window
  | **6.** Enter ``17000`` for Minimum value and ``22500`` for Maximum value
  | **7.** Close with **OK** in Graph options window (spectrum should be visible again)

.. image:: /Images/VibrationalPprogressionOLED/FCspectrum.png
  :width: 60%


References
==========

.. [#ref1] \ A. F. Rausch, M. E. Thompson, H. Yersin, *Triplet state relaxation processes of the OLED emitter Pt(4,6-dFppy)(acac)*, `Chemical Physics Letters 468, 46 (2009) <https://doi.org/10.1016/j.cplett.2008.11.075>`__

