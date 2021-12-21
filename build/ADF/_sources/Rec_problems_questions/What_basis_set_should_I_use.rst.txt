.. _what basis set: 


What basis set should I use in ADF?
===================================

This question is hard to answer in general, but a few general suggestions can be made. 

.. note::
  This page discusses the basis set requirements for DFT calculations. For a discussion of this question for a GW calculations, see also the discussion in the :ref:`GW page input block <keyscheme GW>`. 


ZORA or non-relativistic calculation?
-------------------------------------

By default, :ref:`scalar relativistic effects with ZORA <RELATIVITY>` are included. 

If you are doing a ZORA calculation, you will need the ZORA basis sets which can be found in $AMSHOME/atomicdata/ADF/ZORA. You may also use the all electron basis sets from the ET or AUG directory, but be aware that these were optimized to non-relativistic calculations. Currently the ZORA basis sets cover the entire periodic table and besides all electron basis sets offer a choice of frozen cores. At present the ZORA directory does not contain basis sets with very diffuse functions, which may be required in calculations for hyperpolarizabilities or high-lying excitation energies, but for the lighter elements (H-Kr) you can certainly use the all-electron basis sets from the ET or AUG directory. Warning: in a ZORA calculation use only the frozen core basis sets coming from the $AMSHOME/atomicdata/ADF/ZORA directory, or use all electron basis sets. 

If you do not use ZORA, your basis sets should come from the directories SZ, DZ, DZP, TZP, TZ2P, or one of the ET or AUG basis sets. For many of the heavy elements only ZORA basis sets are available, but for such elements it would be inadvisable to do non-relativistic calculations anyway. For light elements the ZORA and normal basis sets should be identical except for the description of the frozen core. Usually the ZORA basis sets contain much steeper basis and fit functions to accurately describe the core region. 


Large or small molecule?
------------------------

For standard calculations (energies, geometries, etc.) we recommend the following hierarchy of basis sets: SZ < DZ < DZP < TZP < TZ2P < TZ2P+ < ET/ET-pVQZ < ZORA/QZ4P where the largest and most accurate basis is on the right.  Not all basis sets are available for all elements. For small negatively charged atoms or molecules, like :math:`\text{F}^-` or :math:`\text{OH}^-` , basis sets with extra diffuse functions are needed, like they are available in the AUG or ET/QZ3P-nDIFFUSE directories. For example, the standard basis sets, or even the large ZORA/QZ4P basis set will often not be large enough for the accurate calculation of such anions. 

In general it is advisable to use the best basis set that you can afford to use in terms of CPU time and memory. If you want to optimize the geometry or calculate the atomization energy of a diatomic molecule there is little reason not to use the very large ZORA/QZ4P basis, or (for light elements) a similarly large ET basis (we recommend the ET-pVQZ basis). If you are studying a molecule with 100 atoms or more, the use of such large basis sets does not only become prohibitive because of the required CPU time and memory, but it also is much less needed than for smaller systems. In medium-sized or large molecules even the moderately large basis sets will prove to be quite adequate because of the effect of basis set sharing. Each atom profits from the basis functions on its many neighbors. Additionally, if a large basis contains diffuse functions, linear dependency problems may occur. See also the input key DEPENDENCY. In many cases basis DZ or DZP will give acceptable accuracy for calculations on large systems. If you are inexperienced it may be prudent to test a few different basis sets to get a feel for the size of basis set effects. To get a rough idea for the size of various basis sets, we mention here the number of functions for all-electron basis sets from the directories ZORA/SZ up to ZORA/QZ4P. For carbon, the number of functions is 5 (basis ZORA/SZ), 10 (DZ), 15 (DZP), 19 (TZP), 26 (TZ2P), 43 (QZ4P). The same numbers for hydrogen are: 1 (SZ), 2 (DZ), 5 (DZP), 6 (TZP), 11(TZ2P, 21(QZ4P). These numbers arise because ADF uses 'pure' d and f functions. In other words, 5 instead of 6 d functions are used and 7 instead of 10 f functions. Note that especially the jump from TZ2P to QZ4P is quite steep. 

In an overgeneralizing fashion we can state that the single zeta basis SZ is hardly ever sufficient to get more than a qualitative picture and should be used only when larger basis sets are not affordable. The double zeta basis DZ performs already much better and may give quite reasonable results, for example in geometry optimizations on large molecules. However, in more subtle situations, for example if hydrogen bonds are important, it is advisable to use at least one set of polarization functions. This is the double zeta polarized DZP basis set. Basis set TZP extends the valence space (but not the core space which remains double zeta) to triple zeta. In basis TZ2P an additional polarization function is added. For example, hydrogen gets a d polarization function in addition to its p polarization function and carbon gets an f polarization function on top of a d polarization function. Several tests have shown that often the second polarization function is of more use when it has an l value one higher than the first polarization function. This is reflected in the choice just described. If another polarization function is needed it is usually best to add another one of the lowest l-value (2p+1d for hydrogen, 2d+1f for carbon). This choice has been made in the ET basis ET-QZ3P. There, sometimes even three d polarization functions were added, for example 3 p functions for Be, and 3 d functions for S. The reason for this is that S can occur in hypervalent species such as SF\ :sub:`6` , which put special demands on the basis set. In the case of Be, the unoccupied p level is so close in energy to the occupied ones that it is sometimes called a valence level. Semantics aside, it is clear that a proper description of the p level of Be is very important and it is therefore not strange to add a third p function. In general, the unoccupied levels for the atoms on the left side of the periodic table are close to the occupied ones. This makes it necessary to add a few extra functions for the lowest unoccupied levels in order to get a description which corresponds to the general level of accuracy one expects from the hierarchical basis set names SZ-TZ2P. The basis set quality for a particular subdirectory is now rather uniform throughout the periodic system. At the same time we have attempted to increase the number of functions in a systematic fashion so that each element is described by at least as many functions of a particular l value as its predecessor. 

The ZORA/QZ4P basis sets might be roughly described as core triple zeta, valence quadruple zeta, with 4 polarization functions (2 d and 2 f functions for C, 2 p and 2 d for H). The fit sets corresponding to these basis sets are also much larger than the fit sets found in basis sets SZ-TZ2P. If one has doubts about the adequacy of a fit set for a certain element, this can be tested by replacing its fit set by the large one from the QZ4P directory, see the subkey FitType of the key BASIS. In the ZORA/QZ4P basis sets, the choice for the exponents of the polarization functions was done in a systematic, but somewhat hand-waving manner. For this reason the exponents were always rounded to half integers. Also the geometric mean of the exponents usually does not coincide with the choices made in directories SZ-TZ2P and the ET basis sets. However, the fact that two polarization functions (with reasonable exponents) are present instead of a single one is far more important. A reasonable intermediate basis set, in size between TZ2P and QZ4P might be envisaged in which a single polarization function is added, as described above. This is roughly the choice for the polarization functions made in the ET directory ET-QZ3P. 


Frozen core or all-electron?
----------------------------

In general we recommend the use of frozen core basis sets if available (Exceptions are post-KS calculations like GW, RPA, MP2 or double hybrids. For these calculations, frozen cores should not be used). Especially for the heavier atoms the number of functions is much smaller than for their all-electron counterparts. Our tests indicate that the error made by invoking the frozen core approximation is usually clearly smaller than the difference with respect to slightly higher quality basis sets. For the ZORA/QZ4P basis sets, only all-electron basis sets are available as these are intended for near basis set limit calculations only in which the CPU time is not a major concern.  

Geometry optimizations involving atoms with a too large frozen core may give rise to numerical problems. In such cases it is recommendable to use a smaller frozen core. In previous occurrences we have removed such basis sets. 

For accurate results on properties like nuclear magnetic dipole hyperfine interactions (ESR), nuclear quadrupole coupling constants, and chemical shifts (NMR), all electron basis sets are needed on the interesting atoms. For such properties tight functions might be necessary for high accuracy, especially in a ZORA calculation. 


Diffuse functions needed?
-------------------------

For small negatively charged atoms or molecules, like :math:`\text{F}^-` or :math:`\text{OH}^-` , basis sets with extra diffuse functions are needed, like they are available in the AUG or ET/QZ3P-nDIFFUSE directories. For example, the standard basis sets, or even the large ZORA/QZ4P basis set will often not be large enough for the accurate calculation of such anions. 

For accurate results on properties like polarizabilities, hyperpolarizabilities, and high-lying excitation energies, also diffuse functions are needed. This is especially true for calculations on small molecules. In larger molecules the nature of the relevant virtuals is much more 'molecular', much less Rydberg-like, so that the normal basis sets may be sufficient. Basically all properties calculated through the RESPONSE keyword may require diffuse functions. If you use the EXCITATIONS keyword, the necessity of diffuse functions depends on the type of excitation you are interested in. The lowest excitations do not require diffuse functions, but Rydberg excitations do.  

In case of diffuse basis functions the risk of linear dependency in the basis increases. This can be checked, and corrected for with the DEPENDENCY keyword. It is recommended to use this keyword for all calculations involving diffuse functions. A good default setting is  

DEPENDENCY bas=1d-4 

However, it may be advisable to experiment a bit with the parameter, especially if many linear dependent combinations of AOs are removed. Using too many diffuse functions on a large molecule will lead to insurmountable numerical problems. In such a case it is not only useless, but even harmful, to add many diffuse functions.  

In the previous release only some basis sets were provided which contained diffuse functions. These were gathered in the directory Vdiff. Now several ET basis sets have been developed for the elements up to Ar containing some or many diffuse functions. We recommend to use these instead of the Vdiff directory. Most of these basis sets are quite large and not very suitable for large molecules. 

In ADF2005.01 augmented basis sets were added in the AUG directory, especially devised for use in in TDDFT calculations, such that one can do a reasonable accurate calculation of excitation energies, with a relatively small basis set, see D.P. Chong [#ref1]_.  


Normal or even-tempered basis?
------------------------------

For normal calculations (these form the vast majority) we recommend the use of the optimized basis sets in the directories SZ-TZ2P and, for ZORA calculations, ZORA/SZ-QZ4P. These should be sufficient in accuracy for even very demanding users and are available for the entire periodic system (in the case of the ZORA basis sets). They are also available with a frozen core variety, which saves much CPU time.  

The ET basis sets on the other hand are available only in all-electron form at the moment. Furthermore, most are pretty large (larger, but also better than TZ2P). Additionally, relatively large basis set superposition errors were detected for molecules containing atoms in the row K-Kr. For this reason we only recommend ET basis sets for the elements H-Ar at the moment. There they have yielded quite nice, near basis set limit, results for the G2 test set. For these light elements the ET basis sets can be comparable in quality to the ZORA/QZ4P basis, even though it is smaller. The ET basis sets are considered to be especially useful when diffuse functions are required. In that case it is very easy to adapt the original ET basis and fit set. The utilities provided for this in ADF will be described below in an Appendix. The ET basis set utilities will also prove useful for users who want to experiment with making their own basis sets, or who have very special demands on the basis and fit. The provided utilities automate much of the work needed to make new atomicdata files. 

Recommendations for Double-hybrids and MP2
------------------------------------------

Double-hybrid and MP2 calculations are correlated-electrons calculations and consequently they converge slower to the complete basis set limit than independent-electron methods. Also for large molecules, calculations with basis sets smaller than TZ2P are usually not very precise. We thus recommend TZ2P as a minimum requirement. The special, pseudo-correlation-consistent basis sets Corr/TZ3P and Corr/QZ6P usually give better results. They are similar to TZ2P and QZ4P, respectively, but they contain more polarization functions. They can also be ued to extrapolate the **correlation energy** to the complete basis set limit according to

.. math::

    E_{c}^{CBS} = E_{c}^{QZ} -  \frac{1}{N^{QZ}_{bas} }\frac{E_{c}^{QZ} - E_{c}^{TZ}}{\frac{1}{N^{QZ}_{bas}} - \frac{1}{N^{TZ}_{bas}}}\;.

where :math:`E_{c}^{QZ}` and :math:`E_{c}^{TZ}` are the values of the correlation energies calculated with Corr/TZ3P and Corr/QZ6P, respectively and :math:`N^{QZ}_{bas}` and :math:`N^{TZ}_{bas}` are the corresponding number of basis functions. In a double-hybrid calculation, one should only extrapolate the correlation contribution to the total energy and use the KS contribution from the calculation with the Corr/QZ6P basis set. 

The dependency key should always be used also when non-augmented basis sets are used (augmented basis sets should be avoided): 

::

   DEPENDENCY
      Bas 5e-4
   END

is usually sufficient. 

What accuracy do the basis sets give?
-------------------------------------

Tests on many diatomics were performed to test the various basis sets. We now document the results of some of these tests, in order to give a feeling for the quality that can be obtained from the various basis sets. See also van Lenthe and Baerends [#ref2]_. 

Tests for non-relativistic calculations on 36 diatomics containing oxygen, namely the oxides of the first 36 elements (H-Kr). All-electron basis sets were used. The ZORA/QZ4P basis set was used to define the basis set limit result. The numbers in the table refer to bonding energies in eV. Differences were taken between the QZ4P results and the results in smaller basis sets. By construction, the errors in the QZ4P column are zero. 

.. csv-table:: 

    ,QZ4P,DZ,DZP,TZP,TZ2P
   Average error,0.0,1.33,0.39,0.18,0.06
   Average absolute error,0.0,1.33,0.39,0.18,0.06
   Maximum error,0.0,2.84,1.07,0.41,0.13
   Worst case,all,SO,BeO,FO,O\ :sub:`2` 
   
A few comments are in order to explain this table. 

The oxides were used as a small test set because their equilibrium bond lengths are known in many cases. Also, they have a large influence on the electronic structure of the molecule, so that they also test the adequacy of the polarization functions.  

The errors in the small basis sets are systematic, because the isolated atoms are described reasonably well, but the molecular energy is not deep enough. For this reason the average errors and average absolute errors are (nearly) always equal.  

Test calculations on 100 diatomics containing oxygen, using all-electron ZORA basis sets. Many basis sets for (very) heavy elements are included here, which could not be included in the table above. The numbers have the same interpretation as above and are again in eV. 

.. csv-table:: 

    ,QZ4P,DZ,DZ,TZP,TZP,TZ2P,TZ2P
    ,ae,fc,ae,fc,ae,fc,ae
   Average error,0.00,0.95,1.07,0.20,0.20,0.05,0.05
   Average absolute error,0.00,0.98,1.07,0.20,0.21,0.05,0.05
   Maximum error,0.00,2.86,2.83,0.74,0.74,0.19,0.17
   Worst case,all,SO,SO,OgO,OgO,ThO,OgO
   
Again we place a few comments on these frozen core and all-electron results. 

The trends are very similar to those in the previous table for the lighter elements.  

The frozen core results are very satisfactory, as they are very close to the results with the corresponding all-electron basis sets. The error introduced by the frozen core approximation is typically much smaller than the one introduced by basis set incompleteness.  

The average errors are quite comparable to those from the previous table. The heavier elements do not seem to be much more difficult than the lighter ones.  

For heavy elements no reliable ET basis set is yet available for comparison.  

More results, all-electron, non-relativistic on roughly 140 different diatomics at experimental or 'reasonable' equilibrium geometries. 

.. csv-table:: 

    ,QZ4P,DZ,TZP
   Average error,0.00,0.89,0.11
   Average absolute error,0.00,0.89,0.11
   Maximum error,0.00,2.84,0.32
   Worst case,all,SO,O\ :sub:`2` 
   
Only the non-relativistic basis sets DZ and TZP are fairly complete for heavier elements.  

Also for these general diatomics (not just oxides) the average and maximum errors have decreased substantially, especially for basis TZP.  

Same table, but now for frozen core basis sets. In all these tests the smallest frozen core files were employed (i.e. the largest basis). 

.. csv-table:: 

    ,QZ4P,DZ,TZP
   Average error,0.00,0.73,0.13
   Average absolute error,0.00,0.75,0.16
   Maximum error,0.00,2.87,1.80
   Worst case,all,SO,ThO
   
The frozen core approximation has little influence on the accuracy for the new basis DZ, but a somewhat larger effect on the new basis TZP. This is especially due to certain worst cases, such as ThO.  

ZORA, all electron, over 240 diatomics 

.. csv-table:: 

    ,QZ4P,DZ,TZP,TZ2P
   Average error,0.00,0.70,0.11,0.02
   Average absolute error,0.00,0.70,0.11,0.03
   Maximum error,0.00,2.83,0.44,-0.16
   Worst case,all,SO,I\ :sub:`2` ,Cr\ :sub:`2` 
   
The average error goes down very nicely from 0.70 to 0.11 to 0.03 eV when going from DZ to TZP to TZ2P. The average error in basis TZ2P is clearly below 1kcal/mol (the famous chemical accuracy). Errors due to deficiencies in current xc functionals are still much larger than this. As a consequence, the ZORA/TZ2P basis will be more than adequate for all standard calculations.  

It is to be expected that these conclusions will not dramatically change if larger test molecules are used. Also for geometry optimizations the improved basis sets SZ-TZ2P and ZORA/SZ-TZ2P should be more than sufficient for all standard cases. The ZORA/QZ4P can be considered a very safe (though expensive) option for basis set limit calculations.  



.. [#ref1] D.P. Chong, *Augmenting basis set for time-dependent density functional theory calculation of excitation energies: Slater-type orbitals for hydrogen to krypton*, `Molecular Physics 103, 749 (2005) <https://doi.org/10.1080/00268970412331333618>`__ 

.. [#ref2] E.\  van Lenthe and E.J. Baerends, *Optimized Slater-type basis sets for the elements 1-118*, `Journal of Computational Chemistry 24, 1142 (2003) <https://doi.org/10.1002/jcc.10255>`__ 
