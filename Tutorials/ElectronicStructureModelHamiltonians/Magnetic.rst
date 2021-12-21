.. This tutorial has been recorded: examples/tutorials/benzene-magnetic
.. Keep the recording in sync so it may be used to generate the images!

.. _band_Magnetic: 


Benzene molecule in a magnetic field
************************************

This tutorial will show you how to: 

+ handle the effect of a `magnetic field <../../BAND/Model_Hamiltonians/Electric_and_Magnetic_Fields.html#magnetic-field>`__ on a molecule using `BAND <../../BAND/index.html>`__
+ visualize the resulting vector field (magnetic current) as vectors, and as streamlines

Step 1: amsinput
================

Start AMSinput in a clean directory.

.. image:: /Images/Magnetic/amsinput_BAND_Main.png

Step 2: Setup the system - benzene
==================================

Make a benzene molecule. One easy way is to search (|Search|) for Benzene and select it.

.. rst-class:: steps

  \
    | 1. Make a benzene molecule.

Go to the Main panel for BAND, and turn of periodicity:

.. rst-class:: steps

  \ 
    | 2. Switch to **BAND**: |ADFPanel| **→** |BANDPanel|
    | 3. Periodicity **None**

.. image:: /Images/Magnetic/Magnetic-1.png

and turn on the magnetic field:

.. rst-class:: steps

  \ 
    | 4. Go to the **Magnetic Field** panel.
    | 5. Enter 0.1 in the Bz field.
    | 6. Select the NR_LDOTB method.

.. image:: /Images/Magnetic/Magnetic-2.png

Step 3: Run the calculation
---------------------------

Now you can save and run the calculation.

.. rst-class:: steps
  
  \ 
    | 1. **File → Save**, give it a name and press Save.
    | 2. **File → Run**

Step 4a: Magnetic current: vectors
----------------------------------

After the calculation finished, open the result file with AMSview:

.. rst-class:: steps

  \ 
    | 1. **SCM → View**

Add a vector field:

.. rst-class:: steps

  \ 
    | 2. **Add → Vector Field**
    | 3. Select the  **Magnetic and Current fields → Current Density**

You will not see any vectors yet. The reason is that the vectors are very small.
If you move the mouse over the real field at the bottom right (the max-color field), you can notice the range in the help balloon.

The vectors in the Clamp range will be scaled to vectors in the 0 .. 1 range. To make our vectors visible, change the upper clamp value to a smaller number:

.. rst-class:: steps

  \
    | 4. Change the second clamp value to 5e-10
    | 5. Change the color max value also to to 5e-10
    | 6. Check the box in front of Bar to show the color bar
    | 7. Rotate and zoom the image to get a good view

Now you should see your vector field similar to this:

.. image:: /Images/Magnetic/Magnetic-vectors.png

If you wish you can play with the values in the control line.
Please use the help balloons, the meaning of those values is not obvious!


Step 4b: Magnetic current: streamlines
--------------------------------------

Another way to visualize a vector field is to generate streamlines.

Conceptually, one defines seed points, and then a line is generated starting at each seed point, following the vectors.
For visualization purposed, a tube is generated around the lines, and the width of the tube depends on the magnitude of the vectors.

There are many options, the most important is to select the seed points.
Again, the help balloons are important, they describe in detail what the controls do.

The default is to use starting points randomly distributed in a sphere:

.. rst-class:: steps

  \
    | 1. **Add → StreamLines**
    | 2. Select the **Magnetic and Current fields → Current Density**
    | 3. Change Npts to 15
    | 4. Change R to 5
    | 5. Change the max-color field to 5e-10

.. image:: /Images/Magnetic/Magnetic-vectors-sphere.png

An alternative is to define a line, and generate the starting points linearly distributed along that line.
You can activate controls for the line to position it as you want.

.. rst-class:: steps     

  \
    | 6. Change Sphere to Line
    | 7. Check the Controls box
    | 8. Drag the end points of the line such that the line crosses the benzene diagonally (out of plane)

.. image:: /Images/Magnetic/Magnetic-vectors-line.png

Finally you can use a grid in a plane as starting points for the streamlines.
Npts is the number of grid lines per dimension, thus the number of streamlines will be the square of Npts if you are using a plane.

The StreamLines technique has some important Detail options. To get them, select the Show Details option from the StreamLines pull-down menu at the bottom.
The help balloons give the details, especially the streamline radius and the scaling method (flux or norm) are important.

Now try for yourself, make some nice looking picture... the following was made combining several techniques from above.

.. rst-class:: steps

  \
    | 9. Experiment, try to make a picture similar to the following picture.
    | Hint: it consists of vectors visualization, and TWO sets of streamlines (and an improved background color).

.. image:: /Images/Magnetic/Magnetic-show.png

