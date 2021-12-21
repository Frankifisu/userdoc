.. _metatag ADFCRS: 

AMScrs: COSMO-RS
################

AMScrs is a utility program ($AMSBIN/amscrs), which enables AMS users to easily create COSMO-RS jobs. You can use AMScrs to add compounds, choose the desired property, and to set details of your COSMO-RS job using an easy-to-use graphical user interface. AMScrs will generate the complete job script for you. This script takes care of running COSMO-RS. You can also use AMScrs to run these script files and visualize the results. 

The description of a compound that you want to use should be on a file, and should be a result file of quantum mechanical calculations using COSMO. In ADF such a COSMO result file is called a adf.rkf (.rkf) file, or a COSKF (.coskf) file. AMScrs might also be able to read a result file, for example a .cosmo file, from other programs. 

If you have installed the AMS package correctly, the amscrs command is located in $AMSBIN.  

If $AMSBIN is included in your PATH environment variable, you can start the AMScrs program with the following command: 

amscrs [filename filename2 ...] 

The file names are optional. AMSinput handles files that were created by AMSinput before (which have a .crs or .crskf extension), use only one file name in these cases. One can add multiple files, which correspond to different compounds, if these files contain results of quantum mechanical calculations including COSMO on these compounds. these result files should have .rkf, .t21, .coskf, or .cosmo extension. The file can also be a plain text file with a list of file names (.compoundlist), which contains on each line the filename of a .rkf, .t21, .coskf, or .cosmo file. 

An alternative method to start AMScrs: select the COSMO-RS command from the SCM menu, or use AMSjobs to start AMScrs. 

Under windows you can start AMScrs by  double-clicking the icon on the desktop. 

Menu Commands
*************

File menu
=========

``New``
  Same as quitting AMScrs and starting again without specifying a file name. 

``Open...``
  Open an existing AMScrs file (with .crs) or an AMScrs result file (with .crskf). 

  Same as quitting AMScrs and starting again with specifying a file name. When you open a .crs file AMScrs also tries to add all compounds that are specified in this .crs file and tries to open all .crskf files that belong to this .crs file. If you open a .crskf file only this file is read. 

``Save``
  Save the current state of what is present in AMScrs. If you have not saved before, AMScrs will ask you to specify a file name. 

  A run file will not be saved. 

``Save As...``
  Save the current state of what is present in AMScrs in a file with a name of your choice. 

  A run file will not be saved. 

``Save Runfile``
  Not only the .crs file will be saved, but also a matching .run file which is a run script corresponding to your input (for the selected property). 

``Run``
  Start the COSMO-RS calculation as selected in all the input options. 

  You will first be asked to save the changes. The run script (with the .run extension) for the selected property is created. Next your job is run. When the run is finished the results will be visualized by AMScrs and the .run file will be deleted. 

``Kill``
  Kill the COSMO-RS calculation if one is running. The .run file will be deleted. 

``Close``
  Stop AMScrs, ask you to save changes if you made any. 

Compounds menu
==============

``List of Added Compounds``
  Shows a list of all the added compounds, including a possibility to set some input parameters, specific for a certain compound. 

  On the left side of the window the list of the compounds is given with the full path name to the file from which the quantum mechanical results data are read. Part of this quantum mechanical data is given in the right window for the selected compound. In this right window one can also write some pure compound input data. For ring compounds it is important to write the number of ring atoms. For example, this number should be 6 for benzene. 

``Add Compound(s)``
  Use this menu command to add one or more compounds to the list of compounds. The selected files should be of type: 

  + .compoundlist: List of compounds
  + .coskf: COSMO kf file
  + .rkf .t21: ADF result file
  + .compkf: COMPKF file
  + .cosmo: COSMO file

  The added file(s) should be either ADF result files (.rkf or in previous versions .t21), COSMO kf files (.coskf), COMPKF kf files (.compkf), or ASCII COSMO files (.cosmo). These files should be result files of a quantum mechanical calculation including COSMO, which contains COSMO segment data, or a result of the Fas Sigma prediction (.compkf). In case of ADF the ADF result file (.rkf, .t21 or .coskf) will contain COSMO data if the ADF calculation was done with COSMO. The added file can also be a plain text file with a list of file names (.compoundlist), which contains on each line the filename of a .rkf, .t21, .coskf, or .cosmo file. 

``Compound with multiple forms``
  Use this menu command to make a compound with multiple forms, like conformer(s), dimer(s), trimer(s), dissociated form(s), or associated form(s).

``Install COSMO-RS database...``
  Download and install the COSMO-RS database ADFCRS-2018. 

``Select Compound(s) from COSMO-RS database``
  If the COSMO-RS database was downloaded, it is easy to select with this menu compounds from this database. 

Method menu
===========

The methods and its parameters are described in the  `COSMO-RS manual <../COSMO-RS/index.html>`__. 

``COSMO-RS``
  Select this menu command to set the method that will be used in the calculation to COSMO-RS. 

``COSMO-SAC``
  Select this menu command to set the method that will be used in the calculation to COSMO-SAC. 

``UNIFAC``
  Select this menu command to set the method that will be used in the calculation to UNIFAC. 

``Parameters``
  Change the COSMO-RS or COSMO-SAC parameters and technical parameters that are used in the calculation. The COSMO-RS and COSMO-SAC model have general and element specific parameters.  Technical parameters are, for example, convergence criteria and thresholds. 

Properties menu
===============

How the properties are calculated and definitions used can be found in the  `COSMO-RS manual <../COSMO-RS/index.html>`__. 

``Vapor Pressure Pure Solvents Vapor Pressure Mixture``
  In case of a mixture, the mixture can be composed of of up to five compounds, and the mole fraction of each compound of the solvent should be given, and it should add up to 1. 

  It is possible to calculate the vapor pressure for a temperature range, if the first temperature (from:) is different than the last temperature (to:). 

  One can use input values for the vapor pressure of the pure compounds at a given temperature. These input values can be set by selecting **Compounds → List of Added Compounds**, select the desired compound, and set input values for the pure compound in the right window. If these values are not specified (if they are zero) then they will be approximated using the COSMO-RS method. 

``Boiling Point Pure Solvents Boiling Point Mixture``
  In case of a mixture, the mixture can be composed of of up to five compounds, and the mole fraction of each compound of the solvent should be given, and it should add up to 1. 

  It is possible to calculate the boiling point for a pressure range, if the first pressure (from:) is different than that the last pressure (to:). 

  One can use input values for the vapor pressure of the pure compounds at a given temperature. These input values can be set by selecting **Compounds → List of Added Compounds**, select the desired compound, and set input values for the pure compound in the right window. If these values are not specified (if they are zero) then they will be approximated using the COSMO-RS method. 

``Solvent Flash Point``
  The mixture can be composed of of up to five compounds. The mole fraction of each compound of the solvent should be given, and it should add up to 1. 

  One can use input values for the vapor pressure of the pure compounds at a given temperature. These input values can be set by selecting **Compounds → List of Added Compounds**, select the desired compound, and set input values for the pure compound in the right window. If these values are not specified (if they are zero) then they will be approximated using the COSMO-RS method. However, for the compounds in the solvent the flash points of the pure compounds should be given as input, since COSMO-RS does not calculate these. 

``Activity coefficients``
  The solvent can be a mixture of up to five compounds. The mole fraction of each compound of the solvent should be given, and it should add up to 1. One can use an input value for the density of the solvent instead of a calculated value, which can influence the calculated Henry constants. 

  The activity coefficients will be calculated for the selected compounds in the listbox, on the bottom-left side of the window. Compounds not present in the solvent are considered to be infinitely dilute. 

``Log partition coefficients``
  The log of the partition coefficient (logP) of a solute in 2 phases of a solvent. Both phase 1 and phase 2 can be a mixture of up to three compounds. The mole fraction of each compound in phase 1 and phase 2 of the solvent should be given, and for both phases it should add up to 1. For example, if one wants to calculate partition coefficients for Benzene/Water, which are 2 immiscible liquids, phase 1 of the solvent will be purely Benzene, and phase 2 will be purely Water. Another example is the calculation of partition coefficients for 1-Octanol/Water, which are partly miscible liquids, phase 1 of the solvent will be a mixture of 1-Octanol and Water, and phase 2 will be purely Water (the solubility of 1-Octanol in Water is small). 

  One can use an input value for the quotient of the molar volumes of phase 1 and phase 2 instead of calculated values. 

  The logP will be calculated for the selected compounds in the listbox, on the bottom-left side of the window. Compounds not present in the solvent are considered to be infinitely dilute. 

``Solubility in Pure Solvents Solubility in Mixture``
  In case of pure solvents one can select any number of different pure solvents, but only 1 solute. 

  In case of a mixture, the mixture can be composed of of up to five compounds, and the mole fraction of each compound of the solvent should be given, and it should add up to 1. In this case can select any number of different solutes, but they should not be present in the solvent. In case of a mixture one can also use an input value for density of the solvent. 

  It is possible to calculate the vapor pressure for a temperature range, if the first temperature (from:) is different than the last temperature (to:). 

  For the solubility of a gas in a solvent one has to set the vapor pressure of the gas. 

  For the solubility of a solid compound it is necessary to include the melting point, the enthalpy of fusion, and optionally, since it is often not so important, the :math:`\Delta` heat capacity of fusion of the pure compound (default :math:`\Delta` heat capacity of fusion is zero). These input values can be set by selecting **Compounds → List of Added Compounds**, select the desired compound, and set input values for the pure compound in the right window. 

``Binary mixture VLE/LLE``
  Exactly two compounds should be selected. One can select an isothermal, an isobaric, or a flash point calculation of the binary mixture. The binary mixture will be calculated for a list of molar fractions between zero and one. 

  One can use input values for the vapor pressure of the pure compounds at a given temperature. These input values can be set by selecting **Compounds → List of Added Compounds**, select the desired compound, and set input values for the pure compound in the right window. If these values are not specified (if they are zero) then they will be approximated using the COSMO-RS method. 

``Ternary mixture VLE/LLE``
  Exactly three compounds should be selected. One can select an isothermal, an isobaric, or a flash point calculation of the ternary mixture. The ternary mixture will be calculated for a list of compositions. 

  One can use input values for the vapor pressure of the pure compounds at a given temperature. These input values can be set by selecting **Compounds → List of Added Compounds**, select the desired compound, and set input values for the pure compound in the right window. If these values are not specified (if they are zero) then they will be approximated using the COSMO-RS method. 

``Solvents s1 - s2 Composition Line``
  Linear interpolation between the compositions of solvent 1 and solvent 2, which both could be mixtures. The solvents s1 and s2 can be a mixture of up to five compounds. The mole fraction of each compound of the solvent s1 and s2 should be given, and it should add up to 1. One can select an isothermal, an isobaric, or a flash point calculation. 

  One can use input values for the vapor pressure of the pure compounds at a given temperature. These input values can be set by selecting **Compounds → List of Added Compounds**, select the desired compound, and set input values for the pure compound in the right window. If these values are not specified (if they are zero) then they will be approximated using the COSMO-RS method. 

Solvent Optimizations menu
==========================

``Optimize Solubility``
  Optimize the solvent (mixture) in order to maximize or minimize the mole fraction solubility of a solid solute in the liquid mixture.

``Optimize Liquid-Liquid Extraction``
  Optimize a mixture of immiscible solvents in order to maximize or minimize the distribution ratio (D) of two solutes between the two liquid phases.


Analysis menu
=============

``Sigma Profile Pure Solvents Sigma Profile Mixture``
  The :math:`\sigma`-profile is calculated for COSMO charge densities between minus the maximum value for sigma and the maximum value for sigma. In case of pure solvents one can select any number of different pure solvents. In case of a mixture, the mixture can be composed of of up to five compounds. 

``Sigma Potential Pure Solvents Sigma Potential Mixture``
  The :math:`\sigma`-potential is calculated for COSMO charge densities between minus the maximum value for sigma and the maximum value for sigma. In case of a mixture, the mixture can be composed of of up to five compounds. 

Graph menu
==========

``Graph X Axes``
  Use one of the submenu commands to change the X axes of your graph. 

``Graph Y Axes``
  Use one of the submenu commands to change the Y axes of your graph. 

``Graph Z Colormap``
  Use one of the sub-menu commands to change the colormap of your graph. Only available for **Properties → Ternary Mixture**. 

``Save As PostScript``
  If you have any graphs, you can select one of the graphs. It will be saved in a postscript file. 

``Save As XY``
  If you have any graphs, you can select one of the graphs. It will be saved in a text file as XY pairs. Next you can use most other plotting programs to make the graph just as you want it to be. 

Help Menu
=========

The help menu provides an easy way to get to information about the AMS-GUI. It will start a browser on your local machine, and opens a local copy of the documentation on the SCM web site. 

