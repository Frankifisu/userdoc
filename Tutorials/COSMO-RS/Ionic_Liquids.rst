.. _crs6: 

Ionic Liquids
*************

Using the ADF COSMO-RS ionic liquid database
============================================

Ionic liquids (ILs), usually consisting of a large organic cation and a small inorganic polyatomic anion, have attracted considerable attention in recent years due to their unique thermophysical properties. The low vapor pressure and high conductivity of these molten salts combined with highly tunable properties, have resulted in highly diverse applications across many different fields in chemistry, materials science (battery electrolytes), chemical engineering (gas sorption and purification), and many more. 

To calculate thermodynamic properties of ionic liquids with
COSMO-RS, the IL may be described either as a single ion pair or
as discrete cations and anions. The latter method will be mainly used here.
The COSMO-RS ionic liquid database ADFCRS-IL-2014 contains 80
cations and 56 anions. This ADFCRS-IL-2014 database consists of
ADF COSMO result (.coskf) files, from standard ADF quantum
mechanical calculations, as described in tutorial 1: :ref:`COSMO result files <crs1>`.
The user can create new anions and cations using that same approach and add them to the List of Added Compounds.

The ADFCRS-IL-2014 database is part of the ADFCRS-2018 COSMO-RS database.
Install the ADFCRS-2018 database if it is not yet installed, see tutorial 4: :ref:`The COSMO-RS compound database<crs4>`.

SCM gratefully acknowledges Prof. Zhigang Lei's research group (State Key Laboratory of Chemical Resource Engineering, Beijing University of Chemical Technology, China) for providing the ionic liquid database, the corresponding tutorial, and the reparameterization of COSMO-RS for ionic liquids (ADF Lei 2018).

Reparameterization of COSMO-RS for ionic liquids
------------------------------------------------

In Ref. [:ref:`617 <reference 617>`] Han, Lei and coworkers present a reparametrization of COSMO-RS parameters for ionic liquids within the ADF framework. The extensive training set consisted of 2283 activity coefficient data points at infinite dilution and 1433 CO\ :sub:`2` solubility data points that were collected from literature references.

The authors use the refitted parameters to predict CO\ :sub:`2` solubility in pure ionic liquids at low temperatures (<273.2 K) and the CO\ :sub:`2` solubility in mixed ionic liquids over a wide temperature and pressure range.

Their refitted optimal values for the misfit energy constant a', hydrogen bond coefficient c_hb and the effective contact surface area of a segment a_eff can be edited manually:

.. rst-class:: steps

  \ 
    | Select **Method → COSMO-RS**
    | Select **Method → Parameters**
    | Select 'ADF combi2005' in the popup menu Use COSMO-RS parameters
    | Enter 2063.0 for a'
    | Enter 7532.0 for c_hb
    | Enter 3.34 for a_eff

However, in this Tutorial we will use the original COSMO-RS parameters.

.. rst-class:: steps

  \ 
    | Select **Method → COSMO-RS**
    | Select **Method → Parameters**
    | Select 'ADF combi2005' in the popup menu Use COSMO-RS parameters

References
----------

Some of the work of Zhigang Lei group based on the COSMO-RS model using the ADF software is listed as follows: 

.. _reference 611: 

611. Z.\  Lei, C. Dai, J. Zhu, B. Chen, Extractive distillation with ionic liquids: A review,  `AIChE Journal 60, 3312 (2014) <https://doi.org/10.1002/aic.14537>`__ 

.. _reference 612: 

612. Z.\  Lei, C. Dai, B. Chen, Gas solubility in ionic liquids,  `Chemical Reviews 14, 1289 (2014) <https://doi.org/10.1021/cr300497a>`__ 

.. _reference 613: 

613. Z.\  Lei, J. Han, Q. Li, and B. Chen, Process Intensification on the Supercritical Carbon Dioxide Extraction of Low-Concentration Ethanol from Aqueous Solutions,  `Industrial &  Engineering Chemistry research 51, 2730 (2012) <https://doi.org/10.1021/ie2021027>`__ 

.. _reference 614: 

614. Z.\  Lei, J. Han, B. Zhang, Q. Li, J. Zhu, and B. Chen, Solubility of CO\ :sub:`2`  in Binary Mixtures of Room-Temperature Ionic Liquids at High Pressures,  `Journal of Chemical Engineering data 57, 2153 (2012) <https://doi.org/10.1021/je300016q>`__ 

.. _reference 615: 

615. Z.\  Lei, C. Dai, X. Liu, L. Xiao, and B. Chen, Extension of the UNIFAC Model for Ionic Liquids,  `Industrial &  Engineering Chemistry research 51, 12135 (2012) <https://doi.org/10.1021/ie301159v>`__ 

.. _reference 616: 

616. Z.\  Lei, C. Dai, Q. Yang, J. Zhu, and B. Chen, UNIFAC model for ionic liquid-CO (H\ :sub:`2` ) systems: An experimental and modeling study on gas solubility,  `AIChE Journal 60, 4222 (2014) <https://doi.org/10.1002/aic.14606>`__ 

.. _reference 617: 

617. J.\  Han, C. Dai, G. Yu, Z. Lei, Parameterization of COSMO-RS model for ionic liquids,  `Green Energy & Environment 3, 247 (2018) <https://doi.org/10.1016/j.gee.2018.01.001>`__ 

Ionic liquid volumes and densities
==================================

Ionic liquid densities may be estimated from the molecular volume and molar mass (MW) of the constituent cations and anions. The COSMO volume is stored in the coskf file and is displayed, together with the MW, when a compound is selected in the COSMO-RS GUI. 

.. rst-class:: steps

  \ 
    | Click on the search button in the compounds field
    | Select IL_cation_1-butyl-3-methyl-imidazolium
    | Click OK

.. image:: /Images/Ionic_Liquid/t6_compoundBMIM.png
   :width: 15 cm

Volumes and molar mass of other cations and anions can be   similarly found. Data for a few compounds are listed below. 


.. csv-table:: 
   :header: ,COSMO Volume (Å\ :sup:`3`) , MW (g/mol)

   cations, ,
   C4MIM 1-butyl-3-methyl-imidazolium,  197.181, 139.124
   C6MIM 1-hexyl-3-methyl-imidazolium,  241.003, 167.155
   C8MIM 1-octyl-3-methyl-imidazolium,  282.855, 195.186
   anions, ,
   BF\ :sub:`4`   tetrafluoroborate                ,   72.489 ,  87.003
   PF\ :sub:`6`   hexafluorophosphate              ,   103.495,  144.964
   NTF\ :sub:`2`  bis(trifluoromethylsulfonyl)amide,   213.173,  279.917


The molecular liquid density could be approximately calculated as (V in Å\ :sup:`3`  and MW in g/mol) using Avogadro's number:

\
   | density = (MW\ :sub:`cation`  +   MW\ :sub:`anion` )/[0.6022*(V\ :sub:`cation`  +   V\ :sub:`anion` )] 

.. csv-table:: density (g cm\ :sup:`-3`)
   :header: ionic liquid, expt [:ref:`621 <reference 621>`],  calculated

   C4MIMBF\ :sub:`4`  ,  1.208, 1.392
   C6MIMBF\ :sub:`4`  ,  1.148, 1.346
   C8MIMBF\ :sub:`4`  ,  1.109, 1.319
   C4MIMPF\ :sub:`6`  ,  1.37 , 1.569
   C6MIMPF\ :sub:`6`  ,  1.293, 1.505
   C8MIMPF\ :sub:`6`  ,  1.237, 1.462
   C4MIMNTf\ :sub:`2` ,  1.429, 1.696
   C6MIMNTf\ :sub:`2` ,  1.37 , 1.635
   C8MIMNTf\ :sub:`2` ,  1.32 , 1.591


As can be seen from this table, the calculated densities are   systematically overestimated by approximately 15%. Thus, the   COSMO volumes underestimate the volume of a single compound, if   they are used for estimating the liquid densities. 

References
----------

.. _reference 621: 

621. C.\  Ye and J.M. Shreeve,   Rapid and Accurate Estimation of Densities of   Room-Temperature Ionic Liquids and Salts,  `Journal of Physical   Chemistry A 111, 1456 (2007) <https://doi.org/10.1021/jp066202k>`__ 

Activity coefficient calculation
================================

The activity coefficient of a compound i solvated in an ionic liquid is an important thermodynamic property.
The cation and anion, which have been treated separately, will be used in equal amounts to ensure an electroneutral mixture in the COSMO-RS calculation. 

In other applications cation-anion pair have been treated as one
molecule, however, in the COSMO-RS calculations below we will
treat the cation and anion as two separate molecules.
To be able to compare to experimental activity coefficients in which the cation-anion pair is treated as one compound,
we will also make one compound. However, in the calculation this compound only has the dissociated form.

.. rst-class:: steps

  \ 
    | Select **Compounds → Compound with multiple forms**
    | Select 'IL_cation_1-ethyl-3-methyl-imidazolium' for dissociated compound d1.A
    | Select 'IL_anion_tetracyanoborate' for dissociated compound d1.B
    | Press 'Save' at the top of the left window
    | In the file select box, choose 'IL_Emim_Tcb' as name for your file and click 'Save'

.. image:: /Images/Ionic_Liquid/t6_Emim_Tcb.png
   :width: 15 cm

.. rst-class:: steps

  \ 
    | Select **Properties → Activity coefficients**
    | Select '1 component' in the popup menu next to Solvent
    | Select 'IL_Emin_Tcb' for the first component in Solvent
    | Enter 1.0 for the Mole fraction of the first component
    | Enter '308.15' for 'Temperature Kelvin'
    | Check the '+' button to add 'Hexane', 'Heptane', 'Octane', and 'Decane'
    | Press 'Run'

.. image:: /Images/Ionic_Liquid/t6_actinput.png
   :width: 10 cm

If one does not supply a density of the solvent in the input, the program calculates the density of the solvent by dividing the mass of a molecule with its COSMO volume.
Note that the calculated activity coefficients do not depend on this density.
The result of the calculation is given in the form of a table. 

.. image:: /Images/Ionic_Liquid/t6_act.png
   :width: 10 cm

In the next figure the results of the calculated activity coefficients at different temperatures are compared to experiment. 

.. image:: /Images/Ionic_Liquid/t6_lngamalkane.png
   :width: 10 cm

In this figure activity coefficients at infinite dilution of n-alkenes in [EMIM]\ :sup:`+` [TCB]\ :sup:`-`  are shown for different temperatures ranging from 298 K to 358 K.
The scattered points are experimental data from Ref.[633].
The points that are connected with a line are calculated numbers with ADF COSMO-RS.
For example, for Hexane, the calculated values T = 308.15 K are:   1000/308.15 = 3.245, ln(30.219) = 3.41.
Note that the calculated numbers in this figure are calculated with an older version of COSMO-RS.
These will not change much if you use a newer COSMO-RS version.

References
----------

.. _reference 631: 

631. Z.\  Lei, C. Dai, J. Zhu, B.   Chen, Extractive distillation with ionic liquids: A   review,  `AIChE   Journal 60, 3312 (2014) <https://doi.org/10.1002/aic.14537>`__ 

.. _reference 632: 

632. Z.\  Lei, C. Dai, B. Chen,   Gas solubility in ionic liquids,  `Chemical Reviews   14, 1289 (2014) <https://doi.org/10.1021/cr300497a>`__ 

.. _reference 633: 

633. U.\  Domańska, M. Królikowska,   W.E. Acree Jr., G.A. Baker, Activity coefficients at infinite   dilution measurements for organic solutes and water in the ionic   liquid 1-ethyl-3-methylimidazolium tetracyanoborate,    `The Journal   of Chemical Thermodynamics 43, 1050 (2011) <https://doi.org/10.1016/j.jct.2011.02.012>`__ 

Henry's law constants
=====================

In this tutorial, we will calculate Henry's law constants for   CO\ :sub:`2`  in different ionic liquids. Henry's law constant   reflects the solubility of a gas in a solvent, and one way to   define it is 

.. math::

      H_i = \gamma_i^\infty  P_i^S

where H\ :sub:`i`  is the ratio between the partial vapor   pressure of a compound i in the gas phase and its molar   fraction in the liquid phase, :math:`\gamma_i^\infty` is the   the activity coefficient of the compound at infinite dilution,   and P\ :sub:`i` \ :sup:`S`  is the saturated pure compound   vapor pressure of the gas. 

The familiar Antoine and Wagner equations can be used to   calculate the vapor pressure below the critical temperature   T\ :sub:`c` , if one knows the coefficients. Above   T\ :sub:`c` , they can be extrapolated as a hypothetical vapor   pressure. If the experimental saturated vapor pressures of a gas   is not available, then it can be estimated by COSMO-RS. 

The saturated vapor pressure of CO\ :sub:`2`  at 298.15 K can be   calculated by the following Antoine equation: 

\
  | ln P\ :sub:`CO`\ :sub:`2` \ :sup:`S`  (MPa) = 12.3312 -   4759.46/(T(K)+156.462) 

The saturated vapor pressure of CO\ :sub:`2`  at 298.15 K is   6.436 MPa (= 64.36 bar) according to this equation. The Antoine   equation can also be written as: 

\
  | :math:`{}^{10}`\ log P\ :sub:`CO`\ :sub:`2` \ :sup:`S`    (bar) = 6.35537 - 2067.0/(T(K)+156.462) 

The activity coefficients of infinitely diluted carbon dioxide in   [HMIM]\ :sup:`+` [Tf2N]\ :sup:`-`  will now be calculated. 

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Search on the left side 'Carbon dioxide' and click on it
    | Enter 6.35537 for the Antoine coefficient A on the right side
    | Enter 2067.0 for the Antoine coefficient B
    | Enter 156.462 for the Antoine coefficient C
    | Select **Compounds → Compound with multiple forms**
    | Press 'Clear' at the top of the left window
    | Select 'IL_cation_1-hexyl-3-methyl-imidazolium' for dissociated compound d1.A
    | Select 'IL_anion_bis(trifluoromethylsulfonyl)amide' for dissociated compound d1.B
    | Press 'Save' at the top of the left window
    | In the file select box, choose 'IL_Hmim_Tf2N' as name for your file and click 'Save'
    | Select **Properties → Activity coefficients**
    | Select '1 component' in the popup menu next to Solvent
    | Select 'IL_Hmin_Tf2N' for the first component in Solvent
    | Enter 1.0 for the Mole fraction of the first component
    | Enter '298.15' for 'Temperature Kelvin'
    | Check the '+' button to add 'Carbon dioxide' (Remove the alkanes if they are still present)
    | Press 'Run'

.. image:: /Images/Ionic_Liquid/t6_actinputco2.png
   :width: 10 cm

The results of the activity coefficients. 

.. image:: /Images/Ionic_Liquid/t6_actco2.png
   :width: 10 cm

Henry's law coefficient is :math:`\gamma^\infty` times the saturated vapor pressure of CO\ :sub:`2`  at 298.15 K (64.36 bar).
For CO\ :sub:`2`  in [HMIM]\ :sup:`+` [Tf2N]\ :sup:`-` the calculated H = 0.5065*64.36 = 32.6 bar.
Applying the same   calculations for more ionic liquids gives these results: 

.. csv-table:: H (bar)
   :header: ionic liquid, expt [:ref:`644 <reference 644>`],  calculated

   BMIM PF\ :sub:`6`         , 53.4±0.3, 53.1
   BMIM Tf\ :sub:`2` N        , 33.0±0.3, 35.4
   HMIM Tf\ :sub:`2` N        , 31.6±0.2, 32.6
   HMPY Tf\ :sub:`2` N        , 28.4±0.2, 314
   C6F9MIM Tf\ :sub:`2` N     , 27.3±0.1, 33.8
   C8F13MIM Tf\ :sub:`2` N    , 25.2±0.2, 31.0
   HMIM eFAP                 , 25.2±0.1, 27.1
   HMIM pFAP                 , 21.6±0.1, 25.8
   C5MIM bFAP                , 20.2±0.1, 25.2
   Et\ :sub:`3` NBH\ :sub:`2` MIM Tf\ :sub:`2` N  , 33.1±1.2, 30.5



.. image:: /Images/Ionic_Liquid/t6_henry.png

There are many different definitions of Henry's law constant.   Henry's constant as calculated directly by COSMO-RS,   k\ :sub:`H`  (mol/(L atm)), is defined as the ratio between the   liquid phase concentration of a compound and its partial vapor   pressure in the gas phase. The relationship between k\ :sub:`H`    and H is: 

\
  | H = k\ :sub:`H,inv` \ :sup:`px`  = 1/(k\ :sub:`H`    V\ :sub:`solvent` ) 

where V\ :sub:`solvent`  is the molar volume of the ionic   liquid. If no densities for the cation, anion, or solvent are   given, COSMO-RS will use the COSMO volume for calculating the   molar volume of the ionic liquid, which is 0.2735 L/mol   (=(241.00+213.17)*0.6022/1000) for   [HMIM]\ :sup:`+` [Tf2N]\ :sup:`-` , if the usual convention is   followed, that a pair of a cation and an anion is treated as one   molecule. Thus in this case H = 1.01325/(0.1136 * 0.2735) = 32.6   bar, where a conversion factor from atm to bar is included. 

Note that k\ :sub:`H`  does not depend on whether one treats a
cation and an anion as separate molecules, or if a pair of a
cation and an anion is treated as one molecule. H =
k\ :sub:`H,inv` \ :sup:`px`  does depend on this definition.

References
----------

.. _reference 641: 

641. P.G.T. Fogg and W. Gerrard,   Solubility of gases in liquids: A critical evaluation of   gas/liquid systems in theory and practice, New York: John   Wiley & Sons, Inc., 1991. 

.. _reference 642: 

642. J.L. Anthony, J.L. Anderson,   E.J. Maginn, J.F. Brennecke, Anion Effects on Gas Solubility   in Ionic Liquids,  `Journal of Physical   Chemistry B 109, 6366 (2005) <https://doi.org/10.1021/jp046404l>`__ 

.. _reference 643: 

643. J.L. Anderson, E. J. Maginn and   J. F. Brennecke, Measurement of SO\ :sub:`2`  Solubility in   Ionic Liquids,  `Journal of Physical   Chemistry B 110, 15059 (2006) <https://doi.org/10.1021/jp063547u>`__ 

.. _reference 644: 

644. M.J. Muldoon, S.N.V.K. Aki,   J.L. Anderson, J.K. Dixon, J.F. Brennecke, Improving Carbon   Dioxide Solubility in Ionic Liquids,  `Journal of Physical   Chemistry B 111, 9001 (2007) <https://doi.org/10.1021/jp071897q>`__ 

.. _reference 645: 

645. B.H. Culbertson, S. Dai, H.   Luo, D.W. DePaoli, Low-Pressure Solubility of Carbon Dioxide   in Room-Temperature Ionic Liquids Measured with a Quartz Crystal   Microbalance,  `Journal of Physical   Chemistry B 108, 721 (2004) <https://doi.org/10.1021/jp036051a>`__ 

.. _reference 646: 

646. Y.\  Hou and R.E. Baltus,   Experimental Measurement of the Solubility and Diffusivity of   CO2 in Room-Temperature Ionic Liquids Using a Transient   Thin-Liquid-Film Method,  `Industrial &  Engineering Chemistry research 46, 8166   (2007) <https://doi.org/10.1021/ie070501u>`__ 

.. _reference 647: 

647. A.\  Finotello, J.E. Bara, D. Camper and R.D. Noble, Room-Temperature Ionic Liquids: Temperature Dependence of Gas Solubility Selectivity, `Industrial & Engineering Chemistry research 47, 3453 (2008) <https://doi.org/10.1021/ie0704142>`__

Gas solubility and selectivity in ionic liquids
===============================================

In this example the solubility of carbon dioxide in ionic liquids is calculated and compared to experimental data. 

First we use the experimental Antoine coefficients for CO\ :sub:`2`.

.. rst-class:: steps

  \ 
    | **(Skip this part if you have just done COSMO-RS tutorial 6.4)**
    | Select **Compounds → List of Added Compounds**
    | Search on the left side 'Carbon dioxide' and click on it
    | Enter 6.35537 for the Antoine coefficient A on the right side
    | Enter 2067.0 for the Antoine coefficient B
    | Enter 156.462 for the Antoine coefficient C

Next we make the ionic liquid as one compound and calculate CO\ :sub:`2`  solubilities. 

.. rst-class:: steps

  \ 
    | Select **Compounds → Compound with multiple forms**
    | Press 'Clear' at the top of the left window
    | Select 'IL_cation_1-butyl-3-methyl-imidazolium' for dissociated compound d1.A
    | Select 'IL_anion_bis(trifluoromethylsulfonyl)amide' for dissociated compound d1.B
    | Press 'Save' at the top of the left window
    | In the file select box, choose 'IL_Bmim_Tf2N' as name for your file and click 'Save'
    | Select **Properties → Solubility in Mixture**
    | Select '1 component' in the popup menu next to Solvent
    | Select 'IL_Bmin_Tf2N' for the first component in Solvent
    | Enter 1.0 for the Mole fraction of the first component
    | Enter '8' for 'Temperature: number of steps'
    | Enter '282.0' for 'Temperature from'
    | Enter '322.8' for 'Temperature to'
    | Change the popup menu next to Solutes to 'Gas'
    | Enter '3' for 'Pressure: for solubility gas: number of steps'
    | Use 'MPa' units for the pressure
    | Enter '0.5' for the pressure 'from'
    | Enter '2.0' for the pressure 'to'
    | Check the '+' button to add 'Carbon dioxide'
    | Press 'Run'

.. image:: /Images/Ionic_Liquid/t6_solinputco2.png
   :width: 10 cm

From the results we will use the calculated mole fractions at 282.0 K, 297.3 K, and 322.8 K. 

.. image:: /Images/Ionic_Liquid/t6_solco2.png
   :width: 10 cm

In this example we also calculated the solubility of carbon dioxide at relatively high pressures.
In such cases, for more accurate results, we also need to take the nonideal behavior of the gas into account, the gas fugacity. 

\
  | f\ :sub:`gas`  = P\ :sub:`gas`  :math:`\Phi` (T,P) 

where f\ :sub:`gas`  is the gas fugacity at the system temperature and pressure, and :math:`\Phi` (T,P) is the fugacity coefficiency of the gas.
We will approximate the fugacity coefficients with: 

.. math::

  \Phi (T=282.0 K,P) & \approx (1 - 0.06 (P/MPa)) \\
  \Phi (T=297.3 K,P) & \approx (1 - 0.05 (P/MPa)) \\
  \Phi (T=322.8 K,P) & \approx (1 - 0.04 (P/MPa))

Note that these values are only approximate, and certainly not applicable for higher pressures. 
We can use the same solubilities as calculated before but plot them against fugacity instead of pressure. 

.. csv-table:: 
   :header: Temperature, f (MPa),  P (MPa)

   282.0, 0.50,  0.52
   282.0, 1.00,  1.07
   282.0, 1.50,  1.67
   282.0, 2.00,  2.32
   297.3, 0.50,  0.51
   297.3, 1.00,  1.06
   297.3, 1.50,  1.63
   297.3, 2.00,  2.25
   322.8, 0.50,  0.51
   322.8, 1.00,  1.04
   322.8, 1.50,  1.60
   322.8, 2.00,  2.19

The results can be compared with experimental values from Ref.[:ref:`651<reference 651>`]. 
Note that the calculated numbers in this figure are calculated with an older version of COSMO-RS.
These will not change much if you use a newer COSMO-RS version.

.. image:: /Images/Ionic_Liquid/t6_solco2graph.png
   :width: 10 cm


For low pressures one can estimate gas solubility using Henry's law constants: 

.. math::

   x = P_{gas} \Phi (T,P)/H_{gas}

For low pressures :math:`\Phi` (T,P) will be close to 1. Calculating Henry's law constants has been described in COSMO-RS Tutorial 6.4, and following this procedure for CO\ :sub:`2` in [HMIM][Tf\ :sub:`2` N], results in H = 2.24 MPa at T = 282 K, H = 3.20 MPa at T = 297.3 K, and H = 5.51 MPa at T = 322.8 K. 

Gas selectivity in ionic liquids can be defined as 

\
  | S\ :sub:`i/j`  = H\ :sub:`i` /H\ :sub:`j`  

where S\ :sub:`i/j`  is the selectivity between gas i and j in   ionic liquids; H\ :sub:`i`  and H\ :sub:`j`  are Henry's law   constants of gas i and j, which can be calculated using the   methods as described in the COSMO-RS Tutorial 6.4. 

References
----------

.. _reference 651: 

651. M.B. Shiflett and A. Yokozeki,   Solubility of CO\ :sub:`2`  in Room Temperature Ionic Liquid   [hmim][Tf\ :sub:`2` N],  `Journal of Physical   Chemistry B 111, 2070 (2007) <https://doi.org/10.1021/jp067627+>`__ 

VLE for systems containing ionic liquids
========================================

In this example a vapor-liquid diagram of Acetone in   [EMIM][Tf\ :sub:`2` N] at 353.15 K is calculated and compared to   experiment. The experimental saturated pure compound vapor   pressure is used for Acetone. 

.. rst-class:: steps

  \ 
    | Select **Compounds → List of Added Compounds**
    | Search on the left side 'Acetone' and click on it
    | Enter '2.1516' in the 'Pure compound vapor pressure' field
    | Enter '353.15' in the 'at temperature' field
    | Select **Compounds → Compound with multiple forms**
    | Press 'Clear' at the top of the left window
    | Select 'IL_cation_1-ethyl-3-methyl-imidazolium' for dissociated compound d1.A
    | Select 'IL_anion_bis(trifluoromethylsulfonyl)amide' for dissociated compound d1.B
    | Press 'Save' at the top of the left window
    | In the file select box, choose 'IL_Emim_Tf2N' as name for your file and click 'Save'
    | Select **Properties → Binary Mixture VLE/LLE**
    | Select 'Acetone' for the first compound
    | Select 'IL_Emim_Tf2N' for the second compound
    | Enter '20' for 'Number of mixtures'
    | Select 'Isotherm' from the Isotherm, isobar, flash point popup menu
    | Use 'Kelvin' as units for the temperature
    | Enter '353.15' for 'Temperature'
    | Press 'Run'

.. image:: /Images/Ionic_Liquid/t6_inputbinmix.png
   :width: 10 cm

.. csv-table:: 

   x, P (kPa),  x,  P (kPa)
   **calc**,   **calc**,    **expt** [:ref:`661 <reference 661>`], **expt** [:ref:`661 <reference 661>`]
   0.000,  0.000 ,   0.0133 ,  1.139
   0.002,  0.144 ,   0.0383 ,  3.485
   0.01,   0.726,   0.0539 ,  4.825
   0.05,   3.741,   0.0683 ,  6.073
   0.10,   7.774,   0.0949 ,  8.509
   0.15,  12.135 ,   0.1521 ,  14.884
   0.20,  16.863,   0.2081 ,  21.660
   0.25,  22.005,   0.2735 ,  30.115
   0.30,  27.616,   0.3393 ,  39.811
   0.35,  33.760,   0.4022 ,  50.263
   0.40,  40.511,   0.4647 ,  61.862
   0.45,  47.960,   0.5249 ,  74.281
   0.50,  56.210,   0.5839 ,  87.870
   0.55,  65.386,   0.6369 ,  101.46
   0.60,  75.637,   0.6846 ,  114.73
   0.65,  87.133,   0.7264 ,  127.22
   0.70,  100.07,   0.7631 ,  138.75
   0.75,  114.68,   0.7948 ,  149.16
   0.80,  131.18,   0.8222 ,  158.37
   0.85,  149.74,   0.8455 ,  166.29
   0.90,  170.04,   0.8653 ,  173.07
   0.95,  192.70,   0.8967 ,  183.75
   0.99,  210.80,   0.9376 ,  196.92
   0.998, 214.30,   0.9671 ,  205.80
   1.000, 215.16,   0.9844 ,  210.74
       ,        ,   0.9933 ,  213.25
       ,        ,   0.9972 ,  214.40
       ,        ,   0.9990 ,  214.94
       ,        ,   1.0000 ,  215.16

Comparing the calculated and experimental vapor pressure of acetone in [EMIM][Tf2N] in a graph: 

.. image:: /Images/Ionic_Liquid/t6_graphcompline.png 
   :width: 10 cm

**References**

.. _reference 661: 

661. M.\  Döker, J. Gmehling,  Measurement and prediction of vapor-liquid equilibria of  ternary systems containing ionic liquids, `Fluid Phase Equilibria 227 (2005), 255 <https://doi.org/10.1016/j.fluid.2004.11.010>`__ 

