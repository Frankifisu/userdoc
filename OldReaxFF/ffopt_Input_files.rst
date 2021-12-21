
.. _params_file:

Input files common for all optimizers
=====================================

In order to optimize a ReaxFF forcefield, the files listed below must be present in the directory where the reaxff program is executed. 

+ *iopt* - file containing a line of text with a single number on it. To use the basic FFOptimizer features this file must contain 6. See the *ffoact* description below for more details. 

+  :ref:`ffield <ffield>`- the initial force-field file.

+ *control* - in addition to general ReaxFF control parameters it may also contain the FFOptimizer-related ones explained in the corresponding sections.

+ :ref:`trainset.in <trainset_in>` - file with test values from the training set, the same as in the original reaxff force-field optimization, see page 27 of the ReaxFF User Manual.

+ *params* - file that describes variable forcefield parameters, one line per parameter (see example below).

  This format is a generalization of the original params file format. 

  The hash symbol '#' starts a comment. Each non-comment line must begin with three integer numbers, the section-block-item coordinates of the corresponding parameter. The first coordinate specifies a section: 1 - general parameters, 2 - atomic parameters, 3 - bonds, 4 - off-diagonal terms, 5 - valence angles, 6 - torsion angles, 7 - hydrogen bonds. The second coordinate specifies a block within the given section or an item index for the general parameters section (section=1). The third coordinate specifies an item index within the block, except for section 1 for which the third coordinate is ignored. The coordinates can optionally be followed by a one or more real number. The number and the meaning of the reals depends on the selected task. For some force-field optimization methods the first three real number have a special meaning referred to as *delta* (or *sigma*), *ffmin*, and *ffmax* in the following sections, respectively. A params file can be generated using the :ref:`rxffutil utility <rxffutil>`.

  An example of the params file:

::

  # i j k   x1   x2   x3  ...
    1 1 0  0.1 -1.0  1.0   # The 1st general parameter
    2 3 4  0.1 -1.0  1.0   # The 4th parameter of the 3rd atoms block
  ...

+ *ffield_bool* - an alternative way to specify variable parameters if the params file is not present. This file has the same format as ffield but instead of parameter values it contains 1.0 or 0.0 as a flag whether the corresponding value is to be variable or not, respectively.

+ *ffield_min* - an alternative way to specify minimum values (*ffmin*) for the variable parameters if the *params* file is not present. This file has the same format as *ffield*.

+ *ffield_max* - an alternative way to specify maximum values (*ffmax*) for the variable parameters if the *params* file is not present. This file has the same format as *ffield*.

+ *geo* - file with the training set geometries in the BGF format, the same as in the original reaxff force-field optimization. Geometries of different molecules in this file must be concatenated.

+ *models.in* - as an alternative to a single *geo* file one can save each geometry in its own file and list the files that are part of the training set here. The molecule name specified in the *models.in* file must match that in the *trainset.in* file and it takes precedence over any molecule name specified inside the geometry file (filename1, etc.). The format of the file is as follows:

::

  filename1 MoleculeName1
  filename2 MoleculeName2
  ...

