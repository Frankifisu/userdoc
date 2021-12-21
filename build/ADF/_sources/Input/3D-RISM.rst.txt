.. index:: 3D-RISM 
.. index:: RISM 
.. _3D-RISM: 


3D-RISM: 3D reference Interaction Site Model 
============================================

**Introduction** 

The three-dimensional reference interaction site model (3D-RISM) provides the solvent structure in the form of a 3D site distribution function, :math:`g_{\gamma}^{UV}(r)`, for each solvent site, :math:`\gamma`.

It enables, at modest computational cost, the calculations of thermodynamics, electronic properties and molecular solvation structure of a solute molecule in a given molecular liquid or mixture. Using 3D-RISM, one can study chemical reactions, including  reaction coordinates and transition state search, with the molecular solvation described from the first principles based on a molecular-mechanics type description of the solvent. The method yields all of the features available by using other solvation approaches.

The 3D-RISM implementation has been revised and supplemented by a new option that uses the fitted electron density in the interaction between solvent and solute directly. Without the use of point charges, numerical stability has been improved. Using this option, 3D-RISM can now be used for structure optimization, (numerical) frequencies, vertical excitation energies and magnetic properties. The code has also been parallelized. Details can be found in Ref. [#ref1]_.

Details on the original implementation of 3D-RISM-KH in ADF can be found in Ref. [#ref2]_, with applications in Ref. [#ref3]_. 
The theory of 3D-RISM-KH in combination with DFT can be found in Refs. [#ref6]_ [#ref7]_ [#ref8]_ [#ref5]_. A combination of 3D-RISM-KH with FDE (frozen-density embedding) can be found in Ref. [#ref4]_. 

Similar to explicit solvent simulations, 3D-RISM properly accounts for chemical peculiarities of both solute and solvent molecules, such as hydrogen bonding and hydrophobic forces, by yielding the 3D site density distributions of the solvent. Moreover, it readily  provides, via analytical expressions, all of the solvation thermodynamics, including the solvation free energy potential, partial molar volume and compressibility. Due to the complicated electrostatic interaction function used here (which is not based on fixed point charges), the energetic and entropic decomposition of the solvation free energy can only be obtained numerically. The expression for the solvation free energy (and its derivatives) in terms of integrals of the correlation functions follows from a particular approximation for the so-called closure relation used to complete the integral equation for the direct and total correlation functions. 

**Solvation free energy**

The solvation free energy can be calculated as: 
  | Solvation Free Energy =
  | [ (Total Bonding Energy) + (Internal Energy) 
  |       - T * (Entropy) + (Excess Chemical Potential) ]_3D-RISM
  | - [ (Total Bonding Energy) + (Internal Energy) - T * (Entropy) ]_Gas-Phase 

If one assumes that the internal energy and the vibrational and rotational entropy of the solute molecule is the same in solution and in gas phase, then this simplifies to: 
  | Solvation Free Energy = 
  | [ (Total Bonding Energy) + (Excess Chemical Potential) ]_3D-RISM 
  | - [ (Total Bonding Energy)]_Gas-Phase 

However, a formally accurate calculation should include the difference between the thermal corrections from frequency calculations produced by ADF in the SCF calculation with 3D-RISM solvation and in gas phase. 

**Input**

When performing 3D-RISM simulations, each atom in the **ATOMS** block in the AMS part of the input must have two Lennard-Jones parameters specified, adf.SigU and adf.EpsU, for example: 

::

 System
    ATOMS
      C     0.00    0.00    0.00     adf.SigU=3.50    adf.EpsU=0.066
      ...
    END
 End

They can be obtained from a Lennard-Jones force-field parameter set. 

All other 3D-RISM-related input keys are contained in a **RISM** input block. Below, only the mandatory keywords are shown. Optional keywords are described in the next section. 

.. _keyscheme RISM: 


::

  RISM title
    RISM1D
      FLUIDPARAM temper=298. DielConst=78.497 UTotDens=1/A3 0.03333
    SUBEND
    SOLVENT ArbitrarySolventName
      UNITS uWeight=g/mol  ULJsize=A  ULJenergy=kcal/mol Ucoord=A Udens=1/A3
      PARAMETERS Weight=weight nAtoms=NSiteTypes
        N1    Z_alpha1   Sigma_alpha1   Eps_alpha1   X1_1 Y1_1 Z1_1
                                                     X1_2 Y1_2 Z1_2
                                                     ...  ...  ...
        N2    Z_alpha2   Sigma_alpha2   Eps_alpha2   X2_1 Y2_1 Z2_1
                                                     X2_2 Y2_2 Z2_2
                                                     ...  ...  ...
        ...
        DENSPE=density
    SUBEND
    SOLUTE ArbitrarySoluteName
      BOXSIZE   sizeX  sizeY  sizeZ
      BOXGRID    npX    npY    npZ
    SUBEND
  END

The **RISM1D** sub-block contains general parameters for the preceding 1D-RISM calculation of the solvent(s) to create the bulk susceptibility function. Even though all technical RISM1D sub-keys have reasonable defaults, the FLUIDPARAM sub-key will most likely require attention because its default values for density and dielectric constant are only applicable if the solvent is water. Thus, you may need to change these values when modeling a different solvent. Note that even when using all default values from the RISM1D sub-block the sub-block itself must be specified, even if empty. See below for complete description of the RISM1D sub-block.  

The **SOLVENT** sub-block can be repeated for each component if the solvent is a mixture. Each SOLVENT sub-block contains parameters for one solvent. First, each solvent has a name, which is specified on the SOLVENT keyword's line and is arbitrary. The first line in the SOLVENT sub-block must contain the UNITS key. Usually, only the Udens part should be changed. Then follow the actual solvent  parameters. In principle, each solvent consists of multiple atoms and functional groups (so called sites). For example, in 3D-RISM terms, methanol consists of 3 sites: CH\ :sub:`3` , O, and H. Each such site has a set of three parameters, shared between all sites of the same type,  and the coordinates. These parameters follow the PARAMETERS keyword. The line with the PARAMETERS keyword itself must specify the molecular weight of the solvent and the number of site types that follow. The first line for each site type contains, in this order: number of equivalent sites of this type,  :math:`z_\alpha` (the point charge assigned) , :math:`\sigma_\alpha` , :math:`\epsilon_\alpha` (the Lennard-Jones parameters assigned), three coordinates for the first site of this type. If there is more than one site of this type then the coordinates for the 2nd and other sites follow on subsequent lines. The SOLVENT sub-block is concluded by the specific density of this solvent, by default, in molecules per cubic angstrom. This number should be equal to the total density for mono-component solvents. 
Using Udens=MOL, the specific density needs to be given in molar fractions, and should therefore be one for mono-component solvents. 

For example, the SOLVENT block for water would typically look as: 

::

  SOLVENT water
    UNITS      uWeight=g/mol  ULJsize=A  ULJenergy=kcal/mol Ucoord=A Udens=1/A3
    PARAMETERS Weight=18.015   nAtoms=2
      1    -0.8476   3.166    0.1554       0.000000  0.00000 -0.064605
      2     0.4238   1.000    0.0560      -0.816495  0.00000  0.512747
                                           0.816495  0.00000  0.512747
    DENSPE=0.03333
  SUBEND

The **SOLUTE** sub-block specifies 3D-RISM parameters for your molecule. The BOXSIZE and BOXGRID sub-keys specify dimensions of the simulation box, in Angstrom, and the number of points of grid in each direction. The box should at least be twice as large as the molecule and the BOXGRID values must be even numbers. Due to the 3D-FFT routines, the largest prime factor of the BOXGRID values should be 7 for optimal performance. The size/np ratio defines the grid spacing in each direction and this should be not larger than 0.5 angstrom for energy calculations and not larger than 0.35 angstrom for structure optimizations. When the BOXSIZE and BOXGRID keywords are not specified the grid is calculated based on the GRIDSTEP and BOXEXTENT values, see below. The number of grid points along the Cartesian coordinate *i* will then be determined as :math:`N_i = (range(i) + 2*BOXEXTENT)/GRIDSTEP + 1`, where *range(i)* is the span of Cartesian coordinate *i* of the solute molecule. The number of grid points may be increased to be a product of prime numbers not larger than 7. 

The **optional** 3D-RISM keys for the RISM1D and SOLUTE sub-blocks are listed below together with their defaults. 

::

  ! optional RISM1D subkeys with their default values:
  RISM1D Theory=RISM Closure=KH
    FLUIDPARAM temper=298. DielConst=78.497 UTotDens=1/A3 0.03333
    OUTPUT PrintLev=5 File=solvent
    GRID   Nr=8192  dR=0.025 MaxRout=100.0 MaxKout=0.0
    MDIIS  N=20 Step=0.5 Tolerance=1.e-12
    ELSTAT LRsmear=1.0 Adbcor=0.5
    ITER  Ksave=-1 Kshow=1 Max=10000
  SUBEND

``RISM1D``
   Theory - Version of 1D-RISM used: RISM - extended RISM, DRISM - dielectrically consistent RISM (should be used for solvents with a static dipole moment)

   Closure - Closure for the 1D problem: KH - Kovalenko-Hirata, HNC - hypernetted chain, PSEn - partial series expansion of HNC up to order n (n=1 is identical to KH), PY - Perkus-Yevik

``FLUIDPARAM``
   Temper - temperature; 

   DielConst - dielectric constant (only used when theory=DRISM); 

   UTotDens - units for total density: G/CM3, KG/M3, 1/A3 are valid units followed by the density value. 

``OUTPUT`` 
   PrintLev - print level; 
   
   File - common base name for output files; 

   OutList - which information will be written to additional output files (no additional information will be written by default): G - distribution function,  C - direct correlation function, H - total correlation function, U - interaction function, X - ".xvv" file (Only required up to ADF2019), T - thermodynamics. 

``GRID``
   Nr - the size of the 1D-RISM grid, must be a power of 2 (max. value: 16384); 

   dR - mesh size in Angstrom; 

   MaxRout - plot range in direct space; 

   MaxKOut - plot range in reciprocal space. 

``MDIIS``
   N - number of vectors in the DIIS space; 

   Step - step size; 

   Tolerance - convergence criterion. 

``ELSTAT``
   LRsmear - smearing parameters for coulomb potential; 

   Abdcor - switching parameter for dielectric correction (only used if theory=DRISM).

``ITER``
   Ksave - save the current solution every Ksave steps (0 - do not save); 

   Kshow - print convergence progress every Kshow steps; 

   Max - maximum number of iterations. 

::

  SOLUTE ArbitrarySoluteName
    outlist=M  closure=KH  xvvfile=solvent.xvv outfile=rism3d
    Nis=10  DELOZ=0.5 TOLOZ=2.0e-6
    Ksave=-1  Kshow=1  Maxste=10000
    Output=4
    CHRGLVL=ZLM
    GRIDSTEP=0.33
    BOXEXTENT=12.0
  SUBEND

Outlist - output requested: M - detailed output for the excess chemical potential , F - some corrections (GF, PC+, ...) to the excess chemical potential , G - distribution function, C - direct correlation function, H - total correlation function; 

Closure - closure for the 3D problem: KH – Kovalenko-Hirata, HNC - hypernetted chain approximations, PSEn - partial series expansion of HNC up to order n (n=1,2,...; n=1 is identical to KH);

Xvvfile - name of the file with the results of the 1D-RISM calculation specified in the RISM1D keyword above, with .xvv appended to it (Only used up to ADF2019); 

Outfile - name of the output text files; 

Output - print level; 

CHRGLVL - which charges computed by ADF to use. This can be ZLM (default), MDCq, MDCd, MDCm, or EXMDC (labeled EXACT in older versions);

SPHINT - calculate the spherical averaged distribution function around the given atom: 1,2,... - atom in input order , 0 - Center of mass;

OLDCODE - Run the old version of the code (ADF2019 and older), incompatible with CHRGLVL=ZLM or analytical gradients;

GRIDSTEP - Grid spacing, in Angstrom.

BOXEXTENT - Extent of the grid, in Angstrom, beyond the space occupied by atoms in each direction.

The Nis, DELOZ, and TOLOZ have the same meaning for 3D-RISM as parameters of the MDIIS keyword of the RISM1D block. Likewise, Ksave, Kshow, and Maxste are analogous to the parameters of the ITER key in RISM1D. 

**Parameters for some solvents**

The following, compiled set of solvent parameters is taken from the literature (see Ref. [#ref1]_ and references therein for these and additional solvents).

.. csv-table:: **Water Weight=18.015 nAtoms=2**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  O,  -0.8476,  3.166, 0.1554 , 0.000000 ,  0.000000 , -0.064605
  H,  0.4238 ,  1.000, 0.0560 , 0.000000 ,  0.816495 ,  0.512747
   ,         ,       ,        , 0.000000 , -0.816495 ,  0.512747



.. csv-table:: **Methanol Weight=32.04 nAtoms=3**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  H    ,  0.435, 1.000, 0.0560, 1.35136 , 0.00000 , 1.39716
  O    , -0.700, 3.070, 0.1700, 0.00000 , 0.00000 , 0.94500
  CH3  ,  0.265, 3.775, 0.2070, 1.35136 , 0.00000 , 1.39716



.. csv-table:: **Ethanol Weight=47.07 nAtoms=4**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  H    ,  0.435, 1.000, 0.0560, 0.000000 , 0.000000 , 0.000000
  O    , -0.700, 3.070, 0.1700, 0.000000 , 0.000000 , 0.945000
  CH2  ,  0.265, 3.775, 0.2070, 1.356103 , 0.000000 , 1.398746
  CH3  ,  0.000, 3.905, 0.1750, 1.342751 , 0.000000 , 2.928687



.. csv-table:: **Isopropanol Weight=60.10 nAtoms=4**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  H    ,  0.435, 1.000, 0.0560, 0.000000 ,  0.000000 , 0.000000
  O    , -0.700, 3.070, 0.1700, 0.000000 ,  0.000000 , 0.945000
  CH   ,  0.265, 3.850, 0.0800, 1.356103 ,  0.000000 , 1.398746
  CH3  ,  0.000, 3.910, 0.1600, 1.578230 ,  1.268465 , 2.224915
       ,       ,      ,       , 1.578230 , -1.268465 , 2.224915



.. csv-table:: **Acetonitrile Weight=41.052 nAtoms=3**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  CH3 ,  0.150, 3.775, 0.2070,  1.458000 , 0.000000 , 0.000000
  C   ,  0.280, 3.650, 0.1500,  0.000000 , 0.000000 , 0.000000
  N   , -0.430, 3.200, 0.1700, -1.157000 , 0.000000 , 0.000000



.. csv-table:: **Dimethylsulfoxide Weight=78.13 nAtoms=3**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  O   , -0.459, 2.930, 0.2800,  0.000000 ,  0.000000 ,  1.530000
  S   ,  0.139, 3.560, 0.3950,  0.000000 ,  0.000000 ,  0.000000
  CH3 ,  0.160, 3.810, 0.1600,  0.000000 ,  1.716700 , -0.541300
      ,       ,      ,       , -1.665300 , -0.416800 , -0.541300



.. csv-table:: **Acetone Weight=58.08 nAtoms=3**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  O   , -0.424, 2.960, 0.2100, 0.000000 ,  0.000000 , -1.208737
  C   ,  0.300, 3.750, 0.1050, 0.000000 ,  0.000000 ,  0.013263
  CH3 ,  0.062, 3.910, 0.1600, 0.000000 ,  1.286301 ,  0.798425 
      ,       ,      ,       , 0.000000 , -1.286301 ,  0.798425 



.. csv-table:: **Dichloromethane Weight=84.93 nAtoms=3**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  C   , -0.364, 3.400, 0.1094,  0.000000 ,  0.000000 , -0.814053
  H   ,  0.218, 2.293, 0.0157, -0.926635 ,  0.000000 , -1.406798
      ,       ,      ,       ,  0.926635 ,  0.000000 , -1.406798
  Cl  , -0.036, 3.564, 0.2550,  0.000000 , -1.451416 ,  0.177892
      ,       ,      ,       ,  0.000000 ,  1.451416 ,  0.177892



.. csv-table:: **Chloroform Weight=119.38 nAtoms=3**

  Atom, :math:`z_\alpha` / a.u., :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, X/Å , Y/Å, Z/Å
  C   , -0.386, 3.400, 0.1094,  0.000000 ,  0.000000 ,  0.463135
  H   ,  0.266, 2.115, 0.0157,  0.000000 ,  0.000000 ,  1.563010
  Cl  ,  0.040, 3.564, 0.2550,  1.607217 , -0.475149 , -0.067114
      ,       ,      ,       , -0.392118 ,  1.629465 , -0.067114
      ,       ,      ,       , -1.215099 , -1.154317 , -0.067114



**OPLS-AA Parameters for common atoms and atom group**

The table below contains possible sigma and epsilon parameters for some of the most common solvent groups collected from ref. [#ref9]_ [#ref10]_ [#ref11]_. These parameters are kindly provided by Leonardo Costa.




.. csv-table:: **All atoms model**

  Atom, Example, :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, Reference
  C (SP3) , methane       , 3.73 , 0.294  ,  [#ref9]_
  C (SP3) , neopentane    , 3.80 , 0.050  ,  [#ref9]_
  C (SP2) , isobutene     , 3.75 , 0.105  ,  [#ref9]_
  C (SP)  , acetonitrile  , 3.40 , 0.099  ,  [#ref10]_
  C (arom), benzene       , 3.55 , 0.07   ,  [#ref10]_
  C       , chloroform    , 4.10 , 0.05   ,  [#ref11]_
  H       , O---H         , 0.7  , 0.046  ,  [#ref10]_
  H       , hydrocarbons  , 2.42 , 0.03   ,  [#ref10]_
  O       , water         , 3.166, 0.1554 ,  [#ref10]_
  O       , alcohol       , 3.07 , 0.17   ,  [#ref10]_
  O       , sulfoxide     , 2.93 , 0.28   ,  [#ref10]_
  N (SP)  , acetonitrile  , 3.3  , 0.099  ,  [#ref10]_
  S       , sulfoxide     , 3.56 , 0.395  ,  [#ref10]_
  Cl      , chloroform    , 3.40 , 0.300  ,  [#ref11]_


.. csv-table:: **United atom model**

  Atom, Example, :math:`\sigma_\alpha` / Å, :math:`\epsilon_\alpha` / kcal/mol, Reference
  CH (SP3)  ,  isobutane    ,  3.850, 0.080, [#ref9]_
  CH (SP2)  ,  2-butene     ,  3.800, 0.115, [#ref9]_
  CH (arom) ,  benzene      ,  3.750, 0.110, [#ref9]_
  CH2 (SP3) ,  n-butane     ,  3.905, 0.118, [#ref9]_
  CH2 (SP2) ,  1-butene     ,  3.850, 0.140, [#ref9]_
  CH3       ,  hydrocarbon  ,  3.775, 0.207, [#ref9]_
  CH3       ,  acetonitrile ,  3.6  , 0.38 , [#ref10]_
  CH3       ,  sulfoxide    ,  3.81 , 0.16 , [#ref10]_
  NH2       ,  amine        ,  3.3  , 0.17 , [#ref10]_


.. only:: html

  .. rubric:: References

.. [#ref1] M. Reimann and M. Kaupp, *Evaluation of an Efficient 3D-RISM-SCF Implementation as a Tool for Computational Spectroscopy in Solution*, `Journal of Physical Chemistry A 124, 7439 (2020) <https://dx.doi.org/10.1021/acs.jpca.0c06322>`

.. [#ref2] S.\  Gusarov, T. Ziegler and A. Kovalenko, *Self-Consistent Combination of the Three-Dimensional RISM Theory of Molecular Solvation with Analytical Gradients and the Amsterdam Density Functional Package*, `Journal of Physical Chemistry A 110, 6083 (2006) <https://doi.org/10.1021/jp05[#ref10]_4t>`__ 

.. [#ref3] D.\  Casanova, S. Gusarov, A. Kovalenko and T. Ziegler, *Evaluation of the SCF Combination of KS-DFT and 3D-RISM-KH; Solvation Effect on Conformational Equilibria, Tautomerization Energies, and Activation Barriers*, `Journal of Chemical Theory and Computation 3, 458 (2007) <https://doi.org/10.1021/ct6001785>`__ 

.. [#ref4] J.W. Kaminski, S. Gusarov, A. Kovalenko and T.A. Wesolowski, *Modeling solvatochromic shifts using the orbital-free embedding potential at statistically mechanically averaged solvent density*, `Journal of Physical Chemistry A 114, 6082 (2010) <https://doi.org/10.1021/jp100158h>`__ 

.. [#ref5] A.\  Kovalenko and F. Hirata, *Potentials of mean force of simple ions in ambient aqueous solution. II. Solvation structure from the three-dimensional reference-interaction site model approach, and comparison with simulations*, `Journal of Chemical Physics 112, 10403 (2000) <https://doi.org/10.1063/1.481677>`__ 

.. [#ref6] A.\  Kovalenko and F. Hirata, *Self-consistent description of a metal-water interface by the Kohn-Sham density functional theory and the three-dimensional reference-interaction site model*, `Journal of Chemical Physics 110, 10095 (1999) <https://doi.org/10.1063/1.478883>`__ 

.. [#ref7] A.\  Kovalenko and F. Hirata, *Potentials of mean force of simple ions in ambient aqueous solution. I. Three-dimensional reference-interaction site model approach*, `Journal of Chemical Physics 112, 10391 (2000) <https://doi.org/10.1063/1.481676>`__ 

.. [#ref8] A.\  Kovalenko, *Three-dimensional RISM theory for molecular liquids and solid-liquid interfaces*, In Molecular Theory of Solvation; Hirata, Fumio, Ed.; Understanding Chemical Reactivity (series); Mezey, Paul G., Series Ed.; Kluwer Acadamic Publishers: Dordrecht, The Netherlands, 2003; Vol. 24, pp 169-275. 

.. [#ref9] W.L. Jorgensen, J.D. Madura and C.J. Swenson, *Optimized intermolecular potential functions for liquid hydrocarbons,* `Journal of the American Chemical Society 106, 6638 (1984) <https://doi.org/10.1021/ja00334a030>`__ 

.. [#ref10] A.E. Kobryn and A. Kovalenko, *Molecular theory of hydrodynamic boundary conditions in nanofluidics,* `Journal of Chemical Physics 129, 134701 (2008) <https://doi.org/10.1063/1.2972978>`__ 

.. [#ref11] O.\  Acevedo and W.L. Jorgensen, *Influence of Inter- and Intramolecular Hydrogen Bonding on Kemp Decarboxylations from QM/MM Simulations,* `Journal of the American Chemical Society 127, 8829 (2005) <https://doi.org/10.1021/ja051793y>`__ 
