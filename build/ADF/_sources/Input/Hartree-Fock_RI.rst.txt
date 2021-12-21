.. _hartree-fock_RI:

.. _RIHARTREEFOCK:

Hartree-Fock RI scheme
----------------------

The implementation in ADF of the calculation of exact exchange (**Hartree Fock exchange**), which is needed for the hybrid functionals, is based on work by Watson et al., Ref. [#ref1]_. This procedure is generally referred to as **resolution of the identity** (abbreviated as **RI**). It employs an auxiliary set of functions (**fit functions**) to efficiently approximate the Hartree Fock exchange matrix.

.. _keyscheme RIHARTREEFOCK:

Technical aspects of the RI scheme can be tweaked in the ``RIHartreeFock`` key block::

  RIHartreeFock
    UseMe               {True|False}
    Quality             {Auto|Basic|Normal|Good|Verygood}
    FitSetQuality       {VeryBasic|Basic|Normal|Good|VeryGood}
    DependencyThreshold rVal
    QualityPerRegion
       Region myregion
       Quality {VeryBasic|Basic|Normal|Good|VeryGood}
    End
  End


``UseMe``
   **Default: True**. Set to False if you want to use the old RI scheme. 

``Quality``
  **Default: Auto**. Set the quality of the **FitSet** and of other RI specific technical procedures, including numerical integration and linear scaling parameters. If ``Auto``, the quality defined in :ref:`NumericalQuality <keyscheme NUMERICALQUALITY>` will be used.

``FitSetQuality``
  The quality of auxiliary fit set employed in the RI scheme (If both ``RIHartreeFock%Quality`` and ``RIHartreeFock%FitSetQuality`` are specified, the value specified in ``RIHartreeFock%FitSetQuality`` will be used). ``Normal`` quality is generally sufficient for basis sets up to and including TZ2P. Numerical issues have been found, especially if the molecule has symmetry NOSYM and a basis set larger than TZ2P is used. For larger basis sets (or for benchmarking purposes) a ``Good`` or ``VeryGood`` fit set is recommended. For larger basis sets than TZ2P it is recommended to include the DEPENDENCY key with a larger than default criterion for the basis set dependence, namely bas=5e-4.  **Note that the FitSetQuality heavily influences the computational cost of the calculation.** 

``DependencyThreshold``
  **Default: 1.0E-3**. To improve numerical stability, almost linearly-dependent combination of basis functions are removed from the Hartree-Fock exchange matrix. If you obtain unphysically large bond energy in an Hybrid calculation, you might try setting the DependencyThreshold to a larger value (*e.g.* 3.0E-3).

``QualityPerRegion``
   One can overwrite the fit set quality (``FitSetQuality``) for atoms in a particular region. :ref:`example Multiresolution_H2O` illustrates how to use this option.

In ADF2019.3 the fit set for quality GOOD has been improved by adding more diffuse l=0 fit functions to the fit set.

.. note::

  * In ADF2019.3 the fit set for ``FitSetQuality Good`` has been improved.
  * In ADF2017 and previous versions, a different implementation of the Hartree-Fock RI scheme was used by default. See :ref:`old_HartreeFock_RI_scheme`.


.. _old_HartreeFock_RI_scheme:

Old Hartree-Fock RI scheme
==========================

To use the old Hartree-Fock RI scheme one must specify::

  RIHartreeFock
    UseMe False
  End


In ADF2017 and previous versions, a different implementation of the Hartree-Fock RI scheme was used by default.

The old Hartree-Fock RI uses a smaller fit set than the default scheme, and does not include *H* and *I* fit functions; the new scheme should give to more accurate results, especially for f-block elements. 

**Memory usage**

Calculation of the Hartree-Fock exchange may require a lot of memory. Shared memory is used to buffer the necessary data used by all processes on a multi-processor node. By default, ADF will use 30% of the total physical memory of the computer for this buffer, which may be more than is desirable or possible. This amount, in megabytes, can be set using a HFMAXMEMORY input keyword. 

.. _keyscheme HFMAXMEMORY: 


::

   HFMaxMemory mbytes

The amount of memory used is related how many atoms can be done in a single pass. Thus, another way to limit the amount of memory used by ADF is to limit the number of atoms done per pass. The latter can be done using the HFATOMSPERPASS keyword. The safest, but also the slowest, is to set HFATOMSPERPASS to 1. 

.. _keyscheme HFATOMSPERPASS: 


::

   HFAtomsPerPass AtomsPerPass

If both HFMAXMEMORY and HFATOMSPERPASS are present, the value specified in HFATOMSPERPASS takes precedence. To debug memory usage in the Hartree-Fock routine, one can use a PRINT HARTREEFOCK keyword. 

**Numerical issues**

Numerical problems have been found with the present implementation of Hartree-Fock or (meta-)hybrids during the SCF, especially if the molecule has symmetry NOSYM and a basis set TZP or larger is used. Workaround is to use always the DEPENDENCY key with rather strict criteria for the basis set dependence, namely bas=4e-3. In ADF2010 these numerical problems have been reduced. The DEPENDENCY key is automatically switched on in the case of a Hartree-Fock or a (meta-)hybrid potential. The result of the DEPENDENCY key is that linear dependence of the basis set is reduced by removing linear combinations that correspond with eigenvalues in the virtual SFOs overlap matrix, which are smaller than, in this case, 4e-3. Note that this is a rather large value, such that it will have an effect on the bonding energy. For DZ and DZP basis sets this value will normally not result in reduction of the virtual space. However, for TZP, TZ2P, QZ4P and larger this will often result in reduction of the basis set, which will have an effect on the accuracy of the bonding energy. In these cases one could try a smaller value than 4e-3, but be aware that numerical problems may occur. If the molecule has symmetry the numerical problems are reduced.  

The origin of this problem is that for an accurate description of Hartree-Fock exchange one needs more (diffuse) fit functions in the fit procedure which is used in ADF, which uses only fit functions on the two centers of the two STOs. One can get more diffuse fit functions if one adds in the Create run of an atom the key: 

.. _keyscheme ADDDIFFUSEFIT: 


::

   AddDiffuseFit

If the BASIS key is used one can also add this key in the molecular calculation (the scripts in ADF will then automatically add this in the Create runs of the atoms). If one adds this key preliminary results indicate that one can lower the value for the dependency key to bas=1e-4. Such a low value for the dependency key normally means that the basis set is not reduced for basis sets of TZP or TZ2P quality. 

A different way to add fit functions that is useful for standard basis sets DZ, DZP, TZP, and TZ2P is to add the subkey 'Fittype QZ4P' in the BASIS key, thus: 

::

   BASIS
     Type ...
     Core ...
     FitType QZ4P
   End

In ADF2013 use is made of distance cut-offs for the calculation of the HF exchange integrals. This can reduce computation time and memory usage, especially for large molecules, however, this can also reduce the precision, which can lead to numerical problems. It is possible to set the distance cut-off threshold (starting from ADF2013.01b) for the calculation of the HF exchange integrals, A value of 99 for hffit virtually excludes the possibility that something will be neglected:  

::

   LINEARSCALING
     HF_FIT hffit
   END


**SCF problems**

However, for larger molecules and in case the molecule contains heavy elements (Z>36) one still should use rather strict criteria for the basis set dependence, such as bas=4e-3.  

In case of SCF problems that might be related to numerical issues one can try one or more of the following, that were discussed before 

::

   LINEARSCALING
     HF_FIT 99
   END
   Basis
    FitType QZ4P
   End
   AddDiffuseFit
   Dependency bas=5e-3


.. only:: html

  .. rubric:: References

.. [#ref1] M.A. Watson, N.C. Handy and A.J. Cohen, *Density functional calculations, using Slater basis sets, with exact exchange*, `Journal of Chemical Physics 119, 6475 (2003) <https://doi.org/10.1063/1.1604371>`__ 
