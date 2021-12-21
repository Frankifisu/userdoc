.. _AMSREPORT: 
.. index:: amsreport module 

AMSreport: generate report
**************************

The module amsreport is intended to facilitate scripting.
More details on amsreport can be found in the `AMSreport section in the Scripting manual <../Scripting/Commandline_Tools/AMSreport.html>`__.
It makes it very easy to get results calculated by COSMO-RS (or other programs in the ADF suite) in your own script. 
Compared to ADF2014 AMSreport has been extended to get easier results from COSMO-RS result files (.crskf files).
It was already possible to report any proper KF variable from the .crskf file.
Now a few predefined keys are added.
See the $AMSHOME/examples/crs directory for use of amsreport in COSMO-RS calculations.
Depending on the kind of calculation one can use:

::

   Command line option      Property

   TOC                      Table of contents
   PROPERTY                 General:Property

   METHOD                   Property:Method
   NITEMS                   Property:Number of Items
   FRAC1                    Property:Solvent: molar fraction
   FRAC2                    Property:Solvent 2: molar fraction
   SOLVENT-FRACTION         Property:Solvent: solvent fraction
   TEMPERATURE              Property:Temperature (in Kelvin)
   PRESSURE                 Property:Pressure (in bar)
   GIBBS-ENERGY-MIXING      Property:Gibbs free energy of Mixing (in kcal/mol)
   GIBBS-ENERGY-SOLVATION   Property:Gibbs free energy of Solvation (in kcal/mol)
   GIBBS-ENERGY-SOLUTE      Property:Gibbs free energy solute (in kcal/mol)
   EXCESS-G                 Property:Excess Gibbs free energy (in kcal/mol)
   EXCESS-H                 Property:Excess Enthalpy (in kcal/mol)
   ENTHALPY-VAPORIZATION    Property:Enthalpy of vaporization (in kcal/mol)
   LOGP                     Property:LogP
   MOLAR-FRACTION           Property:Molar Fraction
   ACTIVITY-COEFFICIENT     Property:Activity Coefficient
   VAPOR-PRESSURE           Property:Vapor Pressure (in bar)
   SOLUBILITY-X             Property:Solubility: molar fraction
   SOLUBILITY-M             Property:Solubility: moles per liter (in mol/(L solution))
   SOLUBILITY-G             Property:Solubility: gram per liter (in g/(L solution))
   SOLUBILITY-MASS-FRACTION Property:Solubility: mass fraction
   HENRY                    Property:Henry Constant (in mol/(L atm))
   HENRY-NODIM              Property:Henry Constant dimensionless
   MISCIBILITY-GAP          Property:Miscibility gap
   MISCIBILITY-GAP-T        Property:Miscibility gap temperature (in Kelvin)
   MISCIBILITY-GAP-P        Property:Miscibility gap pressure (in bar)
   MISCIBILITY-GAP-X        Property:Miscibility gap molar fraction x1 x1'
   MISCIBILITY-GAP-A        Property:Miscibility gap activities a1 a2
   TIE-LINES-X              Property:Tie Lines molar fraction x1 x2 x3 x1' x2' x3'
   TIE-LINES-A              Property:Tie Lines activities a1 a2 a3
   CHEMICAL-POTENTIAL       Property:Chemical Potential
   CHEMICAL-POTENTIAL-PURE  Property:Chemical Potential Pure Compounds Liquid
   CHEMICAL-POTENTIAL-GAS   Property:Chemical Potential Pure Compounds Gas
   SIGMA                    Property:Sigma
   SIGMA-PROFILE            Property:Sigma Profile
   SIGMA-PROFILE-HB         Property:Sigma Profile Hydrogen Bonding part
   SIGMA-PROFILE-TOTAL      Property:Total Sigma Profile
   SIGMA-PROFILE-HB-TOTAL   Property:Total Sigma Profile Hydrogen Bonding part
   SIGMA-POTENTIAL          Property:Sigma Potential
   SIGMA-POTENTIAL-TOTAL    Property:Total Sigma Potential

   NCOMP                    Compounds:Number of Compounds
   COMPOUNDS-FILENAME       Compounds:Filename
   COMPOUNDS-NAME           Compounds:Name (from filename)
   COMPOUNDS-MOLAR-MASS     Compounds:Molar Mass

   Example
   "$AMSBIN/amsreport" file.crskf TOC
   "$AMSBIN/amsreport" file.crskf ncomp
   "$AMSBIN/amsreport" file.crskf ncomp -plain
