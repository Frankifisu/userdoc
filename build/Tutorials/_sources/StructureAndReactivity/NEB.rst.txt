.. This tutorial has been recorded: examples/tutorials/ams-ts-neb
.. Keep the recording in sync so it may be used to generate the images!

.. _AMS_NEB:

Reaction path and TS search using NEB
*************************************

In this tutorial we will use the climbing-image `Nudged Elastic Band method (NEB) <../../AMS/Tasks/NEB.html>`__ to find the minimum energy reaction path and transition state of the following reaction:

.. image:: /Images/NEB/NEB_reaction.png
   :width: 60%
   :align: center


We will be using the `DFTB engine <../../DFTB/index.html>`__ with the `GFN1-xTB model <../../DFTB/DFTB_Model_Hamiltonian.html>`__. This is a computationally fast method (which is convenient for the purposes of a tutorial) but it is not very accurate in predicting reaction energies. For better accuracy, using the DFT engine `ADF <../../ADF/index.html>`__ (or `BAND <../../BAND/index.html>`__) is recommended.


Setting up and running the calculation
--------------------------------------

You can set up and run the calculations for this tutorial using either the Graphical User Interface (GUI), the python library `PLAMS <../../plams/index.html>`__ or a `bash script <../../AMS/Input_Output.html>`__.

.. tabs::

   .. tab:: GUI

      .. rst-class:: steps

        \
          | Start **AMSjobs**
          | **1.** in the **menu bar** select **SCM → New input**

      This will open a new **AMSinput** window.

      .. rst-class:: steps

        \
          | In **AMSinput**:
          | **1.** Switch to the **DFTB panel**: |ADFPanel| **→** |DFTBPanel|
          | **2.** Select **Task → NEB**

      We will use the GFN1-xTB model, which is the default model as of the AMS2020 release.
      Your AMSinput window should look like this:

      .. image:: /Images/NEB/NEB_Main_DFTB_panel.png

      When setting up an NEB calculation we need to specify two systems: the *initial* and *final* states of the reaction. The NEB algorithm will then generate a set of *images* by interpolating between the initial and final systems. This will be the initial approximation of the reaction path, which will be optimized during the NEB calculation.

      .. rst-class:: steps

        \
          | **1.** Download the following xyz files: file :download:`NEB_initial.xyz <../downloads/NEB_initial.xyz>` and :download:`NEB_final.xyz <../downloads/NEB_final.xyz>`
          | **2.** Import the coordinates of the initial system: in the **menu bar**, select **File → Import Coordinates...** and select the file **NEB_initial.xyz**
          | **3.** Create a new molecule-tab: in the **menu bar**, select **Edit → New Molecule...**
          | **4.** Import the coordinates of the final system in the newly created molecule tab: in the **menu bar**, select **File → Import Coordinates...** and select the file **NEB_final.xyz**

      You can switch between the two molecule tabs by clicking arrows at the bottom of the **molecule drawing area**.

      .. important::

        |order_of_atoms|

        You can see the indices of the atoms by clicking in the **menu bar** on **View → Atom Info → Name → Show**. It is possible to change the order of the atoms in the **Coordinates** panel (in the **panel bar**: **Model → Coordinates**) using the **Move atom(s)** option.



      Now, go to the NEB details panel where we will set up the NEB calculation:

      .. rst-class:: steps

        \
          | **1.** Click on |MoreBtn| next to **Task → NEB** to go to the NEB details panel
          | **2.** From the drop-down menu next to **initial system**, select **Mol-1**
          | **3.** From the drop-down menu next to **final system**, select **Mol-2**
          | **4.** Check the **Characterize PES point** checkbox

      Your AMSinput window should look like this:

      .. image:: /Images/NEB/NEB_ready_to_run.png


      .. tip::

         From most **AMSinput** panels you can jump to the relevant section of the user manual by clicking on |InfoBtn|, which is located in the top-right corner of the panel.


      We are now ready to run the calculation:

      .. rst-class:: steps

        \
          | In **AMSinput**:
          | **1.** In the **menu bar**, click on **File → Save** and give it the name "NEB_tutorial"
          | **2.** In the **menu bar**, click on **File → Run** . This will bring the **AMSjobs** window to the front
          | **3.** Wait for the calculation to finish. It should take just a few seconds


      In the **logfile** you can monitor the progress of your NEB calculation:

      .. rst-class:: steps

        \
          | In **AMSjobs**:
          | **1.** Select the job "NEB_tutorial" and in the **menu bar** click on **SCM → Logfile**. This will open the logfile


      A NEB calculation consists of several steps, which are automatically executed one after the other:

      - first, the two end points (the *initial* and *final* molecules) are optimized (in the logfile, look for ``Optimizing initial state`` and ``Optimizing final state``)
      - then the NEB reaction path will be optimized (in the logfile, look for ``NEB Path Optimization``). During the reaction path optimization, the highest-energy image on the path will *climb* to the transition state
      - finally, a single point calculation for the TS is performed (in the logfile: ``Final calculation for highest-energy image``). If the option **Characterize PES point** is on, then the lowest-lying normal modes will be calculated in order to validate the TS (the TS should have exactly one imaginary frequency). Some information on the reaction path is printed at the end of the logfile::

         NEB found a transition state!
         TS barrier height from the left           0.02576078 Hartree
                                                  16.165 kcal/mol
                                                  67.635 kJ/mol
         TS barrier height from the right          0.08632064 Hartree
                                                  54.167 kcal/mol
                                                 226.635 kJ/mol


   .. tab:: Bash script

      The following bash script performs an NEB calculation using the AMS driver and the DFTB engine. The input options for the AMS driver described in the `AMS driver manual <../../AMS/index.html>`__, while the `DFTB manual <../../DFTB/index.html>`__ describes the input options for the **DFTB** ``Engine`` block.

      .. literalinclude:: <../../../../../examples/TestAMS/TutorialNEB/NEB.run
         :language: bash

      .. important::

        |order_of_atoms|

      To run the calculation:

      .. rst-class:: steps

        \
          | **1.** Save the above script in a file called ``NEB.run``
          | **2.** Make the script executable: in a terminal, type ``chmod +x NEB.run``
          | **3.** Run it interactively and redirect the output to a file: in a terminal, type ``./NEB.run > out``


   .. tab:: Python

      In the following python script (using the `PLAMS <../../plams/index.html>`__ library) we set up a NEB calculation, run it, and extract some results from the binary results files.


      .. literalinclude:: <../../../../../examples/TestAMS/TutorialNEB/NEB.py
         :language: python

      The options for the AMS driver and for the DFTB engine are specified in the `Settings object <../../plams/components/settings.html>`__ object. The various input keys are described in the `AMS driver manual <../../AMS/index.html>`__ and `DFTB manual <../../DFTB/index.html>`__. See the `AMS interface section of the PLAMS manual <../../plams/interfaces/ams.html>`__ for more details.

      .. important::

        |order_of_atoms|

      To run the PLAMS script:

      .. rst-class:: steps

        \
          | **1.** Download the following xyz files: :download:`NEB_initial.xyz <../downloads/NEB_initial.xyz>` and :download:`NEB_final.xyz <../downloads/NEB_final.xyz>`
          | **2.** Save the above script in a file called ``NEB.py``
          | **3.** Run the script using PLAMS: in a terminal, type ``$AMSBIN/plams NEB.py``



To improve the initial approximation of the reaction path in an NEB calculation, you can (optionally) provide an *intermediate* system.

Another important NEB option is the **number of images**. In case of problematic NEB path optimization convergence, using more images might help (note that the computation time increases with the number of images used).

You can read more about the various NEB options in the `AMS manual <../../AMS/Tasks/NEB.html>`__.




Results of the calculation
--------------------------

.. tabs::

   .. tab:: GUI

      Now, let's visualize the reaction path computed by NEB:

      .. rst-class:: steps

        \
          | In **AMSjobs**:
          | **1.** Select the job "NEB_tutorial" and, in the **menu bar**, click on **SCM → Movie**. This will open the **AMSmovie** module

      .. image:: /Images/NEB/NEB_AMSmovie.png

      In AMSmovie, you can click on **play** (or drag the slide-bar) so see the reaction happening. On right-hand side, the energy and gradients of the images in the NEB reaction path are plotted.

      The transition state is characterized by having one imaginary frequency. Let's visualize the normal modes of the transition state geometry with AMSspectra:

      .. rst-class:: steps

        \
          | In **AMSmovie**:
          | **1.** click on **SCM → Spectra**. This will open the **AMSspectra**

      .. image:: /Images/NEB/NEB_AMSspectra.png

      Here you will see the computed normal modes for the TS geometry. Notice that there is one negative frequency (imaginary frequency are shown as negative numbers).

      .. rst-class:: steps

        \
          | In **AMSspectra**:
          | **1.** In the table, click on the line with the negative frequency

      The corresponding normal mode will be displayed in the molecule-visualization area. This normal mode gives you an idea of how the atoms are moving as they cross the transition state.


   .. tab:: Bash script

      In the folder where you executed your script you will find a file ``out``, which contains the text-output of the calculation, and a folder called ``ams.results`` containing binary results of the calculation.

      At the end of the output file ``out`` you will find a section summarizing the results of the NEB calculation:

      .. code-block:: none

         NEB found a transition state!


         ------------------------------------------------------------
         TS barrier height from the left           0.02581511 Hartree
                                                  16.199 kcal/mol
                                                  67.778 kJ/mol
         TS barrier height from the right          0.08637041 Hartree
                                                  54.198 kcal/mol
                                                 226.765 kJ/mol
         Reaction energy                          -0.06055530 Hartree
                                                 -37.999 kcal/mol
                                                -158.988 kJ/mol
         ------------------------------------------------------------
                 Transition state geometry

         --------
         Geometry
         --------

         Atoms
         Index Symbol   x (angstrom)   y (angstrom)   z (angstrom)
            1      N     1.76794468     0.02199401    -0.76530642
            2      N     0.86568320    -0.56021023    -1.14090273
            3      O    -0.28459962    -0.76023024    -0.92163051
            4      C     0.89983351     0.97770099     0.84893165
            5      C    -0.38912967     0.55813520     0.80607959
            6      H     1.18303105     1.94163319     0.44757192
            7      H    -1.15509240     1.14579400     0.31965225
            8      H    -0.73127815    -0.27639812     1.40152984
            9      H     1.61076814     0.51427067     1.51998360

      The folder ``ams.results`` contains:

      * a text file called ``ams.log`` containing a very concise summary of the calculation’s progress during the run.
      * the main binary results file ``ams.rkf``,  containing the reaction path computed in the NEB calculation.
      * the engine results file ``NEB_TS_final.rkf`` corresponding a single point calculation at the transition state geometry. It contains, among other properties, the normal modes.

      You can explore the content of the ``rkf`` binary results files using the **kfbrowser** utility.

      .. rst-class:: steps

        \
          | In a terminal, type: ``$AMSBIN/kfbrowser ams.results/NEB_TS_final.rkf``


      The binary results of the calculation can also be visualized with the GUI modules:

      .. rst-class:: steps

        \
          | In a terminal, type: ``$AMSBIN/amsmovie ams.results/ams.rkf``
          | In a terminal, type: ``$AMSBIN/amsspectra ams.results/NEB_TS_final.rkf``


   .. tab:: Python

      This is the output printed by the PLAMS script:

      .. code-block:: none

            [11:48:45] PLAMS working folder: [...]
            [11:48:45] JOB NEB STARTED
            [11:48:45] JOB NEB RUNNING
            [11:48:47] JOB NEB FINISHED
            [11:48:47] JOB NEB SUCCESSFUL
            Successful NEB calculation!
            PES Point character: transition state
            Geometry of the TS:
              Atoms:
                1         N      1.762731       0.038376      -0.779381
                2         N      0.866215      -0.561703      -1.142377
                3         O     -0.278098      -0.778480      -0.906970
                4         C      0.901016       0.975210       0.848982
                5         C     -0.389988       0.560115       0.803367
                6         H      1.186939       1.941923       0.456712
                7         H     -1.151130       1.151965       0.314116
                8         H     -0.738634      -0.269125       1.402220
                9         H      1.608109       0.504408       1.519239

            Left TS barrier : 16.199224 [kcal/mol]
            Right TS barrier: 54.198250 [kcal/mol]
            [11:48:47] PLAMS run finished. Goodbye

      In the folder where you executed your script you will find a newly created folder ``plams_workdir`` containing the results of the calculations. The folder ``plams_workdir/NEB`` contains the results of the job ``NEB``. Inside this folder you will find all the files generated by AMS, including the binary results files ``ams.rkf`` and ``NEB_TS_final.rkf``.

      The binary results of the calculation can also be visualized with the GUI modules:

      .. rst-class:: steps

        \
          | In a terminal, type: ``$AMSBIN/amsmovie plams_workdir/NEB/ams.rkf``
          | In a terminal, type: ``$AMSBIN/amsspectra plams_workdir/NEB/NEB_TS_final.rkf``



.. |order_of_atoms| replace:: In NEB calculations, the order of the atoms in the initial and final system should be the same (if you provide an intermediate system, you should use a consistent atom-ordering for that too). The order of the atoms should be consistent because the images-interpolation algorithm maps the n-th atom of the initial system to the n-th atom of the final system.
