.. _reaxff_snapping_polyacetylene:

Snapping Polyacetylene Chain
****************************

This tutorial demonstrates how to set up a `molecular dynamics <../../AMS/Tasks/Molecular_Dynamics.html>`__ calculation with an increasingly deformed unit cell in order to study the mechanical properties of a small polymer chain model.
During the simulation, the strain on the chain is increased slowly until the initial double bonds of the cis-Polyacetylene are successively converted into their trans configurations.
Afterwards, an even larger strain causes the polymer chain to snap which immediately reduces the stress to zero.
The stress tensor components computed during the MD simulation are then collected with a small Python script and plotted to demonstrate different changes in the molecular structure of chain.


.. figure:: /Images/SnappingPolyacetylene/preview.png
   :align: center
   :scale: 70

.. note::

   With AMS2020 and later versions, the deformation of the Polyacetylene chain demonstrated in this tutorial can also be realized using a 1D periodic lattice. To use a 1D periodicity, the deformation of the x-axis needs to be set and the Polyacetylene chain needs to be rotated accordingly. 


Step 1: Start the GUI
=====================

We will set up an MD simulation from the GUI. Alternatively, you can download this :download:`PolyStressStrain.run <../downloads/PolyStressStrain.run>`.


.. rst-class:: steps

  \
    | Start AMSjobs
    | **SCM → New input**
    | Switch to **ReaxFF**: |ADFPanel| **→** |ReaxFFPanel|


Step 2: Import Structure and Settings
=====================================

We begin by setting the main calculation options for the molecular dynamics simulation.

.. rst-class:: steps

  \
    | In the **menu bar**, **File → Import Coordinates...**
    | Select :download:`cis_polyacetylene.xyz <../downloads/cis_polyacetylene.xyz>`
    | In the **main panel**, select **Force Field: → CHO.ff**


.. figure:: /Images/SnappingPolyacetylene/snapping_main_1.png
   :align: center
   :scale: 70


Next, set the options for molecular dynamics:

.. rst-class:: steps

  \
    | Click on |MoreBtn| next to **Molecular Dynamics**
    | As **Number of steps**, enter ``850000``
    | As **Checkpoint frequency** enter ``50000``


.. figure:: /Images/SnappingPolyacetylene/snapping_md_1.png
   :align: center
   :scale: 70


The simulation should run at constant temperature, so we add a thermostat:

.. rst-class:: steps

  \
    | Click on |MoreBtn| next to **Thermostat** and add a Thermostat
    | Select **NHC**
    | As **Temperature**, enter ``300.15`` K
    | As **Damping Constant**, enter ``100.0`` fs


.. figure:: /Images/SnappingPolyacetylene/snapping_thermostat_1.png
   :align: center
   :width: 50%


Next, we have to set up the deformation so that the chain is stretched during the simulation.

.. rst-class:: steps

  \
    | Select **Model → MD Deformations**, and add a deformation
    | Set the second field in **Length velocity** ``0.000020`` A/fs.

.. figure:: /Images/SnappingPolyacetylene/snapping_deform_1.png
   :align: center
   :scale: 70

Lastly, we need to calculate the stress tensor

.. rst-class:: steps

  \
    | **Properties → Gradients, Stress Tensor** Check stress tensor.

.. figure:: /Images/SnappingPolyacetylene/snapping_properties_1.png
   :align: center
   :scale: 70



Step 3: Run the Calculation
===========================
After having set all calculation options we are now ready to start the run

.. rst-class:: steps

  \
    | In the **menu bar**, select **File → Save** and enter ``PolyStressStrain``
    | In the **menu bar**, select **File → Run**
    | Switch to **AMSmovie** by clicking on **SCM** **→ Movie** to see the polymer change under strain

.. figure:: /Images/SnappingPolyacetylene/snapping_movie_1.png
   :align: center
   :scale: 70


Step 4: Evaluate the Results
============================
Once the calculation has finished, the stress-strain curves can be extracted from the binary results file
with the help of a Python script using the `PLAMS <../../plams/started.html>`__ library.

The script called :download:`stress_strain_curve.py <../downloads/stress_strain_curve.py>` can be run from the command line:

``$AMSBIN/amspython stress_strain_curve.py PolyStressStrain``

Be sure to match the job name correctly.

The stress-strain curve is written to a file called ``stress-strain-curve.csv``::

  # strain_x, strain_y, strain_z, stress_xx, stress_yy, stress_zz
  0.0000 0.0000 0.0000 -0.000002123540 0.000041449314 -0.000000198040
  0.0000 0.0026 0.0000 0.000001083810 0.000039450993 0.000000882455
  0.0000 0.0053 0.0000 -0.000006368834 0.000040380759 0.000000145990
  0.0000 0.0079 0.0000 0.000000862343 0.000039169395 0.000001048778
  0.0000 0.0105 0.0000 0.000000339014 0.000050208909 -0.000000796209
  0.0000 0.0132 0.0000 0.000000671946 0.000050569092 0.000001392349
  0.0000 0.0158 0.0000 0.000009834386 0.000061383368 0.000003143092
  0.0000 0.0184 0.0000 0.000000607648 0.000053138974 0.000005960118
  0.0000 0.0211 0.0000 -0.000005062346 0.000046333020 0.000000554734

The resulting stress/strain curve can then be plotted as ``stress_yy`` (column 5) against ``strain_y`` (column 2) with any plotting software, e.g. matplotlib:

.. figure:: /Images/SnappingPolyacetylene/curve.png
   :align: center
   :scale: 70

You can download an example script :download:`plot_stress.py <../downloads/plot_stress.py>`, which can be run with amspython to generate an image called ``stress-curve.png``.

Note the different segments in the stress/strain plot.
The first of these segments starts correspond to the polymer chain having increasingly more double bonds in trans configuration.
After the last double bond has been converted the resulting trans-Polyacetylene chain exhibits different mechanical properties which results in a different slope of the stress/strain graph.
At a certain strain, the chain snaps, immediately reducing the stress to zero as beyond this point the periodic polymer chain has turned into a molecular entity.

