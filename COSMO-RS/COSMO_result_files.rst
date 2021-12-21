.. _cosmoresultfile: 

.. only:: html

   .. index:: COSMO result file 

COSMO result files
##################

.. index:: .cosmo file 

COSMO-RS needs as input for the calculation so called COSMO result files for each compound, which are results of quantum mechanical calculation using COSMO.
In ADF such a COSMO result file is called an adf.rkf file (previously ADF<=2019 known as TAPE21 or as a .t21 file) or a COSKF file (.coskf).
With Fast Sigma such a COSMO result file is a COMPKF file (.compkf).
With MOPAC such a COSMO result file is a .cos file, which can be converted to a COSKF file.
In other programs such a file can be a .cosmo file.
ADF has databases of .coskf files, the COSMO-RS compound database :ref:`ADFCRS-2018<ADFCRS-2018>` (including ionic liquids) and the COSMO-RS polymer database :ref:`ADFCRS-2019<ADFCRS-POLYMERS-2019>`.
At `http://www.design.che.vt.edu/VT-Databases.html <http://www.design.che.vt.edu/VT-Databases.html>`__ a database of .cosmo files can be found, which were made with a different program. Note that the optimal COSMO-RS parameters may depend on the program chosen. 

.. toctree::
   :maxdepth: 2

   ADF_COSMO_calculation
   COSMO-RS_Databases
   Fast_Sigma_QSPR_COSMO_sigma-profiles
   MOPAC_COSMO_calculation
