
General
#######

Introduction
************

The ADF COSMO-RS (COnductor like Screening MOdel for Realistic Solvents) program is a program that can be used for calculating thermodynamic properties of (mixed) fluids. The COSMO-RS method was developed by Klamt and coworkers [#ref1]_ [#ref2]_ [#ref3]_. On the basis of the framework of COSMO-RS, Lin and Sandler [#ref6]_ suggested a variation, the COSMO-SAC (where SAC denotes segment activity coefficient) model. There are different implementations of COSMO-RS and COSMO-SAC or derivatives, and different parametrizations. The implementation of COSMO-RS in ADF is described in Ref. [#ref4]_, which is based on the COSMO-RS method developed by Klamt et al. [#ref2]_. The implementation of COSMO-SAC 2013-ADF in ADF is based on the COSMO-SAC model developed by Xiong et al. [#ref7]_. The implementation of COSMO-SAC 2016-ADF in ADF is based on the COSMO-SAC model developed by Hsieh et al. [#ref5]_, but the parameters in COSMO-SAC 2016-ADF were optimized by Chen et al., like in [#ref8]_, for use with ADF. The implementation of COSMO-SAC DHB-ADF in ADF is based on the COSMO-SAC-DHB model developed by Chen et al. [#ref9]_, but the parameters were reoptimized by Chen et al. for use with ADF.

An alternative to COSMO-SAC or COSMO-RS based methods is the UNIFAC (UNIQUAC Functional-group Activity Coefficients) method, which
was developed by Fredenslund, Jones, and Prausnitz, see [#ref10]_.
The empirical UNIFAC method is a group contribution based method to predict activity coefficients and other thermodynamic properties, in which
the group specific parameters and are parametrized against a large data base. The implementation in ADF uses to so called original UNIFAC parameters.

`Our COSMO-RS capabilities are summarized on the product page <https://www.scm.com/product/cosmo-rs>`__. 

With COSMO-RS it is possible to use a thermodynamically consistent combinatorial contribution to the chemical potential as is used in Ref. [#ref3]_, and a temperature dependent hydrogen bond interaction, also described in Ref. [#ref3]_. The parameters in the paper [#ref2]_ were reparametrized for ADF, see Ref. [#ref4]_ for details. 

The parameters in COSMO-SAC 2013-ADF, COSMO-SAC 2016-ADF, and COSMO-SAC DHB-ADF were optimized for use with ADF COSMO result files.
Other COSMO-SAC parameter sets exists that were optimized for different QM packages.

The ADF COSMO-RS (and COSMO-SAC) command line program is called *crs*. The main authors of this program are Cory Pye (Saint Mary's University, Halifax NS Canada) and Jaap Louwen (Albemarle Corporation). COSMO-SAC 2013-ADF was implemented in collaboration with R. Xiong and R.I. Burnett (Sandler group, University of Delaware, Newark, USA). Previous COSMO-SAC methods were implemented by Erin McGarrity (TU Delft, the Netherlands). The COSMO-RS GUI *AMScrs* contains an input builder for COSMO-RS and can visualize results, see the  `COSMO-RS GUI tutorials <../Tutorials/COSMO-RS/index.html>`__ and the `COSMO-RS GUI reference manual <../GUI/AMScrs_COSMO-RS.html>`__. 

COSMO-RS (and COSMO-SAC)  use the intermediate results from quantum mechanical (QM) calculations on individual molecules to predict thermodynamic properties of mixtures of these molecules, for example, solubility. There are a fair number of reports of accurate prediction by COSMO-RS of thermodynamic properties in general in the literature. Many of these have been written by Klamt and co-workers, see Ref. [#ref3]_ and references therein. 
Instead of a relatively expensive QM calculation one can use a fast Quantitative Structure-Property Relationship (QSPR) method to estimate the so called COSMO sigma-profile of a molecule that is needed in COSMO-RS (and COSMO-SAC) calculations.

There are also empirical methods like UNIFAC that can predict thermodynamic properties (including the activity coefficients). These methods contain group specific parameters and are parametrized against a large data base. They will often do better than COSMO-RS or COSMO-SAC methods (especially, of course, if the system of interest was part of the data base used for parameter estimation). An advantage of these methods is that they require no QM calculations to be done in order to provide an estimate of thermodynamics properties.
However, these methods cannot handle every type of molecule. In particular when unusual combinations of functional groups occur (such as in drug molecules), no parametrization is available. COSMO-RS and COSMO-SAC methods, on the other hand, only feature general parameters not specific to chemical groups or functionalities. All that is required is that a quantum mechanical calculation can be done on the molecule. Therefore, COSMO-RS or COSMO-SAC can be a valuable tool for the prediction of chemical engineering thermodynamical properties, like, for example, partial vapor pressures, solubilities, and partition coefficients. An additional advantage of COSMO-RS and COSMO-SAC over empirical methods is that the molecules dissolved may in fact be transition states of a chemical reaction. This follows from the fact that all that is required is that one can do a QM calculation on the solute and QM on a transition state has become standard in the last two decades. This affords a unique opportunity to predict the thermodynamics of a reaction including, for instance, the balance between kinetically and thermodynamically favored reaction pathways as a function of the solvent used. 

Release 2021.1
**************

Changes of COSMO-RS 2021.1 compared to COSMO-RS 2020.1:

* Improved handling of compounds with multi-species components

Release 2020.1
**************

Changes of COSMO-RS 2020.1 compared to COSMO-RS 2019.3:

* Support for compounds with multi-species components

  * conformers
  * dimers, trimers, ...
  * dissociation
  * association


.. only:: html

  .. rubric:: References

.. [#ref1] A.\  Klamt,  *Conductor-like Screening Model for Real Solvents: A New Approach to the Quantitative Calculation of Solvation Phenomena.*  `J. Phys. Chem. 99, 2224 (1995) <https://doi.org/10.1021/j100007a062>`__ 

.. [#ref2] A.\  Klamt, V. Jonas, T. Bürger and J.C. Lohrenz,  *Refinement and Parametrization of COSMO-RS.*  `J. Phys. Chem. A 102, 5074 (1998) <https://doi.org/10.1021/jp980017s>`__ 

.. [#ref3] A.\  Klamt,  *COSMO-RS From Quantum Chemistry to Fluid Phase Thermodynamics and Drug Design, Elsevier.* Amsterdam (2005), ISBN 0-444-51994-7. 

.. [#ref4] C.C. Pye, T. Ziegler, E. van Lenthe, J.N. Louwen,  *An implementation of the conductor-like screening model of solvation within the Amsterdam density functional package. Part II. COSMO for real solvents.*  `Can. J. Chem. 87, 790 (2009) <https://doi.org/10.1139/V09-008>`__ 

.. [#ref5] C.M. Hsieh, S.I. Sandler, S.T. Lin, *Improvements of COSMO-SAC for vapor-liquid and liquid-liquid equilibrium predictions*,  `Fluid Phase Equilib. 297, 90 (2010) <https://doi.org/10.1016/j.fluid.2010.06.011>`__ 

.. [#ref6] S.T. Lin and S.I. Sandler, *A Priori Phase Equilibrium Prediction from a Segment Contribution Solvation Model*,  `Ind. Eng. Chem. Res. 41, 899 (2002) <https://doi.org/10.1021/ie001047w>`__ 

.. [#ref7] R.\  Xiong, S.I. Sandler, R.I. Burnett, *An improvement to COSMO-SAC for predicting thermodynamic properties*,  `Ind. Eng. Chem. Res. 53, 8265 (2014) <https://doi.org/10.1021/ie404410v>`__ 

.. [#ref8] W.L. Chen, C.M. Hsieh, L. Yang, C.C. Hsu, S.T. Lin, *A Critical Evaluation on the Performance of COSMO-SAC Models for Vapor-Liquid and Liquid-Liquid Equilibrium Predictions Based on Different Quantum Chemical Calculations*,  `Ind. Eng. Chem. Res. 55, 9312 (2016) <https://doi.org/10.1021/acs.iecr.6b02345>`__ 

.. [#ref9] W.L. Chen, S.T. Lin, *Explicit consideration of spatial hydrogen bonding direction for activity coefficient prediction based on implicit solvation calculations*,  `Phys.Chem.Chem.Phys. 19, 20367 (2017) <https://doi.org/10.1039/c7cp02317k>`__ 

.. [#ref10] A.\  Fredenslund, R.L. Jones, and J.M. Prausnitz, *Group-contribution estimation of activity coefficients in nonideal liquid mixtures*, `AIChE Journal 21, 1086 (1975) <https://doi.org/10.1002/aic.690210607>`__
