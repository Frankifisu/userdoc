AMSview
#######

.. _metatag ADFVIEW: 

The AMSview module of the GUI is used mainly to visualize field data like orbitals, densities and potentials. Additionally, it can also visualize some scalar atomic data, tensor data, and Bader (AIM) results. 

Visualization methods
*********************

Via the Add menu you can select a visualization tool. This tool (an isosurface, or a cut plane for example) can be used with any kind of field. After selecting the command to add the visualization tool you will get a new extra control bar at the bottom of the window.  

The following visualization tools are available: 

+ Isosurface: a simple isosurface through a scalar field

+ Colored Isosurface: an isosurface through a scalar field colored by a second field

+ Isosurface with Phase: an isosurfaces through a scalar field, colored by the complex phase (or sign for a real field). Typically used for orbitals.

+ Multi Isosurface: multiple isosurfaces colored by isovalue

+ Colored cut plane: a plane through some field, colored by the values of the field

+ Contours cut plane: a plane through some field, with contour lines on the plane to show the values of the field

+ Contours(+/-) cut plane: a plane through some field, with contour lines on the plane to show the values of the field, with negative contours using dashed lines

+ Vector Field: many vectors on a grid, pointing as directed by some vector field. You can get a vector field by calculating the gradient of some other field for example. You can do this via the Calculated Fields menu command.

+ StreamLines: an alternative to visualize a vector field. 

In the control bar you select what field to visualize. The fields will be calculated on the fly. The leftmost field of the control bar (containing the name of the visualization method) also is a pull-down menu that you can use to access details, or to delete that particular visualization tool. 

Spinor: spin magnetization density
==================================

Spinors are a result of spin-orbit coupled calculations. Visualization of spinors is more difficult than visualization of orbitals. A spinor :math:`\Psi` is a two-component complex wave function, which can be described with four real functions :math:`\phi`: real part :math:`\alpha` :math:`\phi_\alpha^R` , imaginary part :math:`\alpha` :math:`\phi_\alpha^I` , real part :math:`\beta` :math:`\phi_\beta^R` , imaginary part :math:`\beta` :math:`\phi_\beta^I`: 

.. math::

   \Psi = \binom{\phi_\alpha^R + i \phi_\alpha^I}{\phi_\beta^R + i \phi_\beta^I}
   
The density :math:`\rho` is: 

.. math::

   \rho = \Psi^\dagger \Psi

The spin magnetization density :math:`m` is: 

.. math::

   m = \Psi^\dagger \sigma \Psi

where :math:`\sigma` is the vector of the Pauli spin matrices :math:`\sigma_x`, :math:`\sigma_y`, and :math:`\sigma_z`. A spinor is fully determined by the spin magnetization density and a phase factor :math:`e^{i \theta}`, which both are functions of spatial coordinates. 

The (square root of the) density and spin magnetization density are visualized as a double isosurface and a vector field respectively. The phase factor :math:`e^{i \theta}` , reduced to a plus or minus sign, is visualized with the double isosurface and with the color of the vector field. 

The main control bar is identical to the control bar of a normal isosurface. If you show the details, you will find that in addition to the controls available for a normal isosurface,  you can also specify coloring information. In this case, the two numbers for the HSV colors define the colors of the minus and plus sign. 

Fields
******

Fields can be things like orbitals or densities. You select them from the field pull-down menu in the control bars. In the Fields menu the Grid option determines on what kind of grid the field will be calculated. 

As a convenient short-cut, you can switch fields using the up/down arrow keys 

For many fields, like orbitals, transition densities etc selecting the option from the field pull-down menu brings up a window where you can select the field of interest. 
As an example, selecting 'Occupied Orbitals' will bring up a window that lists all occupied orbitals.

In these field select windows you can sort the fields by clicking on a column header. Clicking again on the same column header will reverse the sort order.
When you use another command from the field pull-down menu the select window will close, unless you check the 'Keep Open' check box.
That allows you, for example, to show all orbitals (both occupied and virtual) at the same time.

You can also create new fields out of these basic fields by combining them (calculated fields, for example the difference between two fields), or by interpolating them to get a finer or less dense field. 

Steric Interaction
==================

The Steric Interaction field is generated using Van der Waals radii to visualize steric bulk. The field is the minimum distance to the Van der Waals surface of the selected atoms. The radii are taken from the MM3 method by Allinger (N.L. Allinger, X. Zhou, J. Bergsma, *Molecular mechanics parameters*, `Journal of Molecular Structure: THEOCHEM 312, 69 (1994) <https://doi.org/10.1016/S0166-1280(09)80008-0>`__). An isovalue of 0 corresponds to the Van der Waals surface.

Properties
**********

In the Properties menu you find commands to visualize scalar atomic info. Either by displaying the numbers, scaling the atom radii by these numbers, of by using the scalar values to color the atoms. 

You also find some short-cuts to generate orbital plots: HOMO-1, HOMO, LUMO, LUMO+1, Density and Spin=Density. These commands will generate a double isosurface, and select the appropriate field for it. 

Next are commands to visualize some tensor data, depending on what tensor data is available. The tensor is visualized as a sphere scaled in the directions of the  eigen-vectors of the tensors by the eigenvalues of the tensors. For each visualized tensor type you will get a control bar that allows you to tune the visualization. 

Finally, the properties menu allows you to visualize some Bader results. The Bader sampling shows you the integration grid, but with all the grid points colored  that are together in the same Bader basins. The AIM (Bader) command visualized the critical points and critical paths. 

Comparing data from several molecules
*************************************

AMSview can handle more than one molecule at the same time. You can show fields for different molecules in the same window, you can create calculated fields to see differences, and so on. 

The different molecules may come from different files, or from one result file containing multiple geometries. An example of the first situation would be two different calculations, with different XC potential, resulting in two different .t21 files. An example of the second would be the .t21 file from a NEB calculation. That file contains the information for all images, so you can see how (for example) the HOMO changes from image to image. 

To add a new molecule from a different file, just open an additional file using the Open menu command from the File menu. 

AMSview has a 'current' geometry. The molecule shown will be the one for the current geometry only. 

To change the 'current' geometry, use the horizontal slider below the molecule window. 

The visualization items (surfaces) might be filtered in such a way that only items related to the current geometry are shown. This is the default when visualizing NEB results: you want to see how the density or an orbital changes going from one image to the next (using the slider). If you open different files the default is to show visualization items for all  geometries at once. Thus you might compare orbitals from one fragment with those from another. You can switch this behavior using the 'Show All Geometries' menu command from the View menu. 

You can easily compare calculations on the same molecule that differ in something else then geometry. Just open both result files (.t21). Next, you can calculate differences between similar things. If you add a calculated field, you will find that the first command in the field select menu is used to select the geometry from which to take the data. Thus, you can select  the same property from different files and compute the difference. 

**Warning:** The current implementation has no possibility to adjust the orientation or the grid. In practice this means that you need to take care that the fields that you compare actually make sense to compare. This is only the case if the geometry of the molecules is identical and thus the grid is identical. Though this is very restrictive, you can make interesting comparisons for a given molecule: change due to different XC, basis sets or integration accuracy for example. 

Temporary Files
***************

AMSview normally will run DENSF or BAND in the background. This means that it needs scratch space to store inputs and result files to be visualized. After normal termination of AMSview (using Quit) all scratch files will be removed. 

The scratch files will be created in the following location: 

+ If $SCM_TMPDIR is defined : use the $SCM_TMPDIR directory

+ else, if $HOME is defined: use the $HOME directory

+ else, if $TMPDIR is defined: use the $TMPDIR directory

+ else try to use the current working directory.

Calculating Fields
******************

AMSview will show you a progress dialog with some options when calculating fields. 

In front of the progress bar you will notice a right-pointing arrow. If you click on it the progress dialog window will enlarge, and you can follow the progress of the field calculation (by DENSF) in detail. If you scroll back in that window you can also examine the input given to DENSF. Obviously this output is also very useful when there is some problem calculating the field. Click the Close button at the right of the progress bar to close the progress dialog. 

You will also see a Run button, and before it a pull-down menu that you can use to select a queue. When the calculation of a field is slow  (for a fine grid or big molecule) you can press Run, and the calculation will be saved as a job in AMSjobs, and will then automatically be started to run in the specified queue. After the calculated has started you may quit AMSview if you wish, the results should automatically be picked up when you start AMSview again (and when the fields are available). As you can select the queue to used, you can also calculate the fields on some remote  machine if you wish. See the AMSjobs documentation about the use of queues. 

While a field is being calculated via AMSjobs, it will be visible in AMSjobs as a new job. The results will be stored with that job. When you start AMSview for your original molecule it will detect the newly available fields automatically. It will move the newly calculated fields to it self, and delete the job that was used to calculate the fields. 

When you close AMSview after calculating some fields, AMSview may ask you to save the field. If you save the field it will automatically be available the next time you start AMSview (for this job). Be warned that saving many fields may take a lot of disk space. You can use the Clean Up command in AMSjobs to delete them. 

