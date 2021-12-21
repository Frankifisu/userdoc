.. index:: NMR chemical shifts 
.. index:: NMR shielding tensor 
.. index:: nmr module 
.. _NMR_SHIELDING_NMR: 
.. _NMR chemical shifts:


NMR Chemical Shifts
===================

NMR Chemical shifts have been implemented [#ref7]_ [#ref8]_ [#ref9]_ [#ref10]_ [#ref11]_ in a separate property program NMR. It requires the adf.rkf (TAPE21) result file from an ADF calculation. The NMR module can be combined with the ZORA treatment for relativistic effects and with Spin-Orbit effects, making it suitable for treatment of heavy elements. See also the general review on relativistic computations of NMR parameters [#ref1]_. 

Two GUI tutorials on NMR Chemical shift calculations are currently available:

+ Chemical shifts and nuclear spin-spin coupling constants w. NBO analysis: `Analysis of NMR parameters with Localized Molecular Orbitals <../../Tutorials/NMR/NMRAnalysisWithNLMOAndNBO.html>`_ 
+ Chemical shifts and nuclear spin-spin coupling constants w. visualization of the spectrum in the GUI: `H-NMR spectrum with spin-spin coupling <../../Tutorials/NMR/H-NMRSpectrumSpin-SpinCoupling.html>`_ 


Important notes
---------------

**adf.rkf (TAPE21) and TAPE10**

NMR requires an ASCII input file and adf.rkf (TAPE21) and TAPE10 result files from an ADF calculation on the molecule to be analyzed. The ADF result files adf.rkf (TAPE21) and TAPE10 must be present with names TAPE21 and TAPE10 in the directory where you execute NMR, or alternatively one can use the keys ADFFile and TAPE10File to point to an adf.rkf file and TAPE10 file. Use the keywords SAVE TAPE10 in the adf calculation in order to obtain a TAPE10 result file. 

**Recalculation of TAPE10 by NMR**

Warning: the NMR property program will not always give the correct result for every SCF potential in the ADF calculation, like for example the SAOP potential, or if one uses COSMO in the ADF calculation, if one lets the NMR recalculate TAPE10. This is due to the GIAO method used in this program, which requires the calculation of the SCF potential, which is not done correctly for potentials, other than the standard LDA and GGA potentials. To obtain correct results one should, in addition to the use of TAPE21, also use TAPE10 that ADF generates, using the keywords SAVE TAPE10, and use it as input for the NMR property program. On TAPE10 the SCF potential is written, which is read in by the NMR program. 

**Atomic calculation**

NMR calculations on 1 atom must have symmetry NOSYM. 

**Spin-orbit coupling**

NMR calculations on systems computed by ADF with Spin Orbit relativistic effects included must have used NOSYM symmetry in the ADF calculation. NMR can also be combined with ADF ZORA calculations. The NMR program reads from adf.rkf (TAPE21) the relativistic option that is used in the ADF calculation, and will use the same relativistic option in the NMR calculations. 

**Kernel used in spin-orbit coupling**

One can include an improved exchange-correlation kernel, as was implemented by J. Autschbach [#ref2]_, but this is not used by default, see subkey USE. This is an important option that should be seriously considered and has been advocated in Ref. [#ref2]_.


**Bug spin-orbit part ADF2008 - ADF2013**

In the ADF2008.01 a bug was introduced in the spin-orbit part of the calculated chemical shielding, which caused the calculated chemical shielding to be gauge dependent. This bug is relevant for spin-orbit coupled calculations for ADF versions ADF2008-ADF2013. In ADF2014 this bug has been fixed. 

**Unscaled ZORA default ADF2014**

There is gauge dependence if the scaled ZORA method is used in the calculation of NMR chemical shieldings. Therefore the default method for NMR chemical shielding calculations is changed in ADF2014 to use the unscaled ZORA method. 

**SAOP**

The use of the model SAOP potential leads to isotropic chemical shifts which are substantially improved over both LDA and GGA functionals, and of similar accuracy as results with a self-interaction-corrected functional (SIC), see [#ref3]_. SAOP is computationally expedient and routinely applicable to all systems, requiring virtually the same computational effort as LDA and GGA calculations. 

**NICS**

The Nucleus-Independent Chemical Shift (NICS) can be calculated at any point in the molecule. 

**Hybrids**

Starting from ADF2009.01 Hartree-Fock and the hybrid potentials can used in combination with NMR chemical shielding calculations. see Refs. [#ref4]_ [#ref5]_. Use SAVE TAPE10 in the ADF calculation. The use of frozen cores and hybrids gives gauge dependent results for the NMR chemical shieldings, therefore the NMR program will stop in this case. 

**Meta-GGA's and meta-hybrids**

Meta-GGA's and meta-hybrids should not be used in combination with NMR chemical shielding calculations. The results are wrong due to an incorrect inclusion of GIAO terms. 


Input options
-------------

The input file for NMR uses the block key NMR, with several (optional) subkeys, each having a series of options. For analysis a separate block key can be used. 

.. _keyscheme nmr: 

::

  $AMSBIN/nmr << eor
  ADFFile adffile
  TAPE10File tape10file
  ZSOAO2007
  RECALCULATETAPE10
  NMR
  End
  Analysis
  End
  eor

**ADFFile adffile**

Path to adf.rkf (TAPE21) file from which nmr reads data and to which nmr writes data. Default TAPE21.

**TAPE10File tape10file**

Path to TAPE10 file from which nmr reads data. Default TAPE10.

**ZSOAO2007 keyword**

In the ADF2008.01 a bug was introduced in the spin-orbit part of the calculated chemical shielding, which caused the calculated chemical shielding to be gauge dependent. This bug is relevant for spin-orbit coupled calculations for ADF versions ADF2008-ADF2013. Workaround in ADF versions ADF2008-ADF2013 is to include the keyword ZSOAO2007 in the NMR part of the input, which causes a one-center approximation to be used. The bug has been fixed in ADF2014 by introducing an extra gauge-correction term for the spin-orbit coupled part. One can still get the (slightly) incorrect results in ADF2014 by using the keyword WRONGSOGAUGE, and not including ZSOAO2007. 

**REACALCULATETAPE10 keyword**

If there is no TAPE10 present the NMR program will stop. One can use the key REACALCULATETAPE10 such that TAPE10 will be recalculated by the NMR module. Not recommended to be used. Better use 'SAVE TAPE10' in the ADF calculation, and use this TAPE10 as input for NMR. 

**NMR block key**

.. _keyscheme nmr NMR: 


::

  NMR
    Out  OutOptions
    Calc CalcOptions
    Use UseOptions
    U1K  U1KOptions
    Nuc  NucOptions
    Atoms  AtomsOptions
    Ghosts  GhostsOptions
    Analysis  AnalysisOptions
  End

``Out OutOptions``
  The subkey Out controls printed output. Its options specify the details by their (optional) presence. The following OutOptions are recognized (Default ISO TENS):  

  ``All``
    Implies all the other options

  ``ISO``
    Isotropic shielding constants

  ``Tens``
    Shielding tensors 

  ``Eig``
    Eigenvectors 

  ``U1``
    The U1 matrix 

  ``F1``
    The first order change in the Fock matrix 

  ``S1``
    The first order change in the Overlap matrix 

  ``AOP``
    The paramagnetic AO matrix (= the matrix in the representation of elementary atomic basis functions) 

  ``AOD``
    The diamagnetic AO matrix 

  ``AOF``
    The Fermi-contact AO matrix 

  ``REFS``
    Literature references 

  ``INFO``
    General information 

``Calc CalcOptions``
  The subkey Calc controls what is actually calculated. The following options are available (Default ALL): 

  ``All``
    Implies all of the other options to this key 

  ``Para``
    The paramagnetic part 

  ``Dia``
    The diamagnetic part 

  ``FC``
    The Fermi-contact part in case of the Pauli Hamiltonian 

  ``SO``
    The Fermi-contact part in case of the ZORA Hamiltonian 

``Use UseOptions``
  The subkey Use controls some optional options (default none) 

  ``FXC``
    Improves the exchange-correlation kernel used, as was implemented by J. Autschbach [#ref2]_. Important only in case of spin-orbit coupled calculations. This may give some (small) gauge dependent results when using this. Important option that should be seriously considered and has been advocated in Ref. [#ref2]_.

  ``SCALED``
    Implies the scaled ZORA method, which gives (slightly) gauge dependent results, as was shown in Ref. [#ref2]_. Note that in case of the ZORA Hamiltonian default the unscaled ZORA method is used. For chemical shifts, only compare results with the same options. 

  ``SO1C``
    Before ADF2008.01 in the the spin-orbit term a 1-center approximation was used, which does not suffer from gauge dependence. This 1-center approximation can be used with USE SO1C. 

``U1K U1KOptions``
  The subkey U1K determines which terms are included in the calculation of the U1 matrix (first order changes in MO coefficients). Options (Default Best): 

  ``Best``
    The best (recommended) options for each relativistic option are included for this subkey. Implies 'None' for non-relativistic and scalar relativistic ZORA, 'SO' + 'SOFULL' for spin-orbit coupled ZORA, and 'MV + 'Dar' for the Pauli Hamiltonian. 

  ``None``
    Implies none of the other options to this key. 

  ``All``
    Implies all the other options to this key. 

  ``MV``
    The mass-velocity term .

  ``Dar``
    The Darwin term.

  ``ZMAN``
    The Spin-Zeeman term. Can be included only in case of spin-orbit coupled Pauli Hamiltonian.

  ``SO``
    ZORA spin-orbit part.

  ``SOFULL``
    ZORA spin-orbit part.

Note: for chemical shifts, only compare results with the same options. If the subkey U1K is used with the option ALL in the ZORA calculation, then the scaled ZORA orbital energies are used in the making of the U1 matrix, which is not recommended. Recommended is to use 'U1K Best' in all cases, which uses plain ZORA orbital energies in the making of the U1 matrix. 

``NUC NucOptions``
  This subkey NUC specifies for which nuclei the NMR shielding is calculated. Default all nuclei are calculated, i.e. as for omitting the subkeys ATOMS and NUC. Else you may use this options by simply typing Nuc in the NMR block (without any further data); this means: for no nuclei at all. Alternatively you may type the index of the atom(s) you want to see analyzed. Default all nuclei are calculated, i.e. as for omitting this subkey. 

  Example::

    NUC 2 1

  The numbers refer to the internal numbering of the nuclei as it appears somewhere early in the general ADF output. This internal numbering is also the internal NMR numbering, but it is not necessarily the same as the input ordering. Use the subkey ATOMS to specify the nuclei according to this input ordering in the ADF calculation. 

  Note that the number of nuclei has a significant consequence for the total CPU time. 

``Atoms AtomsOptions``
  This subkey ATOMS specifies for which nuclei the NMR shielding is calculated. Default all nuclei are calculated, i.e. as for omitting the subkeys ATOMS and NUC. 

  Example::

    ATOMS 2 1

  The numbers refer to the input ordering in the ADF calculation. Use the subkey NUC to specify the nuclei according to the internal NMR numbers of the atoms.

.. _NICSNMR: 
.. index:: NICS
.. index:: nuclear-independent chemical shift

``GHOSTS``
  The subkey GHOSTS is a block type subkey. The format is::

    Ghosts
      xx1 yy1 zz1
      xx2 yy2 zz2
      ...
    SubEnd

  With this key, the user can specify ANY point(s) within the molecule at which the shielding is to be calculated (whatever the physical meaning of this shielding is). One can think of those points as neutrons within the molecule. There is a publication by P. Schleyer et al. using a similar feature (J. Am. Chem. Soc. **118**, 6317, 1996). They call it NICS, Nucleus-Independent Chemical Shift. Note that the NICS value is minus 1 times the isotropic part of the shielding tensor that is calculated at these points::

    xx1 yy1 zz1

  real numbers that specify the Cartesian coordinates of 'ghost' 1, etc.  

  The coordinates have to be specified in Angstrom. The same set of coordinates has to be specified as 'point charges with charge zero' using the subsubkey MultipolePotential in the ElectrostaticEmbedding subkey of the key System in the AMS block. This is necessary in order to allow the appropriate distribution of integration points around the ghosts. 

  E.g., if you want to have two 'ghosts' with the coordinates xx1 yy1 zz1 and xx2 yy2 zz2 then you **must** also have in the input the key MultipolePotential key as follows::

    System
      ...
      ElectrostaticEmbedding
        MultipolePotential
          Coordinates
            xx1 yy1 zz1   0.0
            xx2 yy2 zz2   0.0
          End
        End
      End
    End

  (the last number is the charge at these coordinates - zero). 

  Eventually, this step should be programmed internally but for now the procedure outlined above works. No check is done to verify whether those 'point charges' are taken care of or not, but their omission leads to unpredictable results. 

  Only Cartesian coordinates are possible for ghosts, even if the atoms were originally specified using internal coordinates. This shouldn't be a problem, though (e.g., one could start an ADF run of the molecule of interest, and get very soon the Cartesian coordinates of the atoms in the output. This run would then be aborted, and restarted with the ghosts specified as desired.) The ghosts are numbered in the output as NNUC+1, NNUC+2 ... where NNUC is the total number of nuclei in this molecule. Default: no ghosts. 

``Analysis AnalysisOptions``
  The subkey Analysis controls the MO analysis. After the word (subkey) Analysis you type an integer, which then specifies that the first so many MOs are to be analyzed. Default no Analysis. The value of this analysis subkey in the block key NMR is somewhat limited. The separate ANALYSIS block key can give more analysis of the NMR chemical shielding. 

**Analysis block key**

The NMR shielding tensor, can be analyzed in detail, see Refs. [#ref12]_ [#ref13]_ [#ref1]_. For the analysis option with the ANALYSIS block key there are some restrictions. In the ADF calculation all electron basis sets should have been used, and SYMMETRY NOSYM. Can not be used in case of non-relativistic calculations. The ADF calculation should use relativistic scalar ZORA or relativistic spinorbit ZORA. In case of scalar relativistic ZORA the keyword FAKESO should be added to the NMR input (outside of the NMR or Analysis block keys). The analysis utilizes the ZORA spin-orbit branch of the NMR code. For scalar ZORA, the NMR analysis contributions will appear in equivalent pairs for spin-orbitals even if the ADF calculation is closed-shell spin restricted. The MO numbering then also reflects this doubling of MOs. In the analysis, canonical MOs number 1 and 2 are the alpha and beta spin ADF MO 1, canonical MOs number 3 and 4 correspond to the alpha and beta spin ADF MO 2, and so on. In case of spinorbit relativistic ZORA the keyword FAKESO should not be included. Curly brackets are not part of the key. For an NBO analysis of NMR, see the  :ref:`section on NBO analysis<NBO_PROPERTIES>`. 

::

  Analysis
    print threshold
    canonical
    {components}
  End
  {FakeSO}

``print threshold``
  The print keyword selects printout of contributions relative to the total diamagnetic, paramagnetic. For example in case of 'print 0.01' only contributions greater than 1% are printed. Set to zero to print ALL contributions.  

``canonical``
  It enables an analysis of the shielding in terms of the canonical MOs. 

``components``
  The components keyword is optional and enables an analysis not only of the isotropic shielding but also of the diagonal Cartesian components of the tensor XX, YY, and ZZ). In order to analyze the principal shielding tensor components with canonical MOs you can calculate the shielding tensor first with the NMR code, rotate the molecule such that the principal axes system aligns with the Cartesian coordinate system, and then repeat the NMR calculation with the analysis features switched on. 

.. _PNMR_SHIELDING: 
.. index:: paramagnetic NMR 

Paramagnetic NMR Chemical Shifts
================================

Knowledge of the g-tensor and hyperfine A-tensor can be used in the prediction and analysis of paramagnetic NMR shifts, see Refs. [#ref6]_ [#ref15]_ [#ref16]_. Because of the dependence on the g-tensor, prediction of paramagnetic NMR (pNMR) shifts is not straightforward, as the dependence of the pNMR shift on excess :math:`\alpha` or :math:`\beta` electron spin density at a nucleus is to be combined with the sign and magnitude of the isotropic g-value.  Ref. [#ref6]_ describes in detail how to calculate pNMR contact chemical shifts and pNMR pseudo-contact chemical shifts, using the ADF program. 

Of course, like for NMR chemical shielding of closed shell molecules, one also needs to calculate of the so called orbital dependent part of the NMR chemical shielding of the open shell molecule. For open shell molecules in ADF this can only be calculated without taken into account spin-orbit coupling: 

::

  $AMSBIN/ams << eor
    ...
    Engine ADF
      SpinPolarization vlaue
      Unrestricted Yes
      Relativity 
        Level Scalar
      End    
      Basis
        Core None
      End
      SAVE TAPE10
    EndEngine
  eor

  $AMSBIN/nmr << eor
    ADFFile path/to/adf.rkf
    TAPE10File path/to/TAPE10
    ALLINONE
    nmr
       u1k best
       calc all
       out iso tens
    end
  eor

Note that one can only do this at the scalar relativistic ZORA level, one needs to use all electron basis sets, and one needs to include the key ALLINONE in the input for NMR, 

.. only:: html

  .. rubric:: References

.. [#ref7] G.\  Schreckenbach and T. Ziegler, *The calculation of NMR shielding tensors using GIAO's and modern density functional theory*, `Journal of Physical Chemistry 99, 606 (1995) <https://doi.org/10.1021/j100002a024>`__ 

.. [#ref8] G.\  Schreckenbach and T. Ziegler, *The calculation of NMR shielding tensors based on density functional theory and the frozen-core approximation*, `International Journal of Quantum Chemistry 60, 753 (1996) <https://doi.org/10.1002/(SICI)1097-461X(1996)60:3%3C753::AID-QUA4%3E3.0.CO;2-W>`__ 

.. [#ref9] G.\  Schreckenbach and T. Ziegler, *Calculation of NMR shielding tensors based on density functional theory and a scalar relativistic Pauli-type Hamiltonian. The application to transition metal complexes*, `International Journal of Quantum Chemistry 61, 899 (1997) <https://doi.org/10.1002/(SICI)1097-461X(1997)61:6%3C899::AID-QUA3%3E3.0.CO;2-R>`__ 

.. [#ref10] S.K. Wolff and T. Ziegler, *Calculation of DFT-GIAO NMR shifts with inclusion of spin-orbit coupling*, `Journal of Chemical Physics 109, 895 (1998) <https://doi.org/10.1063/1.476630>`__ 

.. [#ref11] S.K. Wolff, T. Ziegler, E. van Lenthe and E.J. Baerends, *Density functional calculations of nuclear magnetic shieldings using the zeroth-order regular approximation (ZORA) for relativistic effects: ZORA nuclear magnetic resonance* , `Journal of Chemical Physics 110, 7689 (1999) <https://doi.org/10.1063/1.478680>`__ 

.. [#ref1] J.\  Autschbach and S. Zheng, *Relativistic computations of NMR parameters from first principles: Theory and applications*, `Annual Reports on NMR Spectroscopy 67, 1 (2009) <https://doi.org/10.1016/S0066-4103(09)06701-5>`__ 

.. [#ref2] J.\  Autschbach, *The role of the exchange-correlation response kernel and scaling corrections in relativistic density functional nuclear magnetic shielding calculations with the zeroth-order regular approximation*, `Molecular Physics 111, 2544 (2013) <https://doi.org/10.1080/00268976.2013.796415>`__

.. [#ref3] J.\  Poater, E. van Lenthe and E.J. Baerends, *Nuclear magnetic resonance chemical shifts with the statistical average of orbital-dependent model potentials in Kohn.Sham density functional theory*, `Journal of Chemical Physics 118, 8584 (2003) <https://doi.org/10.1063/1.1567252>`__ 

.. [#ref4] M.\  Krykunov, T. Ziegler and E. van Lenthe, *Hybrid density functional calculations of nuclear magnetic shieldings using Slater-type orbitals and the zeroth-order regular approximation*, `International Journal of Quantum Chemistry 109, 1676 (2009) <https://doi.org/10.1002/qua.21985>`__ 

.. [#ref5] M.\  Krykunov, T. Ziegler and E. van Lenthe, *Implementation of a hybrid DFT method for calculating NMR shieldings using Slater-type orbitals with spin-orbital coupling included. Applications to* \ :sup:`187` Os, \ :sup:`195` Pt and \ :sup:`13` C *in heavy metal complexes*, `Journal of Physical Chemistry A 113, 11495 (2009) <https://doi.org/10.1021/jp901991s>`__ 

.. [#ref6] J.\  Autschbach, S. Patchkovskii, and B. Pritchard, *Calculation of Hyperfine Tensors and Paramagnetic NMR Shifts Using the Relativistic Zeroth-Order Regular Approximation and Density Functional Theory*, `Journal of Chemical Theory and Computation 7, 2175 (2011) <https://doi.org/10.1021/ct200143w>`__ 

.. [#ref12] J.\  Autschbach, *Analyzing NMR shielding tensors calculated with two-component relativistic methods using spin-free localized molecular orbitals*, `Journal of Chemical Physics 128, 164112 (2008) <https://doi.org/10.1063/1.2905235>`__ 

.. [#ref13] J.\  Autschbach and S. Zheng, *Analyzing Pt chemical shifts calculated from relativistic density functional theory using localized orbitals: The role of Pt 5d lone pairs*, `Magnetic Resonance in Chemistry 46, S45 (2008) <https://doi.org/10.1002/mrc.2289>`__ 

.. [#ref15] S.\  Moon, and S. Patchkovskii, *First-principles calculations of paramagnetic NMR shifts*, in Calculation of NMR and EPR parameters, ISBN13: 9783527307791, M. Kaupp, M. Bühl, V.G. Malkin, Editors, (Wiley, Weinheim, 2004). 

.. [#ref16] P.\  Hrobárik, Ro. Reviakine, A.V. Arbuznikov, O.L. Malkina, V.G. Malkin, F.H. Köhler, and M. Kaupp, *Density functional calculations of NMR shielding tensors for paramagnetic systems with arbitrary spin multiplicity: Validation on 3d metallocenes*, `Journal of Chemical Physics 126, 024107 (2007) <https://doi.org/10.1063/1.2423003>`__ 
