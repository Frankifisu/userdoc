.. index:: compounds

Compounds
*********

For each compound one has to add the keyword COMPOUND 

.. _keyscheme COMPOUND: 

::

   COMPOUND filename
   {cosmofile}
   {drophbond}
   {NRING nring}
   {FRAC1 frac1}
   {FRAC2 frac2}
   {PVAP pvap}
   {TVAP tvap}
   {Antoine A B C}
   {MELTINGPOINT meltingpoint}
   {HFUSION hfusion}
   {CPFUSION cpfusion}
   {FLASHPOINT flashpoint}
   {DENSITY density}
   {SCALEAREA scalearea}
   End

``filename``
   The filename (can be a full path, otherwise relative path is assumed) should be a COSMO result file. How to make an ADF COSMO result file can be found  :ref:`here<cosmoresultfile>`. 

``cosmofile``
   If the subkey cosmofile is included the file should be an ASCII COSMO file (.cosmo). If not specified (default) the file should be a kf file, either an ADF COSMO result file adf.rkf (previously ADF<=2019 TAPE21 file or .t21 file) or a COSKF file (.coskf).

``drophbond``     
   If the subkey drophbond is included no hydrogen-bond terms will be included for this compound. If not specified (default) the hydrogen-bond terms are included for this compound.   

``nring``     
   The number of ring atoms. This is a COSMO-RS parameter. It should be 6 for benzene, for example. Default value is 0.   

``frac1``     
   The molar fraction of the compound in the solvent (mass fraction if the key MASSFRACTION is used). This is solvent 1 in case of the calculation of partition coefficients (Log P) or in case of a composition line.   

``frac2``     
   The molar fraction of solvent 2 (mass fraction if the key MASSFRACTION is used), only used in case of the calculation of partition coefficients (Log P) or in case of a composition line.   

``pvap, tvap``     
   Pure compound vapor pressure pvap (bar) at temperature tvap (Kelvin). Used only if both pvap and tvap are specified, and then will have an effect on the calculated vapor pressures or boiling points. Alternative is to set the Antoine coefficients. If both are not specified the pure compound vapor pressure is approximated using the COSMO-RS method.   

``A, B, C``     
   A,  B, and  C are the pure compound Antoine coefficients, such that: log P = A - B/(T+C). This Antoine equation is a 3-parameter fit to experimental pure compound vapor pressures P (bar) over a restricted temperature T (Kelvin) range. If the Antoine coefficients are specified this will have an effect on the calculated vapor pressures or boiling points. Alternative is to give input values for the pure compound vapor pressure at a fixed temperature. If both are not specified the pure compound vapor pressure is approximated using the COSMO-RS method.  

``meltingpoint, hfusion, cpfusion``
   Pure compound melting point meltingpoint (Kelvin), pure compound enthalpy of fusion hfusion (kcal/mol), and pure compound heat capacity of fusion cpfusion (kcal/(mol K)). Only used if both meltingpoint and hfusion are specified (cpfusion optional), and will then have an effect in solubility calculations if the temperature of the solvent is below the melting point. 

``flashpoint``
   Pure compound flash point flashpoint (Kelvin). 

``density``
   Pure compound density density (kg/L). Used for calculating the volume of a solvent molecule. 

``scalearea``
   Input scaling of COSMO surface area for a given compound. Default value 1.0 means the COSMO surface area is not scaled. Changing this value is an expert option, for example, to fit to experiment. 

**Links** COSMO-RS GUI tutorial: set pure compound parameters [`1 <../Tutorials/COSMO-RS/COSMO-RS_overview_parameters_and_analysis.html#step-3-set-pure-compound-parameters>`__] 

