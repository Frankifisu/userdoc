.. index:: TDDFT 
.. index:: time-dependent DFT 
.. index:: response properties 


Time-dependent DFT
******************

Excitation energies, frequency-dependent (hyper) polarizabilities, Van der Waals dispersion coefficients, higher multipole polarizabilities, Raman scattering intensities and depolarization ratios of closed-shell molecules are all available in ADF [#ref1]_ [#ref2]_ as applications of time-dependent DFT (TDDFT) ; see [#ref3]_ for a review. 

New in ADF2004.01 is the calculation of circular dichroism (CD) spectra, and the calculation of the optical rotation (dispersion). 

Starting from the ADF2005.01 version it is possible to calculate excitation energies for open-shell systems with TDDFT, including spin-flip excitation energies. New in ADF2005.01 is the possibility to use time-dependent current-density functional theory (TDCDFT). 

New in ADF2006.01 is the possibility to calculate excitation energies for closed-shell molecules including spin-orbit coupling. 

New in ADF2008.01 is the possibility to calculate lifetime effects in (dynamic) polarizabilities (AORESPONSE key). 

The input description for these properties is split in three parts: (a) general advice and remarks, (b) excitation energies, and (c) frequency-dependent (hyper) polarizabilities (two alternative implementation: RESPONSE key and AORESPONSE key) and related properties. 

.. tip::
  
  See also the ADF Advanced TDDFT tutorial: `TDDFT Study of 3 different Dihydroxyanthraquinones <../../Tutorials/OpticalPropertiesElectronicExcitations/TDDFT_NBO.html>`__ 

General remarks on the Response and Excitation functionality
============================================================

``Symmetry``
  As in calculations without TDDFT the symmetry is automatically detected from the input atomic coordinates and need not be specified, except in the following case: infinite symmetries cannot be handled in the current release (ATOM, C(lin), D(lin)). For such symmetries a subgroup with finite symmetry must be specified in the input. The usual orientation requirements apply. If higher multipole polarizabilities are required, it may also be necessary to use a lower subgroup (the program will stop with an error message otherwise). For verification of results one can always compare to a NOSYM calculation. 

``Closed-shell``
  The current implementation often supports only closed-shell molecules. If occupation numbers other than 0 or 2 are used the program will detect this, (but only at a later stage of the calculation) and abort. All 'RESPONSE' calculations must be spin-restricted. 

``Open-shell``
  Excitation energies can be obtained for open-shell systems in a spin-unrestricted TDDFT calculation. Spin-flip excitation energies can only be obtained in a spin-unrestricted TDDFT calculation. 

``Atomic coordinates in a RAMAN calculation``
  Atomic coordinate displacements in a RAMAN calculation must be Cartesian, not Z-matrix. Furthermore, the current implementation does not yet support constrained displacements, i.e. you must use *all* atomic coordinate displacements. 

``Use of diffuse functions``
  The properties described here may require diffuse functions to be added to the basis (and fit) sets. Poor results will be obtained if the user is unaware of this. As a general rule, diffuse functions are more important for smaller than for larger molecules, more important for hyperpolarizabilities than for normal polarizabilities, more important for high-lying excitation energies (Rydberg states) than for low-lying excitations, more important for higher multipole polarizabilities than for dipole polarizabilities. The user should know when diffuse functions are required and when they are not: the program will not check anything in this respect. For example, in a study on low-lying excitation energies of a large molecule, diffuse functions will usually have little effect, whereas a hyperpolarizability calculation on a small molecule is pointless unless diffuse functions are included. Diffuse even tempered basis sets are included in the ET/ directory in ``$AMSHOME/atomicdata/ADF``), for the elements H-Kr. Somewhat older basis sets can be found in the Special/Vdiff directory in ``$AMSHOME/atomicdata/ADF``. For other atoms, the user will have to add diffuse basis and fit functions to the existing data base sets. It is not necessary to start from basis V as was done for the basis sets in Special/Vdiff. For example, for heavier elements it may be a good idea to start from the ZORA/QZ4P basis sets. It may be expected that even more extensive basis sets will come available in the future, when usage and experience increase. 

``Linear dependency in basis``
  If large diffuse basis sets are used, or if diffuse functions are used for atoms that are not far apart the calculation may suffer from numerical problems because of (near-) linear dependencies in the basis set. The user should be aware of this danger and use the DEPENDENCY key to check and solve this. 

``The LINEARSCALING input keyword``
  For reasons of numerical robustness and safety rather strict defaults apply for the neglect of tails of basis and fit functions (see the key LINEARSCALING) in a Response or Excitation calculation. This may result in longer CPU times than needed for non-TDDFT runs, in particular for larger molecules. Possibly this precaution is not necessary, but we have not yet tested this sufficiently to relax the tightened defaults. 

``Relativistic effects``
  The Response and Excitations options can be combined with scalar relativistic options (ZORA or Pauli). The one-electron relativistic orbitals and orbital energies are then used as input for the property calculation. Spin-orbit effects have been incorporated only in this part of the code (excitation energies). In case of a ZORA calculation, the so-called 'scaled' orbital energies are used as default. 

``Choice of XC potential``
  For properties that depend strongly on the outer region of the molecule (high-lying excitation energies, (hyper) polarizabilities), it may be important to use a XC potential with correct asymptotic behavior (approaching -1/r as r tends to infinity). Finally, several asymptotically correct XC potentials have been implemented in ADF, like the LB94 potential [#ref4]_ and the  statistical average of orbital potentials SAOP [#ref8]_ [#ref6]_. SAOP is recommended. Because of the correct asymptotic behavior the SAOP potential (and the LB94 potential) can describe Rydberg states correctly. The potentials based upon the so-called GRadient regulated seamless connection of model potentials (GRAC) for the inner and the outer region [#ref5]_ [#ref7]_ have similar performance to SAOP, but have the disadvantage that the ionization energy of the molecule has to be used as input.  

  With the SAOP and GRAC  functionals for the potential (as well as for LB94), the XC potential is computed from the exact charge density for reasons of stability and robustness (whereas for other functions the (cheaper) fit density is used). This implies that computation times may be longer. Another 'side effect' is that, since there is no energy expression corresponding to these potentials, the final (bonding) energy of such calculations uses another GGA and hence the energy result is not (exactly) consistent with the SCF procedure. Note, finally, that these potentials have been found to be not suitable for geometry optimizations because they maybe are not sufficiently accurate in the bonding region, see the discussion of the XC input key. Applications with SAOP to (hyper)polarizabilities and excitation energies, also for Rydberg transitions, can be found in [#ref6]_ and with SAOP and Becke-Perdew-GRAC in [#ref5]_ [#ref7]_. Applications with the old LB94 potential to response calculations can be found in refs. [#ref12]_ (polarizabilities), [#ref25]_ [#ref26]_ [#ref27]_ (hyperpolarizabilities), [#ref13]_ (high-lying excitation energies), [#ref14]_ (multipole polarizabilities and dispersion coefficients). 

.. index:: ALDA kernel 
.. index:: XC kernel 

``XC kernel``
  If most cases the adiabatic local density approximated (ALDA) kernel is used in the TDDFT functionality. In case of calculating excitation energies with a hybrid functionals the Hartree-Fock percentage times the Hartree-Fock kernel plus one minus the Hartree-Fock percentage times the ALDA kernel is used. 
  For the LibXC range separated functionals, like CAM-B3LYP, starting from ADF2016.102 the kernel consists of range separated ALDA plus the kernel of the range separated exact exchange part.
  In ADF2016.101 the kernel for LibXC range separated functionals, like CAM-B3LYP, was using a 100% ALDA plus range separated exact exchange kernel (the ALDA part was not range-separated corrected).

  For excitation energy calculations in some cases the full (non-ALDA) kernel can be evaluated, see the :ref:`full XC kernel description<full xc kernel>`. The Full kernel can not be used in combination with symmetry or excited state geometry optimizations.  

``COSMO``
  The COSMO model for solvation is a cheap method to include solvation effects in the TDDFT applications, see the SOLVATION key. Note that in TDDFT calculations one may have to use two dielectric constants. The reason is that the electronic transition is so fast that only the electronic component of the solvent dielectric can respond, i.e., one should use the optical part of the dielectric constant. This is typically referred to as non-equilibrium solvation. The optical dielectric constant can be obtaining from the (frequency dependent) refractive index n of the solvent as: :math:`\epsilon`\ :sub:`opt`  = n\ :sup:`2` . One can use the argument NEQL in the subkey SOLV of the key SOLVATION to set a value for the optical dielectric constant. No dielectric constant in the response might be closer to the optical dielectric constant than using the full dielectric constant, This can be achieved if one includes the subkey NOCSMRSP in the block key SOLVATION, such that  the induced electronic charges do not influence the COSMO surface charges. However, if one does geometry optimization then the full dielectric constant should be used in the TDDFT simulations since the solvent dielectric now has time to fully respond. The default is that the full dielectric constant is used in the TDDFT calculations. 

``Accuracy check list``
  As mentioned before, the TDDFT module is relatively new and not extensively tested for a wide range of applications. Therefore, we strongly recommend the user to build experience about aspects that may affect the accuracy of TDDFT results. In particular we advise to 'experiment' with 

  - Varying integration accuracy 

  - Varying the SCF convergence  

  - Varying the ORTHONORMALITY and TOLERANCE values in an Excitation calculation 

  - Varying the linearscaling parameters 

  - Using diffuse functions 

  - Using the Dependency key 

  - Applying the ZORA relativistic corrections for molecules containing heavy nuclei 

  - Using an asymptotically correct XC potential such as SAOP 


Analysis options for TDDFT (excitation energies and polarizabilities)
=====================================================================

Several options are available to obtain more detailed results than a few bare numbers for excitation energies, oscillator strengths, transition dipole moments, and (hyper)polarizabilities. For a zero-order understanding of which occupied and virtual orbitals play an important in the polarizability or intensity of an absorption peak, 

it may be useful to know the values of the dipole matrix elements between (ground-state) occupied and virtual Kohn-Sham orbitals. If these dipole matrix elements are large for a particular occupied-virtual orbital pair, then this pair is almost certainly of great importance for the whole spectrum or polarizability. This information can be obtained by specifying somewhere in the input file (but NOT inside the RESPONSE or EXCITATION block keys): 

::

  PRINT DIPOLEMAT

.. _TDCDFT: 
.. index:: TDCDFT 
.. index:: time-dependent current DFT 

Time-dependent Current DFT
==========================

The time-dependent current-density-functional (TDCDFT) implementation is built entirely upon the normal TDDFT implementation. Therefore all general remarks that are made for the TDDFT part of the program are also valid for TDCDFT. Only the polarizability and excitation energies of closed shell molecules can be calculated with TDCDFT in the present implementation. 

If TDCDFT is used together with the ALDA functional (NOVK option) it will give the same results for the polarizability and excitation energies as TDDFT in a complete basis set. TDCDFT in ADF by default uses the VK functional [#ref15]_ [#ref16]_, since this is the only current dependent functional that is known presently. Many aspects of the functional are still unknown and the functional should therefore be used with caution. The user is referred to the references for more information on when the VK functional gives good results and when not. 

For more information on the implementation and applications of the TDCDFT and the VK functional please read the references [#ref28]_ [#ref29]_ [#ref30]_ [#ref31]_. For more details on the theory and implementation in ADF see: [#ref17]_. 

To activate TDCDFT and the VK functional one should add the following block key to the input file: 

.. _keyscheme CURRENTRESPONSE: 

::

  CURRENTRESPONSE
  END

To calculate the polarizability the keyword Response can be used with the following options: 

::

  RESPONSE
    ALLCOMPONENTS
    Frequencies freq1 freq2 ... freqN
  END

The block key EXCITATION can be used with all of its options. 

In ADF2012 the block keyword AORESPONSE can also be used with the Vignale-Kohn functional. The current-density is generated on the fly but otherwise the computation is based on the time dependent density response. 

In default the VK functional will be applied where the NCT parametrization [#ref19]_ is chosen for the transverse exchange-correlation kernel for the polarizability and singlet excitation energies (giving the best results for the systems studied so far). For triplet excitation energies the only available parametrization will be used  [#ref20]_. This option is not tested much and the results are in general much worse than ALDA [#ref17]_. It is therefore suggested that VK is not used to calculate triplet excitation energies. 

In the output the polarizability tensor (in case of an ALLCOMPONENTS calculation) has a different shape, the results are printed in the more intuitive order x, y, z, instead of y, z, x that the TDDFT implementation uses. 

The following subkeys are available within the datablock of CURRENTRESPONSE 

::

  CURRENTRESPONSE
    QIANVIGNALE
    NOVK
  END

``QIANVIGNALE``
  The QV parametrization [#ref20]_ will be used for the transverse exchange-correlation kernel instead of NCT. 

``NOVK``
  TDCDFT will be applied with the ALDA functional instead of the VK functional. In a complete basis this will give the same results as a TDDFT calculation. 


.. _MTDCDFT:
.. index:: rotational g-tensor
.. index:: magnetic TDCDFT 

Magnetic properties within TDCDFT
---------------------------------

It is now possible to calculate several magnetic properties via TDCDFT, among which magnetizabilities, rotational g-tensors, NMR shielding constants, specific rotations and circular dichroism. This alternative method is based on the diamagnetic-current sum rule, which consists of rewriting the diamagnetic current in terms of the response functions. This is the magnetic analogue of the conductivity sum rule, which is invalid when an external magnetic field is applied.

Details on the method can be found in these references: [#ref22]_ [#ref23]_.
Further details regarding the implementation can be found in the following PhD thesis as well: [#ref24]_.

In order to obtain these properties, the following subkeys can be used:

::

  CURRENTRESPONSE
    MAGNET
    GTENSOR
    NMRSHIELDING
    CDSPEC
    DAMPING Damping
  END

Depending on which property is calculated, the program chooses a reference point for the external vector potential (see references). For the magnetizability, the center of electronic charges is chosen, while for the rotational g-tensor, the center of nuclear charges is picked up. This choice has no influence in the static case, and has no influence neither for the specific rotations nor for the circular dichroism. It actually only affects the dynamical magnetizabilities (the rotational g-tensor being always computed at zero frequency). Below is a brief description of each subkey and how to use them.

``MAGNET``
  The (static or dynamical) magnetizability tensor.
``GTENSOR``
  The rotational g-tensor, calculated directly from the magnetizability.
``NMRSHIELDING``
  The NMR shielding tensor. Care should be taken when using this keyword, though, as it was observed that the results failed to match experimental and other theoretical studies when using standard basis sets except for the lightest elements. Only when using very large basis sets should the results be trusted.
``CDSPEC``
  Calculates both the specific rotation and the circular dichroism. This keyword should be used in combination with DAMPING if one wants to simulate CD spectra. The output spectrum will exhibit relatively sharp peaks. Linear-interpolating the results with a third-tier program is then necessary. This is done on purpose, so that the final spectrum could be broadened easily (only the absolute amplitudes of the peaks will be affected by this broadening).
``DAMPING Damping``
  Adds a (fixed) damping factor to the response function. This allows one to avoid divergences that may arise from the response function when close to resonance, hence helping the self-consistent cycle converge. The value for Damping should be given in eV. A value of 0.1 eV seems to be reasonable.

.. only:: html

  .. rubric:: References

.. [#ref1] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Implementation of time-dependent density functional response equations*, `Computer Physics Communications 118, 119 (1999) <https://doi.org/10.1016/S0010-4655(99)00187-3>`__ 

.. [#ref2] S.J.A. van Gisbergen, `*Molecular Response Property Calculations using Time Dependent Density Functional Theory*, in *Chemistry*. 1998, <http://downloads.scm.com/Doc/gisbergen.pdf.tar.gz>`__ Vrije Universiteit: Amsterdam. p. 190. 

.. [#ref3] E.K.U. Gross, J.F. Dobson and Petersilka, in *Density Functional Theory*, R.F. Nalewajski, Editor. 1996, Springer: Heidelberg. 

.. [#ref4] R.\  van Leeuwen and E.J. Baerends, *Exchange-correlation potential with correct asymptotic behavior*, `Physical Review A 49, 2421 (1994) <https://doi.org/10.1103/PhysRevA.49.2421>`__ 

.. [#ref5] M.\  Grüning, O.V. Gritsenko, S.J.A. van Gisbergen and E.J. Baerends, *Shape corrections to exchange-correlation Kohn-Sham potentials by gradient-regulated seamless connection of model potentials for inner and outer region*, `Journal of Chemical Physics 114, 652 (2001) <https://doi.org/10.1063/1.1327260>`__ 

.. [#ref6] P.R.T. Schipper, O.V. Gritsenko, S.J.A. van Gisbergen and E.J. Baerends, *Molecular calculations of excitation energies and (hyper)polarizabilities with a statistical average of orbital model exchange-correlation potentials*, `Journal of Chemical Physics 112, 1344 (2000) <https://doi.org/10.1063/1.480688>`__ 

.. [#ref7] M.\  Grüning, O.V. Gritsenko, S.J.A. van Gisbergen and E.J. Baerends, *On the required shape correction to the LDA and GGA Kohn Sham potentials for molecular response calculations of (hyper)polarizabilities and excitation energies*, `Journal of Chemical Physics 116, 9591 (2002) <https://doi.org/10.1063/1.1476007>`__ 

.. [#ref8] O.V. Gritsenko, P.R.T. Schipper and E.J. Baerends, *Approximation of the exchange-correlation Kohn-Sham potential with a statistical average of different orbital model potentials*, `Chemical Physics Letters 302, 199 (1999) <https://doi.org/10.1016/S0009-2614(99)00128-1>`__ 

.. [#ref12] S.J.A. van Gisbergen, V.P. Osinga, O.V. Gritsenko, R. van Leeuwen, J.G. Snijders and E.J. Baerends, *Improved density functional theory results for frequency-dependent polarizabilities, by the use of an exchange-correlation potential with correct asymptotic behavior*, `Journal of Chemical Physics 105, 3142 (1996) <https://doi.org/10.1063/1.472182>`__ 

.. [#ref13] M.E. Casida, C. Jamorski, K.C. Casida and D.R. Salahub, *Molecular excitation energies to high-lying bound states from time-dependent density-functional response theory: Characterization and correction of the time-dependent local density approximation ionization threshold*, `Journal of Chemical Physics 108, 4439 (1998) <https://doi.org/10.1063/1.475855>`__ 

.. [#ref14] V.P. Osinga, S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Density functional results for isotropic and anisotropic multipole polarizabilities and* C\ :sub:`6` , C\ :sub:`7` , and C\ :sub:`8` *Van der Waals dispersion coefficients for molecules*, `Journal of Chemical Physics 106, 5091 (1997) <https://doi.org/10.1063/1.473555>`__ 

.. [#ref15] G.\  Vignale and W. Kohn, *Current-Dependent Exchange-Correlation Potential for Dynamical Linear Response Theory*, `Physical Review Letters 77, 2037 (1996) <https://doi.org/10.1103/PhysRevLett.77.2037>`__ 

.. [#ref16] G.\  Vignale and W. Kohn, in *Electronic Density Functional Theory: Recent Progress and New Direction*, ISBN13: 9780306458347, J. F. Dobson, G. Vignale, and M. P. Das, Editors. 1998, Plenum: New York. 

.. [#ref17] M.\  van Faassen, `Time-Dependent Current-Density-Functional Theory for Molecules, <http://downloads.scm.com/Doc/faassen.pdf>`__ PhD thesis, Rijksuniversiteit Groningen, 2004. 

.. [#ref19] R.\  Nifosi, S. Conti and M. P. Tosi, *Dynamic exchange-correlation potentials for the electron gas in dimensionality D=3 and D=2*, `Physical Review B 58: p. 12758 (1998) <https://doi.org/10.1103/PhysRevB.58.12758>`__ 

.. [#ref20] Z.X. Qian and G. Vignale, *Dynamical exchange-correlation potentials for the electron liquid in the spin channel*, `Physical Review B 68, 195113 (2003) <https://doi.org/10.1103/PhysRevB.68.195113>`__ 

.. [#ref22] N.\  Raimbault, P.L. de Boeij, P. Romaniello, and J.A. Berger, *Gauge-Invariant Calculation of Static and Dynamical Magnetic Properties from the Current Density*, `Physical Review Letters 114, 066404 (2015) <https://doi.org/10.1103/PhysRevLett.114.066404>`__

.. [#ref23] N.\  Raimbault, P.L. de Boeij, P. Romaniello, and J.A. Berger, *Gauge-Invariant Formulation of Circular Dichroism*, `Journal of Chemical Theory and Computation 12, 3278 (2016) <https://doi.org/10.1021/acs.jctc.6b00068>`__

.. [#ref24] N.\  Raimbault, `Gauge-invariant magnetic properties from the current <https://tel.archives-ouvertes.fr/tel-01235055>`__, PhD thesis, Université Paul Sabatier, LCPQ, Toulouse, 2015

.. [#ref25] S.J.A. van Gisbergen, J.G. Snijders, and E.J. Baerends, *Time-dependent Density Functional Results for the Dynamic Hyperpolarizability of* C\ :sub:`60`, `Physical Review Letters 78, 3097 (1997) <https://doi.org/10.1103/PhysRevLett.78.3097>`__ 

.. [#ref26] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Calculating frequency-dependent hyperpolarizabilities using time-dependent density functional theory*, `Journal of Chemical Physics 109, 10644 (1998) <https://doi.org/10.1063/1.477762>`__ 

.. [#ref27] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Accurate density functional calculations on frequency-dependent hyperpolarizabilities of small molecules*, `Journal of Chemical Physics 109, 10657 (1998) <https://doi.org/10.1063/1.477763>`__ 

.. [#ref28] M.\  van Faassen, P. L. de Boeij, R. van Leeuwen, J. A. Berger and J. G. Snijders, *Ultranonlocality in Time-Dependent Current-Density-Functional Theory: Application to Conjugated Polymers*, `Physical Review Letters 88, 186401 (2002) <https://doi.org/10.1103/PhysRevLett.88.186401>`__ 

.. [#ref29] M.\  van Faassen, P. L. de Boeij, R. van Leeuwen, J. A. Berger and J. G. Snijders, *Application of time-dependent current-density-functional theory to nonlocal exchange-correlation effects in polymers*, `Journal of Chemical Physics 118, 1044 (2003) <https://doi.org/10.1063/1.1529679>`__ 

.. [#ref30] M.\  van Faassen and P. L. de Boeij, *Excitation energies for a benchmark set of molecules obtained within time-dependent current-density functional theory using the Vignale-Kohn functional*, `Journal of Chemical Physics 120, 8353 (2004) <https://doi.org/10.1063/1.1697372>`__ 

.. [#ref31] M.\  van Faassen and P. L. de Boeij, *Excitation energies of* :math:`\Pi` *-conjugated oligomers within time-dependent current-density-functional theory*, `Journal of Chemical Physics 121, 10707 (2004) <https://doi.org/10.1063/1.1810137>`__ 
