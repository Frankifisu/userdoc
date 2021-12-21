.. index:: COSMO
.. _COSMO:

COSMO: Conductor like Screening Model and the Solvation-key
-----------------------------------------------------------


You can study chemistry in solution, as contrasted to the gas phase, with the implementation in BAND of the Conductor like Screening Model (COSMO) of solvation [#ref1]_.

In the COSMO model all solvents are roughly the same, and approximated by an enveloping metal sheet. One explicit dependency on the solvent is that the solvation energy is scaled by 

.. math::

   f(\epsilon) = \frac{\epsilon-1}{\epsilon+\chi}

and this depends on the dielectric constant of the solvent, and an empirical factor :math:`\chi`. The other is that the shape of the surface is influenced by the *Rad* parameter, see below. 

The solvent information is specified in the ``solvent`` key of the ``solvation`` block. The simplest option is to use one of the pre-defined solvents:

.. scmautodoc:: band Solvation Enabled Solvent Solvent%Name
  :notrecursive:
  :noref:
  :collapselongchoicesinsummary:


This is the list of possible solvents and their corresponding ``Eps`` and ``Rad`` values:

.. csv-table:: 

    Solvent Name, Formula, Eps, Rad
    AceticAcid, CH3COOH, 6.19, 2.83
    Acetone, CH3COCH3, 20.7, 3.08
    Acetonitrile, CH3CN, 37.5, 2.76
    Ammonia, NH3, 16.9, 2.24
    Aniline, C6H5NH2, 6.8, 3.31
    Benzene, C6H6, 2.3, 3.28
    BenzylAlcohol, C6H5CH2OH, 13.1, 3.45
    Bromoform, CHBr3, 4.3, 3.26
    Butanol, C4H9OH, 17.5, 3.31
    isoButanol, (CH3)2CHCH2OH, 17.9, 3.33
    tertButanol, (CH3)3COH, 12.4, 3.35
    CarbonDisulfide, CS2, 2.6, 2.88
    CarbonTetrachloride, CCl4, 2.2, 3.37
    Chloroform, CHCl3, 4.8, 3.17
    Cyclohexane, C6H12, 2, 3.5
    Cyclohexanone, C6H10O, 15, 3.46
    Dichlorobenzene, C6H4Cl2, 9.8, 3.54
    DiethylEther, (CH3CH2)2O, 4.34, 3.46
    Dioxane, C4H8O2, 2.2, 3.24
    DMFA, (CH3)2NCHO, 37, 3.13
    DMSO, (CH3)2SO, 46.7, 3.04
    Ethanol, CH3CH2OH, 24.55, 2.85
    EthylAcetate, CH3COOCH2CH3, 6.02, 3.39
    Dichloroethane, ClCH2CH2Cl, 10.66, 3.15
    EthyleneGlycol, HOCH2CH2OH, 37.7, 2.81
    Formamide, HCONH2, 109.5, 2.51
    FormicAcid, HCOOH, 58.5, 2.47
    Glycerol, C3H8O3, 42.5, 3.07
    HexamethylPhosphoramide, C6H18N3OP, 43.3, 4.1
    Hexane, C6H14, 1.88, 3.74
    Hydrazine, N2H4, 51.7, 2.33
    Methanol, CH3OH, 32.6, 2.53
    MethylEthylKetone, CH3CH2COCH3, 18.5, 3.3
    Dichloromethane, CH2Cl2, 8.9, 2.94
    Methylformamide, HCONHCH3, 182.4, 2.86
    Methypyrrolidinone, C5H9NO, 33, 3.36
    Nitrobenzene, C6H5NO2, 34.8, 3.44
    Nitrogen, N2, 1.45, 2.36
    Nitromethane, CH3NO2, 35.87, 2.77
    PhosphorylChloride, POCl3, 13.9, 3.33
    IsoPropanol, (CH3)2CHOH, 19.9, 3.12
    Pyridine, C5H5N, 12.4, 3.18
    Sulfolane, C4H8SO2, 43.3, 3.35
    Tetrahydrofuran, C4H8O, 7.58, 3.18
    Toluene, C6H5CH3, 2.38, 3.48
    Triethylamine, (CH3CH2)3N, 2.44, 3.81
    TrifluoroaceticAcid, CF3COOH, 8.55, 3.12
    Water, H2O, 78.39, 1.93


Several other options can be defined in the ``Solvation`` block:

.. scmautodoc:: band Solvation
   :collapselongchoicesinsummary:

Additional keys for periodic systems
------------------------------------

For the simulation of periodic structures ICW solvation, you may specify the following options:

.. scmautodoc:: band PeriodicSolvation RemovePointsWithNegativeZ NStar

**General remarks:** The accuracy of the result and the calculation time is influenced by the screening radius ``SCREENING%RMADEL`` (see :ref:`Screening <band-key-Screening>` block). If the calculation does take too long, defining a smaller radius does help. **But:** too small radii, especially smaller than the lattice constants, will give unphysical results.


.. only:: html

  .. rubric:: References

.. [#ref1] A.\  Klamt  and G. Schüürmann,  *COSMO: a new approach to dielectric screening in solvents with explicit expressions for the screening energy and its gradient.*  `Journal of the Chemical Society: Perkin Transactions  2, 799 (1993) <https://doi.org/10.1039/P29930000799>`__.
