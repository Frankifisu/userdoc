.. _ModelHamiltonians:

Model Hamiltonians
##################

As of the 2020 release, the DFTB engine supports two different classes of model Hamiltonians, Grimme's extended tight-binding, and the classic Slater-Koster based DFTB. All of these model Hamiltonians are obtained by applying tight-binding approximations to the DFT total energy expression.

.. index:: Slater-Koster based DFTB

Slater-Koster based DFTB
************************

The efficiency of Slater-Koster based DFTB stems from its use of an optimized minimum valence orbital basis that reduces the linear algebra operations, and a two center-approximation for the Kohn-Sham potential that allows precalculation and storage of integrals using the Slater-Koster technique. This makes DFTB orders of magnitude faster than DFT, but requires parameter files (containing the integrals) for all pair-wise combinations of atoms in a molecule. Many elements can be handled with the parameter sets included in the distribution. Alternatively, sets of parameters in the SKF format can be downloaded and used from third party sources.

There are three flavors of Slater-Koster based DFTB available in our implementation:

* The "plain" DFTB Hamiltonian as introduced by Porezag and Seifert without a self-consistency cycle.

* The second order self-consistent charge extension SCC-DFTB (recently also called DFTB2), which accounts for density fluctuations and improves results on polar bonds. Note that the self-consistent calculations is about an order of magnitude slower than calculations with the "plain" DFTB Hamiltonian.

* The third order extension known as DFTB3, which improve the description of hydrogen-bonded complexes and proton affinities. Note that DFTB3 calculations are only marginally slower than SCC-DFTB based calculations.

Note that since these methods have been respectively parametrized, it is important to specify a matching parameter set when applying one of these models.

.. index:: xTB
.. index:: GFN-xTB

Extended tight-binding (xTB)
****************************

The extended tight-binding (xTB) model Hamiltonian as recently been introduced by Grimme and coworkers. It makes similar approximations as Slater-Koster based DFTB, but instead of using precalculated integrals, xTB employs a (small) basis of Slater-type orbitals and uses an extended Hückel-like approximation for the Hamiltonian.

The DFTB Engine supports the GFN1-xTB parameterization of xTB, which is optimized for geometries, frequencies and non-covalent interactions and covers all elements of the periodic table up to radon.


Model Hamiltonian
*****************

The following keys allow you to select a model Hamiltonian and control different aspects of how the stationary Schroedinger equation is solved.

.. scmautodoc:: dftb Model

Different parameters may be suitable for different model Hamiltonians. It is important to choose the appropriate parameter set for the type of calculation and molecular system under study, see :ref:`parameter sets<dftb_parameters>`.

.. scmautodoc:: dftb ResourcesDir

**Examples:**

``ResourcesDir Dresden``
  Uses the resource directory $AMSRESOURCES/DFTB/Dresden.

``ResourcesDir /home/myusername/myparamsdir``
  Uses the specified path /home/myusername/myparamsdir as the resource directory.

**NOTE:** Each resource directory must contain a file called *metainfo.yaml*, which specifies the capabilities of the parameter set. For details see :ref:`metainfo.yaml<metainfo.yaml>`.


.. index:: Dispersion correction
.. _DispersionCorrection:

Dispersion correction
*********************

The selected model Hamiltonian can be extended with dispersion correction:

.. scmautodoc:: dftb DispersionCorrection

The newest and most accurate dispersion correction is D4. We recommend both the D3-BJ and D4 dispersion corrections as good defaults, depending on their availability for the specific combination of the model Hamiltonian and parameterization. Note that the D4 dispersion corrections is computationally more expensive than D3-BJ for bulk periodic systems (it scales as O(N\ :sup:`3`) with the number of atoms and is not parallelized), thus the user may first want to evaluate if the increased accuracy justifies the increased computational cost.


.. index:: Solvation model
.. index:: GBSA
.. _Solvation:

Solvation (GBSA)
****************

Solvation effects can be included via the implicit GBSA solvation model. We gratefully acknowledge the Grimme's group in Bonn for their contribution of the GBSA solvation method code.

To enable the GBSA method, specify the desired solvent:

.. scmautodoc:: dftb Solvation Solvent

More options can be specified in the ``Solvation`` block:

.. scmautodoc:: dftb Solvation UseGSASA GSolvState Temperature SurfaceGrid
   :noref:
   :skipblockdescription:



.. _SCCDetails:

SCC details and spin-polarization
*********************************

.. scmautodoc:: dftb SCC

.. scmautodoc:: dftb Occupation

.. scmautodoc:: dftb UnpairedElectrons


.. _KSpace:

k-space integration
*******************

As of the 2019 release, the k-space integration is unified between BAND and DFTB and uses the same keys as input, and the same defaults. See the `page on k-space integration in the BAND manual <../BAND/Accuracy_and_Efficiency/K-Space_Integration.html>`__ for details and recommendations.

.. index:: k-space integration
.. scmautodoc:: dftb KSpace


xTB specific keywords
*********************

A few keywords only apply to the xTB model Hamiltonian.

.. scmautodoc:: dftb XTBConfig

.. note::

   The GFN1-xTB implementation in AMS currently does not implement the electronic entropy term from the article by Grimme et al. It therefore gives slightly different energies (but not gradients!) for systems with partially occupied molecular orbitals.


Technical options
*****************

.. scmautodoc:: dftb Technical

.. scmautodoc:: dftb StoreMatrices
