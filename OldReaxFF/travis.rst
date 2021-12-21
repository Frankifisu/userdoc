TRAVIS: A Trajectory Analyzer and Visualizer 
############################################

TRAVIS is a command line C++ program for analyzing and visualizing trajectories from all kinds of Molecular Dynamics 
or Monte Carlo simulations developed by M. Brehm (`J. Chem. Inf. Model. 51(8) (2011) <https://doi.org/10.1021/ci200217w>`__). 
TRAVIS is shipped with the Amsterdam Modeling Suite from on ADF2017.  

The supported input formats of TRAVIS are:

* *xyz* 
* *pdb* 
* *lmp* (Lammps) 
* *HISTORY* (DLPOLY) 
* *prmtop*/*mdcrd* (Amber)

With ADF2017 the analysis of DFTB and ReaxFF trajectories is supported. 

.. note::

    TRAVIS was designed with non-reactive trajectories in mind, thus one needs to make sure that:

    + *either* the composition of the target species does not change, e.g. by analyzing only a suitable time-interval or running non-reactive dynamics   
    
    + *or* the analysis does not depend on the detection of a particular species, e.g. the diffusion of (inert) atoms 


In order to run a TRAVIS analysis on your trajectory open a shell and navigate to the folder 
you ran your calculation in. Use the python script **kf_to_xyz.py** to convert your trajectory into a TRAVIS-compatible XYZ-format.

Assuming the trajectory is called **traj.rxkf**, run: 

.. rst-class:: steps

  \
    | ``$AMSBIN/amspython $AMSHOME/scripting/trajectory_analysis/kf_to_xyz.py traj.rxkf``


This step will create a file  called **traj_travis.xyz** that contains the frames in XYZ format plus an additional
5th column containing the ReaxFF atomic charges.

Next, start TRAVIS to enter an interactive dialog:

.. rst-class:: steps

  \
    | ``$AMSBIN/travis.exe -p traj_travis.xyz``

An example of how to use TRAVIS with ReaxFF can be found in the
`advanced Li-Batteries ReaxFF tutorial <https://www.scm.com/news/tutorial-li-ion-diffusion-coefficients-reaxff/>`__ .