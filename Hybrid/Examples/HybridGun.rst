.. _example HybridGun:

Example: Molecular gun with the hybrid engine
=============================================

In this example we are going to really stretch the use of the Hybrid Engine, and shoot bullets (treated with a QM engine) at a surface described at the MM level.

The choice of bullets are HF molecules and the target is a two dimensional BN sheet, that looks like a graphene sheet, with half of the C atoms turned into N and the other half into B atoms. In a BN sheet the atoms have of course a small charge, which we pre calculate with a QM engine (DFTB).

It is important to understand the role of bonds in this example, because the number of atoms is not constant during the simulations, as bullets are fired (and hence appear), ricochet off the surface and hence disappear after a while. They may as well stick to, or penetrate into the surface, but this is beyond the hybrid engine concept.

In this example there are fixed bond orders withing the target and within the bullets. This is because we specify GuessBonds in the two system blocks (target and bullet). When a bullet is added its bonds are automatically added. The hybrid engine itself will never guess bonds and always use what is specified on input. No bonds are ever formed between the bullet and the surface (the QM and MM regions).

:download:`Download HybridGun.run <../../../examples/Hybrid/HybridGun/HybridGun.run>` 

.. literalinclude :: ../../../examples/Hybrid/HybridGun/HybridGun.run 
   :language: bash 
