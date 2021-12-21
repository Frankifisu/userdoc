.. _input units:

Units
-----

Some keys have a default unit associated (not all keys have units). For such keys, the default unit is mentioned in the key documentation. One can specify a different unit within square brackets at the end of the line::

   KeyName value [unit]

For example, assuming the key ``EnergyThreshold`` has as default unit ``Hartree``, then the following definitions are equivalent::

   # Use defaults unit:
   EnergyThreshold 1.0

   # use eV as unit:
   EnergyThreshold 27.211 [eV]

   # use kcal/mol as unit:
   EnergyThreshold 627.5 [kcal/mol]

   # Hartree is the atomic unit of energy:
   EnergyThreshold 1.0 [Hartree]


Available units:

- **Energy**: ``Hartree``, ``Joule``, ``eV``, ``kJ/mol``, ``kcal/mol``, ``cm1``, ``MHz``
- **Length**: ``Bohr``, ``Angstrom``, ``meter``
- **Angles**: ``radian``, ``degree``
- **Mass**: ``el``, ``proton``, ``atomic``, ``kg``
- **Pressure**: ``atm``, ``Pascal``, ``GPa``, ``a.u.``, ``bar``, ``kbar``
- **Electric field**: ``V/Angstrom``, ``V/meter``, ``a.u.``
