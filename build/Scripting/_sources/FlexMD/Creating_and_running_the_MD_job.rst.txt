Creating and running the MD job
===============================

Before the simulation can be set in motion, a propagator is needed. The propagatorJob controls simulation settings such as temperature and timestep size. FlexMD uses the Atomistic Simulation Environment (ASE) [:ref:`1<reference 1>`] for this. The MDPropagatorJob object is created just like the other objects in FlexMD: 

::

       # do this after importing flexmd and creating a ForceJob.
       # it creates the MDPropagator job, with some settings
    myMDJob = flexmd.ASEMDPropagatorJob( ForceJob=myForceJob )
    myMDJob.settings.set_tempcontrol( True, nhfreq=2, maxdef=50.0 )
    myMDJob.settings.set_temperature(300.0)
    myMDJob.settings.set_timestep( 0.02 )

For more details on the ASEMDPropagatorJob, view it's help page: help(flexmd.ASEMDPropagatorJob), or take a look at the MDSettings object: help(flexmd.MDSettings).  

The propagatorJob can be used to create an MDManager object: 

::

       # create an MD manager
    myManager = flexmd.MDManager( mdjob=myMDJob)

The manager object is now in control of the MD simulation, and we can use it to run the simulation for a number of steps: 

::

       # tell the MD manager to run the simulation
    myManager.run( ncycles = 2500 )

Note that the number of steps here should be increased a lot if metadynamics effects are to be observed, but it is always wise to first run a small number of steps to check if everything works. Some information will be printed during the simulation, depending on the settings of the components used. The manager will also create some folders in the working directory, and store the data produced by the simulation in there. 

The full flexmd jobfile should now look something like this: 

::

    from scm import flexmd
    myMol = flexmd.MDMolecule('myGeometryFile.xyz')
    myMol = flexmd.pdb.set_box([50.0,25.0,100.0])
       # setup our reaxff ForceJob and attach the forcefield file 
       # (place the ff file in the same dir as the script and the xyz!)
    myReaxffForceJob = flexmd.ReaxffForceJob(molecule=myMol)
    myReaxffForceJob.settings.set_ff_filename('reax_forcefield_file.ff')
   
       # next we define the collective variable: the distance between atom 1 and 2
    myCvs = [flexmd.DistCV([1,2])]
       # create a set of metadynamics properties, using the CV
    mtdSettings = flexmd.MetadynamicsSettings(cvs=myCvs, widths=[0.30], height=0.25 )
       # create the metadynamics job by combining the molecule, settings (with CV) 
       # and the number of md steps between depositing metadynamics hills.
    myMetadynamicsjob = flexmd.MetadynamicsJob( myMol, settings=mtdSettings, nstep=150 )
   
       # add a wall to prevent the two atoms from drifting more than 10 Angstrom away.
    myWalljob = flexmd.WallJob(molecule=myMol, cvs=myCvs, cntrs=[10.0], widths=[1.0], heights=[500.0])
   
       # combine the forces into a hybrid job that will be used for the MD
    myForceJob = flexmd.HybridForceJob( [[myReaxffForceJob,'+'], [theMetadynamicsjob,'+'], [theWalljob,'+']], myMol )
   
       # do this after importing flexmd and creating a ForceJob.
       # it creates the MDPropagator job, with some settings
    myMDJob = flexmd.ASEMDPropagatorJob( ForceJob=myForceJob )
    myMDJob.settings.set_tempcontrol( True, nhfreq=2, maxdef=50.0 )
    myMDJob.settings.set_temperature(300.0)
    myMDJob.settings.set_timestep( 0.02 )
   
       # create an MD manager
    myManager = flexmd.MDManager( mdjob=myMDJob)
       # tell the MD manager to run the simulation
    myManager.run( ncycles = 2500 )

This job can be resumed by just running the script again, FlexMD should pick up on the coordinates and velocities from the QMMD folder. To do this, simply run the job again, and a new set of trajectory and energy files should appear in the QMMD folder. If you wish to specify which files FlexMD restarts from, you can use the set_restartnum() function on myMDJob.settings:

::

    # add this below the "myMDJob.settings.set_timestep( 0.02 )" line
       # FlexMD will restart from the files with index numbers 1 lower than you pass to set_restartnum
       # This will cause FlexMD to restart from QMMD/TRAJEC00.dcd and QMMD/TRAJEC00.dcd
    myMDJob.settings.set_restartnum(1)

