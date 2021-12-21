.. This tutorial has been recorded: examples/tutorials/building-frameworks
.. Keep the recording in sync so it may be used to generate the images!

.. _FRAMEWORKBUILDING:

Building Frameworks and Reticular Compounds
*******************************************

In this tutorial we show to the user how to generate a framework compound through the GUI.
These compounds are issued from reticular chemistry, and have received a considerable amount of attention from the scientific community.
Well-known families of these compounds are Metal-Organic Frameworks (MOFs), Covalent-Organic Frameworks (COFs), Zeolites, etc.

In this tutorial we will learn how to use:

+ The export tool for custom building blocks.

+ Autografs Framework builder.


The Export Fragment tool
========================

While a small database of building units is shipped in the ADF suite, you might need to generate your own collection of parts from which to generate you frameworks.
By default the ``.scm_gui/autografs/custom`` directory in your home directory is used for modified or custom units.
You can also choose to use any other location and point the builder to there.
We first start the process of creating and exporting the units.

.. rst-class:: steps

  \
    | **1.** Start AMSinput and create the molecule you desire to export. Here, we'll use a benzene molecule.
    | **2.** Next make sure to maximize the symmetry of the molecule using the star button.
    | **3.** Check that the bonding information is correct.
    | **4.** Switch to the force field engine: |ADFPanel| **→** |ForceFieldPanel|.
    | **5.** **Model → Atom Details** menu, and fill out the corresponding UFF atomic types in the FF Type fields. These will be used in the post-processing optimization of the framework.

.. figure:: /Images/BuildingFrameworksAndReticularCompounds/benzene_atypes.png
  :align: center

The FF types will already have a guessed value, make sure they are correct.
Finally, specify the connectivity of your fragment using dummy atoms.

.. rst-class:: steps

  \
    | **Replace the hydrogens in para positions with dummy atoms using Atoms → Change Atom Type → Xx**

.. figure:: /Images/BuildingFrameworksAndReticularCompounds/benzene.png
  :align: center

You can now export the fragment to your database.

.. rst-class:: steps

  \
    | Click **Edit → Framework → Export Fragment** in the menu bar.
    | Save in the default directory, ``.scm_gui/autografs/custom/``, as ``benzene``.

We will use the other building units from the default database. You are now set up for generation of at least one cubic MOF.


Framework builder : Build a functionalized MOF with defects
===========================================================


.. rst-class:: steps

  \
    | Click **Edit → Framework → Builder** in the menu bar.

In the builder you can choose to use a different database location. Since we saved in the default location, you can keep it as is.
The input options can be chosen from the dropdown lists. The lists only contain options that are still possible. For example, only centers that match the chosen topology will be in that list.
The lists can be further filtered by typing in part of the name.

.. rst-class:: steps

  \
    | **1.** Choose the **pcu** topology.
    | **2.** Select the **Zn_mof5_octahedral** center.
    | **3.** Select the **benzene** linker we just created.
    | **4.** Click the **+** button next to the linker to add a defect.
    | **5.** Select the **benzene** linker again for the defect.


.. figure:: /Images/BuildingFrameworksAndReticularCompounds/builder_sbus.png
  :align: center

The building units are displayed on the left. Any modification will be carried on to the MOF.

.. rst-class:: steps

  \
    | Replace a hydrogen on the benzene linker defect with an amine group.

.. figure:: /Images/BuildingFrameworksAndReticularCompounds/builder_func.png
  :align: center

You can modify the ratio between the defects. We will keep the ratios equal for this tutorial.
The Reduce sites option can be disabled for some topologies to also choose units for equivalent sites.

.. rst-class:: steps

 \
   | **1.** Set the **Super cell** to ``2``, ``2``, ``2``.
   | **2.** Press the **Generate** button. Answer **No** when asked if you want to save the linker 1 defect 1.

.. figure:: /Images/BuildingFrameworksAndReticularCompounds/builder_generated.png
  :align: center

.. rst-class:: steps

  \
    | **1.** Close the framework builder.
    |
    | **2.** Select **UFF4MOF** as **Force field library**.
    | **3.** On the **Details → Geometry Optimization** panel, enable the **Optimize lattice** option.
    | **4.** Save and run the calculation. When asked to run all, choose **No**.
    |
    | **5.** Once the optimization is ready, use **SCM → Movie** to see the results of the optimization.

.. figure:: /Images/BuildingFrameworksAndReticularCompounds/lattice-optimization-movie.png
  :align: center

