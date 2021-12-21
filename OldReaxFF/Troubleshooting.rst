
Troubleshooting
###############


Geometry optimization
*********************

Geometry optimization issues with reaxff are usually caused by the fact that the derivative of the ReaxFF energy function has discontinuities. These discontinuities are often related to the bond order cutoff (cutof2 in the control file, 0.001 by default). This cutoff determines whether a valence or a torsion angle is included in the potential energy evaluation or not, i.e. when at least one of the bonds forming an angle is of order lower than the cutoff then the angle is discarded. Thus, when the order of a particular bond crosses the cutoff value between two optimization steps, the energy derivative (the force) experiences a sudden change. The magnitude of the jump depends on the cutoff value. The default value of 0.001 is normally not a problem during MD but it may break the geometry optimization convergence. 

There are a two ways to reduce the discontinuity and thus to improve the stability of the geometry optimization. One way is to switch on the 2013 formula for the torsion angles (the tors13=1 key in the control file). This will make the torsion angles change more smoothly at lower bond orders but it will not affect the valence angles. You should be aware, however, that using this option changes the bond order dependence of the ReaxFF 4-center term.

The other way is to decrease the cutof2 value in the control file. This will significantly reduce the discontinuity in the valence angles and somewhat in the torsion angles but will not remove it. This will also make the calculation somewhat slower because more angles will have to be included in the computation. 
