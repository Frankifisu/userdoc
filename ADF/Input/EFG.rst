.. index:: EFG 
.. index:: electric field gradient 
.. index:: NQCC 
.. index:: Q-tensor 
.. index:: Mossbauer quadrupole splittings 
.. _EFG: 

.. _keyscheme QTENS: 

Nuclear Quadrupole Interaction (EFG)
************************************

::

   QTENS

This key activates the computation of the Nuclear Electric Quadrupole Hyperfine interaction. It can be applied to open-shell and to closed-shell systems. QTENS gives you the Nuclear Electric Quadrupole Hyperfine interaction (Q-tensor) [#ref1]_. The latter is directly related to the Electric Field Gradient (EFG) . The Q-tensor elements (in MHz) equal the the electric field gradient tensor elements (in a.u.) times 234.9647 times the nuclear quadrupole moment (NQM in barn units, 1 barn = 10-28m\ :sup:`2`  = 10-24cm\ :sup:`2` ) and divided by 2I(2I-1), where I is the nuclear spin. The Nuclear Quadrupole Coupling Constant (NQCC) (in MHz) is the largest value of the principal values of the EFG (in a.u.) times 234.9647 times the nuclear quadrupole moment (in barn units). The electric field gradient tensor is printed next to the Q-tensor. 

In the case of ZORA the program will calculate the EFG in the so called ZORA-4 approximation,  which includes a small component density ("picture-change correction"), see  [#ref1]_.
If you also want to calculate the EFG using the ZORA density, thus in the Foldy-Wouthuysen picture, include the keywords:

::

    PRINT FWPICTURE

In case QTENS is used for \ :sup:`57` Fe, \ :sup:`119` Sn, \ :sup:`125` Te, \ :sup:`193` Ir, and \ :sup:`197` Au, quadrupole splittings are written in units of mm/s, used in Mössbauer spectroscopy. 

**Analysis of the EFG**

With the EFG keyword in AOResponse a Mulliken type analysis of the EFG principal components, and an analysis in terms of canonical MOs, can be performed. Required is symmetry NOSYM. This not implemented in case of spin-orbit coupling. For an NBO analysis of the EFG, see the  :ref:`section on NBO analysis<NBO_PROPERTIES>`. For an explanation of the output and a general usage tutorial, see [#ref3]_. Further references and recommended citations, see [#ref4]_. 

::

   Symmetry NOSYM
   Aoresponse
    efg NUC
   end

``efg NUC``
   Here NUC is the number of the nucleus at which the EFG is to be computed (ADF internal atom ordering).  Availiable for one nucleus at the time. 

.. only:: html

  .. rubric:: References

.. [#ref1] E.\  van Lenthe and E.J. Baerends, *Density functional calculations of nuclear quadrupole coupling constants in the zero-order regular approximation for relativistic effects*, `Journal of Chemical Physics 112, 8279 (2000) <https://doi.org/10.1063/1.481433>`__ 

.. [#ref3] J.\  Autschbach, S. Zheng, and R.W. Schurko, *Analysis of Electric Field Gradient Tensors at Quadrupolar Nuclei in Common Structural Motifs*, `Concepts in Magnetic Resonance Part A 36A, 84 (2010) <https://doi.org/10.1002/cmr.a.20155>`__ 

.. [#ref4] A.J. Rossini, R.W. Mills, G.A. Briscoe, E.L. Norton, S.J. Geier, I. Hung, S. Zheng, J. Autschbach, and R.W. Schurko, *Solid-State Chlorine NMR of Group IV Transition Metal Organometallic Complexes*, `Journal of the American Chemical Society 131, 3317 (2009) <https://doi.org/10.1021/ja808390a>`__ 
