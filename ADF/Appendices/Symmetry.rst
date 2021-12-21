.. index:: symmetry 
.. index:: Schönflies symbol 
.. index:: symmetry label 
.. index:: subspecies 
.. index:: irreducible representation 
.. index:: double group symmetry 

.. _SCHOENFLIES: 
.. _appendix symmetry:
.. _schonfliess symbols:

Symmetry
********

.. note::

  Starting from the 2020 release, ADF does not automatically symmetrize and re-orient the molecule.
  If your molecule is symmetric and you want to make sure that the highest possible symmetry is used, you should either

  * Symmetrize your molecule in AMSinput using the symmetrize button |symmetrize|

  * Use the **System%Symmetrize** option in the `AMS driver <../../AMS/System.html>`__


Schönfliess symbols and symmetry labels
========================================


A survey of all point groups that are recognized by ADF is given below. The table contains the Schönfliess symbols together with the names of the subspecies of the irreducible representations as they are used internally by ADF. The subspecies names depend on whether single-group or double-group symmetry is used. Double-group symmetry is used only in relativistic spin-orbit calculations. 

Note that for some input of TDDFT (Response) calculations, other conventions apply for the subspecies, see below.

.. csv-table:: Schönfliess symbols and the labels of the irreducible representations.
   :widths: 50,120,200,200

   **Point**,**Schönfliess**,**Irreducible representations**,**Irreducible representations**
   **Group**,**Symbol in ADF**,**in single-group symmetry**,**in double-group symmetry**
   C\ :sub:`1` ,NOSYM,A,A1/2
   R\ :sup:`3` ,ATOM,s p d f,s1/2 p1/2 p3/2 d3/2 d5/2 f5/2 f7/2
   T\ :sub:`d` ,T(D),A1 A2 E T1 T2,E1/2 U3/2 E5/2
   O\ :sub:`h` ,O(H),A1.g A2.g E.g T1.g T2.g,E1/2.g U3/2.g E5/2.g
               ,    ,A1.u A2.u E.u T1.u T2.u,E1/2.u U3/2.u E5/2.u
   C\ :sub:`∞v` ,C(LIN),Sigma Pi Delta Phi,J1/2 J3/2 J5/2 J7/2
   D\ :sub:`∞h` ,D(LIN),Sigma.g Sigma.u Pi.g Pi.u  ,J1/2.g J1/2.u J3/2.g J3/2.u
                ,      ,Delta.g Delta.u Phi.g Phi.u,J5/2.g J5/2.u J7/2.g J7/2.u
   C\ :sub:`i` ,C(I),A.g A.u,A1/2.g A1/2.u
   C\ :sub:`s` ,C(S),AA AAA,A1/2 A1/2*
   C\ :sub:`n` ,"C(N), n must be 2",A B,A1/2 A1/2*
   C\ :sub:`nh` ,"C(NH), n must be 2",A.g B.g A.u B.u,A1/2.g A1/2.g* A1/2.u A1/2.u*
   C\ :sub:`nv` ,"C(NV), n<9",A1 A2 B1 B2 E1 E2 E3 ...,E1/2 E3/2 E5/2 ...
                ,            ,odd n: without B1 and B2,odd n also: An/2 An/2*
   D\ :sub:`n` ,"D(N), n<9",n=2: A B1 B2 B3                ,E1/2 E3/2 ...
               ,           ,other: A1 A2 B1 B2 E1 E2 E3 ...,
               ,           ,odd n: without B1 B2           ,odd n also: An/2 An/2*
   D\ :sub:`nh` ,"D(NH), n<9",n=2: A.g B1.g B2.g B3.g A.u B1.u B2.u B3.u,even n: E1/2.g E1/2.u
                ,            ,other: A1.g A2.g B1.g B2.g E1.g, E3/2.g E3/2.u ...
                ,            ,E2.g E3.g ... A1.u A2.u B1.u ...,
                ,            ,odd n: AA1 AA2 EE1 EE2 ...,odd n: E1/2 E3/2 E5/2 ...
                ,            ,AAA1 AAA2 EEE1 EEE2 ....,
   D\ :sub:`nd` ,"D(ND), n<9",even n: A1 A2 B1 B2 E1 ...               ,even n: E1/2 E3/2 ...
                ,            ,odd n: A1.g A2.g E1.g E2.g ... E(n-1)/2.g,odd n: E1/2.g E1/2.u E3/2.g E3/2.u ...
                ,            ,A1.u A2.u     E1.u E2.u ... E(n-1)/2.u   ,An/2.g An/2.u An/2.g* An/2.u*
   
   
Most labels are easily associated with the notation usually encountered in literature. Exceptions are AA, AAA, EE1, EEE1, EE2, EEE2, etcetera. They stand for A', A'', E1', E1'', and so on. The AA, etc. notation is used in ADF to avoid using quotes in input files in case the subspecies names must be referred to. 

The symmetry labeling of orbitals may depend on the choice of coordinate system. For instance, B1 and B2 representations in C\ :sub:`nv`  are interchanged when you rotate the system by 90 degrees around the z-axis so that x-axis becomes y-axis and vice-versa (apart from sign). 

Labels of the symmetry subspecies are easily derived from those for the irreps. For one-dimensional representations they are identical, for more-dimensional representations a suffix is added, separated by a colon: For the two- and three-dimensional E and T representations the subspecies labels are obtained by adding simply a counting index (1, 2, 3) to the name, with a colon in between; for instance, the EE1 irrep in the Dnh pointgroup has EE1:1 and EE1:2 subspecies. The same holds for the two-dimensional representations of C\ :sub:`∞v`  and D\ :sub:`∞h` . For the R3 (atom) point group symmetry the subspecies are p:x, p:y, p:z, d:z2, d:x2-y2, etc. 

All subspecies labels are listed in the Symmetry section, very early in the ADF output. To get this, perform a quick run of the molecule using the STOPAFTER key (for instance: stopafter config). 


TDDFT irrep labels
------------------

The printed symmetry in the output in TDDFT calculations is actually the symmetry of transition density. For closed-shell systems, the symmetry of the excited state is the same as the symmetry of the transition density, while for open-shell systems, the symmetry of the excited states is the direct product between the symmetry of the transition density and the ground state symmetry. Note that the ground state symmetry of an open shell molecule is not necessarily A1.

The TDDFT module uses a different notation for some irrep names, for example, A' is used instead of AA, A'' (A two apostrophes) instead of AAA, A1' instead of AA1, A2'' instead of AAA2.
In case of atoms, one should use a subgroup. In case of linear systems, if one does not specify the symmetry ADF will lower the symmetry automatically. For C(LIN) ADF will use internally C(7V), however, the names of the irreps in the TDDFT output will be S+, S-, Pi, De, Phi, instead of A1, A2, E1, E2, E3, respectively. 
For D(LIN) ADF will use internally D(7D), however, the names of the irreps in the TDDFT output will be S+.g, S-.g, Pi.g, De.g, Ph.g, S-.u, S+.u, Pi.u, De.u, Ph.u, instead of A1.g, A2.g, E1.g, E2.g, E3.g, A1.u, A2.u, E1.u, E2.u, E3.u, respectively.


.. csv-table:: Schönfliess symbols and the labels of the irreducible representations for TDDFT.
   :widths: 50,120,300

   **Point**,**Schönfliess**,**Irreducible representations**
   **Group**,**Symbol in ADF**,
   C\ :sub:`1` ,NOSYM,A
   T\ :sub:`d` ,T(D),A1 A2 E T1 T2
   O\ :sub:`h` ,O(H),A1.g A1.u A2.g A2.u E.g E.u T1.g T1.u T2.g T2.u
   C\ :sub:`∞v` ,C(LIN),S+ S- Pi De Ph
   D\ :sub:`∞h` ,D(LIN),S+.g S-.g Pi.g De.g Ph.g S-.u S+.u Pi.u De.u Ph.u
   C\ :sub:`i` ,C(I),A.g A.u
   C\ :sub:`s` ,C(S),A' A''
   C\ :sub:`n` ,"C(N), n must be 2",A B
   C\ :sub:`nh` ,"C(NH), n must be 2",A.g B.g A.u B.u
   C\ :sub:`nv` ,"C(NV), n<9",n=2: A1 A2 B1 B2
                ,            ,n=3: A1 A2 E
                ,            ,n=4: A1 A2 B1 B2 E
                ,            ,even n: A1 A2 B1 B2 E1 E2 ...
                ,            ,odd n: A1 A2 E1 E2 ...
   D\ :sub:`n` ,"D(N), n<9",n=2: A B1 B2 B3                
               ,           ,n=3: A1 A2 E
               ,           ,n=4: A1 A2 B1 B2 E
               ,           ,even n: A1 A2 B1 B2 E1 E2 ...
               ,           ,odd n: A1 A2 E1 E2 ...
   D\ :sub:`nh` ,"D(NH), n<9",n=2: A.g A.u B1.g B1.u B2.g B2.u B3.g B3.u
                ,            ,n=4: A1.g A1.u A2.g A2.u B1.g B1.u B2.g B2.u B3.g B3.u E.g E.u
                ,            ,even n: A1.g A1.u A2.g A2.u B1.g B1.u B2.g B2.u B3.g B3.u E1.g E1.u E2.g E2.u ...
                ,            ,n=3: A1' A1'' A2' A2'' E' E''
                ,            ,odd n: A1' A1'' A2' A2'' E1' E1'' E2' E2'' ...
   D\ :sub:`nd` ,"D(ND), n<9",n=2: A1 A2 B1 B2 E
                ,            ,even n: A1 A2 B1 B2 E1 E2 ...
                ,            ,n=3: A1.g A1.u A2.g A2.u E.g E.u
                ,            ,odd n: A1.g A1.u A2.g A2.u E1.g E1.u E2.g E2.u ...
   


Molecular orientation requirements
==================================

ADF requires that the molecule has a specific orientation in space, as follows: 

+ The origin is a fixed point of the symmetry group.

+ The z-axis is the main rotation axis, xy is the :math:`\sigma`\ :sub:`h` -plane (axial groups, C(s)).

+ The x-axis is a C\ :sub:`2`  axis (D symmetries).

+ The xz-plane is a :math:`\sigma`\ :sub:`v` -plane (C\ :sub:`nv`  symmetries).

+ In T\ :sub:`d`  and O\ :sub:`h`  the z-axis is a fourfold axis (S\ :sub:`4`  and C\ :sub:`4` , respectively) and the (111)-direction is a threefold axis.

If the user-specified symmetry equals the true symmetry of the nuclear frame (including electric field and point charges) the program will adapt the input coordinates to the above requirements, if necessary. If no symmetry has been specified at all ADF assumes you have specified the symmetry of the nuclear frame, accounting for any fields. If a subgroup has been specified for the molecular symmetry the input coordinates will be used as specified by the user. If a Z-matrix input is given this implies for the Cartesian coordinates: first atom in the origin, second atom on the positive x-axis, third atom in the xy-plane with positive y value. 


.. |symmetrize| image:: ../../shared/gui_icons/SymmTool.png
   :width: 19
   :height: 20
