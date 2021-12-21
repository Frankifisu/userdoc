.. index:: Fragments

.. _fragments:

Fragments
=========

A fragment feature is available albeit rather primitive. It allows for the analysis of the DOS in a fragment basis and for the calculation of the deformation density with respect to fragment densities. A typical application is the periodical adsorption of one or more molecules on a surface. For instance, consider periodic adsorption of hydrogen molecules over a surface. First you calculate the free molecule in the same orientation as when adsorbed to the substrate. Since you would like to use a molecular fragment, it makes sense to put the molecules far apart (large lattice spacing) and force dispersion to be neglected (KSPACE 1). To use the fragment in the next run you need to rename the result file ("rkf"), to something like "frag.rkf", see the example script discussed below or the :ref:`example <example Frags_COCu>` covering this topic. 

.. scmautodoc:: band Fragment

Example:

::

   Fragment
     filename test.rkf
     AtomMapping
       1 3 !  atom 1 of this fragment is assigned to third atom
       2 4 !  atom 2 of this fragment is assigned to fourth atom
     End
     Labels
       Sigma
       Sigma*
       Pi_x
       Pi_y
       Pi_x*
       Pi_y*
     End
   End

In this example the first six fragment orbitals will be labeled as stated in the body of this key. The remaining orbitals are labeled by the default labeling system (e.g. 1/FO/5, etc.). The labels are used in combination with options like ``Print Eigens`` and ``Print OrbPop``. (See also ``Print OrbLabels``). This key can be given once for each fragment. 

.. Tip::
  
  Specifying::
  
     Print Eigens
  
  for a calculation produces output concerning the eigen states, thereby providing a means to identify the eigen states (e.g. to be   sigma, pi, et cetera). So, one can label the orbitals of a fragment according to this information.
