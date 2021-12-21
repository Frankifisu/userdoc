.. _bondboost:

Bond Boost Method
*****************

.. tip::
  See also the advanced `bond boost tutorial <../Tutorials/MolecularDynamicsAndMonteCarlo/PolymersBondBoost.html>`__ .

The bond boost method implemented here is described in [A. Vashisth, C. Ashraf, W. Zhang, C.E. Bakis, and A.C.T. van Duin, *Accelerated ReaxFF simulations for describing the reactive cross-linking of polymers*, J. Phys. Chem.  A, 2018, 122 (32), 6633-6642]. In this method, the distances between atoms that are relevant to the reaction of interest are calculated to determine the orientation of the reactant molecules. If a suitable initial configuration is recognized, an additional restraint energy (possibly consisting of more than one term) is added to the system that is intended to stretch or compress bonds at a pre-defined rate such that this additional energy can help achieve the energy to cross the reaction barrier. A single term of the restraint energy is given by 

:math:`E_{ij}^{rest} = F_1 * (1 - e^{-F_2 (R_{ij} - R_0) ^2 })`

Where 
:math:`E_{ij}^{rest}` - restraint energy between atoms i and j in kcal/mol;
:math:`F_1` and :math:`F_2` - parameters for restraint energy in units of kcal/mol and :math:`Å^{-2}`, respectively;
:math:`R_0` - target distance (in Å) between two atoms according to the restraint;
:math:`R_{ij}` - actual distance (in Å) between the two atoms under consideration.

The input for this method is given via the tracking.in file, which has the following format::

  #Distance regimes
  #T pair1: at1 at2 min max  pair2: at1 at2 min max  pair3: at1 at2 min max  pair4: at1 at2 min max  pair5: at1 at2 min max
   5         Si  O  1.5 1.8          O   H  0.9 1.3          H   O  0.9 1.3          O  Si  1.5 1.8         Si   O  1.5 1.8
  #Restraint settings
  #iter nr. r1: at1 at2  R0   F1   F2  r2: at1 at2  R0   F1    F2  r3: at1 at2  R0   F1    F2  r4: at1 at2  R0   F1   F2
  10000  4       2   5  1.80 500.0 1.0      2   3  3.00 100.0 0.10      3   6  1.00 500.0 0.25      5   6  3.50 250.0 0.1
  

A hash sign in the first position on a line begins a comment. The first non-comment line contains atom symbols and min/max distances for detection of the initial configuration. The first number (5 in the example above) specifies the number of atom pairs. For each pair, the minimum and maximum distances are specified and the fist atom in each pair after the first corresponds to the second atom in the previous one. This means that the first element symbol in pair 2, 3, etc. is actually ignored. Thus, the example above defines a chain of atoms Si-O-H-O-Si-O with R(Si-O) in the (1.5,1.8) range and R(O-H) in the (0.9,1.3) range. It should be noted that when detecting the initial configuration, an atom may enter the chain more than once. This allows ring configurations to be specified although the ring must consist of at least 4 atoms. 

.. Note::

   When detecting coordinates, the program uses alternative atom names specified after the atomic coordinates in the *geo* file. Since this name is generally not used to detect the ReaxFF element name, one can allow only a subset of A-B bonds to be boosted by giving certain atoms different alternative names. If more than one suitable configuration is found the one with the smallest sum of distances is used to create the restraints.
  

When a configuration matching these criteria is found, parameters specified on the second non-comment line are used to add restraints. The first number specifies the number of time-steps the restraint must remain active for (10000 in this case, which should be long enough for the reaction to take place). During this time no configuration detection is performed. In other words, only one set of restraints may be active at a given time. The second number on the line specifies the number of restraints to add (4 in this case). For each restraint, two indices and three parameters are specified. The indices correspond to positions of the atoms in the chain specified on the first line. In the example above, the restraint is set in such a way that the O2-H3 and Si5-O6 bonds are broken and Si5-O2 and O6-H3 bonds are formed. The results of the detection are written to the fort.84 file together with the imposed restraints.
