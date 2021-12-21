
Troubleshooting and warnings
############################


.. _troubleshooting_geoopt:

Geometry optimization issues
****************************

Geometry optimization issues with ReaxFF are usually caused by the fact that
the derivative of the ReaxFF energy function has discontinuities. These
discontinuities are often related to the bond order cutoff (the ``Engine
ReaxFF%BondOrderCutoff`` key, 0.001 by default). This cutoff determines whether
a valence or a torsion angle is included in the potential energy evaluation or
not, i.e. when at least one of the bonds forming an angle is of order lower
than the cutoff then the angle is discarded. Thus, when the order of a
particular bond crosses the cutoff value between two optimization steps, the
energy derivative (the force) experiences a sudden change. The magnitude of the
jump depends on the cutoff value. The default value of 0.001 is normally not a
problem during molecular dynamics but it may break the geometry optimization convergence. 

There are a several ways to reduce the discontinuity and thus to improve the
stability of the geometry optimization. 

* **Use 2013 torsion angles** (set ``Engine ReaxFF%Torsions`` to 2013):
   Switch on the 2013 formula for the torsion angles. This will make the
   torsion angles change more smoothly at lower bond orders but it will
   not affect the valence angles. You should be aware, however, that using
   this option changes the bond order dependence of the ReaxFF 4-center
   term.

* **Decrease the bond order cutoff** (``Engine ReaxFF%BondOrderCutoff``):
   This will significantly reduce the discontinuity in the valence angles
   and somewhat in the torsion angles but will not remove it. This will
   also make the calculation somewhat slower because more angles will have
   to be included in the computation. 

* **Taper the bond orders** (``Engine ReaxFF%TaperBO``): 
   Use tapered bond
   orders by Furman and Wales (DOI: 10.1021/acs.jpclett.9b02810).


Warnings
********

``WARNING: Inconsistent vdWaals-parameters in forcefield. See output``
   All atom types in a force-field file should normally have consistent Van der Waals screening and short-range repulsion (a.k.a. inner core) parameters. This warning is printed if two atom types have inconsistent parameters.

``WARNING: Suspicious force-field EEM parameters for ...``
   For every atom type, the eta and gamma parameters for the electronegativity equalization method (EEM) should satisfy the relation: eta > 7.2*gamma. Otherwise a polarization catastrophe is likely to occur at a short interatomic distance, the critical distance being dependent on the eta/gamma ratio. The smaller the ratio the larger the distance at which this occurs. When the polarisation catastrophe occurs the amount of charge that flows from one atom to the other can become very large. The EEM routine checks that the resulting charge for each atom lies within the [-10,Z] interval, where Z is the number of electrons in the neutral atom, and throws an error if the check fails.

