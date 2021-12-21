Basic philosophy and intended usage
***********************************

We present a flexible python library for molecular dynamics, specialized in multi-scale simulations in a broad sense. At its core, the library interfaces the :ref:`Atomistic Simulation Environment (ASE) <ASE>` [:ref:`1<reference 1>`] molecular dynamics modules with a wide range of molecular mechanics and electronic structure codes. As such, it allows simple dynamics using forces computed with any energy/gradient evaluator provided by the ADF package. 

Additionally, FlexMD allows the partitioning of a system into regions described at different resolution, with the aim of running multi-scale (hybrid) force calculations. Besides the traditional, rigid, multi-scale partitioning, FlexMD includes different schemes for Adaptive Multi-scale Molecular Dynamics. Such simulations allow the resolution of a particle to change according to its distance from a predefined active site, which is a necessity for successful multi-scale description of diffusive systems such as chemical reactions in solution.  

Finally, the library couples the dynamics to rare events techniques, either implemented in FlexMD itself, or accessible through an interface with the PLUMED library for free energy calculations [:ref:`7<reference 7>`], opening the possibility for evaluation on time-scales beyond the reach of standard molecular dynamics simulations.  

The FlexMD package is designed to make simulation options possible that are not available natively in the ADF package. Its flexible nature makes it very versatile, but comes at a cost. This cost might be completely negligible in most simulations, but it can be very high in some cases (usually when combining only cheap methods such as forcefields).  

The intended users for the FlexMD package are those with some Unix/Linux experience and a basic understanding of the  `Python Programming Language <http://python.org/>`__. The user is also supposed to have a basic understanding of the various methods he wishes to combine. For example, if metadynamics is supposed to be combined with ADF, FlexMD expects the user to have knowledge about DFT calculations and the usage of Collective Variables. Finally, as with every computational method, the user should monitor the FlexMD performance, both in accuracy and speed.  

