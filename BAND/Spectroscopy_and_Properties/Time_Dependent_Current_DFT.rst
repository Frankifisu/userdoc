.. index:: TDCDFT

.. _TDCDFT:

Optical Properties: Time-Dependent Current DFT
==============================================

Time-Dependent Current Density Functional Theory (**TD-CDFT**) is a theoretical framework for computing optical response properties, such as the frequency-dependent dielectric function.

In this section, the TD-CDFT implementation for extended systems (1D, 2D and 3D) in BAND is described.
The input keys are described in :ref:`NewResponse<band-key-NewResponse>` or in :ref:`OldResponse<band-key-OldResponse>`. 

Some examples are available in the ``$AMSHOME/examples/band`` directory and are discussed in the Examples section.

* `Tutorial: Silicon (OldResponse) <../../Tutorials/OpticalPropertiesElectronicExcitations/TDCDFTSiBulk.html>`__
* `Tutorial: MoS2 Monolayer (NewResponse) <../../Tutorials/OpticalPropertiesElectronicExcitations/TDCDFTMoS2Monolayer.html>`__
* :ref:`example OldResp_Diamond`

Insulators, semiconductors  and metals
--------------------------------------

The TD-CDFT module enables the calculation of real and imaginary parts of the material property tensor :math:`\chi_e(\omega)`, called the **electric susceptibility**. The electric susceptibility is related to the macroscopic **dielectric function**, :math:`\varepsilon_M(\omega)`. 

For semi-conductors and insulator, for which the bands are either fully occupied or fully unoccupied, the dielectric function :math:`\varepsilon_M(\omega)` comprises only of the so called interband component:

.. math::

   \varepsilon_M(\omega) = 1 + 4 \pi \chi_e(\omega)

In general :math:`\chi_e(\omega)` and :math:`\varepsilon_M(\omega)` are tensors. They, however, simplify to scalars in isotropic systems.

For metals, for which partially-occupied bands exist, there is a so called intraband component arising due to transitions within a partially-occupied band:

.. math::

   \varepsilon_M(\omega) = 1 + 4 \pi \chi_e(\omega) - 4 \pi i \sigma_e(\omega) / \omega

Frequency dependent kernel
--------------------------

It is known that the exact Vignale-Kohn (VK) kernel greatly improves the static polarizabilities of infinite polymers and nanotubes (see `reference <https://doi.org/10.1063/1.2102899>`__), but gives bad results for the optical spectra of semiconductors and metals. For the low frequency part one needs a frequency dependent kernel, since Drude-like tails are completely absent in the adiabatic local density approximation (ALDA). With a modified VK kernel, which neglects :math:`\mu_{xc}` so that it reduces to the ALDA form in the static limit (see `reference <https://doi.org/10.1103/PhysRevB.74.245117>`__), much better results can be obtained. BAND currently only supports the modified VK kernel in either the QV or CNT parametrization, and it should **only be used for metals**.

.. index:: EELS

EELS
----

From the macroscopic dielectric function it is possible to calculate the electron energy loss function (EELS). In transmission EELS one studies the inelastic scattering of a beam of high energy electrons by a target. The scattering rates obtained in these experiments are related to the dynamical structure factor :math:`S(q,\omega)` [A1]. In the special case with wavevector :math:`q=0`, :math:`S(q,\omega)` is related to the longitudinal macroscopic dielectric function. This is the long-wave limit of EELS. For isotropic system the dielectric function is simply a scalar (:math:`1/3 \text{Tr}  (\varepsilon_M(\omega))` ). In this case the long-wave limit of the electron energy loss function assumes the trivial form

.. math::

   \lim_{q \rightarrow 0} 2 \pi \frac{S(q,\omega)}{q^2 V} = \frac{\varepsilon_2}{\varepsilon_1^2 + \varepsilon_2^2}

with :math:`\varepsilon_1` and :math:`\varepsilon_2` as real and imaginary part of the dielectric function.


**References**

The three related Ph.D. theses, due to F. Kootstra (on TD-DFT for insulators), P. Romaniello (on TD-CDFT for metals), and A. Berger (on the Vignale-Kohn functional in extended systems) contain much background information, and can be downloaded from the `SCM website <http://www.scm.com>`__. 

The most relevant publications on this topic due to the former "Groningen" group of P.L. de Boeij are [#ref1]_ [#ref2]_ [#ref3]_ [#ref4]_. 

[A1] S. E. Schnatterly, in Solid State Physics Vol.34, edited by H. Ehrenreich, F. Seitz, and D. Turnbull (Academic Press, Inc., New York, 1979).

Input Options
-------------

In the 2017 release of BAND there are two implementations of the TD-CDFT formalism. The original implementation, relying on obsolete algorithms of BAND, is accessible via the :ref:`OldResponse<band-key-OldResponse>` key block. The new code section, relying on more modern algorithms of BAND, is accessible via the :ref:`NewResponse<band-key-NewResponse>`, :ref:`NewResponseSCF<band-key-NewResponseSCF>` and :ref:`NewResponseKSpace<band-key-NewResponseKSpace>` key blocks. The differences between the two flavors are summarized in the following table:

.. csv-table:: 

                    , OldResponse , NewResponse
   3D-systems       , yes         , yes
   2D-systems       , no          , yes
   1D-systems       , (yes)       , yes
   Semiconductors   , yes         , yes
   Metals           , yes         , (yes)
   ALDA             , yes         , yes
   Vignale-Kohn     , yes         , no
   Berger2015 (3D)  , yes         , yes
   Scalar ZORA      , yes         , yes
   Spin Orbit ZORA  , yes         , no

Besides these differences, one should not expect both flavors to give the exact same result, if the reciprocal space limit is not reached! This can be explained by different approaches to evaluate the integration weights of single-particle transitions in reciprocal space. 

.. attention::
   
   Response properties **converge slowly** with respect to k-space sampling (number of k-points). **Always check the convergence of** :math:`\varepsilon_M` **with respect to** :ref:`K-Space <band-key-KSpace>` **options!!!**

   .. only:: html

      .. figure:: /Images/Conv_H2.gif
         :scale: 75 %
         :align: center

         Reciprocal space sampling convergence of imaginary part of susceptibility for a dihydrogen chain.

NewResponse
^^^^^^^^^^^

The dielectric function is computed when the key block :ref:`NewResponse<band-key-NewResponse>` is present in the input. Several important settings can be defined in this key block.

Additional details can be specified via the :ref:`NewResponseKSpace<band-key-NewResponseKSpace>` and :ref:`NewResponseSCF<band-key-NewResponseSCF>` blocks.

.. scmautodoc:: band NewResponse NFreq FreqLow FreqHigh EShift ActiveESpace DensityCutOff ActiveXYZ


.. scmautodoc:: band NewResponseSCF


.. scmautodoc:: band NewResponseKSpace


OldResponse
^^^^^^^^^^^

.. scmautodoc:: band OldResponse

.. only:: html

  .. rubric:: References

.. [#ref1] F.\  Kootstra, P.L. de Boeij and J.G. Snijders,  *Efficient real-space approach to time-dependent density functional theory for the dielectric response of nonmetallic crystals.*  `Journal of Chemical Physics 112, 6517 (2000). <https://doi.org/10.1063/1.481315>`__

.. [#ref2] P.\  Romaniello and P.L. de Boeij,  *Time-dependent current-density-functional theory for the metallic response of solids.*  `Physical Review B 71, 155108 (2005) <https://doi.org/10.1103/PhysRevB.71.155108>`__.

.. [#ref3] J.A. Berger, P.L. de Boeij and R. van Leeuwen,  *Analysis of the viscoelastic coefficients in the Vignale-Kohn functional: The cases of one- and three-dimensional polyacetylene.*,  `Physical Review B 71, 155104 (2005) <https://doi.org/10.1103/PhysRevB.71.155104>`__.

.. [#ref4] P.\  Romaniello and P.L. de Boeij,  *Relativistic two-component formulation of time-dependent current-density functional theory: application to the linear response of solids.*,  `Journal of Chemical Physics 127, 174111 (2007) <https://doi.org/10.1063/1.2780146>`__.
