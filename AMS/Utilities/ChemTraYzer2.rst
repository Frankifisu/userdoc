.. _chemtrayzer2:

ChemTraYzer2 (beta version)
***************************



What does ChemTraYzer2 do? Current state of development. 



Using ChemTraYzer2 via the graphical user interface
---------------------------------------------------


How to use ChemTraYzer2 from the GUI. Link to GUI tutorial.



Minimal input
-------------

This is the minimal input script for performing a chemtrayzer2 analysis of your MD trajectory:

.. code-block:: shell

   #!/bin/sh

   $AMSBIN/chemtrayzer2 << EOF
      Trajectory
         Path path/to/the/ams/results/folder
      End
   EOF


Input options
-------------

Several input options can be specified in the chemtrayzer2 input.


Specifying the trajectory to analyze:

.. scmautodoc:: chemtrayzer2 Trajectory


Parameters for the reaction detection algorithm:

.. scmautodoc:: chemtrayzer2 ReactionDetection


Options for the analysis of the reactions:

.. scmautodoc:: chemtrayzer2 Analysis


Other input options:

.. scmautodoc:: chemtrayzer2 WriteXYZFiles
   :nosummary:

.. scmautodoc:: chemtrayzer2 CreateLegacyOutput
   :nosummary:


Ouput
-----

Describe the various output files.