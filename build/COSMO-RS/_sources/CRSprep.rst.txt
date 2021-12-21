.. _CRSPREP: 
.. index:: crsprep module 

CRSprep: generate (multiple) COSMO-RS jobs
******************************************

The module crsprep is intended to facilitate scripting: it makes it easier to construct proper jobs, from within a script.
This module can be used, for example, to run the same type of COSMO-RS job on various compounds, or to change input settings.
This module can also be used to put pure compound data on an ADF COSMO result file.

In $AMSHOME/examples/crs one can find examples that follow the COSMO-RS GUI tutorials, which are also described in the section :ref:`Scripting Examples<EXAMPLES>`.

The most convenient way to see the options of crsprep is to run the crsprep command without arguments.
You will get output very much alike the following description, but probably more up-to-date.

::

   % crsprep -h

   CRSprepare (crsprep) saves pure compound data on an ADF COSMO result file
   or generates a job script for COSMO-RS calculations,
   with user specified changes to input options / method / system.
   Required is at least 1 compound and -savecompound or -t template

   Usage:
      crsprep -savecompound -s compound.coskf
             [-nring nring] [-pvap pvap] [-tvap tvap] [-antoine "A B C"]
             [-meltingpoint meltingpoint] [-hfusion hfusion] [-cpfusion cpfusion]
             [-flashpoint flashpoint] [-density density] [-scalearea scalearea]
      crsprep -t template
             [-s compound.(coskf|compoundlist)] [-c compound.(coskf|compoundlist)]
             [-nring nring] [-pvap pvap] [-tvap tvap] [-antoine "A B C"]
             [-meltingpoint meltingpoint] [-hfusion hfusion] [-cpfusion cpfusion]
             [-flashpoint flashpoint] [-density density] [-scalearea scalearea]
             [-frac1 frac1] [-frac2 frac2]
             [-densitysolvent densitysolvent] [-solphase solphase]
             [-volumequotient volumequotient] [-preset preset]
             [-method method] [-temperature temperature] [-pressure pressure]
             [-iso iso] [-n n] [-inputpurevap inputpurevap]
             [-inputpuredensity inputpuredensity]
             [-sigmax sigmax] [-massfraction] [-file filename] [-j jobname]

   SAVE PURE COMPOUND DATA
   -savecompound
       use to save pure compound data on an existing ADF COSMO result file

   TEMPLATE
   -t template
       use for COSMO-RS property calculation
       template should be one of:
           VAPORPRESSURE, PUREVAPORPRESSURE,
           BOILINGPOINT, PUREBOILINGPOINT, FLASHPOINT,
           LOGP, ACTIVITYCOEF, SOLUBILITY, PURESOLUBILITY,
           BINMIXCOEF, TERNARYMIX, COMPOSITIONLINE,
           SIGMAPROFILE, PURESIGMAPROFILE, SIGMAPOTENTIAl, PURESIGMAPOTENTIAL

   COMPOUNDS
       at least 1 compound is required
   -s file: the special compound(s) to be used, should be a .coskf file,
       or a .compoundlist file. The -s key has to be repeated for each file
   -c file: additional compound(s) to be used, should be a .coskf file,
       or a .compoundlist file. The -c key has to be repeated for each file
       the order of the compounds is: first all compound defined with -s,
       then those with -c
       LOGP, ACTIVITYCOEF, SOLUBILITY: use -s for the solvent and -c for the solutes
       PURESOLUBILITY: use -s for the solute and -c for the solvents

   PURE COMPOUND DATA
   -nring: number of ring atoms 
   -pvap: pure compound vapor pressure (bar) at tvap
   -tvap: at this temperature (Kelvin) pure compound has pressure pvap
   -antoine: Antoine coefficients A, B, and C
   -meltingpoint: melting point (Kelvin)
   -hfusion: enthalpy of fusion (kcal/mol)
   -cpfusion: heat capacity of fusion (kcal/(mol K))
   -flashpoint: flash point (Kelvin)
   -density: liquid density (kg/L)
   -scalearea: COSMO surface area scale factor
       these keys can be repeated for each compound,
       first appearance of the key will be for compound 1, second for compound 2, etc.
       note the order of the compounds

   SOLVENT
   -frac1: define solvent
   -frac2: define solvent 2 (LogP, composition line)
       the -frac1 and -frac2 key have to be repeated for
       each compound that should have a non-default value
       first appearance of the key will be for compound 1, second for compound 2, etc.
       note the order of the compounds
   -densitysolvent: density solvent (kg/L)
   -solphase: pure compound phase solute in solubility calculation
   -volumequotient: molar volume phase 1/molar volume phase 2 (LogP)
   -preset: LogP preset 0, 2, 3, 4, 5
        0: user defined; 2: Octanol/Water; 3: Benzene/Water; 4: Ether/Water;
        5: Hexane/Water

   METHOD, SYSTEM
   -method: COSMO-RS, COSMOSAC2013, COSMOSAC2016
   -temperature: temperature (Kelvin)
       the -temperature key can be used twice to give a range
   -pressure: pressure (bar)
       the -pressure key can be used twice to give a range
   -iso: isotherm, isobar, flashpoint
   -n: number of steps
   -inputpurevap: if 1 use input pure compound pvap and tvap or Antoine equation
   -inputpuredensity: if 1 use input pure compound liquid density
   -sigmax: maximum value sigma (sigma profile, sigma potential)
   -massfraction: use mass fractions

   INPUT FILE
   -file: content of the file will be added at the end of the input for the
       COSMO-RS calculation. The -file key has to be repeated for each file

   OUTPUT
   -j: produce a fully runnable job (as the .job files from AMSjobs),
       using the specified jobname. The job script produces files like jobname.out,
       jobname.crskf etc. Several job scripts can simply be concatenated,
       the results will be stored in different files using the jobname parameter
       the default is a simple run script
   
   EXAMPLES
   crsprep -s benzene.coskf -nring 6 -savecompound
   crsprep -t VAPORPRESSURE -temperature 273.15 -temperature 373.15 -s methanol.coskf
