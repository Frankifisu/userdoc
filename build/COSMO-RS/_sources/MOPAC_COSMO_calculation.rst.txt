.. _metatag MOPAC_SETTINGS: 
.. index:: MOPAC COSMO file
.. index:: MOPAC COSMO settings

MOPAC COSMO calculation
***********************

Here it is described briefly how to make MOPAC COSMO result files. 

The simplest way is to use AMSinput. Draw the molecule using AMSinput, and save the .ams file. Select **Right Panel → MOPAC → Solvation method → COSMO-CRS**. Select 362 for NSPA. Press Run to run the MOPAC calculation. A .coskf file will be saved that can be used as input in COSMO-RS calculations. 

In AMS2019 AMSinput uses the MOPAC engine, which is part of the AMS driver.
Note that this is different than in AMS2018 and before.
In the Atoms block key in the AMS driver part of the input one puts the coordinates of the molecule.
The main input keys for the AMS driver and the MOPAC engine are:

::

   $AMSBIN/ams << eor
   Task GeometryOptimization
   System
       Atoms
          ....
       End
   End

   Engine MOPAC
       Solvation
           Enabled Yes
           NSPA 362
           Solvent
               Name CRS
           End
       End
   EndEngine

   eor

.. index:: .cos file

The use of the solvent CRS makes the MOPAC engine to create a .cos file, which is converted to a .coskf file by  $AMSBIN/cosmo2kf

::         

   cosmo2kf file.cos file.coskf


Note that this is automatically done if one uses AMSinput.   

Compared to the default ADF COSMO-RS values a few  :ref:`COSMO-RS parameters<COSMO-RS parameters>` were reoptimized for MOPAC PM6 COSMO result files to improve the calculation of a number of partition coefficients, when compared to experimental values. Note that MOPAC is a semi-empirical quantum chemistry program, whereas ADF is based on density functional theory (DFT). Thus the MOPAC COSMO result files will not be of the same quality as the ADF COSMO result files.   
