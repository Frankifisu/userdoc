.. index:: electron mobility 
.. index:: hole mobility 
.. index:: charge transport properties 

.. _TRANSFERINTEGRALS:

Charge transport (transfer integrals)
=====================================

DFTB can provide input parameters, such as charge transfer integrals, that are needed in approximate methods that model charge transport properties in the hopping regime.
Note that DFTB is an approximate method, one might use ADF to calculate more accurate charge transfer integrals, or use specifically optimized DFTB parameters.

In theoretical models of charge transport in organic materials, see Refs. [#ref6]_ [#ref7]_ [#ref8]_, the whole system is divided into fragments, in which an electron or hole is localized on a fragment, and can hop from one fragment to another. In the tight-binding approximation that is used in these models the electron or hole is approximated with a single orbital, and it is assumed that only the nearest neighboring fragments can couple. The models require accurate values of electronic couplings for charge transfer (also referred to as charge transfer integrals or hopping matrix elements) and site energies (energy of a charge when it is localized at a particular molecule) as a function of the geometric conformation of adjacent molecules. Charge transfer integrals for hole transport can be  calculated from the energetic splitting of the two highest-occupied molecular orbitals (HOMO and HOMO-1) in a system consisting of two adjacent molecules, also called "energy splitting in dimer" (ESID) method. For electron transport these can be calculated from the two lowest-unoccupied orbitals (LUMO and LUMO+1) in this ESID method. DFTB can also calculate transfer integrals based on the direct method by the using a fragment approach. The charge transfer integrals obtained in this way may differ significantly from values estimated from the energy splitting between the highest occupied molecular orbitals in a dimer. The difference is due to the nonzero spatial overlap between the molecular orbitals on adjacent molecules.  Also, the direct method is applicable in cases where an orbital on one molecule couples with two or more orbitals on another molecule. 


Charge transfer integrals direct method
---------------------------------------

In this method the matrix elements of the molecular DFTB Hamiltonian :math:`H^{DFTB}` in the basis of fragment orbitals is used to calculate site energies and charge transfer integrals. Likewise the overlap integrals between fragment orbitals are calculated. No explicit electrons are removed or added in this method. For electron mobility calculations the fragment LUMO's are considered. For hole mobility calculations the fragment HOMO's are considered. 

To calculate the charge transfer integrals, spatial overlap integrals and site energies, the molecular system typically should be build from 2 fragments.
See also the section on :ref:`Fragment orbital analysis <FRAGMENTS>`.
In the ``Engine DFTB`` block, specify

::

   Properties
      Fragments
         File frag1.results/dftb.rkf
         File frag2.results/dftb.rkf
         TransferIntegrals
      End
   End

By default, integrals are calculated only for the HOMO (LUMO) of the fragments, and possibly HOMO-1, HOMO-2 (LUMO+1, LUMO+2) if the energy of those fragment orbitals are close to the HOMO (LUMO) of that fragment. To calculate the matrix elements and overlap integrals based on all fragment orbitals one can use the key: 

If 2 fragments are used the electronic coupling V (also known as effective (generalized) transfer integrals J_eff) for hole transfer or electron transfer is calculated as V = (J-S(e1+e2)/2)/(1-S^2). Here e1, e2, are the site energies of fragment 1 and 2, respectively. J is the charge transfer integral, and S the overlap integral.

.. math::

  e_1 & = \langle \phi_1 | H^{DFTB} | \phi_1 \rangle \\
  e_2 & = \langle \phi_2 | H^{DFTB} | \phi_2 \rangle \\
  J   & = \langle \phi_1 | H^{DFTB} | \phi_2 \rangle \\
  S   & = \langle \phi_1 | \phi_2 \rangle \\
  V   & = \frac{J-S(e1+e2)/2}{1-S^2}


In case of electron mobility calculations :math:`\phi_1` is the LUMO of fragment 1 and :math:`\phi_2` is the LUMO of fragment 2.
In case of hole mobility calculations :math:`\phi_1` is the HOMO of fragment 1 and :math:`\phi_2` is the HOMO of fragment 2.
The electronic coupling between the HOMO of the donor fragment and the LUMO of the acceptor fragment and vice-versa is also calculated, which represent the probability of a charge recombination process. 

If there is (near) degeneracy in the fragment HOMO and/or LUMO multiple electronic couplings :math:`V_i` are printed. A total electronic coupling is calculated as

.. math::

  V_{tot} = \sqrt{\sum_{deg} {V_i}^2}

.. scmautodoc:: dftb Properties Fragments
   :noref:
   :skipblockdescription:

.. [#ref6] M.D. Newton, *Quantum chemical probes of electron-transfer kinetics: the nature of donor-acceptor interactions*, `Chemical Reviews 91, 767 (1991) <https://doi.org/10.1021/cr00005a007>`__. 

.. [#ref7] K.\  Senthilkumar, F.C. Grozema, F.M. Bickelhaupt, and L.D.A. Siebbeles, *Charge transport in columnar stacked triphenylenes: Effects of conformational fluctuations on charge transfer integrals and site energies*, `Journal of Chemical Physics 119, 9809 (2003) <https://doi.org/10.1063/1.1615476>`__. 

.. [#ref8] K.\  Senthilkumar, F.C. Grozema, C. Fonseca Guerra, F.M. Bickelhaupt, F.D. Lewis, Y.A. Berlin, M.A. Ratner, and L.D.A. Siebbeles, *Absolute Rates of Hole Transfer in DNA*, `Journal of the American Chemical Society 127, 14894 (2005) <https://doi.org/10.1021/ja054257e>`__ 
