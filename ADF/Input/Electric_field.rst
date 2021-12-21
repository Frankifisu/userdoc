.. index:: electric field (homogeneous) 
.. index:: homogeneous electric field 
.. index:: point charges 
.. _keyscheme ELECTROSTATICEMBEDDING:
.. _EFIELD: 


Electric Field: Homogeneous, Point Charges, Polarizability
**********************************************************

A homogeneous external electric field and/or the field due to point charges can be included in the Fock operator. Either can be applied in both a Single-Point calculation or in geometry optimization. When applied in geometry optimization, it will allow for the molecule to rotate with respect to point charges or the field  vector but not translate. Rigid translation is explicitly disabled to avoid drifting of the  molecule in the external electric field. 

Homogeneous electric fields, point charges and external dipole moments should be defined in the `System block <../../AMS/System.html>`__, which is part of the AMS driver input. `This section of the AMS driver manual <../../AMS/System.html#homogeneous-electric-field-and-multipole-charges>`__ describes the various input options.

**Symmetry**

The homogeneous electric field and the point charge fields may polarize the electronic charge density. This must be accounted for in the point group symmetry. If symmetry is not specified in input, ADF uses symmetry NOSYM. You can specify a symmetry, but ADF will not check its correctness. An incorrect symmetry may lead to incorrect results.

**Bonding energy**

The bonding energy is computed as: the energy of the molecule in the field minus the energy of the constituent fragments without the field.


.. index:: polarizability
.. index:: hyperpolarizability

**Polarizability and hyperpolarizability**

ADF supports a direct calculation of the (hyper) polarizability (see section on Spectroscopic Properties). The static (hyper) polarizabilities could also be computed by applying a small homogeneous field and comparing the results with the field-free data. 

