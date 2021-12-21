
.. _RELATIVITY: 

Relativistic effects
********************

Scalar relativistic effects using the ZORA formalism are included by default in ADF calculations. Different relativistic options, such as spin-orbit coupling, can be included using the ``Relativity`` key

.. note:: 
   
   Starting from the 2020 version, scalar relativistic effects are included by default. In 2019.3 and previous versions of ADF, relativistic effects were **not** included by default.


.. index:: relativistic effects 

.. scmautodoc:: adf Relativity

.. index:: MAPA
.. index:: SAPA

**MAPA and SAPA**

The SAPA method is described in Ref. [#ref1]_ for the BAND program. The same potential was used in the ADF program.
However, starting from ADF 2017 instead of SAPA (the Sum of neutral Atomical potential Approximation) MAPA is used by default for ZORA. The MAPA (the Minumium of neutral Atomical potential Approximation) at a point is the minimum of the neutral Atomical potentials at that point. Advantage of MAPA over SAPA is that the gauge dependence of ZORA is reduced. The ZORA gauge dependency is small for almost all properties, except for the electron density very close to a heavy nucleus. The electron density very close to a heavy nucleus can be used for the interpretation of isomer shifts in Mössbauer spectroscopy

**Recommendations:** 

::

   Relativity
      Level Scalar
      Formalism ZORA
      Potential MAPA
   End

or 

::

   Relativity
      Level Spin-Orbit
      Formalism ZORA
      Potential MAPA
   End

.. index:: Pauli Hamiltonian 

Pauli
=====

Specification of the Pauli formalism means that the first order relativistic corrections (the Pauli Hamiltonian) will be used [#ref7]_ [#ref8]_ [#ref9]_ [#ref10]_ [#ref11]_ [#ref12]_ [#ref13]_ [#ref14]_ [#ref15]_ [#ref16]_. In a *scalar* relativistic run ADF employs the single point group symmetry and only the so-called *scalar* relativistic corrections, Darwin and Mass-Velocity. The treatment is not strictly first-order, but is *quasi*-relativistic, in the sense that the first-order scalar relativistic Pauli Hamiltonian is diagonalized in the space of the non-relativistic solutions, i.e. in the non-relativistic basis set. 

The quasi-relativistic approach improves results considerably over a first-order treatment. There are, however, theoretical deficiencies due to the singular behavior of the Pauli Hamiltonian at the nucleus. This would become manifest in a complete basis set but results are reasonable with the normally employed basis sets. However, this aspect implies that it is not recommended to apply this approach with an all-electron basis set for the heavy atoms, and for very heavy elements even a frozen core basis set often fails to give acceptable results. The problems with the quasi relativistic approach of the Pauli Hamiltonian are discussed for example in Ref. [#ref2]_. 

.. index:: ZORA

ZORA
====

The ZORA approach gives generally better results than the Pauli formalism. For all-electron calculations, and in fact also for calculations on very heavy elements (Actinides), the Pauli method is absolutely unreliable. Therefore the ZORA method is the recommended approach for relativistic calculations with ADF. 

ZORA refers to the Zero Order Regular Approximation [#ref2]_ [#ref17]_ [#ref18]_ [#ref19]_ [#ref20]_. This formalism requires special basis sets, primarily to include much steeper core-like functions; applying the ZORA method with other, not-adapted basis sets, gives unreliable results. The ZORA basis sets can be found in subdirectories under the $AMSHOME/atomicdata/ADF/ZORA directory. 

The ZORA formalism can also be used in Geometry Optimizations. However, there is a slight mismatch between the energy expression and the potential in the ZORA approach, which has the effect that the geometry where the gradients are zero does not exactly coincide with the point of lowest energy. The differences are very small, but not completely negligible, in the order of 0.0001 Angstrom. 

.. _X2C: 
.. index:: X2C
.. index:: RA-X2C

X2C and RA-X2C
==============

X2C stands for an exact transformation of the 4-component Dirac equation to 2-components [#ref21]_ [#ref22]_.
RA-X2C also stands for an exact transformation of the 4-component Dirac equation to 2-components, in this case using a regular approach to calculate the transformation matrix.
In practice, however, often approximations are made, and this is also true for the implementation in ADF.
In the X2C and RA-X2C method implemented in ADF, first the 4-component Dirac equation for a model potential (MAPA) of the molecule is calculated for the given ADF basis set,
using the modified Dirac equation by Dyall [#ref3]_ for X2C,
or using the regular approach [#ref4]_ to the modified Dirac equation for RA-X2C.

With the method used in ADF in the basis set limit X2C and RA-X2C should lead to the same results for the model potential (MAPA).
However, since in practice always a finite basis set is used, even for the model potential the results for X2C and RA-X2C will differ.
Next the (electronic) 4-component Dirac solutions are transformed exactly to 2-components [#ref5]_.
The transformation used is also used to calculate an effective one-electron 2-component kinetic energy operator in a basis set representation.
This kinetic energy matrix is then assumed to be constant in further ADF SCF calculation on the molecule.
The full Hamiltonian is approximated using the electron density in the 2-component picture, the so called Foldy-Wouthuysen picture.

In a similar way a spin-free (scalar relativistic) form of X2C and RA-X2C are calculated.
The spin-free form of X2C and RA-X2C will be different even in the basis set limit, see Ref. [#ref6]_.

X2C and RA-X2C in ADF can be used in single point calculations only. An all electron basis set is needed.
For bond energies, polarizabilities and TD-DFT excitation energies the Foldy-Wouthuysen picture will be used.
For the calculation of the EFG, ESR g-value, and ESR A-tensor, the Dirac picure will be used.
X2C and RA-X2C is not implemented for frozen cores, optimization of nuclear coordinates, frequencies, NMR properties.

.. _spin-orbit coupling:
.. index:: spin-orbit coupling, double group symmetry 

Spin-Orbit coupling
===================

The Spin-Orbit option uses double-group symmetry. The symmetry-adapted orbitals are labeled by the quantum number *J* rather than *L* and any references in input to subspecies, such as a specification of occupation numbers, must refer to the double group labels. 

Create runs must *not* use the Spin-Orbit formalism. The SFO analysis of Molecular Orbitals for a Spin-Orbit calculation is only implemented in the case of a scalar relativistic fragment file, which is the whole molecule.

In a Spin-Orbit run each level can allocate 2 electrons (times the dimension of the irreducible representation) as in a normal restricted calculation. However, contrary to the normal case these two electrons are not directly associated with spin-:math:`\alpha` and spin-:math:`\beta`, but rather with the more general Kramer's symmetry. Using the unrestricted feature in order to assign different numbers of electrons to a and b spin respectively cannot be applied as such. However, one can use the unrestricted option in combination with the collinear or non-collinear approximation. In that case one should use symmetry NOSYM, and each level can allocate 1 electron. 


.. only:: html

  .. rubric:: References

.. [#ref1] P.H.T. Philipsen, E. van Lenthe, J.G. Snijders and E.J. Baerends, *Relativistic calculations on the adsorption of CO on the (111) surfaces of Ni, Pd, and Pt within the zeroth-order regular approximation*, `Physical Review B 56, 13556 (1997) <https://doi.org/10.1103/PhysRevB.56.13556>`__ 

.. [#ref7] J.G. Snijders and E.J. Baerends, *A perturbation theory approach to relativistic calculations. I. Atoms*, `Molecular Physics 36, 1789 (1978) <https://doi.org/10.1080/00268977800102771>`__ 

.. [#ref8] J.G. Snijders, E.J. Baerends and P. Ros, *A perturbation theory approach to relativistic calculations. II. Molecules*, `Molecular Physics 38, 1909 (1979) <https://doi.org/10.1080/00268977900102941>`__ 

.. [#ref9] T.\  Ziegler, J.G. Snijders and E.J. Baerends, *Relativistic effects on bonding*, `Journal of Chemical Physics 74, 1271 (1981) <https://doi.org/10.1063/1.441187>`__ 

.. [#ref10] R.L. DeKock, E.J. Baerends, P.M. Boerrigter and J.G. Snijders, *On the nature of the first excited states of the uranyl ion*, `Chemical Physics Letters 105, 308 (1984) <https://doi.org/10.1016/0009-2614(84)85036-8>`__ 

.. [#ref11] R.L. DeKock, E.J. Baerends, P.M. Boerrigter and R. Hengelmolen, *Electronic structure and bonding of* Hg(CH\ :sub:`3` )\ :sub:`2` , Hg(CN)\ :sub:`2` , Hg(CH\ :sub:`3` )(CN), Hg(CCCH\ :sub:`3` )\ :sub:`2` , *and* Au(PMe)\ :sub:`3` (CH\ :sub:`3` ), `Journal of the American Chemical Society 106, 3387 (1984) <https://doi.org/10.1021/ja00324a001>`__ 

.. [#ref12] P.M. Boerrigter, *Spectroscopy and bonding of heavy element compounds*, 1987, Vrije Universiteit. 

.. [#ref13] P.M. Boerrigter, M.A. Buijse and J.G. Snijders, *Spin-Orbit interaction in the excited states of the dihalogen ions* F\ :sub:`2` \ :sup:`+` , Cl\ :sub:`2` \ :sup:`+` and Br\ :sub:`2` \ :sup:`+`, `Chemical Physics 111, 47 (1987) <https://doi.org/10.1016/0301-0104(87)87007-6>`__ 

.. [#ref14] P.M. Boerrigter, E.J. Baerends and J.G. Snijders, *A relativistic LCAO Hartree-Fock-Slater investigation of the electronic structure of the actinocenes* M(COT)\ :sub:`2` , *M=Th, Pa, U, Np and Pu*, `Chemical Physics 122, 357 (1988) <https://doi.org/10.1016/0301-0104(88)80018-1>`__ 

.. [#ref15] T.\  Ziegler, V. Tschinke, E.J. Baerends, J.G. Snijders and W. Ravenek, *Calculation of bond energies in compounds of heavy elements by a quasi-relativistic approach*, `Journal of Physical Chemistry 93, 3050 (1989) <https://doi.org/10.1021/j100345a036>`__ 

.. [#ref16] J.\  Li, G. Schreckenbach and T. Ziegler, *A Reassessment of the First Metal-Carbonyl Dissociation Energy in* M(CO)\ :sub:`4` (M = Ni, Pd, Pt), M(CO)\ :sub:`5` (M = Fe, Ru, Os), and M(CO)\ :sub:`6` (M = Cr, Mo, W) *by a Quasirelativistic Density Functional Method*, `Journal of the American Chemical Society 117, 486 (1995) <https://doi.org/10.1021/ja00106a056>`__ 

.. [#ref2] E.\  van Lenthe, A.E. Ehlers and E.J. Baerends, *Geometry optimization in the Zero Order Regular Approximation for relativistic effects*, `Journal of Chemical Physics 110, 8943 (1999) <https://doi.org/10.1063/1.478813>`__ 

.. [#ref3] K.G. Dyall, *An exact separation of the spin-free and spin-dependent terms of the Dirac-Coulomb-Breit Hamiltonian*, `Journal of Chemical Physics 100, 2118 (1994) <https://doi.org/10.1063/1.466508>`__ 

.. [#ref4] A.J. Sadlej and J.G. Snijders, *Spin separation in the regular Hamiltonian approach to solutions of the Dirac equation*, `Chemical Physics Letters 229, 435 (1994) <https://doi.org/10.1016/0009-2614(94)01067-6>`__ 

.. [#ref5] E.\  van Lenthe, E.J. Baerends, and J.G. Snijders, *Construction of the Foldy-Wouthuysen transformation and solution of the Dirac equation using large components only*, `Journal of Chemical Physics 105, 2373 (1996) <https://doi.org/10.1063/1.472104>`__

.. [#ref6] L.\  Visscher and E. van Lenthe, *On the distinction between scalar and spin-orbit relativistic effects*, `Chemical Physics Letters 306, 357 (1999) <https://doi.org/10.1016/S0009-2614(99)00458-3>`__ 

.. [#ref17] E.\  van Lenthe, E.J. Baerends and J.G. Snijders, *Relativistic regular two-component Hamiltonians*, `Journal of Chemical Physics 99, 4597 (1993) <https://doi.org/10.1063/1.466059>`__ 

.. [#ref18] E.\  van Lenthe, E.J. Baerends and J.G. Snijders, *Relativistic total energy using regular approximations*, `Journal of Chemical Physics 101, 9783 (1994) <https://doi.org/10.1063/1.467943>`__ 

.. [#ref19] E.\  van Lenthe, J.G. Snijders and E.J. Baerends, *The zero-order regular approximation for relativistic effects: The effect of spin-orbit coupling in closed shell molecules*, `Journal of Chemical Physics 105, 6505 (1996) <https://doi.org/10.1063/1.472460>`__ 

.. [#ref20] E.\  van Lenthe, R. van Leeuwen, E.J. Baerends and J.G. Snijders, *Relativistic regular two-component Hamiltonians*, `International Journal of Quantum Chemistry 57, 281 (1996) <https://doi.org/10.1002/(SICI)1097-461X(1996)57:3%3C281::AID-QUA2%3E3.0.CO;2-U>`__ 

.. [#ref21] K.G. Dyall, *Interfacing relativistic and nonrelativistic methods. I. Normalized elimination of the small component in the modified Dirac equation*, `Journal of Chemical Physics 106, 9618 (1997) <https://doi.org/10.1063/1.473860>`__

.. [#ref22] W.\  Kutzelnigg and W. Liu, *Quasirelativistic theory equivalent to fully relativistic theory*, `Journal of Chemical Physics 123, 241102 (2005) <https://doi.org/10.1063/1.2137315>`__

