
eReaxff: classical treatment of the explicit electron
#####################################################

The eReaxFF implementation in the SCM ReaxFF program is based on the paper [`J. Chem.Theory Comput 12, 3463 (2016) <https://doi.org/10.1021/acs.jctc.6b00432>`__] and on the prototype code obtained from the group of Adri van Duin. It was, however, largely rewritten by SCM to meet our coding standards and to maximize performance.

An eReaxFF calculation requires the following additional force-field parameters to be defined (equation numbers are referring to the eReaxFF paper):

* The header of the force-field file must begin with the "[ ereaxff acks2 ]" string,
* General parameter 27: the currently reserved :math:`p_{elho}` parameter in the unpublished electron-hole interaction equation (which is still highly experimental and is subject to change),
* General parameter 37: the Gauss exponent parameter :math:`p_{val}` describing the free electron, Eq(3),
* General parameter 41: a different taper radius for electron and hole interactions can be specified here,
* Atomic parameter 24: the :math:`\alpha` parameter in Eq(2),
* Atomic parameter 27: the :math:`\beta` parameter in Eq(2),
* Atomic parameter 13: the :math:`p_{ij}^{xel2}` parameter in Eq(4d),
* Bond parameter 16: the :math:`p_{ij}^{xel1}` parameter in Eq(4d).

Additionally, since the eReaxFF method is usually coupled to the ACKS2 charge equilibration method, the ACKS2-related parameters should also be defined.

In the input geometry file, the explicit electrons are called 'El' and the holes are 'Ho' (yes we are aware that the latter clashes with holmium but this is what the original authors are using).

It should be noted that the eReaxFF implementation is considered experimental so the users are advised to contact Adri van Duin regarding its use.

