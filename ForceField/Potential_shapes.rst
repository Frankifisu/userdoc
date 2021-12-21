Potential shapes
################

Setting the :ref:`Verbosity <forcefield-key-Verbosity>` to Verbose the engine prints the potential formula and the parameters used. 

The ForceField engine has a couple of potentials defined.

+ Stretch: harmonic

.. math::

   V^\text{stretch/harm} = \frac{1}{2} f_c (r-r_0)^2

+ Angle: harmonic and cyclic

.. math::


   V^\text{bend/harm} = \frac{1}{2} f_c (\phi-\phi_0)^2

   V^\text{bend/cycl} =  f_c \sum_{m=0}^n c_m \cos(m \phi)

+ Torsions: cyclic, possibly linearly combined. The same torsion occurs more than once in the printed table, and the energies are added.

.. math::

   V^\text{torsion/harm} = \frac{1}{2} f_c (\phi-\phi_0)^2

   V^\text{torsion/cycl} =  f_c \sum_{m=0}^n c_m \cos(m \phi)


+ Inversions: either angle or distance based. The angle based one depends on the order of the three atoms connected to the central atom. UFF averages over the three permutations.

.. math::

   V^\text{inversion/harm} = \frac{1}{2} f_c (\phi-\phi_0)^2

   V^\text{inversion/cycl} =  f_c \sum_{m=0}^n c_m \cos(m \phi)

   V^\text{inversion/amber} =  f_c  (1 + \cos(2 \phi- \phi_0))

   V^\text{inversion/dist} =  f_c  \; d^2


+ Dispersion: Lennard-Jones. Neglect up to second neighbors, possibly scale contribution from third neighbors.

.. math::

   V^\text{dispersion/LJ} = d \; (  (x/r)^{12} -2 * (x/r)^6 )

+ Coulomb: Neglect up to second neighbors, possibly scale contributions from third neighbors.

In general which formula is used depends on the parameter files. Note that the scaling of the third neighbors contributions is only possible when using .ff parameter files.
