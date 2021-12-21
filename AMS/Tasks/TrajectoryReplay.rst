.. index:: Trajectory Replay

.. _TrajectoryReplay:

Trajectory replay
=================

For some applications it is necessary to run calculations on all (or a subset of) frames from a trajectory obtained in another job.
Often this is done with a different engine in order to learn something about the differences in the potential energy surface between the engines.
This could easily be scripted with :ref:`PLAMS <AMSScripting>`, but since the 2021.3 release the AMS driver itself also implements a convenient "Replay" task to do this.

The input for the replay task is quite minimal. The following input file would replay every tenth of the first 1000 frames on the trajectory of ``oldjob`` with the DFTB engine to calculate nuclear gradients::

   Task Replay

   Replay
      File oldjob.results
      Frames 1:1000:10
   End

   Properties
      Gradients True
   End

   Engine DFTB
   EndEngine

.. seealso::

  :ref:`Example input files <example Replay>` for replaying PES scans, NEB and MD calculations.

Note that it is not necessary to specify a :ref:`System block<SystemDefinition>` in the input of a replay job, as the system will just be loaded from the job to be replayed.
What properties are evaluated for each frame in the trajectory can be configured in the ``Properties`` block of the input file. For a list of available properties, see for example the the manual pages on :ref:`Gradients, Hessian, Stress tensor, Elasticity<PESPointProperties>` and :ref:`Dipole moment, Polarizability, Bond orders<PESPointExtraProperties>`.

Depending on the kind of job that is being replayed, you will get a slightly different default behavior for the selection of frames to be replayed:

* For :ref:`PES scans <PESScan>` only the frames corresponding to the converged PES points will be replayed. The resulting ``ams.rkf`` output file will contain the ``PESScan`` section, as if it had been produced by running a PES scan job.
* For :ref:`Nudged Elastic Band (NEB) <NEB>` jobs only the frames corresponding to the converged images are replayed. The resulting ``ams.rkf`` file will have an ``NEB`` section that looks like it is from a NEB job that converged immediately.
* All other job types (such as :ref:`Molecular Dynamics<MolecularDynamics>`) will just replay whatever is on the ``History`` section on the ``ams.rkf`` file. By default all frames are replayed, but a subset can be chosen with the ``Replay%Frames`` keyword.

Details of the Replay task can be configure in the ``Replay`` block in the input.

.. scmautodoc:: ams Replay

