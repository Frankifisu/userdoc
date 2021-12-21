.. _metatag COSMOSAC: 
.. index:: COSMO-SAC
.. index:: COSMO-SAC 2013-ADF 
.. index:: COSMO-SAC 2016-ADF 
.. index:: COSMO-SAC DHB-ADF 
.. index:: COSMO-SAC theory 
.. index:: theory COSMO-SAC

COSMO-SAC 2013-ADF, 2016-ADF, DHB-ADF
*************************************

On the basis of the framework of COSMO-RS, Lin and Sandler [#ref1]_ suggested a variation, the COSMO-SAC (where SAC denotes segment activity coefficient) model by invoking a necessary thermodynamic consistency criterion. Although there are differences, COSMO-RS and COSMO-SAC share some similarities. Later improvements of COSMO-SAC appeared, like in Refs. [#ref2]_ [#ref3]_ [#ref4]_.

The COSMO-SAC 2013-ADF method used in ADF is the one developed by Xiong et al., which is described in detail in Ref. [#ref4]_. The COSMO-SAC 2013-ADF parameters in Ref. [#ref4]_ were optimized for use with ADF COSMO result files. COSMO-SAC 2013-ADF is an improved COSMO-SAC method compatible to ADF and different than previous COSMO-SAC methods.  The main difference compared to previous COSMO-SAC methods is that the COSMO-SAC 2013 model includes a dispersion contribution in the mixture interaction. 

In Ref. [#ref5]_ COSMO-SAC model parameters were optimized by Chen et al. for different quantum mechanical calculations.
The authors of Ref. [#ref5]_ also reoptimized the revised COSMO-SAC model [#ref3]_ parameters for quantum mechanical calculations with ADF, which will be called here the COSMO-SAC 2016-ADF method.

In Ref. [#ref6]_ a COSMO-SAC model was proposed that uses a directional hydrogen bond approach, denoted as the COSMO-SAC(DHB) model. The parameters were reoptimized by Chen et al. for use with ADF, which will be called here the COSMO-SAC DHB-ADF method.

The ADF COSMO-RS program can calculate activity coefficients using the COSMO-SAC 2013-ADF model or the COSMO-SAC 2016-ADF model.
Like in the COSMO-RS method, pure compound vapor pressures can be given as input, for example, if experimental values are available.
In case of the COSMO-SAC 2013-ADF model, if these values are not specified then the pure compound vapor pressure will be calculated according to the COSMO-SAC 2013-ADF model.
However, in case of COSMO-SAC 2016-ADF, if these values are not specified then the pure compound vapor pressures will be approximated using a method similar as in the COSMO-RS method.
It is also possible to use some earlier COSMO-SAC methods [#ref2]_ [#ref3]_, but note that the  parameters in those papers were not optimized for use with ADF COSMO result files. 

The COSMO-SAC 2013 model includes a dispersion contribution in the mixture interaction.
This dispersion contribution is a complicated expression which also depends on the liquid molar volume of the pure compounds and on the molar volume of the mixture.
The molar volume of the mixture is calculated from the pure compound liquid molar volumes assuming ideal mixing.
In the input for the ADF COSMO-RS program one include for each compound the experimental pure compound liquid density (kg/L), from which the program can calculated the pure compound liquid molar volumes.
If this density is not given the pure compound liquid molar volume will be calculated from its COSMO volume.
Note that in the calculations with the COSMO-SAC 2013-ADF model in Ref. [#ref4]_ often experimental pure compound liquid molar volumes were used. 

.. only:: html

  .. rubric:: References

.. [#ref1] S.T. Lin and S.I. Sandler, *A Priori Phase Equilibrium Prediction from a Segment Contribution Solvation Model*,  `Ind. Eng. Chem. Res. 41, 899 (2002) <https://doi.org/10.1021/ie001047w>`__ 

.. [#ref2] S.\  Wang, S.I. Sandler, C.C. Chen, *Refinement of COSMO-SAC and the Applications*,  `Ind. Eng. Chem. Res. 46, 7275 (2007) <https://doi.org/10.1021/ie070465z>`__ 

.. [#ref3] C.M. Hsieh, S.I. Sandler, S.T. Lin, *Improvements of COSMO-SAC for vapor-liquid and liquid-liquid equilibrium predictions*,  `Fluid Phase Equilib. 297, 90 (2010) <https://doi.org/10.1016/j.fluid.2010.06.011>`__ 

.. [#ref4] R.\  Xiong, S.I. Sandler, R.I. Burnett, *An improvement to COSMO-SAC for predicting thermodynamic properties*,  `Ind. Eng. Chem. Res. 53, 8265 (2014) <https://doi.org/10.1021/ie404410v>`__ 

.. [#ref5] W.L. Chen, C.M. Hsieh, L. Yang, C.C. Hsu, S.T. Lin, *A Critical Evaluation on the Performance of COSMO-SAC Models for Vapor-Liquid and Liquid-Liquid Equilibrium Predictions Based on Different Quantum Chemical Calculations*,  `Ind. Eng. Chem. Res. 55, 9312 (2016) <https://doi.org/10.1021/acs.iecr.6b02345>`__ 

.. [#ref6] W.L. Chen, S.T. Lin, *Explicit consideration of spatial hydrogen bonding direction for activity coefficient prediction based on implicit solvation calculations*,  `Phys.Chem.Chem.Phys. 19, 20367 (2017) <https://doi.org/10.1039/c7cp02317k>`__ 
