.. index:: execution of UNIFAC

Templates
*********

The -t flag indicates which of several problem types, or templates, should be used.  Different templates expect different input options and produce different results.  A summary of the different templates is given below.

ACTIVITYCOEF
============

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , >= 2
   Mole fraction values (-x) required , Yes
   -solute flag used , No
   -antoine or pvap/tvap required , No
   -hfusion/-meltingpoint required , No

The activity coefficient template calculates activity coefficients from a set of mole fraction values.  In the following example, we calculate the activity coefficients of the water/propanol system over a temperature range of 230-298.15 K.

.. code-block:: bash

  $AMSBIN/unifac -smiles "O" "CCCO" -x 0.2 0.8 \ 
  -t ACTIVITYCOEF -temperature 230 -temperature 298.15 -n 20


LOGP
====

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , >= 1
   Mole fraction values (-x) required , No
   -solute flag used , No
   -antoine or pvap/tvap required , No
   -hfusion/-meltingpoint required , No


The logP template calculate the partition coefficient (P) of input structures between a variety of common liquid/liquid systems.  The specific set of liquids can be chosen with the -preset flag.  A summary of the -preset options is given below:

.. csv-table:: 
  :widths: 100,100
  :header: "-preset value", "Liquid phases"

   2 , Octanol/Water
   3 , Benzene/Water
   4 , Diethyl ether/Water
   5 , Hexane/Water


In the following example, we calculate the logP of Sertraline in the Octanol/Water system. 

.. code-block:: bash

  $AMSBIN/unifac -smiles "CNC1CCC(C2=CC=CC=C12)C3=CC(=C(C=C3)Cl)Cl" -t LOGP -preset 2

PURESOLUBILITY
==============

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , >= 2
   Mole fraction values (-x) required , No
   -solute flag used , Yes
   -antoine or pvap/tvap required , No
   -hfusion/-meltingpoint required , if solute is a solid


The pure solubility template calculates the solubility of a solute (designated by the -solute flag) in a variety of pure solutes.  More specifically, the solute's solubility is calculated in every one of the other input molecules.  

In the following example we calculate the solubility of Undecanedioic acid (a solid at 298.15 K) in n-Hexane, Benzene, Water, and Ethanol.

.. code-block:: bash

  $AMSBIN/unifac -smiles \ 
  "C(CCCCC(=O)O)CCCCC(=O)O" -hfusion 39.65 -meltingpoint 385 -solute \
  "CCCCCC" "c1ccccc1" "O" "CCO" -t PURESOLUBILITY

SOLUBILITY
==========

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , >= 2
   Mole fraction values (-x) required , Yes
   -solute flag used , No
   -antoine or pvap/tvap required , No
   -hfusion/-meltingpoint required , if solute is a solid


The solubility template calculates the solubility of every input molecule in the system defined by the remaining molecules.  For example, assume we input a system with molecules A, B, and C with mole fractions 0.2, 0.6, and 0.2.  The solubility of molecule A is then calculated in a mixture of B/C where the mole fraction ratio is fixed to 3/1 (from the 0.6/0.2 in the input).  The solubility of A may very well be 0.6, but this would mean the remaining mole fractions would be 0.3/0.1 (B/C).  The same calculation is then also done for B and C.  

In the following example we calculate the solubilities of Benzene, n-Hexane, 1-Hexanol, and Acetic acid.  Note that the mole fraction of Benzene is set to 0.0.  This means that Benzene's solubility will still be calculated, but it will not be part of the solvent system when the other molecules' solubilities are being calculated.

.. code-block:: bash

  $AMSBIN/unifac \ 
  -smiles "c1ccccc1" "CCCCCC" "CCCCCCO" "CC(=O)O" \
  -x 0.0 0.2 0.3 0.5 -t SOLUBILITY


PUREVAPORPRESSURE
=================

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , >= 1
   Mole fraction values (-x) required , No
   -solute flag used , No
   -antoine or pvap/tvap required , Yes
   -hfusion/-meltingpoint required , No


The pure vapor pressure template simply calculates the vapor pressure of a pure component.  Because this requires the antoine parameters as input, this template simply evaluates the antoine equation, possibly over a temperature range.

The following example calculates the pure vapor pressure (again using synthetic antoine coefficients) for two molecules over a temperature range:

.. code-block:: bash

  $AMSBIN/unifac \
  -smiles "c1ccccc1" -antoine 4 1245 123 \
  "CCCCC" -antoine 5 1241 242 \
  -t PUREVAPORPRESSURE -temperature 320 -temperature 350 -n 10

VAPORPRESSURE
=============

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , >= 1
   Mole fraction values (-x) required , Yes
   -solute flag used , No
   -antoine or pvap/tvap required , Yes
   -hfusion/-meltingpoint required , No


The vapor pressure template calculates the vapor pressure of a mixture (or a pure component if only one compound is entered).  This again requires the antoine parameters for each compound as input.

We repeat the previous example, now calculating the vapor pressure of the 0.2/0.8 mole fraction mixture.

.. code-block:: bash

  $AMSBIN/unifac \
  -smiles "c1ccccc1" -antoine 4 1245 123 \
  "CCCCC" -antoine 5 1241 242 \
  -x 0.2 0.8 \
  -t VAPORPRESSURE -temperature 320 -temperature 350 -n 10

BINMIXCOEF
==========

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , 2
   Mole fraction values (-x) required , No
   -solute flag used , No
   -antoine or pvap/tvap required , Yes
   -hfusion/-meltingpoint required , No


The binary mixture template takes exactly 2 compounds as input.  Unlike other templates where thermodynamic properties are calculated over a range of temperatures, the binary mixture template calculates properties over a range of mole fractions.  In other words, it takes a number of samples of the mole fraction space.  If no antoine coefficients are given, then no gas phase thermodynamic properties are reported.  

In this example we calculate binary mixture properties for the Water/Ethanol system (again with synthetic antoine parameters).

.. code-block:: bash

  $AMSBIN/unifac -smiles "O" -antoine 4 1245 123 "CCO" \ 
  -antoine 5 1241 242 -t BINMIXCOEF -n 10

TERNARYMIX
==========

.. csv-table:: 
  :widths: 100,100

   Number of compounds required , 3
   Mole fraction values (-x) required , No
   -solute flag used , No
   -antoine or pvap/tvap required , Yes
   -hfusion/-meltingpoint required , No


The ternary mixture template takes exactly 3 molecules as input and performs similar calculations to those done in the binary mixture template.  Note that tie lines are not calculated like they are in the COSMO-RS/-SAC programs.  

In this example we add a Acetone to our previous two compounds and change the temperature to 330 K. 

.. code-block:: bash

  $AMSBIN/unifac -smiles "O" -antoine 4 1245 123 
  "CCO" -antoine 5 1241 242 \
  "CC(=O)C" -antoine 6 2414 221 \
  -t TERNARYMIX -n 20 -temperature 330



