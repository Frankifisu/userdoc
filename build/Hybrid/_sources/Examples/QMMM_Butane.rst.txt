.. _example QMMM_Butane:
.. _example AtomicInfoForCappingAtom:

Example: QMMM with capping atoms
================================

This is an example of QMMM using capping atoms. Capping atoms are added automatically when bonds are broken (between the QM and MM region).
Because the amber forcefield is used the ``AtomicInfoForCappingAtom`` needs to be set, as the default type "H" is not an AMBER type.

:download:`Download QMMM_Butane.run <../../../examples/Hybrid/QMMM_Butane/QMMM_Butane.run>` 

.. literalinclude :: ../../../examples/Hybrid/QMMM_Butane/QMMM_Butane.run 
   :language: bash 
