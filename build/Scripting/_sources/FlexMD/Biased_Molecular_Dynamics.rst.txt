Biased Molecular Dynamics
*************************

.. _metatag BIASEDMD: 

Constraints can be added to a simulation using the derived **ForceJob** class **WallJob**. The constraint is in the form of a large one-dimensional Gaussian on the potential energy surface, along a predefined Collective Variable (CV). Examples of CV’s are the distance between two atoms, the coordination number of two atoms, but also more complex quantities such as the minimum distance between two sets of atoms, or the distance of an atom to a hydroxide ion. The Collective Variables can be specified through the **CollectiveVariable** class. Derived **CollectiveVariable** classes are available to specify  sums or multiples of other **CollectiveVariable** objects. 

Regular MD calculations are limited in the time-scales achievable with current hardware. The order of such time-scales is much smaller than what is required for chemical reactions. To overcome this problem, two rare-events methods have been implemented directly into the library: metadynamics [:ref:`5<reference 5>`] and umbrella sampling [:ref:`6<reference 6>`]. Both these methods involve biasing the simulations along a CV. An example of a metadynamics input can be found in the examples directory in examples/scmlib/metadynamics_emt_h2o. 

For a wider range of rare-events methods, FlexMD also offers an interface with the PLUMED library for free energy calculations [:ref:`7<reference 7>`].To use this, a PLUMED input file is required, and for this we refer to the PLUMED manual. An example of a FlexMD input script using PLUMED can be found in the examples directory in examples/scmlib/plumed_emt_h2o. 

