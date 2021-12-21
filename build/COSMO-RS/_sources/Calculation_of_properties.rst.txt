.. _metatag CALCULATION_OF_PROPERTIES: 
.. index:: calculation of properties

Calculation of properties
*************************

The COSMO-RS method allows to calculate the (pseudo-)chemical potential of a compound in the liquid phase, as well as in the gas phase, see the the COSMO-RS theory that was discussed before and Ref. [#ref1]_. In the ADF COSMO-RS implementation the following equations were used to calculate properties using these chemical potentials. 

.. math::

   \sum_i x_i     & = \sum_i y_i^{vapor} = \sum_i w_i = 1 \\
   w_i            & = x_i M_i^{pure}/M^{ave} \\
   M^{ave}        & = \sum_i x_i M_i^{pure} \\
   p_i^{pure}     & = exp \{ (\mu_i^{pure}-\mu_i^{gas})/RT \} \\
   p_i^{vapor}    & = x_i exp \{ (\mu_i^{solv}-\mu_i^{gas})/RT \} \\
   p^{vapor}      & = \sum_i p_i^{vapor} \\
   y_i^{vapor}    & = p_i^{vapor}/p^{vapor} \\
   \gamma_i       & = exp \{ (\mu_i^{solv}-\mu_i^{pure})/RT \} \\
   a_i            & = \gamma_i x_i \\
   G^E            & = H^E - T S^E = \sum_i x_i (\mu_i^{solv}-\mu_i^{pure}) \\
   H^E            & = -RT^2 \partial \{ G^E/RT \}/ \partial T \\
   G^{mix}        & = G^E + RT \sum_i x_i \ln(x_i) \\
   \Delta_{vap} H & = RT^2/p^{vapor} \partial \{ p^{vapor} \}/ \partial T \\
   k_H            & = 1/V_{solvent} exp \{ (\mu_i^{gas}-\mu_i^{solv})/RT \} \\
   k_H^{cc}       & = 1/(k_H V_{solvent}) = \gamma_i p_i^{pure} \\
   x_i^{SOL}      & = 1/{\gamma_i} (T > T_m) \\
   x_i^{SOL}      & = 1/{\gamma_i} exp \{ \Delta H_{fus}(1/T_m-1/T)/R - \Delta C_p (ln(T_m/T) -T_m/T + 1)/R \} (T < T_m) \\
   \Delta G_{solv}^{liq-solv} & = \mu_i^{solv}-\mu_i^{pure} \\
   \Delta G_{solv}^{gas-solv} & = \mu_i^{solv}-\mu_i^{gas} + RT ln(V_{solvent}/V_{gas}) \\
   log_{10} P_{solv1/solv2}   & = 1/ln(10) (\mu_i^{solv2}-\mu_i^{solv1})/RT + log_{10} (V_{solv1}/V_{solv2}) \\
   1/LFL_{mix}                & = \sum_i (y_i^{vapor}/LFL_i)


The above equations are not always exact, some assume perfect gas behavior, for example. 

The molar fraction :math:`x_i`  of each compound i of the solvent should add up to 1. 

With the COSMO-RS method it is possible to predict vapor pressures. In the COSMO-RS model the free energy difference between the chemical potential in the gas phase (perfect gas with a reference state of 1 bar) and the chemical potential of the liquid phase has been defined in such a way that the equation: :math:`p_i = exp {(\mu_i^{pure} - \mu_i^{gas} )/RT}`, will give the pressure in units of bar. It is also possible to use experimental vapor pressures of pure compounds as input data for the calculation. This may increase the accuracy of the calculated vapor pressures in a mixture, for example. 

In the COSMO-RS method the volume of 1 molecule in the liquid phase is approximated with the volume of the molecule shaped cavity, that is used in the COSMO calculations. In this way it is possible to calculate the volume of 1 mole of solvent molecules in the liquid phase. However, for properties that depend on such volumes, one can also use (related) experimental data as input data for the calculation. 

The calculation of the boiling temperature of a solvent is performed with an iterative method. The temperature is varied until the calculated vapor pressure is within a certain threshold of the desired pressure. 

Also the calculation of solubility of compound i is performed with an iterative method, since the activity coefficient :math:`\gamma_i` depends on the molar fraction of this compound. The COSMO-RS method does not predict :math:`\Delta H_{fus}`, :math:`\Delta C_p` , or :math:`T_m` . These can be given as input data for the calculation of solubility calculations of solid compounds. 

Starting from ADF2012 the Gibbs-Helmholtz equation is used to calculate the excess enthalpy of a mixture. Previously it was estimated using the misfit and hydrogen bonding energy of the mixture and its pure compounds. 


.. csv-table:: 
    :header: "Quantity", "Meaning"
    :widths: 120,480

    :math:`R` ,Gas constant
    :math:`T` ,Temperature
    :math:`x_i` ,The molar fraction of compound i in a liquid solution
    :math:`y_i` \ :sup:`vapor` ,The molar fraction of compound i in the gas phase
    :math:`w_i` ,The mass fraction of compound i in a liquid solution
    :math:`M_i` \ :sup:`pure` ,The molar mass of the pure compound i
    :math:`M^{ave}` ,The average molar mass of the mixture
    :math:`\gamma_i` ,Activity coefficient of compound i in a liquid solution
    :math:`a_i` ,Activity of compound i in a liquid solution
    :math:`p_i^{pure}` ,The vapor pressure of the pure compound i
    :math:`p_i^{vapor}` ,The partial vapor pressure of compound i
    :math:`p^{vapor}` ,The total vapor pressure
    :math:`\mu`\ :sub:`i` \ :sup:`gas` ,The pseudochemical potential of the pure compound i in the gas phase
    :math:`\mu`\ :sub:`i` \ :sup:`pure` ,The pseudochemical potential of the pure compound i in the liquid phase
    :math:`\mu`\ :sub:`i` \ :sup:`solv` ,The pseudochemical potential of compound i in a liquid solution
    :math:`G^E` ,The excess Gibbs free energy
    :math:`H^E` ,"The excess enthalpy, Gibbs-Helmholtz equation"
    :math:`G^{mix}` ,"The Gibbs energy of mixing"
    :math:`\Delta_{vap} H` ,"The enthalpy of vaporization, Clausius-Clapeyron equation"
    :math:`E_i^{HB~pure}` ,"The hydrogen bond energy of the pure compound i in the liquid phase, see Ref. [#ref1]_"
    :math:`E_i^{HB}` ,The partial hydrogen bond energy of compound i in a liquid solution
    :math:`E_i^{misfit~pure}` ,"The misfit energy of the pure compound i in the liquid phase, see Ref. [#ref1]_"
    :math:`E_i^{misfit}` ,The partial misfit energy of compound i in a liquid solution
    :math:`\Delta G_{solv}^{liq-solv}` ,The solvation Gibbs free energy from the pure compound liquid phase
        ,to the solvated phase
    :math:`\Delta G_{solv}^{gas-solv}` ,"The solvation Gibbs free energy from the pure compound gas phase"
        ,"to the solvated phase, with a reference state of 1 mol/L in both phases"
    :math:`k_H` ,Henry's law constant: ratio between the liquid phase concentration of a compound
        ,and its partial vapor pressure in the gas phase
    :math:`k_H^{cc}` ,dimensionless Henry's law constant: ratio between the liquid phase concentration
        ,of a compound and its gas phase concentration
    :math:`k_{H~inv}^{px}` ,"Henry's law constant, representing the volatility instead of the solubility,"
        ,ratio between the partial vapor pressure of a compound in the gas phas
        ,and the molar fraction in the liquid phase"
    :math:`V_{solvent}` ,Volume of 1 mole of solvent molecules in the liquid phase
    :math:`V_{gas}` ,"Volume of 1 mole of molecules in the gas phase (at 1 atm, perfect gas)"
    :math:`x_i^{SOL}` ,Solubility of compound i in a solvent (molar fraction)
    :math:`\Delta H_{fus}` ,The enthalpy of fusion of compound i
    :math:`\Delta C_p` ,The :math:`\Delta` heat capacity of fusion of compound i
    :math:`T_m` ,The melting temperature of compound i
    :math:`log_{10} P_{solv1/solv2}` ,"The logarithm of the partition coefficient P, which is the ratio of the concentrations"
        ,"of a compound in two immiscible solvents, solvent 1 and solvent 2"
    :math:`LFL_i` ,"The flash point (lower flammable limit, LFL) of compound i"
    :math:`LFL_{mix}` ,"The flash point (lower flammable limit, LFL) of a mixture, Le Chatelier's mixing rule"
   
See also the COSMO-RS GUI tutorial for the calculation of the following properties: 

+  solvent vapor pressure [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-2-vapor-pressure>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#parametrization-of-adf-cosmo-rs-ghydr-vapor-pressures-partition-coefficients>`__] 

+ boiling point of a solvent [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-3-boiling-point>`__] 

+ partition coefficients (log P) [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-6-partition-coefficients-log-p>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#parametrization-of-adf-cosmo-rs-ghydr-vapor-pressures-partition-coefficients>`__], Octanol-Water partition coefficients (log P\ :sub:`OW` ) [`1  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#octanol-water-partition-coefficients-log-pow>`__] 

+ activity coefficients [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-5-activity-coefficients-henry-coefficients-solvation-free-energies>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#large-infinite-dilution-activity-coefficients-in-water>`__], solvation free energies [`1  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#parametrization-of-adf-cosmo-rs-ghydr-vapor-pressures-partition-coefficients>`__], Henry's law constants [`1  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#henry-s-law-constants>`__], :math:`pK_a` values [`1  <../Tutorials/COSMO-RS/pKa_values.html>`__]     

+ solubility [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-7-solubility>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#solubility-of-vanillin-in-organic-solvents>`__]  

+ vapor-liquid diagram binary mixture (VLE/LLE) [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-8-binary-mixtures-vle-lle>`__, `2  <../Tutorials/COSMO-RS/The_COSMO-RS_compound_database.html#binary-mixture-of-methanol-and-hexane>`__] 

**Ionic liquids in COSMO-RS 2020**

The activity coefficient of a compound i solvated in an ionic liquid is an important thermodynamic property.
In COSMO-RS 2020 one can treat the ionic liquid as one compound, which means
that the value of the activity coefficient is calculated in the standard way most applications report them.
In particular, in COSMO-RS 2020 one can treat the ionic liquid as one compound, which only has the dissociated form.

+ `ionic liquids tutorial <../Tutorials/COSMO-RS/Ionic_Liquids.html>`__


**Ionic liquids in COSMO-RS <=2019**

The activity coefficient of a compound i solvated in an ionic liquid is an important thermodynamic property.
The cation and anion, which have been treated separately, will be used in equal amounts to ensure an electroneutral mixture in the COSMO-RS calculation. 

In other applications cation-anion pair have been treated as one
molecule, however, below we will
treat the cation and anion as two separate molecules, which is needed in older versions of COSMO-RS <=2019. This has
consequences for the value of the activity coefficient.

For example, for a 1:1 IL (i.e., [A]\ :sup:`+` [B]\ :sup:`-` ), the activity coefficient at a finite concentration of solute i in the binary mixture (IL + solute) can be calculated by 

\
  | γ\ :sub:`i` \ :sup:`bin`  = (γ\ :sub:`i` \ :sup:`tern`    x\ :sub:`i` \ :sup:`tern` )/x\ :sub:`i` \ :sup:`bin`  =   γ\ :sub:`i` \ :sup:`tern` /(1+x\ :sub:`IL` \ :sup:`bin` ) 

where the superscript "tern" represents the hypothetical ternary system comprising cation, anion and solute i, with 

\
  | x\ :sub:`cation` \ :sup:`tern`  =   x\ :sub:`anion` \ :sup:`tern`  


\
  | x\ :sub:`cation` \ :sup:`tern`  +  x\ :sub:`anion` \ :sup:`tern`  + x\ :sub:`i` \ :sup:`tern`  = 1

and the superscript "bin" represents the binary mixture   comprising solute and IL, with 

\
  | x\ :sub:`IL` \ :sup:`bin`  + x\ :sub:`i` \ :sup:`bin`  = 1 

Accordingly, the activity coefficient of a solute i in the binary mixture (IL + solute) at infinite dilution is simplified as 

\
  | γ\ :sub:`i` \ :sup:`bin`  = 0.5 γ\ :sub:`i` \ :sup:`tern`        (at infinite dilution) 

Thus in this case we should scale the activity coefficient at infinite dilution γ\ :sub:`i` \ :sup:`tern` , which is directly obtained from the COSMO-RS calculation, with a factor of 0.5. 

Similarly, for a ternary system comprising component i, component j and an ionic liquid, the activity coefficient at finite concentration of component i can be calculated by 

\
  | γ\ :sub:`i` \ :sup:`tern`  =   γ\ :sub:`i` \ :sup:`quart` /(1+x\ :sub:`IL` \ :sup:`tern` ) 

where the superscript "quart" represents the hypothetical quaternary system comprised of cation, anion, solute i and solute j, with: 

\
  | x\ :sub:`cation` \ :sup:`quart`  =   x\ :sub:`anion` \ :sup:`quart`  

\
  | x\ :sub:`cation` \ :sup:`quart`  +  x\ :sub:`anion` \ :sup:`quart`  + x\ :sub:`i` \ :sup:`quart`   + x\ :sub:`j` \ :sup:`quart`  = 1

and the superscript "tern" represents the ternary mixture comprising solute i, j, and IL, with 

\
  | x\ :sub:`IL` \ :sup:`tern`  + x\ :sub:`i` \ :sup:`tern`  +   x\ :sub:`j` \ :sup:`tern`  = 1 

.. only:: html

  .. rubric:: References

.. [#ref1] A.\  Klamt, V. Jonas, T. Bürger and J.C. Lohrenz,  *Refinement and Parametrization of COSMO-RS.*  `J. Phys. Chem. A 102, 5074 (1998) <https://doi.org/10.1021/jp980017s>`__ 
