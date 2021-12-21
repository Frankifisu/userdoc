AMSmovie
########

.. _metatag ADFMOVIE: 

The AMSmovie module of the GUI is used mainly to visualize molecular geometries, and graphs related to it.
For example, follow the progress of a geometry optimization, the trajectory of an MD run, or visualize the Potential Energy Surface.

Additionally scalar atomic data (like names, charges, atomic temperature, etc) and vector atomic data (forces, gradients, velocities) may be visualized when available.

Geometries
**********

When opening a results file, AMSmovie will show the current geometry of the system.
If multiple geometries are available, there will be a slider and buttons that allow you to play a movie, and to move to a specific frame.

If the calculation is a PES (Linear Transit) calculation, there may be many unconverged geometries as well as converged geometries.
In the View menu you can toggle if you want to see all geometries, or just the converged geometries.

Scalar Atomic Properties
************************

If atomic properties are available for a geometry, you can show them using the View menu:

- Atom Info: show the selected property as a text label
- Color Atoms By: use the selected property to color the atoms
- Atom Radius From: use the selected property to scale the atoms

Properties may be things like Name, AtomType, Charge (actually many different kinds of charges), ...

Atomic Vectors
**************

If atomic vectors are available for a geometry, you can show them using the View menu:
use the Vectors command in the View menu to select which vectors to show.

Examples of atomic vectors: gradient, force, velocity

When doing a geometry optimization via AMS, or an MD calculation via AMS or ReaxFF these may be present.

With the Scale Vectors menu command in the View menu you can make the vectors bigger or smaller (often needed to see very small vectors at all).

Graphs
******

AMSmovie can also make graphs of many properties (like energy, temperature, selected distances, angles etc) that change with the geometry.
Check the tutorials for many examples.


Note that you can have multiple curves in one graph, and you can have multiple graphs.

You can save the graph in many different formats, and you can export the graph data using commands in the Graph menu.
To delete a graph make it the active graph by clicking in it, and next use the Backspace key or the Delete Graph menu command.

In some special cases like NEB and PES you can also visualize a function of two variables in an XYZ style plot.
Thus for a PES you can actually see the landscape as a function of two scan coordinates.


Temperature Profile
*******************

Temperature profiles, if calculated in an AMS MD run, can be visualized either as XY plot for a specific frame "Temperature Profile At Current Frame", or as 2D plot "Temperature Profile At All Frames. Both commands live in the Graph menu.

You will have to select which temperature profile to visualize (along which cell axes). And you will need to specify over how many frames to average.

The average is a simple average over a block of frames of the required size. For frame i, averaging over n frames,  the frames max(i-n+1,0) ... i will be averaged. 

For example, if averaging over 5 frames, the value for frame 10 will be the average over frames 6, 7, 8, 9 and 10. For the first few frames, the blocks will be smaller. In the same example, the value for frame 2 will be the average over frames 0, 1, and 2. 

The visualization at the current frame will show on the X axes the points along the selected cell axes, and on the Y axes the temperature. When moving through the trajectory the full graph will refresh to show the data for the current frame.



Trajectory Analysis
*******************

AMSmovie also provides an interface to some tools to analyze MD trajectories, apart from the graphs.
They are available in the MD Properties menu.

- Autocorrelation functions (ACF, including diffusion coefficient from velocity ACF, and including the Fourier transform)
- Histograms
- Radial Distribution Function (RDF)
- Molecule Fractions: make graphs of specific molecules detected
- ChemTraYzer: use the Reaction Event Detection command in the Properties menu to analyze reactions happening

.. seealso::

   The `Trajectory Analysis <../AMS/Utilities/TrajectoryAnalysis.html>`__ AMS utility.

.. index:: .dcd
.. index:: .psf
.. index:: .bgf
.. index:: .xmol
.. index:: .xyz

Export trajectories to other formats
************************************

In the File menu of AMSmovie there are also commands to convert trajectories to other formats (**File → Export Trajectory As**). 

If you have an AMS results file (with extension .rkf) corresponding to an MD trajectory you can convert it to:

* DCD file (.dcd, with corresponding .psf file) 
* BGF (.bgf)
* Xmol (.xmol) 
* XYZ (.xyz) 

You can also use the **Scripting** menu in **AMSjobs** to perform such conversion.
