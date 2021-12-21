.. index:: execution of UNIFAC

Compound Input
**************

Basic Input
===========

In the UNIFAC program, compounds are expected to be input as SMILES strings, and their ratios are expected as mole fractions.  A summary of basic compound input is given below:

.. csv-table:: 
  :widths: 100,320,200
  :header: "Flag", "Purpose", "Example"

   -h , Produces help message , $AMSBIN/unifac --help
   -smiles , Input molecule as SMILES sting , $AMSBIN/unifac -smiles <SMILES1> <SMILES2> ...
   -x , Input the mole fractions , $AMSBIN/unifac -x <mol fraction 1> <mol fraction 2> ...
   -solute, Specify a molecule as a solute, $AMSBIN/unifac -smiles CCC -solute -smiles ...
   -o , Write output to file , $AMSBIN/unifac -o <output file> ...

Note that the -smiles and -x flags are only specified one time and all information ( SMILES strings and mole fractions ) comes after these flags.  It is assumed that the order of the mole fractions after the -x corresponds to the order of the SMILES strings after the -smiles flag.  A simple example demonstrating an activity coefficient calculation for a mixture of three compounds is given below:

.. code-block:: bash

    $AMSBIN/unifac -smiles CCCCCC CCCO CCCCBr -solute -x 0.2 0.3 0.5 -t ACTIVITYCOEF

The -solute flag is used to specify which compounds should be treated as solutes for the PURESOLUBILITY template.  See the PURESOLUBILITY section for more information.  

Physical Property Input
=======================

A number of problem templates require physical property information to be input.  Physical property information should be input directly after a compound's SMILES representation.  A list of the physical property flags and examples of usage are given below:

.. csv-table:: 
  :widths: 100,320,200
  :header: "Flag", "Purpose", "Example"

   -pvap , Vapor pressure (bar) , $AMSBIN/unifac -smiles <SMILES> -pvap 0.43 ...
   -tvap , Temperature (K) corresponding to pvap , $AMSBIN/unifac -smiles <SMILES> -tvap 320.1 ...
   -antoine , Antoine coefficients for compound , $AMSBIN/unifac -smiles <SMILES> -antoine 7.23 1504.2 246.87 ...
   -hfusion , Enthalpy of fusion  in kJ/mol , $AMSBIN/unifac -smiles <SMILES> -hfusion 6.4
   -meltingpoint , Melting point of compound (K) , $AMSBIN/unifac -smiles <SMILES> -meltingpoint 421.12

Below is an example (with synthetic antoine parameters) demonstrating the command line input for a binary mixture calculation (BINMIXCOEF) using vapor pressure estimated from the antoine parameters.

.. code-block:: bash

    $AMSBIN/unifac -smiles "CCCCOCC" -antoine 5 1500 30 \ 
    "CCCCCC" -antoine 6 1234 10 -t BINMIXCOEF

Additionally, we present an example for calculating the solubility of DDT in ethanol.  Since DDT is a solid at room temperature, this requires us to input Enthalpy of Fusion and Melting Point data. 

.. code-block:: bash

    $AMSBIN/unifac -smiles \ 
    "C1=CC(=CC=C1C(C2=CC=C(C=C2)Cl)C(Cl)(Cl)Cl)Cl" -hfusion 26.28 -meltingpoint 383 \ 
    "CCO" -x 0.0 1.0 -t SOLUBILITY


