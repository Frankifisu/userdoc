
.. index:: basis sets
.. _basis sets:


Basis sets and atomic fragments
*******************************

.. seealso::
   * :ref:`what basis set`
   * :ref:`basis_set_file_format`


.. index:: STO basis sets
.. _STO basis sets:


STO basis sets
==============

The basis functions used in ADF are commonly known as Slater Type Orbitals (STOs). The ADF package comes with a database of STO basis sets. The basis sets are simple ASCII files and they are located in the directory ``$AMSHOME/atomicdata/ADF``. A description of the basis set file format can be found in the appendix :ref:`basis_set_file_format`.


A basis set can roughly be characterized by its size (single-, double-, triple-zeta; with or without polarization) and by the level of frozen core approximation. The standard basis sets available in ADF are:

* **SZ** Minimal basis sets: single-zeta without polarization. The exponents of the functions correspond to the standard STO-3g basis sets used in programs that employ Gaussian type basis functions. Type-SZ files are provided only for the lighter elements, up to Kr.

* **DZ** Double-zeta basis sets without polarization functions. A triple-zeta set is used for the 3d shells of the first row transition metals, the 4f shells of the Lanthanides, and the 5f shells of the Actinides. In all these cases a double-zeta set provides a rather poor expansion basis for the true (numerically computed) atomic orbital.

* **DZP** Double zeta polarized basis. The basis sets in DZP are derived from DZ, extended with a polarization function. This type of basis sets is thus far provided only for the elements up to Ar, and for the 4p series Ga through Kr.

* **TZP** Triple-zeta basis sets. A polarization function is added for H through Ar and for Ga through Kr (from DZP)

* **TZ2P** Triple-zeta with two polarization functions, for H through Ar and Ga through Kr (from DZP). Note that the TZ2P basis set files are provided only for the lighter elements, up to Kr. The ZORA/TZ2P basis set files are provided for all elements. Typically for all elements one polarization function is added compared to the corresponding TZP basis set. Note, however, that TZ2P will not always give you extra basis functions for most lanthanide and actinide frozen core basis sets.

In addition to the standard basis sets, the database contains directories with special basis sets:

* **TZ2P+** For transition metals Sc-Zn and lanthanides (ZORA) only: as TZ2P, but with extra d-STO (3d metals), and extra f-STO (lanthanides, ZORA)

* **ZORA** contains basis sets designed for :ref:`ZORA relativistic calculations<RELATIVITY>` (relativistic calculation have special basis set requirements, especially in the core region). ZORA basis sets with frozen core should be used **exclusively** in relativistic calculations with the ZORA approach, while all-electron ZORA basis sets can be used for both relativistic and non-relativistic calculations. The ZORA/QZ4P basis set can be loosely described as core triple zeta, valence quadruple zeta, with four sets of polarization functions.

* **ET** contains several even tempered basis sets which enables one to go to the basis set limit, such as ET/ET-pVQZ, ET/ET-QZ3P, ET/ET-QZ3P-1DIFFUSE, ET/ET-QZ3P-2DIFFUSE, ET/ET-QZ3P-3DIFFUSE. The accuracy of the smallest basis set in this directory can loosely be described as quadruple zeta in the valence with three polarization functions added. This directory also contains basis sets with extra diffuse functions. In Response calculations one should use such large basis sets. Very diffuse functions are absolutely necessary to get good results for excitation energies corresponding to high lying orbitals.

* **AUG** contains several augmented standard basis sets which enables one to get reasonable results for excitation energies with relatively small basis sets, such as AUG/ASZ, AUG/ADZ, AUG/ADZP, AUG/ATZP, AUG/ATZ2P.

* **Corr** contains several extended all electron ZORA basis sets, especially useful in MBPT calculations, Corr/TZ3P and Corr/QZ6P. For MBPT larger basis sets are needed to achieve the same accuracy as in a standard DFT calculation. 

Furthermore, in ``$AMSHOME/atomicdata/ADF`` you will find:

* **Special/AE** contains non-relativistic basis sets for all-electron calculations. However, these files cannot be used as such, because they don't contain any fit sets. They serve as starting point for the development of (new) basis sets. For some of the all-electron sets appropriate fit sets have already been generated. The corresponding data base files can be found in the appropriate sub-directories SZ, DZ, DZP, et cetera.

* **Special/Vdiff** contains non-relativistic basis sets that include very diffuse functions. These were recommended to be used for Response calculations. Very diffuse functions are absolutely necessary to get good results for excitation energies corresponding to high lying orbitals. Recommendation: use the even tempered basis sets in the ET directory, since these basis sets are better.

* **Special/MDC** contains non-relativistic basis sets with optimized fit functions especially useful for accurate Multipole Derived Charges. These are available only for a limited number of basis sets.

The directory ``$AMSHOME/atomicdata/Dirac`` contains the input files for the DIRAC auxiliary program (see the RELATIVITY keyword).

**Frozen core**

Multiple occurrences of one chemical element in the same basis set sub-directory correspond to different levels of the :ref:`frozen core approximation<FROZEN_CORE>`. Manganese for instance may have a basis set for an atom with a frozen 2p shell and another one with a frozen 3p shell. The file names are self-explanatory: Mn.2p stands for a data file for Manganese with frozen core shells up to the 2p level. An all-electron basis set would correspond to a file that has no frozen-core suffix in its name.

**Electronic configurations specific basis sets**

Another type of multiple occurrence of one element in one basis set directory may be found when basis sets have been developed for different electronic configurations: the Slater-type basis sets are fitted then to numerical orbitals from runs with different occupation numbers. Currently this applies only for Ni (in ``$AMSHOME/atomicdata/ADF`` ``DZ``, ``TZP`` and ``TZ2P``), where basis sets are supplied for the d8s2 and the d9s1 configurations respectively. Since in earlier releases only the d8s2 variety was available, the names of the basis set files are Ni.2p (for d8s2) and Ni_d9.2p, and likewise Ni.3p and Ni_d9.3p.

**References on basis sets**

* E.\  van Lenthe and E.J. Baerends,  *Optimized Slater-type basis sets for the elements 1-118.*  `Journal of Computational Chemistry 24, 1142 (2003) <https://doi.org/10.1002/jcc.10255>`__
* D.P. Chong, E. van Lenthe, S.J.A. van Gisbergen and E.J. Baerends,  *Even-tempered Slater-Type orbitals revisited: From Hydrogen to Krypton.*  `Journal of Computational Chemistry 25, 1030 (2004) <https://doi.org/10.1002/jcc.20030>`__
* D.P. Chong,  *Augmenting basis set for time-dependent density functional theory calculation of excitation energies: Slater-type orbitals for hydrogen to krypton.*  `Molecular Physics 103, 749 (2005) <https://doi.org/10.1080/00268970412331333618>`__

Older references for STO basis sets are Refs. [#ref1]_ [#ref2]_ [#ref3]_. See also the paper by Raffennetti on design and optimization of even-tempered STO basis sets [#ref4]_. The paper by Del Chong describes completeness profiles as a visual tool in estimating the completeness of a basis set [#ref5]_. Finally, Zeiss and coworkers [#ref6]_ describe field-induced polarization functions for STOs. These are useful for defining basis sets with diffuse functions for (hyper)polarizability and other property calculations.

The procedure for the usage and optimization of fit functions is described by Baerends et al. [#ref7]_.

For documentation on how to make custom even-tempered basis/fit sets, see the `old ADF 2014 documentation <https://downloads.scm.com/Doc/Doc2014/ADF/ADFUsersGuide/ADFUsersGuide.pdf>`__.


.. index:: standard basis sets

Available basis sets
====================

ADF has optimized STO basis sets for the whole periodic table (Z=1-120).

.. raw:: html

   <table style="background-color:lightgrey; border-spacing: 2px 2px; border-collapse: separate;">
   <tr style="text-align: center;">
   <th></th>
   <th>1</th><th>2</th><th></th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th>
   <th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th>
   <th>15</th><th>16</th><th>17</th><th>18</th>
   </tr>

   <tr style="text-align: center;">
   <th>1</th>
   <td style="background-color:violet;">1<br>H</td>
   <td colspan=17></td>
   <td style="background-color:violet;">2<br>He</td>
   </tr>

   <tr style="text-align: center;">
   <th>2</th>
   <td style="background-color:violet;">3<br>Li</td>
   <td style="background-color:violet;">4<br>Be</td>
   <td colspan=11></td>
   <td style="background-color:orange">5<br>B</td>
   <td style="background-color:orange">6<br>C</td>
   <td style="background-color:orange">7<br>N</td>
   <td style="background-color:orange">8<br>O</td>
   <td style="background-color:orange">9<br>F</td>
   <td style="background-color:orange">10<br>Ne</td>
   </tr>

   <tr style="text-align: center;">
   <th>3</th>
   <td style="background-color:violet;">11<br>Na</td>
   <td style="background-color:violet;">12<br>Mg</td>
   <td colspan=11></td>
   <td style="background-color:orange">13<br>Al</td>
   <td style="background-color:orange">14<br>Si</td>
   <td style="background-color:orange">15<br>P</td>
   <td style="background-color:orange">16<br>S</td>
   <td style="background-color:orange">17<br>Cl</td>
   <td style="background-color:orange">18<br>Ar</td>
   </tr>

   <tr style="text-align: center;">
   <th>4</th>
   <td style="background-color:violet;">19<br>K</td>
   <td style="background-color:violet;">20<br>Ca</td>
   <td></td>
   <td style="background-color:yellow;">21<br>Sc</td>
   <td style="background-color:yellow;">22<br>Ti</td>
   <td style="background-color:yellow;">23<br>V</td>
   <td style="background-color:yellow;">24<br>Cr</td>
   <td style="background-color:yellow;">25<br>Mn</td>
   <td style="background-color:yellow;">26<br>Fe</td>
   <td style="background-color:yellow;">27<br>Co</td>
   <td style="background-color:yellow;">28<br>Ni</td>
   <td style="background-color:yellow;">29<br>Cu</td>
   <td style="background-color:yellow;">30<br>Zn</td>
   <td style="background-color:orange">31<br>Ga</td>
   <td style="background-color:orange">32<br>Ge</td>
   <td style="background-color:orange">33<br>As</td>
   <td style="background-color:orange">34<br>Se</td>
   <td style="background-color:orange">35<br>Br</td>
   <td style="background-color:orange">36<br>Kr</td>
   </tr>

   <tr style="text-align: center;">
   <th>5</th>
   <td style="background-color:violet;">37<br>Rb</td>
   <td style="background-color:violet;">38<br>Sr</td>
   <td></td>
   <td style="background-color:yellow;">39<br>Y</td>
   <td style="background-color:yellow;">40<br>Zr</td>
   <td style="background-color:yellow;">41<br>Nb</td>
   <td style="background-color:yellow;">42<br>Mo</td>
   <td style="background-color:yellow;">43<br>Tc</td>
   <td style="background-color:yellow;">44<br>Ru</td>
   <td style="background-color:yellow;">45<br>Rh</td>
   <td style="background-color:yellow;">46<br>Pd</td>
   <td style="background-color:yellow;">47<br>Ag</td>
   <td style="background-color:yellow;">48<br>Cd</td>
   <td style="background-color:orange;">49<br>In</td>
   <td style="background-color:orange">50<br>Sn</td>
   <td style="background-color:orange">51<br>Sb</td>
   <td style="background-color:orange">52<br>Te</td>
   <td style="background-color:orange">53<br>I</td>
   <td style="background-color:orange">54<br>Xe</td>
   </tr>

   <tr style="text-align: center;">
   <th>6</th>
   <td style="background-color:violet;">55<br>Cs</td>
   <td style="background-color:violet;">56<br>Ba</td>
   <td>La-<br>Yb</td>
   <td style="background-color:yellow;">71<br>Lu</td>
   <td style="background-color:yellow;">72<br>Hf</td>
   <td style="background-color:yellow;">73<br>Ta</td>
   <td style="background-color:yellow;">74<br>W</td>
   <td style="background-color:yellow;">75<br>Re</td>
   <td style="background-color:yellow;">76<br>Os</td>
   <td style="background-color:yellow;">77<br>Ir</td>
   <td style="background-color:yellow;">78<br>Pt</td>
   <td style="background-color:yellow;">79<br>Au</td>
   <td style="background-color:yellow;">80<br>Hg</td>
   <td style="background-color:orange">81<br>Tl</td>
   <td style="background-color:orange">82<br>Pb</td>
   <td style="background-color:orange">83<br>Bi</td>
   <td style="background-color:orange">84<br>Po</td>
   <td style="background-color:orange">85<br>At</td>
   <td style="background-color:orange">86<br>Rn</td>
   </tr>

   <tr style="text-align: center;">
   <th>7</th>
   <td style="background-color:violet;">87<br>Fr</td>
   <td style="background-color:violet;">88<br>Ra</td>
   <td>Ac-<br>No</td>
   <td style="background-color:yellow;">103<br>Lr</td>
   <td style="background-color:yellow;">104<br>Rf</td>
   <td style="background-color:yellow;">105<br>Db</td>
   <td style="background-color:yellow;">106<br>Sg</td>
   <td style="background-color:yellow;">107<br>Bh</td>
   <td style="background-color:yellow;">108<br>Hs</td>
   <td style="background-color:yellow;">109<br>Mt</td>
   <td style="background-color:yellow;">110<br>Ds</td>
   <td style="background-color:yellow;">111<br>Rg</td>
   <td style="background-color:yellow;">112<br>Cn</td>
   <td style="background-color:orange">113<br>Nh</td>
   <td style="background-color:orange">114<br>Fl</td>
   <td style="background-color:orange">115<br>Mc</td>
   <td style="background-color:orange">116<br>Lv</td>
   <td style="background-color:orange">117<br>Ts</td>
   <td style="background-color:orange">118<br>Og</td>
   </tr>

   <tr style="text-align: center;">
   <th>8</th>
   <td style="background-color:violet;">119<br>Uue</td>
   <td style="background-color:violet;">120<br>Ubn</td>
   <td colspan=17></td>
   </tr>

   <tr><td colspan=20>&nbsp; </td></tr>

   <tr style="text-align: center;">
   <td colspan=4><FONT SIZE=-1>Lanthanide<br>elements</FONT></td>
   <td style="background-color:lightgreen">57<br>La</td>
   <td style="background-color:lightgreen">58<br>Ce</td>
   <td style="background-color:lightgreen">59<br>Pr</td>
   <td style="background-color:lightgreen">60<br>Nd</td>
   <td style="background-color:lightgreen">61<br>Pm</td>
   <td style="background-color:lightgreen">62<br>Sm</td>
   <td style="background-color:lightgreen">63<br>Eu</td>
   <td style="background-color:lightgreen">64<br>Gd</td>
   <td style="background-color:lightgreen">65<br>Tb</td>
   <td style="background-color:lightgreen">66<br>Dy</td>
   <td style="background-color:lightgreen">67<br>Ho</td>
   <td style="background-color:lightgreen">68<br>Er</td>
   <td style="background-color:lightgreen">69<br>Tm</td>
   <td style="background-color:lightgreen">70<br>Yb</td>
   <td colspan=2></td>
   </tr>

   <tr style="text-align: center;">
   <td colspan=4><FONT SIZE=-1>Actinide<br>elements</FONT></td>
   <td style="background-color:lightgreen">89<br>Ac</td>
   <td style="background-color:lightgreen">90<br>Th</td>
   <td style="background-color:lightgreen">91<br>Pa</td>
   <td style="background-color:lightgreen">92<br>U</td>
   <td style="background-color:lightgreen">93<br>Np</td>
   <td style="background-color:lightgreen">94<br>Pu</td>
   <td style="background-color:lightgreen">95<br>Am</td>
   <td style="background-color:lightgreen">96<br>Cm</td>
   <td style="background-color:lightgreen">97<br>Bk</td>
   <td style="background-color:lightgreen">98<br>Cf</td>
   <td style="background-color:lightgreen">99<br>Es</td>
   <td style="background-color:lightgreen">100<br>Fm</td>
   <td style="background-color:lightgreen">101<br>Md</td>
   <td style="background-color:lightgreen">102<br>No</td>
   <td colspan=2></td>
   </tr>
   </table>
   &nbsp;

The next tables give an indication which all electron (ae) and frozen core (fc) standard basis sets are available for the different elements in ADF.

.. csv-table:: Available standard basis sets for non-relativistic (non-rel) and ZORA calculations H-Kr (Z=1-36)
   :header: "Element",  "ae or fc", "SZ, DZ", "DZP", "TZP, TZ2P", "TZ2P+", "QZ4P, ET", "AUG"

   H-He (Z=1-2)    , ae      , Yes ,  Yes  ,  Yes,      ,  Yes ,  Yes
   Li-Ne (Z=3-10)  , ae      , Yes ,  Yes  ,  Yes,      ,  Yes ,  Yes
                   ,.1s      , Yes ,  Yes  ,  Yes,      ,      ,  non-rel
   Na-Ar (Z=11-18) , ae      , Yes ,  Yes  ,  Yes,      ,  Yes ,  Yes
                   ,.1s .2p  , Yes ,  Yes  ,  Yes,      ,      ,  non-rel
   K-Ca (Z=19-20)  , ae      , Yes ,  Yes  ,  Yes,      ,  Yes ,  Yes
                   ,.2p .3p  , Yes ,  Yes  ,  Yes,      ,      ,  non-rel
   Sc-Zn (Z=21-30) , ae      , Yes ,       ,  Yes, Yes  ,  Yes ,  Yes
                   ,.2p .3p  , Yes ,       ,  Yes, Yes  ,      ,  non-rel
   Ga-Kr (Z=31-36) , ae      , Yes ,  Yes  ,  Yes,      ,  Yes ,  Yes
                   ,.3p .3d  , Yes ,  Yes  ,  Yes,      ,      ,  non-rel


.. csv-table:: Available standard basis sets for non-relativistic calculations Rb-Cm (Z=37-96)
   :header: "Element",  "fc", "DZ, TZP"

   Rb-Sr (Z=37-38)    ,.3p .3d  .4p    ,  Yes
   Y-Cd (Z=39-48)     ,.3d .4p         ,  Yes
   In-Ba (Z=49-56)    ,.4p .4d         ,  Yes
   La-Lu (Z=57-71)    ,.4d .5p         ,  Yes
   Hf-Hg (Z=72-80)    ,.4d .4f         ,  Yes
   Tl-Rn (Z=81-86)    ,.4d .4f .5p .5d ,  Yes
   Fr-Ra (Z=87-88)    ,.5p .5d         ,  Yes
   Ac-Cm (Z=89-96)    ,.5d             ,  Yes

.. csv-table:: Available standard basis sets for ZORA calculations Rb-Og (Z=37-120)
   :header: "Element",  "ae or fc", "DZ, TZP, TZ2P", "TZ2P+", "QZ4P"

   Rb-Sr (Z=37-38)    , ae              ,  Yes  ,     ,  Yes
                      ,.3p .3d  .4p     ,  Yes  ,     ,
   Y-Cd (Z=39-48)     , ae              ,  Yes  ,     ,  Yes
                      ,.3d  .4p         ,  Yes  ,     ,
   In-Ba (Z=49-56)    , ae              ,  Yes  ,     ,  Yes
                      ,.4p  .4d         ,  Yes  ,     ,
   La-Yb (Z=57-70)    , ae              ,  Yes  , Yes ,  Yes
                      ,.4d  .5p         ,  Yes  , Yes ,
   Lu (Z=71)          , ae              ,  Yes  ,     ,  Yes
                      ,.4d  .5p         ,  Yes  ,     ,
   Hf-Hg (Z=72-80)    , ae              ,  Yes  ,     ,  Yes
                      ,.4d  .4f         ,  Yes  ,     ,
   Tl    (Z=81)       , ae              ,  Yes  ,     ,  Yes
                      ,.4d  .4f .5p     ,  Yes  ,     ,
   Pb-Rn (Z=82-86)    , ae              ,  Yes  ,     ,  Yes
                      ,.4d  .4f .5p .5d ,  Yes  ,     ,
   Fr-Ra (Z=87-88)    , ae              ,  Yes  ,     ,  Yes
                      ,.5p .5d          ,  Yes  ,     ,
   Ac-Lr (Z=89-103)   , ae              ,  Yes  ,     ,  Yes
                      ,.4f .5d          ,  Yes  ,     ,
   Rf-Cn (Z=104-112)  , ae              ,  Yes  ,     ,  Yes
                      ,.4f .5d .5f      ,  Yes  ,     ,
   Nh-Og (Z=113-118)  , ae              ,  Yes  ,     ,  Yes
                      ,.5d .5f          ,  Yes  ,     ,
   Uue-Ubn (Z=119-120), ae              ,  Yes  ,     ,  Yes
                      ,.5f              ,  Yes  ,     ,

For heavier elements, from Rb on, the non-relativistic all electron basis sets are missing. In the ZORA basis sets directory you will find all-electron basis sets for all elements (Z = 1-120), which also could be used in non-relativistic calculations.
Note, however, that these basis sets were optimized for ZORA calculations, which means that non-relativistic calculations will not always give you the expected accuracy.
Non-relativistically optimized basis sets for the heavier elements are provided in a separate directory AE, which contains basis sets of single-, double- and triple-zeta quality indicated respectively by suffixes 'sz', 'dz', and 'tz'. The files in Special/AE/ are not complete basis set files, because they don't contain fit sets (the usage and relevance of fit functions is explained later).


**Basis sets directories**

Basis sets can be found in the directory ``$AMSHOME/atomicdata/ADF``, for non-relativistic calculations in the sub-directories SZ, DZ, DZP, TZP, TZ2P, TZ2P+, for ZORA calculations in ZORA/SZ, ZORA/DZ, ZORA/DZP, ZORA/TZP, ZORA/TZ2P, ZORA/TZ2P+, ZORA/TZ2P-J, ZORA/QZ4P, ZORA/QZ4P-J, the augmented basis sets can be found in AUG/ASZ, AUG/ADZ, AUG/ADZP, AUG/ATZP, AUG/ATZ2P, the even tempered basis sets in ET/ET-pVQZ, ET/ET-QZ3P, ET/ET-QZ3P-1DIFFUSE, ET/ET-QZ3P-2DIFFUSE, ET/ET-QZ3P-3DIFFUSE, the basis sets for MBPT calculations in Corr/TZ3P, Corr/QZ6P. All electron basis sets can be used in non-relativistic and ZORA calculations.

**Basis sets acronyms**

+ SZ:   single zeta

+ DZ:   double zeta

+ DZP:  double zeta + 1 polarization function

+ TZP:  valence triple zeta + 1 polarization function

+ TZ2P: valence triple zeta + 2 polarization function

+ TZ2P+: = TZ2P + extra d (3d metals) or extra f (lanthanides)

+ QZ4P: valence quadruple zeta + 4 polarization function, relativistically optimized

+ ET: even tempered

  + pVQZ, QZ3P: valence quadruple zeta + 3 polarization function, even tempered

  + QZ3P-nD: = QZ3P + n diffuse sets of s, p, d, and f functions, even tempered

+ AUG: augmented

  + ASZ, ADZ, ADZP, ATZP, ATZ2P: augmented for use in TDDFT

+ Corr: for use in MBPT

  + TZ3P: = all electron (Z=1-54) ZORA/TZ2P + extra tight polarization function

  + QZ6P: = all electron (Z=1-118) ZORA/QZ4P + extra tight polarization functions

+ TZ2P-J, QZ4P-J: for use in ESR hyperfine or NMR spin-spin couplings

  + TZ2P or QZ4P + extra tight (mainly 1s) functions

**All electron or frozen core**

+ element name (without suffix): all electron

+ .1s frozen: 1s

+ .2p frozen: 1s 2s 2p

+ .3p frozen: 1s 2s 2p 3s 3p

+ .3d frozen: 1s 2s 2p 3s 3p 3d

+ .4p frozen: 1s 2s 2p 3s 3p 3d 4s 4p

+ .4d frozen: 1s 2s 2p 3s 3p 3d 4s 4p 4d

+ .4f frozen: 1s 2s 2p 3s 3p 3d 4s 4p 4d 4f

+ .5p frozen: 1s 2s 2p 3s 3p 3d 4s 4p 4d 5s 5p (La-Lu)

+ .5p frozen: 1s 2s 2p 3s 3p 3d 4s 4p 4d 4f 5s 5p (other)

+ .5d frozen: 1s 2s 2p 3s 3p 3d 4s 4p 4d 4f 5s 5p 5d

+ .6p frozen: 1s 2s 2p 3s 3p 3d 4s 4p 4d 4f 5s 5p 5d 6s 6p (Ac-Lr)

+ .5f frozen: 1s 2s 2p 3s 3p 3d 4s 4p 4d 4f 5s 5p 5d 5f 6s 6p



.. _keyscheme BASIS:

The Basis Key
=============

The basis set can be specified in the input via the ``Basis`` key block.
The most important subkeys Type and Core.
Description of all subkeys:

.. scmautodoc:: adf Basis Type Core
   :collapselongchoicesinsummary:

**Warning:** Do not include the :ref:`Corepotentials<keyscheme COREPOTENTIALS>` keys when using the Basis key.
Typically one should not include both the the Basis key and the :ref:`Fragments<MOLECULARFRAGMENTS>` key.

Description of the other Basis subkeys:

.. scmautodoc:: adf Basis CreateOutput Path PerAtomType PerRegion FitType
   :noref:
   :skipblockdescription:
   :collapselongchoicesinsummary:

An example where you can use regions to define basis sets for parts of your system, see :ref:`example Multiresolution_H2O`.

.. index:: automatic mode

Automatic mode
==============

The following input will run a geometry optimization on water, using a (almost) minimal input:

::

   "$AMSBIN/ams" <<eor
      Task GeometryOptimization
      System
         Atoms
            O  0  0  0
            H  1  1  0
            H -1  1  0
         End
         Symmetrize Yes
      End

      Engine ADF
         Basis
            Type TZP
         End
      EndEngine
   eor


* The ``ATOMS`` subblock key in the ``System`` block key specifies the geometry of the system;
* the ``Task GeometryOptimization`` key instructs AMS to perform a geometry optimization;
* the ``Basis`` block key instructs ADF to run the *create runs* automatically, using a TZP basis sets.

The *automatic mode* will be used when the ``Basis`` key is present in the input, or if no ``Fragments`` block key is present.

In *automatic mode* ADF will first create fragment files for all the basic atom fragments found in the ``Atoms`` block. Normally this means that for each atom type in your molecule a fragment file will be created.

You may have different fragments with the same atom: add a dot and a name (without spaces) after the name of the element. For example: ``H.1`` and ``H.2``. In this example two fragment files will be created: one for the ``H.1`` fragment and one for the ``H.2`` fragment. Using the ``PerAtomType`` subkey you may assign different basis sets to these fragments. Another consequence is that the ``H.1`` and ``H.2`` atoms will never be symmetry equivalent to each other.

In case of a relativistic calculation, the DIRAC program will also be run automatically, and the create runs will include the correct relativistic key and corresponding basis sets. For **ZORA** calculations, ADF first tries to locate a special ZORA basis set. If this does not succeed it will use a normal basis set if the required basis set does not use a frozen core.

.. index:: create mode

Create mode
===========

Expert option. In Create mode the input file is relatively simple.
First, the geometry is trivial: one atom at the origin.

Second, the problem is computationally so simple that default settings for precision aspects, such as convergence criteria and levels of numerical integration accuracy, are internally defined to be much more stringent than in normal calculations. These aspects don't have to be looked after.
Also one should specify the wanted XC functional.
If you use the Basis key all this will be handled automatically.

In Create mode you need an input file of the following form:

.. _keyscheme CREATE:


::

   System
     Atoms
       Atomtype 0 0 0
     End
   end
   Task SinglePoint
   Engine ADF
     CREATE Atomtype Datafile
   EndEngine

``Create``
   is the keyword. The remainder of the record (atomtype datafile) is the argument.

``Atomtype``
   is a name for the basic atom that you want to create. The program reads and interprets this name. Therefore, the name must begin with the standard chemical symbol (H, He, Li, ...) of the element to be created. Optionally the name may have an suffix of the form .text. The suffix begins with a period (.); the part after the period (text) is at your discretion as long as it does not contain a delimiter. A few examples:

.. csv-table:: Examples of appropriate and inappropriate atom type names used with the keyword create.

   **appropriate names** , **inappropriate names**
   K                     , Si-with-core (no period after the chemical symbol)
   Li.newbasis           , $HOME/atomicdata/ADF/C.dzp (not beginning with the chemical symbol)
   P.1992_Feb.30         , "Ga.nocore,smallbasis (contains a comma (a delimiter))"
                         , Sodium.2s (Sodium is not the *symbol* for this element (Na))


``Datafile``
   specifies the data file that contains the basis set and related items. It may contain a full path if the file does not reside in the working directory of the job. The datafile part is optional. If you omit it, ADF assumes that the file name is identical to the atom type name, i.e. Create Atomtype is equivalent to and interpreted as Create Atomtype Atomtype In view of the restrictions that apply to the atom type name, the option to use the short form can only be used if the file name has the appropriate format. To make the input file easier to understand for a human reader you may, for Datafile, also type file=Datafile, where file= must be typed as such, and datafile is the name of the file.

So you could have a simple calculation as follows (the 'creation' of a Carbon atom);

::

   $AMSBIN/ams << eor
     System
       Atoms
         C 0 0 0
       End
     end
     Task SinglePoint
     Engine ADF
       Create C $AMSHOME/atomicdata/ADF/DZ/C.1s
     EndEngine
   eor

The presence of the keyword ``create`` sets the computational mode of ADF to: *create a basic atom*.
Here a basis set file is located in ``$AMSHOME/atomicdata/ADF``, where
the file 'C.1s' in the sub-directory DZ/ (this contains basis sets of double-zeta quality).
Examine logfile and out to check that everything has gone well.

A considerable number of basis set files are included in the ADF. You can also create basic atoms corresponding to so-called *Alternative Elements*, with for instance a non-integer nuclear charge or a different mass. See the next section.

.. _GHOST:
.. _Alternative Elements:
.. index:: ghost atoms
.. index:: alternative elements

Ghost Atoms, Non-standard Chemical Elements
===========================================

The atom type names used under atoms (and in the create record) must begin with the standard chemical element symbol (H, He, Li...). The program uses this to deduce the nuclear charge and other elemental properties.

For the standard elements one can redefine the atomic mass (for instance to define a suitable isotope).
Masses are specified by adding the desired mass (in Dalton) at the end of the atom's line (mass=).

It is also possible to define an artificial chemical element with user-specified properties.
Such new elements are denoted *Alternative Elements*; and may for instance have a non-integer nuclear charge.

The chemical symbol of for a (ghost) atom that has zero nuclear charge is Gh.
The ``BASIS`` key recognizes elements denoted with Gh.atom in the ATOMS key as being ghost atoms. If one does not specifically select a basis set for this ghost atom, the all electron basis set for the atom is selected in the creation of the ghost atom using the type of basis set chosen with the BASIS key. The atom name must begin with the standard one- or two-character symbol for the chemical element: Gh.H, Gh.He, Gh.Li, and so on. Optionally it may be appended by .text, where text is any string (not containing delimiters). Examples: Gh.H, Gh.Mn.3, Gh.Cu.dz-new.
See also the `Basis set superposition error (BSSE) tutorial <../../Tutorials/StructureAndReactivity/BSSEDoubleHybrids.html>`__.

For other alternative elements, for instance that have a non-integer nuclear charge, one should use one of the standard chemical symbols.
The ``BASIS`` key will use this chemical symbol for selecting the basis set for this alternative element.
Nuclear charges are specified by adding the nuclear charge at the end of the atom's line (nuclear_charge=).

You can create Gh-type basic atoms and other alternative elements and use them subsequently as fragments in a molecule.

Automatic mode
--------------

AMS allows to set user-defined masses for particular atoms. This can be used to simulate isotopes of different atoms. Masses are specified by adding the desired mass (in Dalton) at the end of the atom's line.

**Example:** three different hydrogen isotopes:

::

   System
      Atoms
         N       0.000000    0.000000    0.010272
         H      -0.471582   -0.816803    0.407861
         H       0.943163    0.000000    0.407861 mass=2.014101778
         H      -0.471582    0.816803    0.407861 mass=3.01604927
      End
   End

**Use as fragment**

Alternative basic atoms can be used like any other basic atoms to build up larger fragments and molecules.
Gh can be considered just one more chemical symbol along with the other traditional ones.
For other alternative elements one should define the nuclear charge, and possibly the nuclear mass.

You may have different alternative elements in a molecule, with different nuclear charges for instance.

**Example:** ghost atoms:

::

   System
      atoms
         Gh.O  -0.525330     -0.050971     -0.314517
         Gh.H  -0.942007      0.747902      0.011253
         Gh.H   0.403697      0.059786     -0.073568
         O      2.316633      0.045501      0.071858
         H      2.684616     -0.526577      0.749387
         C      2.781638     -0.426129     -1.190301
         H      2.350821      0.224965     -1.943415
         H      3.867602     -0.375336     -1.264613
         H      2.453296     -1.445999     -1.389381
      end
   end

**Example:** alternative elements:

::

   System
      Atoms
         Mg 0.0  0.0  0.0
         F  1.0  1.0  1.0  nuclear_charge=9.5
         F  1.0 -1.0 -1.0  nuclear_charge=9.5
         F -1.0  1.0 -1.0  nuclear_charge=9.5
         F -1.0 -1.0  1.0  nuclear_charge=9.5
      End
   End

.. _NUCLEARMODEL:
.. index:: finite nucleus
.. index:: nuclear model

Nuclear Model
=============

By default in ADF a point charge model is used for the nuclear charge distribution. Alternatively, one can use a spherical Gaussian nuclear charge distribution model, see Ref. [#ref8]_. Nuclear finite size effects can have large effects on hyperfine interactions (ESR A-tensor, NMR spin-spin coupling) if heavy atoms like, for example, Mercury (Hg), are involved. In Ref. [#ref8]_ it was asserted that the isotropic J-couplings (parameters in NMR spin-spin coupling) are typically reduced in magnitude by about 10 to 15 % for couplings between one of the heaviest NMR nuclei and a light atomic ligand, and even more so for couplings between two heavy atoms. This Ref. [#ref8]_ gives more details on the parameters used in the Gaussian nuclear charge distribution model. Note that one needs basis sets with very tight functions to see any effect of using a finite size of the nucleus instead of a point nucleus. Such basis sets can be found for all elements in ``$AMSRESOURCES/ZORA/TZ2P-J`` and ``$AMSRESOURCES/ZORA/QZ4P-J``, and for some elements in ``$AMSRESOURCES/ZORA/jcpl``, which are basis sets especially designed for ESR hyperfine and NMR spin-spin coupling calculations.

.. scmautodoc:: adf NuclearModel

In the ADF output parameters will be shown for the Gaussian nuclear charge distribution if one includes in the input for ADF:

::

   PRINT Nuclei

Starting from ADF2013 ADF also uses a finite distribution of the nuclear magnetic dipole moment for the calculation of the A-tensor.

.. only:: html

  .. rubric:: References

.. [#ref1] E.\  Clementi, C. Roetti, *Roothaan-Hartree-Fock atomic wavefunctions: Basis functions and their coefficients for ground and certain excited states of neutral and ionized atoms, Z* :math:`\leq` 54, `Atomic Data and Nuclear Data Tables 14, 177 (1974) <https://doi.org/10.1016/S0092-640X(74)80016-1>`__

.. [#ref2] A.D. McLean, R.S. McLean, *Roothaan-Hartree-Fock atomic wave functions Slater basis-set expansions for Z = 55-92*, `Atomic Data and Nuclear Data Tables 26, 197 (1981) <https://doi.org/10.1016/0092-640X(81)90012-7>`__

.. [#ref3] J.G. Snijders, P. Vernooijs, E.J. Baerends, *Roothaan-Hartree-Fock-Slater atomic wave functions: Single-zeta, double-zeta, and extended Slater-type basis sets for* \ :sub:`87` Fr-\ :sub:`103` Lr, `Atomic Data and Nuclear Data Tables 26, 483 (1981) <https://doi.org/10.1016/0092-640X(81)90004-8>`__

.. [#ref4] R.C. Raffenetti, *Eventempered atomic orbitals. II. Atomic SCF wavefunctions in terms of eventempered exponential bases*, `Journal of Chemical Physics 59, 5936 (1973) <https://doi.org/10.1063/1.1679962>`__

.. [#ref5] D.P. Chong, *Completeness profiles of one-electron basis sets*, `Canadian Journal of Chemistry 73, 79 (1995) <https://doi.org/10.1139/v95-011>`__

.. [#ref6] G.D. Zeiss, W.R. Scott, N. Suzuki, D.P. Chong, S.R. Langhoff, *Finite-field calculations of molecular polarizabilities using field-induced polarization functions: second- and third-order perturbation correlation corrections to the coupled Hartree-Fock polarizability of* H\ :sub:`2` O, `Molecular Physics 37, 1543 (1979) <https://doi.org/10.1080/00268977900101121>`__

.. [#ref7] E.J. Baerends, D.E. Ellis and P. Ros, *Self-consistent molecular Hartree-Fock-Slater calculations I. The computational procedure*, `Chemical Physics 2, 41 (1973) <https://doi.org/10.1016/0301-0104(73)80059-X>`__

.. [#ref8] J.\  Autschbach, *Magnitude of Finite-Nucleus-Size Effects in Relativistic Density Functional Computations of Indirect NMR Nuclear Spin-Spin Coupling Constants*, `ChemPhysChem 10, 2274 (2009) <https://doi.org/10.1002/cphc.200900271>`__
