.. This tutorial has been recorded: examples/tutorials/md-bouncing-buckyball
.. Keep the recording in sync so it may be used to generate the images!

.. _AMS_MoleculeGun:

The Bouncing Buckyball
**********************

In this tutorial we will be modeling the impact of a C60 buckyball on a graphene sheet:

.. image:: /Images/MoleculeGun/ReaxFF_MolGun_Intro.png

For the purpose of this tutorial we are going to use the `ReaxFF <../../ReaxFF/index.html>`__ engine, as it is very fast. However, one can also follow this tutorial using for example the `DFTB <../../DFTB/index.html>`__ engine.


Setting up the geometry
-----------------------

Let us begin by creating a graphene sheet.

.. rst-class:: steps

  \
    | **1.** Start **AMSinput**.
    | **2.** Switch to **ReaxFF**: |ADFPanel| **→** |ReaxFFPanel|
    | **3.** Click on the **magnifying glass** |Search|
    | **4.** Search for ``graphite`` and select **C128: Graphite** from the crystal compounds.

.. image:: ../Images/MoleculeGun/molecule_gun_1.png

The graphite cell shown in the viewport on the left consists of four graphene layers. For our example we need a single layer, so let us delete the others.

.. rst-class:: steps

  \
    | **1.** **Left click and drag** in the viewport to rotate the graphite cell into an orientation where you can easily see the four layers.
    | **2.** Select three of the layers using the **Left mouse button** and **dragging a box** around them in the viewport. Holding down the **Shift** key adds atoms to an existing selection.
    | **3.** Press the **DEL** (or **backspace**) button on your keyboard to delete the selected atoms.

.. image:: ../Images/MoleculeGun/molecule_gun_2.png

In the image above we kept the graphene layer in the xy-plane and deleted the other three. At the moment we still have periodicity along the z-axis. We only really a single graphene sheet, so let us just get rid of this third lattice vector:

.. rst-class:: steps

  \
    | **1.** Switch **Periodicity** from **Bulk** to **Slab**.

We now have a single layer of graphene with an infinite vacuum below and above. Our graphene sheet is still rather small though: Too small to shoot something large like a buckyball at it! Let us make it larger using the super cell tool.

.. rst-class:: steps

  \
    | **1.** Click on the **Edit** menu next to the SCM logo on the top.
    | **2.** Select **Crystal → Generate Super Cell**
    | **3.** In the pop-up window enter ``6``, ``6`` on the diagonal.
    | **4.** Click **Ok**.

.. image:: ../Images/MoleculeGun/molecule_gun_3.png

Now that we have a reasonably sized graphene sheet we can insert the buckyball.

.. rst-class:: steps

  \
    | **1.** Click on the **magnifying glass** |Search|
    | **2.** Enter ``buckyball`` into the search field and select **C60: Buckyball**.

.. image:: ../Images/MoleculeGun/molecule_gun_4.png

The inserted buckyball should automatically be selected. However, it is currently sitting at the origin of the cell *inside* of the graphene sheet. We are going to have to move it out of there.

.. rst-class:: steps

  \
    | **1.** Use your **right mouse button** to drag the buckyball above the graphene sheet.
    | **2.** Position it above one of the sharp corners of the sheet.

.. image:: ../Images/MoleculeGun/molecule_gun_5.png

The buckyball should now be in a nice place from which we can shoot it at the center of the graphene sheet. It is time to aim the gun ...


Setting up the molecule gun
---------------------------

The `molecule gun <../../AMS/Tasks/Molecular_Dynamics.html#molecule-gun-adding-molecules-during-simulation>`__ in AMS uses regions to identify which part of the geometry is the projectile and which is the target. Let's make sure we have the buckyball (our projectile) in a separate region.

.. rst-class:: steps

  \
    | **1.** Open the **Regions panel** by clicking **Model → Regions**.
    | **2.** Select the buckyball by holding down the **Shift** key and dragging a box around it using your **left mouse button** in the viewport.
    | **3.** With the selected buckyball, click the **+** button in the **Regions panel** on the right.
    | **4.** Confirm that your buckyball is now **highlighted** in the viewport on the left.
    | **5.** Rename the newly created region to from ``Region_1`` to ``Buckyball1`` by typing in the corresponding text box on the **Regions panel**.

.. image:: ../Images/MoleculeGun/molecule_gun_6.png

Next we need to set up some general aspects of our MD simulation.

.. rst-class:: steps

  \
    | **1.** Switch the **Main** panel.
    | **2.** Select ``C.ff`` as the **Force field**.
    | **3.** Make sure the **Task** is set to **Molecular Dynamics**.
    | **4.** Go to the molecular dynamics details panel by clicking |MoreBtn| to the right.
    | **5.** Set the **Number of steps** to ``8000``.
    | **6.** Set the **Sample frequency** to ``50``.
    | **7.** Set **Initial velocities** to **Zero**.
    | **7.** Untick all the boxes next to **Preserve**.

.. image:: ../Images/MoleculeGun/molecule_gun_7.png

This should give us a sufficiently long and smooth trajectory of the impact. Note that we have disabled the preservation of the momenta. Otherwise the preservation will make the graphene layer drift towards the incoming buckyball in an attempt to remove the system's total momentum, which is not what we want. We just want the graphene layer to remain stationary until the buckyball hits.

Finally, we need to configure the molecule gun!

.. rst-class:: steps

  \
    | **1.** Click on **Model → Molecule Gun**.
    | **2.** Click on **+** next to **Add Molecules** to add a new projectile.
    | **3.** Select our previously set up region ``Buckyball1`` from the **System** drop-down menu.

As you can see, the molecule gun panel looks relatively complicated. This is because it supports not only single shots, but also a regular shooting from randomized positions in random directions. It could, for example, be used to let many molecules rain down on a surface. Together with the molecule removal features, this can be used to set up quite involved simulations.

.. seealso::
   See the `molecule gun section <../../AMS/Tasks/Molecular_Dynamics.html#molecule-gun-adding-molecules-during-simulation>`__ in the AMS driver manual for a complete overview of the supported options.

In this tutorial we are going to keep things simple and only shoot a single buckyball at the beginning of the simulation.

.. rst-class:: steps

  \
    | **1.** Set **Frequency** to ``1``.
    | **2.** Set **Start step** to ``1``.
    | **3.** Set **Stop step** to ``1``.

The last thing we need to specify is the direction and velocity of our shot. AMSinput uses the vector from one atom to another to define the shooting direction of the molecule gun. This is very convenient for us, since we can just use an atom of the buckyball and an atom of the sheet to define the direction.

.. rst-class:: steps

  \
    | **1.** Select one of the atoms in the buckyball by **left clicking** on it.
    | **2.** Add one of the atoms in the center of the sheet to your selection by holding the **Shift** key and **left clicking** it.
    | **3.** Click the **+** button next to **Velocity direction**.
    | **4.** Set a **Velocity** of ``0.05`` Å/fs.

.. image:: ../Images/MoleculeGun/molecule_gun_8.png

.. warning::

   The order in which the atoms are selected determines the direction of the shot! If you select them in the opposite order before clicking the **+** button, you will shoot in the opposite direction!

.. note::

   The distance between the atoms defining the direction will not affect the starting velocity. Their sole purpose is the definition of a direction.

.. tip::

   If your system does not already contain atoms you can conveniently use to define a shooting direction, you can always insert **dummy atoms** (``Xx`` in the periodic table tool) in convenient locations (or use **centroids**). These are not real atoms and will not be included in your simulation. They are just used for the setup of your calculation in AMSinput.

This concludes the setup of the calculation.

Visualizing the impact
----------------------

We are now ready to shoot! Let us run the calculation.

.. rst-class:: steps

  \
    | **1.** Click on **File → Save as...** and give it a reasonable job name.
    | **2.** Run the calculation with **File → Run**.

The AMSjobs window will come to the front as the calculation starts running. As ReaxFF is a very fast engine and the system not particularly big, it should only take a couple of minutes. We can already visualize our calculation while it is still running.

.. rst-class:: steps

  \
    | **1.** Select your job in AMSjobs by **left clicking on its job name**.
    | **2.** Click on **SCM → Movie** to visualize the trajectory.

.. raw:: html

   <center>
      <video controls width="700" src="../_downloads/molecule_gun.mp4"></video>
   </center>

You can download the movie :download:`here </downloads/molecule_gun.mp4>` if it does not play in your browser.
The saved movie was made using the **File → Save Movie...** command. If you want to use it you will have to install ffmpeg first.

Your initial velocity was probably not large enough to make the buckyball penetrate the graphene sheet. You will likely get a trajectory very similar to the one above. Note how the shock wave in the graphene starts interfering with itself as it travels across the periodic boundary conditions. Feel free to go back to AMSinput and increase the initial velocity of the buckyball. Doubling the velocity might already be enough to punch a hole into the graphene ...

This concludes the tutorial on the molecule gun in AMS.
