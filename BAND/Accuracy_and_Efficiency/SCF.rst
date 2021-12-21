.. index:: SCF Options

.. _scf:

Self Consistent Field (SCF)
===========================

The SCF procedure searches for a self-consistent density. The self-consistent error is the square root of the integral of the squared difference between the input and output density of the cycle operator. When the SCF error is below a certain criterion, controlled by subkey ``Criterion`` of block key ``Convergence``, convergence is reached. In case of bad convergence the SCF looks at the subkeys ``Mixing``, and ``Degenerate``, and the subkeys of block key ``DIIS``. 

.. seealso::

  Troubleshooting: :ref:`scf_does_not_converge`

SCF block
---------

.. scmautodoc:: band SCF


Convergence
-----------

All options and parameters related to the convergence behavior of the SCF procedure are defined in the ``Convergence`` block key. Also the finite temperature distribution is part of this

.. scmautodoc:: band Convergence


.. index:: DIIS

DIIS
----

The DIIS procedure to obtain the SCF solution depends on several parameters. Default values can be overruled with this block.

.. scmautodoc:: band DIIS


.. index:: Multisecant

Multisecant
-----------

For more detais on the multisecant method see ref [#multisecant]_.

.. scmautodoc:: band MultiSecantConfig


DIRIS
-----

In the DIRIS block, which has the same options as the ``DIIS`` block, you can specify the DIIS options to be used in the Dirac subprogram, for numerical single atom calculations, which constructs the radial tables for the NAOs. 


.. [#multisecant] \L. D. Marks and D. R. Luke, *Robust mixing for ab initio quantum mechanical calculations*, `Phys. Rev. B 78, 075114 (2008) <https://doi.org/10.1103/PhysRevB.78.075114>`__
