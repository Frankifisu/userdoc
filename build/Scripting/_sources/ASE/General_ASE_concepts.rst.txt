General Concepts
################

The ASE library makes extensive use of the object oriented programming features included in Python.
`Objects <https://en.wikipedia.org/wiki/Object_(computer_science)>`_ and their corresponding `classes <https://en.wikipedia.org/wiki/Class_(computer_programming)>`_ are therefore the most relevant entities in ASE-based scripts.
While the ASE library consists of very many different classes, they can be subdivided into the following three main groups described in the following section.

Components of ASE
-----------------

Quantum Chemical Model
``````````````````````
Objects like those defined by the `Atoms class <https://wiki.fysik.dtu.dk/ase/ase/atoms.html#module-ase.atoms>`_ represent the core part of ASE.
Different ways to construct Atoms objects are provided by the ASE library, including constructors for specific types of quantum chemical systems such as bulk materials and surfaces, clusters, nanotubes etc. 
During runtime an Atoms object always comprises all available information about the quantum chemical model it describes.
Furthermore, the Atoms class includes the essential `methods for manipulating the atomic model <https://wiki.fysik.dtu.dk/ase/ase/atoms.html#working-with-the-array-methods-of-atoms-objects>`_ under study.

While `Atoms <https://wiki.fysik.dtu.dk/ase/ase/atoms.html#module-ase.atoms>`_ is by far most frequently encountered class in ASE scripts, several other objects have similar purposes in more specialized respective contexts.
The `Constraints and Filter classes <https://wiki.fysik.dtu.dk/ase/ase/constraints.html#module-ase.constraints>`_ are important examples for such cases and serve e.g. to enforce user defined constraints on the system upon geometry relaxation.

Quantum Chemical Calculation
````````````````````````````
`Calculator classes <https://wiki.fysik.dtu.dk/ase/ase/calculators/calculators.html#module-ase.calculators>`_ provide the definition of the quantum chemical computation required to obtain the desired physical property of models defined by the Atoms objects.
Such classes essentially interface ASE to a specific quantum chemistry program and contain methods necessary to transfer input information to this program as well as to retrieve the corresponding results after the completion of the program run.

Calculators are essential for the aforementioned Atoms object to be fully applicable.
As an example, most physical properties of a system represented by an Atoms object require a prescription about how to actually compute the result, which is in turn mediated by the assigned Calculator class.
Due to that, Calculator objects usually become part of the Atoms object during an ASE run (see also the next section).

The ASE variant within the Amsterdam Modeling Suite includes five `additional Calculator classes <SCM_ASE_Calculators.html>`_ which enable computations with `ADF <../../ADF/index.html>`_, `BAND <../../BAND/index.html>`_, `DFTB <../../DFTB/index.html>`_ and `ReaxFF <../../ReaxFF/index.html>`_ from within ASE, respectively.

Simulation Definitions
``````````````````````
Finally, a third type of class (denoted as Simulation object in the following) represents the actual simulation which is conducted for a given combination of Atoms and Calculator objects.
Such a Simulation object can for example either represent a simple
`geometry relaxation <https://wiki.fysik.dtu.dk/ase/ase/optimize.html#module-ase.optimize>`_,
a `(numerical) frequency <https://wiki.fysik.dtu.dk/ase/ase/vibrations/vibrations.html>`_
or `phonon calculation <https://wiki.fysik.dtu.dk/ase/ase/phonons.html#module-ase.phonons>`_,
a `transition state search <https://wiki.fysik.dtu.dk/ase/ase/neb.html>`_,
or an entire `gobal optimization <https://wiki.fysik.dtu.dk/ase/ase/ga.html#module-ase.ga>`_ or `molecular dynamics simulation <https://wiki.fysik.dtu.dk/ase/ase/md.html#module-ase.md>`_.

A Typical ASE Run
-----------------

In a standard ASE run objects of the three kinds presented above interact in order to perform the intended calculations.
A typical ASE run is organized as follows

Definition and Initialization of Objects
   Mind that there are alternative, usually more convenient ways to define a chemical system from file inputs or system specific presets

   ::

        MySystem     = Atoms( <initializing variables> )
        MyCalculator = <CalculatorClass>( <options> )

Calculator → Atoms
   The Calculator object is assigned to the Atoms object and becomes part of it.

   ::

        MySystem.set_calculator( MyCalculator )

   The methods of the Atoms object that refer to calculated results can then directly call methods from the Calculator.

Atoms → Simulation
   The Atoms object is used as one of the initialization variables for the constructor of the Simulation object.

   ::

        MySimulation = <SimulatorClass>( MySystem, <options> )

   The Simulation object is now able to automatically alter the System object (e.g. by setting new atomic coordinates during a geometry relaxation) as well as to request the calculation of the required physical properties for the current status of the system.
   The simulation can be started as follows.

   ::

      MySimulation.run( <options> )
   

Evaluation
   It is sometimes convenient to print or further evaluate the result  e.g. by calculating the reaction energies between two different Systems

   ::

        MyReactands = Atoms(..., calculator = MyCalculator(), ...)
        MyProducts  = ...

        # Relax both, MyReactands and MyProducts
        ...

        E_R = MyReactands.get_potential_energy()
        E_P = MyProducts.get_potential_energy()

        print 'ReactionEnergy (eV) = ', E_P - E_R   

   Mind that ASE exclusively uses eV and Å as units of energy and length, respectively.
