.. index:: Band Structure
.. index:: Fat Bands

.. _BandStructure:

Band Structure
==============

BAND can calculate the band structure for the standard k-path in the Brillouin zone [#ref1]_ and saves the corresponding data to the binary file RUNKF.

The band structure is best examined with the GUI module **BandStructure** see: 

+ Advanced BAND tutorial: `Calculation of Band Structure and COOP of CsPbBr3 with BAND <../../Tutorials/Analysis/BandsAndCOOP.html>`_

.. scmautodoc:: band BandStructure Enabled Automatic DeltaK FatBands UseSymmetry EnergyAboveFermi EnergyBelowFermi


Information on the k-path used for band structure plotting (including the fractional coordinates of high-symmetry k-points) can be found in the section ``KPath`` of the output file.

User-defined path in the Brillouin zone
---------------------------------------

If ``BZStruct%Automatic`` is ``False``, BAND will compute the band structure for the user-defined path in the ``BZPath`` block. 

.. scmautodoc:: band BZPath

You should define the vertices of your path in fractional coordinates (wrt the reciprocal lattice vectors) in the ``Path`` sub-block. 
If you want to make a *jump* in your path, you need to specify a new ``Path`` sub-block.

In the following example we define the path ``Gamma-X-W-K|U-X`` for a FCC lattice::

   BZPath
      Path
         0.000   0.000   0.000 
         0.500   0.000   0.500
         0.500   0.250   0.750 
         0.375   0.375   0.750
      End
      Path 
         0.625   0.250   0.625 
         0.500   0.000   0.500 
      End
   End


Definition of the Fat Bands
---------------------------

The :ref:`fat bands <band-key-BandStructure>` :math:`F_{i,n,\sigma,\vec{k}}` are the periodic equivalent of the Mulliken population. They are defined as:

.. math::
   
   F_{i,n,\sigma,\vec{k}} = \sum_j C_{i,n,\sigma,\vec{k}} C_{j,n,\sigma,\vec{k}} S_{i,j,\vec{k}} 

where :math:`C_{i,n,\sigma,\vec{k}}` and  :math:`S_{i,j,\vec{k}}` are the orbital coefficients and the overlap matrix elements respectively. 
The indices :math:`i` and :math:`j` denote basis functions, :math:`n` is the band index, :math:`\sigma` is the spin index 
and :math:`\vec{k}` is a reciprocal vector in the Brillouin zone.

.. index:: Band Gap

Band Gap
--------

The band gap (if any) is printed in the output. Here is an example for the NaCl crystal::

   ----------------------------------------
   Band gap information
   ----------------------------------------
   Number of valence electrons                    16
   Valence Band index                              8
   Top of valence Band (a.u.)                 -0.192
   Bottom of conduction Band (a.u.)           -0.039
   Band gap (a.u.)                             0.153
   Band gap (eV)                               4.173
   Band gap (kcal)                            96.235


.. only:: html

  .. rubric:: References

.. [#ref1] W.\  Setyawan and S. Curtarolo, *High-throughput electronic band structure calculations: Challenges and tools*, `Computational Materials Science 49 (2010) 299–312 <https://doi.org/10.1016/j.commatsci.2010.05.010>`__.
