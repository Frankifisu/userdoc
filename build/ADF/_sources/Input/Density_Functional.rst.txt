.. _XC: 
.. index:: XC 
.. index:: exchange-correlation 

Density Functionals (XC)
************************

The Density Functional, also called the exchange-and-correlation (XC) functional, consists of an LDA, a GGA part, a Hartree-Fock exchange part (hybrids), and a meta-GGA part (meta-GGA or meta-hybrid).
Possibly, it also depends on virtual Kohn-Sham orbitals through inclusion of an orbital-dependent correlation (double-hybrids).
LDA stands for the Local Density Approximation, which implies that the XC functional in each point in space depends only on the (spin) density in that same point.
GGA stands for Generalized Gradient Approximation and is an addition to the LDA part, by including terms that depend on derivatives of the density.
A hybrid GGA (for example B3LYP) stands for some combination of a standard GGA with a part of Hartree-Fock exchange.
A meta-GGA (for example TPSS) has a GGA part, but also depends on the kinetic energy density.
A meta-hybrid (for example TPSSh) has GGA part, a part of Hartree-Fock exchange and a part that depends on the kinetic energy density.
For these terms ADF supports a large number of the formulas advocated in the literature.
For post-SCF energies only, ADF supports also various other meta-GGA functionals and more hybrid functionals.
A double-hybrid has a hybrid or a meta-hybrid part, but also contains a contribution from second-order Møller-Plesset perturbation theory (MP2). Here, only the hybrid (meta-hybrid) part is evaluated self-consistently, whereas the MP2 part is evaluated post-SCF and added to the hybrid (meta-hybrid) energy.

The key that controls the Density Functional is ``XC``. All subkeys are optional.

.. _keyscheme XC: 

::

  XC
    {LDA LDA {Stoll}}
    {GGA GGA}
    {MetaGGA metagga}
    {Model MODELPOT [IP]}
    {HartreeFock}
    {OEP fitmethod {approximation}}
    {HYBRID hybrid {HF=HFpart}}
    {MetaHYBRID metahybrid}
    {DOUBLEHYBRID doublehybrid}
    {RPA}
    {XCFUN}
    {RANGESEP {GAMMA=X} {ALPHA=a} {BETA=b}}
    (LibXC functional}
    {DISPERSION [s6scaling] [RSCALE=r0scaling] [Grimme3] [BJDAMP] [PAR1=par1]  [PAR2=par2]  [PAR3=par3]  [PAR4=par4] }
    {Dispersion Grimme4 {s6=...} {s8=...} {a1=...} {a2=...}}
    {DISPERSION dDsC}
    {DISPERSION UFF}
  end


If the ``XC`` key is omitted, the program will apply only the Local Density Approximation (no GGA terms). The chosen LDA form is then VWN. 


.. index:: LDA functionals 
.. index:: VWN 
.. _LDA: 

LDA
===

::

  XC
    LDA {functional} {Stoll}
  End


``LDA``
  Defines the LDA part of the XC functional.  
  If ``functional`` is omitted, VWN will be used (also if LYP is specified in the GGA part). 

  Available LDA functionals:

  * **Xonly**: The pure-exchange electron gas formula. Technically this is identical to the Xalpha form (see next) with a value 2/3 for the X-alpha parameter. 
  * **Xalpha**: The scaled (parametrized) exchange-only formula. When this option is used you may (optionally) specify the X-alpha *parameter* by typing a numerical value after the string Xalpha (separated by a blank). If omitted this parameter takes the default value 0.7 
  * **VWN**: The parametrization of electron gas data given by Vosko, Wilk and Nusair (ref [#ref1]_, formula version V). Among the available LDA options this is the more advanced one, including correlation effects to a fair extent. 

    * ``Stoll``: For the VWN variety of the LDA form you may include Stoll's correction [#ref2]_ by typing Stoll on the same line, after  the main LDA specification. You must not use Stoll's correction in combination with the Xonly or the Xalpha form for the Local Density functional. The Stoll formula is considered to be a *correlation* correction to the *Local* Density Approximation. It is conceptually not correct to use the Stoll correction *and* apply gradient (GGA) corrections to the correlation. It is the user's responsibility, in general and also here, to avoid using options that are not solidly justified theoretically. 

  * **PW92**: the parametrization of electron gas data given by Perdew and Wang (ref [#ref3]_). 


.. index:: GGA functionals 
.. index:: PW91 
.. index:: mPW 
.. index:: BLYP 
.. index:: OLYP 
.. index:: XLYP 
.. index:: PBE 
.. index:: RPBE 
.. index:: revPBE 
.. index:: mPBE 
.. index:: PBEsol 
.. index:: HTBS 
.. index:: BP86 
.. index:: LB94 
.. index:: KT1 
.. index:: BEE 
.. index:: S12g 
.. index:: SSB-D 
.. _GGA: 

GGA
===

::

  XC
     GGA functional
  End


``GGA``
  Specifies the GGA part of the XC Functional (in earlier times often called the 'non-local' correction to the LDA part of the density functional). It uses derivatives (gradients) of the charge density.

  Available GGA functionals: 

  * **BP86**:    Exchange: Becke,    Correlation: Perdew 
  * **PW91**:    Exchange: pw91x,    Correlation: pw91c 
  * **mPW**:     Exchange: mPWx,     Correlation: pw91c
  * **PBE**:     Exchange: PBEx,     Correlation: PBEc 
  * **RPBE**:    Exchange: RPBEx,    Correlation: PBEc 
  * **revPBE**:  Exchange: revPBEx,  Correlation: PBEc 
  * **mPBE**:    Exchange: mPBEx,    Correlation: PBEc 
  * **PBEsol**:  Exchange: PBEsolx,  Correlation: PBEsolc 
  * **HTBS**:    Exchange: HTBSx,    Correlation: PBEc 
  * **BLYP**:    Exchange: Becke,    Correlation: LYP 
  * **OLYP**:    Exchange: OPTX,     Correlation: LYP 
  * **OPBE**:    Exchange: OPTX,     Correlation: PBEc [#ref4]_ 
  * **BEE**:     Exchange: BEEx,     Correlation: PBEc
  * **XLYP**:    Exchange: XLYPx [#ref5]_ (exchange, not available separately from LYP) + LYP
  * **SSB-D**: Dispersion corrected functional by Swart-Solà-Bickelhaupt [#ref89]_ [#ref90]_. The SSB-D functional by definition already includes a dispersion correction by Grimme (factor 0.847455). There are some numerical issues with the GGA implementation in ADF of SSB-D (Ref. [#ref89]_ [#ref90]_) for some systems. Because of this, the GGA SSB-D option is only available for single-points (and NMR). Geometry optimizations (etc.) are still possible by using instead::

        XC
          METAGGA SSB-D
        END

    This METAGGA implementation is only possible with all-electron basis sets. Use GGA SSB-D for NMR calculations. 

  * **S12g**: Dispersion corrected (Grimme-D3) functional by Swart, successor of SSB-D [#ref6]_. 
  * **LB94**: By Van Leeuwen and Baerends [#ref7]_.  
  * **KT1**: By Keal and Tozer [#ref8]_. 
  * **KT2**: By Keal and Tozer [#ref8]_. 

  If only a GGA part is specified (omitting the ``LDA`` sub key) the LDA part defaults to VWN, except when the LYP correlation correction is used: in that case the LDA default is Xonly: pure exchange. 
  The reason for this is that the LYP formulas assume the pure-exchange LDA form, while for instance the Perdew-86 correlation correction is a correction to a *correlated*  LDA form. The precise form of this correlated LDA form assumed in the Perdew-86 correlation correction is not available as an option in ADF but the VWN  formulas are fairly close to it. 

  Separate choices can be made for the GGA exchange correction and the GGA correlation correction respectively. 
  Both specifications must be typed (if at all) on the same line, after the ``GGA`` subkey. 

  For the **exchange** part the options are:  

  * **Becke**:  Becke (1988) [#ref10]_. 
  * **PW86x**:  Perdew-Wang (1986) [#ref11]_. 
  * **PW91x**:  Perdew-Wang (1991) [#ref12]_ 
  * **mPWx**:  Modified PW91 by Adamo-Barone (1998) [#ref13]_ 
  * **PBEx**:  Perdew-Burke-Ernzerhof (1996) [#ref14]_ 
  * **RPBEx**:  revised PBE by Hammer-Hansen-Norskov (1999) [#ref15]_ 
  * **revPBEx**:  revised PBE by Zhang-Wang (1998) [#ref16]_  
  * **mPBEx**:  Modified PBE by Adamo-Barone (2002) [#ref17]_  
  * **PBEsolx**:  Perdew-Ruzsinszky-Csonka-Vydrov-Scuseria (2008) [#ref18]_ 
  * **HTBSx**:  [#ref19]_ 
  * **OPTX**:  Handy-Cohen (2001) [#ref20]_ 
  * **BEEx**:  Mortensen-Kaasbjerg-Frederiksen-Nørskov-Sethna-Jacobsen (2005) [#ref21]_  

  For the **correlation** part the options are: 

  * **Perdew**: Perdew (1986) [#ref22]_. 
  * **PBEc**: Perdew-Burke-Ernzerhof (1996) [#ref14]_ . 
  * **PBEsolc**: The PBEsol correlation correction by Perdew-Ruzsinszky-Csonka-Vydrov-Scuseria (2008) [#ref18]_ 
  * **PW91c**: Perdew-Wang (1991), see [#ref12]_. 
  * **LYP**: Lee-Yang-Parr (1988) correlation correction [#ref91]_ [#ref92]_ [#ref93]_.  
   

  The string GGA must contain not more than one of the exchange options and not more than one of the correlation options. 
  If options are applied for both they must be separated by a blank or a comma. 
  Example:

  :: 

    XC
      GGA Becke Perdew  
    End 

  is equivalent to

  :: 

    XC
      GGA BP86
    End 


  It is questionable to apply gradient corrections to the *correlation*, while not doing so at the same time for the exchange. Therefore, the program will check this and stop with an error message. This check can be overruled with the key ALLOW.


.. index:: meta-GGA (SCF) 
.. index:: M06-L 
.. index:: TPSS 
.. index:: revTPSS 
.. index:: MetaGGA 
.. _MetaGGA: 

MetaGGA
=======

:: 

  XC
    MetaGGA functional
  End 

``MetaGGA``
  Specifies that a meta-GGA should be used during the SCF. **All electron basis sets should be used** (see :ref:`Basis key<keyscheme BASIS>`). 

  Available meta-GGA functionals:

  * **M06-L**: Functional by Yan-Truhlar [#ref85]_ [#ref86]_  
  * **TPSS**: Functional by Tao-Perdew-Staroverov-Scuseria [#ref87]_ [#ref88]_ 
  * **revTPSS**: Revised TPSS functional [#ref26]_ 
  * **SSB-D**: Dispersion corrected GGA functional by Swart-Solà-Bickelhaupt [#ref89]_ [#ref90]_. Use GGA SSB-D for NMR calculations. 
  * **MVS**: Functional by Sun-Perdew-Ruzsinszky [#ref27]_
  * **MS0**: Functional by Sun et al. [#ref28]_
  * **MS1**: Functional by Sun et al. [#ref29]_
  * **MS2**: Functional by Sun et al. [#ref29]_
  * **SCAN**: Functional by Sun et al. [#ref31]_
  * **TASKxc**: Functional by `Aschebrock et al <https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.1.033082>`__. Intended for charge transfer systems.


The M06-L functional needs high integration accuracy (at least :ref:`BeckeGrid quality good<keyscheme BECKEGRID>`) for reasonable gradients. For TPSS moderate integration accuracy for reasonable gradients is sufficient. For heavier elements (Z>36) and if one uses the M06-L functional it is also necessary to include the following keyword 

::

  FragMetaGGAToten

Using this key FRAGMETAGGATOTEN the difference in the meta-hybrid or meta-GGA exchange-correlation energies between the molecule and its fragments will be calculated using the molecular integration grid, which is more accurate than the default, but is much more time consuming. Default is to calculate the meta-GGA exchange-correlation energies for the fragments in the numerical integration grid of the fragments. 



.. index:: Hartree-Fock

Hartree-Fock
============

:: 

  XC
    HartreeFock
  End 

``HartreeFock``
  Specifies that the Hartree-Fock exchange should be used during the SCF. 


.. index:: hybrid
.. _hybrids: 

.. index:: hybrid
.. index:: B3LYP 
.. index:: B3LYP* 
.. index:: B1LYP 
.. index:: KMLYP 
.. index:: O3LYP 
.. index:: X3LYP 
.. index:: BHandH 
.. index:: BHandHLYP 
.. index:: B1PW91 
.. index:: mPW1PW 
.. index:: mPW1K 
.. index:: PBE0 
.. index:: OPBE0 

Hybrid
======

::

  XC
    HYBRID functional {HF=HFpart}
  End

``HYBRID``
  Specifies that a hybrid functional should be used during the SCF. 

  Available Hybrid functionals:

  * **B3LYP**:  ADF uses VWN5 in B3LYP. functional (20% HF exchange) by Stephens-Devlin-Chablowski-Frisch  [#ref32]_. 
  * **B3LYP\***: Modified B3LYP functional (15% HF exchange) by Reiher-Salomon-Hess  [#ref33]_. 
  * **B1LYP**:  Functional (25% HF exchange) by Adamo-Barone  [#ref34]_. 
  * **KMLYP**:  Functional (55.7% HF exchange) by Kang-Musgrave  [#ref35]_. 
  * **O3LYP**:  Functional (12% HF exchange) by Cohen-Handy  [#ref36]_. 
  * **X3LYP**:  Functional (21.8% HF exchange) by Xu-Goddard  [#ref5]_. 
  * **BHandH**:  50% HF exchange, 50% LDA exchange, and 100% LYP correlation. 
  * **BHandHLYP**:  50% HF exchange, 50% LDA exchange, 50% Becke88 exchange, and 100% LYP correlation. 
  * **B1PW91**:  Functional by (25% HF exchange) Adamo-Barone  [#ref34]_. 
  * **mPW1PW**:  Functional (25% HF exchange) by Adamo-Barone  [#ref13]_. 
  * **mPW1K**:  Functional (42.8% HF exchange) by Lynch-Fast-Harris-Truhlar  [#ref40]_. 
  * **PBE0**:  Functional (25% HF exchange)  by Ernzerhof-Scuseria [#ref41]_  and by Adamo-Barone [#ref42]_,  hybrid form of PBE. 
  * **OPBE0**:  Functional (25% HF exchange) by Swart-Ehlers-Lammertsma  [#ref4]_,  hybrid form of OPBE. 
  * **S12H**:  Dispersion corrected (Grimme-D3) functional (25% HF exchange) by Swart [#ref6]_. 

  ``HFpart``
    Specifies the amount of HF exchange that should be used in the functional, instead of the default HF exchange percentage for the given hybrid. Example HF=0.25 means 25% Hartree-Fock exchange.

.. index:: meta-hybrid
.. index:: M06 
.. index:: M06-2X 
.. index:: M06-HF 
.. index:: TPSSH 

Meta-Hybrid
===========

::

  XC
    MetaHYBRID functional
  End

``MetaHYBRID``
  Specifies that a meta-hybrid functional should be used during the SCF.  

  Available meta-hybrid functionals: 

  * **M06**: Functional (27% HF exchange) by Yan-Truhlar [#ref85]_ [#ref86]_  
  * **M06-2X**: Functional (54% HF exchange) by Yan-Truhlar [#ref85]_ [#ref86]_  
  * **M06-HF**: Functional (100% HF exchange) by Yan-Truhlar [#ref85]_ [#ref86]_  
  * **TPSSH**: Functional (10% HF exchange) by Tao-Perdew-Staroverov-Scuseria [#ref87]_ [#ref88]_ 


.. _RS_FUNCTIONAL: 
.. index:: range-separated functionals
.. index:: long range corrected functionals
.. index:: LC functionals
.. index:: RS functionals
.. index:: range-separated functionals 
.. index:: long range corrected functionals 
.. index:: LC functionals 
.. index:: RS functionals 
.. index:: CAM-B3LYP 
.. index:: CAMY-B3LYP 

Range separated hybrids
=======================

In ADF there are two (mutually exclusive) ways of specifying range separated hybrids functionals: 

- Through the ``RANGESEP`` and ``XCFUN`` keys. This will use the Yukawa potential as switching function, see Ref. [#ref45]_;
- By specifying a range separated functional via the ``LibXC`` key.

See also the advanced tutorial: `Tuning the range separation in LC-wPBE for organic electronics <https://www.scm.com/news/tuning-range-separation-lc-wpbe-organic-electronics/>`__ 

.. _RSXCFUN:

RangeSep + XCFun: Yukawa-range separated hybrids
------------------------------------------------

``RANGESEP {GAMMA=X} {ALPHA=a} {BETA=b}``
  If RANGESEP is included, by default a long-range corrected (LC) functional is created with range separation parameter GAMMA of 0.75. As switching function in ADF the Yukawa potential is utilized, see Ref. [#ref45]_. Range separated functionals require XCFUN and are limited to GGA, meta-GGA, and CAMY-B3LYP. The CAMY-B3LYP functional is not the same as the CAM-B3LYP functional, since a different switching function is used. No other hybrids or meta-hybrids are supported. The special CAMYB3LYP functional is defined by three parameters, ALPHA, BETA and the attenuation parameter GAMMA. For CAMYB3LYP by default ALPHA is 0.19, BETA is 0.46, and GAMMA is 0.34.


Range-separated functionals make use of a modified form of the Coulomb operator that is split into pieces for exact exchange and DFT. As switching function in ADF the Yukawa potential is utilized, see Ref. [#ref45]_. Global hybrids can be thought of as a special case of a range-separated functional where the split is independent of the inter-electronic distance and is a simple X exact and 1-X DFT in all space. 

In a general RS-functional the split depends on the inter-electronic distance. How the split is achieved depends on the functional in question but it is achieved using functions that smoothly go from 1 to 0. In ADF an exponential function is used (the error function is common in Gaussian based codes). In a range-separated function the potential goes from a Coulomb interaction to a sum of Coulomb functions attenuated by an exponential function. 

In practical terms, this means that a range-separated functional looks very much like a hybrid (or meta-hybrid) functional but with additional integrals over the attenuated interaction with fit functions on the exact exchange side and a modified functional on the DFT side. 

**DFT part of RS-functionals**

Using Hirao's approach for creating RS-functionals, the RS form of a given exchange functional is created by multiplying the standard energy density by a factor that depends on the energy density. The factor is the same for all functionals and the only difference is introduced by the individual energy densities. 

The range-separation comes in at the level of the integrals over the operator with fit functions. They are very similar to the standard Coulomb integrals. 

**RS-functionals**

An RS-functional is described by a series of regions describing each of the pieces of the Coulomb operator. The total function is built up by looping over the regions and adding up all the pieces. Currently, simple LC functionals can be defined where the exact exchange goes from 0 to 1 as the inter-electronic distance increases and the DFT part does the reverse. In addition, CAMY-B3LYP type functionals can be defined. More general functionals are not possible yet. 

**Functionality/Limitations**

RS functionals with XCFUN are limited to the GGA and meta-GGA functionals and one hybrid CAMY-B3LYP. The following functionals can be evaluated with range-separation at the present time: 

+ LDA: VWN5, X-ALPHA PW92

+ GGA exchange: Becke88, PBEX, OPTX, PW91X, mPW, revPBEX

+ GGA correlation: LYP, Perdew86, PBEC

+ MetaGGA: TPSS, M06L, B95

+ Hybrids: CAMY-B3LYP

The following functionality has been tested: XC potential, energy, ground state geometry, TDDFT. Starting from ADF2018 singlet-triplet excitation calculations and excited state geometry optimizations are possible. See for possible limitations in case of excitation calculations or excited state geometry optimizations the corresponding part of the ADF manual. 

**Numerical stability**

The range-separated implementation requires that the range-separation parameter is not too close to the exponent of a fit function. In practice this means that values of the separation parameter between 1.0 and 50 can cause numerical problems. Typical useful values are in the range 0.2 to 0.9 so this should not be too serious a limitation. 

::

  XC
    XCFUN
    RANGESEP {GAMMA=X} {ALPHA=a} {BETA=b}
  END

Range separation is activated by putting RANGESEP in the XC block. Inclusion of XCFUN is required, see the  :ref:`XCFUN description <XCFUN>`. By default a long-range corrected (LC) functional is created with range separation parameter of 0.75. The parameter can be changed by modifying X in GAMMA=X in the RANGESEP card. Range separation typically will be used in combination with a GGA or METAGGA functional.  

Range separation can not be included with a hybrid or meta-hybrid, with one exception, the special RS functional: CAMY-B3LYP. This is entered as HYBRID CAMY-B3LYP and must be used in combination with XCFUN (see  :ref:`XCFUN description <XCFUN>`) and RANGESEP. The CAMY-B3LYP functional is defined by three parameters, alpha, beta and the attenuation parameter gamma. The gamma parameter can be modified as for the LC functionals. For CAMY-B3LYP it defaults to 0.34. The alpha and beta parameters can be modified through ALPHA=a and BETA=b in the RANGESEP card. They default to 0.19 and 0.46 respectively. 

::

  XC
    HYBRID CAMY-B3LYP   
    XCFUN
    RANGESEP GAMMA=0.34 ALPHA=0.19 BETA=0.46
  END


List of the most important functionals, for which one can use range separation: 

::

  LDA VWN
  GGA BLYP
  GGA BP86
  GGA PBE
  HYBRID CAMY-B3LYP


Range-separated hybrids with LibXC
----------------------------------

One can simply specify a range separated hybrid functional in the :ref:`LIBXC` key, *e.g.*::

  XC
    LibXC CAM-B3LYP
  End

See the :ref:`LIBXC` section for a list of available range separated hybrid functionals.

For the HSE03 and HSE06 short range-separated hybrids you can (optionally) specify the switching parameter omega, *e.g.*::

  XC
    LibXC HSE06 omega=0.1
  End



Notes on Hartree-Fock and (meta-)hybrid functionals
===================================================

If a functional contains a part of Hartree-Fock exchange then the LDA, GGA, metaGGA, or MODEL key should not be used in combination with this key, and one should only specify one of HartreeFock, HYBRID or MetaHYBRID. Dispersion can be added. Note that it is not recommended to use (part of the) Hartree-Fock exchange in combination with frozen cores, since at the moment the frozen core orbitals are not included in the Hartree Fock exchange operator. In ADF one can do unrestricted Hartree-Fock (or hybrid or meta-hybrid) calculations, as long as one has integer occupation numbers (ROHF is not implemented in ADF, only UHF). You also need to use the same XC-potential in the create run of the atoms, which is done automatically if you use the BASIS key. 

Starting from ADF2009.01 the meta-hybrids M06, M06-2X, M06-HF, and TPSSH can be used during the SCF. Also starting from ADF2009.01 Hartree-Fock and the (meta-)hybrid potentials can be used in combination with geometry optimization, TS, IRC, LT, and numerical frequencies; hybrids can be used in calculating :ref:`NMR chemical shift <NMR chemical shifts>`; PBE0 can be used in calculating  :ref:`NMR spin-spin coupling <NMR ss coupling const>`; Hartree-Fock and (meta-)hybrid can be used in calculating excitation energies, in which the kernel consists of the Hartree-Fock percentage times the Hartree-Fock kernel plus one minus the Hartree-Fock percentage times the ALDA kernel (thus no (meta-)GGA kernel). Hartree-Fock and the (meta-)hybrid potentials still can not or should not be used in combination with analytical frequencies, the (AO)RESPONSE key, EPR/ESR g-tensor, and frozen cores. Starting from ADF2010 it is possible to use Hartree-Fock and hybrids to calculate CD spectra. 

In ADF one can do unrestricted Hartree-Fock (or hybrid or meta-hybrid) calculations, as long as one has integer occupation numbers (ROHF is not implemented in ADF, only UHF). 

.. index:: HF exchange percentage 

It is possible to change the amount of HF exchange in the input for hybrids (not for meta-hybrids and Hartree-Fock). For many hybrid functionals the sum of the amount of Hartree-Fock exchange and the amount of LDA exchange (or GGA exchange) is one. If that is the case, then if one changes the amount of Hartree-Fock exchange in the input the amount of LDA exchange (or GGA exchange) will also be changed, such that the sum remains one. Example: 

::

  XC
    Hybrid B3LYP HF=0.25
  END

In this case the amount of Hartree-Fock for the B3LYP functional will be changed to 25% (instead of 20%), and the amount of LDA exchange to 75% (instead of 80%). The LDA correlation and GGA exchange and correlation part will be left unaltered. 

An accuracy issue is relevant for some of the meta-GGA functionals, in particular the M06 functionals. These need high integration accuracy (at least BeckeGrid quality good) for reasonable gradients. For TPSSH moderate integration accuracy for reasonable gradients is sufficient. For heavier elements (Z>36) and if one uses one of the M06 functionals it is also necessary to include the following keyword 

.. _keyscheme FRAGMETAGGATOTEN: 


::

  FragMetaGGAToten

Using this key ``FRAGMETAGGATOTEN`` the difference in the metahybrid or metagga exchange-correlation energies between the molecule and its fragments will be calculated using the molecular integration grid, which is more accurate than the default, but is much more time consuming. Default is to calculate the meta-hybrid or meta-GGA exchange-correlation energies for the fragments in the numerical integration grid of the fragments. 

For benchmark calculations one would like to use a large basis set, like the QZ4P basis set. In such cases it is recommended to use a good numerical quality. Thus for accurate hybrid calculations of **small** molecules one could use: 

::

  basis
    type QZ4P
  end
  AddDiffuseFit
  Dependency bas=1e-4
  NumericalQuality good


Post-SCF correlation methods
============================

Post-SCF correlation methods consist of two steps. In a first step, a DFT calculation using LDA, (meta-)GGA or (most often) a (meta-)hybrid calculation is performed. Based on the converged orbitals and orbital energies, a correlation energy is calculated after the SCF is completed and the result is added to the SCF XC-energy (or alternatively, in case of RPA, replaces the SCF XC energy). ADF offers RPA and MP2 methods and most importantly combinations of MP2 with various kinds of XC-functionals (so-called double-hybrids).

While traditionally, post-SCF correlation methods are associated with high-computational cost, ADF offers algorithms for RPA and some double-hybrids which offer tremendous speed-ups and make routine application to systems with hundreds of atoms possible. **These are RPA and all double-hybrids using only the opposite-spin component of the MP2 energy.** In case post-SCF correlation methods are to be used, we strongly recommend to use one of these methods for large systems. 

.. index:: double-hybrid
.. index:: B2-PLYP 
.. index:: B2GP-PLYP
.. index:: MPW2-PLYP
.. index:: B2K-PLYP
.. index:: B2T-PLYP
.. index:: B2PI-PLYP
.. index:: B2NC-PLYP
.. index:: ROB2-PLYP
.. index:: MPW2K-PLYP
.. index:: MPW2NC-PLYP
.. index:: DH-BLYP
.. index:: PBE0-DH
.. index:: LS1-DH
.. index:: PBE0-2
.. index:: PBE-QIDH
.. index:: SOS1-PBE-QIDH 
.. index:: rev-DSD-BLYP
.. index:: rev-DSD-PBEP86
.. index:: rev-DSD-PBE
.. index:: rev-DOD-BLYP
.. index:: rev-DOD-PBEP86
.. index:: rev-DOD-PBE
.. index:: DSD-BLYP
.. index:: DSD-PBEP86
.. index:: DSD-PBE
.. index:: rev-DSD-PBEP86-D4
.. index:: rev-DSD-PBE-D4
.. index:: rev-DSD-BLYP-D4
.. index:: rev-DOD-PBEP86-D4
.. index:: rev-DOD-PBE-D4
.. index:: rev-DOD-BLYP-D4
.. index:: LS1-TPSS
.. index:: DS1-TPSS
.. index:: DOD-SCAN
.. index:: rev-DOD-SCAN-D4
.. index:: rev-DSD-SCAN-D4
.. index:: SD-SCAN69
.. _DoubleHybrid: 


Double-Hybrid
-------------

::

  XC
    DOUBLEHYBRID functional
  End

``DOUBLEHYBRID``
  Specifies that a double-hybrid functional [#ref95]_ should be used. They combine a self-consistent (meta-)hybrid calculation with a post-SCF MP2 energy correction.

.. seealso::
  
   The paper `Double hybrid DFT calculations with Slater type orbitals <https://doi.org/10.1002/jcc.26209>`__ and the page `Double hybrids: recommendations for accurate thermochemistry and kinetics <https://www.scm.com/highlights/double-hybrids-recommendations-for-accurate-thermochemistry-kinetics/>`__ contain useful recommendations for double-hybrid calculations in ADF.


Double hybrids usually yield considerably better ground state energies than (meta-)GGA and (meta-)hybrid functionals. This especially true for thermochemistry, kinetics, transition metal chemistry as well as relative isomerization energies for systems with difficult electronic structure. For an overview of the capabilities of double-hybrids implemented in ADF we refer to a recent review. [#ref96]_

The MP2 correlation energy can be partitioned into two components, correlation of electron with paired spins (SS), and correlation of electron with unpaired spins (OS). Thus, it makes sense to divide double-hybrids into three categories: double-hybrids using the OS-component only, double-hybrids using both components, and double-hybrids using both components scaled independently.
In case of spin-orbit coupling approximate SS and OS contributions are calculated.

The computational effort for the evaluation of the latter component is much lower and a very efficient, quadratic scaling algorithm for this task has been developed and implemented in ADF. Double-hybrids using all spin-components can be treated with a standard, canonical implementation using global density fitting. Starting from AMS2020, the **canonical MP2 implementation has been improved**. Systems with more than 100 atoms are not a problem any more. Especially when larger QZ basis sets are used, the MP2 correction is usually evaluated faster than the preceding SCF. For systems much larger than ~100 atoms, it is advised however, to use an OS-only functional. 

**OS-only functionals**

OS-functionals combine a (meta-)hybrid-functional with empirical dispersion correction (in most cases) and use the correlation energy of unpaired spins only. They are often referred to as DOD-functionals. With the efficient implementation in ADF [#ref117]_, these calculations are routine for systems of hundreds of atoms, the computational bottleneck always being the underlying hybrid calculation during the SCF. **A DOD-calculation is always feasible when a hybrid calculation is feasible too!**

Currently, ADF supports the following DOD-functionals:

* **SOS1-PBE-QIDH**:     1-parameter functional with PBE exchange, PBE correlation (69 % HF, 44 % OS-MP2 [#ref97]_
* **rev-DOD-BLYP**:      B88 exchange, LYP correlation, Grimme3 dispersion (71 % HF, 62.2 % OS-MP2) [#ref98]_  
* **rev-DOD-BLYP-D4**:   B88 exchange, LYP correlation, Grimme4 dispersion (71 % HF, 63.5 % OS-MP2) [#ref98]_
* **rev-DOD-PBE**:       PBE exchange, PBE correlation, Grimme3 dispersion (68 % HF, 61.3 % OS-MP2) [#ref98]_  
* **rev-DOD-PBE-D4**:    PBE exchange, PBE correlation, Grimme4 dispersion (68 % HF, 61.8 % OS-MP2) [#ref98]_
* **rev-DOD-PBEP86**:    PBE exchange, P86 correlation, Grimme3 dispersion (69 % HF, 60.6 % OS-MP2) [#ref98]_  
* **rev-DOD-PBEP86-D4**: PBE exchange, P86 correlation, Grimme4 dispersion (69 % HF, 61.2 % OS-MP2) [#ref98]_
* **DOD-SCAN**:          SCAN exchange and correlation, Grimme3 dispersion (66 % HF, 63,0 % OS-MP2) [#ref98]_  
* **rev-DOD-SCAN-D4**:   SCAN exchange and correlation, Grimme4 dispersion (66 % HF, 63.4 % OS-MP2) [#ref98]_

Note, that except for **SOS1-PBE-QIDH**, all functionals include dispersion correction by default since they are an intrinsic part of the functionals. 

**Standard and 1-parameter functionals**

The functionals in this category combine a (meta-hybrid) functional with a scaled correlation energy from both components of the MP2-energy. 

Available functionals in this category:

* **B2PLYP**:     B88 exchange and LYP correlation (53 % HF, 27 % MP2)[#ref95]_
* **B2PIPLYP**:   B88 exchange and LYP correlation (60 % HF, 27 % MP2), parametrized for pi-pi interactions [#ref99]_ 
* **ROB2PLYP**:   B88 exchange and LYP correlation (59 % HF, 28 % MP2), restricted-open-shell version of B2PLYP [#ref100]_ 
* **B2TPLYP**:    B88 exchange and LYP correlation (60 % HF, 31 % MP2), parametrized for thermodynamics [#ref101]_ 
* **B2GPPLYP**:   B88 exchange and LYP correlation (65 % HF, 36 % MP2), 'General Purpose' parametrization [#ref102]_ 
* **B2KPLYP**:    B88 exchange and LYP correlation (72 % HF, 42 % MP2), parametrized for kinetics [#ref101]_ 
* **B2NCPLYP**:   B88 exchange and LYP correlation (70 % HF, 49 % MP2), parametrized for non-covalent interactions [#ref103]_
* **mPW2PLYP**:   mPW exchange and LYP correlation (55 % HF, 25 % MP2) [#ref104]_ 
* **mPW2KPLYP**:  mPW exchange and LYP correlation (72 % HF, 42 % MP2) [#ref101]_ 
* **mPW2NCPLYP**: mPW exchange and LYP correlation (42 % HF, 49 % MP2) [#ref103]_
* **DH-BLYP**:    1-Parameter functional with B88 exchange and LYP correlation (65 % HF, 42 % MP2) [#ref105]_
* **PBE0-DH**:    1-Parameter functional with PBE exchange and PBE correlation (50 % HF, 13 % MP2) [#ref106]_
* **PBE-QIDH**:   1-parameter functional with PBE exchange and PBE correlation (69 % HF, 33 % MP2) [#ref97]_
* **LS1-DH**:     1-Parameter functional with PBE exchange and PBE correlation (75 % HF, 42 % MP2) [#ref107]_
* **PBE0-2**:     1-Parameter functional with PBE exchange and PBE correlation (79 % HF, 50 % MP2) [#ref108]_
* **LS1-TPSS**:   1-Parameter functional with TPSS meta-GGA (85 % HF, 61 % MP2) [#ref109]_
* **DS1-TPSS**:   1-Parameter functional with TPSS meta-GGA (73 % HF, 53 % MP2) [#ref109]_ 

All functionals in this category can be combined with empirical dispersion correction which can be requested in the XC block in the usual way.

**Spin-component-scaled functionals**

The functionals in this category combine a (meta-hybrid) functional with a scaled correlation energy from both components of the MP2-energy. Opposed to the preceding category, both spin-components are scaled individually, allowing for more flexibility in the functional parametrization. As OS-functionals, they also include an empirical dispersion correction term in their parametrization. They are often referred to as DSD-functionals

Currently, ADF supports the following DSD-functionals:

* **DSD-BLYP**:          B88 exchange and LYP correlation, Grimme3 dispersion (69 % HF, 46 % OS-MP2, % 37 % SS-MP2) [#ref110]_  
* **rev-DSD-BLYP**:      revised version of DSD-BLYP, Grimme3 dispersion (71 % HF, 54.7 % os, 19.8 % SS-MP2) [#ref98]_  
* **rev-DSD-BLYP-D4**:   revised version of DSD-BLYP, Grimme4 dispersion (71 % HF, 55.9 % OS-, 19.7 % SS-MP2) [#ref98]_  
* **DSD-PBEP86**:        PBE exchange and P86 correlation (69 % HF, 52 % OS-, % 22 % SS-MP2) [#ref111]_  
* **rev-DSD-PBEP86**:    revised version of DSD-PBEP86 (69 % HF, 57.9 % OS-, 8 % SS-MP2) [#ref98]_  
* **rev-DSD-PBEP86-D4**: PBE exchange and P86 correlation, Grimme4 dispersion (69 % HF, 59.2 % OS-, 6.4 % SS-MP2) [#ref98]_  
* **DSD-PBE**:           PBE exchange and PBE correlation, Grimme3 dispersion (68 % HF, 55 % OS-, % 13 % SS-MP2) [#ref111]_  
* **rev-DSD-PBE**:       revised version of DSD-PBE, Grimme3 dispersion (68 % HF, 58.5 % os, 7 % SS-MP2) [#ref98]_  
* **rev-DSD-PBE-D4**:    revised version of DSD-PBE, Grimme4 dispersion (68 % HF, 60 % os, 4.2 % SS-MP2) [#ref98]_  
* **rev-DSD-SCAN-D4**:   based on SCAN meta-GGA (66 % HF, 63.2 % OS-, 1.3 % SS-MP2) [#ref98]_
* **SD-SCAN69**:         Based on SCAN meta-GGA, no dispersion correction (69 % HF, 62 % OS-, 26 % SS-MP2) [#ref98]_  

Except for **SD-SCAN69**, all functionals mentioned include dispersion correction by default. For more technical details of the algorithm and how to tweak parameters, see :ref:`the MBPT section<keyscheme MBPT>`.

.. _MP2:
.. index:: MP2

MP2-methods
-----------

::

  XC
    MP2
    EmpiricalScaling {NONE|SOS|SCS|SCSMI}
  END

In addition to double-hybrids, ADF also implements MP2 including some popular spin-scaled variants. Technically, they are not distinct from double-hybrids, however, the all rely on a HF instead of a DFT calculation. The following variants are supported.

* **SOS-MP2**:    pure HF reference (100 % HF, 130 % OS-MP2) [#ref113]_
* **MP2**:        pure HF reference (100 % HF, 100 % MP2 correlation)
* **SCS-MP2**:    pure HF reference (100 % HF, 120 % OS-MP2, 33 % SS-MP2) [#ref114]_
* **SOS-MI-MP2**: pure HF reference (100 % HF, 40 % OS-MP2, 129 % SS-MP2) [#ref115]_

In case of spin-orbit coupling approximate SS and OS contributions are calculated.

The spin-scaling variant can be requested in the XC block together with the ``MP2`` keyword:

::

  XC
    MP2
    EmpiricalScaling SOS
  END

requests an SOS-MP2 calculation.

For more technical details of the algorithm and how to tweak parameters, see :ref:`the MBPT section<keyscheme MBPT>`.

.. _RPA:
.. index:: RPA

RPA and RPA + SOSSX
-------------------

::

  XC
    RPA
  End

``RPA``
  requests that the RPA exchange and correlation energies are evaluated after the SCF. The XC-energy evaluated from the functional used in the SCF is replaced by the RPA XC-energy. 

::

  XC
    RPASOX
  End

requests that a statically screened second-order exchange term is added to the RPA energy. This improves total energies and most often also relative energies. The following explanations are equially valid for RPA+SOSSX.

RPA can be used in conjunction with LDA, GGAs and hybrid functionals (``RPA@LDA``, ``RPA@PBE``, ``RPA@hybrid``, respectively). IMPORTANT: **spin-orbit coupled relativistic effects are not supported yet!** ``RPA@LDA`` is the default. To specify a different functional for the SCF, simply add the ``RPA`` keyword to the functional specification. In example, the following key specifies a ``RPA@PBE`` calculation, 

::

  XC
    GGA PBE
    RPA
  END

A ``RPA@PBE0`` calculation is requested by


::

  XC
    HYBRID PBE0
    RPA
  END


In ADF, the RPA energy is always evaluated in the AO-basis and the algorithm is similar to SOS-AO-PARI-MP2. The main difference is that the final RPA correlation energy is evaluated along the imaginary frequency axis, while the polarizability (non-interacting Kohn-Sham density response function, which is also evaluated in SOS-MP2) is evaluated in imaginary time. Thus, two grid parameters can be tweaked:

::

  MBPT
     nTime 12
     nFrequency 12
  END

requests 12 points for imaginary time and imaginary frequency integration each, which is also the default (As opposed to 9 points for MP2). It is also possible to use a different number of points for imaginary frequency than for imaginary time. The computational time required for the RPA calculation increases linearly with the number of imaginary time points and sub-linearly with the number of imaginary frequency points. However, memory increases linearly with the number of imaginary frequency points while it is not affected by the size of the imaginary time grid.

Notes on MP2, double-hybrid functionals and RPA
-----------------------------------------------

All post-SCF correlation methods can only be used for single-point calculations (Although numerical gradients are available in the AMS driver). However, they all support the use of frozen cores, empirical dispersion correction, and spin-unrestricted calculations.
MP2 and double-hybrid functionals can be used icw scalar and spin-orbit coupled relativistic effects within the ``ZORA``, ``X2C``, or ``RA-X2C`` formalism.
RPA can be used icw scalar relativistic effects within the ``ZORA``, ``X2C``, or ``RA-X2C`` formalism, but not icw spin-orbit coupling.

The basis set requirements are higher than for standard functionals. We recommend to use all-electron basis sets of at least TZP quality to obtain meaningful results. Using basis sets of quadruple-zeta quality is usually better. all post-SCF correlation methods rely on information from virtual orbitals which are especially prone to linear dependency issues in the basis set coming from almost linearly dependent linear combinations of AOs. These linear combinations need to be removed during the SCF. This is controlled inside the ``DEPENDENCY`` block. While in ADF the default is 1e-4, for post-SCF correlation methods, a default of 1e-03 is chosen. This is a safe choice, in the sense that it ensures numerical stability in most cases but does not truncate the basis set size too much. Still, one should be aware that this value already corresponds to a drastic truncation of the virtual space.

It is also recommended to use ``NumericalQuality GOOD`` but ``FitSetQuality NORMAL``. Thus, recommended settings for e.g. a double-hybrid calculation using the **rev-DOD-BLYP-D4** functional with the QZ4P basis set is:

::

  BASIS
     Type QZ4P
     Core NONE
  End

  XC
    Doublehybrid revDODBLYPD4
  End 

  NumericalQualtity Good

  RIHartreeFock 
    FitSetQuality Normal
  End

In case of numerical difficulties to converge the SCF, it is often a good idea to increase also the fitset during the SCF, but still use ``FitSetQuality NORMAL`` for the post-SCF correlation method. 

::

  BASIS
     Type QZ4P
     Core NONE
  End

  XC
    Doublehybrid revDODBLYPD4
  End 

  NumericalQualtity Good
  
  MPBT 
    FitsetQuality Normal
  End


In this case, ``FitSetQuality GOOD`` is used during the SCF (through the NumericalQuality key). After the SCF, the fit is recalculated using ``FitSetQuality NORMAL``.

For more technical details of the algorithm and how to tweak parameters, see :ref:`the RPA section<keyscheme MBPT>`.

.. index:: SAOP 
.. index:: GRAC 
.. _MODELPOTENTIALS: 
.. index:: model potentials

Model Potentials
================

Several asymptotically correct XC potentials have been implemented in ADF, such as the (now somewhat outdated) LB94 potential [#ref7]_, the gradient-regulated asymptotic correction (GRAC) [#ref49]_, and the statistical average of orbital potentials (SAOP) [#ref52]_ [#ref50]_. These can currently be used only for response property calculations, not for geometry optimizations. For spectroscopic properties, they usually give results superior to those obtained with LDA or GGA potentials, (see Ref. [#ref51]_ for applications to (hyper)polarizabilities Cauchy coefficients, etc. of small molecules). This is particularly true if the molecule is small and the (high-lying) virtual orbitals are important for the property under study.  

It was also shown that, simply using the orbital energies of the occupied Kohn-Sham orbitals of a SAOP calculation, quite good agreement with experiment vertical ionization potentials is obtained. This is true not only for the HOMO orbital energy, which should be identical to (minus) the experimental ionization potential with the exact XC potential, but also for lower-lying occupied orbital energies. The agreement becomes worse for deep-lying core orbital energies. A theoretical explanation and practical results are given in Ref. [#ref53]_. 

:: 

  XC
    Model ModelPotential [IP]
  End 


``MODEL``
  Specifies that one of the less common XC potentials should be used during the SCF. These potentials specify both the exchange and the correlation part. No LDA, GGA, MetaGGA, HartreeFock, HYBRID or MetaHYBRID key should be used in combination with these keys. It is also not advised to use any energy analysis in combination with these potentials. For energy analysis we recommend to use one of the GGA potentials. It is currently not possible to do a Create run with these potentials. It is possible to do a one atom regular ADF calculation with these potentials though, using a regular adf.rkf (TAPE21) file from an LDA or GGA potential as input.  
  Available model potentials:

  * **LB94**: This refers to the XC functional of Van Leeuwen and Baerends [#ref7]_. There are no separate entries for the Exchange and Correlation parts respectively of LB94. Usually the GRAC or SAOP potentials give results superior to LB94. 

  * **GRAC**: The gradient-regulated asymptotic correction, which in the outer region closely resembles the LB94 potential [#ref49]_. It requires a further argument: the ionization potential [IP] of the molecule, in hartree units. This should be estimated or obtained externally, or calculated in advance from two GGA total energy calculations. 

  * ``IP``:Should be supplied only if GRAC is specified.  

  * **SAOP**: The statistical average of orbital potentials [#ref52]_ [#ref50]_. It can be used for all electron calculations only. It will be expensive for large molecules, but requires no further parameter input. 


The LB94, GRAC, and SAOP functionals have only a SCF (=Potential) implementation, but **no Energy** counterpart. 

The LB94, GRAC, and SAOP forms are density functionals specifically designed to get the correct asymptotic behavior. This yields much better energies for the highest occupied molecular orbital (HOMO) and better excitation energies in a calculation of response properties (Time Dependent DFT). Energies for lower lying orbitals (sub-valence) should improve as well (in case of GRAC and SAOP, but not LB94). The energy expression underlying the LB94 functional is very inaccurate. This does not affect the response properties but it does imply that the energy and its derivatives (gradients) should not be used because LB94-optimized geometries will be wrong, see for instance [#ref58]_. The application of the LB94 functional in a runtype that involves the computation of energy gradients is disabled in ADF. You can override this internal check with the key :ref:`ALLOW<keyscheme ALLOW>`. 

In case of a GRAC calculation, the user should be aware that the potential in the outer region is shifted up with respect to the usual level. In other words, the XC potential does not tend to zero in the outer region in this case. The size of the shift is the difference between the HOMO orbital energy and the IP given as input. In order to compare to regular GGA orbital energies, it is advisable to subtract this amount from all orbital energies. Of course, orbital energy differences, which enter excitation energies, are not affected by this shift in the potential. 




.. index:: OEP 
.. index:: KLI 
.. index:: CEDA 
.. index:: optimized effective potential 

Optimized effective potentials
==============================

::

  XC
    OEP fitmethod {approximation}
  End


``OEP``
  Defines the optimized effective potential expanded into a set of the fit functions. The subkeyword fitmethod can be any of the following: BARTLETT [#ref59]_, SCUSERIA [#ref60]_. In the case of SCUSERIA one of the following approximations needs to be specified: CEDA, KLI or SLATER. An application of OEP in ADF can be found in Ref. [#ref61]_. 






.. index:: XCFUN 
.. _XCFUN:

XCFun
=====

``XCFUN``
  XCFun is a library of approximate exchange-correlation functionals, see Ref. [#ref62]_, for which functional derivatives can be calculated automatically. For example, with XCFUN the full (non-ALDA) kernel can be evaluated and this has been implemented in the calculation of TDDFT excitations. The Full kernel can not be used in combination with symmetry or excited state geometry optimizations. The following functionals can be evaluated with XCFUN at the present time: 

  + LDA: VWN5, X-ALPHA, PW92
  + GGA exchange: Becke88, PBEX, OPTX, PW91X, mPW, revPBEX
  + GGA correlation: LYP, Perdew86, PBEC
  + MetaGGA: TPSS, M06L, B95
  + MetaHybrids: M06, M05, M062X, M06HF
  + Hybrids: PBE0, B3LYP, BHandH, B1LYP, B3LYP*, PBEFALFX
  + Yukawa range separated Hybrids: CAMY-B3LYP and more, see :ref:`Yukawa RS hybrids with XCFUN <RSXCFUN>`

Here MetaGGA B95 means Becke88 exchange + B95c correlation.
The Metahybrids PW6B95 and PWB6K have been removed from this list, since they do not agree with the LibXC implementation.

.. index:: LIBXC 
.. _LIBXC:

LibXC
=====

``LibXC functional``
  LibXC is a library of approximate exchange-correlation functionals, see Ref. [#ref63]_ [#ref64]_. 
  **All electron basis sets should be used** (see :ref:`Basis key<keyscheme BASIS>`).
  Version 5.1.2 of LibXC is used.
  The following functionals can be evaluated with LibXC (incomplete list): 

  + LDA: LDA, PW92, TETER93
  + GGA: AM05, BCGP, B97-GGA1, B97-K, BLYP, BP86, EDF1, GAM, HCTH-93, HCTH-120, HCTH-147, HCTH-407, HCTH-407P, HCTH-P14, PBEINT, HTBS, KT2, MOHLYP, MOHLYP2, MPBE, MPW, N12, OLYP, PBE, PBEINT, PBESOL, PW91, Q2D, SOGGA, SOGGA11, TH-FL, TH-FC, TH-FCFO, TH-FCO, TH1, TH2, TH3, TH4, XLYP, XPBE, HLE16
  + MetaGGA: M06-L, M11-L, MN12-L, MS0, MS1, MS2, MVS, PKZB, RSCAN, R2SCAN, REVSCAN, SCAN, TPSS, HLE17
  + Hybrids: B1LYP, B1PW91, B1WC, B3LYP, B3LYP*, B3LYP5, B3LYP5, B3P86, B3PW91, B97, B97-1 B97-2, B97-3, BHANDH, BHANDHLYP, EDF2, MB3LYP-RC04, MPW1K, MPW1PW, MPW3LYP, MPW3PW, MPWLYP1M, O3LYP, OPBE, PBE0, PBE0-13, REVB3LYP, REVPBE, RPBE, SB98-1A, SB98-1B, SB98-1C, SB98-2A, SB98-2B, SB98-2C, SOGGA11-X, SSB, SSB-D, X3LYP
  + MetaHybrids: B86B95, B88B95, BB1K, M05, M05-2X, M06, M06-2X, M06-HF, M08-HX, M08-SO, MPW1B95, MPWB1K, MS2H, MVSH, PW6B95, PW86B95, PWB6K, REVSCAN0, SCAN0, REVTPSSH, TPSSH, X1B95, XB1K
  + Range-separated: CAM-B3LYP, CAMY-B3LYP, HJS-PBE, HJS-PBESOL, HJS-B97X, HSE03, HSE06, LRC_WPBE, LRC_WPBEH, LCY-BLYP, LCY-PBE, M06-SX, M11, MN12-SX, N12-SX, TUNED-CAM-B3LYP, WB97, WB97X

One of the acronyms in the list above can be used,
or one can also use the functionals described at the LibXC website `http://www.tddft.org/programs/Libxc <http://www.tddft.org/programs/Libxc>`__.
Note that ADF can not calculate VV10 dependent LibXC functionals, like VV10, LC-VV10, B97M-V, WB97X-V.
Example usage for the BP86 functional:

::

  XC
    LibXC BP86
  End

Alternative

::

  XC
    LibXC XC_GGA_X_B88 XC_GGA_C_P86
  End

In case of LibXC the output of the ADF calculation will give the reference for the used functional, see also the LibXC website `http://www.tddft.org/programs/Libxc <http://www.tddft.org/programs/Libxc>`__.

Do not use any of the subkeys LDA, GGA, METAGGA, MODEL, HARTREEFOCK, OEP, HYBRID, METAHYBRID, XCFUN, RANGESEP in combination with the subkey LIBXC.
One can use the DISPERSION key icw LIBXC. For a selected number of functionals the optimized dispersion parameters will then be used automatically,
please check the output in that case.
Note that in many cases you have to include the DISPERSION key and include the correct dispersion parameters yourself. 

The LibXC functionals can not be used icw frozen cores, NMR calculations, the (AO)RESPONSE key, EPR/ESR g-tensor.
Most LibXC functionals can be used in combination with geometry optimization, TS, IRC, LT, numerical frequencies, and excitation energies (ALDA kernel used).
For a few GGA LibXC functionals analytical frequencies can be calculated, and
one can use the full kernel in the calculation of excitation energies (if FULLKERNEL is included as subkey of the key EXCITATIONS).
In case of LibXC (meta-)hybrids and calculating excitation energies, the kernel consists of the Hartree-Fock percentage times the Hartree-Fock kernel plus one minus the Hartree-Fock percentage times the ALDA kernel (thus no (meta-)GGA kernel). 
For the LibXC range separated functionals, like CAM-B3LYP, starting from ADF2016.102 the kernel consists of range separated ALDA plus the kernel of the range separated exact exchange part.
In ADF2016.101 the kernel for LibXC range separated functionals, like CAM-B3LYP, was using a 100% ALDA plus range separated exact exchange kernel (the ALDA part was not range-separated corrected).
For the range separated functionals WB97 and WB97X one can use the full kernel in the calculation of excitation energies.


.. index:: van der Waals
.. index:: MM dispersion
.. index:: dispersion corrected functionals
.. index:: GGA-D
.. index:: DFT-D
.. index:: GGA-D3
.. index:: DFT-D3
.. index:: GGA-D4
.. index:: DFT-D4
.. _MM dispersion:
.. _dispersion corrections:

Dispersion corrections
======================

``Dispersion Grimme4 {s6=...} {s8=...} {a1=...} {a2=...}``
  If ``Dispersion Grimme4`` is present in the ``XC`` block the D4(EEQ) dispersion correction (with the electronegativity equilibrium model) by the Grimme group [#ref65]_ will be added to the total bonding energy, gradient and second derivatives, where applicable.

  The D4(EEQ) model has four parameters: :math:`s_6`, :math:`s_8`, :math:`a_1` and :math:`a_2` and their value should depend on the XC functional used. For the following functionals the D4(EEQ) parameters are **predefined**: B1B95, B3LYP, B3PW91, BLYP, BP86, CAM-B3LYP, HartreeFock, OLYP, OPBE, PBE, PBE0, PW6B95, REVPBE, RPBE, TPSS, TPSSH. For these functionals it is enough to specify ``Dispersion Grimme4`` in the input block. E.g.:

  .. code-block:: none

    XC
      GGA BLYP
      Dispersion Grimme4
    END

  For all other functionals you should explicitly specify the D4(EEQ) parameters in the ``Dispersion`` key (otherwise the PBE parameters will be used). For example, for the PW91 functional you should use the following input:

  .. code-block:: none

    XC
      GGA PW91
      Dispersion Grimme4 s6=1.0 s8=0.7728 a1=0.3958 a2=4.9341
    END

  The D4(EEQ) parameters for many functionals can be found in the supporting information of the following paper: [#ref65]_.

  For Double-Hybrids, see the :ref:`DoubleHybrid` section of the user manual.



``DISPERSION Grimme3 BJDAMP``
  If DISPERSION Grimme3 BJDAMP is present a dispersion correction (DFT-D3(BJ)) by Grimme [#ref66]_ will be added to the total bonding energy, gradient and second derivatives, where applicable. Parametrizations are implemented e.g. for B3LYP, TPSS, BP86, BLYP, PBE, PBEsol, and RPBE. For SCAN parameters from Ref. [#ref67]_ are used. 

  For example, this is the input block for specifying the PBE functional with Grimme3 BJDAMP dispersion correction (PBE-D3(BJ)):

  .. code-block:: none

    XC
      GGA PBE
      DISPERSION Grimme3 BJDAMP
    End

  The D3(BJ) dispersion correction has four parameters. One can override the default parametrization by using *PAR1=.. PAR2=..*, etc. In the table the relation is shown between the parameters and the real parameters in the Dispersion correction.

  .. csv-table::

    variable, variable on Bonn  `website <https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3/functionalsbj>`__
    PAR1,    s6
    PAR2,    a1
    PAR3,    s8
    PAR4,    a2

  For example, this is the input block for specifying the PBE-D3(BJ)-GP parametrization by Proppe et.al. [#ref116]_ (i.e. :math:`a_1=0, s_8=0, a_2=5.6841`):

  .. code-block:: none

    XC
      GGA PBE
      DISPERSION Grimme3 BJDAMP PAR2=0 PAR3=0 PAR4=5.6841
    End



``DISPERSION Grimme3``
  If DISPERSION Grimme3 is present a dispersion correction (DFT-D3) by Grimme [#ref68]_ will be added to the total bonding energy, gradient and second derivatives, where applicable. Parametrizations are available e.g. for B3LYP, TPSS, BP86, BLYP, revPBE, PBE, PBEsol, and RPBE, and will be automatically set if one of these functionals is used. There are also parameters directly recognized for S12g and S12h. For SCAN parameters from Ref. [#ref67]_ are used. For all other functionals, PBE-D3 parameters are used as default. You can explicitly specify the three parameters.

  .. csv-table::

    variable, variable on Bonn  `website <https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3/functionals>`__
    PAR1 ,   s6
    PAR2 ,   "sr,6"
    PAR3 ,   s8

``DISPERSION {s6scaling]} {RSCALE=r0scaling}``
  If the DISPERSION keyword is present (without the argument Grimme3) a dispersion correction (DFT-D) by Grimme [#ref41]_  will be added to the total bonding energy, gradient and second derivatives, where applicable.  The global scaling  factor with which the correction is added depends on the exchange-correlation functional used at SCF but it can be modified using the *s6scaling* parameter. The following scaling factors are used  (with the XC functional in parentheses):  1.20 (BLYP), 1.05 (BP), 0.75 (PBE), 1.05 (B3LYP). In all other cases a factor 1.0 is used unless modified  via the s6scaling parameter. The SSB-D functional includes the dispersion correction (factor 0.847455) by default. 

  The van der Waals radii used in this implementation are hard coded in ADF.  However, it is possible to modify the global scaling parameter for them using the *RSCALE=r0scaling* argument. The default value is 1.1 as proposed by Grimme  [#ref41]_. Please also see   :ref:`additional documentation<MM dispersion>` for more information about this topic. 

``DISPERSION dDsC``
  The DISPERSION dDsC key invokes the density dependent dispersion correction [#ref72]_, which has been parametrized for the functionals BLYP, PBE, BP, revPBE, B3LYP, PBE0 and BHANDHLYP. 

``DISPERSION UFF``
  The DISPERSION UFF key invokes the universal correction of density functional theory to include London dispersion (DFT-ulg) [#ref73]_,  which has been parametrized for all elements up to Lr (Z=103), and for the functional PBE, PW91, and B3LYP. For other functionals the PBE parameters will be used. 

``DISPERSION MBD``
  The DISPERSION MBD key invokes the MBD\@rsSCS method [#ref74]_, which is designed to accurately describe long-range correlation (and thus dispersion) in finite-gap systems, including at the same time a description of the short-range interactions from the underlying DFT computation of the electronic structure.

.. _GrimmeD4:

DFT-D4 functionals
------------------

Grimme's latest dispersion correction, D4(EEQ) [#ref65]_, has been added in the 2019.3 release of the Amsterdam Modeling Suite. This is the latest dispersion correction in the DFT-D family. In contrast to the earlier D3 dispersion correction, in D4(EEQ) the atomic coordination-dependent dipole polarizabilities are scaled based on atomic partial charges obtained from an electronegativity equilibrium model (EEQ). Compared to D3 the introduced charge dependence improves thermochemical properties, especially for systems containing metals. The authors recommend D4(EEQ) as a physically improved and more sophisticated dispersion model in place of D3.


DFT-D3 functionals
------------------

The D3 dispersion correction by Stefan Grimme is available in ADF. Grimme and his coworkers at the Universität Münster outlined the parametrization of this new correction, dubbed DFT-D3, in Ref. [#ref68]_. A slightly improved version with a more moderate BJ damping function appeared later, and was called DFTB-D3-BJ. [#ref66]_ Here they list the advantages of the new method as the following: 

+ It is less empirical, i.e., the most important parameters are computed from first principles by standard Kohn-Sham (KS)-(TD)DFT.

+ The approach is asymptotically correct with all DFs for finite systems (molecules) or nonmetallic infinite systems. It gives the almost exact dispersion energy for a gas of weakly interacting neutral atoms and smoothly interpolates to molecular (bulk) regions.

+ It provides a consistent description of all chemically relevant elements of the periodic system (nuclear charge Z = 1-94).

+ Atom pair-specific dispersion coefficients and cutoff radii are explicitly computed.

+ Coordination number (geometry) dependent dispersion coefficients are used that do not rely on atom connectivity information (differentiable energy expression).

+ It provides similar or better accuracy for "light" molecules and a strongly improved description of metallic and "heavier" systems.

DFT-D3-BJ is invoked with the XC block, for example 

::

  XC
    GGA BLYP
    Dispersion Grimme3 BJDAMP
  END

Parametrizations are available for: B3LYP, TPSS, BP86, BLYP, revPBE, PBE, PBEsol, RPBE, and some more functionals, and will be automatically set if one of these functionals is used. Otherwise PBE parameters will be used. The parameters can be set manually, see the XC key block. 
In ADF2016 parameters for Grimme3 and Grimme3 BJDAMP were updated according to version 3.1.1 of the coefficients, available at the
Bonn  `website <https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3/dft-d3>`__


DFT-D functionals
-----------------

An implementation for dispersion corrections based, called DFT-D is available in ADF. Like DFT-D3 this implementation is easy to use and is also supported by the GUI.

This DFT-D implementation is based on the paper by Grimme [#ref41]_ and is  extremely easy to use. The correction is switched on by specifying *DISPERSION*,  possibly with parameters, in the XC input block.  See  :ref:`description of the XC input block<keyscheme XC>`  for details about the DISPERSION keyword.  

Energies calculated Post-SCF using different DFT-D or GGA-D functionals are also present in table printed  when METAGGA keyword is specified. These include: BLYP-D, PBE-D, BP86-D, TPSS-D, B3LYP-D, and B97-D.  NOTE: this option does not require specifying a DISPERSION keyword in the XC block and  thus there is **no correction added to the energy gradient** in this case. Please also note that although the original B97 functional includes HF exchange (and is thus  a hybrid functional), the B97-D is a pure GGA. B3LYP-D is, however, a hybrid functional.  The following functional-dependent global scaling factors s\ :sub:`6`  are used:  1.2 (BLYP-D), 0.75 (PBE-D), 1.05 (BP86-D), 1.0 (TPSS-D), 1.05 (B3LYP-D), and 1.25 (B97-D).  These are fixed and cannot be changed. 

Regarding performance of different functionals, testing has shown that BLYP-D gives good results  for both energies and gradients involving VdW interactions. Post-SCF energy-only calculations  at fixed geometries showed that also B97-D gives good binding energies compared to high-level  reference data. Thorough comparison of different DFT-D functionals can be found in  ref. [#ref94]_

**Note:** The original paper by Grimme included parameters for elements H throughout Xe. In ADF2009.01 values for dispersion parameters for DFT-D functionals for heavier elements (Cs-Rn) have been added. These new values have not been tested extensively. Thus, in this implementation, no dispersion correction is added for interactions involving atoms heavier than Radon. 

DFT-D is invoked with the XC block, for example 

::

  XC
    GGA BLYP
    Dispersion
  END



.. index:: dDsC dispersion correction 

dDsC: density dependent dispersion correction
---------------------------------------------

The DISPERSION dDsC key invokes the density dependent dispersion correction [#ref72]_, which has been parametrized for the functionals BLYP, PBE, BP, revPBE, B3LYP, PBE0 and BHANDHLYP. 

::

  XC
    GGA BLYP
    Dispersion dDsC
  END

For other functionals one can set the dDsC parameters ATT0 and BTT0 with

::

  XC
    ...
    DISPERSION dDsC ATT0=att0 BTT0=btt0
  END

The dispersion dDsC in ADF can not be used icw fragments larger than 1 atom. The reason is that ADF uses the Hirshfeld partitioning on fragments for dDsC, which is only correct if the fragments are atoms.

.. index:: UFF dispersion correction 
.. index:: DFT-ulg 

DFT-ulg
-------

The DISPERSION UFF key invokes the universal correction of density functional theory to include London dispersion (DFT-ulg) [#ref73]_,  which has been parametrized for all elements up to Lr (Z=103), and for the functional PBE, PW91, and B3LYP. For other functionals the PBE parameters will be used. Example: 

::

  XC
    GGA PBE
    Dispersion UFF
  END

.. index:: GGA-MBD 
.. index:: DFT-MBD 

DFT-MBD functionals
-------------------

The DISPERSION MBD key invokes the MBD\@rsSCS method [#ref74]_, which is designed to accurately describe long-range correlation (and thus dispersion) in finite-gap systems, including at the same time a description of the short-range interactions from the underlying DFT computation of the electronic structure. The MBD (many-body dispersion) method [#ref81]_ obtains an accurate description of van der Waals (vdW) interactions that includes both screening effects and treatment of the many-body vdW energy to infinite order.  The revised MBD\@rsSCS method [#ref74]_ employs a range-separation (rs) of the self-consistent screening (SCS) of polarizabilities and the calculation of the long-range correlation energy. It has been parametrized for the elements H-Ba, Hf-Rn, and for the functional PBE and PBE0. Note that the MBD\@rsSCS method depends on Hirshfeld charges. In calculating forces the dependence of the Hirshfeld charges on the actual geometry is neglected. The MBD method is implemented in case the BeckeGrid is used for the numerical integration. Example for PBE MBD\@rsSCS: 

::

  XC
    GGA PBE
    Dispersion MBD
  END

One can use user defined values with::

  XC
    Dispersion MBD {RSSCS|TS} {BETA=beta}
  END

``MBD {RSSCS|TS} {BETA=beta}``
  The default method for MBD is MBD\@rsSCS. Optionally one can use MBD\@TS or change the used parameter :math:`\beta` with setting beta. 



Post-SCF energy functionals
===========================


GGA energy functionals
----------------------

In principle you may specify different functionals to be used for the *potential,* which determines the self-consistent charge density, and for the *energy* expression that is used to evaluate the (XC part of the) energy of the charge density. To be consistent, one should generally apply the same functional to evaluate the potential and energy respectively. Two reasons, however, may lead one to do otherwise: 

+ The evaluation of the GGA part in the *potential* is more time-consuming than LDA. The effect of the GGA term in the potential on the self-consistent charge density is often not very large. From the point of view of computational efficiency it may, therefore, be attractive to solve the SCF equations at the LDA level (i.e. not including GGA terms in the potential), and to apply the full expression, including GGA terms, to the energy evaluation *a posteriori*: post-SCF.

+ A particular XC functional may have only an implementation for the potential, but not for the energy (or vice versa). This is a rather special case, intended primarily for fundamental research of Density Functional Theory, rather than for run-of-the-mill production runs.

One possibility is to calculate a whole list of post-SCF energy functionals using the METAGGA keyword, see next section. For some functionals the next possibility is enough. One has to specify different functionals for potential and energy evaluations respectively, using: 

::

  XC
   {LDA {Apply} LDA {Stoll}}
   {GGA {Apply} GGA}
  end

``Apply``
  States whether the functional defined on the pertaining line will be used self-consistently (in the SCF-potential), or only post-SCF, i.e. to evaluate the XC energy corresponding to the charge density. The value of apply must be SCF or Energy. A value postSCF will also be accepted and is equivalent to Energy. A value Potential will also be accepted and is equivalent to SCF. For each record separately the default (if no Apply value is given in that record) is SCF. For each of the two terms (LDA, GGA) in the functional: if no record with Energy specification is found in the data block, the evaluation of the XC energy will use the same functional as is applied for the potential. 

``LDA, GGA``
  See the XC potential section for all possible values. 


.. index:: hybrid functionals post SCF
.. index:: meta-GGA functionals 


Meta-GGA and hybrid energy functionals
--------------------------------------

The post SCF energy calculation is an easy and cheap way to get a reasonable guess for the bond energies for different XC functionals at the same time. Note that post-SCF energy calculations for a certain XC functional will not be so accurate if the functional form of the XC functional used in the SCF is very different from the XC functional used post SCF. The relative accuracy of post-SCF energies may not be so high if one looks at small energy differences. For accurate energy calculations it is recommended to use the same XC functional during the SCF as for the energy. 

The calculation of a large, pre-specified list of LDA, GGA, and meta-GGA energy functionals is invoked by specifying 

.. _keyscheme METAGGA: 


::

  METAGGA

as a separate keyword.  The following (incomplete) list gives an idea of the (meta-)GGA density functionals that will then be calculated
(the t-MGGA functional is the :math:`\theta`-MGGA functional of Ref. [#ref83]_):

::

  BP, PW91, mPW, BLYP, PBE, RPBE, revPBE, mPBE, OLYP, OPBE, KCIS, PKZB, VS98, FT97, BLAP3,
  HCTH, tau-HCTH, BmTau1, BOP, OLAP3, TPSS, KT1, KT2, B97, M06-L, t-MGGA.


The hybrid GGA and hybrid meta-GGA energy functionals are calculated if in addition to the METAGGA key, the key 

.. _keyscheme HARTREEFOCK: 

::

  HARTREEFOCK

is included. The following (incomplete) list gives an idea of the extra hybrid (meta-)GGA density functionals that will then be calculated::

  B3LYP, B3LYP*, B1LYP, KMLYP, O3LYP, X3LYP, BHandH, BHandHLYP, B1PW91, MPW1PW, MPW1K,
  PBE0, OPBE0, TPSSh, tau-HCTH-hybrid, B97, M05, M05-2X, M06, M06-2X.


The keys METAGGA and HARTREEFOCK can be used in combination with any XC potential. 
Note that at the moment hybrid functionals can not be used in combination with frozen cores. 
Also most METAGGA functionals will give wrong results if used in combination with frozen cores. 
Thus it is best to use an all electron basis set if one of the keywords METAGGA or HARTREEFOCK is used. One should include the ``HARTREEFOCK`` keyword also in the create runs of the atoms. In ADF the hybrid energies only make sense if the calculation is performed with completely filled orbitals (ROHF is not implemented in ADF, only UHF). 

The Examples document describes an application to the OH molecule for the METAGGA option. More output, on the total XC energy of the system, can be obtained by specifying 

::

  PRINT METAGGA

This latter option is intended for debugging purposes mainly and is not recommended for general use.  

The implementation calculates the total XC energy for a system and writes it to a file. This is always done in Create runs. If the basic fragments are atoms, the keyword 

.. _keyscheme ENERGYFRAG: 


::

  ENERGYFRAG
     ATOM [filename]
     ATOM [filename]
     ... ...
  END 

specifies that different atomic fragment files are to be used in the meta-GGA energy analysis than the regular atomic fragment files from the create runs. This keyword cannot be used for molecular fragment files. In order to compare meta-GGA energy differences between molecular fragments and the total molecule, results from the various calculations need to be combined by hand.  

In such situations, it is advisable to use a somewhat higher integration accuracy than one would normally do, at least for the smaller fragments, as there is no error cancellation as in a regular ADF bond energy analysis.  

A general comment is that some functionals show a more stable behavior than others (at least in our current implementation). In general, the functionals which are dependent on the Laplacian of the density may display a large variation with respect to basis set changes or different numerical integration accuracy. For this reason we currently recommend FT97 in favor of FT98. Similarly, the results with the BmTau1 functional should still be carefully checked. In our test calculations on the G2 set of molecules, the VS98 showed best performance, both for the average error and for the maximum error. The G2 set consists only of small molecules with elements up to Cl. The relative performance for transition metals and heavy elements is unknown and may well be very different from the ordering for the G2 set.  

.. index Hartree-Fock post SCF
.. index DC-DFT
.. index HF-DFT
.. index density corrected DFT

Post Hartree-Fock energy functionals
------------------------------------

This is mostly taken from text by the authors of Ref. [#ref84]_:
  In the early days of DFT, non-self-consistent Kohn-Sham energy was often evaluated upon Hartree-Fock (HF) densities as a way to test new approximations.
  This method was called HF-DFT.
  It has been discovered that in some cases, HF-DFT actually gave more accurate answers when compared to self-consistent DFT calculations.
  In Ref. [#ref84]_,
  it was found that DFT calculations can be categorized into two different types of calculations.
  The error of an approximate functional can be decomposed into two parts: error from the functional (functional error), and error from the density (density-driven error).
  For most calculations, functional error is dominant, and here self-consistent DFT is usually better than non-self consistent DFT on more accurate densities (called density corrected DFT (DC-DFT)).
  Unlike these 'normal' calculations, there is a class of calculations where the density-driven error is much larger, so DC-DFT give better a result than self-consistent DFT.
  These calculations can be classified as 'abnormal'.
  HF-DFT is a simple implementation of DC-DFT and a small HOMO-LUMO gap is an indicator of an 'abnormal' calculation, thus, HF-DFT would perform better in such cases.

In ADF one can do HF-DFT with:

::

  XC
    HartreeFock
  END
  MetaGGA

This will produce a large, pre-specified list of LDA, GGA, meta-GGA, hybrid, and metahybrid energy functionals.


.. only:: html

  .. rubric:: References

.. [#ref1] S.H. Vosko, L. Wilk and M. Nusair, *Accurate spin-dependent electron liquid correlation energies for local spin density calculations: a critical analysis*, `Canadian Journal of Physics 58 (8), 1200 (1980) <https://doi.org/10.1139/p80-159>`__ 

.. [#ref2] H.\  Stoll, C.M.E. Pavlidou, and H. Preuss, *On the calculation of correlation energies in the spin-density functional formalism*, `Theoretica Chimica Acta 49, 143 (1978) <https://doi.org/10.1007/BF00553794>`__ 

.. [#ref3] J.P. Perdew and Y. Wang, *Accurate and simple analytic representation of the electron-gas correlation energy*, `Physical Review B 45, 13244 (1992) <https://doi.org/10.1103/PhysRevB.45.13244>`__ 

.. [#ref4] M.\  Swart, A.W. Ehlers and K. Lammertsma, *Performance of the OPBE exchange-correlation functional*, `Molecular Physics 2004 102, 2467 (2004) <https://doi.org/10.1080/0026897042000275017>`__ 

.. [#ref5] X.\  Xu and W.A. Goddard III, *The X3LYP extended density functional for accurate descriptions of nonbond interactions, spin states, and thermochemical properties*, `Proceedings of the National Academy of Sciences 101, 2673 (2004) <https://doi.org/10.1073/pnas.0308730100>`__ 

.. [#ref6] M.\  Swart, *A new family of hybrid density functionals*, `Chemical Physics Letters 580, 166 (2013) <https://doi.org/10.1016/j.cplett.2013.06.045>`__ 

.. [#ref7] R.\  van Leeuwen and E.J. Baerends, *Exchange-correlation potential with correct asymptotic behavior*, `Physical Review A 49, 2421 (1994) <https://doi.org/10.1103/PhysRevA.49.2421>`__ 

.. [#ref8] T.W. Keal and D.J. Tozer, *The exchange-correlation potential in Kohn.Sham nuclear magnetic resonance shielding calculations*, `Journal of Chemical Physics 119, 3015 (2003) <https://doi.org/10.1063/1.1590634>`__ 

.. [#ref10] A.D. Becke, *Density-functional exchange-energy approximation with correct asymptotic behavior*, `Physical Review A 38, 3098 (1988) <https://doi.org/10.1103/PhysRevA.38.3098>`__ 

.. [#ref11] J.P. Perdew and Y. Wang, *Accurate and simple density functional for the electronic exchange energy: generalized gradient approximation*, `Physical Review B 33, 8822 (1986) <https://doi.org/10.1103/PhysRevB.33.8800>`__ 

.. [#ref12] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Sing and C. Fiolhais, *Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation*, `Physical Review B 46, 6671 (1992) <https://doi.org/10.1103/PhysRevB.46.6671>`__ 

.. [#ref13] C.\  Adamo and V. Barone, *Exchange functionals with improved long-range behavior and adiabatic connection methods without adjustable parameters: The mPW and mPW1PW models*, `Journal of Chemical Physics 108, 664 (1998) <https://doi.org/10.1063/1.475428>`__ 

.. [#ref14] J.P. Perdew, K. Burke and M. Ernzerhof, *Generalized Gradient Approximation Made Simple*, `Physical Review Letters 77, 3865 (1996) <https://doi.org/10.1103/PhysRevLett.77.3865>`__ 

.. [#ref15] B.\  Hammer, L.B. Hansen, and J.K. Norskøv, *Improved adsorption energetics within density-functional theory using revised Perdew-Burke-Ernzerhof functionals*, `Physical Review B 59, 7413 (1999) <https://doi.org/10.1103/PhysRevB.59.7413>`__ 

.. [#ref16] Y.\  Zhang and W. Yang, *Comment on "Generalized Gradient Approximation Made Simple"*, `Physical Review Letters 80, 890 (1998) <https://doi.org/10.1103/PhysRevLett.80.890>`__ 

.. [#ref17] C.\  Adamo and V. Barone, *Physically motivated density functionals with improved performances: The modified Perdew.Burke.Ernzerhof model*, `Journal of Chemical Physics 1996 116, 5933 (1996) <https://doi.org/10.1063/1.1458927>`__ 

.. [#ref18] J.P. Perdew, A. Ruzsinszky, G.I. Csonka, O.A. Vydrov, G.E. Scuseria, *Restoring the Density-Gradient Expansion for Exchange in Solids and Surfaces*, `Physical Review Letters 100, 136406 (2008) <https://doi.org/10.1103/PhysRevLett.100.136406>`__ 

.. [#ref19] Ph. Haas, F. Tran, P. Blaha, and K.H. Schwartz, *Construction of an optimal GGA functional for molecules and solids*, `Physical Review B83, 205117 (2011) <https://doi.org/10.1103/PhysRevB.83.205117>`__. 

.. [#ref20] N.C. Handy and A.J. Cohen, *Left-right correlation energy*, `Molecular Physics 99, 403 (2001) <https://doi.org/10.1080/00268970010018431>`__ 

.. [#ref21] J.J. Mortensen, K. Kaasbjerg, S.L. Frederiksen, J.K. Nørskov, J.P. Sethna, and K.W. Jacobsen, *Bayesian Error Estimation in Density-Functional Theory*, `Physical Review Letters 95, 216401 (2005) <https://doi.org/10.1103/PhysRevLett.95.216401>`__ 

.. [#ref22] J.P. Perdew, *Density-functional approximation for the correlation energy of the inhomogeneous electron gas*, `Physical Revied B 33, 8822 (1986) <https://doi.org/10.1103/PhysRevB.33.8822>`__ Erratum: J.P. Perdew, `Physical Review B 34, 7406 (1986) <https://doi.org/10.1103/PhysRevB.34.7406>`__ 

.. [#ref26] J.P. Perdew, A. Ruzsinszky, G.I. Csonka, L.A. Constantin, and J. Sun, *Workhorse Semilocal Density Functional for Condensed Matter Physics and Quantum Chemistry*, `Physical Review Letters 103, 026403 (2009) <https://doi.org/10.1103/PhysRevLett.103.026403>`__. 

.. [#ref27] J.\  Sun, J.P. Perdew, and A. Ruzsinszky, *Semilocal density functional obeying a strongly tightened bound for exchange*, `Proceedings of the National Academy of Sciences 112, 685 (2015) <https://doi.org/10.1073/pnas.1423145112>`__

.. [#ref28] J.\  Sun, B. Xiao, A. Ruzsinszky, *Communication: Effect of the orbital-overlap dependence in the meta generalized gradient approximation*, `Journal of Chemical Physics 137, 051101 (2012) <https://doi.org/10.1063/1.4742312>`__. 

.. [#ref29] J.\  Sun, R. Haunschild, B. Xiao, I.W. Bulik, G.E. Scuseria, J.P. Perdew, *Semilocal and hybrid meta-generalized gradient approximations based on the understanding of the kinetic-energy-density dependence*, `Journal of Chemical Physics 138, 044113 (2013) <https://doi.org/10.1063/1.4789414>`__. 

.. [#ref31] J.\  Sun, A. Ruzsinszky, J.P. Perdew, *Strongly Constrained and Appropriately Normed Semilocal Density Functional*, `Physical Review Letters 115, 036402 (2015) <https://doi.org/10.1103/PhysRevLett.115.036402>`__. 

.. [#ref32] P.J. Stephens, F.J. Devlin, C.F. Chabalowski and M.J. Frisch, *Ab Initio Calculation of Vibrational Absorption and Circular Dichroism Spectra Using Density Functional Force Fields*, `Journal of Physical Chemistry 98, 11623 (1994) <https://doi.org/10.1021/j100096a001>`__ 

.. [#ref33] M.\  Reiher, O. Salomon and B.A. Hess, *Reparameterization of hybrid functionals based on energy differences of states of different multiplicity*, `Theoretical Chemistry Accounts 107, 48 (2001) <https://doi.org/10.1007/s00214-001-0300-3>`__ 

.. [#ref34] C.\  Adamo and V. Barone, *Toward reliable adiabatic connection models free from adjustable parameters*, `Chemical Physics Letters 274, 242 (1997) <https://doi.org/10.1016/S0009-2614(97)00651-9>`__ 

.. [#ref35] J.K. Kang and C.B. Musgrave, *Prediction of transition state barriers and enthalpies of reaction by a new hybrid density-functional approximation*, `Journal of Chemical Physics 115, 11040 (2001) <https://doi.org/10.1063/1.1415079>`__ 

.. [#ref36] A.J. Cohen and N.C. Handy, *Dynamic correlation*, `Molecular Physics 99, 607 (2001) <https://doi.org/10.1080/00268970010023435>`__ 

.. [#ref40] B.J. Lynch, P.L. Fast, M. Harris and D.G. Truhlar, *Adiabatic Connection for Kinetics*, `Journal of Physical Chemistry A 104, 4811 (2000) <https://doi.org/10.1021/jp000497z>`__ 

.. [#ref41] S.\  Grimme, *Accurate description of van der Waals complexes by density functional theory including empirical corrections*, `Journal of Computational Chemistry 25, 1463 (2004) <https://doi.org/10.1002/jcc.20078>`__ 

.. [#ref42] M.\  Ernzerhof and G. Scuseria, *Assessment of the Perdew.Burke.Ernzerhof exchange-correlation functional*, `Journal of Chemical Physics 110, 5029 (1999) <https://doi.org/10.1063/1.478401>`__ 

.. [#ref45] M.\  Seth and T. Ziegler, *Range-Separated Exchange Functionals with Slater-Type Functions*, `Journal of Chemical Theory and Computation 8, 901 (2012) <https://doi.org/10.1021/ct300006h>`__ 

.. [#ref49] M.\  Grüning, O.V. Gritsenko, S.J.A. van Gisbergen and E.J. Baerends, *Shape corrections to exchange-correlation Kohn-Sham potentials by gradient-regulated seamless connection of model potentials for inner and outer region*, `Journal of Chemical Physics 114, 652 (2001) <https://doi.org/10.1063/1.1327260>`__ 

.. [#ref50] P.R.T. Schipper, O.V. Gritsenko, S.J.A. van Gisbergen and E.J. Baerends, *Molecular calculations of excitation energies and (hyper)polarizabilities with a statistical average of orbital model exchange-correlation potentials*, `Journal of Chemical Physics 112, 1344 (2000) <https://doi.org/10.1063/1.480688>`__ 

.. [#ref51] M.\  Grüning, O.V. Gritsenko, S.J.A. van Gisbergen and E.J. Baerends, *On the required shape correction to the LDA and GGA Kohn Sham potentials for molecular response calculations of (hyper)polarizabilities and excitation energies*, `Journal of Chemical Physics 116, 9591 (2002) <https://doi.org/10.1063/1.1476007>`__ 

.. [#ref52] O.V. Gritsenko, P.R.T. Schipper and E.J. Baerends, *Approximation of the exchange-correlation Kohn-Sham potential with a statistical average of different orbital model potentials*, `Chemical Physics Letters 302, 199 (1999) <https://doi.org/10.1016/S0009-2614(99)00128-1>`__ 

.. [#ref53] D.P. Chong, O.V. Gritsenko and E.J. Baerends, *Interpretation of the Kohn-Sham orbital energies as approximate vertical ionization potentials*, `Journal of Chemical Physics 116, 1760 (2002) <https://doi.org/10.1063/1.1430255>`__ 

.. [#ref58] R.\  Neumann, R.H. Nobes and N.C. Handy, *Exchange functionals and potentials*, `Molecular Physics 87, 1 (1996) <https://doi.org/10.1080/00268979600100011>`__ 

.. [#ref59] S.\  Ivanov, S. Hirata, R. J. Bartlett, *Exact Exchange Treatment for Molecules in Finite-Basis-Set Kohn-Sham Theory*, `Physical Review Letters 83, 5455 (1999) <https://doi.org/10.1103/PhysRevLett.83.5455>`__ 

.. [#ref60] A.F. Izmaylov, V.N. Staroverov, G.E. Scuseria, E.R. Davidson, G. Stoltz, E. Cancès, *The effective local potential method: Implementation for molecules and relation to approximate optimized effective potential techniques*, `Journal of Chemical Physics 126, 084107 (2007) <https://doi.org/10.1063/1.2434784>`__ 

.. [#ref61] M.\  Krykunov and T. Ziegler, *On the use of the exact exchange optimized effective potential method for static response properties*, `International Journal of Quantum Chemistry 109, 3246 (2009) <https://doi.org/10.1002/qua.21937>`__ 

.. [#ref62] U.\  Ekström, L. Visscher, R. Bast, A.J. Thorvaldsen, and K. Ruud, *Arbitrary-Order Density Functional Response Theory from Automatic Differentiation*, `Journal of Chemical Theory and Computation 6, 1971 (2010) <https://doi.org/10.1021/ct100117s>`__ 

.. [#ref63] M.A.L. Marques, M.J.T. Oliveira, and T. Burnus, *Libxc: a library of exchange and correlation functionals for density functional theory*, `Computer Physics Communications 183, 2272 (2012) <https://doi.org/10.1016/j.cpc.2012.05.007>`__ 

.. [#ref64] S.\  Lehtola, C. Steigemann, M.J.T. Oliveira, M.A.L. Marques, *Recent developments in LibXC -- A comprehensive library of functionals for density functional theory*, `SoftwareX 7, 1 (2018) <https://doi.org/10.1016/j.softx.2017.11.002>`__ 

.. [#ref65] E.\  Caldeweyher, S. Ehlert, A. Hansen, H. Neugebauer, S. Spicher, C. Bannwarth, S. Grimme, *A Generally Applicable Atomic-Charge Dependent London Dispersion Correction Scheme*, `ChemRxiv 7430216 v2 <https://doi.org/10.26434/chemrxiv.7430216>`__

.. [#ref66] S.\  Grimme, S. Ehrlich, and L. Goerigk, *Effect of the Damping Function in Dispersion Corrected Density Functional Theory*, `Journal of Computational Chemistry 32, 1457 (2011) <https://doi.org/10.1002/jcc.21759>`__. 

.. [#ref67] J.G. Brandenburg, J.E. Bates, J. Sun, and J.P. Perdew, *Benchmark tests of a strongly constrained semilocal functional with a long-range dispersion correction*, `Physical Review B 94, 115144 (2016) <https://doi.org/10.1103/PhysRevB.94.115144>`__. 

.. [#ref68] S.\  Grimme, J. Anthony, S. Ehrlich, and H. Krieg, *A consistent and accurate* ab initio *parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu*, `Journal of Chemical Physics 132, 154104 (2010) <https://doi.org/10.1063/1.3382344>`__. 

.. [#ref73] H.\  Kim, J.-M. Choi, W.A. Goddard, *Universal Correction of Density Functional Theory to Include London Dispersion (up to Lr, Element 103)*, `Journal of Physical Chemistry Letters 3, 360 (2012) <https://doi.org/10.1021/jz2016395>`__ 

.. [#ref74] A.\  Ambrosetti, A.M. Reilly, Robert A. DiStasio Jr., A. Tkatchenko, *Long-range correlation energy calculated from coupled atomic response functions*, `Journal of Chemical Physics 140, 18A508 (2014) <https://doi.org/10.1063/1.4865104>`__ 

.. [#ref72] S.N. Steinmann, and C. Corminboeuf, *Comprehensive Benchmarking of a Density-Dependent Dispersion Correction*, `Journal of Chemical Theory and Computation 7, 3567 (2011) <https://doi.org/10.1021/ct200602x>`__. 

.. [#ref81] A.\  Tkatchenko, R.A. DiStasio Jr., R. Car, M. Scheffler *Accurate and Efficient Method for Many-Body van der Waals Interactions*, `Physical Review Letters 108, 236402 (2012) <https://doi.org/10.1103/PhysRevLett.108.236402>`__ 

.. [#ref83] P.\  de Silva and C. Corminboeuf, *Communication: A new class of non-empirical explicit density functionals on the third rung of Jacob's ladder*, `Journal of Chemical Physics 143, 111105 (2015) <https://doi.org/10.1063/1.4931628>`__ 

.. [#ref84] M.-C. Kim, E. Sim, and K. Burke, *Understanding and Reducing Errors in Density Functional Calculations*, `Physical Review Letters 111, 2073003 (2013) <https://doi.org/10.1103/PhysRevLett.111.073003>`__ 

.. [#ref85] Y.\  Zhao and D.G. Truhlar, *A new local density functional for main-group thermochemistry, transition metal bonding, thermochemical kinetics, and noncovalent interactions*, `Journal of Chemical Physics 125, 194101 (2006) <https://doi.org/10.1063/1.2370993>`__ 

.. [#ref86] Y.\  Zhao and D.G. Truhlar, *The M06 suite of density functionals for main group thermochemistry, thermochemical kinetics, noncovalent interactions, excited states, and transition elements: two new functionals and systematic testing of four M06-class functionals and 12 other functionals*, `Theoretical Chemical Accounts 120, 215 (2008) <https://doi.org/10.1007/s00214-007-0310-x>`__ 

.. [#ref87] J.\  Tao, J.P. Perdew, V.N. Staroverov and G.E. Scuseria, *Climbing the Density Functional Ladder: Nonempirical MetaGeneralized Gradient Approximation Designed for Molecules and Solids* `Physical Review Letters 91, 146401 (2003) <https://doi.org/10.1103/PhysRevLett.91.146401>`__ 

.. [#ref88] V.N. Staroverov, G.E. Scuseria, J. Tao and J.P. Perdew, *Comparative assessment of a new non empirical density functional: Molecules and hydrogen-bonded complexes* `Journal of Chemical Physics 119, 12129 (2003) <https://doi.org/10.1063/1.1626543>`__ 

.. [#ref89] M.\  Swart, M. Solà and F.M. Bickelhaupt, *A new all-round DFT functional based on spin states and SN2 barriers*, `Journal of Chemical Physics 131, 094103 (2009) <https://doi.org/10.1063/1.3213193>`__ 

.. [#ref90] M.\  Swart, M. Solà and F.M. Bickelhaupt, *Switching between OPTX and PBE exchange functionals*, `Journal of Computational Methods in Science and Engineering 9, 69 (2009) <https://doi.org/10.3233/JCM-2009-0230>`__ 

.. [#ref91] C.\  Lee, W. Yang and R.G. Parr, *Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density*, `Physical Review B 37, 785 (1988) <https://doi.org/10.1103/PhysRevB.37.785>`__ 

.. [#ref92] B.G. Johnson, P.M.W. Gill and J.A. Pople, *The performance of a family of density functional methods*, `Journal of Chemical Physics 98, 5612 (1993) <https://doi.org/10.1063/1.464906>`__ 

.. [#ref93] T.V. Russo, R.L. Martin and P.J. Hay, *Density Functional calculations on first-row transition metals*, `Journal of Chemical Physics 101, 7729 (1994) <https://doi.org/10.1063/1.468265>`__ 

.. [#ref94] S.\  Grimme, , J. Antony, T. Schwabe and C. Mück-Lichtenfeld, *Density Functional Theory with Dispersion Corrections for Supramolecular Structures, Aggregates, and Complexes of (Bio)Organic Molecules*, `Organic & Biomolecular Chemistry 5, 741 (2007) <https://doi.org/10.1039/B615319B>`__ 

.. [#ref95] S.\  Grimme, *Semiempirical hybrid density functional with perturbative second-order* `J. Chem. Phys. 2006, 124, 034108 <https://doi.org/10.1063/1.2148954>`__

.. [#ref96] A. Förster, L. Visscher, *Double hybrid DFT calculations with Slater type orbitals*, `Journal of Computational Chemistry 41 1660–1684 (2020) <https://doi.org/10.1002/jcc.26209>`__

.. [#ref97] Js. Garcia, E. Bremond, M. Savarese, AJ. Perez-Gimenez, C. Adamo, *Partnering dispersion corrections with modern parameter-free double-hybrid density functionals* `Phys. Chem. Chem. Phys., 19, 13481 (2017) <https://doi.org/10.1021/acs.jctc.8b01203>`__

.. [#ref98] G.\  Santra, N. Sylvetsky, and J.M.L. Martin, *Minimally Empirical Double-Hybrid Functionals Trained against the GMTKN55 Database: revDSD-PBEP86-D4 revDOD-PBE-D4, and DOD-SCAN-D4* `J. Chem. Phys. 2019, 123, 5129 <https://doi.org/10.1021/acs.jpca.9b03157>`__

.. [#ref99] J.C. Sancho-García, A.J. Pérez-Jiménez, *Assessment of double-hybrid energy functionals for PI-conjugated systems* `J. Chem. Phys. 2009, 131, 084108 <https://doi.org/10.1063/1.3212881>`__

.. [#ref100] D.C. Graham, A.S. Menon, L. Goerigk, S. Grimme, L. Radom *Optimization and basis-set dependence of a restricted-open-shell form of B2-PLYP double-hybrid density functional theory* `J. Phys. Chem. A 2009, 113, 9861 <https://doi.org/10.1021/jp9042864>`__

.. [#ref101] A.\  Tarnopolsky, A. Karton, R. Sertchook, D. Vuzman, J.M.L Martin, *Double-hybrid functionals for thermochemical kinetics* `J. Phys. Chem. A 2008, 112, 3 <https://doi.org/10.1021/jp710179r>`__

.. [#ref102] A.\  Karton, A. Tarnopolsky, J.F. Lamere, G.C. Schatz, J.M.L, Martin, *Highly accurate first-principles bench- mark data sets for the parametrization and validation of density functional and other approximate methods. Derivation of a robust, generally applicable, double-hybrid functional or thermochemistry and thermochemical kinetics.* `J. Phys. Chem. A 2008, 112, 12868 <https://doi.org/10.1021/jp801805p>`__

.. [#ref103] Y.\  Feng, *Double-Hybrid Density Functionals Free of Dispersion and Counterpoise Corrections for Non-Covalent Interactions* `J. Phys. Chem. A 2014, 118, 3175 <https://doi.org/10.1021/jp5005506>`__

.. [#ref104] T.\  Schwabe, S. Grimme, *Towards chemical accuracy for the thermodynamics of large molecules: new hybrid density functionals including non-local correlation effects.* `Phys. Chem. Chem. Phys. 2006, 8, 4398 <https://doi.org/10.1039/B608478H>`__

.. [#ref105] K.\  Sharkas, J. Toulouse, A. Savin, *Double-hybrid density-functional theory made rigorous* `J. Chem. Phys. 2011, 134, 064113 <https://doi.org/10.1063/1.3544215>`__

.. [#ref106] E.\  Bremond, C. Adamo, *Seeking for parameter-free double-hybrid functionals: The PBE0-DH model* `J. Chem. Phys. 2011, 135, 024106 <https://doi.org/10.1063/1.3604569>`__

.. [#ref107] J.\  Toulouse, K. Sharkas, E. Bremond, C. Adamo, *Rationale for a new class of double-hybrid approximations* `J. Chem. Phys.  2011, 135, 101102 <https://doi.org/10.1063/1.3640019>`__

.. [#ref108] J.D. Chai, S.P. Mao, *Seeking for reliable double-hybrid density functionals without fitting parameters: the PBE0-2 functional* `Chem. Phys. Lett. 2012, 538, 121 <https://doi.org/10.1016/j.cplett.2012.04.045>`__

.. [#ref109] S.O. Souvi, K. Sharkas and J. Toulouse, *Double-hybrid density functional theory with meta-generalized gradient approximations* `J. Chem. Phys. 2014, 140, 084107 <https://doi.org/10.1016/j.cplett.2012.04.045>`__

.. [#ref110] S.\  Kozuch, D. Gruzman, J.M.L. Martin, *DSD-BLYP: a general purpose double hybrid density functional including spin component scaling and dispersion correction* `J. Phys. Chem. C 2010, 114, 20801 <https://doi.org/10.1021/jp1070852>`__

.. [#ref111] S.\  Kozuch, J.M.L. Martin, *DSD-PBEP86: In search of the best double-hybrid DFT with spin-component scaled MP2 and dispersion corrections* `Phys. Chem. Chem. Phys. 2011, 13, 20104 <https://doi.org/10.1039/C1CP22592H>`__

.. [#ref113] Y.\  Jung, R.C. Lochan, A. D. Dutoi, M. Head-Gordon, *Scaled opposite-spin second order Møller-plesset correlation energy: An economical electronic structure method.* `Journal of Chemical Physics 2004, 121, 9793 <https://doi.org/10.1063/1.1809602>`__

.. [#ref114] S.\  Grimme, *Improved  second-order  Møller-Plesset  perturbation  theory  by  separate scaling of parallel- and antiparallel-spin pair correlation energies.* `Journal of Chemical Physics 2003, 118, 9095 <https://doi.org/10.1063/1.1569242>`__

.. [#ref115] R.C. Lochan, Y. Jung, M. Head-Gordon, *Scaled opposite spin second order Møller-Plesset theory with improved physical description of long-range dispersion interactions* `Journal of Physical Chemistry A2005,109, 7598 <https://doi.org/10.1021/jp0514426>`__

.. [#ref116] J.\  Proppe, S. Guglerb and M. Reiher, *Gaussian Process-Based Refinement of Dispersion Corrections* `<https://arxiv.org/pdf/1906.09342.pdf>`__

.. [#ref117] A.\  Förster, M. Franchini, E. van Lenthe, L. Visscher, *A Quadratic Pair Atomic Resolution of the Identity Based SOS-AO-MP2 Algorithm Using Slater Type Orbitals*, `Journal of Chemical Theory and Computation 16, 875 (2020) <https://doi.org/10.1021/acs.jctc.9b00854>`__
