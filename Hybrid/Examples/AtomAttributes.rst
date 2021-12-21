.. _example AtomAttributes:

Example: The effect of specifying atom types, or not
====================================================

Whether or not you specify the ForceField.Type on input (via atom attributes) makes a difference for the hybrid engine using a ForceField sub engine.

If you do, then for all regions these atom types will be used.

If you do not specify them, then for each region independently the atom typing will done automatically (if possible).

:download:`Download AtomAttributes.run <../../../examples/Hybrid/AtomAttributes/AtomAttributes.run>` 

.. literalinclude :: ../../../examples/Hybrid/AtomAttributes/AtomAttributes.run 
   :language: bash 
