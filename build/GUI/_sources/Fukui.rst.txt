Fukui Function
**************

The Fukui function describes the electron density after adding or removing some amount of electrons. It can predict where the most electrophilic and nucleophilic sites on a molecule are.

Fukui functions can be easily calculated using the GUI, as shown in the `Fukui tutorial <../Tutorials/Analysis/FukuiFunctionsAndDualDescriptor.html>`__.

The Fukui function is implemented as a finite charge change. By default a whole electron is added or removed, however the calculation is not restricted to this amount. Fractional amounts of electrons are allowed.

The Fukui equation for the electrophilic attack,  :math:`f^-`, is given for when 1 electron is removed.

.. math::
 f^{-} = \rho(N) - \rho(N - 1) 

Equally, the Fukui function for the nucleophilic attack,  :math:`f^+`, is given for when 1 electron is added.

.. math::
 f^{+} = \rho(N + 1) - \rho(N)

Do note that in all cases the geometry of the neutral state is used to get the electron density.

The Dual Descriptor is a way to combine the two Fukui functions. It has a positive value where it is electrophilic and negative where it is nucleophilic. It is implemented as the difference between the Fukui plus and Fukui minus functions.

.. math::
 f(r) = f^{+} - f^{-}

The Fukui function can be used to describe local chemical reactivity. This can even be done per atom by using the condensed Fukui function.

.. math::
 f_k^{-} = q_k(N) - q_k(N - 1)
.. math::
 f_k^{+} = q_k(N + 1) - q_k(N)

Atomic charges are used to get the condensed Fukui function. There are several ways to partition the atomic charges. The Fukui calculation prints the condensed Fukui functions for Hirshfeld, Mulliken, Voronoi, and if calculated, Bader charges.

The condensed Fukui function is normalized, so that atomic Fukui values sum to one.

.. math::
 \sum_{k=1}^{Natoms} f_k(\mathbf{r}) = 1

The local softness can be calculated as the product of the condensed Fukui function and the global softness.  
An approximation for the global softness is given as the inverse of the HOMO-LUMO gap.

.. math::
 S = \frac{1}{E_{LUMO} - E_{HOMO}}

The local softness is then simply

.. math::
 s_k^{-}(\mathbf{r}) = Sf_k^{-}(\mathbf{r})
.. math::
 s_k^{+}(\mathbf{r}) = Sf_k^{+}(\mathbf{r})
