Working with FlexMD
*******************

.. _metatag WORKINGWITHFLEXMD: 

It is recommended to read the sections :ref:`Introduction<metatag INTRODUCTION>` and  :ref:`Molecular Dynamics<metatag MOLECULARDYNAMICS>` before working with FlexMD. Basic understanding of the  `Python Programming Language <http://python.org/>`__ is also required. The Python website hosts documentation and a `tutorial <http://docs.python.org/2/tutorial/>`__ that can be used to learn Python. 

The performance of the FlexMD package is difficult to predict because it depends on system size, the type of ForceJobs used and how these ForceJobs are combined. It is advised to first test the overhead of the FlexMD package for your system before running large simulations. When ab initio forces are involved, the overhead should not give a significant performance penalty. However, it may become a bottleneck when your system only uses cheap forcefields. 

.. toctree::
   :maxdepth: 1

   Creating_a_molecule_object
   Creating_a_ForceJob
   Creating_and_running_the_MD_job



