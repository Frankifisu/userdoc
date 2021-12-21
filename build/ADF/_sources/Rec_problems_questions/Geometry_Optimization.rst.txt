
.. _go_troubleshooting:


Geometry Optimization troubleshooting
=====================================

**No convergence**

First of all one should look how the energy changed during the latest ten or so iterations.  If the energy is changing more or less in one direction (increasing or decreasing), possibly with  occasional jumps, then there is probably nothing wrong with the optimization. This behavior is  typical in the cases when the starting geometry was far away from the minimum and the optimization  has a long way to go. Just increase the allowed number of iterations, restart from the latest geometry  and see if the optimization converges.  

If the **energy oscillates** around some value and the energy gradient hardly changes then you  may need to look at the calculation setup. We give some recommendations below.  

The success of geometry optimization depends on the accuracy of the calculated forces.  The default accuracy settings are sufficient in most cases. There are, however, cases when one  has to increase the accuracy in order to get geometry optimization converged. First of all,  this may be necessary if you tighten the optimization  convergence criteria. In some cases it may be necessary to  increase the accuracy also for the default criteria. Here's what you can do to increase the accuracy  of gradients: 

+ Increase the numerical quality to "good"

+ Add an ExactDensity keyword or select "Exact" in the "Density used in XC-potential" list in the  Details:Accuracy panel. This will make the calculation 2 or 3 times slower.

+ Tighten the SCF convergence criteria, for example, to 1e-8.

Example input with some of these stricter settings using a TZ2P basis set. ExactDensity is not included here since it will make the calculation much slower. 

::

   NumericalQuality Good
   Basis
     Type TZ2P
     Core None
   End
   SCF
    converge 1e-8
   End

**Small HOMO-LUMO gap**: check the HOMO-LUMO gap at the last SCF cycle at a recent geometry.  Is it comparable with the changes in the MO energies between geometries? If yes, then it is possible  that the electronic structure changes between optimization steps, which may lead to non-convergence.  This may indicate a fundamental problem with the calculation setup. First of all, check that you  obtain a ground state in a single-point calculation. Is the spin-polarization value correct? Try  calculating some of the high-spin states if possible and see if they have lower energy. If the  MO repopulation that is taking place is between MOs of different symmetry, then you can try freezing  the number of electrons per symmetry using an OCCUPATIONS block. 


Are there **constraints** imposed on the optimization? If yes, then check that  the constraints do not break the symmetry. ADF automatically preserves symmetry when the starting  structure is symmetric and no *Symmetry NOSYM* has been specified. This symmetry preservation  may conflict with constraints if the constraints are not specified according to symmetry.  For example, if two inter-atomic distances are symmetry-equivalent and you freeze one of them,  then you should also freeze the other explicitly. 

**Optimization in Cartesian coordinates** usually needs more steps to converge compared   to delocalized. If you haven't tried delocalized optimization for the system then you should do it. 

**Near 180-degree angles** with optimization in delocalized coordinates. ADF normally  does not have a problem with a near-180-degree valence angle if the initial value of the angle was  larger than 175 degrees or if it is a terminal bond angle. If the initial angle was larger  than 175 degrees then it gets a special treatment. For example, any torsion angle that contains  the three atoms is removed or replaced with a torsion angle involving only the two end atoms of  the near-180-degrees angle. If the angle defines a terminal bond then two angles in two coordinate  planes are used to define the bond instead of a valence and a torsion angle. However, if the initial  value of the angle was far from 180 degrees and has become close to it during optimization then  optimization may become unstable, especially if this is an angle connecting large fragments.  In this case, it may be useful to restart geometry optimization from the latest geometry. As a  last resort, you may want to constrain the angle to a value close, but not equal, to 180 degrees.  


Very short bonds
----------------

If the computed equilibrium geometry appears to exhibit unlikely values, typically  significantly *too short* bond lengths, you may have run into a basis set problem, in particular (but not only) if the Pauli relativistic method is applied. 

**Problem**: Optimized bond lengths are clearly too short. The energy may also look suspicious. 

**Possible cause 1**: Basis set trouble: onset of Pauli variational collapse, if you have applied the Pauli relativistic option. Caused by small (or absent) frozen cores and/or relatively large basis sets, applied to heavy elements. 

**Possible cause 2**: Basis set trouble also, but quite different from the previous potential cause: you have used relatively *large* frozen cores. When the atoms approach each other during the optimization and the frozen cores start to overlap, the energy computation and the computed energy gradients become more and more incorrect. This is a result of the inappropriateness of the frozen core approximation, which indeed assumes that frozen cores of neighboring atoms do not significantly overlap. Without going into a detailed explanation here, the net effect is that certain repulsive terms in the energy computation are missing and hence a spurious tendency to a 'core collapse' arises, yielding too short bond lengths.  

**Cure**: Best is to abandon the Pauli method and use the ZORA approach instead for any relativistic calculation. If for whatever reason you insist on using the Pauli formalism, apply bigger frozen cores and, if that doesn't help, reduce the basis set (not by deleting polarization functions, but by reducing the flexibility of the occupied-atomic-orbitals space, in particular *s*- and *p*-functions). Note, however, that large frozen cores can be a cause for trouble by themselves, irrespective of any relativistic feature. If you have reason to believe that your frozen cores might be too *large*,  given the resulting bond lengths in your calculation, you have to pick smaller cores  (and hence be very wary of using the Pauli formalism for any relativity). 

