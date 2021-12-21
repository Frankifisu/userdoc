.. This tutorial has been recorded: examples/tutorials/vcd-oxirane
.. Keep the recording in sync so it may be used to generate the images!

.. _VCDtools:

Analysis of the VCD spectrum of Oxirane with VCDtools
*****************************************************

This tutorial will teach you how to calculate and analyze the `vibrational circular dichroism (VCD) <../../AMS/Vibrational_Spectroscopy.html#vcd-vibrational-circular-dichroism>`__ spectrum of a small molecule using `ADF <../../ADF/index.html>`__ and `VCDtools <../../AMS/Utilities/VCDtools.html>`__.

Create your oxirane molecule
============================

These are the coordinates of the oxirane molecule::

    C      -1.44589917      -0.26968372      -0.00000000
    C       0.02774960      -0.35459913      -0.00000000
    O      -0.64012001       0.88449058      -0.00000000
    H      -1.94641916      -0.41741698       0.97962259
    H      -1.94641916      -0.41741698      -0.97962259
    H       0.50817848      -0.55867470      -0.97957478
    H       0.50817848      -0.55867469       0.97957478

Copy-paste these into AMSinput:

.. rst-class:: steps

  \
    | **1.** Start **AMSinput**
    | **2.** Select the oxirane coordinates above, and **copy** and **paste** in the molecule drawing area of AMSinput

Now you should have the oxirane molecule. 

.. figure:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane.png
  :align: center

To ensure chirality, two hydrogen atoms should be changed to deuterium atoms:

.. rst-class:: steps

  \
    | **1.** Select two hydrogen atoms diagonally across from each other (holding shift)
    | **2.** In the menu bar: **Atoms → Details (Color, Radius, Mass)** command

The panel area changes to display the atom details menu.
 
.. rst-class:: steps

  \
    | Set the **Mass** of the two selected Hydrogens to 2

.. image:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane-deuterated.png

Note that if the two other hydrogen atoms are changed to deuterium atoms then one has the mirror image of this molecule, and one would get an inverse VCD spectrum.

Set up and run the calculation
==============================

We will perform a `geometry optimization <../../AMS/Tasks/Geometry_Optimization.html>`__ followed by `frequency <../../AMS/Vibrational_Spectroscopy.html#ir-frequencies-and-normal-modes>`__ + `VCD <../../AMS/Vibrational_Spectroscopy.html#vcd-vibrational-circular-dichroism>`__

.. rst-class:: steps

  \
    | **1.** Click on the **Main** tab in the **panel bar**.
    | **2.** Select **Task → Geometry Optimization**
    | **3.** Check the **Frequencies** check-box
    | **4.** Select **GGA:BP86** as **XC functional**
    | **5.** Select **Frozen Core → None**

.. figure:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane-input.png
    :align: center

To request the calculation of VCD intensities:

.. rst-class:: steps

  \
    | **1.** In the **panel bar**, select **Properties → IR (Frequencies), VCD**
    | **2.** Check the **VCD** check-box

.. figure:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane-vcdinput.png
    :align: center

Now run ADF:

.. rst-class:: steps

  \
    | **1.** Select the **File → Run** command
    | **2.** In the file select box, choose a name for your file ("Oxirane") and click 'Save'

Now ADF will start automatically, and you can follow the calculation in the logfile.


.. rst-class:: steps

  \
    | **1.** Wait until the calculation is finished (should take a minute or so)
    | **2.** Click 'Yes' when asked if you want to update the coordinates


Analyze the VCD Spectra
=======================

Next start analyzing the VCD spectrum with AMSspectra. To open the spectra:  

.. rst-class:: steps

  \
    | **SCM → Spectra**

Basically, two types of analysis methods are offered by the analysis program `VCDtools <../../AMS/Utilities/VCDtools.html>`__.
First, it can visualize the properties relevant for the VCD intensity, *i.e.*, the **Electric and Magnetic Dipole Transition Moments (EDTM and MDTM)** and the normal mode motion. 
Second, a **General Coupled Oscillator (GCO)** analysis can be performed. 

Normal modes can be selected either by clicking in the spectrum or by clicking in the *'Vibrations Window'*. 
After a normal mode is selected the vibration will be shown in the molecule and some details will be given in the right side of the *'Vibrations Window'*. 
In the next picture '1/cm' is chosen as horizontal unit, with a 'Lorentzian Height' line shape and a width of '8.0'.

.. image:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane-spectrum.png

.. rst-class:: steps

  \
    | Select normal mode 15, a large positive peak at 3100 wavenumbers
    | In the '*Vibration Window*'' click the header **EDTM** to sort the atoms accordingly.
    | Click on the row with the highest electric dipole transition moment. 

 
Now one of the hydrogens should be selected. 
In general, atoms with a high contribution to the EDTM are important for the VCD intensity. 
To show this a GCO analysis will be performed in the following.

.. rst-class:: steps

  \
    | Select the **VCDtools →  Default Visualization for GCO Analysis**

.. image:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane-scaleedtm.png

The atom sizes are now scaled by their EDTM and the nuclear displacement vectors are shown as arrows. 
To scale the size of these arrows, use the "*up*" and "*down*" keys.
Using these visualization settings, we immediately see that two of the C-H groups are important for the VCD signal in this normal mode.
You can change which vectors are visualized, the phase of these vectors and the scaling of the atoms by clicking the buttons under need the molecule. 
The buttons that are active will have a glow effect. 

The next step in a GCO analysis is to select VCD active fragments: 

.. rst-class:: steps

  \
    | Select one of the important C-H groups by pressing the 'shift button' while clicking on the atoms. 
    | Select the **Regions → Set Selection As → New Region** command
    | Select the other important C-H group
    | Select the **Regions → Set Selection As → New Region** command again

.. image:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane-regions.png

The two important regions will be highlighted by transparent red and green spheres. 
Additional tools for setting up the regions can be found under the “*Regions*” menu. 

.. rst-class:: steps

  \
    | Select the **Regions → Save Regions** command
    | Enter a Name (for example *'NM15'*)
    | Press the *'Return'* -key or press save

The current regions will have been saved in the *'.results/adf.results'* folder in the file 'Regions.txt' and can be loaded by the command: **Regions → Load Regions → 'Name'**.

To determine whether the coupling between two important C-H groups is important to the rotational strength it can be decomposed using the GCO formalism.

.. rst-class:: steps

  \
    | Click the **GCO analysis** button with the text *'GCO'*

.. image:: /Images/AnalysisOfVCDSpectrumOfOxirane/oxirane-vcdtoolsout.png

An *'AMStail'* window will now have opened showing the *'vcdtools.txt'* file.
In this file all output from VCDtools is stored. Each output entry begins by defining the settings such as the selected regions and normal modes. 
For normal mode 15 we see that indeed the major part of the VCD signal is caused by the GCO interaction between the two selected regions. The rest of the molecule barely contributes and also the VCD signal from the individual fragments is insignificant. 
We have thus successfully determined the source of the VCD intensity for normal mode 15.

If needed arrows can be shown inside the molecule to indicate the EDTM and the MDTM. This can be done per atom or per regions. 
For example:

.. rst-class:: steps

  \
    | Select the **VCDtools → EDTM Vectors (regional)** command

Two arrows will have appeared at the geometric centers of the regions displaying the relative size and direction of the EDTMs. 

Under the "**VCDtools**" menu there are many other commands.
For example, VCDtools can guess the best fragments for GCO fragments and can compute the normal mode localization on the selected regions within the molecule.
Feel free to test them out. 
