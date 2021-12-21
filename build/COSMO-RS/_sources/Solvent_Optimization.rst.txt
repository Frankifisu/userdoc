.. _metatag SOLVENT_OPTIMIZATION: 

.. only:: html

   .. index:: solvent optimization

Solvent Optimization
********************

.. index:: optimizing the solvent

Introduction
============

The choice of solvent or solvent system can have a dramatic impact on the solubility of solutes, the performance of the solvent system for liquid-liquid extraction, or reaction rates/selectivities for many chemical reactions.  The solvent is also one of the most accessible variables in formulation/reaction/extraction design as many of the other species in these problems (active ingredients, co-solvents, reactants, catalysts, extracts, raffinates, etc. ) are often fixed or tightly constrained. However, the solvent selection problem is combinatorially complex and non-trivial.  As an example of this complexity, consider the problem of choosing up to 4 solvents for a process from a set of 100 possible solvents.  The number of combinations alone is over 4 million, a number that makes laboratory- or pilot-scale testing for every system untenable.  An additional complication is that the identities of the solvents alone do not determine a solvent system: we must also know the mole fractions.  Of course, there are an infinite number of possible mole fraction values for a solvent system ( a value of :math:`x_1 = 0.3 ,\, x_2=0.7` is just as valid as :math:`x_1 = 0.29999 ,\, x_2=0.70001` ), meaning a high-throughput approach would still require multiple mole fraction values for each solvent system to effectively sample the mole fraction space.

Luckily, the complexity of this problem can be addressed with modern mathematical optimization approaches.  Following the approach of [#ref1]_, we re-structure the COSMO-RS/-SAC parameters and equations and incorporate them into a Mixed Integer Nonlinear Programming (MINLP) formulation.  Using this generic formulation, we can apply a number of optimization solvers and solution techniques to the problem of determining an optimal solvent system.  We note that the optimization methods currently in use only guarantee local solutions, but the formulation should be robust enough to provide high-quality solutions for many types of problems.  In fact, for most of our example problems, our optimization approach was able to find the globally optimal solution (as determined by an exhaustive enumeration of the solvent space and dense sampling of the mole fractions space).  There are additionally some features in the program (e.g., the -multistart flag) which help to provide a diversity of starting conditions so the solvers can find high-quality solutions.

.. index:: optimizing solubility
.. index:: liquid-liquid extraction

Problem types
=============

At present, the program has two problem templates:

+ The **SOLUBILITY** template: this selects a solvent system and mole fractions in order to maximize or minimize the mole fraction solubility of a solid solute in the liquid mixture.  Note that currently only solid/liquid equilibria calculations are supported. 
+ The **LLEXTRACTION** template: this selects a two-phase solvent system and mole fractions in order to maximize (or minimize) the distribution ratio (D) of two solutes between the two liquid phases.  The distribution ratio for these problems is defined in terms of mole fractions rather than concentrations.  The formula for this is given in an equation below.  Note that LLEXTRACTION problems will fail if all possible solvents are miscible.

Because liquid densities are not always known, we calculate the distribution ratio (D) in terms of mole fractions.  The liquid-liquid phase equilibrium condition provides an equivalent expression for D.  More precisely, this means that D can be calculated as follows:

.. math::

  D = max \left( \frac{\gamma_1^I}{\gamma_1^{II}} \frac{\gamma_2^{II}}{\gamma_2^I}, \frac{\gamma_2^I}{\gamma_2^{II}} \frac{\gamma_1^{II}}{\gamma_1^I} \right)

where :math:`\gamma_i^j` represents the activity coefficient of solute *i*  in phase *j*.  Here, we assume that the two solutes to be separated are indexed with :math:`i \in \{1,2\}`.  The max operator, though not used in the optimization problem itself, allows us to express the correct value of D in the equation above.  In other words, the max operator removes the dependence of the D value on arbitrary indexing of solutes and phases.  

.. note:: 

    For LLEXTRACTION problems, the mole fractions of the solutes are fixed to 0 unless they are also specified as solvents.  This means that the distribution coefficient is calculated using the infinite dilution activity coefficients.


A brief summary of what to expect for solvent optimization problems using the two templates is given below:

.. csv-table:: 
  :widths: 100,150,150
  :header: "", "SOLUBILITY","LLEXTRACTION"

   Minimum number of solvents, 1, 2
   Preferred number of solvents, >1, >4
   Typical solution times, <2s, 1-30s
   Recommended multistarts, <5 if any, 5-10
   Warmstart recommended, No, Problem-dependent

The warmstart and multistart options will be explained in a later section.


Running the Solvent Optimization program
========================================

The Solvent Optimization program can be run from the command line.  The following general flags are used by the program:

.. csv-table:: 
  :widths: 100,320,200
  :header: "Flag", "Purpose", "Example"

   -h [--help] , Produces help message , $AMSBIN/solvent_opt --help
   -s [--smiles] , Input molecule as SMILES sting , $AMSBIN/solvent_opt --smiles <SMILES> ...
   -m [--mol] , Input molecule as .mol file , $AMSBIN/solvent_opt --mol <mol file> ...
   -c [--coskf] , Input molecule as .coskf file , $AMSBIN/solvent_opt --coskf <.coskf file> ...
   -d [--display] , Display problem results, $AMSBIN/solvent_opt --d ...
   -o [--output] , Write output to file , $AMSBIN/solvent_opt --o <output file> ...

Additionally, physical properties required for the calculation can be input on the command line.  Presently, only two physical properties (Enthalpy of Fusion and Melting Point) are required for certain calculations.  These flags must follow a molecule input and be followed by the property value.  Some examples are given below:

.. csv-table:: 
  :widths: 80,100, 300
  :header: "Flag", "Property", "Example"

   -hfusion  , H of Fusion (kJ/mol), $AMSBIN/solvent_opt -c Ibuprofen.coskf -hfusion 26.6 ...
   -meltingpoint  , Melting point (K),  $AMSBIN/solvent_opt -c Ibuprofen.coskf -meltingpoint 349.2 ...

Optimization problem specifications and method options can be input with the following flags:

.. csv-table:: 
  :widths: 80,100, 300
  :header: "Flag", "Meaning", "Example"

   -method  , Choice of method (COSMO-RS COSMOSAC2016), ... -method COSMO-RS ...
   -max  , maximize the Solubility/Extraction ratio, 
   -min,  minimize the Solubility/Extraction ratio, 
   -solute, specify which molecules are solutes, ... -s CCCO -solute ...
   -t [--template], choose a problem template, ... -t LLEXTRACTION ...
   -temperature, input 1 or 2 temperatures (K), ... -temperature 298.15 ...

Note that, like the -hfusion and -meltingpoint flags, the -solute flag comes *after* a compound identifier (SMILES string/filename).

Finally, there are two more optimization problem flags which can be altered for problems that do not converge.  The first is the -multistart flag.  This flag takes an integer *N* as input and instructs the algorithm to begin from *N* randomly-generated starting points.  This can be useful for difficult problems because not only will the algorithm begin from more starting points, but it will also adjust internal parameters every time a problem fails.  The -warmstart flag instructs the main algorithm to attempt to make the convert the initial starting point to a high-quality, feasible starting point which can then be given to the optimization algorithm.  This option can be helpful for many problems, especially those with small numbers of solvents or LLEXTRACTION problems where the solvents are extremely immiscible (e.g., Water and n-Hexane).  A summary of these options is presented below:

.. csv-table:: 
  :widths: 80,100, 300
  :header: "Flag", "Meaning", "Example"

   -multistart  , Start from a number of random starting points, ... -multistart 5 ...
   -warmstart  , Use the warmstart strategy, $AMSBIN/solvent_opt --warmstart ...


Examples
========

In this section, we provide a few example problems to demonstrate a few of the features available in the Solvent Optimization program.  We first do a sample problem with the SOLUBILITY template, and then we provide an example of the usage of the LLEXTRACTION template.

Solubility
----------

For a first example, we determine a mixture of solvents to maximize the solubility of Paracetamol.  For the purposes of illustrating features, we assume that we do not have an available .coskf file for Paracetamol and must use its SMILES string.  We can use a few common solvents from the ADFCRS-2018 database:

.. code-block:: bash 

  $AMSBIN/solvent_opt -t SOLUBILITY -d -max \
    -s "CC(=O)NC1=CC=C(C=C1)O" -solute -meltingpoint 443.1 \ 
    -c $AMSHOME/atomicdata/ADFCRS-2018/Acetic_acid.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Hexane.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Toluene.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Butanoic_acid.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Ethanol.coskf


::
  
  ================================================
         Estimating missing property values       
  ================================================

                                        Estimated values                                    
  --------------------------------------------------------------------------------------
   Molecule                                     Missing Property    Estimated Value
  --------------------------------------------------------------------------------------
   CC(=O)NC1=CC=C(C=C1)O                        Hfusion             7.89433        
  --------------------------------------------------------------------------------------


  ================================================
       Beginning solvent optimization problem     
  ================================================

  **********************************************
                   Iteration 1
  **********************************************
                                     
  Initial guess x1:   0.0235183      
  Initial guess x2:   0.0758477      
  Initial guess x3:   0.220089       
  Initial guess x4:   0.283974       
  Initial guess x5:   0.314382       
  Initial guess x6:   0.082189       
  ------> Solver Status: CONVERGED 
  Objective value: 0.159729
  ---------------------------------------------------------------------------------
                                   Variable values 
  ---------------------------------------------------------------------------------
                x1:   0.159729       CC(=O)NC1=CC=C(C=C1)O
                x2:   0              Acetic_acid.coskf
                x3:   0              Hexane.coskf
                x4:   0              Toluene.coskf
                x5:   0              Butanoic_acid.coskf
                x6:   0.840271       Ethanol.coskf

 



The problem correctly selects Ethanol as the solvent in which Paracetamol is most soluble.  Single solvent solutions are common in SOLUBILITY problems as often no mixed solvent system outperforms single solvents.  Notice that in this example any required property values for solid/liquid equilibria that are missing are estimated based on the input SMILES string.  Because the -meltingpoint flag provided a value for the Melting Point, only the Enthalpy of Fusion is estimated. 

Liquid-liquid extraction
------------------------

Our next example focuses on a classic liquid-liquid extraction problem: separating Acetic acid and Water.  In this example, we assume that we want to replace a standard solvent for this extraction (n-Hexane) with something more environmentally-friendly.  Consulting GSK's Solvent Selection Guide [#ref2]_, we restrict our problem to the solvents with the fewest issues: Water, 1-Butanol, 2-Butanol, t-Butyl acetate, Isopropyl acetate, Propyl acetate, and Dimethyl carbonate.  

.. code-block:: bash

  $AMSBIN/solvent_opt -d -t LLEXTRACTION -max \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Acetic_acid.coskf -solute \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Water.coskf -solute \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Water.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/1-Butanol.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/2-Butanol.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/tert-Butyl_acetate.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Isopropyl_acetate.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Propyl_acetate.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Dimethyl_carbonate.coskf

Notice that water is repeated because it is both a solute and a solvent in the solvent space.  The output produced is the following:

::

  Removing duplicate entry: /home/austin/amshome/atomicdata/ADFCRS-2018/Water.coskf
  ================================================ 
       Beginning solvent optimization problem     
  ================================================

  **********************************************
                   Iteration 1
  **********************************************
                      Phase I        Phase II       
  Initial guess x1:   0.0818796      0.241048       
  Initial guess x2:   0.162378       0.185238       
  Initial guess x3:   0.198892       0.0429676      
  Initial guess x4:   0.114387       0.152842       
  Initial guess x5:   0.0267187      0.0437898      
  Initial guess x6:   0.232349       0.042073       
  Initial guess x7:   0.112232       0.182333       
  Initial guess x8:   0.071164       0.109708       
  ------> Solver Status: CONVERGED 
  Objective value: 232.779
  ---------------------------------------------------------------------------------
                                   Variable values 
  ---------------------------------------------------------------------------------
                x1:   0              0                   Acetic_acid.coskf
                x2:   0.994592       0.0358616           Water.coskf
                x3:   0              0                   1-Butanol.coskf
                x4:   0              0                   2-Butanol.coskf
                x5:   0.000100098    0.186012            tert-Butyl_acetate.coskf
                x6:   0              0                   Isopropyl_acetate.coskf
                x7:   0              0                   Propyl_acetate.coskf
                x8:   0.00530747     0.778127            Dimethyl_carbonate.coskf
  ---------------------------------------------------------------------------------
                                  Extraction values             
  ---------------------------------------------------------------------------------
   Distribution            
   coefficient (D)         log10(D)            
   ---------------------------------
   232.779                  2.36694             

  Solute 1 ID:        Acetic_acid.coskf
  Solute 2 ID:        Water.coskf

                     -------------------------                              
                          Partition ratio           Partition                          
                      Phase I        Phase II       coefficient (P)     log10(P)       
                     -------------------------------------------------------------
  Solute 1:           1              8.39321        0.119144            -0.923928      
  Solute 2:           27.7342        1              27.7342             1.44302        



In this problem, we obtain a mostly aqueous phase and a dimethyl carbonate/tert-butyl acetate phase as the solution.  This solvent system provides a distribution coefficient (D) of 232.779.  This is a good value for a separation, but it is still worse than the distribution coefficient of the water/hexane solvent system (D = 1372.14) by roughly a factor of 6.

We then increase our solvent search space to include the solvents deemed to have "some isssues" by GSK and are also present in our database: Ethanol, 1-Propanol, 2-Propanol, Methanol, Ethyl acetate, Methyl acetate, Methyl isobutyl ketone, Acetone, p-xylene, Toluene, Isooctane, Cyclohexane, Heptane, and DMSO.  

.. code-block:: bash
  
  $AMSBIN/solvent_opt -d -t LLEXTRACTION -max \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Acetic_acid.coskf -solute \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Water.coskf -solute \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Water.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/1-Butanol.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/2-Butanol.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/tert-Butyl_acetate.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Isopropyl_acetate.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Propyl_acetate.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Dimethyl_carbonate.coskf
    -c $AMSHOME/atomicdata/ADFCRS-2018/Ethanol.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/1-Propanol.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/2-Propanol.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Methanol.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Ethyl_acetate.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Methyl_acetate.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Methyl_isobutyl_ketone.coskf \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Acetone.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/p-Xylene.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Toluene.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/2,2,4-Trimethylpentane.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Cyclohexane.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Heptane.coskf  \
    -c $AMSHOME/atomicdata/ADFCRS-2018/Dimethyl_sulfoxide.coskf 


This produces the following: 

::

  ...
  ---------------------------------------------------------------------------------
                                   Variable values 
  ---------------------------------------------------------------------------------
                ...
                x2:   0.999972       7.50215e-05         Water.coskf
                ...
                x15:  5.58242e-06    0.00252496          Methyl_isobutyl_ketone.coskf
                ...
                x20:  2.27012e-05    0.9974              Cyclohexane.coskf
                ...
  ---------------------------------------------------------------------------------
                                  Extraction values             
  ---------------------------------------------------------------------------------
   Distribution            
   coefficient (D)         log10(D)            
   ---------------------------------
   1892.42                  3.27702             

  Solute 1 ID:        Acetic_acid.coskf
  Solute 2 ID:        Water.coskf

                    -------------------------                              
                          Partition ratio           Partition                          
                      Phase I        Phase II       coefficient (P)     log10(P)       
                     -------------------------------------------------------------
  Solute 1:           7.04343        1              7.04343             0.847784       
  Solute 2:           13329.1        1              13329.1             4.1248         



As shown, this solvent system has a D value of 1892.42, better than that of the hexane/water system.  Removing cyclohexane from the possible solvents, we still obtain a solution with a D value of 1891.09.  Successively removing the best non-aqueous solvents from the solvent list, we obtain solutions with D values of: 1864.41, 1645.38, 1597.42, and finally 232.779 again.  The number of good solutions for this problem lends credence to the idea of using such a solvent selection algorithm in general extraction design.  

Additionally, there is a `tutorial on solvent optimization <../Tutorials/COSMO-RS/COSMO-RS_overview_properties.html#step-12-solvent-optimizations-optimize-solubility>`__ which demonstrates running the program from the COSMO-RS GUI.

Guidelines for difficult problems
=================================

The Solvent Optimization program should produce high-quality solutions for many problems.  However, there may be examples where the algorithm struggles to produce solutions at all.  Below we list troubleshooting guidelines to help solve problematic solvent optimizations:

**(1) For LLEXTRACTION problems, ensure that there are at least 2 immiscible solvents**

Because the LLEXTRACTION template requires that both the liquid-liquid phase equilibria condition is met and that there are two distinct liquid phases, the Solvent Optimization program will fail if all of the available solvents are miscible in all mole fractions (no phase separation is possible).  

**(2) Re-execute the program several times**

The Solvent Optimization program is not entirely deterministic.  In particular, starting points are selected at random for every iteration.  These starting points affect the convergence of the problem and in some cases can have a large impact on the optimization.  This means that if one execution of the Solvent Optimization program fails to produce a solution, then it is possible that a subsequent execution could succeed.  If the program continues to fail after multiple attempts at re-execution, consider using the *multistart* or *warmstart* flags.

**(3) Use the -multistart flag**

This flag executes the program multiple times from multiple starting points.  If problems fail, the program uses information from these problems and updates internal optimization parameters to aid in the convergence of successive problems.  Because each iteration takes a relatively short amount of time, the multistart flag can be used with high numbers of different starting points.  It is useful to first try a smaller number of multistarts (5-15).  If this produces no solution, try using the -warmstart flag in addition to the multistarts.  If the problems continue to fail, use gradually higher numbers of multistarts (20,40,60,80,100+).  

**(4) Use the -warmstart flag**

If this flag is present, the program attempts to find a good starting point for LLEXTRACTION problems rather than simply using the randomly-generated starting point.  This can be useful with or without the -multistart flag and is very problem-dependent.  In our experience, LLEXTRACTION problems sometimes have difficulty converging if there are a small number of solvents and/or if the solution contains two highly-immiscible liquids (e.g., Hexane/Water).  We reiterate that this is very problem-dependent.

Differences from standard implementations
=========================================

The COSMO-RS method of the Solvent Optimization program is nearly identical to the ADF combi2005 implementation (the default COSMO-RS method).  The single difference is that there is no *f_corr* parameter in the Solvent Optimization implementation.  This parameter is used for the perpendicular component of the sigma values and has only a small effect on the results.  Removing it from the Solvent Optimization program was done to improve solution times and robustness.  Though the calculated values will be similar, results from the Solvent Optimization program can easily be input to ADFCRS and checked against the full ADF combi2005 method if desired.

The COSMOSAC2016 implementation in Solvent Optimization is identical to the 2016-ADF Chen implementation in ADFCRS.

To reproduce the results from the Solvent Optimization program to within tolerance, parameters must be changed in the GUI or from the command line.  The following parameter changes are required:

.. csv-table:: 
  :widths: 100,100
  :header: "Method", "Required parameter changes"

   COSMO-RS , set *f_corr* to 0
   COSMOSAC2016 , none

In the current version of the program, the COSMO-RS/-SAC parameters *cannot* be changed/customized.  

.. only:: html

  .. rubric:: References

.. [#ref1] N.D. Austin, N.V. Sahinidis, D.W. Trahan, *COSMO-based computer-aided molecular/mixture design: A focus on reaction solvents*, `AIChE Journal 64, 104 (2018) <https://doi.org/10.1002/aic.15871>`__

.. [#ref2] GSK Solvent Selection Guide. Accessed 1/9/18. `<http://www.rsc.org/suppdata/gc/c0/c0gc00918k/c0gc00918k.pdf>`__
