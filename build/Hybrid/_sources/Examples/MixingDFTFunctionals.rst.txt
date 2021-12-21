.. _example MixingDFTFunctionals:

Example: Mixing DFT functionals
===============================

We consider a system of two weakly bonded molecules, namely NH3 and N2. We will use a GGA for the intra molecular interactions and LDA for the intermolecular one.

We look at two bond lengths, an N-H bond within the NH3 molecule, this is the "intra" bond.

The other is the bond from the N in NH3 to an N atom in the N2 molecule: the "inter" bond.

First we run the whole system with LDA and GGA, and finally with the hybrid engine.

The result for the hybrid calculation is that the "inter" bond has the value of the GGA calculation, whereas the "intra" one is equal to the LDA calculated one.


The energy expression used in the hybrid calculation is

.. math::

  E^\text{hybrid} = E^\text{LDA/*} + E^\text{GGA/NH3} - E^\text{LDA/NH3}  + E^\text{GGA/N2} - E^\text{LDA/N2}

Remember that the region * indicates the whole system, i.e. NH3 + N2.

:download:`Download MixingDFTFunctionals.run <../../../examples/Hybrid/MixingDFTFunctionals/MixingDFTFunctionals.run>` 

.. literalinclude :: ../../../examples/Hybrid/MixingDFTFunctionals/MixingDFTFunctionals.run 
   :language: bash 
