.. _POLARIZABILITIES: 


(Hyper-)Polarizabilities, ORD, magnetizabilities, Verdet constants
******************************************************************

A (frequency dependent) electric field induces a dipole moment in a molecule, which is proportional to the (frequency dependent) molecular polarizability. Van der Waals dispersion coefficients describe the long-range dispersion interaction between two molecules. Optical rotation or optical activity (ORD) is the rotation of linearly polarized light as it travels through certain materials. A (frequency dependent) magnetic field induces a magnetic moment in a molecule, which is proportional to the (frequency dependent) molecular magnetizability. The Faraday effects describes the rotation of the plane-polarized light due to a magnetic field, which is proportional to the intensity of the component of the magnetic field in the direction of the beam of light. The Verdet constant describes the strength of the Faraday effect for a particular molecule.  All these properties are available in ADF as applications of time-dependent DFT (TDDFT). 

Two keys can be used for calculating these properties:

+ RESPONSE 
+ AORESPONSE

The RESPONSE key has many unique features compared to the AORESPONSE key, like the use of symmetry during the calculation.
The AORESPONSE key also has many unique features compared to the RESPONSE key, namely lifetime effects (polarizabilities at resonance), the calculation of (dynamic) magnetizabilities, Verdet constants, the Faraday B terms, and an alternative way to calculate (resonance) Raman scattering factors.
Both RESPONSE and AORESPONSE can calculate polarizabilities in case of spin-orbit coupling.

.. index:: polarizability 
.. _response: 


RESPONSE: (Hyper-)Polarizabilities, ORD
=======================================

RESPONSE: Polarizabilities
------------------------------

The calculation of frequency-dependent (hyper)polarizabilities and related properties (Raman, ORD) is activated with the block key RESPONSE 

::

  RESPONSE
  END

In this example only the *zz* component of the dipole polarizability tensor is calculated, at zero frequency. The orientation of the molecule is therefore crucial. Be aware that the program may modify the orientation of the molecule if the input coordinates do not agree with the symmetry conventions in ADF! (This calculation could equivalently be done through a finite field method). 

See also the alternative implementation with the AORESPONSE key that offers some unique features like magnetizability, and lifetime options. 

The impact of various approximations on the quality of computed polarizabilities has been studied in, for instance, Refs. [#ref1]_ [#ref2]_ [#ref3]_. If you are new to this application field, we strongly recommend that you study a few general references first, in particular when you consider hyperpolarizability calculations. These have many pitfalls, technically (which basis sets to use, application of the DEPENDENCY key) and theoretically (how do theoretical tensor components relate to experimental quantities, different conventions used). Please, take a good look both at ADF-specific references [#ref34]_ [#ref35]_ [#ref6]_ [#ref4]_ and at general references related to this subject: Refs. [#ref5]_ [#ref36]_ [#ref37]_, the entire issues of Chem.Rev.94, the ACS Symposium Series #628, and further references in the ADF-specific references. 

.. _keyscheme RESPONSE: 

::

  RESPONSE
    ALLCOMPONENTS
    Frequencies freq1 freq2 ... freqN [unit]
    ALLTENSOR
    Quadrupole
    Octupole
    Traceless
  END

``Entire tensor or only one component``
  You specify the ALLCOMPONENTS subkey to get the entire polarizability tensor, instead of just the *zz* component. 

``Frequencies``
  List of frequencies at which the polarizability is to be calculated. Default unit eV. A range of frequencies with equidistant points can be specified with the boundaries (inclusive) as well as the number of desired subintervals separated by colons. For example, 1.0:1.5:5 is equivalent to 1.0 1.1 1.2 1.3 1.4 1.5.

``Higher multipole polarizabilities``
  Instead of just calculating the dipole-dipole polarizability, one may address the dipole-quadrupole, quadrupole-quadrupole, dipole-octupole, quadrupole-octupole, and octupole-octupole polarizability tensors. These can all be calculated in a single run, using the subkey ALLTENSOR. If only quadrupole-quadrupole or octupole-octupole tensors are needed, the subkey quadrupole or octupole should be used. 


``Traceless``
  If the subkey TRACELESS is included this ensures the calculation of tensors using the traceless form of the quadrupole operator.

RESPONSE: Accuracy and convergence
----------------------------------

::

  RESPONSE
    erralf 1e-6
    erabsx 1e-6
    errtmx 1e-6
    ncycmx 30
  END

``erralf, erabsx, errtmx``
  The subkeys erralf, erabsx, errtmx determine the convergence criteria for a polarizability calculation. The strict defaults are shown. It is rarely necessary to change the defaults, as these are rather strict but do not lead to many iterations. 

``ncycmx``
  The maximum number of attempts within which the algorithm has to converge. The default appears to be adequate in most cases. 

.. _HYPERPOL: 
.. index:: hyperpolarizability 
.. _keyscheme HYPERPOL: 

RESPONSE: Hyperpolarizabilities
-------------------------------

``Hyperpolarizabilities``


::

  RESPONSE
    HYPERPOL LaserFreq
  END

The first hyperpolarizability tensor :math:`\beta` is calculated (in atomic units in the 'theoreticians convention', i.e. convention T=AB in Ref. [#ref5]_) if the subkey HYPERPOL is present with a specification of the laser frequency (in Hartree units). If also the subkey ALLCOMPONENTS is specified, all components of the hyperpolarizability tensor will be obtained. 

As mentioned before, by default only the static dipole hyperpolarizability tensor is computed. If one is interested in the frequency-dependent hyperpolarizability, the input could look like: 

::

  RESPONSE
    ALLCOMPONENTS
    HYPERPOL 0.01
    DYNAHYP
  END

The subkey DYNAHYP has to be added and the main frequency :math:`\omega` has to be specified in Hartrees after the subkey hyperpol. In the output all nonzero components of the tensors governing the static first hyperpolarizability, second harmonic generation, electro-optic Pockels effect, and optical rectification are printed.  

**Note**: Second hyperpolarizabilities are currently not available analytically in case of RESPONSE. Some can however be obtained by calculating the first hyperpolarizability in a finite field.

The effect of using different DFT functionals (LDA, LB94, BLYP) on hyperpolarizabilities in small molecules has been investigated in [#ref6]_. 


RESPONSE: Optical rotation dispersion (ORD)
-------------------------------------------

::

  RESPONSE
    OPTICALROTATION
  END

.. _ORD: 
.. index:: ORD 
.. index:: optical rotation (dispersion) 
.. _keyscheme OPTICALROTATION: 

``OPTICALROTATION``
  With the subkey OPTICALROTATION the (frequency dependent) optical rotation [#ref7]_ [#ref8]_ will be calculated. For correct calculations one should calculate the entire tensor (see also the subkey ALLCOMPONENTS), which is done automatically. 

An alternative implementation uses the AORESPONSE key, in which life time effects can be included. 


.. index:: lifetime effects 
.. index:: magnetizability 
.. index:: polarizability
.. index:: polarizability at resonance 
.. index:: ORD
.. index:: optical rotation (dispersion)
.. _AORESPONSE: 
.. _MAGNETIZABILITY: 
.. _LIFETIMEEFFECTS: 


AORESPONSE: Lifetime effects, (Hyper-)polarizabilities, ORD, magnetizabilities, Verdet constants
================================================================================================

The AORESPONSE key offers some unique features compared to the RESPONSE key, namely lifetime effects (polarizabilities at resonance), the calculation of (dynamic) magnetizabilities, Verdet constants, the Faraday B terms, and an alternative way to calculate (resonance) Raman scattering factors. Note that the RESPONSE key also has many unique features, like the use of symmetry during the calculation. 


AORESPONSE: Polarizabilities
--------------------------------

If the block key AORESPONSE is used, by default, the polarizability is calculated.

.. _keyscheme AORESPONSE: 

::

  AORESPONSE
    Frequencies freq1 freq2 ... freqN
    LIFETIME width
  END

``Frequencies``
  List of frequencies at which the time-dependent properties are to be calculated. Default unit eV. A range of frequencies with equidistant points can be specified with the boundaries (inclusive) as well as the number of desired subintervals separated by colons. For example, 1.0:1.5:5 is equivalent to 1.0 1.1 1.2 1.3 1.4 1.5. 

``LIFETIME width``
  Specify the resonance peak width (damping) in Hartree units. Typically the lifetime of the excited states is approximated with a common phenomenological damping parameter. Values are best obtained by fitting absorption data for the molecule, however, the values do not vary a lot between similar molecules, so it is not hard to estimate values.  A value of 0.004 Hartree was used in Ref. [#ref9]_. 

.. index:: spin-orbit polarizability 

The spin-orbit ZORA polarizability code (Ref. [#ref11]_) is automatically selected if the AORESPONSE keyword is given in a spin-orbit coupled calculation. In this case a spin-restricted calculation is required, but, unlike the rest of AORESPONSE, also SYMMETRY NOSYM. Spin-polarization terms in the XC response kernel are neglected. In Ref. [#ref11]_ the imaginary polarizability dispersion curves (spin-restricted) match well the broadened spin-orbit TDDFT data from Ref. [#ref10]_. Thus the corrections from the spin-polarization terms appear to be rather minor. No picture change corrections were applied in the ZORA formalism. AORESPONSE icw hybrids icw spin-orbit is not implemented.


AORESPONSE: Technical parameters and expert options
---------------------------------------------------

::

  AORESPONSE
   ...
    SCF        {NOCYC} {NOACCEL} {CONV=conv} {ITER=niter}
    GIAO
    FITAODERIV
    COMPONENTS {XX} {XY} {XZ} {YX} {YY} {YZ} {ZX} {ZY} {ZZ}
    ALDA|XALPHA
    ALPHA
  END

``SCF {NOCYC} {NOACCEL} {CONV=conv} {ITER=niter}``
  Specify CPKS parameters such as the degree of convergence and the maximum number of iterations: 

  NOCYC - disable self-consistence altogether 

  NOACCEL - disable convergence acceleration 

  CONV - convergence criterion for CPKS. The default value is 10\ :sup:`-6` .  The value is relative to the uncoupled result (i.e. to the value without self-consistence). 

  ITER - maximum number of CPKS iterations, 50 by default.  

  Specifying ITER=0 has the same effect as specifying NOCYC. 

``GIAO``
  Include the Gauge-Independent Atomic Orbitals (GIAO). This option should not be used with damping (LIFETIME keyword) and the VELOCITYORD option should be used instead. 

``FITAODERIV``
  Use fitted AO Derivatives. This will improve the density fitting, can only be used in cae of STO fitting. In case of ZlmFit one can improve the fitting with the ZLMFIT block key. 

``COMPONENTS {XX} {XY} {XZ} {YX} {YY} {YZ} {ZX} {ZY} {ZZ}``
  Limit the tensor components to the specified ones. Using this option may save the computation time. 

``ALDA|XALPHA``
  If ALDA is specified the VWN kernel is used. This option is the default. If ALPHA is specified the X\ :math:`\alpha` kernel is used instead of the default VWN one. For functionals that use LYP correlation, like BLYP, always the X\ :math:`\alpha` kernel is used, even if one specified ALDA.

``ALPHA``
  Writes perturbed density matrix to TAPE16.

.. _Damped First Hyperpolarizability: 

AORESPONSE: Damped First Hyperpolarizabilities
----------------------------------------------

In Ref. [#ref12]_ an implementation of finite lifetimes into TDDFT for the calculation of quadratic response properties in ADF is described.
All :math:`\beta` tensor components (27 in total) will be printed in the output.

::

  AORESPONSE
    BETA|QUADRATIC
    Frequencies  freq1 freq2
    LIFETIME width
    STATIC|OPTICALR|EOPE|SHG
  END

``BETA``
   Option to calculate the damped first hyperpolarizability (:math:`\beta`) using quadratic response theory based on the 2n+1 rule. Two input frequencies are required for this calculation and the property :math:`\beta (-(\omega_1+\omega_2); \omega_1, \omega_2)` will be the output. Note that one can choose certain values of the two frequencies to calculate different types of :math:`\beta`, such as static case :math:`\beta(0;0,0)`, optical rectification :math:`\beta(0;\omega,-\omega)`, electro-optical Pockels effect :math:`\beta(-\omega;\omega,0)`, and second harmonic generation :math:`\beta(-2\omega;\omega,\omega)`. Alternatively, these can be efficiently calculated using the (sub-)keywords STATIC, OPTICALR, EOPE, and SHG, respectively. Note that the needed input frequencies all rely on :math:`\omega_1` (freq1) when using the (sub)keywords above.

``QUADRATIC``
   This option possess the same functionality as BETA, i.e., calculate the damped :math:`\beta`, except not adapting the 2n+1 rule. The (sub)keywords STATIC, OPTICALR, EOPE,and SHG are also applicable here. Note that this approach facilitates the direct partitioning of the response into contributions from localized orbitals and is important for natural bond analysis.

Note: Please only use HARTREE or EV as the unit for the input frequencies. The unit option ANGSTROM does not work correctly due to the current implementation structure.

.. _Damped Second Hyperpolarizability: 

AORESPONSE: Damped Second Hyperpolarizabilities
-----------------------------------------------

In Ref. [#ref13]_ a general implementation for damped cubic response properties is presented using time-dependent density functional theory (TDDFT) and Slater-type orbital basis sets.
To directly calculate two-photon absorption (TPA) cross sections, an implementation of a reduced damped cubic response approach is described in Ref. [#ref13]_.
All :math:`\gamma` tensor components (81 in total) will be printed in the output.

::

  AORESPONSE
    GAMMA|CUBIC
    Frequencies  freq1 freq2 freq3
    LIFETIME width
    STATIC|EFIOR|OKE|IDRI|EFISHG|THG|TPA
  END

``GAMMA``
   Option to calculate the damped second hyperpolarizability (:math:`\gamma`) using cubic response theory based on the 2n+1 rule. Three input frequencies are required for this calculation and the property  :math:`\gamma(-(\omega_1+\omega_2+\omega_3); \omega_1, \omega_2, \omega_3)` will be the output. Note that one can choose certain values of the three frequencies to calculate different types of :math:`\gamma`, such as static case :math:`\gamma(0;0,0,0)`, electric field induced optical rectification :math:`\gamma(0;\omega,-\omega,0)`, optical Kerr effect :math:`\gamma(-\omega;\omega,0,0)`, intensity dependent refractive index :math:`\gamma(-\omega;\omega,\omega,-\omega)`, electric field induced second harmonic generation :math:`\gamma(-2 \omega;\omega,\omega,0)`, and third harmonic generation :math:`\gamma(-3 \omega;\omega,\omega,\omega)`. Alternatively, these can be efficiently calculated using the (sub)keywords STATIC, EFIOR, OKE, IDRI, EFISHG, and THG, respectively. The (sub)keyword TPA can be used to calculate the :math:`\gamma` corresponding to the two photon absorption process (i.e., the reduced form of :math:`\gamma(-\omega;\omega,\omega,-\omega)`), however, it can ONLY be used with keyword GAMMA. Note that the needed input frequencies all rely on :math:`\omega_1` (freq1) when using the (sub)keywords above.

``CUBIC``
   This option possess the same functionality as GAMMA, i.e., calculate the damped :math:`\gamma`, except not adapting the 2n+1 rule. The (sub)keywords STATIC, EFIOR, OKE, IDRI, EFISHG and THG are also applicable here. Note that this approach facilitates the direct partitioning of the response into contributions from localized orbitals and is important for natural bond analysis.

Note: Please only use HARTREE or EV as the unit for the input frequencies. The unit option ANGSTROM does not work correctly due to the current implementation structure.

AORESPONSE: ORD
---------------

::

  AORESPONSE
    OPTICALROTATION
    VELOCITYORD
    Frequencies freq1 freq2 ... freqN
    LIFETIME width
  END

``OPTICALROTION``
  Specify OPTICALROTION to calculate optical rotatory dispersion spectrum instead of polarizabilities. 

``VELOCITYORD``
  This option should be used instead of OPTICALROT with GIAO if the finite lifetime effects need to be taken into account (LIFETIME option). 


AORESPONSE: magnetizabilities, Verdet constants, Faraday B term
---------------------------------------------------------------

.. index:: Verdet constant 
.. index:: Faraday B term 

::

  AORESPONSE
    MAGNETICPERT
    MAGOPTROT
    FREQUENCIES freq1 freq2 ... freqN [unit]
    LIFETIME width
  END

``MAGNETICPERT``
  Calculate static or time-dependent magnetizability, see also Ref. [#ref15]_. 

``MAGOPTROT``
  Specify MAGOPTROT to calculate the Verdet constant instead of polarizability, see for the details of the implementation Ref. [#ref17]_. When it is specified together with the LIFETIME key the real and imaginary part of the damped Verdet constant  will be calculated. Combination of three keys MAGOPTROT, LIFETIME and FREQUENCIES yields  the magnetic optical rotatory dispersion and magnetic circular dichroism spectrum (Faraday A and B terms) calculated simultaneously in the range from freq1 to freqN. It is also possible to combine MAGOPTROT, LIFETIME and FREQUENCY. In order to obtain the Faraday B terms from the Verdet constant calculations it is necessary to perform several steps, involving a fit of the imaginary Verdet data to the MCD spectrum. You can request SCM for details on the fitting procedure. For details of the method, see  Ref. [#ref16]_. 

AORESPONSE: Raman
-----------------

::

  AORESPONSE
    RAMAN
    Frequencies  freq1 [unit]
    LIFETIME width
  END

``RAMAN``
  Calculates the Raman scattering factors. The AORESPONSE-Raman only works with one frequency. If one frequency is specified the Raman scattering factors are calculated at that frequency. The Raman option is compatible with the lifetime option so that resonance Raman scattering can be calculated. For details of this method, see  Ref. [#ref9]_. To get Raman intensities with AORESPONSE, numerical frequencies need to be calculated  using a FREQUENCIES key in the GEOMETRY input block. Non-resonance Raman intensities can  also be obtained using the RESPONSE key or, alternatively, using RAMANRANGE in combination with  analytically or numerically pre-calculated frequencies. 

Applications of AORESPONSE
--------------------------

It may be useful to consult the following applications of the AORESPONSE key in ADF: 

+ Calculation of static and dynamic linear magnetic response in approximate time-dependent density functional theory [#ref15]_

+ Calculation of CD spectra from optical rotatory dispersion, and vice versa, as complementary tools for theoretical studies of optical activity using time-dependent density functional theory [#ref20]_

+ Calculation of origin independent optical rotation tensor components for chiral oriented systems in approximate time-dependent density functional theory [#ref21]_

+  Time-dependent density functional calculations of optical rotatory dispersion including resonance wavelengths as a potentially useful tool for determining absolute configurations of chiral molecules [#ref22]_

+ Calculation of optical rotation with time-periodic magnetic field-dependent basis functions in approximate time-dependent density functional theory [#ref23]_

+  A Quantum Chemical Approach to the Design of Chiral Negative Index Materials [#ref24]_

+ Calculation of Verdet constants with time-dependent density functional theory. Implementation and results for small molecules [#ref17]_

+ Calculations of resonance Raman [#ref9]_ [#ref38]_

+ Calculations of surface-enhanced Raman scattering (SERS) [#ref39]_ [#ref40]_

+ Calculation of magnetic circular dichroism spectra from damped Verdet constants  [#ref16]_

+ Calculation of the polarizability in case of spin-orbit coupling [#ref11]_

.. seealso::

   - `advanced tutorial on plasmon enhanced two photon absorption <../../Tutorials/OpticalPropertiesElectronicExcitations/PlasmonEnhancedTwoPhotonAbsorption.html>`__

.. _POLTDDFT: 

POLTDDFT: Damped Complex Polarizabilities
=========================================

A fast algorithm to solve the Time Dependent Density Functional Theory (TDDFT) equations in the space of the density fitting auxiliary basis set has been developed and implemented [#ref28]_.
The method, named POLTDDFT, extracts the spectrum from the imaginary part of the polarizability at any given photon energy, avoiding the bottleneck of Davidson diagonalization.
The original idea which made the present scheme very efficient consists in the simplification of the double sum over occupied-virtual pairs in the definition of the complex dynamical polarizability, allowing an easy calculation of such matrix as a linear combination of constant matrices with photon energy dependent coefficients. 
The method has been extended for the calculation of circular dichroism spectra [#ref29]_.

In case a (meta-)hybrid is used in the SCF, the hybrid diagonal approximation (HDA) [#ref41]_ is used.
HDA is based on utilizing the hybrid exchange only for the diagonal terms in the response equations.
This allows one to limit the computational cost of the TD-DFT simulation while keeping basically the same accuracy as in the full TD-DFT scheme using hybrid xc-functionals.

It is very important to use specially made auxiliary fit sets, which are available only for a very limited amount of elements.
Symmetry and frozen cores can be used.
Should not be used for range-separated functionals.
Should not be used icw spin-orbit coupling.
STOFIT can not be used.


.. _keyscheme POLTDDFT: 

UV/Vis spectra, CD spectra
--------------------------

If one includes the POLTDDFT keyword the (real and imaginary part of the) diagonal of the polarizability tensor and rotatory strengths will be calculated, which can be used to calculate the photoabsorption and circular dichroism (CD) spectra.

::

   POLTDDFT
     IRREP
        Irrep1
        Irrep2
        ...
     SUBEND
     KGRID eVgrid
     NGRID ngrid
     FREQRANGE eVi eVf
     NFREQ nfreq
     LIFETIME eVwidth
     CUTOFF eVcutoff
     LAMBDA lambda
     VELOCITY
   END

``IRREP``
  Subblock key for selecting which symmetry irreps of the excitations to calculate (all excitations by default). In the subkey data block list the symmetry irrep labels, like B1, for example. 

``KGRID eVgrid``
  Keyword KGRID is used to discretize the energy scale for calculating the complex dynamical polarizability. Only pairs of an occupied and virtual orbital are included, for which the orbital energy difference is lower than eVgrid (9 eV by default).

``NGRID ngrid``
  Ngrid is the number of points within the energy grid (180 by default).

``FREQRANGE eVi eVf``
  Keyword FREQRANGE is used to specify the equally spaced points in the spectrum for which one would like to calculate the complex dynamical polarizability. The first point is eVi (0 eV by default) and the last one is eVf (5 eV by default).

``NFREQ nfreq``
  The total number of points in the spectrum is nfreq (100 by default).

``LIFETIME eVwidth``
  Specify the resonance peak width (damping) in eV units. Typically the lifetime of the excited states is approximated with a common phenomenological damping parameter. Values are best obtained by fitting absorption data for the molecule, however, the values do not vary a lot between similar molecules, so it is not hard to estimate values. Default value is 0.1 eV.

``CUTOFF eVcutoff``
   For a given point in the spectrum, only include pairs of an occupied and virtual orbital, for which the orbital energy difference is lower than the energy of the point in the spectrum plus eVcutoff. The default value for eVcutoff is 4 eV.

``LAMBDA lambda``
   Jacob's scaling factor [#ref30]_ for the study of plasmonic resonances. This factor, 0<lambda<1 (default lambda=1), turns on the coupling matrix K.

``VELOCITY``
   If the subkey VELOCITY is included ADF calculates the dipole moment in velocity gauge. Default the dipole-length representation is used.


Reduced fit set
---------------

For POLTDDFT it very important is to use specially made auxiliary fit sets. These are available for most elements, except lanthanides and actinides, using a large frozen core.
These special basis sets can be found in the atomic database directories, with a directory name POLTDDFT,
for example, the directory $AMSHOME/atomicdata/ADF/POLTDDFT/TZP. They require relativistic ZORA to be used, since the frozen core description is relativistic ZORA.
An example:

::

   Basis
     Type POLTDDFT/DZ
     PerAtomType Symbol=Au File=POLTDDFT/TZP/Au.4f
   End

.. csv-table:: Available basis sets in POLTDDFT (May 2021)
   :header: "Element",  "ae or fc", "DZ", "DZP", "TZP"

   H-He (Z=1-2)    , ae      , Yes ,  Yes  ,  Yes
   Li-Ne (Z=3-10)  ,.1s      , Yes ,  Yes  ,  Yes
   Na-Ar (Z=11-18) ,.2p      , Yes ,  Yes  ,  Yes
   K-Ca (Z=19-20)  ,.3p      , Yes ,  Yes  ,  Yes
   Sc-Zn (Z=21-30) ,.3p      , Yes ,       ,  Yes
   Ga-Kr (Z=31-36) ,.3d      , Yes ,  Yes  ,  Yes
   Rb-Cd (Z=37-48) ,.4p      , Yes ,       ,  Yes
   In-Ba (Z=49-56) ,.4d      , Yes ,       ,  Yes
   Hf-Hg (Z=72-80) ,.4f      , Yes ,       ,  Yes
   Tl    (Z=81)    ,.5p      , Yes ,       ,  Yes
   Pb-Ra (Z=82-88) ,.5d      , Yes ,       ,  Yes

.. _keyscheme VANDERWAALS: 

Van der Waals dispersion coefficients
=====================================

::

  RESPONSE
    ALLCOMPONENTS
    VANDERWAALS NVanderWaals
    {ALLTENSOR}
  END

.. _C6DISPERSION: 

.. index:: dispersion coefficients 

.. index:: van der Waals

``Dispersion coefficients``
  Simple dispersion coefficients (the dipole-dipole interaction between two identical molecules, the C\ :sub:`6`  coefficient) are calculated in a single ADF calculation. General dispersion coefficients are obtained with the auxiliary program DISPER, which uses two output files (file named TENSOR) of two separate ADF runs as input. See the Properties and the Examples documents. To get the dispersion coefficients one has to calculate polarizabilities at imaginary frequencies between 0 and infinity. The ADF program chooses the frequencies itself. The user has to specify the number of frequencies, which in a sense defines the level of accuracy, as an argument to the subkey VanDerWaals. 

``NVanderWaals``
  One can specify the number of frequencies with NVanderWaals. Ten frequencies is reasonable. Without the key ALLTENSOR only dipole-dipole interactions are considered. If ALLTENSOR is specified, higher dispersion coefficients are also calculated. This ADF calculation generates a file with name TENSOR, which contains the results of multipole polarizabilities at imaginary frequencies. This TENSOR file has to be saved. Similarly, the TENSOR file for the second monomer has to be saved. The files have to be renamed to files 'tensorA' and 'tensorB' (case sensitive) respectively. Then the program DISPER has to be called in the same directory where the 'tensorA' and 'tensorB' files are located. DISPER needs no further input. 

.. _DISPER: 

DISPER program: Dispersion Coefficients
---------------------------------------

The DISPER program was originally written by V.Osinga [#ref31]_. The original documentation was written by S.J.A. van Gisbergen. 

**Van der Waals dispersion coefficients**

.. index:: C8 coefficient 

.. index:: C10 coefficient 

.. index:: long range dispersion interaction 

.. index:: van der Waals 

The program DISPER computes Van der Waals dispersion coefficients up to C\ :sub:`10`  for two arbitrary closed-shell molecules. ADF itself can already compute some C\ :sub:`6`  and C\ :sub:`8`  coefficients between two identical closed-shell molecules. These coefficients describe the long-range dispersion interaction between two molecules. It requires previous ADF-TDDFT calculations for the polarizability tensors at imaginary frequencies for the two interacting molecules. Each such ADF calculation produces a file TENSOR (if suitable input for ADF is given). The TENSOR files must be renamed tensorA and tensorB, respectively and must be present as local files for DISPER. The DISPER program takes no other input and prints a list of dispersion coefficients. 

A schematic example, taken from the set of sample runs, for the usage of DISPER is the following: 

Step1: run ADF for, say, the HF molecule. In the input file you specify the RESPONSE data block: 

::

  RESPONSE
    MaxWaals 8    ! Compute dispersion coefficients up to C8
    ALLTENSOR     ! This option must be specified in the ADF calc for a
                  ! subsequent DISPER run
    ALLCOMPONENTS ! Must also be specified for DISPER
  End

At the end of the run, copy the local file 'TENSOR' to a file 'tensorA'. For simplicity, we will now compute the dispersion coefficients between two HF molecules. Therefore, copy 'tensorA' to 'tensorB'. 

Now run DISPER (without any other input). It will look for the local files 'tensorA' and 'tensorB' and compute corresponding dispersion coefficients to print them on standard output. 

.. _keyscheme disper: 


::

  $AMSBIN/disper -n1 << eor
  eor

The output might look something like this: 

::

  DISPER 2000.02 RunTime: Apr04-2001 14:14:13
    C-COEFFICIENTS 
    n   LA  KA  LB  KB  L  coefficient(Y)    coefficient(P)
    6   0   0   0   0   0   28.29432373         28.29432373
    6   2   0   0   0   2    7.487547697         3.348533127
    8   0   0   0   0   0  416.1888455         416.1888455
    8   0   0   2   0   2    0.4323024202E-05    0.1933315197E-05
    8   2   0   0   0   2  402.3556946         179.9389368
    8   2   0   2   0   4    0.4238960180E-05
    8   4   0   0   0   4  -36.67895539        -12.22631846
    8   4   0   2   0   6   -0.2000286301E-05

The n-value in the first column refers to the long-range radial interaction. The case n=6 refers to the usual dipole-dipole type interaction related to a 1/R\ :sup:`6` dependence in the dispersion energy. The n=7 case relates to a dipole-quadrupole polarizability on one system and a dipole-dipole polarizability on the other (this is not symmetric!). The n=8 term may contain contributions from a quadrupole-quadrupole polarizability on one system in combination with a dipole-dipole polarizability on the other as well as contributions from two dipole-quadrupole polarizabilities. 

Terms which are zero by symmetry are not printed. In the example above, this is the case for all n=7 terms, because the systems (apparently) are too symmetric to have a nonzero dipole-quadrupole polarizability. The best known and most important coefficients are the isotropic ones, determining the purely radial dependence of the dispersion energy. They are characterized by the quantum numbers: 6 0 0 0 0 0 (or 8 0 0 0 0 0 etc.) Other combinations of quantum numbers refer to different types of angular dependence. The complete set determines the dispersion energy for arbitrary orientations between the two subsystems A and B.  

The complete expressions are rather involved and lengthy. We refer the interested reader to the paper [#ref31]_ which contains a complete description of the meaning of the various parts of the output, as well as references to the earlier literature which contain the mathematical derivations. In particular, a useful review, which was at the basis of the ADF implementation, is given in [#ref33]_. Of particular significance is Eq.(8) of the JCP paper mentioned above, as it defines the meaning of the calculated coefficients :math:`C_n^{L_A, K_A, L_B, K_B, L}` as printed above.  

For highly symmetric systems, a different convention is sometimes employed. It is based on Legendre polynomials (hence the 'P' in the final column) instead of on the spherical harmonics (the 'Y' in the column before the last). The 'P' coefficients are defined only for those coefficients that are nonzero in highly symmetric systems and never contain additional information with respect to the 'Y' coefficients. They are defined [Eq. (14) in the mentioned J. Chem. Phys. paper] in terms of the 'Y' coefficients by: 


.. math::

  C_n^L = (-1)^L C_n^{L,0,0,0,L} / \sqrt{2L+1}


Because the quality of the dispersion coefficients is determined by the quality of the polarizabilities that are the input for DISPER, it is important to get good polarizabilities from ADF. For that it is important, in the case of small systems, to use an asymptotically correct XC potential (several choices are available in ADF, such as SAOP or GRAC) and a basis set containing diffuse functions. We refer to the ADF User's Guide for details. 


.. only:: html

  .. rubric:: References

.. [#ref1] S.J.A. van Gisbergen, V.P. Osinga, O.V. Gritsenko, R. van Leeuwen, J.G. Snijders and E.J. Baerends, *Improved density functional theory results for frequency-dependent polarizabilities, by the use of an exchange-correlation potential with correct asymptotic behavior*, `Journal of Chemical Physics 105, 3142 (1996) <https://doi.org/10.1063/1.472182>`__ 

.. [#ref2] S.J.A. van Gisbergen, F. Kootstra, P.R.T. Schipper, O.V. Gritsenko, J.G. Snijders and E.J. Baerends, *Density-functional-theory response-property calculations with accurate exchange-correlation potentials*, `Physical Review A 57, 2556 (1998) <https://doi.org/10.1103/PhysRevA.57.2556>`__ 

.. [#ref3] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *A Density Functional Theory study of frequency-dependent polarizabilities and van der Waals dispersion coefficients for polyatomic molecules*, `Journal of Chemical Physics 103, 9347 (1995) <https://doi.org/10.1063/1.469994>`__ 

.. [#ref4] B.\  Champagne, E.A. Perpète, S.J.A. van Gisbergen, E.J. Baerends, J.G. Snijders, C. Soubra-Ghaoui, K.A. Robins and B.Kirtman, *Assessment of conventional density functional schemes for computing the polarizabilities and hyperpolarizabilities of conjugated oligomers: An ab initio investigation of polyacetylene chains*, `Journal of Chemical Physics 109, 10489 (1998) <https://doi.org/10.1063/1.477731>`__ Erratum: `Journal of Chemical Physics 111, 6652 (1999) <https://doi.org/10.1063/1.479106>`__ 

.. [#ref5] A.\  Willets, J.E. Rice, D.M. Burland and D.P. Shelton, *Problems in comparison of experimental and theoretical hyperpolarizabilities*, `Journal of Chemical Physics 97, 7590 (1992) <https://doi.org/10.1063/1.463479>`__ 

.. [#ref6] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Accurate density functional calculations on frequency-dependent hyperpolarizabilities of small molecules*, `Journal of Chemical Physics 109, 10657 (1998) <https://doi.org/10.1063/1.477763>`__ 

.. [#ref7] J.\  Autschbach and T. Ziegler, *Calculating molecular electric and magnetic properties from time-dependent density functional response theory*, `Journal of Chemical Physics 116, 891 (2002) <https://doi.org/10.1063/1.1420401>`__ 

.. [#ref8] J.\  Autschbach, S. Patchkovskii, T. Ziegler, S.J.A. van Gisbergen and E.J. Baerends, *Chiroptical properties from time-dependent density functional theory. II. Optical rotations of small to medium sized organic molecules*, `Journal of Chemical Physics 117, 581 (2002) <https://doi.org/10.1063/1.1477925>`__ 

.. [#ref9] L.\  Jensen, L. Zhao, J. Autschbach and G.C. Schatz, *Theory and method for calculating resonance Raman scattering from resonance polarizability derivatives*, `Journal of Chemical Physics 123, 174110 (2005) <https://doi.org/10.1063/1.2046670>`__ 

.. [#ref10] F.\  Wang, T. Ziegler, E. van Lenthe, S.J.A. van Gisbergen and E.J. Baerends, *The calculation of excitation energies based on the relativistic two-component zeroth-order regular approximation and time-dependent density-functional with full use of symmetry*, `Journal of Chemical Physics 122, 204103 (2005) <https://doi.org/10.1063/1.1899143>`__ 

.. [#ref11] A.\  Devarajan, A. Gaenko, and J. Autschbach, *Two-component relativistic density functional method for computing nonsingular complex linear response of molecules based on the zeroth order regular approximation*, `Journal of Chemical Physics 130, 194102 (2009) <https://doi.org/10.1063/1.3123765>`__ 

.. [#ref12] Z.\  Hu, J. Autschbach, and L. Jensen, *Simulation of resonance hyper-Rayleigh scattering of molecules and metal clusters using a time-dependent density functional theory approach*, `Journal of Chemical Physics 141, 124305 (2014) <https://doi.org/10.1063/1.4895971>`__

.. [#ref13] Z.\  Hu, J. Autschbach, and L. Jensen, *Simulating Third-Order Nonlinear Optical Properties Using Damped Cubic Response Theory within Time-Dependent Density Functional Theory*, `Journal of Chemical Theory and Computation 12, 1294 (2016) <https://doi.org/10.1021/acs.jctc.5b01060>`__

.. [#ref15] M.\  Krykunov and J. Autschbach, *Calculation of static and dynamic linear magnetic response in approximate time-dependent density functional theory*, `Journal of Chemical Physics 126, 24101 (2007) <https://doi.org/10.1063/1.2423007>`__ 

.. [#ref16] M.\  Krykunov, M. Seth, T. Ziegler and J. Autschbach, *Calculation of the magnetic circular dichroism B term from the imaginary part of the Verdet constant using damped time-dependent density functional theory*, `Journal of Chemical Physics 127, 244102 (2007) <https://doi.org/10.1063/1.2806990>`__ 

.. [#ref17] M.\  Krykunov, A. Banerjee, T. Ziegler and J. Autschbach, *Calculation of Verdet constants with time-dependent density functional theory. Implementation and results for small molecules*, `Journal of Chemical Physics 122, 074105 (2005) <https://doi.org/10.1063/1.1850919>`__ 

.. [#ref20] M.\  Krykunov, M.D. Kundrat and J. Autschbach, *Calculation of CD spectra from optical rotatory dispersion, and vice versa, as complementary tools for theoretical studies of optical activity using time-dependent density functional theory*, `Journal of Chemical Physics 125, 194110 (2006) <https://doi.org/10.1063/1.2363372>`__ 

.. [#ref21] M.\  Krykunov and J. Autschbach, *Calculation of origin independent optical rotation tensor components for chiral oriented systems in approximate time-dependent density functional theory*, `Journal of Chemical Physics 125, 34102 (2006) <https://doi.org/10.1063/1.2210474>`__ 

.. [#ref22] J.\  Autschbach, L. Jensen, G.C. Schatz, Y.C.E. Tse and M. Krykunov, *Time-dependent density functional calculations of optical rotatory dispersion including resonance wavelengths as a potentially useful tool for determining absolute configurations of chiral molecules*, `Journal of Physical Chemistry A 110, 2461 (2006) <https://doi.org/10.1021/jp054847z>`__ 

.. [#ref23] M.\  Krykunov and J. Autschbach, *Calculation of optical rotation with time-periodic magnetic field-dependent basis functions in approximate time-dependent density functional theory*, `Journal of Chemical Physics 123, 114103 (2005) <https://doi.org/10.1063/1.2032428>`__ 

.. [#ref24] A.\  Baev, M. Samoc, P.N. Prasad, M. Krykunov and J. Autschbach, *A Quantum Chemical Approach to the Design of Chiral Negative Index Materials*, `Optics Express 15, 5730 (2007) <https://doi.org/10.1364/OE.15.005730>`__ 

.. [#ref28] O.\  Baseggio, G. Fronzoni, and M. Stener, *A new time dependent density functional algorithm for large systems and plasmons in metal clusters*, `Journal of Chemical Physics 143, 024106 (2015) <https://doi.org/10.1063/1.4923368>`__ 

.. [#ref29] O.\  Baseggio, D. Toffoli, G. Fronzoni, M. Stener, L. Sementa, and A. Fortunelli, *Extension of the Time-Dependent Density Functional Complex Polarizability Algorithm to Circular Dichroism: Implementation and Applications to* Ag\ :sub:`8` *and* Au\ :sub:`38` (SC\ :sub:`2` H\ :sub:`4` C\ :sub:`6` H\ :sub:`5` )\ :sub:`24`, `Journal of Physical Chemistry C 120, 24335 (2016) <https://doi.org/10.1021/acs.jpcc.6b07323>`__ 

.. [#ref30] S.\  Bernadotte, F. Evers, and C.R. Jacob, *Plasmons in Molecules*, `Journal of Physical Chemistry C 117, 1863 (2013) <https://doi.org/10.1021/jp3113073>`__ 

.. [#ref31] V.P. Osinga, S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Density functional results for isotropic and anisotropic multipole polarizabilities and* C\ :sub:`6` , C\ :sub:`7` , and C\ :sub:`8` *Van der Waals dispersion coefficients for molecules*, `Journal of Chemical Physics 106, 5091 (1997) <https://doi.org/10.1063/1.473555>`__ 

.. [#ref33] A.\  van der Avoird, P.E.S. Wormer, F. Mulder, R.M. Berns, Topics in Current Chemistry 93, 1 (1980) 

.. [#ref34] S.J.A. van Gisbergen, J.G. Snijders, and E.J. Baerends, *Time-dependent Density Functional Results for the Dynamic Hyperpolarizability of* C\ :sub:`60`, `Physical Review Letters 78, 3097 (1997) <https://doi.org/10.1103/PhysRevLett.78.3097>`__ 

.. [#ref35] S.J.A. van Gisbergen, J.G. Snijders and E.J. Baerends, *Calculating frequency-dependent hyperpolarizabilities using time-dependent density functional theory*, `Journal of Chemical Physics 109, 10644 (1998) <https://doi.org/10.1063/1.477762>`__ 

.. [#ref36] D.M. Bishop, *Aspects of Non-Linear-Optical Calculations*, `Advances in Quantum Chemistry 25, 3 (1994) <https://doi.org/10.1016/S0065-3276(08)60017-9>`__ 

.. [#ref37] D.P. Shelton and J.E. Rice, *Measurements and calculations of the hyperpolarizabilities of atoms and small molecules in the gas phase*, `Chemical Reviews 94, 3 (1994) <https://doi.org/10.1021/cr00025a001>`__ 

.. [#ref38] L.\  Jensen, L. Zhao, J. Autschbach and G.C. Schatz, *Resonance Raman Scattering of Rhodamine 6G as calculated using Time-Dependent Density Functional Theory*, `Journal of Physical Chemistry A 110, 5973 (2006) <https://doi.org/10.1021/jp0610867>`__ 

.. [#ref39] L.L. Zhao, L. Jensen and G.C. Schatz, Pyridine - Ag\ :sub:`20` *Cluster: A Model System for Studying Surface-Enhanced Raman Scattering*, `Journal of the American Chemical Society 128, 2911 (2006) <https://doi.org/10.1021/ja0556326>`__ 

.. [#ref40] L.\  Jensen, L.L. Zhao and G.C. Schatz, *Size-Dependence of the Enhanced Raman Scattering of Pyridine Adsorbed on* Ag\ :sub:`n` (n=2-8,20) *Clusters*, `Journal of Physical Chemistry C 111, 4756 (2007) <https://doi.org/10.1021/jp067634y>`__ 

.. [#ref41] M.\  Medves, L. Sementa, D. Toffoli, G. Fronzoni, A. Fortunelli, *An efficient hybrid scheme for time dependent density functional theory*, `Journal of Chemical Physics 152, 184104 (2020) <https://doi.org/10.1063/5.0005954>`__


