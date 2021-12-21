References
##########


Slater-Koster based DFTB
************************

.. _DFTBReference:

General Description
===================

D.\  Porezag, T. Frauenheim, T. Köhler, G. Seifert, R. Kaschner, *Construction of tight-binding-like potentials on the basis of density-functional theory: Application to carbon*, `Phys. Rev. B 51, 12947-12957 (1995) <https://doi.org/10.1103/PhysRevB.51.12947>`__

G.\  Seifert, D. Porezag, T. Frauenheim, *Calculations of molecules, clusters, and solids with a simplified LCAO-DFT-LDA scheme*, `Int. J. Quantum Chem. 58, 185-192 (1996) <https://doi.org/10.1002/(SICI)1097-461X(1996)58:2%3C185::AID-QUA7%3E3.0.CO;2-U>`__

M.\  Elstner, D. Porezag, G. Jungnickel, J. Elsner, M. Haugk, T. Frauenheim, S. Suhai, and G. Seifert,  *Self-consistent charge density functional tight-binding method for simulation of complex material properties*,  `Physical Review B  58, 7260 (1998) <http://link.aps.org/doi/10.1103/PhysRevB.58.7260>`__

T.\  Frauenheim, G. Seifert, M. Elstner, Z. Hajnal, G. Jungnickel, D. Porezag, S. Suhai, and R. Scholz,  *A self-consistent charge density-functional based tight-binding method for predictive materials simulations in physics, chemistry and biology*,  `Physica Status Solidi (b) 217, 41 (2000) <http://onlinelibrary.wiley.com/doi/10.1002/(SICI)1521-3951(200001)217:1%3C41::AID-PSSB41%3E3.0.CO;2-V/abstract>`__

M.\  Elstner, T. Frauenheim, E. Kaxiras, G. Seifert, and S. Suhai,  *A self-consistent charge density-functional based tight-binding scheme for large biomolecules*,  `Physica Status Solidi (b)  217, 357 (2000) <http://onlinelibrary.wiley.com/doi/10.1002/(SICI)1521-3951(200001)217:1%3C357::AID-PSSB357%3E3.0.CO;2-J/abstract>`__

C.\  Koehler, G. Seifert, U. Gerstmann, M. Elstner, H. Overhof, and T. Frauenheim,  *Approximate density-functional calculations of spin densities in large molecular systems and complex solids*,  `Physical Chemistry Chemical Physics  3, 5109 (2001) <http://www.rsc.org/publishing/journals/CP/article.asp?doi=b105782k>`__

T.\  Frauenheim, G. Seifert, M. Elstner, T. Niehaus, C. Kohler, M. Armkreutz, M. Sternberg, Z. Hajnal, A. di Carlo, and S. Suhai,  *Atomistic Simulations of complex materials: ground and excited state properties*,  `Journal of Physics: Condensed Matter 14, 3015 (2002) <http://www.iop.org/EJ/abstract/0953-8984/14/11/313>`__

M.\  Gaus, Q. Cui, and M. Elstner, *DFTB3: Extension of the Self-Consistent-Charge Density-Functional Tight-Binding Method (SCC-DFTB)*,  `Journal of Chemical Theory and Computation 7, 931 (2011) <http://pubs.acs.org/doi/abs/10.1021/ct100684s>`__

T.\  A. Niehaus, S. Suhai, F. Della Sala, P. Lugli, M. Elstner, G. Seifert, and Th. Frauenheim, *Tight-binding approach to time-dependent density-functional response theory*, `Phys. Rev. B 63, 085108 (2001) <https://doi.org/10.1103/PhysRevB.63.085108>`__

D.\  Heringer, T. A. Niehaus, M. Wanko, Th. Frauenheim *Analytical excited state forces for the time-dependent density-functional tight-binding method*, `J. Comput. Chem., 28: 2589-2601 <https://doi.org/10.1002/jcc.20697>`__


Parameter sets
==============


.. _QUASINANO2013.1:

QUASINANO2013.1
---------------

The DFTB parameter files in $AMSHOME/atomicdata/DFTB/QUASINANO2013.1 are distributed with the AMS package.
These are parameters only for the electronic part of the DFTB method that covers almost the complete periodic table (no f-elements).
No forces can be calculated.
These parameters can be used in TDDFTB calculations, for example.

M.\  Wahiduzzaman, A.F. Oliveira, P.H.T. Philipsen, L. Zhechkov, E. van Lenthe, H.A. Witek, T. Heine, *DFTB Parameters for the Periodic Table: Part 1, Electronic Structure*,  `Journal of Chemical Theory and Computation 9, 4006 (2013) <https://doi.org/10.1021/ct4004959>`__


.. _QUASINANO2015:

QUASINANO2015
=============

The DFTB parameter files in $AMSHOME/atomicdata/DFTB/QUASINANO2015 are distributed with the AMS package.
The QUASINANO2015 parameter set extends the QUASINANO2013.1 parameter set, and includes terms that are needed to compute the total energy and its gradient.

A.\  F. Oliveira, P. Philipsen, T. Heine. *DFTB Parameters for the Periodic Table, Part 2: Energies and Energy Gradients from Hydrogen to Calcium*, `Journal of Chemical Theory and Computation 11 (11), pp 5209–5218 (2015) <https://doi.org/10.1021/acs.jctc.5b00702>`__


.. _DRESDEN:

Dresden
=======

The DFTB parameter files in $AMSHOME/atomicdata/DFTB/Dresden are distributed with the AMS package. For more detailed information, see also the README file in the directory $AMSHOME/atomicdata/DFTB/Dresden.

General reference for the construction of all integral tables in $AMSHOME/atomicdata/DFTB/Dresden:
J. Frenzel, A. F. Oliveira, N. Jardillier, T. Heine, and G. Seifert, *Semi-relativistic, self-consistent charge Slater-Koster tables for density-functional based tight-binding (DFTB) for materials science simulations*, TU-Dresden 2004-2009.

For construction and application of integral tables for Al-O-H:
J. Frenzel, A. F. Oliveira, H. A. Duarte, T. Heine, and G. Seifert, *Structural and electronic properties of bulk gibbsite and gibbsite, surfaces*,  `Zeitschrift fr Anorganische und Allgemeine Chemie 631, 1267 (2005) <https://doi.org/10.1002/zaac.200500051>`__

For construction and application of integral tables for Al-Si-O-H:
L. Guimares, A. N. Enyashin, J. Frenzel, T. Heine, H. A. Duarte, and G. Seifert,  *Imogolite Nanotubes: Stability, electronic and mechanical properties*,  `Nano 1, 362 (2007) <https://doi.org/10.1021/nn700184k>`__

For construction and application of integral tables for Al-O-P-C-H:
R. Luschtinetz, A. F. Oliveira, J. Frenzel, J. Joswig, G. Seifert, and H. A. Duarte, *Adsorption of phosphonic and ethylphosphonic acid on aluminum oxide surfaces*,  `Surface Science 602, 1347 (2008) <https://doi.org/10.1016/j.susc.2008.01.035>`__

For construction and application of integral tables for Ti-O-P-C-H:
R. Luschtinetz, J. Frenzel, T. Milek, and G. Seifert, *Adsorption of phosphonic acid at the TiO2 anatase (101) and rutile (110) surface*,  `Journal of Physical Chemistry C 113, 5730 (2009) <https://doi.org/10.1021/jp8110343>`__


DFTB.org
========

For detailed information please visit the official DFTB webpage:  `www.dftb.org <http://www.dftb.org/parameters/>`__. Detailed references of each specific parameter set are available in the corresponding *metainfo.yaml* file.


Extended tight-binding (xTB)
****************************

S.\  Grimme, C. Bannwarth, P. Shushkov, *A Robust and Accurate Tight-Binding Quantum Chemical Method for Structures, Vibrational Frequencies, and Noncovalent Interactions of Large Molecular Systems Parametrized for All spd-Block Elements (Z = 1-86)*, `J. Chem. Theory Comput., 2017, 13 (5), pp 1989–2009 <https://doi.org/10.1021/acs.jctc.7b00118>`__


External programs and Libraries
*******************************

`Click here <../Ref_third_party/index.html>`_ for the list of programs and/or libraries used in the AMS package.
On some platforms optimized libraries have been used and/or vendor specific MPI implementations.
