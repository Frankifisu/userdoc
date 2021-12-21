.. _metatag CRSPARAMETERS:

COSMO-RS and COSMO-SAC parameters
*********************************

The COSMO-RS model has general parameters and element specific parameters. ADF's COSMO-SAC 2013-ADF model has general parameters, but also uses some of the COSMO-RS parameters, such as the element specific parameters. There are also technical and accuracy parameters, such as convergence criteria. This section explains how to set these parameters, and shows the default values for these parameters. By default the COSMO-RS method is chosen. 

.. index:: COSMO-RS parameters
.. _COSMO-RS parameters:

COSMO-RS general parameters
===========================

.. _keyscheme CRSPARAMETERS: 

::

   CRSPARAMETERS
     {RAV         rav}
     {APRIME      aprime}
     {FCORR       fcorr}
     {CHB         chb}
     {SIGMAHBOND  sigmahbond}
     {AEFF        aeff}
     {LAMBDA      lambda}
     {OMEGA       omega}
     {ETA         eta}
     {CHORTF      chortf}
     {combi1998 | combi2005}
     {hb_all    | hb_hnof}
     {hb_temp   | hb_notemp}
     {fast      | nofast}
   End

The ADF default values are optimized parameters for ADF calculations. The Klamt values can be found in Ref. [#ref1]_. See also Ref. [#ref1]_ for the meaning of the parameters. 


.. csv-table:: 
  :widths: 150,120,120,120,120
  :header: "symbol", "ADF Default", "ADF combi1998", "Klamt", "MOPAC PM6"

   ,"Ref. [#ref2]_","Ref. [#ref2]_","Ref. [#ref1]_", 
   rav (:math:`r_{av}` ),0.400,0.415,0.5,0.400
   aprime (a'),1510.0,1515.0,1288.0,1550.0
   fcorr (:math:`f_{corr}` ),2.802,2.812,2.4,2.802
   chb (:math:`c_{hb}` ),8850.0,8850.0,7400.0,8400.0
   sigmahbond (:math:`\sigma_{hb}` ),0.00854,0.00849,0.0082,0.00978
   aeff (:math:`a_{eff}` ),6.94,7.62,7.1,5.96
   lambda (:math:`\lambda` ),0.130,0.129,0.14,0.135
   omega (:math:`\omega` ),-0.212,-0.217,-0.21,-0.212
   eta (:math:`\eta` ),-9.65,-9.91,-9.15,-9.65
   chortf (:math:`c^\perp` ),0.816,0.816,0.816,0.816
   combi1998 | combi2005,combi2005,combi1998,combi1998,combi2005
   hb_all | hb_hnof,hb_hnof,hb_hnof,hb_hnof,hb_hnof
   hb_temp | hb_notemp,hb_temp,hb_notemp,hb_notemp,hb_temp
   fast | nofast,fast,fast,fast,fast
   
``chortf``
   See Ref. [#ref1]_ for the definitions: :math:`\sigma_v^\perp = \sigma_v^0 - c^\perp \sigma_v`  

``combi1998 | combi2005``
   If the subkey combi1998 is included a thermodynamically inconsistent combinatorial contribution to the chemical potential :math:`\mu_i^{comb}`  of Ref. [#ref1]_ is used. If the subkey combi2005 is included (default) a thermodynamically consistent combinatorial contribution of Ref. [#ref3]_ is used. See  :ref:`the section on the combinatorial term <combinatorial term>` and Ref. [#ref3]_. 

``hb_all | hb_hnof``
   If the subkey hb_all is included hydrogen bond interaction can be included between segments that belong to H atoms and all other segments. If the subkey hb_hbnof is included (default) hydrogen bond interaction can be included only between segments that belong to H atoms that are bonded to N, O, or, F, and segments that belong to N, O, or F atoms. 

``hb_temp | hb_notemp``
   If the subkey hb_notemp is included the hydrogen bond interaction is not temperature dependent, as in Ref. [#ref1]_. If the subkey hb_temp is included (default) the hydrogen bond interaction is temperature dependent, as in Ref. [#ref3]_. See  :ref:`the section on the temperature dependent hydrogen bond interaction <hydrogen bond interaction>` and Ref. [#ref3]_. 

``fast | nofast``
   If the subkey fast is included the fast approximation is used. This fast approximation is the default. Use nofast for the original approach. See  :ref:`the section on the fast approximation for COSMO-RS calculations<fast approximation>`. 

**Links** COSMO-RS GUI tutorial: set COSMO-RS parameters [`1 <../Tutorials/COSMO-RS/COSMO-RS_overview_parameters_and_analysis.html#step-4-cosmo-rs-and-cosmo-sac-parameters>`__] 

.. index:: element specific parameters

COSMO-RS element specific parameters
====================================

.. _keyscheme DISPERSION: 

::

   DISPERSION
     {H  dispH}
     {C  dispC}
     {N  dispN}
     {...}
   End


The following table gives the element specific dispersion constants. The ADF default values are optimized parameters for ADF calculations. The Klamt values can again be found in Ref. [#ref1]_. The constants for F, Si, P, S, Br, and I in the ADF defaults were only fitted to a small number of experimental values or taken from Ref. [#ref3]_. 

.. csv-table:: 
  :widths: 150,150,150,150
  :header: "element", "ADF Default", "ADF combi1998", "Klamt"

   , , ,"Ref. [#ref1]_"
   H,-0.0340,-0.0346,-0.041
   C,-0.0356,-0.0356,-0.037
   N,-0.0224,-0.0225,-0.027
   O,-0.0333,-0.0322,-0.042
   Cl,-0.0485,-0.0487,-0.052
   F,-0.026,,
   Si,-0.04,,
   P,-0.045,,
   S,-0.052,,
   Br,-0.055,,
   I,-0.062,,
   
Note that not for all elements in the periodic system COSMO-RS parameters were fitted. 

**Links** COSMO-RS GUI tutorial: set COSMO-RS parameters [`1 <../Tutorials/COSMO-RS/COSMO-RS_overview_parameters_and_analysis.html#step-4-cosmo-rs-and-cosmo-sac-parameters>`__] 

.. _metatag COSMOSAC_SETTINGS: 
.. index:: COSMO-SAC parameters
.. index:: COSMO-SAC 2013-ADF parameters

COSMO-SAC general parameters
============================

The ADF COSMO-RS program can calculate activity coefficients using the COSMO-SAC 2013-ADF model, based on Ref. [#ref4]_.
Like in the COSMO-RS method, pure compound vapor pressures can be given as input, for example, if experimental values are available.
If these values are not specified then the pure compound vapor pressure will
be calculated according to the COSMO-SAC 2013-ADF model.
This part of the COSMO-SAC 2013-ADF has been implemented in ADF2016.
The COSMO-SAC 2013-ADF parameters in Ref. [#ref4]_ are optimized parameters for use with ADF COSMO result files.
The authors of Ref. [#ref6]_ reoptimized the revised COSMO-SAC model [#ref5]_ parameters for use with ADF COSMO result files, which is called here the COSMO-SAC 2016-ADF method.
Note that the earlier COSMO-SAC papers [#ref7]_ [#ref5]_ do not include parameters that were optimized for use with ADF COSMO result files.
The key COSMOSAC2013 needs to be included if one wants to do a COSMO-SAC 2013-ADF calculation.
The key COSMOSACDHB needs to be included if one wants to do a COSMO-SAC DHB-ADF calculation.
For other COSMO-SAC methods one needs to include the key COSMOSAC. 


.. _keyscheme COSMOSAC2013: 
.. _keyscheme COSMOSAC: 
.. _keyscheme COSMOSACDHB: 

::

   COSMOSAC2013 | COSMOSAC | COSMOSACDHB
   SACPARAMETERS
     {AEFF        aeff}
     {FDECAY      fdecay}
     {SIGMA0      sigma0}
     {RN          rn}
     {QN          qn}
     {AES         aes}
     {BES         bes}
     {COHOH       cohoh}
     {COTOT       cotot}
     {COHOT       cohot}
     {RAV         rav}
     {QS          qs}
     {rhbcut      rhbcut}
     {hb_temp   | hb_notemp}
   End

.. csv-table:: 
   :widths: 120,100,100,100,100,100
   :header: "symbol", "2013-ADF Xiong", "2016-ADF Chen", "DHB-ADF Chen", "2010 Hsieh", "2007 Wang"

   ,"Ref. [#ref4]_","Ref. [#ref6]_", "Ref. [#ref8]_", "Ref. [#ref5]_","Ref. [#ref7]_"
   aeff (a\ :sub:`eff` ),6.4813,5.8447,5.8447,7.25,7.25
   fdecay (f\ :sub:`decay` ),  ,3.57,3.57,3.57,3.57
   sigma0 (:math:`\sigma`\ :sub:`0` ),0.01233,0.007,0.0063,0.007,0.007
   rn (r), ,66.69,66.69,66.69,66.69
   qn (q),79.352,79.53,79.53,79.53,79.53
   aes (A\ :sub:`ES` ),7877.13,5920.84,5920.84,6525.69,8451.77
   bes (B\ :sub:`ES` ),0.0,1.3950 10\ :sup:`8` ,1.3950 10\ :sup:`8` ,1.4859 10\ :sup:`8` ,0.0
   cohoh (c\ :sub:`OH-OH` ),5786.72,3551.10,33306.83,4013.78,3484.42
   cotot (c\ :sub:`OT-OT` ),2739.58,1077.26,33306.83,932.31,3484.42
   cohot (c\ :sub:`OH-OT` ),4707.75,3099.31,33306.83,3016.43,3484.42
   rav (r\ :sub:`av` ),0.51,   ,   ,  , 
   qs (q\ :sub:`s` ),0.57,   ,   ,  , 
   rhbcut,   ,   ,1.4432,  , 
   hb_temp | hb_notemp,hb_notemp,hb_notemp,hb_notemp,hb_notemp, hb_notemp
   
See also Refs. [#ref4]_ [#ref5]_ for the meaning of the parameters a\ :sub:`eff` , f\ :sub:`decay` , :math:`\sigma`\ :sub:`0` , r, q, A\ :sub:`ES` , B\ :sub:`ES` , c\ :sub:`OH-OH` , c\ :sub:`OT-OT` , c\ :sub:`OH-OT` , r\ :sub:`av` , q\ :sub:`s` . The parameter names in [#ref7]_ have been translated into parameter names used in Ref. [#ref5]_, by calculating A\ :sub:`ES`  from 0.3 f\ :sub:`pol`  a\ :sub:`eff` \ :sup:`3/2` /(2\ :math:`\epsilon_0` ), using B\ :sub:`ES`  = 0, and  using c\ :sub:`OH-OH`  = c\ :sub:`OT-OT`  = c\ :sub:`OH-OT` = c\ :sub:`hb` . The parameters f\ :sub:`decay`  and r are not used in COSMO-SAC 2013-ADF [#ref4]_. The parameters r\ :sub:`av`  and q\ :sub:`s`  are only used in COSMO-SAC 2013-ADF. The element specific COSMO-SAC 2013-ADF epsilon constants can be set with the block key  :ref:`EPSILON<keyscheme EPSILON>`. These element specific epsilon constants can not be used in ADF's implementation of earlier COSMO-SAC methods. The parameter rhbcut is only used in COSMO-SAC DHB-ADF [#ref8]_. Note that the parameters for COSMO-SAC DHB-ADF were reoptimized by Chen et al., and are different than in Ref. [#ref8]_.


``hb_temp | hb_notemp``
   If the subkey hb_notemp is included (default) the hydrogen bond interaction is not temperature dependent, as in Refs. [#ref7]_ [#ref5]_ [#ref4]_. If the subkey hb_temp is included the temperature dependence of the hydrogen bond interaction f\ :sub:`hb`  (T) is the same as is described in  :ref:`the section on the temperature dependent hydrogen bond interaction <hydrogen bond interaction>`. 


Except for COSMO-SAC 2013-ADF, some COSMO-RS specific parameters are used in the next COSMO-SAC methods:

::

   COSMOSAC
   SACPARAMETERS
     ...
     {OMEGA       omega}
     {ETA         eta}
   End

.. csv-table:: 
   :widths: 50,100,300
   :header: "symbol", "2013-ADF Xiong", "2016-ADF Chen, DHB-ADF Chen, 2010 Hsieh, 2007 Wang"

   omega (:math:`\omega`), , -0.212
   eta (:math:`\eta`), ,-9.00

In ADF2016 these parameters are not used in the COSMO-SAC 2013-ADF method, only in the ADF implementation of the other COSMO-SAC methods.
The parameters :math:`\omega`, :math:`\eta` and the element specific COSMO-RS dispersion constants are taken from the COSMO-RS model. 
The element specific COSMO-RS dispersion constants can be set with the block key DISPERSION. :math:`\omega`, :math:`\eta`, and the element specific COSMO-RS dispersion constants are used in a COSMO-RS like method for the calculation of pure compound vapor pressures.

COSMO-SAC element specific parameters
=====================================

.. _keyscheme EPSILON: 

::

   COSMOSAC2013
   EPSILON
     {H  epsH}
     {C  epsC}
     {N  epsN}
     {...}
   End

The following table gives the element specific epsilon constants in case of COSMO-SAC 2013-ADF, see Ref. [#ref4]_.
Like in the COSMO-RS method, pure compound vapor pressures can be given as input, for example, if experimental values are available.
In these values ar not given, in ADF2016 the pure compound vapor pressure will be approximated using the the COSMO-SAC 2013-ADF method, which depend on these element specific epsilon constants.
These constants will also have an effect on the calculated activity coefficients in case of a mixture.
Note that these only have an effect in the ADF's COSMO-SAC 2013-ADF implementation.


.. csv-table:: 
   :widths: 150,150
   :header: "element", "2013-ADF Xiong"

   ,"Ref. [#ref4]_"
   H,338.13
   C.sp3,29160.92
   C.sp2,30951.83
   C.sp,20685.98
   N.sp3,23488.54
   N.sp2,22663.34
   N.sp,6390.40
   O.sp3-H,8527.06
   O.sp3,8484.38
   O.sp2,6736.85
   O.sp2-N,12145.28
   Cl,8435.13
   F,82512.21
   P,56067.81
   S,45065.19
   Br,62947.83
   I,105910.88
   
Note that not for all elements in the periodic system COSMO-SAC 2013-ADF parameters were fitted. 

If one leaves the EPSILON block keyword empty the contribution of the mixture dispersion to the activity coefficient will be zero. 

::

   EPSILON
   End


**Links** COSMO-RS GUI tutorial: Expert option: set COSMO-SAC 2013-ADF parameters [`1 <../Tutorials/COSMO-RS/COSMO-RS_overview_parameters_and_analysis.html#step-4-cosmo-rs-and-cosmo-sac-parameters>`__] 

.. _metatag TECHNICAL:

Technical and accuracy parameters
=================================

.. _keyscheme TECHNICAL: 

::

   TECHNICAL
     {RSCONV rsconv}
     {SACCONV sacconv}
     {MAXITER maxiter}
     {BPCONV bpconv}
     {BPMAXITER bpmaxiter}
     {SOLCONV solconv}
     {SOLMAXITER solmaxiter}
     {SOLXILARGE solxilarge}
     {EHDELTAT ehdeltaT}
   End

.. csv-table:: 
   :widths: 100,150
   :header: "symbol", "Default values"

   rsconv,10\ :sup:`-7`  kcal/mol
   sacconv,10\ :sup:`-7` 
   maxiter,10000
   bpconv,10\ :sup:`-6`   bar
   bpmaxiter,40
   solconv,10\ :sup:`-5`   molar fraction
   solmaxiter,40
   solxilarge,0.99  molar fraction
   ehdeltaT,1.0 Kelvin
   
``rsconv``
   Convergence criterion in kcal/mol in chemical potential calculation, not used in COSMO-SAC 2013-ADF. Default value 1e-7 kcal/mol. 

``sacconv``
   Convergence criterion in activity coefficient calculation, only used in COSMO-SAC 2013-ADF. Default value 1e-7. 

``maxiter``
   Maximum number of cycles in chemical potential or activity coefficients calculation. Default value 10000. 

``bpconv``
   Convergence criterion (bar) for isobar or solvent boiling point calculation. Default value 1e-6 bar. 

``bpmaxiter``
   Maximum number of cycles in isobar or solvent boiling point calculation. Default value 40. 

``solconv``
   Convergence criterion (molar fraction) used in solubility calculations. Default value 1e-5 molar fraction. 

``solmaxiter``
   Maximum number of cycles in solubility calculation. Default value 40. 

``solxilarge``
   Threshold for (im-)miscibility (molar fraction) in solubility calculations. Above this value the mixture is considered to be fully miscible. Default value 0.99. 

``ehdeltaT``
   :math:`\Delta T` (Kelvin) used in the calculation of the excess enthalpy using the Gibbs-Helmholtz equation and in the calculation of the enthalpy of vaporization using the Clausius-Clapeyron equation using a numerical derivative with respect to T. Default value 1.0 Kelvin. 

**Links** COSMO-RS GUI tutorial: set COSMO-RS or COSMO-SAC 2013-ADF parameters [`1  <../Tutorials/COSMO-RS/COSMO-RS_overview_parameters_and_analysis.html#step-4-cosmo-rs-and-cosmo-sac-parameters>`__] 


.. only:: html

  .. rubric:: References

.. [#ref1] A.\  Klamt, V. Jonas, T. Bürger and J.C. Lohrenz,  *Refinement and Parametrization of COSMO-RS.*  `J. Phys. Chem. A 102, 5074 (1998) <https://doi.org/10.1021/jp980017s>`__ 

.. [#ref2] C.C. Pye, T. Ziegler, E. van Lenthe, J.N. Louwen,  *An implementation of the conductor-like screening model of solvation within the Amsterdam density functional package. Part II. COSMO for real solvents.*  `Can. J. Chem. 87, 790 (2009) <https://doi.org/10.1139/V09-008>`__ 

.. [#ref3] A.\  Klamt,  *COSMO-RS From Quantum Chemistry to Fluid Phase Thermodynamics and Drug Design, Elsevier.* Amsterdam (2005), ISBN 0-444-51994-7. 

.. [#ref4] R.\  Xiong, S.I. Sandler, R.I. Burnett, *An improvement to COSMO-SAC for predicting thermodynamic properties*,  `Ind. Eng. Chem. Res. 53, 8265 (2014) <https://doi.org/10.1021/ie404410v>`__ 

.. [#ref5] C.M. Hsieh, S.I. Sandler, S.T. Lin, *Improvements of COSMO-SAC for vapor-liquid and liquid-liquid equilibrium predictions*,  `Fluid Phase Equilib. 297, 90 (2010) <https://doi.org/10.1016/j.fluid.2010.06.011>`__ 

.. [#ref6] W.L. Chen, C.M. Hsieh, L. Yang, C.C. Hsu, S.T. Lin, *A Critical Evaluation on the Performance of COSMO-SAC Models for Vapor-Liquid and Liquid-Liquid Equilibrium Predictions Based on Different Quantum Chemical Calculations*,  `Ind. Eng. Chem. Res. 55, 9312 (2016) <https://doi.org/10.1021/acs.iecr.6b02345>`__ 

.. [#ref7] S.\  Wang, S.I. Sandler, C.C. Chen, *Refinement of COSMO-SAC and the Applications*,  `Ind. Eng. Chem. Res. 46, 7275 (2007) <https://doi.org/10.1021/ie070465z>`__ 

.. [#ref8] W.L. Chen, S.T. Lin, *Explicit consideration of spatial hydrogen bonding direction for activity coefficient prediction based on implicit solvation calculations*,  `Phys.Chem.Chem.Phys. 19, 20367 (2017) <https://doi.org/10.1039/c7cp02317k>`__ 
