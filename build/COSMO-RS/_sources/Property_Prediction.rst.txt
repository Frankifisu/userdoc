.. _metatag PROPERTY_PREDICTION:

.. only:: html

   .. index:: pure compound properties

Pure compound property prediction
*********************************

.. index:: property prediction

Introduction
============

The Property Prediction program in ADF provides quick, accurate estimates for many important pure component physical properties.  At its core, the Property Prediction program maps various QSPR descriptors of an input molecule onto a single numerical value, the property estimate.  Many of these property models rely on easy-to-evaluate QSPR descriptors and numerically straightforward computations, meaning that an estimate can be provided for every property in << 1s per molecule.  The general expression for the models used in the Property Prediction program is as follows: 

.. math::
    f(P) = C + g \left( \sum\limits_i c_i n_i  \right) + h\left( \sum\limits_i d_i n_i, T \right)

where *f* is a function that transforms the property value space, *g* is a function that maps QSPR descriptors onto a numerical value, and *h* is a function which also captures temperature-dependence of certain properties by including temperature, *T*, as an input.  Additionally, *C* is a constant, :math:`n_i` refers to QSPR values of QSPR descriptor *i*, and :math:`c_i` and :math:`d_i` are fitted coefficients corresponding to each QSPR descriptor *i*. 

.. _ACCEPTED_ATOM_TYPES_TABLE:

The accuracy of the property estimates depends on the nature/complexity of the input molecular structure.  For many common organic structures, the property estimates should be reasonably accurate.  However, as is always the case with QSPR models, the Property Prediction program will likely lose accuracy for molecules outside its training domain, i.e., for molecules that are very "dissimilar" to compounds which occur in the training set.  In general, the program can be used for molecules with the following atom types:

.. csv-table:: 
  :widths: 100,320
  :header: "Accepted atom types", "Example functional groups which can be used with atom type"

   H, "Alkanes, Alkenes, Alkynes, Aldehydes, Amides, Amines, Aromatics, Carboxylic Acids, Hydroxides, Sulfides, Thiols"
   C, "Acid chlorides, Alkanes, Alkenes, Alkynes, Aldehydes, Amides, Aromatics, Carboxylic Acids, Esters, Ethers, Ketones, C-X (halogens)"
   N, "Amides, Amines, Aromatics, Cyanides, Imines, Nitro groups"
   O, "Acid chlorides, Aldehydes, Amides, Aromatics, Carboxylic Acids, Esters, Ethers, Ketones, Nitro groups"
   F, "-CF, -CF2, -CF3"
   S, "Sulfides, Thiols"
   Cl, "Acid chlorides, -CCl, -CCl2, -CCl3"
   Br, "-CBr"
   I, "-CI"

A brief description of molecule types for which this method will not work well is given in the `General warnings section <Property_Prediction.html#general-warnings>`__.  Common molecules for which this method will fail are: (1) those that contain only one non-hydrogen atom, e.g., Methane or Water; (2) those that contain atoms not listed in the table above.

Available properties
====================

The Property Prediction program can predict the values of various pure component physical properties.  These properties can be of interest themselves or can be used in conjunction with other COSMO-RS property calculations (e.g., to calculate the solubility of a solid in a liquid, we must know the enthalpy of fusion and melting point of the solid -- both of these properties can be estimated with the Property Prediction program). The available properties and their units are listed below:

.. csv-table:: 
  :widths: 200,100, 100, 300
  :header: "Property Name", "Units", "Additional Information", "Typical error"

  Boiling point, K, at 1 atm, 15 K 
  Critical Pressure, bar, , 1.5 bar
  Critical Temperature, K, , 30 K
  Critical Volume, L/mol, , 0.02 L/mol
  Dielectric Constant, ,, 3
  Ideal Gas Entropy, J/(mol K), at 298.15 K and 1 bar, 20 J/(mol K)
  Flash point, K , , 15 K 
  Gibbs Energy Ideal Gas, kJ/mol, at 298.15 K and 1 bar , 25 kJ/mol
  Enthalpy of Combustion, kJ/mol, at 298.15 K , 50 kJ/mol
  Std. Enthalpy of Formation, kJ/mol, at 298.15 K and 1 bar , 30 kJ/mol
  Enthalpy of Fusion, kJ/mol, at Normal Melting Point, 4 kJ/mol
  Enthalpy of Form. Ideal Gas , kJ/mol, at 298.15 K and 1 bar, 25 kJ/mol
  Enthalpy of Sublimation, kJ/mol , , 5 kJ/mol
  Melting point, K, at 1 atm , 35 K 
  Liquid Molar volume, L/mol, at 298.15 K, 0.005 L/mol 
  (Liquid Density), kg/L, at 298.15 K , uses Liquid Molar Volume
  Liquid Vapor Pressure, bar,  , 10-30%
  Parachor, , , 7
  Solubility Parameter, (cal/cm^3)^1/2, at 298.15 K , 0.7
  Triple point temperature, K, , 35 K 
  Van der Waals Area,  Å², , 6 Å²
  Van der Waals Volume,  Å³, , 3 Å³

Running the Property Prediction program
=======================================

The Property Prediction program can be run from the command line.  The following general flags are used by the program:

.. csv-table:: 
  :widths: 100,320,200
  :header: "Flag", "Purpose", "Example"

   ``-h [--help]`` , Produces help message , ``$AMSBIN/prop_prediction --help``
   ``-s [--smiles]`` , Input molecule as SMILES sting , ``$AMSBIN/prop_prediction --smiles <SMILES> ...``
   ``-m [--mol]`` , Input molecule as .mol file , ``$AMSBIN/prop_prediction --mol <mol file> ...``
   ``--temperature``, Set temperature/range (K), ``$AMSBIN/prop_prediction --temperature 298.15 ...``
   ``-n`` , number of steps for temperature range , ``$AMSBIN/prop_prediction --n 20 ...``
   ``-d [--display]`` , Display calculated properties , ``$AMSBIN/prop_prediction --d ...``
   ``-o [--output]`` , Write output to file , ``$AMSBIN/prop_prediction --o <output file> ...``

Note, if no output flag is supplied, then the results are written to a file called CRSKF by default.  Additionally, the user may enter as many compounds as desired on the command line in either of the two available input formats.    

The program can be run in 2 ways:

+ Estimating all available properties for every molecule
+ Estimating specific properties for every molecule

To estimate all properties for every input compound, simply execute the program with all molecules specified on the command line.  Don't forget that the -d flag is required to display the results in the terminal.  An example of this is below.

.. code-block:: bash

   $AMSBIN/prop_prediction --smiles CCCCCCO -o example.crskf -temperature 298.15 -temperature 398.15 -n 20 -d
    
::

    
   Boiling point at standard pressure : 
   CCCCCCO              435.777  K  
   Critical pressure : 
   CCCCCCO              34.3493  bar       
   Critical temperature : 
   CCCCCCO              576.466  K    
   Critical volume  : 
   CCCCCCO             0.404124  L/mol     
   Liquid density : 
   CCCCCCO              0.79182  kg/L      
   Dielectric constant : 
   CCCCCCO              10.9512            
   Absolute entropy of an ideal gas at 298.15 K and 1 bar : 
   CCCCCCO              439.885  J/(mol K) 
   Flash point : 
   CCCCCCO              342.271  K         
   Gibbs energy of formation for an ideal gas at 298.15 K and 1 bar : 
   CCCCCCO             -131.869  kJ/mol    
   Net enthalpy of combustion at 298.15 K  : 
   CCCCCCO             -3678.12  kJ/mol    
   Standard state enthalpy of formation at 298.15 K and 1 bar : 
   CCCCCCO             -384.388  kJ/mol    
   Enthalpy of fusion at normal melting point : 
   CCCCCCO              18.5054  kJ/mol    
   Enthalpy of formation for an ideal gas 298.15 K : 
   CCCCCCO             -316.821  kJ/mol    
   Enthalpy of sublimation : 
   CCCCCCO              80.9799  kJ/mol    
   Melting point at 1 atm : 
   CCCCCCO              231.141  K         
   Liquid molar volume : 
   CCCCCCO             0.128949  L/mol     
   Parachor : 
   CCCCCCO              289.059            
   Solubility parameter : 
   CCCCCCO              10.1294  (cal/cm^3)^0.5 
   Triple point temperature : 
   CCCCCCO              230.404  K         
   Van der Waals area : 
   CCCCCCO              171.059  Å^2      
   Van der Waals volume : 
   CCCCCCO              120.519  Å^3      
   Liquid vapor pressure : 
   Molecule: CCCCCCO        
      Temperature (K)     Vapor pressure (bar)
       298.15                 0.001229
       303.15                 0.001809
       308.15                 0.002623
       313.15                 0.003750
       318.15                 0.005289
       323.15                 0.007362
       328.15                 0.010123
       333.15                 0.013757
       338.15                 0.018487
       343.15                 0.024582
       348.15                 0.032357
       353.15                 0.042182
       358.15                 0.054484
       363.15                 0.069757
       368.15                 0.088563
       373.15                 0.111537
       378.15                 0.139394
       383.15                 0.172929
       388.15                 0.213022
       393.15                 0.260644
       398.15                 0.316852
 

For most applications, it is not necessary to calculate all of the available physical properties (although doing so is practically just as fast).  In these cases, additional property flags need to be specified on the command line to restrict the program to calculating only certain physical properties.  For example, if we were doing solid/liquid solubility calculations on Ibuprofen and Paracetamol, we would require the Enthalpy of Fusion and the Melting Point of both compounds.  To calculate only these two properties, we simply have to add the two property flags "-hfusion" and "-meltingpoint" to the command line.  Using the .mol file for Ibuprofen and the SMILES string for Paracetamol, we execute the following: 

.. code-block:: bash

   $AMSBIN/prop_prediction -d -m Ibuprofen.mol -s 'CC(=O)NC1=CC=C(C=C1)O' -hfusion -meltingpoint
    
::

   Enthalpy of fusion at normal melting point : 
   CC(=O)NC1=CC=C(C=C1)O      33.0298  kJ/mol    
   Ibuprofen.mol              24.0336  kJ/mol

   Melting point at 1 atm : 
   CC(=O)NC1=CC=C(C=C1)O      469.282  K         
   Ibuprofen.mol              331.887  K


Index of property keys 
======================

The available properties and their corresponding property flags are listed below:

.. csv-table:: 
   :widths: 200,200
   :header: "Property Name", "Property Flag"

   Boiling point, ``--boilingpoint``
   Critical Pressure, ``--criticalpressure``
   Critical Temperature, ``--criticaltemp``
   Critical Volume, ``--criticalvol``
   Dielectric Constant, ``--dielectricconstant``
   Ideal Gas Entropy, ``--entropygas``
   Flash point, ``--flashpoint``
   Gibbs Energy Ideal Gas, ``--gidealgas``
   Enthalpy of Combustion, ``--hcombust``
   Std. Enthalpy of Formation, ``--hformstd``
   Enthalpy of Fusion, ``--hfusion``
   Enthalpy of Form. Ideal Gas , ``--hidealgas``
   Enthalpy of Sublimation, ``--hsublimation``
   Melting point, ``--meltingpoint``
   Liquid Molar volume, ``--molarvol``
   (Liquid Density), ``--molarvol``
   Liquid Vapor Pressure, ``--vaporpressure``
   Parachor, ``--parachor``
   Solubility Parameter, ``--solubilityparam``
   Triple point temperature, ``--tpt``
   Van der Waals Area, ``--vdwarea``
   Van der Waals Volume,  ``--vdwvol``


General warnings
================

This method will **fail** for the following types of molecules:

+ Those that contain *only one non-hydrogen atom* (e.g., Methane or Water).  However, experimental data is ample for these small molecules.  The vapor pressure model is the exception in that it *can* represent such small structures.  
+ Those that contain atoms or substructures that are not listed in the :ref:`Accepted atom types table <ACCEPTED_ATOM_TYPES_TABLE>` above.  
+ Polymers and Ionic Liquids

This method will **lose accuracy** for some properties in the following domains:

+ Molecules with *many different types of functional groups*
+ Molecules that are *extremely light* (< 3 non-Hydrogen atoms) or *heavy* (> 30 non-Hydrogen atoms)

Equations for temperature-dependent properties
==============================================

**VPM1**: liquid vapor pressure
-------------------------------

.. math::
    ln(P) = A/T + Bln(T) + CT + D

.. csv-table:: 
   :widths: 200,200
   :header: "Symbol", "Meaning"

   P, vapor pressure
   T, absolute temperature
   "A,B,C,D", estimated constants
