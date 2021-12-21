.. index:: execution of UNIFAC

Program Input
*************

List of possible input flags
============================

The UNIFAC program accepts a few additional flags to specify system conditions, choose a template for the calculation, or set the number of points taken over a provided range (e.g., a temperature range).  A summary of these input options is provided below.  In the following section, examples are given for each flag.  

.. csv-table:: 
  :widths: 100,320
  :header: "Flag", "Meaning"

   -t , One of a number of template strings to indicate the problem type
   -temperature , One/two values (K) to specify the system temperature/temperature range
   -n , the number of steps taken if a range is specified or for a BINMIXCOEF or TERNARYMIX calculation
   -preset , an integer to indicate which solvent system is chosen for logP calculations


Examples of general program flags
=================================

In this section, we provide a brief example of each of the above flags.


-t 
---
 
The -t flag has been shown in previous examples and will be described in more detail in the following section.  The -t flag must be followed by one of the following template names: 

::

  LOGP
  ACTIVITYCOEF
  PURESOLUBILITY
  SOLUBILITY
  VAPORPRESSURE
  PUREVAPORPRESSURE
  BINMIXCOEF
  TERNARYMIX

A brief example of this for the ACTIVITYCOEF template is given below:

.. code-block:: bash

    $AMSBIN/unifac -smiles "CCCCO" "CCCOCCC" -x 0.5 0.5 -t SOLUBILITY

-temperature
------------

In this example, we take the previous DDT solubility calculation and perform the calculation at a temperature of 310 K.  This is shown below: 

.. code-block:: bash

    $AMSBIN/unifac -smiles \ 
    "C1=CC(=CC=C1C(C2=CC=C(C=C2)Cl)C(Cl)(Cl)Cl)Cl" -hfusion 26.28 -meltingpoint 383 \ 
    "CCO" -x 0.0 1.0 -temperature 310 -t SOLUBILITY


If we want to calculate the solubility over a temperature range (say, 310-350 K), we need to specify the temperature flag twice and also include a number of steps to take between the two temperatures with the -n flag. This looks like the following:

.. code-block:: bash

    $AMSBIN/unifac -smiles \
    "C1=CC(=CC=C1C(C2=CC=C(C=C2)Cl)C(Cl)(Cl)Cl)Cl" -hfusion 26.28 -meltingpoint 383 \
    "CCO" -x 0.0 1.0 -temperature 310 -temperature 350 -n 10 -t SOLUBILITY

-n 
---

The -n flag specifies a number of steps to take between a temperature range or the number of steps to take along each mole fraction axis for a BINMIXCOEF or a TERNARYMIX calculation.  For an input value of N for the -n flag, the BINMIXCOEF and TERNARYMIX templates consider the following number of distinct mole fraction combinations:

.. csv-table:: 
  :widths: 100,320
  :header: "Template", "Number of distinct systems considered"

   BINMIXCOEF , N+5
   TERNARYMIX , (N+1)(N+2)/2

If we wanted to calculate the thermodynamic properties of a binary mixture with a very small step size, we could input a N value of 1000 to take 1005 samples of the mole fraction space:

.. code-block:: bash

    $AMSBIN/unifac -smiles \
    "CCCCOCC" -antoine 5 1500 30 \ 
    "CCCCCC" -antoine 6 1234 10 \
    -t BINMIXCOEF -n 1000

-preset
-------

The preset flag is used for a logP calculation.  A preset of 2 (default) indicates that that we do a logP calculation on the traditional Octanol/Water system.  This looks like the following:

.. code-block:: bash

  $AMSBIN/unifac -smiles "CCCCOCC" -t LOGP -preset 2


More information on the preset flag options for the LOGP template will be given in the templates section.
