.. _AMSPREP: 
.. index:: amsprep module 

AMSprep: generate (multiple) ADF jobs
=====================================

AMSprep allows one to generate input files for the different programs of the Amsterdam Modeling Suite by means of console commands.
As such AMSprep can be used to run the same type of calculation on a series of different chemical systems.
Another important example are automatic checks of the convergence of the results with respect to the computational parameters e.g. by varying input settings such as basis set choice or numerical integration accuracy while recomputing the same system.

AMSprepare ($AMSBIN/amsprep) generates a job script from a template .ams file.
Such a template file can either be produced by AMSinput or simply be found among the default templates included.
These default templates are identical to those present in AMSinput.

Two **examples** are presented here to demonstrate the capabilities of AMSprep:

* In `BakersetSP <../../ADF/Examples/BakersetSP.html>`__ you will see how to use amsprep to run a particular job for a test set of molecules. The individual molecular structures are provided as xyz-files which contain no ADF specific information. AMSreport is used to collect the values of the bonding energies resulting from these calculations.

* In `ConvergenceTestCH4 <../../ADF/Examples/ConvergenceTestCH4.html>`__ you will see how to use AMSprep to test convergence of the bonding energy with respect to the basis set and the numerical integration grid.

The options of AMSprep are listed when running the module without further command line arguments, or with the -h flag:

::

   % amsprep -h
   AMSprepare (amsprep) generates a job script from a .ams file (the template),
   with user specified changes to input options / method / system.
   
   Usage: amsprep -t template.ams [-m molecule.(ams|adf|xyz|mol|t21)] [-z charge] [-s spin]
                                  [-runtype SinglePoint|GeometryOptimization|Frequencies]
                                  [-gradientsonly]
                                  [-q quality] [-zlmfit quality] [-kspace quality]
                                  [-lattice v1.x v1.y v1.z ...]
                                  [-i integration] [-b basis] [-c core] [-r relativity]
                                  [-basiscacheid id]
                                  [-x xcpotential] [-e xcenergy] [-bondsonly]
                                  [-dftbmodel DFTB|SCC-DFTB|DFTB3] [-dftbparameters dir]
                                  [-dftbdispersion None|Default|D3-BJ|D2|ULG|UFF]
                                  [-logfile logfile] [-j jobname] [-a amsfile]
                                  [-dist "atom1 atom2 distance ..."]
                                  [-angle "atom1 atom2 atom3 angle ..."]
                                  [-dihed "atom1 atom2 atom3 atom4 angle ..."]
                                  [-atomtype "atom type ..."]
                                  [-structure "atom structure ..."]
                                  [-pointcharges file]
                                  [-efield "Ex Ey Ez"]
                                  [-rxforcefield fname] [-rxniter n] [-rxnrstep n] [-rxtstep T]
                                  [-rxmethod method] [-rxmdtemp T] [-rxmdpres p]
                                  [-region "name at1 at2... "]
                                  [-fragments prefix] [-onejob]
                                  [-g "key value"]
   
   
   Start with a job template, adjust it for this particular job, and write the resulting job
   to standard output. Values specified should match exactly the values as you would specify
   using AMSinput, also for menu choices.
   
   TEMPLATE
   -t: the .ams file (saved by AMSinput) to be used as template, defining the whole job
       All other options override values from this job

       Instead of a .ams file, you may also specify the name of one of the standard templates
       as defined in AMSinput: "Single Point", Frequencies, "Geometry Optimization", etc
       A special option for energy and gradients 
       for the current geometry: EG (see also -gradientsonly)
   
       Some shortcuts: SP, EG, GO, FREQ, optionally prefixed by (ADF|BAND|DFTB|UFF|MOPAC)-
       For example: ADF-FREQ, BAND-SP, DFTB-GO, MOPAC-EG

       Some ReaxFF shortcuts: REAXFF-EG for a single ReaxFF iteration

   CHANGES TO TEMPLATE
   -m: the molecule to use, element types and coordinates
       This can be taken from anything that AMSinput can import,
       for example .ams, .mol, xyz or .t21 files
   
       The -m flag may be repeated, each molecule added will be in its own region
       This may be used for fragment calculations, but it does not work with .ams files
   
       If you specify an .sdf file, you can select which frames to import:
           conformers.sdf#1-10         loop over the first 10 frames
           conformers.sdf#e2.0         loop over all frames with energy below 2.0 
              (units as in the file, wrt the lowest energy of all frames in the file,
              energies from comment lines)
           conformers.sdf#1-10e2.0     loop over the first 10 frames,
                                       and use only those  with energy below 2.0
           conformers.sdf              use the first frame of the sdf file
   
       If you specify a .t21 file, you can select which frames or range of frames to import:
           ajob.t21#ircf3               3rd frame in the IRC forward path
           ajob.t21#ircb2               2nd frame in the IRC backward path
           ajob.t21#h7                  7th frame in the history
           ajob.t21#lt8                 8th frame in the LT path
           ajob.t21#ircf3-10            IRCForward frame 3, 4, ... 10
           ajob.t21#ircf                IRCForward all frames, starting at 1
           ajob.t21#ircf0-              IRCForward all frames, starting at 0 
                                        (original geometry, before first step)
   
       If you specify a .cry file, the compound to import may be specified:
           $AMSHOME/atomicdata/Molecules/Crystals/Cubic/CsCl.cry#MgTl
   
       When looping, all resulting jobs will be joined together, the jobname and ams files
       get the frame sequence number appended after an _ 
       When looping only one -m flag may be specified
   
   -xyz: use xyz coordinates from specified file, not touching anything else
         it is applied after -t and -m
         the elements and number of atoms should match
         currently works with KF and xyz files
   -smiles: use smiles to describe the molecule
   
   -irc: when using IRC frames in the -m flag, revert the backwards order
   
   -dist: change the distance between atom1 and atom2 to the specified distance
          the arguments must be enclosed in quotes, and may be repeated for multiple distances
   -angle: change the angle (atom1, atom2, atom3) to the specified angle
          the arguments must be enclosed in quotes, and may be repeated for multiple angles
   -dihed: change the dihedral (atom1, atom2, atom3, atom4) to the specified angle
          the arguments must be enclosed in quotes, and may be repeated for multiple angles
   -atomtype: set the type (element) of atom to type
          the arguments must be enclosed in quotes, and may be repeated for multiple types
   -structure: add a structure just as if using the structure tool in AMSinput
          atom is the selected atom, structure is the name of the structure file
          the arguments must be enclosed in quotes, and may be repeated for multiple changes
   -liststructures: list available structure files for use with -structure, and exit
   
   -runtype: run type (SinglePoint,GeometryOptimization,Frequencies)
   -gradientsonly: after calculating the gradients, stop
                   works also for excited state gradients if requested in your template
   -z: charge (real number)
   -s: spin (integer), if not zero this implies an unrestricted calculation
   -q: quality (Basic, Normal, Good, VeryGood or Excellent), default for Becke/ZlmFit
   -i: integration (integer)
   -i: Becke integration (Basic, Normal, Good, VeryGood or Excellent)
   -i: teVelde integration (integer)
   -zlmfit: ZlmFit quality (Basic, Normal, Good, VeryGood or Excellent)
   -kspace: KSpace quality (GammaOnly, Basic, Normal, Good, VeryGood or Excellent)
   -lattice: lattice vectors first three numbers for the first vector, next for the second etc
             The dimension follows from the number of vectors
   -b: basis type (SZ, DZ, DZP, TZ, TCP, TZ2P, QZ4P)
   -c: core type (None, Small, Medium, Large)
   -basiscacheid id: refer to t21 files from previous runs prefixed with this id
   -r: relativistic level (None, Scalar, Spin-Orbit), using ZORA
   -x: XC potential during SCF, one from the options available in AMSinput:
           LDA, 
           GGA:BP, GGA:BLYP, GGA:PW91, GGA:mPW, GGA:PBE, GGA:RPBE, GGA:revPBE, GGA:mPBE,
           GGA:OLYP, GGA:OPBE, 
           Model:SAOP, Model:LB94, 
           Hartree-Fock, 
           Hybrid:B3LYP, Hybrid:B3LYP*, Hybrid:B1LYP, Hybrid:KMLYP, Hybrid:O3LYP, Hybrid:X3LYP, 
           Hybrid:BHandH, Hybrid:BHandHLYP, Hybrid:B1PW91, Hybrid:MPW1PW, Hybrid:MPW1K, 
           Hybrid:PBE0, Hybrid:OPBE0 
   -e: XC energy after SCF (Default, LDA+GGA_METAGGA, LDA+GGA+METAGGA+HYBRIDS)
   -pointcharges: file, file with point charges, one point charge per line (ADF only)
                  x y z charge, xyz in Angstrom, charge in elementary units (+1 for a proton)
   -efield: Ex Ey Ez the electric field vector (in Hartree/(e Bohr))
   -k: replace any key, the single argument will be broken into:
        the key, the replacement value, and END for a block key
        all separated by spaces. To insert a return, add a |
        When the key is not found, it is added just before the ATOMS key
        The -k key may be repeated, and is applied at the end, replacing even earlier changes 
   
   -dftbmodel DFTB|SCC-DFTB|DFTB3: select the DFTB model
   -dftbparameters dir: select the directory with DFTB parameters
   -dftbdispersion [None|Default|D3-BJ|D2|ULG|UFF]: dispersion option to use, default is None
   
   -rxforcefield fname: the ReaxFF force field file
   -rxniter n: number of ReaxFF iterations
   -rxnrstep n: number of non-reactive iterations (out of the total number of iterations)
   -rxtstep T: the time step used in the MD simulation
   -rxmethod string: the simulation type: Velocity Verlet + Berendsen|NPT|NVE
   -rxmdtemp T: the thermostat temperature
   -rxmdpres p: the required pressure
   
   -region name at1 at2 ...: make a region with specified name and atoms, may be repeated
        The atom numbers at1 at2 refer to input order, after geometry modifications, start at 1
        Use at1-at2 to refer to all atoms between at1 and including at2
        If the region key is present all regions already present are deleted
   -fragments prefix: set up a fragment calculation, prefix fragment run/job scripts with prefix
                      if this key is present fragment run/job scripts will be saved (unless -onejob)
                      if a job script is requested, the fragment job names will be prefix.fragname.job
    -onejob: for fragment jobs, concatenate the fragment jobs and final job into one on stdout
   -g "key value": set any key to the specified value (note key value within quotes)
            key: internal name in AMSinput for some option, see bin/amsinput.tcl/tpl/Defaults.tpl
            value: set gin(key) to the specified value
    -nochain: unset chain option (used internally by chain jobs)
   
   OUTPUT
   -bondsonly: only the bonds as generated by the GUI will be exported (the GUIBONDS block)
   -logfile: force the specified logfile to be used in the run script
   -j: produce a fully runnable job (as the .job files from AMSjobs), 
       using the specified jobname.
       The job script produces files like jobname.out, jobname.t21 etc. Several job scripts can simply
       be concatenated, the results will be stored in different files using th jobname parameter
       the default is a simple run script (the .run file from AMSinput, files are left as they are)
   -a: save a .ams file that matches the run script, except for the -k arguments
       (they are listed in the user input field)
       amsfile is the name of the AMSinput, including the .ams extension (required)
   
   Example: calculate gradients for a molecule in file mymol.xyz
            amsprep -t GO -m mymol.xyz -k "stopafter ggrads"
   
   Example: calculate gradients for a molecule in file mymol.xyz, using good quality integration and fit:
            amsprep -t GO -q Good -m mymol.xyz -k "stopafter ggrads"
   
   Example: calculate DFTB frequencies for a molecule in file mymol.xyz
            amsprep -t DFTB-FREQ -m mymol.xyz
   
   

Additional Notes
----------------

`CRSprep <../../COSMO-RS/CRSprep.html>`_ represents a scripting solution which is exclusively oriented towards generating input files for the `COSMO-RS program <../../COSMO-RS/index.html>`_.
