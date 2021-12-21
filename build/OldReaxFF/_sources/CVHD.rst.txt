.. _cvhd:

CVHD: Collective Variable-Driven Hyperdynamics
**********************************************

.. tip::
  See also the advanced `cvhd tutorial <../Tutorials/MolecularDynamicsAndMonteCarlo/CVHD.html>`__ .

The CVHD implementation in Reaxff follows the algorithm described in `K.M. Bal, E.C. Neyts, JCTC, 11 (2015) <https://doi.org/10.1021/acs.jctc.5b00597>`__

Currently only the bond-breaking collective variable is implemented. The CVHD takes a cvhd.in file as the only additional input. The file describes both the hyperdynamics and the collective variables and it has the following format:

::

   # Comments may be present, starting with a hash sign.
   # CVHD bias potential parameters
   startIter   freqIter    waitIter   gaussHeight    gaussHalfWidth  [wellTemperedT]
   # Bond collective variable components (one per line, up to 10)
   type   AtomName1   AtomName2   rmin  rmax  BOcutoff  pExponent
   [type   AtomName1   AtomName2   rmin  rmax  BOcutoff]

The bias potential parameters are: startIter - the first iteration at which the bias potential is deposited, freqIter - bias potential deposition rate in steps, waitIter - number of steps to wait before removing the bias after CV becomes equal to 1, gaussHeight - height of a single gaussian deposited at a time in kcal/mol, gaussHalfWidth - gaussian delta of the deposited bias, wellTemperedT - the bias temperature as defined in [PhysRevLett 100, 020603 (2008)] (optional, the full bias is applied if wellTemperedT is absent).

The bond-breaking CV parameters: type = bond, AtomName1 and AtomName2 - atom names specified in the second atom name entry (the one after the coordinates) in the BGF-type geo file, which may be different from the element name specified before the coordinates; rmin and rmax - rmin and rmax from Eq 5 in the paper above, BOcutoff - bond order cutoff, bonds with BO below this value are not considered even of the bond distance is within the (rmin,rmax) interval; pExponent - corresponds to p in Eq 3 in the paper. The same pExponent value is used for all bond types but the rmin, rmax, and BOcutoff may (and should) be different.

An example cvhd.in file that one could use to reproduce the NVT pyrolysis modeling results from `this paper <https://doi.org/10.1039/c6sc00498a>`__ is given below:

::

  # CVHD bias potential parameters
  # startIter   freqIter    waitIter   gaussHeight    gaussHalfWidth
      10000       2000       10000        0.250           0.025
  # Bond-breaking collective variable
  # type  AtomName1   AtomName2     rmin  rmax   BOcutoff  pExponent
     bond     C           H         1.05   1.65    0.5         6
     bond     C           C         1.55   2.2     0.5

