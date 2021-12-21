.. index:: Electric Field
.. index:: Magnetic Field

Electric and Magnetic Fields
============================

.. _ElectricField:

Electric Field
^^^^^^^^^^^^^^

The external electric field is handled at the AMS level, see the documentation there.

The effect of a magnetic filed can be **approximated** by the following potential: :math:`\mu_B \vec{\sigma}_i \vec{B}`,
where :math:`\mu_B` is the Bohr magneton, :math:`\vec{\sigma}_i` are the Pauli matrices and :math:`\vec{B}` is the magnetic field.
For :ref:`Spin-unrestricted collinear <band-key-Unrestricted>` calculations, the spin is assumed to be aligned with the z-axis.

.. _MagneticField:

Magnetic Field
^^^^^^^^^^^^^^

.. scmautodoc:: band BField


Atom-wise fuzzy potential
^^^^^^^^^^^^^^^^^^^^^^^^^

.. scmautodoc:: band FuzzyPotential

Example::

   FuzzyPotential
      scale $scale
      a1 v1   ! atom with index a1 gets potential coefficient v1 (a.u.)
      a2 v2   ! atom a2 gets potential v2
      ...
   End

``scale``
   Overall scaling factor to be applied.

   If an atom is not in the list it gets a coefficient of zero. The potential of an atom is its number (:math:`v_i`) as specified on input times its fuzzy cell

   .. math::

      V(r)  = \sum_i^\text{atoms} v_i \mathcal{P}_{i,U} (r)

   using the same partition function :math:`\mathcal{P}` as for the :ref:`BeckeGrid <band-key-BeckeGrid>`.  A partition function (or fuzzy cell) of an atom is close to one in the neighborhood of this atom.

   The sign convention is: negative is favorable for electrons. (Unit: a.u.)


