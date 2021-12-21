FlexMD functionality summary
****************************

.. _metatag FUNCTIONALITY: 

**Molecule**

Input/output

+ Reads and writes PDB and XYZ files
+ Reads and writes topology data (in CHARMM format)
+ Reads and writes force field data (on CHARMM format)

Analysis

+ Extracts geometry data

Drawing functionality

+ Adds atoms and bonds
+ Changes bond-lengths, angles and torsions
+ Cuts fragments
+ Cuts solvent boxes and droplets
+ Performs rotations and translations, to fit bonds to axes and planes

Periodic functionality

+ Adds periodic images
+ Wraps molecules into periodic box

Water specific 

+ Finds hydrogen bonds
+ Finds shortest water bridge connecting H-donor and acceptor

**Energy and force calculations**

Standard

+ ADF
+ DFTB
+ REAXFF
+ UFF
+ MOPAC
+ NAMD
+ Lennard-Jones force fields

Multi-scale

+ QM/MM, mechanical embedding: Combines all the codes above
+ Hybrid: More flexible than QM/MM. Combines different force calculations by summing or subtracting the energies and forces. The standard calculations (above) can therefore be combined with:

  + Metadynamics
  + Plumed (external code that computes free energy data)
  + Constraints

+ Adaptive QM/MM (for chemistry in solution) 

  + Difference-based Adaptive Solvation (DAS)
  + Sorted Adaptive Partitioning (SAP)
  + Buffered-Core (BC)
  + Flexible Inner Region Ensemble Separator (FIRES)

**Molecular Dynamics**

+ Uses ASE as the molecular dynamics driver for all above methods
+ Analyses trajectories

