.. index:: K-Space
.. index:: Reciprocal Space
.. index:: Brillouin zone (BZ)

.. _k-space:

K-Space
=======

The K-Space sampling (i.e., the k-points used to sample the Brillouin Zone) is an important technical aspect of Band, as it influences heavily the accuracy, the CPU time and the memory usage of the calculation (see section :ref:`k-space recommendations`).

KSpace input block
------------------

The K-Space can be controlled via the ``KSpace`` input block. Two different k-space integration methods are available: the *Regular Grid* (**default**) and the *Symmetric Grid*.

.. scmautodoc:: band KSpace Type Quality 


Regular K-Space grid
^^^^^^^^^^^^^^^^^^^^

By default, Band will look at the size of a lattice vectors and the KSpace quality to determine the number of k-points. The larger the lattice vector in real space, the smaller the reciprocal space vectors are, and as a result fewer k-points are needed. The following intervals will be distinguished: 0-5 Bohr, 5-10 Bohr, 10-20 Bohr, 20-50 Bohr, and beyond. Here is the table explaining how many k-points will be used along a lattice vector. 

.. csv-table:: 

   Lattice vector length,Basic,Normal,Good,VeryGood,Excellent
   0-5 Bohr,5,9,13,17,21
   5-10 Bohr,3,5,9,13,17
   10-20 Bohr,1,3,5,9,13
   20-50 Bohr,1,1,3,5,9
   50- Bohr...,1,1,1,3,5
   
By preferring odd-numbered values we can use a quadratic interpolation method, and have the :math:`\Gamma` point in the grid. It is then reasonable to assume a decaying error when going to a better quality setting.

It is also possible to manually specify the number of k-space points along each reciprocal lattice vector

.. scmautodoc:: band KSpace Regular
   :noref:


Symmetric K-Space grid (tetrahedron method)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The tetrahedron method can be useful when high symmetry points in the BZ are needed to capture the correct physics of the system, graphene being a notable example.

The number of k-points in the symmetric grid depends on the KSpace quality and on the length of the shortest lattice vector. 

It is also possible to manually specify the symmetric k-space integration parameter:

.. scmautodoc:: band KSpace Symmetric
   :noref:


**General Remark**: The tetrahedron method samples the irreducible wedge of the first BZ, whereas the regular grid samples the whole, first BZ. As a rule of thumb you need to choose roughly twice the value for the regular grid. For example kspace 2 compares to grid 4 4 4, kspace 3 to grid 5 5 5, etc.. Sticking to this rule the number of unique k-points will be roughly similar.

.. _k-space recommendations:

Recommendations for k-space
---------------------------

Which K-Space quality to use depends very much a) the system you are studying and b) the property you are interested in. 
We strongly recommend you to test the effect of different K-Space qualities on your system and properties of interest.

As an example, in the following table we list the errors on formation energy and band gap for diamond using regular k-space grids of different qualities (using Excellent kSpace quality as reference).

.. csv-table:: Accuracy of formation energy for diamond (primitive unit cell) using different KSpace grids
   :header: KSpace quality, Energy error / atom [eV], CPU time ratio 

   Gamma-Only, 3.3, 1
   Basic, 0.6, 2
   Normal, 0.03, 6
   Good, 0.002, 16
   VeryGood, 0.0001, 35
   Excellent, reference, 64

It is worthwhile noting that the errors due to finite k-space sampling in formation energies are to some extend systematic, and they partially cancel each other out when taking energy differences.

In general, metals (or narrow-gap semiconductor) require higher K-Space sampling than insulators.
For insulators and wide-gap semiconductors, Normal K-Space quality often suffices.
For Narrow-gap semiconductor and metals, Good K-Space quality is highly recommended. 
For geometry optimizations under pressure, Good K-Space quality is recommended.


Furthermore for certain properties, such as band gaps, Normal K-Space quality might not be enough to obtain reliable results. For example, in following figure we see how Normal K-Space quality is often not enough for computing band gaps (especially for the narrow-gap semiconductor of the top panel). For band gap prediction, it is recommended to use Good K-Space quality.

.. figure:: /Images/band_gaps_k-space_jetsa.png

   Convergence of band gaps WRT the k-space quality set for various system. (XC:PBE, Basis:TZP)




