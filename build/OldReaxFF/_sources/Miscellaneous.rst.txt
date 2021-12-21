

Other new features and fixes
############################

Repeating the unit cells
************************

A simple way to increase the size of the simulation box is by multiplying it a number of times in the a, b, and c directions. In the ReaxFF program this can be achieved by specifying the *reptx*, *repty*, and *reptz* keys (for the a, b, and c direction, respectively) in the control file. The specified value must be strictly positive and the default is 1 (one) for each of them. 

Molecular charges
*****************

In order to freeze the total charge of a group of atoms (for example, a molecule) one can add a MOLCHARGE key to the geo file in the BGF format. The format of the key is as follows::

 MOLCHARGE  n1 n2 q

where ``n1`` and ``n2`` specify indices of the first and the last atoms of the molecule and ``q`` is the charge. All atoms between ``n1`` and ``n2`` will be included in the molecule. 
When specifying the MOLCHARGE key *all* atoms present in the system must be assigned to one of the the molecules. For example, if your system consists of 10 water molecules and 
the charge of the first of them is constrained to be +1 and the total charge of the system is zero then the following two MOLCHARGE keys must be specified::

 MOLCHARGE  1  3  1.0
 MOLCHARGE  4 30 -1.0

.. Note::
  
  The MOLCHARGE is implemented as a simple constraint in the charge equilibration procedure and it does not take any bonding information into account. 
  This means that specifying molecular charges using the MOLCHARGE key makes sense only if you are sure that the constitution of the molecule will not change during calculation. 
  This is useful, for example, when fitting EEM-related parameters in a force-field.

External electric fields
************************

External electric field regimes are specified in an external file ``eregime.in``.
The presence of this file in the ReaxFF run directory will activate the electric fields. 

The format of this file is as follows::

 #Electric field regimes
 #start #V direction1 Magnitude1(V/A) direction2 Magnitude2(V/A)
  0000  1      x        0.010000
  1000  1      x       -0.010000
  2000  1      y        0.010000
  3000  1      y       -0.010000
  4000  2      x       -0.010000           y       -0.0100
  5000  2      x        0.010000           y        0.0100 

.. Note::
  
  The electrostatic potential is sawtooth-like, which requires a vacuum zone (we suggest 10Å) 
  on the box plane perpendicular to the efield vector. Otherwise one risks abnormal polarization for atoms on two sides of the plane.
  A good strategy to ensure the vacuum zone is to define an elastic wall restraint (see below).

Example: 

Adding the following lines to your run script::

 cat > eregime.in <<eor
 #Electric field regimes
 #start #V direction Magnitude(V/Angstrom)
 0000 1 x  0.010000
 1000 1 x -0.010000
 eor

will overlay an external electric field with magnitude 0.01 V/Å in x-direction for the duration of 1000 iterations, then
the magnitude is switched to -0.01 V/Å and kept for the rest of the simulation.


Elastic wall restraint
**********************

.. _elasticwall:

The wall is implemented as a :math:`cos^2(x)` function (one period) between Coord-HalfWidth and Coord+HalfWidth with a maximum at Coord. The Height value is given in kcal/mole. At this moment, the elastic wall restraint can only be used with an orthorhombic unit cell. 

The wall is specified in the geo file as::

 EWALL RESTRAINT AxisIndex Coord HalfWidth Height

For example, for a wall that crosses the Z axis at z=7 Angstrom, is 2.0 Angstom thick and 100 kcal/mole high, the input would look like this::

 EWALL RESTRAINT  3  7.0  1.0  100.0

.. Note::

   We recommended to set the icentr option in the control file to 0 to avoid inconsistencies between the initial atomic coordinates and the wall position.


.. _ACKS2:

ACKS2: Atom-condensed Kohn-Sham DFT approximated to second order
****************************************************************

The ACKS2 charge equilibration scheme has been implemented following the original paper 
"ACKS2: Atom-condensed Kohn-Sham DFT approximated to second order" by T. Verstraelen et al. 
J. Chem. Phys. 138 (2013) 074108. 

Using the ACKS2 scheme requires a suitable force-field, which is recognized by 
"[ acks2 ]" at the start of the first line of force field file (note: the spaces around "acks2" are important!). 
Besides, the `icharg` parameter in the control file must be set to 7.
In addition to the general EEM parameters the ACKS2 scheme needs 
the general force-field parameter #35 ("Xamp") and the atomic cut-off parameter #23 ("softcut").

.. _taperbo:

Correction for small bond orders
********************************

There is a discontinuity problem for small bond orders in the expressions for covalent and hydrogen bonds, valence and torsion angles. 
The discontinuity and the correction for it are described in detail in `J. Phys. Chem. Lett. 10 (2019) 7215 <https://doi.org/10.1021/acs.jpclett.9b02810>`__.

The correction can be switched on by setting the taperb control flag to 1.

.. _torsions2013:

Correction for torsion angles asymptotics
*****************************************

The discontinuity at small bond orders in the expression for torsion angles and conjugation contributions can alternatively be corrected for using the tors13 correction. 
The corresponding terms are given by f\ :sub:`10` (eq. 10b) and f\ :sub:`12` (eq. 11b) in the `original ReaxFF paper <https://doi.org/10.1021/jp004368u>`__. 
The new expression for each term in f\ :sub:`10` is :math:`\left(1 - e^{-2 \lambda_{23} BO^2} \right)` and in f\ :sub:`12` the new expression is :math:`sin(\frac{\pi}{3} BO)^4`. 
The new expressions ensure correct asymptotic behavior for the dE/dBO for BO :math:`\rightarrow` 0. 

The correction can be enabled by setting the tors13 flag in the control file to 1.

Another discontinuity in the torsion angle term is when one or both valence angles approach 180 degrees. It is described in detail in `J. Chem. Phys. 153 (2020) 021102 <https://doi.org/10.1063/5.0013906>`__. 

The corresponding correction can be enabled by setting the tors19 flag in the control file to 1.

Using the above corrections can make geometry optimizations more stable and improve conservation of energy during MD.

LG dispersion
*************

The LG dispersion correction was implemented following the paper `Liu et al., *ReaxFF-lg: Correction of the ReaxFF 
Reactive Force Field for London Dispersion, with Applications to the Equations of State for Energetic 
Materials*, J. Phys. Chem. A, 2011, 115 (40), pp 11016–11022 <https://doi.org/10.1021/jp201599t>`__

The LG dispersion correction is turned on when using a suitable forcefield, which is recognized by the 
"[ lgDispersion=1 ]" key in the file header. 

.. _rxffutil:

The rxffutil utility
********************

Usage::

  rxffutil command [arguments]

reformat
--------

The **reformat** command tells rxffutil to read a (possibly mis-formatted) force-field file from standard input and write it in the format required by the ReaxFF program::

  rxffutil reformat < input_ffield_file

The result is written as a 'ffield' file in the current directory. The input can be almost free-format but the following points need to be taken into account:

* If you copy-paste force-field parameters from a pdf document (for example, from a publication's supporting info), then make sure to remove any page numbers that may have been copied together.

* The atom types section header (with the number of atom types in it) must have three comment lines following the line with the number of atom types.

* Likewise, the bond types section must have one comment line following the line with the number of bond types. Any comments provided on input are ignored and the standard comments are written instead.

* Numbers must be separated by at least one space

minmax
------

The **minmax** command is intended for analyzing existing forcefield files. It will print the number of entries, as well as the minimum, maximum and average values for the given parameters::

  rxffutil minmax [--ffdir=/path/to/ff/directory] key ...

Command arguments:

* *- -ffdir=/path/to/ff/directory* -- scan the specified directory for ff files when computing parameter ranges. The $AMSRESOURCES/ForceFields/ReaxFF directory is used if this option is absent.

* *key* (mandatory) -- specifies which parameters to gather data for. Multiple keys may be specified. The syntax of the keys is as follows:

  -  gen:i    -- the i-th general parameter;
  -  A:i      -- the i-th item of the A atom type block;
  -  b%AB:i   -- the i-th item of the A-B bonds block;
  -  o%AB:i   -- the i-th item of the A-B off-diagonal block;
  -  v%ABC:i  -- the i-th item of the A-B-C valence angle block;
  -  t%ABCD:i -- the i-th item of the A-B-C-D torsion angle block;
  -  h%XHY:i  -- the i-th item of the X-H-Y hydrogen bond block.

The index part of the key (:i) may be omitted, in which case the whole block is considered. In order to match *wildcard* torsions (indicated by 0 in the ff file) a question mark "?" instead of the atom type may be used. Examples of valid keys::

  v%HPtH:1 - first parameter of the H-Pt-H valence angle block
  v%HPtH   - all parameters of the H-Pt-H valence angle block
  t%?CC?:4 - fourth parameter of the *-C-C-* torsion angle block

Note that some angles may have more than one optimal value (for example 90 and 180 degrees), in which case ReaxFF may have more than one block per key in a force-field file. For such a key, the number of entries may be larger than the number of scanned files. In the following example, the number of entries for a C-O-O-C torsion is larger than that for the C-O bond because twelve force-fields contain two C-O-O-C torsion angles each::

  $ rxffutil minmax b%CO:1 t%COOC:1
  Key                   N         min         max     average
  t%COOC:1             64     -2.0324      3.4682      0.8679
  b%CO:1               52     95.6228    197.3588    151.8473

One can see which files contain the given keys using the -vv verbosity option. There are three verbosity levels:

* *-v* -- log ff files as they are opened, read in and parsed;
* *-vv* -- as -v plus print a parameter value for each case of the found key together with the corresponding file and block index within the section;
* *-vvv* -- as -vv plus print a key-block_index pair for every block found when parsing ff files.

For example::

  $ rxffutil minmax -vv v%HPtH:1
  ... [snip] ...
  Key                   N         min         max     average
  Found v%HPtH:1               95.0000 in c:/adf2018.105/atomicdata/ForceFields/ReaxFF/CHONSFPtClNi.ff block 69
  Found v%HPtH:1               57.3916 in c:/adf2018.105/atomicdata/ForceFields/ReaxFF/PtCH.ff block 14
  v%HPtH:1              2     57.3916     95.0000     76.1958

pdist
-----

The **pdist** command can be used in addition to *minmax* to get a better idea about the parameter values distribution::

  rxffutil pdist [--ffdir=/path/to/ff/directory] [--npoints=int] key ...

Keys used with the pdist command are required to have a non-empty index part. That is, v%HPtH is not a valid key while v%HPtH:1 is. 

The number of points (bins) in the distribution is set by the - -npoints option (20 by default).

params
------

The **params** command can be used to prepare a params file used by ReaxFF for force-field fitting::

  rxffutil params [options] key ...

In additions to - -ffdir, the following options are available:

* *- -ff=/path/to/ffield* -- specify the ffield file for which the params file is to be created. If this option is omitted, the ffield file in he current directory is used. If there is no such file the program will quit.

* *- -delta=real* -- specify a value for the *delta* (or *sigma*) column of the :ref:`params file <params_file>` as a fraction of the corresponding min-max interval. The default value is 0.01.

* The min-max interval for each parameter is determined from parameter values (having the same key) found in the ffdir directory. This range is initially identical to the one printed by the minmax command but it can be modified using the following options:

  - *- -scalebound=real* -- change the parameter range by scaling both boundaries by the specified factor. The boundaries are scaled in such a way that the range is expanded scalebound is greater than 1, or reduced otherwise. In other words, a negative lower bound is multiplied by the factor, while a positive one is divided. Likewise, a positive upper bound is multiplied by the factor, while a negative one is divided by it. This way, the bounds do not change their sign when extending or shrinking the parameter range (the scalebound must be positive);
  - *- -scalerange=real* may be specified when the - -scalebound option is not used (otherwise it is ignored). If this option is present then the initial range is multiplied by the given factor and the lower and upper bounds are shifted symmetrically. Using this option may change the sign of the parameter boundary, which may lead to undesired consequences;
  - if none of the above options is specified then the lower and upper bounds may be scaled independently using the *- -scalemin=real* and *- -scalemax=real* options. When using this option the range can be expanded or shrunk depending on the sign of the boundary value.

For example, to get a params file for optimization of the C-O-O-C torsion angle parameters from the CHO-2016 force-field using MCFFOptimizer one can use the following commands::

  $ cp $AMSRESOURCES/ForceFields/ReaxFF/CHO-2016.ff ./ffield
  $ rxffutil params --scalebound=1.2 t%COOC:1 t%COOC:2 t%COOC:3 t%COOC:4 t%COOC:5
  #     Key          delta         min         max     comment
     6  16   1    0.066007     -2.4389      4.1618     # t%COOC:1 V1
     6  16   2    1.168364    -20.8364     96.0000     # t%COOC:2 V2
     6  16   3    0.030000     -1.8000      1.2000     # t%COOC:3 V3
     6  16   4    0.061995     -8.2829     -2.0833     # t%COOC:4 p_tor1
     6  16   5    0.034717     -3.4800     -0.0083     # t%COOC:5 p_cot1

In this example, the range is expanded by scaling the lower and upper bounds by 20% outwards. Exercise: run this command with and without the - -scalebound option and compare min max values. 

When preparing a params file for the CMA-ES optimizer one should use the  - -delta option to specify a suitably large initial sigma (typically in the order of 0.1 -- 0.25).

.. Note:: 

  When optimizing valence and torsion angle parameters, care should be taken when selecting starting parameters for a parameters that are present more than once in the forcefield in question, e.g. the C-O-O-C torsion that has two optimal values in many force-fields. The average printed by the program is based on all entries so it will be somewhere in the middle between the optimal values, i.e. highly non-optimal.

.. Note:: 

  The fields in the output of the params command are sorted by the key (actually by its integer equivalent), while the output from the minmax command has an arbitrary order.

.. Note:: 

  When working on a real force-field fitting project one should not use the default ffdir value ($AMSRESOURCES/ForceFields/ReaxFF). Instead, one should copy related ff files from there to a separate folder and use it. By related files one should understand, for example, the ones corresponding to the same branch (combustion or water) and/or having the same kind of non-bonding parameters (shielding/no-shielding, inner-core/no-inner-core).

