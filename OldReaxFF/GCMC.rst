

Grand Canonical Monte Carlo (GCMC)
**********************************


.. toctree::
   :maxdepth: 2



General info
============

.. tip::
  Take a look at the `GCMC tutorial <../Tutorials/MolecularDynamicsAndMonteCarlo/GCMCLiSBattery.html>`__ and learn how to setup a GCMC calculation.

**About Monte Carlo / the Grand Canonical Ensemble** 

It is best to read a bit about Monte Carlo and ensembles before working with the GCMC code. Almost every book or review text on molecular simulations will do, for example: Frenkel D, Smit B. Understanding molecular simulation: from algorithms to applications. Academic Press; 2002. 672 p.  

Wikipedia also has some pages of interest:  

+  `http://en.wikipedia.org/wiki/Monte_Carlo_method <http://en.wikipedia.org/wiki/Monte_Carlo_method>`__

+  `http://en.wikipedia.org/wiki/Grand_canonical_ensemble <http://en.wikipedia.org/wiki/Grand_canonical_ensemble>`__

It is important to note that this method heavily relies on random numbers, and simulations are thus non-repeatable in detail, but should converge to the same answer. 

**About the Reaxff GCMC code** 

The GCMC code for reaxff was originally developed by Thomas Senftle, working as a Graduate Student at Penn State University under the supervision of Dr. Adri van Duin. The original version was a wrapper code that called an external executable to perform the reaxff minimization step and energy calculation, and relied on file modification and parsing to steer the reaxff code and get the results back. 

A rewrite of the code, made by Hans van Schoot (SCM) in close collaboration with Thomas Senftle, is now available in the ADF package. The rewrite directly integrates into the ADF-ReaxFF code, solving performance issues of the original code by removing the calling overhead of the reaxff executable and the relatively slow file management. It also merged several modifications of the original code to support the usage of whole molecules for Monte Carlo moves, and supports the usage of multiple atom/molecule types during the simulation. Other improvements were made on the input options, the accessible volume calculation, the MC acceptance prefactor calculation and the writing of logfiles. 

The relevant papers are: 

Thomas P. Senftle, Randall J. Meyer, Michael J. Janik and Adri C.T. van Duin,
*Development of a ReaxFF potential for Pd/O and application to palladium oxide formation*,
`J. Chem. Phys. 139, 044109 (2013) <https://doi.org/10.1063/1.4815820>`__

Thomas P. Senftle, Adri C.T. van Duin, Michael J. Janik,
*Determining in situ phases of a nanoparticle catalyst via grand canonical Monte Carlo simulations with the ReaxFF potential*,
`Catalysis Communications volume 52, 5 July 2014, Pages 72–77 <https://doi.org/10.1016/j.catcom.2013.12.001>`__


Input
=====

A worked out GCMC exercise is available from a `2-day ReaxFF workshop <https://www.scm.com/adf-modeling-suite/adf-hands-on-workshops/advanced-2-day-reaxff-workshop/>`__.

**Overview** 

The GCMC code in ADF-ReaxFF needs the following input files to run: 

+ control_MC    : The GCMC control file, which holds MC settings and the atoms/molecules to insert/move/delete

+ control       : A reaxff control file, in which only a small number of parameters is of interest

+ ffield        : A standard reaxff forcefield file

+ geo           : A geometry file, preferably in biograph format (code not yet tested with xyz)

+ iopt          : Text file that should only contain a "5" (without the quotes)

+ insertData_MC : (optional file) Table used when restarting GCMC simulations


**the control_MC file** 

Lines in the control_MC file that start with ! or # will be ignored, so those can be used for comments. Empty lines are also ignored, so feel free to leave some in the file. Lines with keywords should have their value in the first 8 columns, followed by a couple of spaces (at least 1), followed by the 6-character keyword. The order is free, except for the nmols keyword, which should be the last one. The nmols keyword signals the parser that the next section of control_MC will define X new MC Molecule Types. 

This is an example for the control_MC file: 

::

   ! GCMC control file example
         0   iensmb !select MC ensemble (0=Mu-NVT with fixed volume, 1=Mu-NPT with variable volume)
      5000   niter  !number of MC iterations to do this simulation
         0   nstart !start the iteration counter with an offset, usefull for restarts to avoid double files
     300.0   mctemp !Temperature of the simulation, affects acceptance rate for steps that increase the energy
       0.0   mcpres !NPT pressure in GPa (set to zero for incompressible solid systems unless at very high pressures)
       3.0   rmaxpl !Max radius for atom placement on insert/displace move
       1.2   rminpl !Min radius for atom placement on insert/displace move
      2000   nmctry !Maximum number of trials allowed when inserting or moving a molecule. If the
   !                !  rmaxpl and rminpl variables are very strict, this number needs to be large
         1   igcfac !include GC prefactor in probabilities? 0 = no 1 = yes
         0   ivol   !select MC volume calculation technique:
   !                !  0: vvacu needed! volume = total volume - occupied volume - specified vacuum volume (vvacu)
   !                !  1:               volume = total cell volume
   !                !  2: vacc needed!  volume = specified accessible volume (vacc)
   !                !  3:               volume = total cell volume - occupied volume
   !                !  4: vacc needed!  volume = specified accessible volume (vacc) - occupied volume
     435.0   vacc   !if ivol=2 or ivol=4, specify Vacc in angstroms^3
       0.0   vvacu  !if ivol=0 specify non-accessible (vacuum) volume Vvacu in angstroms^3
      0.25   ivlim  !volume change limit (value between between 0 and 1, Vnew = ((1+ivlim)*V1) 
         1   resopt !write restart files: 0=no, 1=yes
         1   resfrq !frequency of writing restart files (MC code only writes files if the MC move is accepted)
         0   debug  !print debug output if set to 1, print even more debug output when set to 2
         5   nmols  !Number of MC molecule types, must match the number of molecule blocks that follow!
   !
   ! Molecule Specific Data: C2H2 example
   !    This part is fixed format! 
   !    We need cmpot on line 1, 
   !    possibly followed by the noinsr on line two,
   !    and forced to be ended with nmatom on line 2 or 3, followed by nmatom lines of coordinates.
   ! the coordinates are FIXED FORMAT! (24d.15,1x,A2) x,y,z (24 wide, 15 after decimal), 1 space, 2chars symbol)
    -75.00   cmpot   !chemical potential of molecule
         4   nmatom  !number of atoms in molecule
         12.180480000000000       0.421696000000000       1.316689000000000 C 
         13.124731000000000       0.376902000000000       0.568360000000000 C 
         11.349475000000000       0.459560000000000       1.988208000000000 H 
         13.957314000000000       0.335843000000000      -0.101000000000000 H 
   
   !Molecule Specific Data: C2H4 example
    -75.00   cmpot   !chemical potential of molecule
         6   nmatom  !number of atoms in molecule
         13.989222000000000       0.405391000000000       1.000150000000000 C 
         13.316784000000000       0.399646000000000       0.885795000000000 C 
         11.494513000000000       0.461837000000000       1.970612000000000 H 
         11.335219000000000       0.353577000000000       0.129581000000000 H 
         13.811701000000000       0.340224000000000      -0.084000000000000 H 
         13.970561000000000       0.453325000000000       1.756236000000000 H 
   
   !Molecule Specific Data: H2O Example
    -75.00   cmpot   !chemical potential of molecule
         1   noinsr  !setting this to 1 disables insert/deletion moves. If it is set to 1 for all types, the ensemble becomes NVT/NPT
         3   nmatom  !number of atoms in molecule
         39.996720000000000      40.747660000000000      40.512210000000000 H 
         40.000210000000000      39.999520000000000      39.934730000000000 O 
         40.000030000000000      39.259880000000000      40.523700000000000 H 
   
   !Molecule Specific Data: H2 Example
    -75.00   cmpot   !chemical potential of molecule
         2   nmatom  !number of atoms in molecule
          5.025812000000000      0.0000000000000000       0.000000000000000 H 
          5.774188000000000      0.0000000000000000       0.000000000000000 H 
   
   !Molecule Specific Data: Single atom example
    -75.00   cmpot   !chemical potential of molecule
         1   nmatom  !number of atoms in molecule
          0.000000000000000      0.0000000000000000       0.000000000000000 H 

The Molecule Specific Data blocks define the molecules (or atoms) that can be inserted/moved/deleted with the MC code. The atoms named here should of course be in the forcefield files, and the coordinates should form a reasonable structure. The MC code uses these coordinates during the insertion step by giving them a random rotation, followed by a random translation to generate a random position of the molecule inside the box. Currently, there is no check to make sure the molecule stays inside the boundaries of the box, the code only checks that the rmaxpl/rminpl values are satisfied. If you plan on inserting large molecules, make sure there is enough room in the rmaxpl value, otherwise the code will stop with an error message. 

**The chemical potential (cmpot) keyword** 

The cmpot keyword sets the chemical potential of the molecule (or atom) reservoir, and is employed when calculating the Boltzmann accept/reject criteria after a MC move is executed. This value can be derived from first principles using statistical mechanics, or equivalently, it can be determined from thermochemical tables available in literature sources. 

For example, the proper chemical potential for a GCMC simulation in which single oxygen atoms are exchanged with a reservoir of O2 gas, should equal 1/2 the chemical potential of O2 at the temperature and pressure of the reservoir: 

cmpot = Mu_O(T,P) = 1/2*Mu_O2(T,P) = 1/2 * [Mu_ref(T,P_ref) + kT*Log(P/Pref) - E_diss] 

where the reference chemical potential [Mu_ref(T,P_ref)] is the experimentally determined chemical potential of O2 at T and Pref, kT*Log(P/Pref) is the pressure correction to the free energy, and E_diss is the dissociation energy of the O2 molecule. 

**The no insert (noinsr) keyword** 

The noinsr keyword tells the GCMC code to keep the number of molecules/atoms of this type fixed. It will thus disable Insert/Delete moves on this type, meaning it can only do a displacement move, or volume change move (if the iensmb keyword is set to 1). 

**the control file** 

The control file is a regular reaxff control file and it influences the minimization step after an MC trial move. Because of this, only a small number of the reaxff keywords are used during the GCMC simulation. 

An example of the control file: 

::

   # some of the parameters that influence the minimization step in the GCMC code
         1 icentr     Put the center of mass at the center of the cube
         1 igeofo     0:xyz-input geometry 1: Biograf input geometry 2: xmol-input geometry
   2.50000 endmm      End point criterion for MM energy minimization
       500 imaxit     Maximum number of iterations
         0 icelop     Optimize cell parameters 0=no 1=yes
   1.00050 celopt     Cell parameter change
         0 imaxmo     In this case: 0: POLAK_RIBIERE Conj.Grad method, 1: Limited-memory BFGS method

The code has been tested with various imaxit and endmm values, the other options have not been fully tested. Other reaxff keywords might also influence the minimization procedure, but those are best left to their default settings 

**the ffield file** 

The ffield file should be an normal reaxff forcefield file, as described in the reaxff documentation by A. van Duin (visit the documentation section on the SCM website to obtain this document). 

**the geo file** 

The GCMC code has been tested with biograph input files, but other input formats might work. The details of this file are also described in the original reaxff documentation by van Duin. 

**the iopt file** 

The iopt file is a text file with a single digit inside that selects the execution mode of the reaxff code. To run the GCMC code, this file should contain a "5" (without the quotes). 

**the insertData_MC file** 

The GCMC code can insert multiple atom/molecule types in a single simulation, so it needs to keep track of what atom belongs to which insert. This information is automatically stored and updated when insertion/deletion/moving of atoms or molecules during the simulation, but is by default unknown of the atoms of the starting geometry. The GCMC code will therefore by default not modify the atoms in the original input in the MC trial moves (keep in mind that they can move around during the minimization step). the insertData_MC file can be used to tell the GCMC code what atoms in the geo file belong to which molecule. 

An example of the insertData_MC file: 

::

   #   atomNumber  MCInsMolType  MCInsertNmbr
         30       1       1
         40       2       1
         46       2       1
         47       1       2
         48       1       3

This example specifies 4 molecules/atoms that are modifiable by the GCMC code, belonging to 2 different GCMC molecules/atoms that are defined in the control_MC file. The first "molecule" in the control_MC file should thus consist of a single atom (if this doesn't match, the code will most likely crash!). It was inserted three times (atom 30, 47 and 48) The second molecule has two atoms, and was inserted once. 

The atoms do not have a fixed order, and not all atoms have to be defined. If an atom is not appointed to a certain MCInsMolType and MCInsertNmbr, if will simply not be modified during the MC moves. The insertData_MCXXXXXX files generated by the restart option of the code can be directly used as valid insertData_MC files, just remove the digits from the filename and replace the geo file with the corresponding geo_MCXXXXXX file. 


Output
======

**Overview** 

The GCMC code writes a couple of output files, each described in this section. It also produces a number of reaxff output files, and some of these are described in the original reaxff documentation by van Duin. Keep in mind that these files might not provide a complete or correct picture of the simulation, as they could also contain data originating from rejected MC trial moves. 

**geo_MCXXXXXX** 

This file is generated every X accepted MC moves and contains the current geometry of the system in biograph format (X is set with the resfrq keyword in the control_MC file). 

**insertData_MCXXXXXX** 

This file contains a table of all the atoms in the system with their MC Molecule Type and MC Insert Number. This data can be used to map atoms to an inserted molecule, and is needed if you want to restart your calculation from an accepted MC step. The table contains -1 values for atoms that were in the original input and did not get a manually assigned MCInsert Molecule Type and MC Insert Number, the GCMC code will not modify these atoms during the MC steps. 

Also see the section on insertData_MC file. 

**MCstats** 

The MCstats file is a logfile that contains the statistics of the MC simulation. The GCMC code writes a single line to it after every MC step, containing the number of: Tried MC moves (tried), Accepted MC moves (accept), Rejected MC moves (reject), Accepted Insertion/Deletion/Moving/Volume change MC moves (addAcc/delAcc/mvAcc/volAcc), Rejected Insertion/Deletion/Moving/Volume change MC moves (addRej/delRej/mvRej/volRej) 

An example of the MCstats file: 

::

     tried accept reject    addAcc delAcc  mvAcc volAcc    addRej delRej  mvRej volRej
         0      1      0         1      0      0      0         0      0      0      0
         1      1      1         1      0      0      0         0      0      1      0
         2      1      2         1      0      0      0         0      0      2      0
         3      1      3         1      0      0      0         0      1      2      0
         4      1      4         1      0      0      0         1      1      2      0
         5      1      5         1      0      0      0         1      1      3      0
         6      1      6         1      0      0      0         1      2      3      0
         7      1      7         1      0      0      0         1      3      3      0
         8      1      8         1      0      0      0         1      3      4      0
         9      1      9         1      0      0      0         1      4      4      0
        10      1     10         1      0      0      0         1      4      5      0
        11      2     10         2      0      0      0         1      4      5      0
        12      3     10         3      0      0      0         1      4      5      0

**Elog** 

The Elog file contains the Volume and energies of the accepted MC steps. The energies in this logfile are the pure ReaxFF energy of the system (RxFFEnergy) and the MC corrected energy, which is used in determining if the step should be accepted or not (see the section on calculating energies for details). 

An example of the Elog file:

::

    Iteration Naccepted      Volume   MC Energy  RxFFEnergy
            0         1    15625.00    -3098.88    -3179.88
            2         2    15625.00    -3107.92    -3269.92
            3         3    15625.00    -3130.13    -3373.13
            4         4    15625.00    -3160.05    -3484.05
            6         5    15625.00    -3169.77    -3493.77
           11         6    15625.00    -3200.13    -3605.13

**reaxout.kf** 

This is the binary logfile generated by the GCMC code. Its contents can be viewed with the KFBrowser utility, or it can be loaded into AMSmovie to view the geometries in the file. Only the data of successful MC moves is written to this file. 


Code Details
============

**Overview** 

The GCMC code will perform niter (control_MC file option) Grand Canonical Monte Carlo trial moves, and accept or reject them based on the Energy produced by the ReaxFF minimization step of the trial geometry. The Monte Carlo algorithm will always accept a step if it results in a decrease of the energy, and accept steps that go up in energy with a probability. This section will give some details about how the code works. 

**MC Moves (Insert/Delete/Move/Volume)** 

The GCMC code currently supports 4 types of MC Moves: Insert, Delete, Move (displace), Volume change. The first three moves always change a whole "molecule" of the system, as defined in the control_MC file (a molecule can of course contain only a single atom). Every MC iteration selects one MC Molecule Type from the defined molecules in control_MC at random, followed by a random MC Move (unless there are no molecules of the type in the system, in that case it will do an insert move). 

The Insert and Displace (move) MC Moves will generate a random rotation and position for the molecule, and then check if the random positions are within the "RminPl" and "RmaxPl" boundaries (this means no atom in the molecule can be closer to any atom currently in the system than "RminPl", and it should be within "RmaxPl" distance to an atom in the system). If the conditions are not satisfied, a new set of coordinates is generated and the code checks again. This is repeated a maximum number of "nmctry" times before stopping with an error. 

The volume change is controlled by the "ivlim" variable in control_MC. The ivlim sets the volume change limit, and it should be a value between between 0 and 1. The new volume will be calculated like this: Vnew = (1+ivlim)*Vold. 

**Calculating energies** 

Because the GCMC simulation adds and deletes atoms or molecules during the runtime, it cannot directly compare the ReaxFF energies for the MC acceptance criteria: inserting a molecule will usually lower the total energy of the system, causing the MC to always accept it, and always reject a deletion. To balance this out, the GCMC code calculates a "corrected" MC energy to compare the trial reaxFF energy with, consisting of the previously accepted ReaxFF energy + the chemical potential (cmpot in control)MC) for the inserted molecule, or the ReaxFF energy - the chemical potential for the deleted molecule. The volume change energy is also corrected, using the following formula: 

E_MC_Corr = E_reaxff_last_accept - (Pressure * 0.1439 * (newV-oldV)) + ((1.0/beta) * nInsertedMols * log(newVavail/oldVavail)) 

where newVavail and oldVavail are calculated from the MC available volume (see the section calculating volumes). 

**Calculating volumes** 

The GCMC code can calculate the available volume in a couple of different ways, depending on the ivol setting in control_MC: 

+ ivol = 0: volume = total volume - occupied volume - specified vacuum volume (vvacu)

+ ivol = 1: volume = total cell volume

+ ivol = 2: volume = specified accessible volume (vacc)

+ ivol = 3: volume = total cell volume - occupied volume

+ ivol = 4: volume = specified accessible volume (vacc) - occupied volume

Where the occupied volume is calculated by summing up the volumes of the atoms in the geo file that are not specified to be part of an MC type molecule. The volume of an atom is calculated using the average of the covalent atomic radius and the vd Waals radius of the atom, which are found in the reaxff forcefield file (ffield). 

the vacc and vvacu options can be specified in the control_MC file to get a more accurate available volume. 

**Acceptance criteria** 

An MC move is always accepted if the reaxff energy is lower than the corrected MC energy of the last accepted MC move, or if the energy increase is small enough. If the new energy is higher, the code generates a random number between 0 and 1, and accepts the move if the random number is bigger than: 

::

   prob = preFactor * exp(-Beta*deltaE)

Where the prefactor is calculated (for insert and delete moves) using the deBroglie wavelength of the inserted molecules, the number of inserted molecules and the available MC volume of the system. 



