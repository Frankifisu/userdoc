
.. _excitation energies: 


Excitation energies: UV/Vis, X-ray, CD, MCD
*******************************************

Ultraviolet-visible (UV/Vis) spectroscopy studies electronic excitations of valence electrons, whereas X-ray spectroscopy studies electronic excitations of core electrons. Excitation energies and oscillator strengths are all available in ADF as applications of time-dependent DFT (TDDFT). Excitation energies can be calculated for closed-shell as well as for open-shell molecules. It is also possible to include spin-orbit coupling and to calculate core excitations (X-ray absorption spectra). Circular dichroism (CD) is the differential absorption of left- and right-handed circularly polarized light. 

.. index:: excitation energies 
.. index:: UV/Vis 
.. index:: singlet-singlet excitations 
.. index:: singlet-triplet excitations 
.. _UV_VIS: 

.. tip::
  
  See also the ADF Advanced TDDFT tutorial: `TDDFT Study of 3 different Dihydroxyanthraquinones <../../Tutorials/OpticalPropertiesElectronicExcitations/TDDFT_NBO.html>`__ 

Excitation energies, UV/Vis spectra
===================================

You can perform a calculation of singlet-singlet and singlet-triplet excitation energies of a closed-shell molecule by supplying in the input file the block key EXCITATION. See the next sections for settings of technical parameters, the calculation of excitation energies for open shell molecules, inclusion of spin-orbit coupling, and the calculation of CD spectra. 

.. _keyscheme EXCITATIONS: 


::

   EXCITATIONS
    EXACT
      {IRREP1 N1}
      {IRREP2 N2}
    END
    DAVIDSON
      {IRREP3 N3}
      {IRREP4 N4}
    END
    ALLOWED
    ONLYSING
    ONLYTRIP
    LOWEST nlowest 
   End

Several options can be addressed with subkeys in the data block. This functionality is based on TDDFT and consequently has a different theoretical foundation than the SCF techniques described elsewhere in this User's Guide. Two possible ways are available to solve the eigenvalue equation from which the excitation energies and oscillator strengths are obtained, of which the iterative Davidson procedure is the default. In this case, the program needs to know how many excitation energies are needed per irrep, what accuracy is required, and what type of excitation energies are required (singlet-singlet or singlet-triplet). Suitable defaults have been defined for all of these. Each of these points is discussed below. 

``Exact diagonalization vs. iterative Davidson procedure``
   The most straightforward procedure is a direct diagonalization of the matrix from which the excitation energies and oscillator strengths are obtained. Since the matrix may become very large, this option is possible only for very small molecules. It can be activated by specifying the block EXACT as one of the subkeys in the Excitations data block. The default is the iterative Davidson method. A few of the lowest excitation energies and oscillator strengths are then found within an error tolerance. An advantage of the EXACT option is that additional information is produced, such as the Cauchy coefficients that determine the average dipole polarizability. The EXACT option can not be used in unrestricted calculations. 

``Singlet versus triplet``
   By default, the singlet-singlet and singlet-triplet excitation energies are both calculated. The singlets are handled first, then the corresponding triplet excitation energies. One can skip one of these two parts of the calculation by specifying either ONLYSING or ONLYTRIP as a subkey in the data block. 

   In case of a calculation including spin-orbit coupling one can not separate the singlet-singlet and singlet-triplet excitations. The subkeys ONLYSING and ONLYTRIP are misused in this case to do a spin-restricted calculation, or a spin-polarized calculation, respectively. One should in fact only use the results of the spin-polarized calculation. 

.. index:: dipole allowed 

``Dipole-allowed versus general excitations.``
   If you are interested in the optical absorption spectrum, you may not want to compute singlet-triplet excitation energies, nor singlet-singlet excitation energies which, by symmetry, have zero oscillator strengths. This subkey should not be used in case of spin-orbit coupling. The subkey ALLOWED tells ADF to treat only those irreducible representations for which the oscillator strengths will be nonzero. Of course, the oscillator strengths may still be negligibly small. The ALLOWED subkey automatically implies ONLYSING. The simplest, fastest, and recommended way to obtain information about the ten lowest dipole-allowed excitation energies would be: 

.. index:: Davidson algorithm 

::

   EXCITATIONS
    ALLOWED
    LOWEST 10
   END

``Which excitation energies and how many?``
   The user can specify how many excitation energies per irrep should be calculated. If no pertaining input is available the program determines these numbers from the smallest differences between occupied and virtual Kohn-Sham orbital energies. By default it looks at the 10 lowest orbital energy differences. This number can be modified, by specifying inside the Excitation block key, for example::

     LOWEST 30

   One should be aware that this procedure does not guarantee that the lowest 10 (or 30) excitation energies will actually be found, since the orbital energy difference approximation to the excitation energy is rather crude. However, if the program decides on the basis of this procedure to calculate 4 excitation energies in a certain irreducible representation, these 4 excitation energies are certainly the lowest in that particular irrep. 

   The user has more control when the number of excitations per irrep is explicitly specified within the EXCITATION block key by the Davidson subkey::

      DAVIDSON
       E'' 5
       T1.u 2
      END


   The DAVIDSON sub block may contain any number of records and must end with a record END. In the subkey data block a list of irreps, followed by the number of requested excitation energies is specified. Note that the irrep name may not be identical to the usual ADF name. For example E'' is called EEE in ADF. The Excitation code will skip an irrep if the label is not recognized. For multidimensional irreps, only the first column is treated, because the other would produce identical output. This implies that the oscillator strengths for E-irreps have to be multiplied by 2 and the oscillator strengths for T-irreps by 3. The ALLOWED subkey should not be used if irreps are specified with the Davidson block subkey, however, the subkey ONLYSING (or ONLYTRIP) can be used in this case. 

   The EXACT sub-block, mentioned already above, can also be used to treat only a few irreps instead of all. The number of excitation energies does not have to be specified then. 

Some early applications of the Excitation feature in ADF can be found in Refs. [#ref45]_  [#ref46]_  [#ref47]_  [#ref48]_  [#ref49]_  [#ref50]_.

In case of closed shell molecules the unrelaxed excited state electric dipole moment is calculated, see Ref. [#ref60]_.
In case of a TDDFT-gradients calculation also the relaxed excited state electric dipole moment is calculated.
For the definition of unrelaxed and relaxed excited state density, see Ref. [#ref59]_.

.. index:: TDA 
.. index:: Tamm-Dancoff approximation 
.. _TDA:


Tamm-Dancoff approximation
--------------------------

Excitation energies can be calculated using the Tamm-Dancoff approximation (TDA) [#ref1]_ if one includes, besides the EXCITATION block key, the key TDA: 

.. _keyscheme TDA: 

::

   TDA




.. index:: full XC kernel 
.. _full xc kernel:


Full XC kernel
--------------

With XCFUN the full (non-ALDA) kernel can be evaluated, see the  :ref:`XCFUN description <XCFUN>`. To use the non-ALDA kernel the keyword FULLKERNEL should be put in the EXCITATIONS block.
FULLKERNEL can be used with GGAs (including hybrids and RS functionals) but not meta-GGAs or meta-hybrids.
For some of the LibXC functionals (mostly GGA's and hybrids) it also possible to use the Full (non-ALDA) kernel.
FULLKERNEL can not be used in combination with excited state geometry optimizations or other response properties.
If symmetry is used, recommended is to check that SYMMETRY NOSYM gives the same results.

::

   XC
    ...
    XCFUN
   End
   EXCITATIONS
    ...
    FullKernel
   END

::

   XC
    LibXC ...
   End
   EXCITATIONS
    ...
    FullKernel
   END

Singlet-triplet excitations are now also possible with FULLKERNEL.

Plasmons in Molecules
---------------------

In Ref. [#ref2]_ a scaling approach was used to identify plasmons in molecules.
To identify plasmons in general molecules, they proposed to analyze the excitations by scaling the electron-electron interaction in the response calculation.
While single-particle excitations are only slightly affected by this scaling, plasmonic excitations are sensitive to variations in the scaling parameter :math:`\lambda`.
More specifically, their squared excitation energies should increase linearly with the scaling parameter :math:`\lambda`.
Scaling of Coulomb, XC, and HF parts of the response kernel in TDDFT, can be performed
using the subkeywords SCALECOUL, SCALEXC, SCALEHF in the EXCITATIONS block.

::

   EXCITATIONS
      SCALECOUL scalecoul
      SCALEXC   scalexc
      SCALEHF   scalehf
   END

``SCALECOUL scalecoul``
  Scaling of Coulomb kernel with scale parameter scalecoul.

``SCALEXC scalexc``
  Scaling of the XC-kernel (excluding a possible HF-part) with scale parameter scalexc.

``SCALEHF scalehf``
  Scaling of the HF part of the kernel with scale parameter scalehf.

.. _ESESTDM: 

Transition dipole moments between excited states
------------------------------------------------

In Ref. [#ref60]_ transition dipole moments (electric dipole approximation) between different excited states are calculated.
In ADF these transition dipole moments between different calculated excited states can be calculated if the subkey ESESTDM is included.
Spin-orbit coupling can also be included.
Only implemented for closed shell molecules.

::

   EXCITATIONS
      ESESTDM
   END

``ESESTDM``
  Compute transition dipole moments between excited states.


Accuracy and other technical parameters
---------------------------------------

For details regarding the (near linear scaling and parallelized) implementation, please check Refs. [#ref3]_ [#ref4]_.

A summary of technical parameters with their defaults is: 

::

   EXCITATIONS
    VECTORS 40
    TOLERANCE 1e-6
    ORTHONORMALITY 1e-8
    ITERATIONS 200
    KFWRITE 3
   END

``VECTORS vectors``
   The maximum number of trial vectors in the Davidson algorithm for which space is allocated. If this number is small less memory will be needed, but the trial vector space is smaller and has to be collapsed more often, at the expense of CPU time. The default if usually adequate. 

``TOLERANCE tolerance``
   Specifies the error tolerance in *the square* of the excitation energies in Hartree units. The default is probably acceptable but we recommend that you verify the results against a stricter default (e.g. 1e-8) for at least a few cases. 

``ORTHONORMALITY orthonormality``
   The Davidson algorithm orthonormalizes its trial vectors. Increasing the default orthonormality criterion increases the CPU time somewhat, but is another useful check on the reliability of the results. 

``ITERATIONS iterations``
   The maximum number of attempts within which the Davidson algorithm has to converge. The default appears to be adequate in most cases. 

``KFWRITE kfwrite``
   If kfwrite is 0 then do not write contributions, transition densities, and restart vectors to adf.rkf, since this can lead to a huge adf.rkf, especially if many excitations are calculated. Default value kfwrite is 3, which means that contributions, transition densities, and restart vectors are written to adf.rkf. 

.. _EXCITATION_OPEN: 
.. index:: open shell TDDFT 
.. index:: doublet-quartet excitations 
.. index:: unrestricted excitations 

Excitation energies for open-shell systems
==========================================

Excitation energies can be obtained for open-shell systems in a spin-unrestricted TDDFT calculation [#ref5]_. To perform an open-shell TDDFT calculation one just needs to do an unrestricted SCF calculation and use the EXCITATION keyword. Presently the excitation energies can only be found with Davidson's procedure. In case of spin-orbit coupling, see the section on  :ref:`approximate spin-orbit coupled excitation energies open shell molecule<excitations SO>`. 

The printed symmetry in the output in TDDFT calculations is actually the symmetry of transition density. For closed-shell systems, the symmetry of the excited state is the same as the symmetry of the transition density, while for open-shell systems, the symmetry of the excited states is the direct product between the symmetry of the transition density and the ground state symmetry. Note that the ground state symmetry of an open shell molecule is not necessarily A1. 

For degenerate representations such as the 2-dimensional E-representations or the 3-dimensional T-representations, the occupation should be either fully occupied or zero. For example, for an orbital in an E-representation the :math:`\alpha` and :math:`\beta` occupation number should be either 2 or 0. The :math:`\alpha` occupation number can of course be different from the :math:`\beta` occupation number. 

As for the spin-state, the general rule is that if the excited state mainly results from transitions from the singly occupied orbitals to virtual orbitals or from fully occupied orbitals to the singly occupied orbitals, the spin state of the excited state should roughly be the same as that of the ground state. However, if the excited state mainly comes from transitions from fully occupied orbitals to virtual orbitals, the spin state of the excited state are usually a mixture since TDDFT can only deal with single excitations within adiabatic approximation for the XC kernel [#ref7]_. Sometimes we just suppose the spin state of this kind of excited states to be the same as that of ground state [#ref5]_. In the MO → MO transitions part for the excitations of the output file, the spin of each molecular orbitals are also specified to help assign the spin state of the excited states. The transitions are always from :math:`\alpha` spin-orbital to :math:`\alpha` spin-orbital or from :math:`\beta` spin-orbital to :math:`\beta` spin-orbital. 

.. index:: spin-flip excitations 

Spin-flip excitation energies
=============================

Spin-flip excitation energies [#ref8]_ [#ref9]_ can only be obtained in a spin-unrestricted TDDFT calculation. This can not be used in case of spin-orbit coupling. At present, the spin-flip excitation energies can only be calculated with Tamm-Dancoff approximation (TDA) [#ref1]_ and Davidson's method. 

To calculate spin-flip excitation energies, one must specify two keys:  

.. _keyscheme SFTDDFT: 


::

   SFTDDFT
   TDA

anywhere in the input file in addition to the EXCITATION block keyword. 

In spin-flip TDDFT, the XC kernel can be calculated directly from the XC potential. To use the LDA potential for the XC kernel, which roughly corresponds to the ALDA in ordinary TDDFT, one must specify the key 

.. _keyscheme FORCEALDA: 


::

   FORCEALDA

anywhere in the input file. Only calculations using the LDA potential in the SCF are fully tested. Using other GGA potentials in the SCF and using the FORCEALDA key at the same time may introduce unreasonable results, while using LB94 or SAOP potential in the SCF without the FORCEALDA key may give unstable results. Unstable results have been reported for the PW91 functional. 

For open-shell molecules, spin-flip transition can result in transition to the ground state with a different S\ :sub:`z`  value, while the symmetry of the transition density is A1. The excitation energy of this transition should be zero and this can be used to test the reliability of spin-flip TDDFT. 

The symmetry of the excited states can be determined in the same way as that in spin-unrestricted TDDFT calculations. As for the spin state, similar to that in the spin-unrestricted TDDFT calculations, some states may be more or less pure spin states, others may just be mixtures. The users can interpret the excited state through the transitions that contribute to this state. Note that the transitions are always from :math:`\alpha` spin-orbital to :math:`\beta` spin-orbital in spin-flip calculations, or from :math:`\beta` spin-orbital to :math:`\alpha` spin-orbital. 

.. _EXCITATION_CORE: 
.. index:: core excitations 

Select (core) excitation energies, X-ray absorption
===================================================

Two methods can be used to reduce the computational costs of, for example, core excitation energies, or some other high lying excitation energy. In the state selective method scheme a guess vector for the orbital transition has to be provided. An overlap criterion is used to follow the wanted eigenvector. In this scheme the one-electron excited state configuration space remains complete, see Ref [#ref12]_. In the second scheme, the range of excitations that are calculated is modified, which means that the one-electron excited state configuration space is reduced to the interesting part, see Ref. [#ref11]_. The calculated excited states are more accurate with the state selective method if convergence is reached, however, the second scheme is more robust, and it is easier to find convergence. 

These selection methods can, for example, also be used in case one calculates excitation energies as Kohn-Sham orbital energy differences, see subkey :ref:`SINGLEORBTRANS<keyscheme SINGLEORBTRANS>` of the key EXCITATIONS. 

For X-ray spectra it can be important to include quadrupole intensities.

.. index:: state selective excitations 

State selective optimization excitation energies
------------------------------------------------

The state selective method (key SELECTEXCITATION) can be used to reduce the computational costs of, for example, core excitation energies. In this scheme a guess vector for the orbital transition has to be provided. It should be used in combination with the Davidson method to calculate excitation energies. An overlap criterion is used to follow the wanted eigenvector. This method for state selective optimization of excitation energies is based on the method by Kovyrshin and Neugebauer, see Ref. [#ref12]_. This key can also be used in case of spin-orbit coupling. The use of the key SELECTEXCITATION is similar as the use of the key MODIFYEXCITATION. However, the key SELECTEXCITATION can not be used in combination with the key MODIFYEXCITATION. In the state selective method (key SELECTEXCITATION) the one-electron excited state configuration space remains complete, whereas it is reduced in case the scheme with the MODIFYEXCITATION key. 

The starting guess vector(s) for the excitation energies can be selected, for example by selecting 1 occupied orbital and 1 virtual orbital. 

.. _keyscheme SELECTEXCITATION: 


::

   SELECTEXCITATION
      OscStrength oscstrength
      UseOccVirtRange elowoccvirt ehighoccvirt
      UseOccVirtNumbers nrlowoccvirt nrhighoccvirt
      UseOccRange elowocc ehighocc
      UseVirtRange elowvirt ehighvirt
      UseOccupied
         irrep orbitalnumbers
         irrep orbitalnumbers
         ...
      SubEnd
      UseVirtuaL
         irrep orbitalnumbers
         irrep orbitalnumbers
         ...
      SubEnd
      UseScaledZORA
   end

``OscStrength oscstrength``
   Use only pairs of an occupied and virtual orbital as guess vectors, for which the oscillator strength of the single-orbital transition is larger than oscstrength. 

``UseOccVirtRange elowoccvirt ehighoccvirt``
   Use only pairs of an occupied and virtual orbital as guess vectors, for which the orbital energy difference is between elowoccvirt and ehighoccvirt (in hartree). If one is interested in the lowest excitation energies, use for elowoccvirt a value smaller than the HOMO-LUMO gap, and for ehighoccvirt a value larger than the energy range one is interested in.

``UseOccVirtNumbers nrlowoccvirt nrhighoccvirt``
   Use only pairs of an occupied and virtual orbital as guess vectors, for which in the sorted list of the orbital energy differences, the number of the single-orbital transition is between nrlowoccvirt and nrhighoccvirt. 

``UseOccRange elowocc ehighocc``
   Use only occupied orbitals in the guess vectors which have orbital energies between elowocc and ehighocc (in hartree). 

``UseVirtRange elowvirt ehighvirt``
   Use only virtual orbitals in the guess vectors which have orbital energies between elowvirt and ehighvirt (in hartree). 

``UseOccupied``
   Use only the occupied orbitals in the guess vectors which are specified. 

``UseVirtual``
   Use only the virtual orbitals in the guess vectors which are specified. 

``irrep``
   The name of one of the irreducible representations (not a subspecies) of the point group of the system. See the Appendix for the irrep names as they are used in ADF. 

``orbitalnumbers``
   A series of one or more numbers: include all numbers of the orbitals in the guess vectors that are to be used. In an unrestricted calculation the same numbers are used for the spin-:math:`\alpha` orbitals and the spin-:math:`\beta` orbitals. 


.. _MODIFYEXCITATION:

Modify range of excitation energies
-----------------------------------

The key MODIFYEXCITATION can be used to reduce the computational costs of, for example, core excitation energies. This key can also be used in case of spin-orbit coupling. The use of the key MODIFYEXCITATION is similar as the use of the key SELECTEXCITATION. However, the key MODIFYEXCITATION can not be used in combination with the key SELECTEXCITATION. In the state selective method (key SELECTEXCITATION) the one-electron excited state configuration space remains complete, whereas it is (effectively) reduced in case the scheme with the MODIFYEXCITATION key. 

One possibility is to allow only selected occupied orbitals and or selected virtual orbitals in the TDDFT calculations. In this scheme the complete one-electron excited state configuration space is reduced to the subspace where only the core electrons are excited, see Stener et al. [#ref11]_. In the actual implementation this is done by artificially changing the orbital energies of the uninteresting occupied orbitals to a large negative value (default -1d6 Hartree), and by by artificially changing the orbital energies of the uninteresting virtual orbitals to a large positive value (default 1d6). 

In ADF2010 an extra possibility is added with the new subkey UseOccVirtRange, which restricts the space of excitation energies, by allowing only pairs of occupied and virtual orbitals, for which the difference in orbital energy is between a certain range. 

.. _keyscheme MODIFYEXCITATION: 


::

   MODIFYEXCITATION
      OscStrength oscstrength
      UseOccVirtRange elowoccvirt ehighoccvirt
      UseOccVirtNumbers nrlowoccvirt nrhighoccvirt
      UseOccRange elowocc ehighocc
      UseVirtRange elowvirt ehighvirt
      UseOccupied
         irrep orbitalnumbers
         irrep orbitalnumbers
         ...
      SubEnd
      UseVirtuaL
         irrep orbitalnumbers
         irrep orbitalnumbers
         ...
      SubEnd
      SetOccEnergy esetocc
      SetLargeEnergy epsbig
      UseScaledZORA
   end

``OscStrength oscstrength``
   Use only pairs of an occupied and virtual orbital as guess vectors, for which the oscillator strength of the single-orbital transition is larger than oscstrength. 

``UseOccVirtRange elowoccvirt ehighoccvirt``
   Use only pairs of an occupied and virtual orbital, for  which the orbital energy difference is between elowoccvirt and ehighoccvirt (in hartree). 

``UseOccVirtNumbers nrlowoccvirt nrhighoccvirt``
   Use only pairs of an occupied and virtual orbital as guess vectors, for which in the sorted list of the orbital energy differences, the number of the single-orbital transition is between nrlowoccvirt and nrhighoccvirt. 

``UseOccRange elowocc ehighocc``
   Use only occupied orbitals which have orbital energies between elowocc and ehighocc (in Hartree). 

``UseVirtRange elowvirt ehighvirt``
   Use only virtual orbitals which have orbital energies between elowvirt and ehighvirt (in Hartree). 

``UseOccupied``
   Use only the occupied orbitals which are specified. 

``UseVirtual``
   Use only the virtual orbitals which are specified. 

``irrep``
   The name of one of the irreducible representations (not a subspecies) of the point group of the system. See the Appendix for the irrep names as they are used in ADF. 

``orbitalnumbers``
   A series of one or more numbers: include all numbers of the orbitals that are to be used. In an unrestricted calculation the same numbers are used for the spin-:math:`\alpha` orbitals and the spin-:math:`\beta` orbitals. 

``SetOccEnergy esetocc``
   All occupied orbitals that have to be used will change their orbital energy to esetocc. In practice only useful if one has selected one occupied orbital energy, and one want to change this to another value. Default: the orbital energies of the occupied orbitals that are used are not changed. 

``SetLargeEnergy epsbig``
   The orbital energies of the uninteresting occupied orbitals are changed to -epsbig Hartree, and the orbital energies of the uninteresting virtual orbitals are changed to epsbig Hartree (Default: epsbig = 1d6 Hartree). 

``UseScaledZORA``
   Use everywhere the scaled ZORA orbital energies instead of the ZORA orbital energies in the TDDFT equations. This can improve deep core excitation energies. Only valid if ZORA is used. Default: use the unscaled ZORA orbital energies. 

.. index:: single orbital transition
.. index:: KSSPECTRUM
.. index:: XAS

Excitations as orbital energy differences
-----------------------------------------

Instead of the relative expensive TDDFT calculation of excitation energies, sometimes just calculating Kohn-Sham orbital energy differences may already be useful.
The subkeyword SINGLEORBTRANS in the block key EXCITATIONS, will calculate excitation energies as Kohn-Sham orbital energy differences.
The subkeyword SINGLEORBTRANS in the block key EXCITATIONS replaces the obsolete key KSSPECTRUM.
For a given excitation from an occupied orbital to a virtual orbital the oscillator strength is calculated from the the dipole transition moment between this occupied orbital and this virtual orbital.
This method is best suited if LDA or a GGA is used in the SCF.

Especially useful for core excitation energy calculations.
If SINGLEORBTRANS is used, it is possible to use fractional occupation numbers in the SCF, like is used in the DFT transition state (DFT-TS) scheme, see, for example, Ref. [#ref15]_.
Note: for fractional occupation numbers, typically an orbital is treated in the excitation calculation as if it is fully occupied if the occupation number is 1.5 or more, and it is treated as if it is fully unoccupied if the occupation number is 0.5 or less. 
In the transition state procedure for core excitations half an electron is moved from an initial core orbital to final virtual orbital
and the SCF KS eigenvalue difference is taken as excitation energy.
This is the original Slater formulation and is justified doing a Taylor expansion of total energy with respect to occupation numbers, it can be shown that errors arise from
third order terms which are small.
This,  however, is not very practical: to converge SCF by putting half an electron in virtual orbitals is very hard,
usually it works only for the lowest virtuals.
In order to avoid this problem one neglects the half an electron in virtual, this scheme (only half an electron
removed from occupied orbital) is called Transition Potential (TP) and is widely employed in XAS from K-edges.


.. _keyscheme SINGLEORBTRANS: 

::

   EXCITATIONS
    SingleOrbTrans
   END

``SingleOrbTrans``
   keyword to use only orbital energy differences 

The value for the subkeyword KFWRITE in the EXCITATIONS block key is set by default to 0 in case of SINGLEORBTRANS. If kfwrite is 0 then do not write contributions, transition densities, and restart vectors to adf.rkf, since this can lead to a huge adf.rkf, especially if many excitations are calculated.



.. index:: quadrupole oscillator strength
.. index:: XAS
.. _quadrupole oscillator strength: 

Quadrupole intensities in X-ray spectroscopy
--------------------------------------------

For electronic excitations in the ultraviolet and visible range of the electromagnetic spectrum,
the intensities are usually calculated within the dipole approximation,
which assumes that the oscillating electric field is constant over the length scale of the transition.
For the short wavelengths used in hard X-ray spectroscopy, the dipole approximation may not be adequate.
In particular, for metal K-edge X-ray absorption spectroscopy (XAS), it becomes necessary to include higher-order contributions.
An origin-independent calculation of quadrupole intensities in XAS was implemented in ADF by Bernadotte et al., see Ref. [#ref16]_.
These quadrupole intensities may also be important for the calculation of X-ray emission spectroscopy, see :ref:`section on XES<XES>`.
Can not be used in combination with spin-orbit coupling.

Usage

::

   EXCITATION
     ...
     XAS
     {ALLXASMOMENTS}
     {ALLXASQUADRUPOLE}
   END


``XAS``
   Use XAS within the EXCITATION block to initiate the calculation of the higher oder multipole moment integrals and the calculation of the quadrupole oscillator strengths.
   This will only print the total oscillator strength and the excitation energy.

``ALLXASMOMENTS``
   Use ALLXASMOMENTS within the EXCITATION block in combination with the XAS keyword.
   This will print out all the individual transition moments used within the calculation of the total oscillator strength.

``ALLXASQUADRUPOLE``
   Use ALLXASQUADRUPOLE within the EXCITATION block in combination with the XAS keyword.
   This will print out the individual oscillator strength components to the total oscillator strength.

The :ref:`MODIFYEXCITATION<keyscheme MODIFYEXCITATION>` or :ref:`SELECTEXCITATION<keyscheme SELECTEXCITATION>` keyword could be used to select
a core orbital.

.. index:: XES
.. _XES: 

XES: X-ray emission spectroscopy
================================

For the calculation of XES (X-ray emission spectroscopy) spectra the approach of Ref. [#ref17]_ is implemented in the ADF program by Atkins et. al., see Ref. [#ref18]_.
This is a frozen orbital, one-electron ΔDFT approach which uses orbital energy differences between occupied orbitals to model the X-ray emission energies.
Even though it is the simplest possible approximation for the calculation of XES spectra,
it has been shown to work well for V2C-XES (valence-to-core X-ray emission spectroscopy) spectra of transition metal complexes.

The XES keyword initiates the calculation of X-ray emission energies to a core orbital.
In addition to dipole oscillator strengths this keyword also triggers the calculation of the higher order moment integrals
and the calculation of the quadrupole oscillator strengths.
By default it calculates the emission to the first orbital in the first symmetry,
often the deepest core orbital,
and only prints the total oscillator strength and the excitation energy.
Can not be used in combination with spin-orbit coupling.

.. _keyscheme XES: 

::

   XES
      {COREHOLE irrep number}
      {ALLXESMOMENTS}
      {ALLXESQUADRUPOLE}
   END

``COREHOLE irrep number``
   This allows the selection of the acceptor orbital for the calculation of the emission oscillator strengths.
   For example 'COREHOLE A1 2' calculates oscillator strengths to the orbital 2 in irrep A1.

``ALLXESMOMENTS``
   Use ALLXESMOMENTS within the XES block.
   This will print out all the individual transition moments used within the calculation of the total oscillator strength.

``ALLXESQUADRUPOLE``
   Use ALLXESQUADRUPOLE within the XES block.
   This will print out the individual oscillator strength components to the total oscillator strength.

.. index:: excitation energies spin-orbit 
.. index:: TDDFT SO 
.. index:: spin-orbit excitation energies 
.. index:: zero-field splitting
.. index:: ZFS excited state 
.. index:: SOCME
.. _excitations SO: 


Excitation energies and Spin-Orbit coupling
===========================================

Spin-orbit coupling can be included in the TDDFT calculation of excitation energies for closed-shell molecules. Two methods can be used in ADF. The first one includes spin-orbit coupling as a perturbation to a scalar relativistic calculation of excitation energies, in which spin-orbit coupling matrix elements (SOCMEs) between excited states are calculated. The second one includes spin-orbit coupling self-consistently in the ground state calculation. If spin-orbit coupling is large, the second one is more accurate, but is also more time-consuming. 

The results of these spin-orbit coupled TDDFT calculations include the calculation of the zero field splitting (ZFS) of triplet excited states and the calculation of radiative rate constants, which could be used to calculate radiative phosphorescence lifetimes. 


.. _excitations SOPERT: 

Perturbative inclusion of spin-orbit coupling
---------------------------------------------

.. _keyscheme SOPERT:

::

   SOPERT 
     {NCALC ncalc} 
     {ESHIFT eshift}
     {GSCorr Yes/No}
   End
   Relativity
     Level Scalar
     Formalism ZORA
   End
   EXCITATIONS
   END

The perturbative method, which is described in Ref. [#ref19]_, is an approximate time-dependent density-functional theory (TDDFT) formalism to deal with the influence of spin-orbit coupling effect on the excitation energies for closed-shell systems. In this formalism scalar relativistic TDDFT calculations are first performed to determine the lowest single-group excited states and the spin-orbit coupling operator is applied to these single-group excited states to obtain the excitation energies with spin-orbit coupling effects included. The computational effort of the present method is much smaller than that of the two-component TDDFT formalism. The compositions of the double-group excited states in terms of single-group singlet and triplet excited states are obtained automatically from the calculations. In Ref. [#ref19]_ it was shown that the calculated excitation energies based on the present formalism affords reasonable excitation energies for transitions not involving 5p and 6p orbitals. For transitions involving 5p orbitals, one can still obtain acceptable results for excitations with a small truncation error, while the formalism will fail for transitions involving 6p orbitals, especially 6p1/2 spinors. 

Although this method is not completely correctly implemented for (meta-)hybrids or Hartree-Fock, it still gives reasonable excitation energies, and can thus be useful also in that case. Note that SYMMETRY C(2H) is not implemented for spin-orbit coupled excitations, use SYMMETRY C(S), C(I) or NOSYM, instead. 

``NCALC=ncalc``
   Number of spin-orbit coupled excitation energies to be calculated. Default (and maximum) value: 4 times the number of scalar relativistic singlet-singlet excitations. 

``ESHIFT=eshift``
   The actually calculated eigenvalues are calculated up to the maximum singlet-singlet or singlet-triplet scalar relativistic excitation energy plus eshift (in Hartree). Default value: 0.2 Hartree. 

``GSCORR Yes/No``
   The singlet ground state is included, which means that spin-orbit coupling can also have some effect on energy of the ground state. The spin-orbit matrix in this case is on basis of the ground state and the singlet and triplet excited states. Default Yes.


Some extra information about the spin-obit matrix is written to the output if one includes

::

   SOPERT 
     {NCALC ncalc} 
     {ESHIFT eshift}
     {GSCorr Yes/No}
   End
   PRINT SOMATRIX

If one includes PRINT SOMATRIX the spin-orbit matrix (in Hartree) on basis of singlet and triplet excited states will be printed.
Note that a triplet has three sublevels.
The numbering of the basis of singlets and triplets is given above the spin-orbit matrix.
The spin-orbit matrix has a real and imaginary part.
On the diagonal the singlet or triplet energies is added.
This spin-orbit matrix is the one that is diagonalized to get the spin-orbit coupled excitation energies. 
For example, for the effect of spin-orbit coupling between T1 and S1 one finds 3 complex values, between the 3 sublevels of T1 and the one level of S1.
For a magnitude one could take the square root of the (real part squared + imaginary part squared).

Starting from ADF2018 these spin-orbit coupling matrix elements (SOCMEs) are printed in an easier format in the ouput.
The SOCME that is printed is calculated as a root mean square: square root
of (the sum of squares of spin-orbit coupling matrix elements of all sublevels of the uncoupled states).

Self-consistent spin-orbit coupling
-----------------------------------

::

   Relativity
     Level Spin-Orbit
     Formalism ZORA
   End
   EXCITATIONS
     {ALSORESTRICTED}
   END

Starting from the ADF2006.01 version in ADF the relativistic TDDFT formalism, including spin-orbit coupling, is implemented for closed-shell molecules with full use of double-group symmetry [#ref20]_. This relativistic time-dependent density-functional theory (TDDFT) is based on the two-component zeroth-order regular approximation (ZORA) and a noncollinear exchange-correlation (XC) functional. This two-component TDDFT formalism has the correct non-relativistic limit and affords the correct threefold degeneracy of triplet excitations. 

In case of a calculation including spin-orbit coupling one can not separate the singlet-singlet and singlet-triplet excitations. By default the spin-polarized excitation energies are calculated (the noncollinear scheme is used for the spin-dependent exchange-correlation kernel). The subkeys ALSORESTRICTED can be used to include also excitation energies in which a spin-restricted exchange-correlation kernel is used. One should in fact only use the results of the spin-polarized calculation, which is based on the noncollinear exchange-correlation (XC) functional. For the same reason, the ALLOWED subkey should not be used if spin-orbit coupling is included. Note that SYMMETRY C(2H) is not implemented for spin-orbit coupled excitations, use SYMMETRY C(S), C(I) or NOSYM, instead. 

To perform a spin-orbit coupled TDDFT calculation one just needs to do a spin-orbit coupled SCF calculation and use the EXCITATION keyword. The molecule needs to be closed shell, and should be calculated spin-restricted. Thus do not use the UNRESTRICTED, COLLINEAR, or NONCOLLINEAR keyword. See, however, also next section. 

The contribution to the double group excited states in terms of singlet and triplet single group excited states can be estimated through the inner product of the transition density matrix obtained from two-component and scalar relativistic TDDFT calculations to better understand the double group excited states [#ref21]_. In order to get this analysis one needs to perform a scalar relativistic TDDFT calculation of excitation energies on the closed shell molecule first, and use the resulting adf.rkf as a fragment in the spin-orbit coupled TDDFT calculation of excitation energies, including the keyword STCONTRIB (Singlet and Triplet CONTRIButions): 

.. _keyscheme STCONTRIB: 


::

   STCONTRIB

This STCONTRIB analysis is not performed for (meta-)hybrids, unless one uses the Tamm-Dancoff approximation (TDA) approximation, but then it may also fail. If one wants a similar analysis for (meta-)hybrids one may consider to the perturbative inclusion of spin-orbit coupling in the calculation of excitation energies.

Note that if hybrids are used, the dependency key is automatically set, and this may effectively reduce the number of excitations, which may give problems in the STCONTRIB analysis. A workaround for these problems is to first calculate the scalar relativistic fragment without the EXCITATIONS keyword. Use the adf.rkf of this calculation as fragment in a scalar relativistic calculation with the EXCITATIONS keyword. Use the adf.rkf of the second calculation as fragment in the spin-orbit coupled calculation, including the STCONTRIB keyword. 


Highly approximate spin-orbit coupled excitation energies open shell molecule
-----------------------------------------------------------------------------

Excitation energies can be obtained for open-shell systems in a spin-unrestricted TDDFT calculation including spin-orbit coupling. This approximate method uses a single determinant for the open shell ground state. The Tamm-Dancoff approximation (TDA) is needed and symmetry NOSYM should be used. Best is to use the noncollinear approximation. For analysis it is advised to calculate the molecule also with the scalar relativistic spin-restricted method and use it as fragment in the spin-orbit coupled calculation. This will make it easier to identify the excitations. 

::

   Unrestricted
   Symmetry NOSYM
   Relativity
     Level Spin-Orbit
     Formalism ZORA
     SpinOrbitMagnetization NONCOLLINEAR
   End
   TDA
   Excitations
   End

Note that this approximate method for open shell molecules is not able to show the subtle effects of spin-orbit coupling. Some of the reasons are the approximate nature of the XC functionals for open shell molecules, the single determinant that is used for the open shell ground state,  and that only single excitations are included in the excitation. If one does not include spin-orbit coupling the spin-unrestricted TDDFT approach introduces spin-contamination such that the result does not represent transitions between pure spin states. Inclusion of spin-orbit coupling will not simplify this. However, if spin-orbit coupling is large, then this method may help to identify excitations. 

Note that the approximations made in this approximate method are much worse than for spin-orbit coupled TDDFT for closed shell systems. In that case one can get a reasonable description of the subtle effects of spin-orbit coupling, for example, for the zero-field splitting of a triplet excited state. 

.. index:: CV(n)-DFT
.. index:: CVDFT
.. index:: constricted variational DFT
.. _CVNDFT: 

CV(n)-DFT: Constricted Variational DFT
======================================

In the constricted nth order variational density functional method (CV(n)-DFT) [#ref22]_ [#ref6]_ [#ref23]_ the occupied excited state orbitals are allowed to relax in response to the change of both the Coulomb and exchange-correlation potential in going from the ground state to the excited state.
This theory is not time-dependent nor is it based on response theory. It is instead variational in nature and has been termed constricted variational DFT or CV(n)-DFT.

Due to bugs in older versions it is important to use ADF2016.105 or later.
In ADF2017 the relaxation density is a bit differently calculated than in ADF2016, which will slightly modify the results compared to ADF2016.
In ADF2017 singlet-triplet excitations are added [#ref24]_
There have been different working equations implemented in different modified versions of ADF.
In ADF2016 and ADF2017 all CV-DFT excitation energies are calculated consistently, this is why some energies may
differ from previously published values.

CV(n)-DFT requires an all electron basis set.

The CVNDFT block key regulates the execution of the CV(n)-DFT code, which calculates the singlet or triplet
electronic excitations for the closed shell molecules. 
Note that one has to choose either singlet-singlet excitations (subkey ONLYSING in EXCITATIONS) or singlet-triplet excitations
(subkey ONLYTRIP in EXCITATIONS), in case of CV(n)-DFT, one can not calculate them both in one run.
The parameter n in (n) describes the
order of this theory. There are two limiting cases implemented in the CV(n)-DFT code: n=2
and n= :math:`\infty`. Since CV(n)-DFT coincides in the second order with TDDFT, CV(n)-DFT code is 
designed as an extension of the EXCITATIONS module. Therefore, the EXCITATIONS block has to be 
present in the input file together with CVNDFT. CVNDFT takes all the information about the number 
of excitations and their symmetry from the EXCITATIONS block. Moreover, the TDDFT transition 
density vectors are used as an initial guess for the CV(:math:`\infty`)-DFT calculations.


There are a few approximations within the CV(:math:`\infty`)-DFT approach, therefore there are a few 
corresponding sub-blocks in the CVNDFT block. In the simplest case the TDDFT transition density
U-vector is substituted into the infinite order CV(:math:`\infty`)-DFT excitation energy. 
This approximation corresponds to the CV_DFT sub-block, so the input fragment would look like 
this:

.. _keyscheme CVNDFT: 

::

   CVNDFT
     CV_DFT &
     SUBEND
   END
   EXCITATIONS
     ONLYSING|ONLYTRIP
     ...
   END

In general, the U-vector has to be optimized with respect to the infinite order 
CV(:math:`\infty`)-DFT excitation energy. It is accomplished iteratively in the SCF-CV(:math:`\infty`)-DFT 
method [#ref25]_, which is invoked when the SCF_CV_DFT sub-block is present. Therefore, there are 
input parameters that control the SCF procedure, i.e. the total number of iterations and 
tolerance. The corresponding input fragment would look like this:

::

   CVNDFT
     ITERATION iter
     TOLERANCE tol
     SCF_CV_DFT &
       DAMPING mix
     SUBEND
   END
   EXCITATIONS
     ONLYSING|ONLYTRIP
     ...
   END

``iter``
  iter is the maximum number of iterations. Default 50.

``tol``
  tol is the convergence criterion, i.e.  the SCF-CV(:math:`\infty`)-DFT procedure stops when the given accuracy is achieved. Default 1e-4.

``mix``
  mix is the relative weight of the new U-vector that is added to the one from the previous iteration (default value is mix=0.2).

Another feature of CV(:math:`\infty`)-DFT is a possibility to optimize (or relax) the molecular 
orbitals for the particular excitation. This is accomplished in the R-CV(:math:`\infty`)-DFT method, see for an application Ref. [#ref26]_.
In the last case, the transition U-vector is frozen, while the orbitals are relaxed.
For example, the input fragment which employs the U-vector from TDDFT would look like 
this:

::

   CVNDFT
     ITERATION iter
     TOLERANCE tol
     R_CV_DFT &
       RELAXALPHA start_a_iter
       RELAXBETA  start_b_iter
       DAMPORBRELAX mix_relax
     SUBEND
   END
   EXCITATIONS
     ONLYSING|ONLYTRIP
     ...
   END

``start_a_iter``
  start_a_iter is the SCF cycle number at which the relaxation of :math:`\alpha` orbitals starts. Default value 1.

``start_b_iter``
  start_b_iter is the SCF cycle number at which the relaxation of :math:`\beta` orbitals starts. Default value 1.

  Since there is no optimization of the U-vector in R-CV(:math:`\infty`)-DFT, the relaxation of orbitals (either :math:`\alpha` or :math:`\beta` or both) should be turned on at the very first iteration.

``mix_relax``
  The mix_relax parameter defines the relative weight of the new relaxation vector that is added to the one from the previous iteration (the default value is mix_relax=0.2).

Note that all tree methods can be used in the input file. The corresponding input fragment would look like this:

::

   CVNDFT
     ITERATION iter
     TOLERANCE tol
     CV_DFT & 
     SUBEND
     SCF_CV_DFT &
       DAMPING mix
     SUBEND
     R_CV_DFT &
       RELAXALPHA start_a_iter
       RELAXBETA  start_b_iter
       DAMPORBRELAX mix_relax
     SUBEND
   END
   EXCITATIONS
     ONLYSING|ONLYTRIP
     ...
   END

In this case the U-vector will be optimized with respect to the infinite 
order CV(:math:`\infty`)-DFT excitation energy by the SCF-CV(:math:`\infty`)-DFT code and then 
supplied to the R-CV(:math:`\infty`)-DFT code.

CVNDFT prints in the output the excitation energies as well as the maximum value of 
the lambda parameter :math:`\lambda`. This number corresponds to the largest singular value of the 
singular value decomposition of the U matrix/vector (i.e. the U-vector can be considered 
as a matrix with *nvir* rows and *nocc* columns, where *nvir* is the number of virtual 
orbitals and *nocc* is the number of occupied orbitals). If this number is close to 
:math:`\pi / 2` (i.e. :math:`\lambda_{max} \approx 1.57`), then the corresponding electronic 
excitation can be approximated by a single natural transition orbital (NTO) to another 
single NTO transition. This type of transitions are obtained in :math:`\Delta` SCF. Therefore, 
this information can be used, for example, to compare the CV(:math:`\infty`)-DFT results 
to the :math:`\Delta` SCF excitation energies.

.. index:: HDA
.. _HDA:

HDA: Hybrid Diagonal Approximation
==================================

This method is only relevant if a (meta-)hybrid is used in the SCF.
The hybrid diagonal approximation (HDA) [#ref58]_ is based on utilizing the hybrid exchange only for the diagonal terms in the response equations to calculate excitations.
This allows one to limit the computational cost of the TD-DFT simulation while keeping basically the same accuracy as in the full TD-DFT scheme using hybrid xc-functionals.
It is furthermore not necessary to correct all the diagonal terms with hybrid exchange.
A cutoff parameter can be chosen in the input in order to reduce the number of diagonal terms that have to be calculated, which can speed up the HDA calculations.

::

   EXCITATIONS
    HDA
    HDA_CutOff hda_cutoff
   End

``HDA``
  Activate the hybrid diagonal approximation (HDA).

``hda_cutoff``
  Cutoff on difference in energy between virtual and occupied orbitals eps_virt-eps_occ, in order to reduce the number of diagonal terms that are corrected.
  Default is a huge value, which means that all diagonal terms are corrected.


This method can not be used in excited state geometry optimizations.
For spin-orbit coupled HDA excitations one needs to use symmetry NOSYM:

::

   relativity
    level spin-orbit
   end
   Symmetry NOSYM
   EXCITATIONS
    HDA
    HDA_CutOff hda_cutoff
   End


.. index:: TD-DFT+TB
.. index:: TD-DFTB
.. _TD-DFTB:

TD-DFT+TB
===========

The basis idea of TD-DFT+TB [#ref27]_ is to use the molecular orbitals from a DFT ground state calculation as input to an excited state calculation with TD-DFTB coupling matrices. TB means tight binding.
If many excitations are required, this method will speed up the calculation drastically in comparison to the standard time needed for TDDFT calculations of excitation energies.
This method is best suited if a (meta-)GGA or LDA is used in the SCF.
This method can not be used in excited state geometry optimizations.

::

   SYMMETRY NOSYM
   EXCITATIONS
    TD-DFTB
   END

One can use this, for example, in combination with the :ref:`MODIFYEXCITATION key<MODIFYEXCITATION>` to use only single-orbital transitions that have a minimal oscillator strength:

::

   SYMMETRY NOSYM
   EXCITATIONS
    TD-DFTB
    ONLYSING
   END
   MODIFYEXCITATION
     OscStrength 0.001
   End

In TD-DFT+TB reducing the space of single-orbital transitions with the key MODIFYEXCITATION will reduce the memory needed in ADF.
Starting from ADF2016.102 for TD-DFT+TB only the lowest (in energy) 100000 single orbital transitions are included by default.
One can override this by using a different value for the subkey UseOccVirtNumbers of the key MODIFYEXCITATION.

::

   MODIFYEXCITATION
    UseOccVirtNumbers 1 100000
   END

The value for the subkeyword KFWRITE in the EXCITATIONS block key is set by default to 0 in case of TD-DFT+TB. If kfwrite is 0 then do not write contributions, transition densities, and restart vectors to adf.rkf, since this can lead to a huge adf.rkf, especially if many excitations are calculated.


.. index:: sTDA
.. index:: sTDDFT
.. _sTDA:
.. _sTDDFT:

sTDA, sTDDFT
============

The simplified Tamm-Dancoff approach (sTDA) [#ref28]_ and simplified time-dependent DFT approach (sTDDFT) [#ref29]_ by Grimme et al. are implemented in ADF.
In these approaches the time-dependent DFT equations are simplified by the evaluation of the two-electron integrals as short-range damped Coulomb interactions between (transition) charge density monopoles and a truncation of the single excitation expansion space.
These methods are best suited if a (meta-)hybrid or a range-separated-hybrid is used in the SCF.
These methods will speed up the calculation drastically in comparison to the standard time needed for TDA or TDDFT calculations of excitation energies for hybrids.
Theses methods can not be used in excited state geometry optimizations.

An example application of sTDDFT is given in the `TDDFT advanced tutorial <../../Tutorials/OpticalPropertiesElectronicExcitations/TDDFT_NBO.html#faster-tddft-variant-stddft>`__

For sTDA use:

::

   SYMMETRY NOSYM
   EXCITATIONS
    sTDA
   END

For sTDDFT use:

::

   SYMMETRY NOSYM
   EXCITATIONS
    sTDDFT
   END

For global hybrids ADF will use the parameters :math:`\alpha` and :math:`\beta` that depend on the amount of exact exchange 
:math:`a_x` as:

.. math::

  \alpha = \alpha_1 + \alpha_2 a_x \\
  \beta = \beta_1 + \beta_2 a_x

where :math:`\alpha_1 = 1.42`, :math:`\alpha_2 = 0.48`, :math:`\beta_1 = 0.2`, :math:`\beta_2 = 1.83` are used in ADF.
These values are fitted parameters by Grimme [#ref28]_.
For range-separated hybrids one should set the parameters :math:`\alpha`, :math:`\beta` and :math:`a_x` in the input of ADF with the keyword MODIFYEXCITATION.
See Ref. [#ref31]_ for parameters that are used by Risthaus et al. for a few range-separated functionals.
However the :math:`\alpha` and :math:`\beta` parameters are mixed up in Ref. [#ref31]_. 
Thus use:

.. csv-table:: 
   :widths: 200,100,100,100

   
   **Functional**, :math:`a_x`, :math:`\alpha`, :math:`\beta`
   CAM-B3LYP, 0.38, 0.90, 1.86
   WB97,      0.61, 4.41, 8.00
   WB97X,     0.56, 4.58, 8.00

For example, for CAM-B3LYP use

::

   MODIFYEXCITATION
     GrimmeAlpha 0.9
     GrimmeBeta 1.86
     GrimmeAex 0.38
   END

If one uses the keyword MODIFYEXCITATION one may also set more parameters that are used in the sTDA and sTDDFT approach.

::

   MODIFYEXCITATION
     GrimmeAlpha Alpha
     GrimmeBeta Beta
     GrimmeAex Aex
     GrimmeDEmax DEmax
     GrimmeTPmin TPmin
     GrimmePertC|NoGrimmePertC
   END

``GrimmeAlpha Alpha``
   To set the :math:`\alpha` parameters, should be used icw GrimmeBeta and GrimmeAex.

``GrimmeBeta Beta``
   To set the :math:`\beta` parameters, should be used icw GrimmeAlpha and GrimmeAex.

``GrimmeAex Aex``
   To set :math:`a_x` that is used in the sTDA or sTDDFT part of the calculation, should be used icw GrimmeAlpha and GrimmeBeta.

``GrimmeDEmax DEmax``
   Single orbital transitions that have an orbital energy difference less than DEmax (in Hartree) are included. Default value DEmax = 0.4 Hartree.
   See also the meaning of :math:`E_{max}` in Grimme [#ref28]_.

``GrimmeTPmin TPmin``
   Single orbital transitions that would have a cumulative perturbative energy contribution larger than TPmin is included.
   Default value TPmin = :math:`10^{-4}`. See also the meaning of :math:`t_p` in Grimme [#ref28]_.

``GrimmePertC|NoGrimmePertC``
  In case of GrimmePertC, which is the default, if the cumulative perturbative energy contribution for a single orbital transition is smaller TPmin, this contribution is used to modify the diagonal value of a matrix that is used in the sTDA or the sTDDFT method.
  If NoGrimmePertC is included such contributions are neglected.
  See Grimme [#ref28]_ for more details on the truncation of the single excitation space.

Starting from ADF2016.102 for sTDA or sTDDFT only the lowest (in energy) 10000 single orbital transitions are included by default.
One can override this by using a different value for the subkey UseOccVirtNumbers of the key MODIFYEXCITATION.

::

   MODIFYEXCITATION
    UseOccVirtNumbers 1 10000
   END

The value for the subkeyword KFWRITE in the EXCITATIONS block key is set by default to 0 in case of sTDA or sTDDFT. If kfwrite is 0 then do not write contributions, transition densities, and restart vectors to adf.rkf, since this can lead to a huge adf.rkf, especially if many excitations are calculated.



.. index:: CD spectrum 
.. index:: circular dichroism 

CD spectra
==========

Circular dichroism (CD) is the differential absorption of left- and right-handed circularly polarized light. Starting from ADF2010 Hartree-Fock and hybrids can also be used to calculate CD spectra. 

.. _keyscheme CDSPECTRUM: 

::

   EXCITATIONS
    CDSPECTRUM
    ANALYTICAL
    VELOCITY
   End

``CDSPECTRUM``
   If the subkey *CDSPECTRUM* is included in the key EXCITATIONS the rotatory strengths for the calculated excitations are calculated, in order to simulate Circular Dichroism (CD) spectra [#ref36]_ [#ref37]_. Interesting for chiral molecules. This subkey should not be used in case of spin-orbit coupling. For accuracy reasons you should also use the subkey *ANALYTICAL* in the block key EXCITATIONS, otherwise the results may be nonsense. 

``ANALYTICAL``
   If the subkey *ANALYTICAL* is included the required integrals for the CD spectrum are calculated analytically, instead of numerically. Only used in case of CD spectrum. 

``Velocity``
   If the subkey *VELOCITY* is included ADF calculates the dipole-velocity representation of the oscillator strength. If applicable (use of subkey *CDSPECTRUM*) the dipole-velocity representation of the rotatory strength is calculated. Default the dipole-length representation of the oscillator strength and rotatory strength is calculated. 

MCD
===

.. _MCD: 

.. index:: MCD 

.. index:: magnetic circular dichroism 

MCD or magnetic circular dichroism is the differential absorption of left and right circularly polarized light in the presence of a magnetic field. MCD intensity is usually described in terms of different contributions called A, B and C terms, see Refs. [#ref38]_ [#ref39]_. A further parameter D is often discussed in MCD studies. D is proportional to the intensity of an absorption band and is closely related to the oscillator strength. A and B terms for closed and open-shell molecules and C terms of open-shell molecules induced by spin-orbit coupling can be calculated.  Starting from ADF2010 C terms related to spatially degenerate states, i.e. breaking of degeneracies can be calculated.  
The A term is only calculated in case the molecule has symmetry and then only for excited states that belong to multi-dimensional irreps.

For MCD calculations for molecules that have C(2) or D(2) symmetry use SYMMETRY NOSYM. 

.. _keyscheme MCD: 
.. _keyscheme SOMCD: 

**Input options**

::

   EXCITATIONS
      MCD {options}
      ONLYSINGLET
      {SELECT transition number}
      {DTENSOR {Dxx Dxy Dyy Dxz Dyz|D E/D}}
   End

   ALLPOINTS
   {Relativity
      Level Scalar
      Formalism ZORA
    End}
   {SOMCD}
   {ZFS}

``MCD``
   If the subkey MCD is included in the key EXCITATIONS the MCD parameters of some or all of the excitations considered in the TDDFT procedure are calculated [#ref51]_ [#ref52]_ [#ref53]_ [#ref41]_. This subkey should not be used with spin-orbit coupling (but, see below). Several other keywords could be important.

   ALLPOINTS: required for an MCD calculation.

   ONLYSINGLET: this keyword should be used in combination with a MCD calculation.

   RELATIVITY: Scalar Relativistic ZORA: required for a calculation of temperature-dependent C terms.
   In this case the keyword SOMCD must also be added as a key by itself, and the calculation must be unrestricted.
   If only A and B terms are calculated then ZORA is not needed but can be included if desired.

   ZFS: If the ZFS keyword and MCD with SOMCD are also included then the influence of the calculated zero-field splitting (ZFS) on the temperature-dependent MCD is evaluated. The MCD in the presence of ZFS is described as anisotropic in the output because the Zeeman splitting becomes orientation dependent in the presence of ZFS. 

   In ADF2010 the temperature-dependent MCD due to the breaking of degeneracies of excited states by spin-orbit coupling can be calculated. Although all temperature-dependent MCD is typically called "C terms", the parameters associated with the MCD are labeled "CE" to distinguish them from the MCD due to mixing between states caused by spin-orbit coupling that is labeled "C". The CE terms have a derivative shape like A terms. They have the same temperature-dependence as normal C terms. If they are present, CE terms are calculated automatically along with C terms if the keyword SOMCD is included in the input. 

``MCD {options}``
   Options include NMCDTERM, NMIX, DCUTOFF, MCDOUT, CGOUT, NANAL, NANAL2, FULLOMEGA, NOAB, NODIRECT, NOCG, CONVCG, ITERCG, ITER2CG, BMIN, BMAX, TMIN, TMAX and NTEMP. 

   ``NMCDTERM=nmcdterm``
      Number of excitations for which MCD parameters are to be calculated. The nmcdterm lowest energy excitations are treated. The default is the number of transitions considered in the TDDFT calculation. 

   ``NMIX=nmix``
      Number of transitions allowed to mix in a SOS calculation. Default is the number of transitions considered in the TDDFT calculation. 

   ``DCUTOFF=dcutoff``
      MCD parameters will only be calculated for transitions with sufficient intensity. Each Cartesian component of each transition is considered separately. If the dipole strength D of that component is below dcutoff then the MCD is not calculated. The default is 1.0e-6. 

   ``MCDOUT=mcdout``
      Number that determines the  amount of output to be printed about the MCD calculation. Higher means more output. Possible values are 0, (orientationally averaged and Cartesian components of MCD parameters only) 1 (as for 0 but with the addition of a short  analysis)  or 2 (as for 1 but with the addition of a lengthy analysis).  Theoretical analyses of MCD parameters are presented in several places including Refs. [#ref38]_ [#ref39]_ [#ref52]_ [#ref53]_ [#ref41]_. The default for MCDOUT is 0. 

   ``CGOUT=cgout``
      The perturbed transition densities used to evaluate  the B and C term parameters can be obtained through an iterative conjugate-gradient procedure. Convergence information of  the conjugate-gradient algorithm is printed every cgout iterations.  Default is 10. 

   ``NANAL=nanal, NANAL2=nanal2``
      If MCDOUT is set to 2, a detailed analysis of the B and/or C term parameters in terms of which states mix and  how much MCD each mixing causes, is presented. The parameters NANAL and NANAL2 determine how many contributions are included in the analyses. Defaults are 10 for NANAL and 5 for NANAL2. 

   ``FULLOMEGA``
      A standard  TDDFT calculation involves the solution of  an eigenvalue equation to obtain the excitation energies and  transition densities of interest. ADF can solve this eigenvalue equation  two ways: through diagonalization of the full Omega matrix or through the Davidson procedure where Omega is never explicitly constructed.  Construction of the complete Omega matrix is generally only feasible for smaller problems. The matrix Omega appears again in the equations solved to obtain MCD. Here again Omega can be built or only the products of Omega with a vector can be used as is the case in the Davidson procedure. The default is to not construct Omega. If the keyword FULLOMEGA is included then Omega is constructed. Note that  the choice of FULLOMEGA is completely independent of whether EXACT or DAVIDSON is chosen in the earlier TDDFT calculation.   

   ``NOAB``
      If this keyword is included then A and B terms are not calculated.  NOAB only makes sense if SOMCD is included in the input otherwise no MCD will be calculated at all. 

   ``NODIRECT``
      The perturbed transition density needed to evaluate B and C term parameters is obtained through the solution of a large system of  equations. This system of equations is solved in two ways: through a sum-over-states (SOS) type approach where the solution is expanded in a known set of transition densities or through the direct solution of the system of equations by the conjugate gradient procedure. The SOS method is much faster but also less accurate, particularly for larger systems. By default MCD parameters are evaluated through both approaches. If the NODIRECT keyword is included then only the SOS calculation is performed. 

   ``NOCG``
      The conjugate gradient procedure is first used in combination with a preconditioner that generally speeds up convergence significantly. If no solution is found in a reasonable number of iterations then the procedure is restarted without the  preconditioner. If the NOCG keyword in included then the preconditioner is never used.  

   ``CONVCG``
      Convergence criterion for the CG iterative methods. The default value of 0.01 is probably good enough for most applications.  This choice seems to produce B and C terms that are converged to 3 significant figures. Except for small systems, it is not recommended that CONVCG be set to a much smaller number as this will probably cause a large number of convergence failures. 

   ``ITERCG=itercg``
      Number of iterations before failure in the first (preconditioned) CG solver. This solver either succeeds quickly or not at all so the default value is 30. 

   ``ITER2CG=iterc2g``
      Number of iterations before failure in the B of C term parameter calculation of the unconditioned CG solver.  This solver is often slow so the default value is 200. 

   ``BMIN=bmin, BMAX=bmax, NBFIELD=nbfield, TMIN=tmin, TMAX=tmax, NTEMP=ntemp``
      Temperature dependent MCD intensity often varies nonlinearly with T and B when T is small and/or B is large. It may therefore be of interest to evaluate the MCD intensity over a range of temperatures and/or magnetic fields. This can be achieved through the use of the BMIN, BMAX, NBFIELD, TMIN, TMAX and NTEMP keywords. The MIN and MAX keywords give the maximum values of B or T. NBFIELD and NTEMp indicate how many values are to be considered. Note that magnetic fields are assumed to be given in Tesla and temperatures in Kelvin. For example, BMIN=1, BMAX=5, NBFIELD=5 means that fields of 1,2,3,4 and 5 T will   be considered. Defaults are BMIN=BMAX=1, TMIN=TMAX=5 and NBFIELD=NTEMP=1. 

``SELECT nselect1 nselect2 nselect3...``
   Rather than selecting the first nmcdterm transitions for consideration individual transitions can be selected through the SELECT keyword. The transitions of interest are listed after the SELECT keyword. Note that the numbering follows that given in the summary table at the end of the TDDFT calculation. To consider a degenerate transition only the first component need be included. Note that it makes no sense to use both the SELECT and NMCDTERM keywords together. 

``DTENSOR Dxx Dxy Dyy Dxz Dyz`` ``DTENSOR D E/D``
   As noted earlier, if the ZFS keyword is included with MCD and SOMCD then the influence of zero-field splitting on temperature-dependent MCD will be evaluated. As an alternative to the ZFS keyword the D-tensor parameters can be entered directly through the DTENSOR keyword in the EXCITATIONS block. Two input formats are possible. Five real numbers Dxx Dxy Dyy Dxz Dyz can be entered. These five numbers are sufficient to define the traceless tensor D. Alternatively, the two parameters D and E/D can be entered. In this case the coordinate system chosen to define the molecular geometry must be the the principle axis system of the D-tensor. D, Dxx, Dxy, Dyy, Dxz and Dyz should be given in wavenumbers (cm-1). 

**Notes**

If an MCD calculation is run, the transition densities obtained in the TDDFT calculation are saved to adf.rkf. For large molecules this can result in a very large adf.rkf file. 

An MCD calculation relies on the excitation energies and, in particular, the transition densities that result from the preceding TDDFT calculation. If the results of the TDDFT calculation are poor then it is likely that the results of the MCD calculation will be poor. It therefore should be kept in mind that most TDDFT calculations will make use of the Davidson method for finding the eigenvalues and eigenvectors of the TDDFT equation. The Davidson approach involves some approximations that can lead to some variation in results with the applied parameters. The most important example of this is the fact that the results vary depending on how many eigenvalue/eigenvector  pairs are calculated, ie how many transitions are selected through the  LOWEST keyword. The variation is small for the eigenvalues (excitation energies) but can be significant for the eigenvectors (transition densities). A variation in the transition densities leads to variation in the transition dipoles which can significantly impact calculated MCD parameters. The moral of this story is that when calculating MCD parameters it is best to choose one value of LOWEST and stick with it. 

The most time-consuming part of an MCD calculation is the solution of the system of equations through the conjugate-gradient solver. The solver can fail so be aware of warnings concerning convergence in the output. A few hints to improve convergence are: a) choose a value of LOWEST that is at least double the number of transitions for which you desire MCD parameters. This helps to improve the SOS calculation which provides an initial guess for the conjugate gradient solver. The solver is sensitive to the initial guess so changing LOWEST by a small amount may help (or hinder) convergence significantly. Keep the previous note in mind when playing with LOWEST however. b) The preconditioned conjugate gradient solver is usually fast but does not converge monotonically to the correct answer. The unpreconditioned solver is much slower but tends to converge monotonically. If the preconditioned solver fails but leaves a fairly well converged result for the unpreconditioned solver the latter usually converges quickly. If the preconditioned solver does not leave a fairly well converged result it may be worth changing the number of iterations it uses since a few iterations earlier or later may provide a much better converged answer. c) The SELECT keyword can be used to work on the remaining transitions for which converged results  have not been obtained.  

All MCD parameters are presented in au. To convert A and C terms to the alternative unit D\ :sup:`2`  (Debye squared) the value in au should be multiplied by 6.46044. To convert the B term to the  alternative unit of D\ :sup:`2` /cm-1 the value in au should be multiplied by 2.94359e-05. 

The A, B and C terms are defined through the equation suggested by Stephens (equation 1 in [#ref41]_ and also see refs. [#ref38]_ [#ref39]_ [#ref40]_). This equation assumes that MCD intensity varies linearly with applied magnetic field and that the temperature-dependent component varies linearly with temperature as 1/T. For the most part, these assumptions are reasonable.  An exception  is  that the temperature-dependent part varies from linearity when T is very small. To allow for this situation a temperature and magnetic field dependent  multiplicative constant (chi(B,T)) is evaluated whenever temperature-dependent MCD parameters are considered. This constant includes all magnetic field and temperature dependence of the temperature-dependent MCD. Thus chi(B,T)*C can be used in place of B*C/kT in equation 1 of [#ref41]_ when  MCD spectra are to be simulated. Note that, since the g-factor for all states is here approximated by 2.0, chi applies to all transitions. 

.. _ANALYSISEXCITATION:

Analysis
========

By default the ADF output will show the excitation energies, oscillator strengths from ground state to excited state, and transition dipole moments from ground state to excited state.
Also an analysis in terms of single orbital transitions (occupied to virtual) is given, and their contributions to the transition dipole moment.
For analysis reasons one might be interested in pure single orbital transition.
Such information can be obtained in case one calculates excitation energies as Kohn-Sham orbital energy differences, see subkey :ref:`SINGLEORBTRANS<keyscheme SINGLEORBTRANS>` of the key EXCITATIONS.

.. _NTO:
.. index:: NTO

NTO: Natural Transition Orbitals
--------------------------------

Natural Transition Orbitals [#ref42]_ come from a transformation of the transition density matrix.
They are the closest you can get to visualizing an excitation as a one-electron excitation from 1 orbital to another.
They give insight in the localization of excitations.
Calculation of Natural Transition Orbitals (NTO's) will be performed if the subkey NTO is included in the key EXCITATIONS.

::

   EXCITATIONS
     ...
     NTO
   End

For (meta-)hybrids and range-separated functionals NTO's will be calculated only if one uses the Tamm-Dancoff approximation (TDA).

NTOs can be visualized in AMSspectra as shown in the `GUI tutorial <../../Tutorials/GettingStarted/ExcitationsAndUVVisOfEthene.html>`__ . 

.. _SFOEXCITATION:

SFO analysis
------------

In ADF2018 an SFO analysis of the excitation is implemented. This includes an analysis of the transition dipole moment.
Especially useful in a fragment calculation, where one only has a few fragments.
Not implemented for spin-orbit coupled excitations.

::

   EXCITATIONS
     ...
     SFOANALYSIS {NMAXPRINTED}
   End

``SFOANALYSIS {NMAXPRINTED}``
   If SFOANALYSIS is included a the SFO analysis of the excitation will be calculated. NMAXPRINTED is the maximum number of printed contributions. Default value for NMAXPRINTED is 40.

The SFO - SFO dipole matrix elements can be printed in the output with:

:: 

    PRINT DIPOLEMAT

.. index:: charge transfer descriptors
.. _CTDESCRIPTORS:

Charge-transfer descriptors
---------------------------

Two methods for calculating charge-transfer descriptors are implemented (also working for spin-orbit coupled excitations).

The first method is the charge-transfer diagnostic overlap quantity LAMBDA, developed by Peach, Tozer, et al. [#ref43]_
and a hole-electron distance R_EH, see  Guido, Adamo, et al. [#ref44]_.

The second method is the charge transfer descriptor CT, hole-electron distance R_EH, and some other descriptors, developed by Plasser, Lischka, et al. [#ref54]_ [#ref55]_ [#ref56]_ [#ref57]_. For this method a fragment calculation is required.
Using a similar method a charge transfer descriptor CT_AT was defined that uses an atomic distance criterion, which will also be calculated in case of atomic fragments.

::

   EXCITATIONS
     ...
     DESCRIPTORS
     {Descriptors_CT_AT_Rab Rab}
   END

``DESCRIPTORS``
   If DESCRIPTORS is included the charge transfer descriptors are calculated.

``Descriptors_CT_AT_Rab Rab``
   Rab is the atomic distance criterion used for the calculation of CT_AT (in Angstrom). Default value for Rab is 2 Angstrom.

.. only:: html

  .. rubric:: References

.. [#ref1] S.\  Hirata and M. Head-Gordon, *Time-dependent density functional theory within the Tamm-Dancoff approximation*, `Chemical Physics Letters 314, 291 (1999) <https://doi.org/10.1016/S0009-2614(99)01149-5>`__ 

.. [#ref2] S.\  Bernadotte, F. Evers, and C.R. Jacob, *Plasmons in Molecules*, `Journal of Physical Chemistry C 117, 1863 (2013) <https://doi.org/10.1021/jp3113073>`__ 

.. [#ref3] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Implementation of time-dependent density functional response equations*, `Computer Physics Communications 118, 119 (1999) <https://doi.org/10.1016/S0010-4655(99)00187-3>`__ 

.. [#ref4] S.J.A. van Gisbergen, C. Fonseca Guerra and E.J. Baerends, *Towards excitation energies and (hyper)polarizability calculations of large molecules. Application of parallelization and linear scaling techniques to time-dependent density functional response theory*, `Journal of Computational Chemistry 21, 1511 (2000) <https://doi.org/10.1002/1096-987X(200012)21:16%3C1511::AID-JCC8%3E3.0.CO;2-C/abstract>`__ 

.. [#ref5] F.\  Wang and T. Ziegler, *Excitation energies of some d1 systems calculated using time-dependent density functional theory: an implementation of open-shell TDDFT theory for doublet-doublet excitations*, `Molecular Physics 102, 2585 (2004) <https://doi.org/10.1080/0026897042000275080>`__ 

.. [#ref6] M.\  Krykunov and T. Ziegler, *Self-consistent Formulation of Constricted Variational Density Functional Theory with Orbital Relaxation. Implementation and Applications*, `Journal of Chemical Theory and Computation 9, 2761 (2013) <https://doi.org/10.1021/ct300891k>`__ 

.. [#ref7] Z.\  Rinkevicius, I. Tunell, P. Salek, O. Vahtras and H. Agren, *Restricted density functional theory of linear time-dependent properties in open-shell molecules*, `Journal of Chemical Physics 119, 34 (2003) <https://doi.org/10.1063/1.1577329>`__ 

.. [#ref8] F.\  Wang and T. Ziegler, *Time-dependent density functional theory based on a noncollinear formulation of the exchange-correlation potential*, `Journal of Chemical Physics 121, 12191 (2004) <https://doi.org/10.1063/1.1821494>`__ 

.. [#ref9] F.\  Wang and T. Ziegler, *The performance of time-dependent density functional theory based on a noncollinear exchange-correlation potential in the calculations of excitation energies*, `Journal of Chemical Physics 122, 74109 (2005) <https://doi.org/10.1063/1.1844299>`__ 

.. [#ref11] M.\  Stener, G. Fronzoni and M. de Simone, *Time dependent density functional theory of core electrons excitations*, `Chemical Physics Letters 373, 115 (2003) <https://doi.org/10.1016/S0009-2614(03)00543-8>`__ 

.. [#ref12] A.\  Kovyrshin, J. Neugebauer, *State-selective optimization of local excited electronic states in extended systems*, `Journal of Chemical Physics 133, 174114 (2010) <https://doi.org/10.1063/1.3488230>`__ 

.. [#ref15] R.\  De Francesco, M. Stener, and G. Fronzoni, *Theoretical Study of Near-Edge X-ray Absorption Fine Structure Spectra of Metal Phthalocyanines at C and N K-Edges*, `Journal of Physical Chemistry A, 116 2285 (2012) <https://doi.org/10.1021/jp2109913>`__ 

.. [#ref16] S.\  Bernadotte, A.J. Atkins, Ch.R. Jacob, *Origin-independent calculation of quadrupole intensities in X-ray spectroscopy*, `Journal of Chemical Physics 137, 204106 (2012) <https://doi.org/10.1063/1.4766359>`__ 

.. [#ref17] N.\  Lee, T. Petrenko, U, Bergmann, F. Neese, and S. DeBeer, *Probing Valence Orbital Composition with Iron Kβ X-ray Emission Spectroscopy*, `Journal of the American Chemical Society 132, 9715 (2010) <https://doi.org/10.1021/ja101281e>`__ 

.. [#ref18] A.J. Atkins, M. Bauer, and Ch.R. Jacob, *The chemical sensitivity of X-ray spectroscopy: high energy resolution XANES versus X-ray emission spectroscopy of substituted ferrocenes*, `Physical Chemistry Chemical Physics 15, 8095 (2013) <https://doi.org/10.1039/C3CP50999K>`__ 

.. [#ref19] F.\  Wang and T. Ziegler, *A simplified relativistic time-dependent density-functional theory formalism for the calculations of excitation energies including spin-orbit coupling effect*, `Journal of Chemical Physics 123, 154102 (2005) <https://doi.org/10.1063/1.2061187>`__ 

.. [#ref20] F.\  Wang, T. Ziegler, E. van Lenthe, S.J.A. van Gisbergen and E.J. Baerends, *The calculation of excitation energies based on the relativistic two-component zeroth-order regular approximation and time-dependent density-functional with full use of symmetry*, `Journal of Chemical Physics 122, 204103 (2005) <https://doi.org/10.1063/1.1899143>`__ 

.. [#ref21] F.\  Wang and T. Ziegler, *Theoretical study of the electronic spectra of square-planar platinum (II) complexes based on the two-component relativistic time-dependent density-functional theory*, `Journal of Chemical Physics 123, 194102 (2005) <https://doi.org/10.1063/1.2104427>`__ 

.. [#ref22] J.\  Cullen, M. Krykunov, and T. Ziegler, *The formulation of a self-consistent constricted variational density functional theory for the description of excited states*, `Chemical Physics 391, 11 (2011) <https://doi.org/10.1016/j.chemphys.2011.05.021>`__ 

.. [#ref23] T.\  Ziegler, M. Krykunov, I. Seidu, Y.C. Park, *Constricted Variational Density Functional Theory Approach to the Description of Excited States*, `Density Functional Methods for Excited States: Topics in Current Chemistry 368, 61 (2016) <https://doi.org/10.1007/128_2014_611>`__ 

.. [#ref24] Y.C. Park, F. Senn, M. Krykunov, and T. Ziegler, *Self-Consistent Constricted Variational Theory RSCF-CV(* :math:`\infty` *)-DFT and Its Restrictions To Obtain a Numerically Stable* :math:`\Delta` *SCF-DFT-like Method: Theory and Calculations for Triplet States*, `Journal of Chemical Theory and Computation 12, 5438 (2016) <https://doi.org/10.1021/acs.jctc.6b00333>`__

.. [#ref25] T.\  Ziegler, M. Krykunov, J. Cullen, *The implementation of a self-consistent constricted variational density functional theory for the description of excited states*, `Journal of Chemical Physics 136, 124107 (2012) <https://doi.org/10.1063/1.3696967>`__ 

.. [#ref26] F.\  Senn, M. Krykunov, *Excited State Studies of Polyacenes Using the All-Order Constricted Variational Density Functional Theory with Orbital Relaxation*, `Journal of Physical Chemistry A 119, 10575 (2015) <https://doi.org/10.1021/acs.jpca.5b07075>`__ 

.. [#ref27] R.\  Rüger, E. van Lenthe, T. Heine, L. Visscher, *Tight-Binding Approximations to Time-Dependent Density Functional Theory - a fast approach for the calculation of electronically excited states*, `Journal of Chemical Physics 144, 184103 (2016) <https://doi.org/10.1063/1.4948647>`__ 

.. [#ref28] S.\  Grimme, *A simplified Tamm-Dancoff density functional approach for the electronic excitation spectra of very large molecules*, `Journal of Chemical Physics 138, 244104 (2013) <https://doi.org/10.1063/1.4811331>`__ 

.. [#ref29] C.\  Bannwarth and S. Grimme, *A simplified time-dependent density functional theory approach for electronic ultraviolet and circular dichroism spectra of very large molecules*, `Computational and Theoretical Chemistry 1040-1041, 45 (2014) <https://doi.org/10.1016/j.comptc.2014.02.023>`__ 

.. [#ref31] T.\  Risthaus, A. Hansen, and S. Grimme, *Excited states using the simplified Tamm-Dancoff-Approach for range-separated hybrid density functionals: development and application*, `Physical Chemistry Chemical Physics 16, 14408 (2014) <https://doi.org/10.1039/C3CP54517B>`__ 

.. [#ref36] J.\  Autschbach and T. Ziegler, *Calculating molecular electric and magnetic properties from time-dependent density functional response theory*, `Journal of Chemical Physics 116, 891 (2002) <https://doi.org/10.1063/1.1420401>`__ 

.. [#ref37] J.\  Autschbach, T. Ziegler, S.J.A. van Gisbergen and E.J. Baerends, *Chiroptical properties from time-dependent density functional theory. I. Circular dichroism spectra of organic molecules*, `Journal of Chemical Physics 116, 6930 (2002) <https://doi.org/10.1063/1.1436466>`__ 

.. [#ref38] S.B. Piepho and P. N. Schatz, *Group Theory in Spectroscopy With Application to Magnetic Circular Dichroism*, (Wiley, New York, 1983). 

.. [#ref39] W.R. Mason, *A Practical Guide to Magnetic Circular Dichroism Spectroscopy*, (Wiley, New Jersey, 2007). 

.. [#ref40] A.\  Bérces and T. Ziegler, *The harmonic force field of benzene. A local density functional study*, `Journal of Chemical Physics 98, 4793 (1993) <https://doi.org/10.1063/1.464983>`__ 

.. [#ref41] M.\  Seth, T. Ziegler and J. Autschbach, *Application of magnetically perturbed time-dependent density functional theory to magnetic circular dichroism. III. Temperature-dependent magnetic circular dichroism induced by spin-orbit coupling*, `Journal of Chemical Physics 129, 104105 (2008) <https://doi.org/10.1063/1.2976568>`__ 

.. [#ref42] R.L. Martin, *Natural transition orbitals*, `Journal of Chemical Physics 118, 4775 (2003) <https://doi.org/10.1063/1.1558471>`__ 

.. [#ref43] M.J.G. Peach, P. Benfield, T. Helgaker, and D.J. Tozer, *Excitation energies in density functional theory: An evaluation and a diagnostic test*, `Journal of Chemical Physics 128, 044118 (2008) <https://doi.org/10.1063/1.2831900>`__

.. [#ref44] C.A. Guido, P. Cortona, B. Mennucci, and C. Adamo, *On the Metric of Charge Transfer Molecular Excitations: A Simple Chemical Descriptor*, `Journal of Chemical Theory and Computation 9, 3118 (2013) <https://doi.org/10.1021/ct400337e>`__

.. [#ref45] S.J.A. van Gisbergen, F. Kootstra, P.R.T. Schipper, O.V. Gritsenko, J.G. Snijders and E.J. Baerends, *Density-functional-theory response-property calculations with accurate exchange-correlation potentials*, `Physical Review A 57, 2556 (1998) <https://doi.org/10.1103/PhysRevA.57.2556>`__ 

.. [#ref46] S.J.A. van Gisbergen, A. Rosa, G. Ricciardi and E.J. Baerends, *Time-dependent density functional calculations on the electronic absorption spectrum of free base porphin*, `Journal of Chemical Physics 111, 2499 (1999) <https://doi.org/10.1063/1.479617>`__ 

.. [#ref47] A.\  Rosa, G. Ricciardi, E.J. Baerends and S.J.A. van Gisbergen, *The Optical Spectra of NiP, Nipz, NiTBP, and NiPc. Electronic effects of meso-tetraaza substitution and tetrabenzoannulation*, `Journal of Physical Chemistry A 105, 3311 (2001) <https://doi.org/10.1021/jp003508x>`__ 

.. [#ref48] G.\  Ricciardi, A. Rosa and E.J. Baerends, *Ground and Excited States of Zinc Phthalocyanine studied by Density Functional Methods*, `Journal of Physical Chemistry A 105, 5242 (2001) <https://doi.org/10.1021/jp0042361>`__ 

.. [#ref49] S.J.A. van Gisbergen, J.A. Groeneveld, A. Rosa, J.G. Snijders and E.J.Baerends, *Excitation energies for transition metal compounds from time-dependent density functional theory. Applications to* MnO4\ :sup:`-` , Ni(CO)\ :sub:`4` and Mn\ :sup:`2` (CO)\ :sub:`10`, `Journal of Physical Chemistry A 103, 6835 (1999) <https://doi.org/10.1021/jp991060y>`__ 

.. [#ref50] A.\  Rosa, E.J. Baerends, S.J.A. van Gisbergen, E. van Lenthe, J.A. Groeneveld and J. G. Snijders, *Article Electronic Spectra of* M(CO)\ :sub:`6` (M = Cr, Mo, W) *Revisited by a Relativistic TDDFT Approach*, `Journal of the American Chemical Society 121, 10356 (1999) <https://doi.org/10.1021/ja990747t>`__ 

.. [#ref51] M.\  Seth and T. Ziegler, *Formulation of magnetically perturbed time-dependent density functional theory*, `Journal of Chemical Physics 127, 134108 (2007) <https://doi.org/10.1063/1.2772849>`__ 

.. [#ref52] M.\  Seth, M. Krykunov, T. Ziegler, J. Autschbach and A. Banerjee, *Application of magnetically perturbed time-dependent density functional theory to magnetic circular dichroism: Calculation of B terms*, `Journal of Chemical Physics 128, 144105 (2008) <https://doi.org/10.1063/1.2901967>`__ 

.. [#ref53] M.\  Seth, M. Krykunov, T. Ziegler and J. Autschbach, *Application of magnetically perturbed time-dependent density functional theory to magnetic circular dichroism. II. Calculation of A terms*, `Journal of Chemical Physics 128, 234102 (2008) <https://doi.org/10.1063/1.2933550>`__ 

.. [#ref54] F.\  Plasser, and H. Lischka, *Analysis of Excitonic and Charge Transfer Interactions from Quantum Chemical Calculations*, `Journal of Chemical Theory and Computation 8, 2777 (2012) <https://doi.org/10.1021/ct300307c>`__

.. [#ref55] F.\  Plasser, M. Wormit, and A. Dreuw, *New tools for the systematic analysis and visualization of electronic excitations. I. Formalism*, `Journal of Chemical Physics 141, 024106 (2008) <https://doi.org/10.1063/1.4885819>`__

.. [#ref56] F.\  Plasser, S.A. Bäppler, Wormit, and A. Dreuw, *New tools for the systematic analysis and visualization of electronic excitations. II. Applications*, `Journal of Chemical Physics 141, 024107 (2008) <https://doi.org/10.1063/1.4885820>`__

.. [#ref57] S.A. Mewes, J.-M. Mewes, A. Dreuw, and F. Plasser, *Excitons in poly(para phenylene vinylene): a quantum-chemical perspective based on high-level ab initio calculations*, `Physical Chemistry Chemical Physics 18, 2548 (2016) <https://doi.org/10.1039/c5cp07077e>`__.

.. [#ref58] M.\  Medves, L. Sementa, D. Toffoli, G. Fronzoni, A. Fortunelli, *An efficient hybrid scheme for time dependent density functional theory*, `Journal of Chemical Physics 152, 184104 (2020) <https://doi.org/10.1063/5.0005954>`__ 

.. [#ref59] F.\  Furche, R. Ahlrichs, *Adiabatic time-dependent density functional methods for excited state properties*, `Journal of Chemical Physics 117, 7433 (20002) <https://doi.org/10.1063/1.1508368>`__ 

.. [#ref60] P.\  Grobas-Illobre, M. Marsili, S. Corni, M. Stener, D. Toffoli, and E. Coccia, `Journal of Chemical Theory and Computation XXXX, XXX (2021) <https://doi.org/10.1021/acs.jctc.1c00211>`__

