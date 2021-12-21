
Vibrational Spectroscopy
************************

See the `Vibrational Spectroscopy section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html>`__.

.. _IR:

IR frequencies and normal modes
===============================

.. index:: IR frequencies 
.. index:: infrared frequencies 
.. index:: infrared intensities 
.. index:: frequencies 
.. index:: analytic second derivatives 
.. index:: Hessian 
.. index:: force constants 
.. index:: partial Hessian
.. index:: Mobile Block Hessian 
.. index:: MBH 
.. index:: thermodynamics 
.. index:: isotope shift 
.. index:: frequency scan 
.. index:: moments of inertia 

See the `IR frequencies and normal modes section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html#ir-frequencies-and-normal-modes>`__.

The Hessian that is needed can be calculated numerically or analytically. This can be set in the AMS part of the input.

::

   $ADFBIN/ams <<eor
      NormalModes
         Hessian [Auto | Analytical | Numerical]
      End
      ...
   eor

Analytical Hessian
------------------

The analytical second derivatives (Hessian) implementation in ADF is based on Ref. [#ref3]_ [#ref4]_ [#ref5]_. 
The analytical Hessian is as accurate as the numerical Hessian for the same integration accuracy, but can be up to 3 to 5 times quicker to compute, depending on the molecule, integration grid parameters, and choice of basis set. Using the analytical Hessian AMS will calculate the vibrational frequencies and normal modes.

.. warning::

   In previous versions ADF2006-ADF2020 contained a bug for analytical frequencies calculations of spin polarized molecules using PBEc.

**Bug PBEc** The bug for analytical frequencies calculations of spin-polarized molecules using PBEc affects calculations with the exchange-correlation functionals PBE, OPBE, RPBE, revPBE, and S12g. This bug was introduced in ADF2006 and fixed in AMS2020.103.
Analytical frequencies using LibXC were not affected.
Workaround for older versions is to use numerical frequencies.
For AMS2020 one should use AMS2020.103 or later.
For ADF2019.3 one should use ADF2019.307.

Calculating the analytical Hessian requires the solution of the Coupled Perturbed Kohn-Sham (CPKS) equations, which is an iterative process. This part of the process is of order 3 x *number of atoms*, and is generally the main bottle neck in calculating the frequencies. The immediate result of the solution of the CPKS equations is the U1 matrix, the components of which are closely related to the derivatives of the MO coefficients. One of the adjustable parameters in the input of an analytical frequencies calculation can be used to control the accuracy of the U1 matrix components.

One disadvantage in calculating analytical Hessian is that the range of exchange-correlation functionals is limited. This is because derivative formulas have to be derived for each exchange-correlation functional in ADF, which is not an straight forward task. Here are the currently available functionals: 

**LDA:** XONLY, VWN, STOLL, PW92    

**Exchange GGA:** Becke88, OPTx, PBEx, rPBEx, revPBEx, S12g

**Correlation GGA:** LYP, Perdew86, PBEc    

**XC GGA shortcuts:** BP86, PBE, RPBE, revPBE, BLYP, OLYP, OPBE 

Any functional not mentioned above is not implemented, including PW91 and Hartree-Fock. 

**A note of caution**: For accurate frequencies it is especially important to also have an accurately optimized geometry. During a geometry optimization the integration accuracy is set by  default to "Normal", and so the resulting frequencies will also have this level  of integration accuracy while it may be desirable to have frequencies computed with a higher  accuracy. One might consider using Good NumericalQuality (or BeckeGrid quality) and set the convergence criteria for the geometry optimization tighter. 

.. scmautodoc:: adf AnalyticalFreq

.. [#ref3] A.\  Bérces, R. M. Dickson, L. Fan, H. Jacobsen, D. Swerhone and T. Ziegler, *An implementation of the coupled perturbed Kohn-Sham equations: perturbation due to nuclear displacements*, `Computer Physics Communications 100, 247 (1997) <https://doi.org/10.1016/S0010-4655(96)00120-8>`__ 

.. [#ref4] H.\  Jacobsen, A. Bérces, D. Swerhone and T. Ziegler, *Analytic second derivatives of molecular energies: a density functional implementation*, `Computer Physics Communications 100, 263 (1997) <https://doi.org/10.1016/S0010-4655(96)00119-1>`__ 

.. [#ref5] S.K. Wolff, *Analytical second derivatives in the Amsterdam density functional package*, `International Journal of Quantum Chemistry 104, 645 (2005) <https://doi.org/10.1002/qua.20653>`__ 


(Resonance) Raman
=================

.. _Raman:

.. index:: Raman scattering 
.. index:: Raman intensities 
.. index:: Raman for selected frequencies 
.. index:: Raman (resonance) 
.. index:: resonance Raman

See the `(Resonance) Raman section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html#resonance-raman>`__.

For Raman calculations by default AORESPONSE will be used to calculate the frequency-dependent polarizability.
To use RESPONSE instead of AORESPONSE include the RESPONSE block key in the Engine ADF part of the input:

::

   Engine ADF
     Response
     End
   EndEngine

VROA: (Resonance) vibrational Raman optical activity
====================================================

.. _VROA:

.. index:: VROA 
.. index:: vibrational Raman optical activity 

See the `VROA section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html#vroa-resonance-vibrational-raman-optical-activity>`__.


VCD: Vibrational Circular Dichroism
===================================

.. _VCD:

.. index:: VCD 
.. index:: vibrational circular dichroism

New in AMS2020 is that one can calculate VCD also for open-shell systems in a spin-unrestricted calculation.

See the `VCD section of the AMS manual <../../AMS/Vibrational_Spectroscopy.html#vcd-vibrational-circular-dichroism>`__.

