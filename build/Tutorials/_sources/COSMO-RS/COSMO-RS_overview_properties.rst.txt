.. _crs3: 

Overview: properties
********************

How the properties are calculated and definitions used can be found in the section `Calculation of properties <../../COSMO-RS/Calculation_of_properties.html>`__ in the `COSMO-RS manual <../../COSMO-RS/index.html>`__. 

Step 1: Start AMScrs
====================

For this tutorial we assume that you know how start AMScrs and how to add compounds. Like in tutorial 2 we ask you to add the compounds water, methanol, ethanol, and benzene. One can do this, for example, by opening the .crs file that was created in tutorial 2. Save the file as tutorial3.crs. 

.. rst-class:: steps

  \ 
    | Start AMScrs
    | Select **File → Open...**
    | Select 'tutorial2.crs' in the 'Filename' field
    | Select **File → Save As**
    | Enter the name 'tutorial3' in the 'Filename' field

Alternatively on a Unix like system one may copy the COSMO result files (water.coskf, methanol.coskf, ethanol.coskf, and benzene.coskf) in the directory $AMSHOME/examples/COSMO-RS/Parameters_and_Analysis to an empty directory and enter the following command in this directory where the COSMO result files are present: 

::

   $AMSBIN/amscrs benzene.coskf ethanol.coskf methanol.coskf water.coskf &

Note that one has to set the number of ring atoms for the benzene compound.  This is set to the correct value in the benzene ``.coskf`` file in the CRS database, but users will have to set (or estimate) this manually if they generate their own ``.coskf`` file.

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Click on the left side benzene
    | Enter '6' without quotes in the 'Nring' field
    | Select **File → Save As**
    | Enter the name 'tutorial3' in the 'Filename' field

In the compounds window one can also set the vapor pressure of the pure compounds at a given temperature, or set the Antoine parameters. If these values are not specified (if they are zero) then the pure compound vapor pressure will be approximated using the COSMO-RS method. This is relevant, for example, for the calculation of the (partial) vapor pressures of mixtures, calculation of boiling points of mixtures, and calculation of Henry's law constants. 

.. _crsVAPOR: 

Step 2: Vapor pressure
======================

The vapor pressure of a solvent at different temperatures can be calculated with **Properties → Vapor Pressure Pure Solvents** or **Properties → Vapor Pressure Mixture**. 

.. rst-class:: steps

  \ 
    | Select **Properties → Vapor Pressure Pure Solvents**
    | Check the '+' button to add 'methanol'
    | Select unwanted solvents in the the list
    | Check the '-' button to remove these unwanted solvents
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_vaporinput.png
   :width: 10 cm

In this case the result is a table with one entry: 

.. image:: /Images/COSMO-RS_overview_propertie/t3_vaportable.png
   :width: 10 cm

.. rst-class:: steps
  
  \ 
    | Select **Celsius** for the unit of temperature
    | Enter '0.0' without quotes in the 'Temperature from:' field
    | Enter '100.0' in the 'to:' field
    | Press 'Run'

In this case the result is a graph and a table. The graph can be edited to change the general appearance and units.  Graph editing options can be accessed by clicking outside of the plot, so in the area around the left or bottom axes.  Changing a few settings, the graph now looks like the following: 

.. image:: /Images/COSMO-RS_overview_propertie/t3_vaporgraph.png

In this case COSMO-RS predicts a vapor pressure of about 0.61 bar (around 455 Torr) at 323.15 K (50.0 °C) for the pure liquid methanol. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_vaportable2.png
   :width: 10 cm

.. _crsBOILINGPOINT: 

Step 3: Boiling point
=====================

The boiling point of a solvent at different pressures can be calculated with **Properties → Boiling Point Pure Solvents** or **Properties → Boiling Point Mixture**. 

.. rst-class:: steps

  \ 
    | Select **Properties → Boiling Point Mixture**
    | Select '2 components' in the popup menu next to Solvent
    | Select 'methanol' for the first component in the Solvent
    | Select 'ethanol' for the second component in the Solvent
    | Enter '0.5' for the 'Mole fraction' of methanol
    | Enter '0.5' for the 'Mole fraction' of ethanol
    | Select **atm** for the unit of pressure
    | Enter '0.1' in the 'Pressure from:' field
    | Enter '1.0' in the 'to:' field
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_boilinginput.png
   :width: 10 cm

In this case the result (may take several seconds) is a graph and   a table. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_boilinggraph.png

The red curve is the total vapor pressure, the blue curve the partial methanol vapor pressure, and the green curve is the partial ethanol vapor pressure. The table gives the numerical values. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_boilingtable.png

Thus in this case COSMO-RS predicts a boiling point of 339.8 K (66.7 °C) at 1 atm. for this mixture of 50% mole fraction methanol and 50% mole fraction ethanol. At this temperature COSMO-RS predicts that the vapor consists about 69% of methanol. 

Using **Graph → Y Axes →** one can view different properties in the graph, like activity coefficients and excess energies. 

.. _crsFLASHPOINT: 

Step 4: Flash point
===================

The flash point of a mixture can be calculated with **Properties → Flash Point**, if pure compound flash points are given as input. 

Here we mix equal volumes of water (assuming a density of 0.997 kg/L) and ethanol (assuming a density 0.789 kg/L). For a flash point calculation the pure compound flash points are needed as input, since COSMO-RS does not predict pure compound flash points. The AMS COSMO-RS module uses Le Chatelier's mixing rule to calculate the flash point of a mixture. 

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Select 'ethanol'
    | Enter '286' for the 'Flash point' of ethanol
    | Select **Properties → Flash Point**
    | Change the popup menu 'Mole fraction' in 'Mass fraction'
    | Select '2 components' in the popup menu next to Solvent
    | Select 'ethanol' for the first component in the Solvent
    | Select 'water' for the second component in the Solvent
    | Enter '0.442' for the 'Mass fraction' of ethanol
    | Enter '0.558' for the 'Mass fraction' of water
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_flashpointinput.png
   :width: 10 cm

In this case the calculated flash point will be close to 25 °C. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_flashpointtable.png

.. _crsACTIVITIES: 

Step 5: Activity coefficients, Henry coefficients, Solvation free  energies
===========================================================================

The activity coefficients a solvent and the activity coefficients of infinitely diluted solutes in a solvent can be calculated with **Properties → Activity coefficients**. At the same time Henry coefficients and solvation free energies will be calculated. 

.. rst-class:: steps

  \ 
    | Select **Properties → Activity coefficients**
    | Select 'water' for the first component in Solvent
    | Add 'benzene', 'ethanol', and 'methanol' to the list of Solutes
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_activitiesinput.png
   :width: 10 cm

If one does not supply a density of the solvent in the input the program calculates the density of the solvent by dividing the mass of a molecule with its COSMO volume. Note that the calculated activity coefficients do not depend on this density. One may improve the results for the calculation of the Henry constants, by selecting a compound in the **List of Added Compounds**, and include pure a compound vapor pressure at a given temperature. 

The result of the calculation is given in the form of a table. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_activitiestable.png

Relevant for the calculation of the Gibbs free energy of solvation ΔG from the gas phase to the solvated phase is the reference state, used here is 1 mol/L in both phases. 

.. _crsLOGP: 

Step 6: Partition coefficients (log P)
======================================

**Preset Octanol/Water, Benzene/Water, Ether/Water, Hexane/Water**

The partition coefficients (log P) of infinitely diluted solutes in a mixture of two immiscible solvents can be calculated with **Properties → Partition Coefficients (LogP)**. There are presets for the calculation of Octanol/Water, Benzene/Water, Ether/Water, and Hexane/Water partition coefficients. The presets use compounds that are present in $AMSHOME/atomicdata/AMSCRS. First the preset Octanol/Water is used. 

.. rst-class:: steps

  \ 
    | Select **Properties → Partition Coefficients (LogP)**
    | Select 'Preset Octanol-Water' in the popup menu next to Solvent
    | Add 'benzene', 'ethanol', and 'methanol' to the list of Solutes
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_logpinput.png
   :width: 10 cm

In case of partly miscible liquids, like the Octanol-rich phase of Octanol and Water, both components have nonzero mole fractions. The preset also gives a value for the molar volume quotient of the two solvents. 

The result of the calculation is given in the form of a table. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_logptable.png
   :width: 7 cm

**User defined**

A user can also define 2 phases of a mixture of two (or three) immiscible solvents. 

.. rst-class:: steps

  \ 
    | Select **Properties → Partition Coefficients (LogP)**
    | Select 'User Defined 2 components' in the popup menu next to Solvent
    | Select 'benzene' for the first component in the solvent
    | Select 'water' for the second component in the solvent
    | Click the check box 'Use input volume solvent phase 1/phase 2'
    | Enter '4.93' in the 'Use input volume solvent phase 1/phase 2' field
    | Add 'ethanol', and 'methanol' to the list of Solutes
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_logpinput2.png
   :width: 10 cm

Here an input value is used for the volume quotient of the two solvents. If one does not include such value, the program will use the COSMO volumes to calculate the volume quotient. The COSMO volumes can be found by selecting a compound in the **List of Added Compounds**. 

The result of the calculation is given again in the form of a table. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_logptable2.png
   :width: 10 cm

.. _crsSOLUBILITY: 

Step 7: Solubility
==================

The solubility of a solute in a solvent can be calculated with **Properties → Solubility in Pure Solvents** or **Properties → Solubility in Mixture**. The solute can either be a liquid, solid, or gas. 

Solubility liquid in a solvent
------------------------------

First the solubility of benzene in water for a range of temperatures. 

.. rst-class:: steps

  \ 
    | Select **Properties → Solubility in Pure Solvents**
    | Check the '+' button to add 'water'
    | Select 'benzene' for the 'Solute'
    | Enter '273.15' without quotes for the temperature in the 'from:' field
    | Enter '373.15' in the 'to:' field
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_solubilityinput.png
   :width: 10 cm

If a range of temperatures is requested a graph is shown. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_solubilitygraph.png

A major assumption made in here in liquid-liquid solubility calculations is that at the point of liquid-liquid equilibrium, the solute will co-exist in a pure liquid phase.  In many cases, this is an invalid assumption.  This can lead to particularly high errors if the solubility of the solvent in the liquid is high. A better way to calculate liquid-liquid solubility in general is to do a binary mixture calculation and look at the miscibility gap.  An example is given for the calculation of the miscibility gap in the :ref:`binary mixture of Methanol and Hexane <crsMETHANOL_HEXANE>`. 

Note that experimentally benzene is a solid below 5.5 °C, and a gas above 80.1 °C. This has not been taken into account in this case. See the next examples. 

Solubility solid in a solvent
-----------------------------

For the solubility of a solid compound in a liquid, it is necessary to include the melting point, the enthalpy of fusion, and the Δ heat capacity of fusion of the pure compound.  The Δ heat capacity of fusion is optional (and often hard to find experimental numbers for) as it often makes little difference in these calculations. These required values can be input for each compound from the **Compounds → List of Added Compounds** menu. Here, some experimental values will be included for benzene (see, for example, `http://en.wikipedia.org/wiki/Benzene <http://en.wikipedia.org/wiki/Benzene>`__). 

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Click on the left side benzene
    | Enter '278.7' in the 'Melting point' field
    | Enter '2.37' in the 'Δ_fusion H' field

.. image:: /Images/COSMO-RS_overview_propertie/t3_compoundbenzene.png
   :width: 10 cm

Also an experimental value for the density of water will be used: 

.. rst-class:: steps

  \ 
    | Select **Properties → Solubility in Mixture**
    | Select 'water' for the first component in 'Solvent'
    | Check the '+' button to add 'benzene' in the list of Solutes
    | Click the check box 'Use input density solvent (kg/L)'
    | Enter '1.0' in the 'Use input density solvent (kg/L)' field
    | Change one of the popup menu's 'Kelvin' in 'Celsius'
    | Enter '0.0' without quotes in the 'from:' field
    | Enter '10.0' in the 'to:' field
    | Select **Graph → Y Axes → solubility (g/L solvent)**
    | Change the popup menu next to Solutes from 'Liquid' to 'Solid'
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_solubilityinput2.png
   :width: 10 cm

After editing the appearance of the graph, the result looks like the following:

.. image:: /Images/COSMO-RS_overview_propertie/t3_solubilitygraph2.png

Solubility gas in a solvent
---------------------------

For the solubility of a gas one should the change the 'Liquid' popup menu in 'Gas' and enter a partial pressure in the 'Pressure' field. 

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Click on the left side benzene
    | Enter '1.01325' in the 'Pure compound vapor pressure' field
    | Enter '353.3' in the 'at temperature' field
    | Select **Properties → Solubility in Mixture**
    | Select 'water' for the first component in 'Solvent'
    | Check the '+' button to add 'benzene' in the list of Solutes
    | Click the check box 'Use input density solvent (kg/L)'
    | Enter '1.0' in the 'Use input density solvent (kg/L)' field
    | Use 'Kelvin' as unit for the temperature
    | Enter '353.3' without quotes in the 'from:' field
    | Enter '373.15' in the 'to:' field
    | Change the popup menu next to Solutes from 'Solid' to 'Gas'
    | Use 'atm' units for the pressure
    | Enter '1.0' for the partial vapor pressure of benzene
    | Select **Graph → Y Axes → solubility (mol/L solvent)**
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_solubilityinputgas.png
   :width: 10 cm

A graph (and table) is shown, which after some manipulations   could look like: 

.. image:: /Images/COSMO-RS_overview_propertie/t3_solubilitygraphgas.png

The solubility of a gas in a solvent can also be calculated using Henry's law, which is valid for ideal dilute solutions, 

.. rst-class:: steps

  \ 
    | Select **Properties → Activity coefficients**
    | Select 'water' for the first component in Solvent
    | Click the check box 'Use input density solvent (kg/L)'
    | Enter '1.0' in the 'Use input density solvent (kg/L)' field
    | Use 'Celsius' as unit for the temperature
    | Enter '90.0' for 'Temperature'
    | Select only 'benzene' in the list of 'Solutes (infinite dilute)'
    | Press 'Run'

The calculated Henry constant for benzene (infinite dilute) in water will be close to 0.049 mol/(L atm) at 90 °C (363.15 K). 

Note that for benzene in the compounds window the vapor pressure of benzene at 353.3 Kelvin was entered. If these values are not specified (if they are zero) then the vapor pressure will be approximated using only the COSMO-RS method. This is relevant for all properties where the vapor pressure plays a role, thus it is relevant for the calculation of Henry's law constants and relevant for the calculation of the solubility of a gas in a solvent. 

.. _crsBINMIX: 

Step 8: Binary mixtures VLE/LLE
===============================

A phase diagram of a mixture of two components can be calculated with **Properties → Binary Mixture VLE/LLE**. The binary mixture will be calculated for a list of molar fractions between zero and one. This can be done at constant temperature (isothermal) or at constant vapor pressure (isobaric). 

Isothermal
----------

A binary mixture is calculated in which the pure compound vapor pressures are approximated using the COSMO-RS method. 

.. rst-class:: steps

  \ 
    | Select **Properties → Binary Mixture VLE/LLE**
    | Select 'water' for the first compound
    | Select 'methanol' for the second compound
    | Use 'K' as unit for the temperature
    | Enter '298.14' in the 'Temperature' field
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixinput.png
   :width: 10 cm

An activity coefficient plot for water(1) and methanol(2) will be shown. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixactivitycoef.png

The results of the calculation are also given in the form of a table, which shows the molar (and mass) fraction of each compound in the liquid, the activity coefficients, the activities, the temperature, the total and partial vapor pressures, the molar fraction of each compound in the vapor (y), the excess Gibbs free energy G\ :sup:`E` , the excess enthalpy H\ :sup:`E` (calculated with the Gibbs-Helmholtz equation), the excess entropy of mixing -TS\ :sup:`E` , the Gibbs free energy of mixing G\ :sup:`mix` , the enthalpy of vaporization Δ\ :sub:`vap` H (calculated with the Clausius-Clapeyron equation). 

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixtable.png

These values can also be shown in a graph. The property for the x- and y-axes can be selected from the 'Graph' Menu. For example, a graph of the excess energies can be shown by: 

.. rst-class:: steps

  \ 
    | Select **Graph → Y Axes → excess energies**

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixselectexcess.png
   :width: 5 cm

A plot of the excess energies will be shown. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixexcessenergies.png

The red curve is the excess Gibbs free energy G\ :sup:`E` , the   blue curve is the excess enthalpy H\ :sup:`E` , and the green   curve is -T times the excess entropy S\ :sup:`E` . 

Isothermal, input pure compound vapor pressure
----------------------------------------------

A binary mixture is calculated with input data for the pure compound vapor pressures. These can be, for example, experimentally observed pure compound vapor pressures. Note that the calculated partial and total vapor pressures will now depend on these input pure compound vapor pressures. 

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Click on the left side water
    | Enter '0.123416' in the 'Pure compound vapor pressure:' field
    | Enter '322.45' in the 'at temperature:' field

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixpvap.png
   :width: 10 cm

.. rst-class:: steps

  \ 
    | Click on the left side ethanol
    | Enter '0.294896' in the 'Pure compound vapor pressure:' field
    | Enter '322.45' in the 'at temperature:' field
    | Select **Properties → Binary Mixture VLE/LLE**
    | Select 'water' for the first compound
    | Select 'ethanol' for the second compound
    | Enter '322.45' in the 'Temperature' field
    | Select **Graph → X Axes → x2: molar fraction 2**
    | Select **Graph → Y Axes → partial and total vapor pressures**
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixinput2.png
   :width: 10 cm

A vapor liquid equilibrium (VLE) diagram for water(1) and   ethanol(2) will be shown. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixvaporpressures.png

The red curve is the total vapor pressure, the blue curve is the partial water vapor pressure, and the green curve is the partial ethanol vapor pressure. One can also change the x and y axes, for example: 

.. rst-class:: steps

  \ 
    | Select **Graph → X Axes → x2, y2**
    | Select **Graph → Y Axes → total vapor pressure**

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixvle.png

Isothermal, miscibility gap, LLE
--------------------------------

Water and benzene do not mix well, thus there will be a miscibility gap. 

.. rst-class:: steps

  \ 
    | Select **Properties → Binary Mixture VLE/LLE**
    | Select 'water' for the first compound
    | Select 'benzene' for the second compound
    | Use 'Celsius' as units for the temperature
    | Enter '50.0' in the 'Temperature' field
    | Enter '100' for 'Number of mixtures'
    | Press 'Run'


In this case a a liquid-liquid equilibrium (LLE) is calculated. The number of mixtures for which the binary mixture is calculated should be not too small, otherwise the properties of the 2 immiscible liquids phases will not be so accurate. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixmiscibilitygap.png

If the check box **Graph → X axes → force 1 liquid phase within possible miscibility gap** is deselected, then results will be shown in the graph and table only for those compositions of the mixture, which are outside of the miscibility gap. If the check box **Graph → X axes → force 1 liquid phase within possible miscibility gap** is selected, then results will be shown also within the miscibility gap, with the unphysical conditions that the two liquids are forced to mix. 

.. rst-class:: steps

  \ 
    | Deselect check box
    | **Graph → X axes → force 1 liquid phase within possible miscibility gap**
    | Select check box
    | **Graph → X axes → force 1 liquid phase within possible miscibility gap**

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmix1liquid.png
   :width: 5 cm

Isobaric
--------

A binary mixture is calculated in which the pure compound vapor pressures are approximated using the COSMO-RS method if the input values for the pure compound vapor pressures are zero. Alternative one can click a check box in the 'Method' Menu. 

.. rst-class:: steps

  \ 
    | Select **Method → Parameters**
    | Click on the check box 'use input (Compounds Menu) pure compound vapor pressures(s)'
    | to deselect it

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixnotusepure.png
   :width: 10 cm

.. rst-class:: steps

  \ 
    | Select **Properties → Binary Mixture VLE/LLE**
    | Select 'methanol' for the first compound
    | Select 'ethanol' for the second compound
    | Enter '10' for 'Number of mixtures'
    | Select **Isotherm, isobar, flash point → isobar**
    | Select **Graph → X Axes → x1: molar fraction 1**
    | Select **Graph → Y Axes → temperature**
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixinput3.png
   :width: 10 cm

The calculated boiling points (may take several seconds) for a binary mixture of methanol(1) and ethanol(2) will be shown. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixtemperature.png

If one clicks in the graph window at the left or below the axes, a popup window will appear in which one can set details for the graph window. In the graph above the 'Units' for the 'Left Y Axes' were chosen to be 'Celsius'. 

Next the same binary mixture is calculated in which experimental pure compound vapor pressures are used. 

.. rst-class:: steps

  \ 
    | Select **Method → Parameters**
    | Click on the check box 'use input (Compounds Menu) pure compound vapor pressures(s)'
    | to select it

.. image:: /Images/COSMO-RS_overview_propertie/t3_binmixusepure.png
   :width: 10 cm

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Click on the left side methanol
    | Enter '1.01325' in the 'Pure compound vapor pressure:' field
    | Enter '338' in the 'at temperature:' field
    | Click on the left side ethanol
    | Enter '1.01325' in the 'Pure compound vapor pressure:' field
    | Enter '351' in the 'at temperature:' field
    | Select **Properties → Binary Mixture VLE/LLE**
    | Press 'Run'

The calculated graph will not look very different, but it will be more accurate. 

.. _crsTERNARYMIX: 

Step 9: Ternary mixtures VLE/LLE
================================

A phase diagram of a mixture of three components can be calculated with **Properties → Ternary Mixture VLE/LLE**. The ternary mixture plot will be calculated by iterating over possible values of molar (or mass) fractions for each of the compounds. This can be done at constant temperature (isothermal) or at constant vapor pressure (isobaric). 

In this step we will use experimental boiling points as input. 

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Click on the left side water
    | Enter '1.01325' in the 'Pure compound vapor pressure:' field
    | Enter '373.15' in the 'at temperature:' field
    | Click on the left side methanol
    | Enter '1.01325' in the 'Pure compound vapor pressure:' field
    | Enter '338' in the 'at temperature:' field
    | Click on the left side benzene
    | Enter '1.01325' in the 'Pure compound vapor pressure' field
    | Enter '353.3' in the 'at temperature' field
    | Click on the left side ethanol
    | Enter '1.01325' in the 'Pure compound vapor pressure:' field
    | Enter '351' in the 'at temperature:' field

Isothermal
----------

.. rst-class:: steps

  \ 
    | Select **Properties → Ternary Mixture VLE/LLE**
    | Select 'methanol' for the first compound
    | Select 'ethanol' for the second compound
    | Select 'benzene' for the third compound
    | Use 'Mole fraction'
    | Enter '10' for 'Number of mixtures'
    | Select **Graph → X Axes → x1: molar fraction 1**
    | Select **Graph → Y Axes → x2: molar fraction 2**
    | Select **Graph → Z Colormap → total vapor pressures**
    | Select **Isotherm, isobar, flash point → isotherm**
    | Use 'Celsius' as units for the temperature
    | Enter '70.0' in the 'Temperature' field
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_ternarymixinput.png
   :width: 10 cm

The result will be a graph and a table. In the table one can find the results of the calculation at 55 (=(n+1)(n+2)/2, with n=10) different compositions. At those compositions the table shows the molar (and mass) fraction of each compound in the liquid, the activity coefficients, the activities, the temperature, the total and partial vapor pressures, the molar fraction of each compound in the vapor (Y), the excess Gibbs free energy G\ :sup:`E` , the excess enthalpy H\ :sup:`E` (calculated with the Gibbs-Helmholtz equation), the excess entropy of mixing -TS\ :sup:`E` , the Gibbs free energy of mixing G\ :sup:`mix` , the enthalpy of vaporization Δ\ :sub:`vap` H (calculated with the Clausius-Clapeyron equation). 

These quantities can also be shown in the graph as a colormap, in which the color represents the value of the quantity at a certain composition. On the X axes of the graph one can choose the molar (or mass fraction) of one of the compounds, on the Y axes one can choose the molar (or mass fraction) of another compound. The molar (or mass) fraction of the third compound is then fixed, since the sum of the fractions is 1. 

In this case the colormap shows the total vapor pressure: 

.. image:: /Images/COSMO-RS_overview_propertie/t3_ternaryvap.png

One can improve the quality of the graph by increasing the number of compositions. Note that the number of different compositions for n=20 is 231 (=(n+1)(n+2)/2). 

.. rst-class:: steps

  \ 
    | Enter '20' for 'Number of mixtures'
    | Press 'Run'

If one clicks in the graph window at the left or below the axes, a popup window 'Graph details' will appear in which one can set details for the graph window. If one chooses in the 'Z Colormap' part of this popup window as the minimum color magenta, as maximum color red, use 100 as number of colors, and change the minimum and maximum values, then the graph could look like this: 

.. image:: /Images/COSMO-RS_overview_propertie/t3_ternaryvap2.png

Isobaric
--------

Note that isobaric calculations are more expensive than isothermal calculations. Thus the following example takes quite some time, since again for n=20 the number of different compositions is 231. 

.. rst-class:: steps

  \ 
    | Select **Properties → Ternary Mixture VLE/LLE**
    | Select 'water' for the first compound
    | Select 'ethanol' for the second compound
    | Select 'benzene' for the third compound
    | Use 'Mole fraction'
    | Enter '20' for 'Number of mixtures'
    | Select **Isotherm, isobar, flash point → isobar**
    | Use 'bar' as units for the pressure
    | Enter '1.01325' in the 'Pressure' field
    | Select **Graph → X Axes → x1: molar fraction 1**
    | Select **Graph → Y Axes → x2: molar fraction 2**
    | Select **Graph → Z Colormap → temperature**
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_ternarymixinput2.png
   :width: 10 cm

The result will be a graph and a table. Note that this may take some time, since isobaric calculations are more expensive than isothermal calculations. Click in the graph window at the left or below the axes. If one chooses in the 'Z Colormap' part of the 'Graph details' as the minimum color blue, as maximum color red, use 5 as number of colors, change the unit to Celsius, and change the minimum and maximum values, then the graph could look like this: 

.. image:: /Images/COSMO-RS_overview_propertie/t3_ternarytemp.png

In addition to the colormap of the temperature, an approximate miscibility gap of the ternary mixture is shown in the graph. In this case, within the miscibility gap there are two immiscible phases of the liquid in equilibrium. The composition of the two phases, which are in equilibrium, can be found at the end points of the tie line that are drawn. The calculated temperatures within the miscibility gap are calculated with the unphysical condition that the three liquids are forced to mix, thus these calculated temperatures (and other quantities) within the miscibility gap should not be used. By inspection of the graph, one can observe that the calculated minimum boiling point (azeotrope) is around 68 °C. 

.. _crsCOMPOSITIONLINE: 

Step 10: A composition line between solvents s1 and s2
======================================================

A phase diagram of a mixture of two solvents, which both could be mixtures, can be calculated with **Properties → Solvents s1 - s2 Composition Line**. The mixture will be calculated for a list of molar (or mass) fractions of the solvents between zero and one, and the compositions of solvent 1 and solvent 2 are linearly interpolated. This can be done at constant temperature (isothermal) or at constant vapor pressure (isobaric). 

In this step we will try to investigate one of the tie lines of the ternary mixture of water, ethanol, and benzene in more detail. An attempt is made to use the tie line on which ends the calculated minimum boiling point is found, see the tie line which is below the black line in the next picture: 

.. image:: /Images/COSMO-RS_overview_propertie/t3_compositionlinestart.png

The compositions of solvents s1 and s2 are chosen where the black line in the picture above crosses the boundary of possible compositions. This means that solvent s1 and solvent s2 are mixtures of 2 compounds. Again experimental boiling points are used in the calculation. 

.. rst-class:: steps

  \ 
    | Select **Properties → Solvents s1 - s2 Composition Line**
    | Use 'Mole fraction'
    | Select '3 components' in the popup menu next to Solvent
    | Select 'water' for the first compound
    | Select 'ethanol' for the second compound
    | Select 'benzene' for the third compound
    | Enter '0.0' for the mole fraction of compound 1 of solvent s1
    | Enter '0.9' for the mole fraction of compound 1 of solvent s2
    | Enter '0.3' for the mole fraction of compound 2 of solvent s1
    | Enter '0.1' for the mole fraction of compound 2 of solvent s2
    | Enter '0.7' for the mole fraction of compound 3 of solvent s1
    | Enter '0.0' for the mole fraction of compound 3 of solvent s2
    | Enter '100' for 'Number of mixtures'
    | Select **Isotherm, isobar, flash point → isobar**
    | Use 'bar' as units for the pressure
    | Enter '1.01325' in the 'Pressure' field
    | Select **Graph → X Axes → s1_x: molar fraction s1**
    | Select **Graph → Y Axes → pure compound activities**
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_compositionlineinput.png
   :width: 10 cm

The result will be a table and a graph. 

.. image:: /Images/COSMO-RS_overview_propertie/t3_compositionlinegraph.png

The activities of the pure compounds should be equal at the end point of a tie line a\ :sub:`1` = a\ :sub:`1` ',a\ :sub:`2`  = a\ :sub:`2` ', and a\ :sub:`3` = a\ :sub:`3` '. If we look at the graph with close inspection this is approximately true for the molar fraction of solvent s1 with (approximately) s1_x = 0.007 and s1_x' = 0.91. At a molar fraction of 0.91 of solvent s1 the calculated temperature is approximately 67.9 °C (341.05 K). 

Next we will use this temperature of 67.9 °C and look at the Gibbs free energy of mixing. This will also give information about the miscibility gap. 

.. rst-class:: steps

  \ 
    | Select **Isotherm, isobar, flash point → isotherm**
    | Use 'Celsius' as units for the temperature
    | Enter '67.9' in the 'Temperature' field
    | Select **Graph → X Axes → s1_x: molar fraction s1**
    | Select **Graph → Y Axes → Gibbs energy of mixing wrt pure compounds**
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_compositionlineinput2.png
   :width: 10 cm

.. image:: /Images/COSMO-RS_overview_propertie/t3_compositionlinegraphgmix.png

The black line was added to show the miscibility gap more clearly. Indeed at 67.9 °C for molar fractions between s1_x = 0.007 and s1_x' = 0.91, the Gibbs free energy is lower in a system with 2 liquid phases.

Note, that one should use isothermal conditions, if one wants to use the calculated Gibbs free energy of mixing to determine whether there is a miscibility gap. Note also, that no miscibility gap is calculated if one uses **Properties → Solvents s1 - s2 Composition Line**, even if there is one, like in this case. This is because with the calculated values for only 1 composition line between 2 solvents, that involve more than 2 compounds, in general one does not have enough information to determine the exact miscibility gap. 

Step 11: Pure Compound Properties
=================================

A QSPR (Quantitative Structure-Property Relationship) method can be used to estimate some pure compound properties. This QSPR method needs a SMILES string as input.

.. rst-class:: steps

  \
    | Select **Compounds → List of Added Compounds**
    | Click on the left side benzene
    | Press 'Generate' to generate a SMILES string

Openbabel is used to generate a SMILES string for benzene, which should be "c1ccccc1".

.. rst-class:: steps

  \
    | Select **Properties → Pure Compound Properties**
    | Add on the left side benzene
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_benzenepureprop.png
   :width: 10 cm

Step 12: Solvent Optimizations: Optimize Solubility
===================================================

Note that the solvent optimization code has fixed parameters for COSMO-RS: the AMS combi2005 parameter set with the f_corr parameter set to 0.

In this step a solvent is optimized in order to maximize or minimize the mole fraction solubility of a solid solute in the liquid mixture.
A list of pure solvents should be provided.
The optimal solution might be one of the pure solvents, but might also be a mixture of these solvents.
Note that if the optimal solution is a mixture of solvents, no check is done whether these solvents are in fact miscible.
Note that for the solubility of a solid compound it is necessary to include the melting point and the enthalpy of fusion of the solid.
First we try to optimize the solvents, such that it maximizes the solubility (mole fraction) of solid benzene

.. rst-class:: steps

  \
    | Select **Compounds → List of Added Compounds**
    | Click on the left side benzene
    | Enter '278.7' in the 'Melting point' field
    | Enter '2.37' in the 'Δ_fusion H' field
    | Select **Solvent Optimizations → Optimize Solubility**
    | Add 'ethanol', 'methanol', and 'water' to the list of Solvents
    | Select 'benzene' as Solute (Solid)
    | Use 'Maximize' for the Solubility
    | Use 'K' as unit for the temperature
    | Enter '273.15' in the 'Constraint Temperature from:' field
    | Enter '273.15' in the 'to:' field
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_optsolubilitymenu.png
   :width: 10 cm

In this case the pure solvent ethanol is found as optimal solvent

.. image:: /Images/COSMO-RS_overview_propertie/t3_optsolubilitytable.png
   :width: 5 cm

Next we try to optimize the solvents, such that it minimizes the solubility (mole fraction) of solid benzene

.. rst-class:: steps

  \
    | Select **Solvent Optimizations → Optimize Solubility**
    | Use 'Minimize' for the Solubility
    | Press 'Run'

In this case the pure solvent water is found as optimal solvent.

Step 13: Solvent Optimizations: Optimize Liquid-Liquid Extraction
=================================================================

Note that the solvent optimization code has fixed parameters for COSMO-RS: the AMS combi2005 parameter set with the f_corr parameter set to 0.

In this step a mixture of immiscible solvents is optimized in order to maximize or minimize the distribution ratio (D) of two solutes between the two liquid phases. 
A list of pure solvents should be provided. At least two of these solvent should be immiscible with each other.
In this example we try to optimize the mixture of immiscible solvents for liquid-liquid extraction (LLE) of methanol and ethanol.

.. rst-class:: steps

  \
    | Select **Solvent Optimizations → Liquid-Liquid Extraction**
    | Add 'benzene, 'ethanol', 'methanol', and 'water' to the list of Solvents
    | Select 'ethanol' as first Solute
    | Select 'methanol' as second Solute
    | Use 'K' as unit for the temperature
    | Enter '298.15' in the 'Constraint Temperature from:' field
    | Enter '298.15' in the 'to:' field
    | Press 'Run'

.. image:: /Images/COSMO-RS_overview_propertie/t3_optllemenu.png
   :width: 10 cm

In this case the optimized mixture of immiscible solvents is benzene and water.

.. image:: /Images/COSMO-RS_overview_propertie/t3_optlletable.png
   :width: 10 cm
