.. _metatag PERIODICFORCEFIELD:

Periodic ForceField
###################

The forcefield engine can be used to optimize the geometries of periodic systems. When specifying bonds, via the System%Bondorders key block, one should also specify the bonds that pass through a cell boundary. The GUI does this automatically. You can also simply set the key System%GuessBonds to true, and then UFF-guessed bonds will be used. 

When you are having charges, Ewald summation will be used to calculate the Coulomb interaction. Currently this will be fairly slow for 1D and 2D periodic systems, as the classical Ewald trick cannot be applied.


