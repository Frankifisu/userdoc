Creating a ForceJob
===================

To specify what type of forces we want to use in the MD simulation, a ForceJob must be created. FlexMD has a number of ForceJobs (see PACKAGE CONTENTS in help(flexmd)), most of them with examples in $AMSHOME/examples/scmlib. The ForceJobs can be combined into a single ForceJob using flexmd.hybrid_ForceJob. As an example, we combine a reaxff_ForceJob with a metadynamicsjob and a walljob: 

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

Note that all the ForceJobs require some special input and settings, and that these settings can be applied both before and after defining the ForceJob. For the reaxffForceJob, we first define the ForceJob, and add the forcefield parameters file afterwards. For the metadynamics job we reverse this, and first create a metadynamicsJobSettings object, which is then used in the creation of the metadynamics job. For more detailed info on the different ForceJobs and their inputs, see the help function by calling help on a ForceJob, for example: help(flexmd.ReaxffForceJob) or help(flexmd.WallJob). Also remember that other examples of ForceJobs can be found in $AMSHOME/examples/scmlib. 

