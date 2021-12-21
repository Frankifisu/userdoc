
Analysis
********

.. _metatag SIGMA_PROFILE: 
.. index:: sigma profile 

Sigma profile
=============

The sigma profile of a mixture can be calculated with: 

.. _keyscheme PROPERTY_sigmaprofile: 

::

   PROPERTY sigmaprofile
   {Nprofile nprofile}
   {SigmaMax sigmamax}
   End

In case of a mixture the mole fraction of each compound in the mixture should be given with the subkey  FRAC1 of the key COMPOUND for this compound. 

The sigma profile pure compounds can be calculated with: 

.. _keyscheme PROPERTY_puresigmaprofile: 


::

   PROPERTY puresigmaprofile
   {Nprofile nprofile}
   {SigmaMax sigmamax}
   End

``nprofile``
   Number of data points for which to calculate the sigma profile. default value 50. 

``sigmamax``
   The sigma profile is calculated between -sigmamax and sigmamax. Default value 0.025. 

The hydrogen bonding part (HB) of the sigma profile(s) will also be calculated. In case of a COSMO-SAC 2013-ADF calculation also the OH component of hydrogen bonding (HB-OH) is calculated, and the other type component of hydrogen bonding (HB-OT) is calculated. 

**Links** COSMO-RS GUI tutorial: sigma profile [`1 <../Tutorials/COSMO-RS/COSMO-RS_overview_parameters_and_analysis.html#step-6-analysis-the-sigma-profile>`__] 

.. _metatag SIGMA_POTENTIAL: 
.. index:: sigma potential: 

Sigma potential
===============

The sigma potential of a mixture can be calculated with: 

.. _keyscheme PROPERTY_sigmapotential: 

::

   PROPERTY sigmapotential
   {Nprofile nprofile}
   {SigmaMax sigmamax}
   End

In case of a mixture the mole fraction of each compound in the mixture should be given with the subkey  FRAC1 of the key COMPOUND for this compound. 

The sigma profile pure compounds can be calculated with: 

.. _keyscheme PROPERTY_puresigmapotential: 

::

   PROPERTY puresigmapotential
   {Nprofile nprofile}
   {SigmaMax sigmamax}
   End

``nprofile``
   Number of data points for which to calculate the sigma potential. default value 50. 

``sigmamax``
   The sigma potential is calculated between -sigmamax and sigmamax. Default value 0.025. 

**Links** COSMO-RS GUI tutorial: sigma potential [`1 <../Tutorials/COSMO-RS/COSMO-RS_overview_parameters_and_analysis.html#step-7-analysis-the-sigma-potential>`__] 

