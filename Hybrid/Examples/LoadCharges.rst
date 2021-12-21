.. _example LoadCharges:

Example: Loading MM charges for regions
=======================================

In this example we consider an OH- with an H3O+ fragment. As the charges on the fragments are kept fixed, the formation of two water molecules is avoided.

First we "estimate" the charges for the two fragments with a DFTB calculation.

These charges are then loaded for the correct regions in the total system. Observe that this is done in the ``System`` block, see the `System definition section of the AMS manual <../../AMS/System.html>`__.

We do this first for a QUILD-like setup (mechanical embedding), and next for a QMMM calculation with electrostatic coupling.

:download:`Download LoadCharges.run <../../../examples/Hybrid/LoadCharges/LoadCharges.run>` 

.. literalinclude :: ../../../examples/Hybrid/LoadCharges/LoadCharges.run 
   :language: bash 
