.. index:: ESR
.. index:: EPR
.. _ESR_EPR:

ESR/EPR
=======

BAND is capable to calculate electron paramagnetic resonance (EPR) parameters for paramagnetic defects in solids: hyperfine A-tensor and the Zeeman g-tensor. 

The implementation of EPR parameters in BAND is described in the publications by Kadantsev and co-workers [#ref1]_ and [#ref2]_. 

.. index:: A-Tensor

**Hyperfine A-tensor**   

The A-tensor is implemented within the non-relativistic and scalar relativistic, spin-polarized Kohn-Sham scheme.

.. scmautodoc:: band ATensor

Two methods  are used for A-tensor calculation:

* Method 1: involves the gradient of the spin-polarized density and integration by parts. The isotropic component of the A-tensor obtained through integration, in a "non-local fashion".

* Method 2: the A-tensor is computed from spin-polarized density and does not relies on the integration by parts. The isotropic component is obtained in a "local fashion" from the value of the spin-polarized density on the grid points near the nuclei. 

The user should be aware that numerical integration in A- and g-tensor routines is carried out over the Wigner-Seitz (WS) cell, and, therefore, to obtain a meaningful result, the defect in question should lie at or very close to the WS cell origin. This might require, on the user's part, some modification of the input geometry. 

It also might happen that the size of the WS cell is not large enough for the adequate description of the paramagnetic defect in question. In this case, Method 1 will fails, since it relies on the integration by parts and assumes that the spin-polarized density is localized inside the WS cell. For the same reason, we recommend that the user removes diffuse basis set functions that describe the defect subsystem. 

Finally, we note that the final result for A-tensor as presented by BAND is not scaled by the nuclear spin (as it is done in ADF) and the user is responsible for making necessary adjustments. 

.. index:: G-Tensor

**g-tensor**   

The calculation of the Zeeman g-tensor is invoked within the ESR block:

.. scmautodoc:: band ESR



(:math:`\Gamma`-only calculation). The g-tensor is then computed from the HOMO spinor at the :math:`\Gamma` point. In the output, the user can find two-contributions to the g-tensor: one that stems from the :math:`K_\sigma` operator and a second one, that stems from the orbital angular momentum. By default, GIAO and spin-Zeeman corrections are **not** included. From our experience, these corrections are quite small. 


.. only:: html

  .. rubric:: References

.. [#ref1] E.S. Kadantsev and T. Ziegler,  *Implementation of a Density Functional Theory-Based Method for the Calculation of the Hyperfine A-tensor in Periodic Systems with the Use of Numerical and Slater Type Atomic Orbitals: Application to Paramagnetic Defects.*  `Journal of Physical Chemistry A 112, 4521 (2008) <https://doi.org/10.1021/jp800494m>`__.

.. [#ref2] E.S. Kadantsev and T. Ziegler,  *Implementation of a DFT Based Method for the Calculation of Zeeman g-tensor in Periodic Systems with the use of Numerical and Slater Type Atomic Orbitals.*  `Journal of Physical Chemistry A  113, 1327 (2009) <https://doi.org/10.1021/jp805466c>`__.
