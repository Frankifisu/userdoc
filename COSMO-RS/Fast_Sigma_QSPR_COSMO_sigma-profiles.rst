.. _metatag FAST_SIGMA: 
.. index:: QSPR COSMO file
.. index:: Fast Sigma COSMO file
.. index:: Fast Sigma COSMO settings

Fast Sigma: a QSPR method to estimate COSMO sigma-profiles
**********************************************************

Introduction
============

The Fast Sigma program reads a molecule in SMILES format and estimates all of the properties required for a COSMO-RS/-SAC calculation: the HB-/Non-HB-/OT-/OH- :math:`\sigma`-profiles, COSMO surface area, and COSMO volume.  This code uses QSPR techniques similar to those applied in our `Property Prediction program <./Property_Prediction.html>`__.  The efficiency of these techniques means that this program can provide estimates for these essential COSMO-RS/-SAC properties in milliseconds.  This allows for quick estimates to be done for a new molecule of interest as well as drastically expedited searches through screening databases of molecular candidates as compared to the full-fledged COSMO-RS strategy, which requires costly DFT calculations. 

Input options
=============

A list of the input options and examples of their usage is given below.

.. csv-table:: 
  :widths: 100,320,200
  :header: "Flag", "Purpose", "Example"

   -h [--help] , Produces help message , $AMSBIN/fast_sigma --help
   -s [--smiles] , Input molecule as SMILES sting , $AMSBIN/fast_sigma --smiles <SMILES> ...
   -m [--mol] , Input molecule as .mol file , $AMSBIN/fast_sigma --mol <mol file> ...
   -d [--display] , Display problem results, $AMSBIN/fast_sigma -d ...
   -o [--output] , Write output to file , $AMSBIN/fast_sigma --o <output.compkf> ...
   --method , Chose a COSMO-RS/-SAC method , $AMSBIN/fast_sigma --method COSMO-RS ...

There are currently two supported methods: **COSMO-RS** and **COSMOSAC2016**.  One of these method names must be entered after the --method flag.  The default method is COSMO-RS.

.. index:: .compkf file

``<output.compkf>``
    The fast sigma program writes the output results to a file in .compkf format.  The chosen output filename should generally end with .compkf.  This suffix helps other parts of the code (COSMO-RS/-SAC/-UNIFAC/Solvent Optimization) recognize the format and use the file accordingly.  If no filename is supplied the program writes to a file called CRSKF.  

``SMILES_string or .mol file``
    Though COSMO-RS/-SAC can make estimates for many types of molecular species, the fast sigma program currently only supports organic, neutral, closed shell molecules. 

GUI Input
=========

The simplest way to use the Fast Sigma program is through the COSMO-RS GUI.  There are two ways to do this:

* SMILES string:  **Compounds → List of Compounds → Add Compound using QSPR (Fast Sigma) → SMILES** and select Add.
* .xyz file: **Compounds → List of Compounds → Add Compound using QSPR (Fast Sigma) → .xyz**, and select Add.

A .compkf file will be saved that can be used as input in COSMO-RS calculations. 

Examples
========

This example calculates COSMO-RS (the default) parameters for phenol:

.. code-block:: bash
    
    $AMSBIN/fast_sigma --smiles "c1ccccc1(O)" -d

::

           sigma value       Total profile          HB profile
                -0.025               0.000               0.000
                -0.024               0.000               0.000
                -0.023               0.000               0.000
                -0.022               0.002               0.002
                -0.021               0.054               0.054
                -0.020               0.263               0.263
                -0.019               0.523               0.523
                -0.018               0.684               0.684
                -0.017               0.828               0.828
                -0.016               0.801               0.801
                -0.015               0.732               0.716
                -0.014               0.642               0.597
                -0.013               0.653               0.519
                -0.012               0.678               0.487
                -0.011               0.607               0.423
                -0.010               0.567               0.382
                -0.009               0.646               0.245
                -0.008               4.183               0.023
                -0.007               7.405               0.000
                -0.006               7.912               0.000
                -0.005               6.701               0.000
                -0.004               5.544               0.000
                -0.003               4.658               0.000
                -0.002               3.899               0.000
                -0.001               4.097               0.000
                 0.000               6.109               0.000
                 0.001               7.854               0.000
                 0.002               8.640               0.000
                 0.003               9.726               0.000
                 0.004              11.175               0.000
                 0.005              12.524               0.000
                 0.006               8.673               0.000
                 0.007               2.255               0.000
                 0.008               1.174               0.161
                 0.009               1.279               1.159
                 0.010               1.442               1.442
                 0.011               1.759               1.751
                 0.012               1.795               1.788
                 0.013               0.838               0.829
                 0.014               0.095               0.093
                 0.015               0.054               0.054
                 0.016               0.030               0.030
                 0.017               0.000               0.000
                 0.018               0.000               0.000
                 0.019               0.000               0.000
                 0.020               0.000               0.000
                 0.021               0.000               0.000
                 0.022               0.000               0.000
                 0.023               0.000               0.000
                 0.024               0.000               0.000
                 0.025               0.000               0.000
           Molecular Mass =        94.0418648120 g/mol
               COSMO Area =       127.5012207186 Angstrom**2
             COSMO Volume =       122.0791950835 Angstrom**3
    Gas Phase Bond Energy =        -2.9875007647 Hartree
              Bond Energy =        -2.9968155744 Hartree
               Dispersion =        -4.5319123638 kcal/mol
               Deltaediel =         0.0000000000 Hartree
                    Nring =         6
         Chemical Formula =         C6H6O
                   SMILES =         c1ccccc1(O)


Additionally, we calculate the COSMOSAC2016 parameters for Ibuprofen as a mol file:

.. code-block:: bash
    
    $AMSBIN/fast_sigma --mol Ibuprofen.mol --method COSMOSAC2016 -d

::


           sigma value       Total profile          OH profile          OT profile
                -0.025               0.000               0.000               0.000
                -0.024               0.000               0.000               0.000
                -0.023               0.000               0.000               0.000
                -0.022               0.000               0.000               0.000
                -0.021               0.009               0.009               0.000
                -0.020               0.062               0.061               0.000
                -0.019               0.395               0.385               0.000
                -0.018               0.914               0.881               0.000
                -0.017               0.925               0.879               0.000
                -0.016               0.840               0.781               0.000
                -0.015               0.652               0.590               0.000
                -0.014               0.697               0.606               0.000
                -0.013               0.604               0.499               0.000
                -0.012               0.561               0.398               0.000
                -0.011               0.725               0.418               0.000
                -0.010               0.833               0.350               0.000
                -0.009               1.282               0.230               0.000
                -0.008               2.141               0.158               0.000
                -0.007               5.133               0.085               0.000
                -0.006              10.428               0.048               0.000
                -0.005              14.386               0.000               0.000
                -0.004              23.816               0.000               0.000
                -0.003              26.081               0.000               0.000
                -0.002              23.295               0.000               0.000
                -0.001              21.443               0.000               0.000
                 0.000              22.124               0.000               0.000
                 0.001              20.652               0.000               0.000
                 0.002              24.315               0.036               0.000
                 0.003              15.722               0.086               0.035
                 0.004              11.878               0.171               0.092
                 0.005              13.670               0.288               0.197
                 0.006              10.405               0.381               0.307
                 0.007               5.479               0.561               0.413
                 0.008               3.525               0.713               0.613
                 0.009               3.358               0.823               1.055
                 0.010               3.879               0.639               1.840
                 0.011               4.503               0.180               3.025
                 0.012               2.708               0.083               2.006
                 0.013               0.930               0.020               0.745
                 0.014               0.061               0.000               0.104
                 0.015               0.000               0.000               0.000
                 0.016               0.000               0.000               0.000
                 0.017               0.000               0.000               0.000
                 0.018               0.000               0.000               0.000
                 0.019               0.000               0.000               0.000
                 0.020               0.000               0.000               0.000
                 0.021               0.000               0.000               0.000
                 0.022               0.000               0.000               0.000
                 0.023               0.000               0.000               0.000
                 0.024               0.000               0.000               0.000
                 0.025               0.000               0.000               0.000
           Molecular Mass =       206.1306798160 g/mol
               COSMO Area =       278.4276940312 Angstrom**2
             COSMO Volume =       279.3341044098 Angstrom**3
    Gas Phase Bond Energy =        -7.1463537624 Hartree
              Bond Energy =        -7.1619486814 Hartree
               Dispersion =        -9.7153055452 kcal/mol
               Deltaediel =         0.0007518662 Hartree
                    Nring =         0
         Chemical Formula =         C13H18O2
                   SMILES =         CC(C)Cc1ccc(C(C)C(=O)O)cc1
