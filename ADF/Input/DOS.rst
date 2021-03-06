.. index:: dos module 
.. _DOS: 


Dos: Density of States
**********************

The auxiliary program *dos* computes various types of densities-of-states (DOS) for a user-specified energy interval. 

*dos* requires an ASCII input file where the user specifies the items to be calculated and computational details, plus the standard result file adf.rkf (TAPE21) from an *adf* calculation. The latter file must be present as a local file with name TAPE21 in the directory where *dos* is executed, or one can use the key adffile to point to the adf.rkf file,

*dos* produces as result one or more ASCII files with the density-of-states values. Error messages and computational info (if any) are written to standard output. 


Introduction
============

The program *dos* gives information on the number and character of one-electron levels (molecular orbitals) as a function of the (orbital) energy. The total density of states *N*(*E*) is a well known concept in electronic structure theory of infinite systems (crystals). *N*(*E*)*dE* denotes the number of one-electron levels (orbitals) in the infinitesimal energy interval *dE*. The total density of states (TDOS) at energy *E* is usually written as 

.. math:: 

   N(E) = \sum_i \delta(E-\epsilon_i)  \qquad (4.5.1)

where the :math:`\epsilon_i`  denote the one-electron energies. So the integral of :math:`N(E)` over an energy interval *E*\ :sub:`1`  to *E*\ :sub:`2`  gives the number of one-electron states in that interval. Usually the :math:`\delta`-functions are broadened to make a graphical representation possible. 

When the :math:`\delta`-functions are multiplied by a weight factor that describes some property of the one-electron state  :math:`\phi_i`  at energy :math:`\epsilon_i`  various types of densities-of-states are obtained that provide a graphical representation of the state character (orbital character) as a function of one-electron energy. 

In calculations on finite molecules the total density of states as a function of (orbital) energy may also be useful, but the main use of various types of densities-of-states is to provide a pictorial representation of Mulliken populations. The weight factors employed are related to the orbital character determined by means of a Mulliken population analysis *per orbital* (see below). The program *dos,* therefore, provides the same information as can be generated by the ADF program (a population analysis per orbital) but *dos* enables an easy graphical representation and is particularly useful when there are many one-electron levels, for instance in calculations on clusters. You can obtain a simple view of the character of the orbitals in a certain energy range. You can also find out in which orbitals (at which energies) certain basis functions or fragment orbitals give a large contribution, and whether such contributions are bonding, nonbonding or antibonding with respect to particular bonds. Such information is provided by *dos* in the form of (weighted) density of states values over a user-specified energy range, which can for instance be plotted by *gnuplot*. 

The following options are available for computations by *dos*: 

+ TDOS: Total Density of States

+ GPDOS: Gross Population Density of States

+ OPDOS: Overlap Population Density of States

+ PDOS: Projected Density of States

The total density of states (TDOS) has large values at energies where there are many states per energy interval. 

The GPDOS (Gross Population based Density Of States) of a function  :math:`\chi_\mu`  (or a sum of such functions) has large values at energies where this function (these functions) occur(s) in the molecular orbitals. 

The PDOS of a function :math:`\chi_\mu`  provides similar information, but with the projection of :math:`\chi_\mu`  onto the orbital :math:`\phi_i`  as weight factor for the importance of :math:`\chi_\mu`  in the orbital :math:`\phi_i` . 

The OPDOS (Overlap Population based Density Of States) between :math:`\chi_\mu`  and :math:`\chi_\nu`  has large positive values at energies where the interaction between them is bonding, and negative values where the interaction is anti-bonding. An example of the use of these plots is provided in  [#ref1]_. 

We review below the Mulliken population analysis, and then describe the forms of density of states analysis performed by DOS. Finally an input description of DOS is given. 


Mulliken population analysis
============================

The orbitals :math:`\phi_i`  with energies :math:`\epsilon_i`  are expanded in basis functions :math:`\chi_\mu` , which leads to the definition of density matrices :math:`P_i` describing orbital densities, from which the total density matrix can be constructed: 

.. math::
   
   \phi_i(r) = \sum_\mu \chi_\mu(r) C_{\mu i}

.. math::

         & \rho_i(r) = \int |\phi_i(r)|^2 = \sum_{\mu \nu} P_{i,\mu \nu} \chi_\mu(r) \chi_\nu(r)      \\
         &  P_{i,\mu \nu} = C_{\mu i} C_{\nu i} 

.. math:: 

         & \rho(r) = \sum_i n_i \rho_i(r) = \sum_{\mu \nu} P_{\mu \nu} \chi_\mu(r) \chi_\nu(r)      \\
         &  P_{i,\mu \nu} = \sum_i n_i C_{\mu i} C_{\nu i} \qquad (4.5.2) \\


Here :math:`\mu` and :math:`\mu` run over the basis functions, which may be either primitive functions, or combinations of primitive functions, for instance the SCF orbitals of atoms or larger fragments. 

The Mulliken population analysis provides a partitioning of either the total charge density or an orbital density. The total density is written as 

.. math::

      \rho(r) & = \sum_{\mu \nu} P_{\mu \nu} \chi_\mu(r) \chi_\nu(r) \\
              & = \sum_{A \leq B} \sum_{\mu \in A} \sum_{\nu \in B}  P_{\mu \nu} \chi_\mu(r) \chi_\nu(r) \\
              & = \sum_{A \leq B} \rho_{AB} \qquad (4.5.3a)

.. math:: 

   \rho_{AB} = \sum_{\mu \in A} \sum_{\nu \in B}  P_{\mu \nu} \chi_\mu(r) \chi_\nu(r) \qquad (4.5.3b)


The total number of electrons, :math:`N = \int \rho(r) dr`, is now partitioned over the atoms by assigning an overlap population :math:`P_{\mu \nu} S_{\mu \nu} + P_{\nu \mu} S_{\nu \mu}`  for one half to the atom *A* of  :math:`\chi_\mu`  and one half to atom *B* of :math:`\chi_\nu`,

.. math:: 

   N = \int \rho(r) dr = \sum_{\mu \nu}  P_{\mu \nu} S_{\mu \nu} = \sum_\mu GP_\mu \qquad (4.5.4a)


.. math:: 

   GP_\mu = \sum_\nu P_{\mu \nu} S_{\mu \nu} \qquad (4.5.4b)

:math:`GP_\mu` is the gross population of  :math:`\chi_\mu` . It contains the net population
:math:`P_{\mu \mu}` and half of each total overlap population :math:`P_{\mu \nu} S_{\mu \nu} + P_{\nu \mu} S_{\nu \mu}` between :math:`\chi_\mu` and :math:`\chi_\nu`.
Summing the gross population over the functions :math:`\mu \in A` yields the total number of electrons assigned to atom *A*, or the gross population of atom *A*, :math:`GP_A` , and hence the gross charge :math:`Q_A` of atom *A*, 

.. math::

   GP_A = \sum_{\mu \in A} GP_\mu \qquad (4.5.5a)

.. math::

   Q_A = Z_A - GP_A \qquad (4.5.5b)

The overlap population :math:`OP_{\mu \nu}` between two functions and the overlap population :math:`Q_{AB}` between two atoms are defined in an analogous manner, 

.. math::

   OP_{\mu \nu} = P_{\mu \nu} S_{\mu \nu} + P_{\nu \mu} S_{\nu \mu} \qquad (4.5.6a)

.. math::

   Q_{AB} =  \sum_{\mu \in A} \sum_{\nu \in B} OP_{\mu \nu} \qquad (4.5.6b)

These quantities can be evaluated for a single orbital density, :math:`N = 1 = \int |\phi_i(r)|^2 dr`. The gross population :math:`GP_{i,\mu}` of a function in a specific orbital density :math:`|\phi_i(r)|^2`  is then associated with the fraction of the orbital density belonging to that function (or the percentage :math:`\chi_\mu`  character of orbital :math:`\phi_i` , and the overlap population :math:`OP_{i, \mu \nu}` gives an indication of the strength of bonding or anti-bonding between :math:`\chi_\mu`  and :math:`\chi_\nu`  in orbital :math:`\phi_i` , 

.. math:: 

   GP_{i \mu} = \sum_\nu P_{i, \mu \nu} S_{\mu \nu} = \sum_\nu C_{\mu i} C_{\nu i} S_{\mu \nu} \qquad (4.5.7a) 


.. math:: 

   OP_{i, \mu \nu} = P_{i, \mu \nu} S_{\mu \nu} + P_{i, \nu \mu} S_{\nu \mu} = 2 C_{\mu i} C_{\nu i} S_{\mu \nu} \qquad (4.5.7b) 




Density of states analyses based on Mulliken population analysis
================================================================

**Total density of states** 

The total density of states TDOS at energy *E* is written as  

.. math::

   TDOS: N(E) = \sum_i \delta(E - \epsilon_i)

so the integral of :math:`N(E)` over an energy interval :math:`E_1` to :math:`E_2`  gives the number of one-electron states in that interval. In practice the delta functions are approximated by Lorentzians, 

.. math::
   
   TDOS: N(E) = \sum_i L(E-\epsilon_i) = \sum_i \left(  \frac{\sigma}{\pi} \frac{1}{(E-\epsilon_i)^2 + \sigma^2}  \right)


A plot of :math:`N(E)` versus :math:`E` reveals energetic regions where many levels are located. The width parameter s determines of course the appearance of the plot. A typical value is 0.25 eV (used as default in *dos*). 

**Partial (gross population and projected) density of states** 

In order to find out if a given function :math:`\chi_\mu`  contributes strongly to one-electron levels at certain energies, one may weigh a one-electron level with the percentage :math:`\chi_\mu`  character. We usually determine the :math:`\chi_\mu`  character by the gross populations, obtaining the GPDOS form of the partial density of states,  

.. math::

   GPDOS: N_\mu (E) = \sum_i GP_{i,\mu} L(E-\epsilon_i)

If the weight factor is determined by projection of :math:`\phi_i`  against :math:`\chi_\mu` , we obtain the projected density of states PDOS, 

.. math::

   PDOS: N_\mu (E) = \sum_i |\langle \chi_\mu | \phi_i \rangle|^2 L(E-\epsilon_i)


One should not use the PDOS for d-type or f-type primitive basis functions ('BAS'). A d-type function consists of 6 Cartesian functions, while there can of course be only 5 true d-type functions among them: one (linear combination) of them is in fact an s-type function (x2+y2+z2). Similarly, there are 10 f-type Cartesian functions, 3 of which are in fact p-functions.  The PDOS is calculated for the 6 d-type and 10 f-type Cartesian functions, which leads to undesired results. An PDOS for SFOs does not suffer from this problem. 

**Overlap population density of states (OPDOS)** 

If the delta function representing orbital :math:`\phi_i`  is weighed with the overlap population between :math:`\chi_\mu`  and :math:`\chi_\nu`  in :math:`\phi_i` , the overlap population density of states OPDOS is obtained, 

.. math::

   OPDOS: N_{\mu \nu} (E) = \sum_i OP_{i, \mu \nu} L(E-\epsilon_i)

If an orbital :math:`\phi_i`  at energy :math:`\epsilon_i`  is strongly bonding between :math:`\chi_\mu`  and :math:`\chi_\nu`  the overlap population is strongly positive and OPDOS(e) will be large and positive around :math:`E=\epsilon_i` . Similarly, OPDOS(E) will be negative around energy :math:`\epsilon_i`  when there is antibonding between :math:`\chi_\mu`  and :math:`\chi_\nu`  in :math:`\phi_i` . 

The OPDOS(E) has been used under the name coop (crystal orbital overlap population) in Extended-H??ckel solid state calculations by Hoffmann and coworkers [2]. 

[2] R. Hoffmann, *A chemist's view of bonding in extended structures* (VCH Publishers, New York, 1988). 


Generalizations of OPDOS, GPDOS, PDOS
=====================================

As observed above, the basis functions in the above expressions may be primitive basis functions ('Slater type orbitals'), but of course the formulas are equally applicable for other types of MO expansions. In *dos* the user may select either the expansion in primitive basis functions ('BAS') or the expansion in SFOs (Symmetrized Fragment Orbitals) for the DOS analyses.  

It is also possible in DOS to treat a *set* of basis functions simultaneously. For instance, the GPDOS for a set of basis functions :math:`\mu`\ :sub:`1` , :math:`\mu`\ :sub:`2` , ... is simply defined as the summation of the corresponding single-function GPDOS(E) values 


.. math:: 

   N_{\mu-set} (E) = \sum_{\mu \in \mu-set} \sum_i GP_{i,\mu} L(E-\epsilon_i)

In a similar fashion the OPDOS can be defined for *two sets* of basis functions :math:`\mu`\ :sub:`1` , :math:`\mu`\ :sub:`2` , ... and :math:`\nu`\ :sub:`1` , :math:`\nu`\ :sub:`2` , ... as 

.. math:: 

   N_{\mu-set, \nu-set} (E) = \sum_{\nu \in \nu-set} \sum_{\mu \in \mu-set} \sum_i OP_{i,\mu \nu} L(E-\epsilon_i)

and finally for the PDOS we get in similar fashion 

.. math::

   N_{\mu-set} (E) = \sum_{\mu \in \mu-set} \sum_i | \langle \chi_\mu | \phi_i \rangle |^2 L(E-\epsilon_i)


Input
=====

The (ASCII) input for *dos* is keyword oriented. Reading input by *dos* terminates whenever it finds a line END INPUT or the end-of-file, whichever comes first. 

Follows a list of keywords with their meaning. Generally keys may occur more than once and *the order in which they appear is relevant in some cases*. For instance the key energyrange (which defines for what energy values to compute densities-of-states, see below) applies to all items that come after it in input until the next occurrence of energyrange. 

.. _keyscheme dos: 


::

   $AMSBIN/dos << eor
   ADFFILE adffile
   ENERGYRANGE {Npoint=nr} {E-start=e1} {E-end=e2 / E-step=de}
   LORENTZIAN width=width
   FILE file
   TDOS { title }
   OPDOS ...
   GPDOS ...
   PDOS ...
   eor

**ADFFILE adffile**

::

   ADFFILE adffile

Specifies a (relative) path to an adf.rkf file. If not specified dos requires a file named TAPE21 in the current directory.


**Energy scan values**

::

   ENERGYRANGE {Npoint=nr} {E-start=e1} {E-end=e2 / E-step=de}

This specifies for which energy values the densities-of-states are computed that are specified *after* it in the input file and *until* the next occurrence of ENERGYRANGE. 

ENERGYRANGE specifies the lower bound, upper bound and number of equidistant energy values (including end-points). All items are optional with defaults applying for those omitted. 

The E end and E-step values determine one another and must therefore not be specified both (or be consistent). 

The initial defaults are: 

::

   nr=301
   e1=-20
   de=0.1

All energy data are in eV. 

When values have been changed with the key ENERGYVALUE, the so-modified values are the defaults for the next occurrence of ENERGYVALUE. 

**Peak widening**

The peaks in the DOS curves corresponding to the energies of the molecular orbitals are widened by a Lorentzian curve, the width of which can be adjusted. 

::

   LORENTZIAN width=width

Initial default width is 0.25 (eV). 

As for ENERGYRANGE, the key LORENTZIAN may occur more than once and each occurrence sets the width for all items after it. 

**Result files**

The computed densities-of-states are stored on one or more ASCII files, which have to be specified in input. 

::

   FILE file

The key FILE may occur any number of times in input. Each time it occurs the specified file is opened by *dos*. The file must not yet exist and the new file will accumulate (ASCII) the densities-of-states data of all DOS items subsequently specified, until the next occurrence of FILE. The first occurrence of the key FILE must be given before any DOS specification (by the keys TDOS, OPDOS, GPDOS, PDOS, see below). 

The format of the result file is such that it can be fed directly into *gnuplot*. 

**Densities of States**

Total density of states. 

::

   TDOS { title }

``TDOS``
   instructs the program to compute the total density of states.

``title`` (optional)
   will appear as title to the section of corresponding Density-of-States data in the result file.



The other types of densities-of-states require block-type keyword input. 


::

   OPDOS { title }
   Ftype numbers
   Ftype numbers
   ...
   *SUBEND*
   Ftype numbers
   Ftype numbers
   ...
   END


``Ftype``
   Specifies the type of basis functions to use in the MO expansions. If the primitive basis functions are to be used Ftype must be bas. For the SFO representation Ftype must be one of the irreducible representations of the point group symmetry. All Ftype values in the data block must be consistent: either all are bas or all are irrep labels. The scope of this consistency requirement is the data block of the current key: in a next OPDOS data block, for instance, a different choice may be made.

``numbers``
   Must be a sequence of integers referring to the basis functions to be selected, i.e. the '??-set' and '??-set' in (4.5.13) etc.
   If bas-type basis functions are selected the numbers refer to the overall list of all basis functions as printed in the output file of the adf run. If SFOs are selected the numbers refer to the SFO list of the pertaining symmetry representation without the core functions, see the adf output file.

``SUBEND``
   Must be typed as such and separates the '??-set' and the '??-set': all records before subend specify together the '??-set' and all records below subend comprise the '??-set'. Each of these two sections may consist of any number of records.







The input for GPDOS and PDOS are similar, but simpler because only one set of functions (':math:`\mu`-set') has to be specified, so there is no subend in the data blocks for these keys. 


::

   GPDOS { title }
   Ftype numbers
   Ftype numbers
   ...
   END


::

   PDOS { title }
   Ftype numbers
   Ftype numbers
   ...
   END

The keys GPDOS, OPDOS, PDOS and (TDOS) may occur any number of times in input and in any order. Each time the DOS key occurs the current energyrange and lorentzian settings apply and the results are written to the current file. 


.. only:: html

  .. rubric:: References

.. [#ref1] P.J. van den Hoek, E.J. Baerends, and R.A. van Santen, *Ethylene epoxidation on silver(110): the role of subsurface oxygen*, `Journal of Physical Chemistry 93, 6469 (1989) <https://doi.org/10.1021/j100354a038>`__ 
