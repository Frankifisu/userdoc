
Properties
**********

.. _metatag VAPOR_PRESSURE: 
.. index:: solvent vapor pressure 
.. index:: vapor pressure

Vapor pressure
==============

The vapor pressure of a mixture can be calculated with: 

.. _keyscheme PROPERTY_vaporpressure: 

::

   PROPERTY vaporpressure
   End

In case of a mixture the mole fraction of each compound of the solvent should be given with the subkey  FRAC1 of the key COMPOUND for each compound. In case of a mixture also activity coefficients, and excess energies are calculated. 

To calculate pure compound vapor pressures for more than one compound use: 

.. _keyscheme PROPERTY_purevaporpressure: 

::

   PROPERTY purevaporpressure
   End

It is possible to calculate the vapor pressure for a temperature range, see key TEMPERATURE. 

The input pure compound vapor pressure will be used in the calculation of the vapor pressure of this compound if it is supplied with the key COMPOUND for this compound. If it is not specified then it will be approximated using the COSMO-RS method. 

**Links** COSMO-RS GUI tutorial: solvent vapor pressure [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-2-vapor-pressure>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#parametrization-of-adf-cosmo-rs-ghydr-vapor-pressures-partition-coefficients>`__] 

.. _metatag BOILING_POINT: 
.. index:: solvent boiling point 
.. index:: boiling point

Boiling point
=============

The boiling point of a mixture can be calculated with the block key: 

.. _keyscheme PROPERTY_boilingpoint: 

::

   PROPERTY boilingpoint
   End

In case of a mixture the mole fraction of each compound of the solvent should be given with the subkey  FRAC1 of the key COMPOUND for each compound. In case of a mixture also activity coefficients, and excess energies are calculated. 

To calculate pure compound boiling points for more than one compound use: 

.. _keyscheme PROPERTY_pureboilingpoint: 

::

   PROPERTY pureboilingpoint
   End

It is possible to calculate the boiling temperature for a pressure range, see key PRESSURE. 

The input pure compound vapor pressure will be used in the calculation of the vapor pressure of this compound in the mixture if it is supplied with the key COMPOUND for this compound. If it is not specified then it will be approximated using the COSMO-RS method. 

The COSMO-RS calculation of the boiling temperature of a solvent is performed with an iterative method. The temperature is varied until the calculated vapor pressure is within a certain threshold of the desired pressure. 

**Links** COSMO-RS GUI tutorial: boiling point of a solvent [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-3-boiling-point>`__] 

.. _metatag FLASH_POINT: 
.. index:: solvent flash point 
.. index:: flash point

Solvent flash point
===================

The flash point (lower flammable limit) of a compound is the lowest temperature at which the vapor of the compound forms an ignitable mixture in air. The COSMO-RS module can calculate the flash point of a mixture. The COSMO-RS module, however, does not calculate or predict the flash point of pure compounds. The COSMO-RS method is used to calculate the partial vapor pressures of each compound in the mixture, and it uses Le Chatelier's mixing rule to calculate the flash point of this mixture in the gas phase. Input pure compound flash points should be provided by the user, with the subkey FLASHPOINT flashpoint of the key COMPOUND. 

.. _keyscheme PROPERTY_flashpoint: 

::

   PROPERTY flashpoint
   End

The mole fraction of each compound of the solvent should be given with the subkey  FRAC1 of the key COMPOUND for each compound. 

.. _metatag LOGP: 
.. index:: partition coefficients 
.. index:: log P
.. index:: Octanol/Water partition coefficients

Partition coefficients (LogP)
=============================

The partition coefficient of a compound in a mixture of two immiscible solvents, can be calculated with: 

.. _keyscheme PROPERTY_logp: 

::

   PROPERTY logp
   {VOLUMEQUOTIENT volumequotient}
   End

``volumequotient``
   If the subkey VOLUMEQUOTIENT is included the volumequotient will be used for quotient of the molar volumes of solvent 1 and solvent 2 instead of calculated values. 

The mole fraction of each compound of the solvent 1 and solvent 2 should be given with the subkey  FRAC1 and subkey FRAC2 of the key COMPOUND for each compound, respectively. In case of partly miscible liquids, like, for example, the Octanol-rich phase of Octanol and Water, both components have nonzero mole fractions.  The compounds that are included without a given mole fraction are considered to be infinite diluted solutes. The partition coefficients are calculated for all compounds. 

One can use some compounds that are present in $AMSHOME/atomicdata/ADFCRS (Water, 1-Octanol, Benzene, Ethoxyethane, Hexane), or one can use compounds from the ADFCRS-2010 database. For example, for Octanol/Water partition coefficients one can use: 

::

   Property logp 
     VolumeQuotient 4.93
   End
   Compound "$AMSHOME/atomicdata/ADFCRS/1-Octanol.coskf" 
     frac1 0.725 
   End 
   Compound "$AMSHOME/atomicdata/ADFCRS/Water.coskf" 
     frac1 0.275 
     frac2 1.0 
   End

**Links** COSMO-RS GUI tutorial: partition coefficients (log P) [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-6-partition-coefficients-log-p>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#parametrization-of-adf-cosmo-rs-ghydr-vapor-pressures-partition-coefficients>`__], Octanol-Water partition coefficients (log P\ :sub:`OW` ) [`1  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#octanol-water-partition-coefficients-log-pow>`__] 

.. _metatag ACTIVITY_COEFFICIENTS: 
.. index:: activity coefficients 
.. index:: Henry's law constants 
.. index:: solvation energies
.. index:: pKa values
.. index:: infinite dilute

Activity coefficients solvent and solute
========================================

The mole fraction of each compound of the solvent should be given with the subkey  FRAC1 of the key COMPOUND for each compound. The compounds that are included without a given mole fraction are considered to be infinite diluted solutes. The activity coefficients are calculated for all compounds. 

.. _keyscheme PROPERTY_activitycoef: 


::

   PROPERTY activitycoef
   {DENSITYSOLVENT densitysolvent}
   End

``densitysolvent``
   If the subkey DENSITYSOLVENT is included the densitysolvent will be used for the density of the solvent (kg/L) instead of calculated values. Relevant for the calculation of the Henry's law constant. 

The input pure compound vapor pressure will be used in the calculation of the partial vapor pressure of this compound in the mixture if it is supplied with the key COMPOUND for this compound. If it is not specified then it will be approximated using the COSMO-RS method. Relevant for the calculation of the Henry's law constant. 

The Henry's law constants are calculated in 2 units. The Henry's law constant k\ :sub:`H`  is the ratio between the liquid phase concentration of a compound and its partial vapor pressure in the gas phase. The dimensionless Henry's law constant k\ :sub:`H` \ :sup:`cc`  is the ratio between the liquid phase concentration of a compound and its gas phase concentration. 

Also calculated is :math:`\Delta G_{solv}^{liq-solv}` , which is the solvation Gibbs free energy from the pure compound liquid phase to the solvated phase, and :math:`\Delta G_{solv}^{gas-solv}` , which is the solvation Gibbs free energy from the pure compound gas phase to the solvated phase, with a reference state of 1 mol/L in both phases. In addition a Gibbs free energy is calculated which is the free energy of the solvated compound with respect to the gas phase energy of the spin restricted spherical averaged neutral atoms, the compound consist of. Note that zero-point vibrational energies are not taken into account in the calculation of this free energy. This energy could be used in the calculation of :math:`pK_a` values. 

**Links** COSMO-RS GUI tutorial: activity coefficients [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-5-activity-coefficients-henry-coefficients-solvation-free-energies>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#large-infinite-dilution-activity-coefficients-in-water>`__], solvation free energies [`1  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#parametrization-of-adf-cosmo-rs-ghydr-vapor-pressures-partition-coefficients>`__], Henry's law constants [`1  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#henry-s-law-constants>`__], :math:`pK_a` values [`1  <../Tutorials/COSMO-RS/pKa_values.html>`__]     

.. _metatag SOLUBILITY: 
.. index:: solubility

Solubility 
==========     

The solubility of solutes in 1 mixture can be calculated with:     

.. _keyscheme PROPERTY_solubility: 

::

  PROPERTY solubility    
  End     

The mole fraction of each compound of the solvent should be given with the subkey  FRAC1 of the key COMPOUND for each compound, and should add up to 1.0. The solutes should have zero molar fraction in the solvent.   The solubility of 1 solute in pure solvents can be calculated with     

.. _keyscheme PROPERTY_puresolubility: 

::

  PROPERTY puresolubility    
  End     

The mole fraction of each pure solvent should be 1.0, and should be set the subkey  FRAC1 of the key COMPOUND for each compound. The solute should have zero molar fraction in the solvent.   It is possible to calculate the solubility of a solute at a temperature range, see key TEMPERATURE.   

For solubility calculations of a solid compound one should add the pure compound melting point :math:`T_m` , pure compound enthalpy of fusion :math:`\Delta H_{fus}` , and optionally the pure compound heat capacity of fusion :math:`\Delta C_p`  using the subkeys meltingpoint, hfusion, and cpfusion, respectively, of the key COMPOUND for this compound. The COSMO-RS method does not predict these :math:`\Delta H_{fus}`, :math:`\Delta C_p`, or :math:`T_m` .

The assumption made in the solubility calculation may be invalid in case of a solubility of a liquid in a solvent, especially if the solubility of the solvent in the liquid is high. For binary systems one may check this by calculating the miscibility gap in the binary mixture of the two liquids.   It is possible to calculate the solubility of a gas in a solvent, if one adds the subkey isobar and adds the partial vapor pressure partialvaporpressure (bar) of the gas as argument for the key PRESSURE:

::

  PROPERTY solubility      
    isobar    
  End    

  PRESSURE partialvaporpressure  

The solubility of a gas in a solvent can also be calculated using Henry's law, which is valid for ideal dilute solutions, see see the key PROPERTY activitycoef.   The COSMO-RS calculation of the solubility of a compound is performed with an iterative method, since the activity coefficient of the compound depends on the molar fraction of this compound.   

**Links** COSMO-RS GUI tutorial: solubility [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-7-solubility>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#solubility-of-vanillin-in-organic-solvents>`__]  

.. _metatag BINARY_MIXTURE: 
.. index:: binary mixture 
.. index:: VLE diagram 
.. index:: LLE diagram
.. index:: VLE binary mixture 
.. index:: LLE binary mixture 
.. index:: excess energies

Binary mixture (VLE/LLE)
========================

The COSMO-RS module can automatically calculate properties of a binary mixture, by calculating these properties for a number of different compositions. 

Exactly two compounds should be given in the input file. 

.. _keyscheme PROPERTY_binmixcoef: 

::

   PROPERTY binmixcoef
   {Nfrac nfrac}
   {isotherm | isobar | flashpoint}
   End

``nfrac``
   Number of different mixtures for which the binary mixture is calculated will be nfrac+5. Default value for nfrac is 10, which means 15 different mixtures. 

``isotherm | isobar |flashpoint``
   If the subkey isotherm is included (default) the binary mixture will be calculated at a fixed temperature. If the subkey isobar is included the binary mixture will be calculated at a fixed vapor pressure. If the subkey flashpoint is included the flash point of the binary mixture will be calculated. 

The input pure compound vapor pressure will be used in the calculation of the partial vapor pressure of this compound in the mixture if it is supplied with the key COMPOUND for this compound. If it is not specified then it will be approximated using the COSMO-RS method. 

In case of a miscibility gap (LLE) data of the 2 immiscible liquid phases will be calculated. Also information about possible azeotropes will be calculated. With the COSMO-RS GUI, activity coefficients, (partial) vapor pressures, and excess energies can be viewed. 

**Links** COSMO-RS GUI tutorial: vapor-liquid diagram binary mixture (VLE/LLE) [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-8-binary-mixtures-vle-lle>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#binary-mixture-of-methanol-and-hexane>`__] 


.. _metatag TERNARY_MIXTURE: 
.. index:: ternary mixture
.. index:: VLE ternary mixture
.. index:: LLE ternary mixture

Ternary mixture (VLE/LLE)
=========================

The COSMO-RS module can automatically calculate properties of a ternary mixture, by calculating these properties for a number of different compositions. Exactly three compounds should be given in the input file.     

.. _keyscheme PROPERTY_ternarymix: 

:: 

  PROPERTY ternarymix    
    {Nfrac nfrac}    
    {isotherm | isobar |flashpoint}    
  End   

``nfrac``     
    Number of different mixtures for which the ternary mixture is calculated will be (nfrac+1)*(nfrac+2)/2. Default value for nfrac is 10, which means 55 different mixtures.    

``isotherm | isobar | flashpoint``     
    If the subkey isotherm is included (default) the ternary mixture will be calculated at a fixed temperature. If the subkey isobar is included the ternary mixture will be calculated at a fixed vapor pressure. If the subkey flashpoint is included the flash point of the ternary mixture will be calculated.   

The input pure compound vapor pressure will be used in the calculation of the partial vapor pressure of this compound in the mixture if it is supplied with the key COMPOUND for this compound. If it is not specified then it will be approximated using the COSMO-RS method.   

In case of a miscibility gap liquid-liquid equilibrium (LLE) data such as tie lines and an approximate phase diagram, are calculated. With the COSMO-RS GUI, activity coefficients, (partial) vapor pressures, and excess energies can be viewed as a colormap in a 2-dimensional plot with 2 of the liquid compositions on the axes.    


**Links** COSMO-RS GUI tutorial: ternary mixtures (VLE/LLE) [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-9-ternary-mixtures-vle-lle>`__]

.. _metatag COMPOSITION_LINE: 
.. index:: composition line

Solvents s1 - s2 Composition Line 
=================================     

The COSMO-RS module can linear interpolate between the compositions of solvent 1 and solvent 2, which both could be mixtures, and calculate properties, like activity coefficients, and excess energies. This property calculation does not calculate a possible miscibility gap.   The mole fraction of each compound of the solvent 1 and solvent 2 should be given with the subkey FRAC1 and subkey FRAC2 of the key COMPOUND for each compound, respectively.     

.. _keyscheme PROPERTY_compositionline: 

::                 

  PROPERTY compositionline    
    {Nfrac nfrac}    
    {isotherm | isobar | flashpoint}    
  End   

  
``nfrac``     
  Number of different mixtures of the 2 solvents is calculated will be (nfrac+1). Default value for nfrac is 10, which means 11 different mixtures.    

``isotherm | isobar | flashpoint``
  If the subkey isotherm is included (default) a fixed temperature will be used. If the subkey isobar is included a fixed vapor pressure will be used. If the subkey flashpoint is included the flashpoint will be calculated.   

**Links** COSMO-RS GUI tutorial: A composition line between solvents s1 and s2 [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-10-a-composition-line-between-solvents-s1-and-s2>`__]
