.. _VASP:

TiO\ :sub:`2` surface relaxation
*********************************

**This tutorial will teach you how to**: 

* construct a slab for rutile TiO\ :sub:`2`\ (001)
* set up a geometry optimization job with constraints
* set up a DFT+U VASP job to be run via the AMS driver

.. image:: /Images/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_TOC.png

* :download:`Download .ams GUI input file </downloads/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_VASP.ams>` for this tutorial (optional).
* :download:`Download .py PLAMS Python script </downloads/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_VASP.py>` that sets up and runs an equivalent job (optional).


.. seealso::

   `VASP via AMS documentation <../../GUI/VASP_via_AMS.html>`__

Step 1: Check the VASP installation
===================================

.. important::

   VASP is **not** distributed together with the Amsterdam Modeling Suite, but
   needs to be obtained and installed separately.

Verify that you have access to a working installation of VASP 5, on either your local or a remote machine. If you want to run on a remote machine or computer cluster, check that you have set up a working `AMSjobs queue <../../GUI/AMSjobs.html#setting-up-your-own-queues>`__ for that system.

Check that you can run VASP, for example using one of the following commands:

.. code-block:: bash

   vasp
   mpirun -np 4 vasp #parallelize over 4 cores

If you do not know the proper command to launch VASP, ask your system administrator.

Step 2: Locate the POTCAR library
=================================

VASP requires the use of pseudopotentials or PAW potentials for each element.
These are distributed with VASP in files called POTCAR or POTCAR.Z.

In this tutorial, you will use the Projector Augmented Wave (PAW) potentials for
Ti and O constructed for the PBE density functional. You should have obtained
those PAW potentials with VASP.

On your local machine (the machine running AMSinput), locate the needed POTCAR files.
If you do not have them, you can download them from the VASP website.

For example, if the needed POTCAR or POTCAR.Z files are at

.. code-block:: bash

   /some/path/PAW_PBE/Ti/POTCAR
   /some/path/PAW_PBE/O/POTCAR

then the path ``/some/path/PAW_PBE/`` would be the **POTCAR Library** that you need
to specify in one of the following steps.


Step 3: Set up the system - a TiO\ :sub:`2`\ (001) slab
=======================================================

.. rst-class:: steps

  \
    | **1.** Start AMSinput
    | **2.** Switch to **VASP**: |ADFPanel| **→** |VASPPanel|
    | **3.** In the **menu bar**, select **Edit → Crystal → Tetragonal → Rutile**
    | **4.** Click **OK** to get the experimental rutile TiO\ :sub:`2` crystal structure unit cell (*a* = 4.59 Å, *c* = 2.96 Å).
    | **5.** Click **Yes** when asked whether to map the atoms to the unit cell.

.. note::

   In production calculations, one would normally perform a lattice optimization of the bulk structure
   before creating a slab. In this tutorial, we will just use the experimental lattice parameters.

Now create a 2-layer (001) slab (because the crystal unit cell contains 2 layers of atoms
at different positions along **c**, the resulting slab will actually be 4
*atomic* layers thick).

.. rst-class:: steps

  \
    | **6.** Select **Edit → Crystal → Generate slab** 
    | **7.** Enter ``0 0 1`` as the Miller indices.
    | **8.** Set the **number of layers** to ``2``.
    | **9.** Click "Generate slab".

This should create a 2-layer slab in the 3D area on the left. Select **View →
View Direction → Along X** from the menu bar, or rotate the system so that the
z-axis (shown as a blue line) is roughly displayed vertically, giving you a
side view of the slab.  The slab is 2\ *c* = 5.92 Å thick.

.. note::

   * It may happen that bonds are drawn between adjacent Ti ions. These bonds do not affect the VASP calculation and can safely be ignored. If you prefer, you can remove them by clicking on them and pressing Backspace.

   * In production calculations, one would normally use a much thicker slab.

All VASP calculations are performed under 3D periodic boundary conditions. Therefore, slabs
are necessarily separated by a **vacuum gap** in the surface normal direction.

.. rst-class:: steps

  \
    | **10.** Click on the Periodic View Tool |PeriodicViewTool| to visualize a few periodically repeated images of the central cell.

Note that the vacuum gap is very large. Because VASP uses a planewave basis
set, a larger vacuum gap will increase the computational cost.  Therefore, it
is a good idea to use a smaller vacuum gap, but the vacuum gap should not be
so small that one side of the slab interacts with the other side through the
vacuum gap. Here, we will set a rather small vacuum gap of about 8 Å.

.. note::

   In production calculations, the vacuum gap should be systematically varied for
   the particular system at hand, and be large enough such that any calculated
   quantity (surface energy, adsorption energy, work function, etc.) is
   converged.

.. rst-class:: steps

  \
    | **11.** In the **panel bar**, select **Model → Lattice**.
    | **12.** Set the components of the **c** lattice vector to ``0.0 0.0 14.0``. (Note: this **c** lattice vector now refers to the slab system including the vacuum gap, and no longer to the original unit cell of the crystal).
    | **13.** Click on one of the Ti atoms in the center of the slab to select it. Then, in the **menu bar** select **Edit → Crystal → Set (0.5, 0.5, 0.5)**. This moves the slab to the center of the vacuum gap, which typically makes visualization easier.
    | **14.** Click again on the Periodic View Tool |PeriodicViewTool| so that only a single periodic image is displayed.
    | **15.** In the **menu bar**, select **Edit → Crystal → Map atoms to (0..1)**. This places all of the atoms inside the displayed unit cell.

.. image:: /Images/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_slab_small_vacuum_gap.png

Step 4: Set the VASP settings
==============================

.. rst-class:: steps

  \
    | **1.** In the **panel bar**, select **Main**. 
    | **2.** In **Command to execute VASP** enter the command to execute VASP (from **Step 1**).
    | **3.** In **POTCAR library** enter the path to the PBE PAW POTCAR library (from **Step 2**). This path will be remembered the next time you start AMSinput.

.. tip::

   In the **panel bar**, select **Details → Pseudopotentials** to see and/or change exactly which POTCAR files that will be used in the calculation.

.. rst-class:: steps

  \
    | **4.** In the **main panel**, set the **Type of k-point grid** to **Monkhorst-Pack** (default).
    | **5.** Set the **k-point grid dimensions** to ``3 3 1``.
    | **6.** Set the **XC Functional** to **PBE**.
    | **7.** Set the **Planewave energy cutoff** to **400 eV** (default).
    | **8.** Set the **Type of smearing** to **Gaussian** (default).
    | **9.** Set the **Smearing width** to **0.1 eV**.
   
.. image:: /Images/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_VASP_settings.png

.. note::

   In production calculations, the k-point grid dimensions and planewave energy cutoff need to be converged by means of convergence tests.

.. rst-class:: steps

  \
    | **10.** In the **panel bar**, select **Model → Hubbard U**.
    | **11.** Check the **Use DFT+U** checkbox.
    | **12.** Set **Hubbard U-type** to **2** (default, the method by Dudarev et al.)
    | **13.** Set **LMAXMIX** to  **4**.
    | **14.** For Ti, set **U** to **3.0 eV**, and **l** to **d** (default).
    | **15.** For O, set **l** to **Disable**.

.. image:: /Images/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_HubbardU.png

The main VASP input file, INCAR, allows the user to set an enormous number of
settings and have great control over the resulting calculation.  AMSinput does
not have dedicated panels for all of the settings. Instead, it is possible for you to
set arbitrary settings by simply typing them in. In this example, you will
change the self-consistent-field algorithm.

.. rst-class:: steps

  \
    | **16.** In the **panel bar**, select **Details → Expert VASP**.
    | **17.** Type ``ALGO = Fast`` in the **Additional INCAR options** text box.

.. tip::

   On the **Details → Expert VASP** panel, consider checking the **Only
   preprocess** box. When you submit your calculation, VASP will then not be
   executed, but all of the input files that VASP *would* have seen will be
   left on disk for you to inspect. This way, you can double-check that the
   input to VASP is correct before actually running the calculation.



Step 5: Set the AMS settings
============================

.. rst-class:: steps

  \
    | **1.** In the **main panel**, select **Task → Geometry Optimization**.
    | **2.** Click the |MoreBtn| button, or in the **menu bar** select **Details → Geometry Optimization**.
    | **3.** Inspect, but do not change, the **convergence criteria**.
    | **4.** Click the |MoreBtn| next to **Constraints**, or in the **menu bar** select **Model → Geometry Constraints and PES Scan**.
    | **5.** In the **molecule drawing area**, select the six atoms (2 Ti and 4 O) in the center of the slab, by first clicking on one of them, and subsequently **clicking the others while holding Shift**.
    | **6.** Click the |AddButton| button next to **selected atoms (fix positions)**.


.. image:: /Images/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_constraints.png

.. rst-class:: steps

  \
    | **7.** In the **menu bar**, select **File → Save**, and save your job with the name ``VASP_PBE_U_TiO2_slab.ams``.

.. note::
   When running VASP via the AMS driver, the geometry optimization settings and constraints are set for the AMS driver and not for VASP. This means that VASP's internal geometry convergence criteria, like the EDIFFG setting in INCAR, should *not* be set. You also do not need to enable VASP's "Selective optimization" to keep some atoms fixed. Instead, all geometry optimization settings are handled by the AMS driver.

Step 6: Run your job
====================

.. rst-class:: steps

  \
    | **1.** Open AMSjobs: **SCM → Jobs**.
    | **2.** Select your job in the list. In the **menu bar**, select **Queue → Interactive** if you want to run the job on your local machine, or select the queue for the remote machine that you want to run on.
    | **3.** In the **menu bar**, select **Job → Run**.

After the calculation has finished, visualize the geometry optimization in AMSmovie. 

.. rst-class:: steps

  \
    | **4.** Select your job in AMSjobs, and open AMSmovie: **SCM → Movie**.
    | **5.** In the **menu bar**, select **View → Molecule → Balls**
    | **6.** Use the horizontal scrollbar at the bottom of the window to see the steps of the geometry optimization.

.. image:: /Images/VASPTiO2SurfaceRelaxation/TiO2_surface_relaxation_amsmovie.png

Did the top-layer Ti atoms relax "in" towards the bulk or "out" towards the vacuum?

