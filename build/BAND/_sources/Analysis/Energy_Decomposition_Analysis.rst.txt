Energy Decomposition Analysis
=============================

In BAND there are two fragment-based energy decomposition methods available: the periodic energy decomposition analysis (PEDA) [#ref1]_ and the periodic energy decomposition analysis combined with the natural orbitals of chemical valency method (PEDA-NOCV) [#ref1]_.

.. index:: PEDA

.. _PEDA:

Periodic Energy Decomposition Analysis (PEDA)
---------------------------------------------

.. scmautodoc:: band PEDA

If used in combination with the ``fragment`` keyblocks the decomposition of the interaction energy between fragments is invoked and the resulting energy terms (:math:`\Delta E_{int}`, :math:`\Delta E_{disp}`, :math:`\Delta E_{Pauli}`, :math:`\Delta E_{elstat}`, :math:`\Delta E_{orb}`) presented in the output file. (See the :ref:`example<example PEDA_MgO+CO>` or the `tutorial <../../Tutorials/Analysis/index.html>`__)

.. Attention::

  In case of the error message "Fragments cannot be assigned by a simple translation!", BAND does only allow for fragments which can be transformed to the structure in the PEDA calculation by a simple translation. So, a rotation is not allowed. 
  
  
.. index:: PEDA-NOCV

.. _PEDA-NOCV:

Periodic Energy Decomposition Analysis and natural orbitals of chemical valency (PEDA-NOCV)
-------------------------------------------------------------------------------------------

``PEDANOCV (block-type)``

If present in combination with the ``fragment`` keyblocks and the ``PEDA`` key the decomposition of the orbital relaxation term is performed. The binary result file will contain the information to :ref:`plot NOCV Orbitals and NOCV deformation densities<band-key-NOCVOrbitalPlot>`.

.. seealso::

   - :ref:`example<example PEDANOCV_MgO+CO>`
   - `tutorial <../../Tutorials/Analysis/PEDAWithNOCV.html>`__
   - `advanced tutorial <../../Tutorials/Analysis/BANDAdvancedPEDA.html>`__


.. scmautodoc:: band PEDANOCV

.. only:: html

  .. rubric:: References

.. [#ref1] M.\  Raupach and R. Tonner, *A periodic energy decomposition analysis method for the investigation of chemical bonding in extended systems*, `The Journal of Chemical Physics 142, 194105 (2015) <https://doi.org/10.1063/1.4919943>`__.
