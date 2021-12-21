.. index:: GW
.. index:: G0W0

.. _GWscheme:

GW
**

General
=======

This page describes the basic procedure, usage and scope of a GW calculation. Technical details of the algorithm can be tweaked in the :ref:`MBPT input block <keyscheme MBPT>`. Note, that evGW and |evGW0| calculations are only available in AMS2021.1. |G0W0| is also available in AMS2020.

.. seealso::
  `Tutorial: Accurate Ionization Potential and Electron Affinity with G0W0  <../../Tutorials/OpticalPropertiesElectronicExcitations/GW.html>`_

  :ref:`example GW_H2O`, :ref:`example GW_Phenol`, :ref:`example GW_O3` and :ref:`example evGW_H2O`

The GW method is a relatively accurate method to obtain information about so-called charged excitations, or single-particle excitations. We refer to them as Quasiparticle energies. These are especially important to interpret and predict the outcome of direct and inverse photo-emission spectroscopy and can be used to obtain e.g. very accurate ionization potentials and electron affinities which gives access to the so-called fundamental gap (not to be confused with the optical gap).

GW can be used icw scalar relativistic effects within the ``ZORA``, ``X2C``, or ``RA-X2C`` formalism, but can not be used icw spin-orbit coupling.

In practice, fully self-consistent GW is rarely used for molecular systems. Instead, perturbative approximations, so called quasiparticle GW methods are used since they are cheaper and also more accurate than fully self-consistent GW. The most popular approach is |G0W0| [#arnoGW]_, in which quasiparticle energies are obtained as a one-shot perturbative correction to KS eigenvalues. A downside of this approach is the rather pronounced starting-point dependence. This can be overcome to a large extent in eigenvalue-only self-consistent GW (evGW), in which the quasiparticle energies (but not the density) are iteratively updated until self-consistency is reached. In quasiparticle self-consistent GW, also the density is updated in each iteration, so that the results become completely starting point independent. The partially self-consistent GW variants usually converge within 6-12 iterations which make these approaches a factor of 6 to 12 more expensive than |G0W0|.

A GW calculation as implemented in ADF proceeds in five steps as has been described in detail in a series of papers [#arnoGW]_ [#ref4]_ [#ref5]_. The technique is also known as the as GW space-time method. Our implementation is closely related to the scheme outlined in [#ref3]_. 

* A DFT single-point calculation is performed. This can be an LDA, GGA or hybrid calculation. At the moment, ADF does not support the use of XCfun, but libXC is supported. Valid choices could be LDA, PBE, BLYP, PBE0, BHandHLYP and many more. The default is LDA. As usual, the functional to be used during the SCF is requested in the :ref:`XC input block <keyscheme XC>` block. The following requests a |G0W0| calculation with default settings using a PBE reference:: 

    XC
       GGA PBE
    END  

    GW
    End 

* From the KS orbitals and orbital energies, a Green's function (G) is evaluated and from the Green's function the so-called independent-particle polarizability is calculated. This is done in imaginary time.

* The polarizability is Fourier transformed to the imaginary frequency axis where the screened Coulomb potential (W) is evaluated using the Coulomb potential and the polarizability.

* The screened Coulomb potential is Fourier transformed to imaginary time. Here, the self-energy is calculated using G and W (that why it is called GW) which gives access to spectroscopic properties. 

* The self-energy is transformed to the molecular orbital basis from where it is Fourier transformed to the imaginary frequency axis from where it is analytically continued to the complex plane. Along the real frequency axis, the quasiparticle energies are evaluated.

* In case of evGW (|evGW0|), the input KS eigenvalues are replaced by the quasiparticle energies from the previous iteration and the scheme is iterated until self-consistency in the quasiparticle energies is reached.

* In case of qsGW (|qsGW0|), A non-local, hermitian, and static exchange-correlation potential is constructed from the self-energy. This exchange-correlation potential replaces the KS exchange-correlation potential. Diagonalization gives a new set of single-particle orbitals and quasiparticle energies. The procedure is repeated until self-consistency is reached.

* By default, the DIIS algorithm is used to accelerate and stabilize convergence of the self-consistent GW schemes. A linear-mixing scheme can also be used.

The GW space-time method has the distinct advantage that it can be very fast, while a full frequency, conventional GW calculation scales to the 6th power of the system size and is prohibitive for systems larger than a few tens of atoms. ADF used advanced density fitting options to accelerate the space-time method further and in practice nearly quadratic scaling can be reached. This enables the routine application of the method to systems of several hundreds of atoms. A |G0W0| calculation (without the preceding SCF) is usually not much slower than a hybrid calculation. The downside of the approach is that the analytical continuation technique produces large errors (up to several eV) for core states which are in example important in X-ray spectroscopy. Thus, the GW implementation in ADF should only be used to predict quasiparticle energies for states in the valence-region. In fact, we have only tested it for HOMO and LUMO states (which are arguably most important)

The states of interest can be requested in the GW block

::

    GW
      nStates 5
    End 

is the default and calculates 5 occupied and five unoccupied states.

:: 

    GW
      nStates 1
    End 

calculates the HOMO and LUMO quasiparticle energy only.

Levels of self-consistency
==========================

Eigenvalue-only self-consistent GW
----------------------------------

An evGW calculation is requested by 

:: 

    GW
      SelfConsistency evGW 
    End 

One can also only iterate G by keep W fixed which reduces the cost of each iteration by roughly 50 %. This is requested by 

:: 

    GW
      SelfConsistency evGW0 
    End 

On the other hand, much of the starting point dependence of the |G0W0| method remains in the |evGW0| method and it is generally not recommended. 

quasiparticle self-consistent GW
--------------------------------

An qsGW calculation is requested by 

:: 

    GW
      SelfConsistency qsGW 
    End 

One can also only iterate G by keep W fixed which reduces the cost of each iteration by roughly 50 %. This is requested by 

:: 

    GW
      SelfConsistency qsGW0 
    End 

On the other hand, much of the starting point dependence of the |G0W0| method remains in the |qsGW0| method and it is generally not recommended. 

More options:

``QPHamiltonian``
   In quasiparticle self-consistent GW, the frequency-dependent self-energy is mapped to a static exchange-correlation in each iteration. The mapping is not unique and different schemes have been suggested. They differ in the way the frequency dependence of the self-energy is treated. In ADF, three variants can be used. KSF1 and KSF2 are from the paper by Kotani et al. [#ref6]_. KSF1 refers to eq. 10 therein and is most commonly implemented, KSF2 refers to eq. 11 therein. KSF2 is the default in ADF since it is numerically more stable. The variant denoted as Kutepov has been suggested bu Kutepov et al. [#ref7]_ and uses a first-order expansion around the chemical potential. 

``FixedGrids``
   Per default, the imaginary frequency and imaginary time grids used in the GW calculation are updated in each iteration in a qsGW calculation since this is necessary to make the results strictly starting point dependent. This can also be turned off, and fixed grids are used throughout. This might be helpful in case of convergence problems. 

Convergence
-----------

The self-consistency can be controlled by a few parameters: For example

:: 

    GW
      Converge HOMO=5e-3
    End 

requests that the evGW(0) calculation is considered converged if the difference between the HOMO quasiparticle energies of 2 consecutive iterations does not change by more than 5 meV. The default is 1 meV which is in practice usually a little too tight. We recommend to adjust this parameter according to your requirements, for example the experimental resolution you would like to match.

For qsGW (|qsGW0|), the change in the norm of the density matrix is used as an additional criterion to control convergence. In evGW (|evGW0|) it is ignored.

:: 

    GW
      Converge Density=1e-07
    End 

is the default. For very large systems and when QZ basis sets are used, it is recommended to decrease that value, for example to 

:: 

    GW
      Converge Density=1e-08
    End 


:: 

    GW
      linearmixing 0.2
    End 

turns of DIIS and request to use linear mixing instead with a mixing parameter of 0.2. This can be useful if for some reason, convergence using DIIS cannot be achieved. However, it is usually better to adjust the number of vectors in the DIIS expansion. This is achieved by (for example) 

:: 

    GW
      DIIS 5
    End 

The default are 10 expansion vectors. 

Second-order self-energy
========================

Starting from ADF2022, it is possible to go beyond the GW approximation for the self-energy (expansion in screened interaction to first order) and also take into account the next term (expansion in the screened interaction to second order). 

* This can be used with all variants of self-consistency.  

* The second-order self-energy is always applied as a perturbative correction of the GW quasiparticle energies, using a statically screened interaction W. More precisely, 

.. math::

    \Sigma^{GW} = G(\omega) * W (\omega) 

.. math::

    \Sigma^{GW+G3W2} = G(\omega) * W(\omega) + G(\omega) * W (\omega = 0) * G(\omega) * G(\omega) * W (\omega = 0) 

* The second-order self-energy is activated by typing 

:: 

    GW
      selfenergy G3W2
    End 

* It has been shown that the second-order correction is especially accurate for electron affinities and HOMO-LUMO gaps. Since it effectively scales as the fourth power of the system size, it should not be used for systems much larger than 100 atoms. 

* It is often useful, to take the average results of a GW and a GW+G3W2 calculation, i.e. to only include 50 % of the second-order correction. Using qsGW or range-separated hybrids as starting points, this is one of the most accurate methods for the calculation of quasiparticle energies.   

Recommendations
===============

Basis sets
----------


The recommended numerical settings depend strongly on the basis set. The recommended basis set depends on system size and the property of interest. The following are recommendations:

**Basis sets**

| **All-electron:**  All-electron calculations are always recommended.
| **Basis set size:** Larger basis sets are needed to achieve the same accuracy as in a DFT calculation
| **Augmented basis sets:** Should only be used if absolutely necessary. They are however often necessary for an accurate description of the electron affinity for molecules with LUMO above the vacuum level.

| **Ionization Potentials:** TZ2P or larger
| **Electron affinities, bound LUMO:** Corr/TZ3P or larger
| **Electron affinities, unbound LUMO:** AUG/ATZ2P or larger
| **Fundamental Gap, bound LUMO:** AUG/ADZP and TZ2P for larger systems. 
| **Fundamental Gap, unbound LUMO:** AUG/ATZ2P or larger

For **highly accurate results** we recommend to perform an extrapolation to the complete basis set limit: For this, perform 2 calculations using the Corr/TZ3P and Corr/QZ6P. The basis set limit is then calculated according to

.. math::

    \epsilon_n^{CBS} = \epsilon_n^{QZ} -  \frac{1}{N^{QZ}_{bas} }\frac{\epsilon_n^{QZ} - \epsilon_n^{TZ}}{\frac{1}{N^{QZ}_{bas}} - \frac{1}{N^{TZ}_{bas}}} 

The values for :math:`N^{TZ}_{bas}` and :math:`N^{QZ}_{bas}` can be found in the adf.log file in the ``GW`` section under the entry ``nBas``.

Numerical aspects
-----------------

* According to the choice of basis set, the recommended numerical settings can differ. For a discussion, see the :ref:`MBPT page<keyscheme MBPT>`. 

* qsGW has the highest requirements on the numerical parameters than evGW and |G0W0|. Usually, it is necessary to use a larger value in the ``Dependency`` key, see the :ref:`MBPT page<keyscheme MBPT>`.

* The implemented GW algorithm is very sensitive to numerical noise and depending on the numerical settings and/or the underlying exchange-correlation functional, (occupied) quasiparticle energies from partially self-consistent GW calculations performed on different hardware can differ by a few meV. The discrepancies are generally more pronounced for core states for which the analytical continuation technique is rather inaccurate.

* In our experience, these differences only occur with large basis sets (QZ4P or larger) and when Minnesota functionals (we tested M06, M06-2X and M06-HF) are used to calculate the KS reference. When the DIIS algorithm is used to converge the quasiparticle energies, the number of iterations needed for convergence can then differ as well. 

* For optimal accuracy, full cores should be used. Note, that frozen cores do not require in large computational savings for GW calculations. 

Choosing the KS reference
-------------------------

* As for ground-state properties, it is far from trivial to recommend a universal functional. However, for |G0W0| calculations, a few general guidelines can be offered. A good discussion is found in [#ref1]_. It should be noted, that GGA functional should not be used, even though a PBE starting point is a popular choice. We rather recommend to use a hybrid functional. The relevant parameter in the choice of the hybrid is usually the fraction of exact exchange. In our experience, PBE0 with 40-50 % exact exchange is a good choice. You might also use a range-separated hybrid via LibXC, for example LRC-wPBEH. 

* If in doubt, one of the partially self-consistent schemes should be used. evGW is almost starting point independent and qsGW is completely starting point independent. Therefore, for qsGW, it is in principle irrelevant what starting point is chosen. Convergence properties can in principle be affected, although the number of iterations until convergence is reached is also more or less independent of the starting point [#ref5]_. Also for evGW, starting from a hybrid functional or a range-separated usually results in the highest accuracy.


Troubleshooting
---------------

* You see the following warning in the output: `` Warning: no convergence in non-uniform Fourier transform for at least one frequency point.``: This could mean that something is wrong with the imaginary frequency integration but most likely it can be ignored. If you want to be sure, repeat your calculation with a smaller frequency grid. 

* You see that some virtual quasiparticle energies (LUMO-X) have very large shifts which are not consistent with the other shifts or the GW correction to some KS eigenvalues is exactly zero: This indicates numerical problems. Usually you will need to adjust the ``Dependency`` key to a larger value or you need to increase the numerical quality,

GW key
======

.. _keyscheme GW:

.. scmautodoc:: adf GW nStates SelfEnergy SelfConsistency QPHamiltonian nIterations Converge FixedGrids LinearMixing DIIS


.. only:: html

  .. rubric:: References

.. [#arnoGW] Arno Förster, Lucas Visscher, *Low-order scaling G0W0 by pair atomic density fitting*, `Journal of Chemical Theory and Computation 16 (12), 7381–7399 (2020) <https://doi.org/10.1021/acs.jctc.0c00693>`__ 

.. [#ref1] F.\  Bruneval, M.A.L., Marques, *Benchmarking the starting points of the GW approximation for molecules*, `Journal of Chemical Theory and Computation 9 (1), 324-329 (2013) <https://dx.doi.org/10.1021/ct300835h>`__ 

.. [#ref2] M.J. Van Setten, F. Caruso S. Sharifzadeh X. Ren M. Scheffler F. Liu J. Lischner L. Lin J. Deslippe S.G. Louie C. Yang F. Weigend J.B. Neaton F. Evers P. Rinke, *GW100: Benchmarking G0W0 for Molecular Systems*, `Journal of Chemical Theory and Computation 11 (12), 5665-5687 (2015) <https://doi.org/10.1021/acs.jctc.5b00453>`__

.. [#ref3] J.\  Wilhelm, D. Golze, L. Talirz, J. Hutter, C.A. Pignedoli, *Toward GW Calculations on Thousands of Atoms*, `Journal of Physical Chemistry Letters 9 (2), 306-312 (2012) <https://doi.org/10.1021/acs.jpclett.7b02740>`__

.. [#ref4] Arno Förster, Lucas Visscher, *GW100: A Slater-Type Orbital Perspective*, `Journal of Chemical Theory and Computation 17 (8), 5080–5097 (2021) <https://doi.org/10.1021/acs.jctc.1c00308>`__

.. [#ref5] Arno Förster, Lucas Visscher, *Low-Order Scaling Quasiparticle Self-Consistent GW for Molecules*, `frontiers in Chemistry 9, 736591 (2021) <https://doi.org/10.3389/fchem.2021.736591>`__

.. [#ref6] A.L. Kutepov, V.S. Oudovenko, G. Kotliar, *Linearized self-consistent quasiparticle GW method: Application to semiconductors and simple metals*, `Computer Physics Communications 407-414 (2017) <http://dx.doi.org/10.1016/j.cpc.2017.06.012>`__

.. [#ref7] Takao Kotani, Mark Van Schilfgaarde, Sergey V. Faleev, *Quasiparticle self-consistent GW method: A basis for the independent-particle approximation*, `Physical Review B 76 (16) 1-24 (2007) <https://doi.org/10.1103/PhysRevB.76.165106>`__


.. |G0W0| replace:: G\ :sub:`0`\ W\ :sub:`0`
.. |GW0| replace:: GW\ :sub:`0`
.. |evGW0| replace:: evGW\ :sub:`0`
.. |qsGW0| replace:: qsGW\ :sub:`0`

