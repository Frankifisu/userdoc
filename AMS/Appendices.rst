Appendices
##########

.. _ExtendedXYZ:
.. index:: XYZ file format

Extended XYZ file format
========================

The ``.xyz`` file format is a simple text based format for molecular geometries.
``.xyz`` files have the number of atoms in the first line, followed by a comment
line, followed by one line per atom, specifying the element as well as the x, y,
and z coordinates of this atom.

However, the standard ``.xyz`` file format does not include lattice vectors. AMS
therefore uses an extended ``.xyz`` file format which is also suitable for
periodic systems. In this extended format the lattice vectors are specified at
the end of the ``.xyz`` file via the keys ``VEC1``, ``VEC2`` and ``VEC3``. For
1D periodic systems (chains) only ``VEC1`` is needed. For 2D periodic systems
(slabs) only ``VEC1`` and ``VEC2`` are needed. An example extended ``.xyz`` for
graphene looks like this::

   2

   C     0.0   0.0      0.0
   C     1.23  0.71014  0.0
   VEC1  2.46  0.0      0.0
   VEC2  1.23  2.13042  0.0

Note that the extended ``.xyz`` format is also understood by the AMS GUI for
importing and exporting geometries from/to ``.xyz`` files.


.. index:: Developer options

Developer options
=================

.. scmautodoc:: ams Print Timers

.. scmautodoc:: ams EngineDebugging

.. index:: Symmetry 
.. index:: Schönflies symbol 
.. index:: Symmetry label 
.. index:: Subspecies 
.. index:: Irreducible representation 
.. index:: Double group symmetry 

.. _appendix symmetry:

Symmetry
========

.. _SCHOENFLIES: 

Schönfliess symbols and symmetry labels
****************************************

A survey of all molecular point groups that are recognized by AMS is given below. The table contains the Schönfliess symbols together with the names of the subspecies of the irreducible representations as they are used by AMS to label normal modes.

.. csv-table:: Schönfliess symbols and the labels of the irreducible representations.
   :widths: 50,120,400

   **Point**,**Schönfliess**,**Irreducible representations**
   **Group**,**Symbol in AMS**,
   C\ :sub:`1` ,NOSYM,A
   C\ :sub:`∞v` ,C(LIN),Sigma Pi
   D\ :sub:`∞h` ,D(LIN),Sigma.g Sigma.u Pi.g Pi.u
   I            ,I    ,A T1 T2 G H
   I\ :sub:`h`  ,I(H) ,A.g A.u T1.g T1.u T2.g T2.u G.g G.u H.g H.u
   O            ,O    ,A1 A2 E T1 T2
   O\ :sub:`h`  ,O(H) ,A1.g A1.u A2.g A2.u E.g E.u T1.g T1.u T2.g T2.u
   T            ,T    ,A E T
   T\ :sub:`h`  ,T(H) ,A.g A.u E.g E.u T.g T.u
   T\ :sub:`d`  ,T(D) ,A1 A2 E T1 T2
   C\ :sub:`i`  ,C(I) ,A.g A.u
   S\ :sub:`n`  ,S(N) ,n=4: A B E
                ,     ,n=6: A.g A.u E.g E.u
                ,     ,n=8: A B E1 E2 E3
   C\ :sub:`n`  ,C(N) ,n=2: A B
                ,     ,n=4: A B E
                ,     ,even n: A B E1 E2 ...
                ,     ,n=3: A E
                ,     ,odd n: A E1 E2 ...
   C\ :sub:`nv` ,C(NV),n=2: A1 A2 B1 B2
                ,     ,n=4: A1 A2 B1 B2 E
                ,     ,even n: A1 A2 B1 B2 E1 E2 ...
                ,     ,n=3: A1 A2 E
                ,     ,odd n: A1 A2 E1 E2 ...
   C\ :sub:`s`  ,C(S) ,A' A''
   C\ :sub:`nh` ,C(NH),n=2: A.g A.u B.g B.u
                ,     ,n=4: A.g A.u B.g B.u E.g E.u
                ,     ,even n: A.g A.u B.g B.u E1.g E1.u E2.g E2.u ...
                ,     ,n=3: A' A'' E' E''
                ,     ,odd n: A' A'' E1' E1'' E2' E2'' ...
   D\ :sub:`n`  ,D(N) ,n=2: A B1 B2 B3
                ,     ,n=4: A1 A2 B1 B2 E
                ,     ,even n A1 A2 B1 B2 E1 E2 ...
                ,     ,n=3: A1 A2 E
                ,     ,odd n: A1 A2 E1 E2 ...
   D\ :sub:`nd` ,D(ND),n=2: A1 A2 B1 B2 E
                ,     ,even n: A1 A2 B1 B2 E1 E2 ...
                ,     ,n=3: A1.g A1.u A2.g A2.u E.g E.u
                ,     ,odd n: A1.g A1.u A2.g A2.u E1.g E1.u E2.g E2.u ...
   D\ :sub:`nh` ,D(NH),n=2: A.g A.u B1.g B1.u B2.g B2.u B3.g B3.u
                ,     ,n=4: A.g A.u B1.g B1.u B2.g B2.u B3.g B3.u E.g E.u
                ,     ,even n: A.g A.u B1.g B1.u B2.g B2.u B3.g B3.u E1.g E1.u E2.g E2.u ...
                ,     ,n=3: A1' A1'' A2' A2'' E' E''
                ,     ,odd n: A1' A1'' A2' A2'' E1' E1'' E2' E2'' ...
   
The symmetry labeling may depend on the choice of coordinate system. For instance, B1 and B2 representations in C\ :sub:`nv`  are interchanged when you rotate the system by 90 degrees around the z-axis so that x-axis becomes y-axis and vice-versa (apart from sign). 

.. _orientation requirements:

Molecular orientation requirements
**********************************

In order that AMS recognizes the (sub)symmetry of a molecule, the molecule has to have a specific orientation in space.

+ The origin is a fixed point of the symmetry group.

+ The z-axis is the main rotation axis.

+ xy is the :math:`\sigma`\ :sub:`h` -plane (axial groups, C(s)).

+ The x-axis is a C\ :sub:`2`  axis (D symmetries).

+ The xz-plane is a :math:`\sigma`\ :sub:`v` -plane (C\ :sub:`nv`  symmetries).

+ In T\ :sub:`d`  and O\ :sub:`h`  the z-axis is a fourfold axis (S\ :sub:`4`  and C\ :sub:`4` , respectively) and the (111)-direction is a threefold axis.

If the system is symmetrized (and no symmetry is given in the System block key) the molecular structure is rotranslated into this standard orientation.
