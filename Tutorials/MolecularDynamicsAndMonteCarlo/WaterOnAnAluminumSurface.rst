.. This tutorial has been recorded: examples/tutorials/md-water-aluminum
.. Keep the recording in sync so it may be used to generate the images!

.. _reaxff_water_on_alu:

Water on an aluminum surface
****************************

This tutorial will help you to:

+ create an aluminum slab

+ add a solvent (water)

+ set different `thermostats <../../AMS/Tasks/Molecular_Dynamics.html#thermostats-and-barostats>`__ (temperatures) for different regions of the system.

+ run the `molecular dynamics <../../AMS/Tasks/Molecular_Dynamics.html>`__ simulation and see what happens

For this simulation we will use the ReaxFF force field through the AMS driver program.

.. note::

   The purpose of this tutorial is to demonstrate how to technically set up and run a simulation. The employed `Al-H2O ReaxFF force field <../../ReaxFF/Included_Forcefields.html>`__ was parameterized to handle similar, but not exactly the same, types of systems as in this tutorial. Always do your own testing to see if the results from a simulation are reasonable.


Step 1: Start AMSinput in ReaxFF mode
=====================================

.. rst-class:: steps

  \
    | **1.** Start AMSjobs
    | **2.** Use the **SCM → New input** menu command
    | **3.** Switch to **ReaxFF**: |ADFPanel| **→** |ReaxFFPanel|


Step 2: Creating the surface
============================

Bulk aluminum has an fcc crystal structure, with a lattice constant of 4.05 Å of the conventional unit cell.

To create the surface, we first build the primitive unit cell of bulk aluminum:

.. rst-class:: steps

  \
    | **1.** **Edit → Crystal → Cubic → fcc**
    | **2.** In the dialog that appears:
    | **3.** Select the preset **Al**
    | **4.** Click the **OK** button
    | **5.** **View → Periodic → Repeat Unit Cells**

In your molecule editor screen you should see a picture of the bulk aluminum structure. The primitive unit cell contains one atom. As ReaxFF input by default does not show repeated cells, it had to be turned on explicitly. Otherwise you see only the single atom in the unit cell.

.. image:: /Images/WaterOnAnAluminumSurface/bulk-al.png

.. tip::

   In the **menu bar**, select **View → Properties (including estimated)** to see some properties of the system, such as stoichiometry, angles between lattice vectors, and the system density.

Now create the surface. Surfaces are constructed by specifying the Miller indices, which requires that the conventional (and not primitive) cell be used.

.. rst-class:: steps

  \
    | **1.** **Edit → Crystal → Convert To Conventional Cell**. This creates a conventional cubic unit cell with lattice constant 4.05 Å.
    | **2.** **Edit → Crystal → Generate Slab...**
    | **3.** Set the Miller indices to ``0``, ``0``, ``1``.
    | **4.** Set the number of layers to ``2``
    | **5.** Click **Generate Slab**
    | **6.** Rotate to see the system from the side

.. image:: /Images/WaterOnAnAluminumSurface/al-layer.png

You should be able to see it is a four-layer slab.

In this case we do not want just one unit cell, but a much bigger   piece of the slab:

.. rst-class:: steps

  \
    | **1.** Turn off periodic view: **View → Periodic → Repeat Unit Cells**
    | **2.** **Edit → Crystal → Generate Super Cell...**
    | **3.** Put ``10``, ``10`` on the diagonal
    | **4.** Click **OK**
    | **5.** Rotate the system and get a better view

.. image:: /Images/WaterOnAnAluminumSurface/layer10x10.png

Now we have a slab of aluminum, four layers thick.


Step 3: Add solvent
===================

The next step is to add water to the system.

.. rst-class:: steps

  \
    | **1.** Select Bulk (instead of Slab) for periodicity
    | **2.** **Edit → Builder**
    |
    | **3.** Change the third dimension of the lattice vectors to ``50.0``
    |
    | **4.** Type ``wa`` in the line with 'Fill box with'
    | **5.** Select **Water (ADF)** from the search results
    | **6.** Specify ``1600`` copies.
    | **7.** Click the **Generate Molecules** button on the bottom
    |
    | **8.** Click **View → Periodic → Show Unit Cell** to visualize the box
    | **9.** Rotate to your favorite view

.. image:: /Images/WaterOnAnAluminumSurface/al-water.png

   
.. note::

   After the water has been added, the density :math:`\rho_{\textrm{tot}} = 1.021` g/mL. This is the density of the **entire** system, including the Al slab. The resulting density of the added water can be estimated as
   :math:`\rho_{\textrm{water}} = \frac{m_{\textrm{tot}}-m_{\textrm{Al}}}{V_{\textrm{tot}}-V_{\textrm{Al}}} = \frac{\rho_{\textrm{tot}}V_{\textrm{tot}} - \rho_{\textrm{Al}}V_{\textrm{Al}}}{V_{\textrm{tot}}-V_{\textrm{Al}}} = \frac{10^{-24}}{10^{-24}}\cdot\frac{1.021\cdot82012.5-2.97\cdot4.05^3\cdot2\cdot10\cdot10}{82012.5-4.05^3\cdot2\cdot10\cdot10} = 0.64` \ g/mL.
   In this tutorial, this lower density (compared to liquid water) is used because the water will be heated to a very high temperature (see **Step 4**)


Step 4: Set up the simulation, including a temperature regime
=============================================================

Now we will set up the MD-simulation. We will use the Al-water force field
and a Nose-Hoover thermostat with a default damping constant of 100 fs:

.. rst-class:: steps

  \
    | **1.** Close the Builder by clicking the **Close** button on the bottom
    | **2.** Click on the **Force field** folder icon and select the **Al-H2O** force field
    | **3.** Make sure the **Task** is set to **Molecular Dynamics** and click |MoreBtn| to go the **Model → MD** panel
    | **4.** Set the **Number of steps** to ``1000000``
    | **5.** Set **Initial velocities** to **Zero**
    | **6.** Go to the **Model → Thermostat** panel by clicking the |MoreBtn| next to **Thermostat**
    | **7.** Click the **+** button to create a new thermostat
    | **8.** Set **Thermostat** to **NHC**
    | **9.** Set **Damping constant** to ``100.0`` fs

.. image:: /Images/WaterOnAnAluminumSurface/al-water-main.png

For the purpose of this tutorial we want to quickly see something happen in our simulation. We will therefore use a very high temperature for the  water, but try to keep the aluminum cool. Also, we will start with a low temperature MD to relax the initial set-up. This can all be accomplished using several thermostats for different regions.

For this we first need to define two new regions: one for the aluminum slab, and one for the water. In AMSinput, regions are just defined as a collection of atoms, which can be set up via the **Regions panel**:

.. rst-class:: steps

  \
    | **1.** In the panel bar, click **Model → Regions**
    | **2.** Click the button with the checkmark under **Selection** for the ``Auto_Generated`` region

By pressing the select button you have selected all atoms in the ``Auto_Generated`` region. This region will always contain the atoms that are added by the Builder tool we used earlier. Thus, as you can see, all water molecules are selected.

.. image:: /Images/WaterOnAnAluminumSurface/autoregion.png

For clarity, let us rename the ``Auto_Generated`` region to ``Water``:

.. rst-class:: steps

  \
    | **1.** Click and select the text ``Auto_Generated`` and change it into ``Water``

Now that we have a region defined that contains all water molecules, let us also make a region that contains just the aluminum slab.

.. rst-class:: steps

  \
    | **1.** Click on any of the aluminum atoms to select it.
    | **2.** Select all other aluminum atoms by clicking ``Select → Select atoms of the same type``.
    | **3.** Press the **+** button in front of the Regions label to add a new region (containing all the selected atoms)
    | **4.** Change the region's name from ``Region_2`` to ``Al``
    | **5.** Click the checkbox to the left of the ``Water`` region to highlight it

You should now see the two different regions highlighted in different colors:

.. image:: /Images/WaterOnAnAluminumSurface/wateralregions.png

You can also set the visualization style per region:

.. rst-class:: steps

  \
    | **1.** Uncheck the check boxes at the left of the ``Water`` and ``Al`` region lines
    | **2.** Press the triangle on the right side of the ``Al`` region line, and select the **Wireframe** visualization option

The aluminum slab is now shown in wireframe style.

.. image:: /Images/WaterOnAnAluminumSurface/nowatercolor.png

Now that we have defined the regions we needed, we will set up the temperature regime. We will start the water with a temperature of 300 K for 4000 steps, then warm it up to 2000 K within 4000 steps and maintain this temperature for the rest of the simulation.

.. rst-class:: steps

  \
    | **1.** Go back to the **Model → Thermostat** panel
    | **2.** Select the **Water** region from the **Atoms in region** drop-down menu
    | **3.** Type ``300 300 2000`` into the **Temperature(s)** field
    | **4.** Type ``4000 4000`` into the **Duration(s)** field

.. hint::

   Note that with time-dependent thermostats the set temperatures are always connected with a linear ramp. The **Temperatures** field should therefore always contain one number more than the **Durations** field, as the last temperature will be held indefinitely. In the example above, in order to have a constant temperature of 300 K in the beginning, we explicitly specified that the temperature should go from 300 K to 300 K within the first 4000 steps.

We now have the time-dependent thermostat of the water set up. Let us add another thermostat that just keeps the aluminum slab cold.

.. rst-class:: steps

  \
    | **1.** Click the **+** button to create another thermostat
    | **3.** Set the new **Thermostat** to **NHC**
    | **2.** Set the new **Temperature(s)** to ``300`` K
    | **4.** Also set the **Damping constant** to ``100.0`` fs
    | **5.** Select the **Al** region from the **Atoms in region** drop-down menu

Your thermostat setup should look like this:

.. image:: /Images/WaterOnAnAluminumSurface/tregimes.png


Step 5: Run the simulation
==========================

Now we can run our set up:

.. rst-class:: steps

  \
    | **1.** **File → Run**
    | **2.** When asked to save, specify ``Al-water`` as filename
    | **3.** Follow your calculation by clicking **SCM → Movie**
    | **4.** Rotate and zoom to get a good view of the surface
    | **5.** Add a graph of the temperature by clicking **MD Properties → Temperature**
    | **6.** Let the calculation run for a while (roughly until iteration 30000, that is frame 300)

.. image:: /Images/WaterOnAnAluminumSurface/alwatermovie.png

You will see many water molecules adsorb on the aluminum surface almost immediately. Around frame 40 (that is MD step 4000) you will see the temperature increase, as the water thermostat starts heating its region. After some time, you will also see some of the adsorbed water molecules loose one hydrogen. The lone proton will likely drift off into the water, while the remaining OH goes into a bridge-like configuration with two of the surface Al. This configuration can already be seen in the picture above.

You can leave the simulation running to see what will happen. It will take a long time though. If you do leave it running for a while, you will see that the OH in the aforementioned bridge configuration tend to pull one of the Al atoms out of the surface, essentially roughening it and allowing more water to adsorb. You might also see aluminum atoms completely detach from the surface an become dissolved in the water layer as AlO3H3. Eventually a rough aluminum oxide layer forms, while the split off protons combine to form molecular hydrogen.

.. raw:: html

   <center>
      <video controls width="700" src="../_downloads/Al-water.mp4"></video>
   </center>

You can download the movie :download:`here </downloads/Al-water.mp4>` if it does not play in your browser.

We can use the molecular composition analysis tools in AMSmovie to get a bit clearer picture of that process. Let us plot the number of H2O, H3O and H2 molecules in our simulation:

.. rst-class:: steps

  \
    | **1.** Click **MD Properties → Molecules**
    | **2.** Tick the **Graph** check-box for **H2O**
    | **3.** Tick the **Graph** check-box for **H3O**
    | **4.** Move the last curve to the right axes: **Graph → Curve On Right Axes**
    | **5.** Tick the **Graph** check-box for **H2**
    | **6.** Move the last curve to the right axes: **Graph → Curve On Right Axes**

.. image:: /Images/WaterOnAnAluminumSurface/H2O-H3O-H2-molecules.png
   :width: 60%
   :align: left

.. image:: /Images/WaterOnAnAluminumSurface/H2O-H3O-H2.png

To make it easier to see what is going on, hide all the H2O molecules:

.. rst-class:: steps

  \
    | **1.** Untick the **Show** check-box for **H2O** to hide all the water molecules

.. image:: /Images/WaterOnAnAluminumSurface/no-H2O-molecules.png
   :width: 60%
   :align: left

.. image:: /Images/WaterOnAnAluminumSurface/no-H2O.png

If you do not want to wait for the simulation to finish, you can now request the job to stop:

.. rst-class:: steps

  \
    | **1.** Bring the AMSjobs window to the front
    | **2.** Make sure your Al-water job is selected (click once on it if not)
    | **3.** Stop it it using **Job → Request Early Stop**

Your job will quit after the next sampled MD step.
