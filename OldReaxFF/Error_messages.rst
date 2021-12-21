
Warnings
########

``WARNING: Inconsistent vdWaals-parameters in forcefield. See output``
   All atom types in a force-field file should normally have consistent Van der Waals screening and short-range repulsion (a.k.a. inner core) parameters. This warning is printed if two atom types have inconsistent parameters.

``WARNING: Suspicious force-field EEM parameters for ...``
   For every atom type, the eta and gamma parameters for the electronegativity equalization method (EEM) should satisfy the relation: eta > 7.2*gamma. Otherwise a polarization catastrophe is likely to occur at a short interatomic distance, the critical distance being dependent on the eta/gamma ratio. The smaller the ratio the larger the distance at which this occurs. When the polarisation catastrophe occurs the amount of charge that flows from one atom to the other can become very large. The EEM routine checks that the resulting charge for each atom lies within the [-10,Z] interval, where Z is the number of electrons in the neutral atom, and throws an error if the check fails.

