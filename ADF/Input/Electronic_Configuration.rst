.. index:: electronic configuration 

Electronic Configuration
************************

The next few keys can be used to specify the electronic configuration. If you don't specify any such keys, certain defaults will apply. In principle, the program will (by default) attempt to find the lowest-energy spin-restricted (one-determinant) state. If SCF convergence is problematic the program may wind up at an excited state, by which (in this context) we mean a one-determinant state with a higher energy than some other one-determinant state with the same net spin polarization. In worse cases the program may fail to converge to any state at all. It is good practice to *always* verify which configuration you actually have computed. 

When you specify a particular configuration and/or net charge and/or net spin-polarization of the system, the program will try to compute accordingly, even if the requested configuration has no physical or chemical meaning. The program has no knowledge about the existence of materials and will simply try to carry out what you tell it to do. 

.. index:: spin 

Charge and Spin
===============

.. _UNRESTRICTED: 
.. index:: unrestricted calculation 
.. index:: spin-polarized calculation 

Spin: restricted vs. unrestricted
---------------------------------

.. scmautodoc:: adf Unrestricted

.. scmautodoc:: adf SpinPolarization

In an ``unrestricted`` calculation spin-:math:`\alpha` and spin-:math:`\beta` MOs may be spatially different and may have different occupation numbers.
In the case of Spin-Orbit coupling, it means that Kramer's symmetry does not have to be satisfied, in which case the key ``UNRESTRICTED`` should be used in combination with the subkey ``SpinOrbitMagnetization NONCOLLINEAR`` or ``SpinOrbitMagnetization COLLINEAR`` of the key ``Relativity``. 

The unrestricted mode roughly doubles the computational effort. The actual numbers of spin-:math:`\alpha` and spin-:math:`\beta` electrons respectively are controlled by the keys ``SpinPolarization`` and :ref:`OCCUPATIONS<keyscheme OCCUPATIONS>`. Note carefully, that using *only* the keyword ``unrestricted``, without either ``SpinPolarization`` or ``Occupations`` (or both) will not result in any spin polarization. This implies that you would effectively perform a spin-restricted calculation, but with increased computational effort. Therefore, the program will check that in an unrestricted calculation at least one of the keys ``SpinPolarization`` or ``Occupations`` is applied. 

The unrestricted feature is equivalent, in *ab-initio* terminology, to (Spin-)Unrestricted-Hartree-Fock (UHF); the N-particle wave function is a single determinant and not necessarily an eigenfunction of the spin operator S\ :sup:`2` . 

A *restricted* calculation implies that the (spatial) orbitals *and* the occupation numbers are identical for spin-:math:`\alpha` and spin-:math:`\beta`. 

An unrestricted calculation with ``SpinPolarization 0.0`` (for instance by not specifying the spin polarization at all) is, in case one does not break the spin symmetry, in fact a restricted run: it should give exactly the same as the restricted calculation, but it will use more CPU time. If one does break the spin symmetry, for example with the key ``MODIFYSTARTPOTENTIAL`` or the ``SPINFLIP`` option in the key :ref:`RESTART<keyscheme RESTART>`, the solution may also be a broken spin symmetry solution. For example one may want to start a calculation in broken symmetry with spin-:math:`\alpha` density on one fragment and spin-:math:`\beta` density on another, e.g. in a spin-unrestricted calculation of H\ :sub:`2`  at large separation. 

The Fock operator, both in an unrestricted and in a restricted run, commutes with the spin operator Sz, but not (unless accidentally) with S\ :sup:`2` . The obtained one-determinant wave function may for instance be a mixture of a singlet and a triplet state. 

In an unrestricted calculation the expectation value of S\ :sup:`2`  is computed in ADF (note 29 in ref. [#ref1]_). The implementation of an evaluation of S\ :sup:`2`  is not quite trivial. DFT is essentially a one-particle formalism, so the S-operator for the n-particle system has to be written out in single-particle operators [#ref2]_. The equations used in ADF to calculate the expectation value of S\ :sup:`2`  can be found in Szabo and Ostlund [#ref3]_. Note that the so called exact value (S\ :sub:`exact` )\ :sup:`2` , which is printed in the ADF output, is defined as (S\ :sub:`exact` )\ :sup:`2`  = (\|N\ :sub:`a` - N\ :sub:`b` \|/2)(\|N\ :sub:`a` - N\ :sub:`b` \|/2+1), where N\ :sub:`a`  and N\ :sub:`b`  are the number of spin-:math:`\alpha` and spin-:math:`\beta` electrons, respectively. The expectation value of S\ :sup:`2`  is not calculated in a Spin-Orbit coupled calculation. 

If one includes the :ref:`UNRESTRICTEDFRAGMENTS<keyscheme UNRESTRICTEDFRAGMENTS>` key, molecules that have been calculated using the spin-unrestricted formalism can be employed as fragments. In this case, the calculation on the full complex also needs to use the spin-unrestricted formalism.
See also the examples :ref:`example EDA_Unr_CH3I` and :ref:`example EDA_Unr_C2H4_Cu_C2H4`.

A fair approximation to a computation with spin-unrestricted fragments can be achieved with the key :ref:`FRAGOCCUPATIONS<keyscheme FRAGOCCUPATIONS>`, which uses spin restricted fragments, but allows for spin-unrestricted fragment occupations.  See also the examples :ref:`example UnrFrag_H2`, :ref:`example EDA_meta_gga_hybrid` and :ref:`example PCCP_Unr_BondEnergy`.

.. index:: collinear 
.. index:: non-collinear 
.. _COLLINEAR: 

Unrestricted and Spin-Orbit Coupling
------------------------------------

In the case of Spin-Orbit coupling there are two ways to do spin-polarized calculations, either using the collinear approximation or the noncollinear approximation [#ref4]_ [#ref5]_. Using the unrestricted feature in order to assign different numbers of electrons to a and b spin, respectively, cannot be applied as such, if one includes Spin-Orbit coupling, since the electrons are not directly associated with spin-:math:`\alpha` and spin-:math:`\beta`. For the collinear and noncollinear approximation one should use ``Symmetry NOSYM`` (see :ref:`Symmetry key <adf-key-symmetry>`), and each level can allocate 1 electron. One should not specify the spin-polarization. 

**Collinear approximation**

::

   Unrestricted Yes
   Symmetry NOSYM
   Relativity
      Level Spin-Orbit
      SpinOrbitMagnetization COLLINEAR
   End

The ``SpinOrbitMagnetization`` key is only relevant in the case of Spin-Orbit coupling.

In the collinear approximation in each point in space the spin-polarization has the same direction (default is in the direction of the z-axis). Kramer's symmetry does not have to be satisfied. Symmetry used in the calculation should be NOSYM. The default direction of the spin-polarization can be overruled using as argument ``COLLINEARX`` for spin-polarization only in the direction of the x-axis, or as argument ``COLLINEARY`` for spin-polarization only in the direction of the y-axis.

**Noncollinear approximation**

::

   Unrestricted Yes
   Symmetry NOSYM
   Relativity
      Level Spin-Orbit
      SpinOrbitMagnetization NONCOLLINEAR
   End

In the noncollinear approximation in each point in space the spin-polarization can have a different direction. Kramer's symmetry does not have to be satisfied. Symmetry used in the calculation should be NOSYM. 


.. _keyscheme CHARGE:

Net Charge
----------

The net charge of the molecule can be controlled with the key CHARGE in the `System block in the AMS part of the input <../../AMS/System.html>`__:

.. scmautodoc:: ams System Charge
   :noref:
   :skipblockdescription:



.. _keyscheme OCCUPATIONS: 

Orbital occupations: electronic configuration, excited states
=============================================================

With the keys ``OCCUPATIONS`` and ``IRREPOCCUPATIONS`` you can specify in detail the assignment of electrons to MOs 

.. index:: smeared occupations 
.. index:: electron smearing 

.. _ElectronSmearing:

Aufbau, smearing, freezing
--------------------------

::

   OCCUPATIONS Options

``Options``
   May contain IntegerAufbau, Keeporbitals, ElectronicTemperature, Smear, Freeze, or Steep: 

   ``IntegerAufbau``
      Electrons are assigned to MOs according to the Aufbau principle, trying to use integer occupations, also in case of degeneracy at the Fermi level. ADF normally may use fractional occupation numbers in that case. Note that for multi-dimensional irreps, using the subkey IntegerAufbau may still not prevent fractional occupation numers to be used.

   ``Keeporbitals=NKeep``
      Until SCF cycle Nkeep electrons are assigned to MOs according to the Aufbau principle, using at each cycle the then current orbital energies of the MOs. Thereafter the KeepOrbitals feature is applied. As soon as this is activated the program will on successive SCF cycles assign electrons to the MOs that maximally resemble - in spatial form - those that were occupied in a 'reference cycle number'. The default for Nkeep is 20, except: 

      a) When orbital occupations for MOs are specified explicitly in the data block of the occupations key, these apply throughout. 

      b) In a Create run fixed occupations are derived from a database in the program. 

      c) When electron smearing is explicitly turned on by the user (see the Smear option below) Nkeep is by default 1,000,000 so the program will 'never' compare the spatial forms of MOs to determine the occupation numbers. The 'reference cycle number' is by default the previous cycle, which will suppress jumps in the spatial occupations during the SCF development while at the other hand allowing the system to let the more-or-less-frozen configuration relax to self-consistency. 

   ``Freeze``
      Occurrence of this word in the option list specifies that the 'reference cycle number' will be the cycle number on which the KeepOrbitals feature is activated: during all subsequent SCF cycles the program will assign electrons to MOs that resemble the MOs of that specific SCF cycle. This may be used when the MOs of that cycle are already reasonably close to the final ones, and it will suppress unwanted step-by-step charge-transfers from occupied to empty orbitals that are very close in energy. By default this option is not active. 

   ``ElectronicTemperature=T``
      Invokes orbital population using the Fermi-Dirac distribution with temperature ``T`` (in Kelvin). This may be used to achieve SCF convergence in an otherwise problematically converging system. Note that the default SCF acceleration method A-DIIS is not compatible with non-aufbau orbital occupations so it is disabled automatically and the classical Pulay DIIS scheme is used. For this reason it is strongly recommended to use either MESA or one of the methods from the LIST family in combination with ``ElectronicTemperature`` or ``Smear``.

   ``Smear=Smear1[,Smear2,Smear3,...,Smear10]``
      Another form of specifying the electronic temperature (in Hartree). The smearing parameter Smear\ *N* is related to the ``ElectronicTemperature`` in such a way that the occupation number for any orbital outside the smearing interval will deviate from an integer value (0 and 1 for spin-unrestricted, 0 and 2 for spin-restricted) by no more than 1% (0.01 electron for spin-unrestricted, 0.02 for spin-restricted). More precisely, a smearing value of 1 Hartree is equivalent to an electronic temperature of 34285 Kelvin. When a comma-delimited list of values is specified, the next value from the list is picked after SCF has converged, and the SCF is continued. This way one can specify a list of gradually decreasing values  to get sort of annealing effect. NOTE: No spaces are allowed when specifying the list of values for Smear. 

   ``Steep=Lambda[,Nmax]``
      The occupation number for each orbitals are updated according to steepest-descent  method (Ref: F. W. Averill and G. S. Painter, Phys. Rev. B **46**, 2498 (1992)).  During an SCF cycle, the occupation number for each new orbital is initially  determined by decomposing the old charge density with new orbitals. Then, the  occupation numbers are modified so that the total energy of the system will decrease.  The Lambda parameter gives the coefficient for the charge transfer in 1/au unit. The second parameter, Nmax, is an additional limit for the amount of the charge transfer. Nmax would be useful for early steps of cycle when the Lambda parameter gives too large charge transfer. Too small Nmax results in irregular behavior in SCF convergence. In the case of difficult SCF convergence, you should make mixing and Lambda smaller. From our experience, Nmax=0.1 or 0.2 is usually OK.  This method should be used with turning off DIIS method (DIIS N=0), and the choice of the mixing parameter in SCF cycle is also important. This option is especially useful for systems with many quasi-degenerate orbitals around Fermi level. For instance, cluster models of surface systems usually suffer from dangling bonds and should be converged with this method. Note though that slow convergence is an intrinsic feature of this method so one should specify a large limit for the number  of SCF cycles, say 500 or even 1000, depending on the cluster size. 

   ``OptimizeSpin=Delta``, ``OptimizeSpinRound=Delta``
      The spin polarization can be optimized by minimizing the difference between Fermi level values for spin-alpha and spin-beta MOs. This method works reliably only when a reasonably large finite electron temperature is used (300K is found to be sufficiently large for small transition metal clusters). The polarization value is optimized up to a specified tolerance Delta (fractional values are allowed) by step-wise reduction of the root-bracketing interval for the objective function f=FermiLevel(alpha)-FermiLevel(beta). The SCF procedure is converged for each spin polarization. When the interval becomes smaller than Delta the optimization is considered converged. After that the SCF may optionally be repeated with the spin polarization set to the nearest even or odd number (depending on the total number of electrons in the system) or, in other words, with the total number of electrons per spin rounded to the nearest integer. The method is invoked using either the OptimizeSpin or the OptimizeSpinRound Occupation option. As mentioned above, it must be used together with the ElectronicTemperature option.  The OptimizeSpin and OptimizeSpinRound argument specifies the tolerance value. The OptimizeSpinRound option specifies that after polarization has converged the SCF must be completed with the total number of electrons per spin rounded to the nearest integer. It should be noted that, as usual, the Unrestricted and Charge keys must be specified as for any other spin-unrestricted calculation. The second argument of the Charge key sets the initial spin polarization value from which the optimization is started. The result of the optimization may depend on the initial value because the objective function may have more than one root.

Notes about the occupations options: 

+ When occupation numbers are explicitly defined via the block ``IRREPOCCUPATIONS`` (see next section), the Smear option cannot be used.

+ The aufbau principle does not determine or adjust the distribution of electrons over spin-:math:`\alpha` versus spin-:math:`\beta` in an unrestricted calculation. This aspect is controlled by the key ``SpinPolarization`` and by any explicit occupations in the data block of occupations.

+ Smearing cannot be used in combination with the keeporbitals option. 

.. _keyscheme IRREPOCCUPATIONS: 

Explicit occupation numbers
---------------------------

::

   IrrepOccupations
     irrep orbitalnumbers
     irrep orbitalnumbers
     ...
   End

``irrep``
   The name of one of the irreducible representations (not a subspecies) of the point group of the system. See the  :ref:`appendix symmetry` for the irrep names as they are used in ADF. 

``orbitalnumbers``
   A series of one or more numbers: the occupation numbers for one-electron *valence* orbitals in that irrep. The orbitals are ordered according to their energy eigenvalue; higher states than those listed get an occupation number zero. 

   For degenerate representations such as the 2-dimensional E-representations or the 3-dimensional T-representations, you must give the *total* occupation, i.e. the sum over the partner representations; ADF assigns each partner an occupation equal to the appropriate fraction of what appears here. 

   In an unrestricted calculation, two sequences of numbers must be specified for each irrep; the sequences are separated by a double slash (//). The first set of numbers is assigned to the spin-:math:`\alpha` orbitals, the second set to the spin-:math:`\beta` orbitals. Example unrestricted calculation in symmetry NOSYM with two unpaired electrons: 

   ::

      IrrepOccupations
         A 28 // 26
      End
      SpinPolarization 2
      Symmetry NOSYM

   Note that this is not meaningful in an unrestricted Spin-Orbit coupled calculation using the (non-)collinear approximation, where one should use one sequence of occupation numbers for each irrep. 

Notes about the occupations data block: 

+  When specifying electron configurations, all valence electrons in the calculation must be explicitly assigned to MOs and the IRREPOCCUPATIONS keyword must be used. In this context the concept *valence electrons* and hence *valence orbitals* is not necessarily identical to what you may normally assume to be the valence space of an atom or molecule. The meaning of *valence* is here strictly defined as whatever electrons are outside the frozen core. It depends therefore on the level of frozen core approximation applied in the calculation. This traces back to the Create runs in which the basic atoms were generated that are now used to build the molecule.

+ When for some irrep there is a rather long list of occupation numbers, corresponding to *  consecutive fully occupied* states, you can combine these numbers and enter their sum instead: ADF knows the maximum occupation for an irrep, and when you put a larger number the program will split it up. For instance, if you give for the *p*-representation (in a single atom calculation)::

   P 17 3 

  ADF will interpret this as::

   P 6 6 5 3 

  i.e. the occupation number 17 is interpreted as denoting two fully occupied p-shells and the remaining five electrons in the next higher shell. This example also illustrates how to specify an excited state: here we have defined a hole in the third p-shell.

+ Fractional occupation numbers in input are allowed. For a discussion of the interpretation of fractional occupation numbers see ref. [#ref6]_. The program even allows you (technically) to use a non-integer total number of electrons, whatever the physical meaning of such a calculation is.

+ The data block of occupations is not parsed (see the section :ref:`input parsing`). The program does not replace expressions by their value and it does not recognize constants or functions defined with the define key.

+ In a numerical frequencies run (without symmetric displacements) the symmetry used internally in the program is NOSYM, irrespective of any Schönfliess symbol in the input file. As a consequence the program will recognize only the A representation (the only irrep in nosym), but not the representations belonging to the input point group symmetry. (The symmetry in the equilibrium geometry, defined by the input Schönfliess symbol, is used to enhance efficiency and stability in the construction of the matrix of Force constants). 


CHARGE and SPINPOLARIZATION vs. IRREPOCCUPATIONS
------------------------------------------------

The contents of the data block of IRREPOCCUPATIONS, if used, defines the total number of valence electrons and hence the net total charge. In an unrestricted run it also defines the net spin polarization. If the keys ``CHARGE`` and ``SPINPOLARIZATION`` are also used, the program will check that the specifications are consistent. 

We strongly recommend to employ this and always specify the net total charge and spin polarization with charge whenever explicit occupation numbers are supplied with IRREPOCCUPATIONS, to that the program will check that your occupation numbers result in the total charge and spin polarization that you have in mind. 


Create mode
-----------

In Create mode occupation numbers are predefined (see Appendix :ref:`periodic table`), and these are applied unless you specify occupations in input yourself. Conceivably this may result in a non-aufbau configuration. In Create mode the program always operates as if the occupations were set in input. 


.. _frozen core:

Frozen core approximation
=========================

**Frozen core vs. pseudopotentials**

.. index:: pseudopotentials 

Pseudopotentials are not supported. The frozen core approximation is automatic in a normal (Fragment mode) calculation and is defined by the basic atomic fragments. The data file used in the Create run specifies the frozen core for the atom, which is then used in all molecules that incorporate that atomic fragment. 

**Core Potentials**

.. index:: core potential 

In the standard approach the Coulomb potential and the charge density due to the atomic frozen core are computed from the frozen one-electron orbitals. ADF stores the computed core density and core potential for each atom type in the molecule on a file TAPE12. Alternatively, you may attach a file with (core) potentials and densities. The file must have the same structure as the standard TAPE12. It should contain one or more sections, each with the core information for one type of atom. With the block COREPOTENTIALS you specify the core file and (optionally) which sections pertain to the distinct atom types in the molecule.

.. _keyscheme COREPOTENTIALS: 

::

   COREPOTENTIALS corefile
     {atomtype index}
     {atomtype index}
     ...
   end

``corefile``
   The file with core potentials and charge densities. The name may contain a path. 

``atomtype``
   One of the atom type names as defined by atoms. 

``index``
   Points to the core section on the attached file that applies to the atom type. Different atom types may use the same section. A non-positive index tells the program that the atoms of that type don't have a frozen core. If the information on the corresponding fragment file (or data file in Create mode) indicates the contrary the program will abort with an error message. 

If the key is used as a simple key (specifying only the core file) the sections on the file are associated with the atom types in order: the first section is used for the first atom type, et cetera. This is overruled by applying the block form. However, since the key *must* have the core file as argument, the block form requires that you apply the continuation symbol: an ampersand (), separated from the core file name by at least one blank. 

If you omit an atom type from the data block it gets a zero index (no core). 

The attached file may contain more sections than used in the calculation, and the indices specified in the data block don't have to be in ascending order, consecutive, or cover a specific interval. 

When a file with non-standard (e.g. relativistic) cores is attached and used in the calculation of an atom or molecule, and the result is used as fragment in a subsequent calculation, you should attach and use the same core potentials again. Otherwise, the program will internally compute the standard core potentials and hence implicitly employ another fragment than you may think, i.e. a fragment with other properties. ADF will not check anything in this respect and corepotentials should therefore be handled with great care. 

The primary application of the corepotentials option is to include (scalar) relativistic corrections in the (frozen core part of the) Fock operator. The relativistic core potentials can be computed with the auxiliary program dirac (see the RELATIVITY keyword). 


Spin-polarized start-up potential
=================================

The Fock matrix for the first SCF cycle is built by combining the Fock matrices from the fragment files. When performing a :ref:`Restart <keyscheme RESTART>`, the initial Fock Matrix may be read from the specified ``adf.rkf`` file.

.. index:: spin-flip broken symmetry 
.. _spin flip broken symmetry:


Spin-flip method for broken symmetries
--------------------------------------

It is possible to exchange alpha and beta electrons for selected atoms when performing a restart from a previous spin-unrestricted calculation.  

In many cases, one wishes to perform a calculation of a low-spin complex  where spin-density is positive on some atoms and negative on the others. It is  usually very difficult to achieve SCF convergence if one starts from scratch.  Sometimes, the ``ModifyStartPotential`` feature (see next section) helps with this problem but sometimes  it does not. A more robust way is to first perform a high-spin calculation and then modify the resulting adf.rkf file by "flipping" the spin on some atoms. This file then  can be used to restart a subsequent low-spin calculation. 

Such a "flipping" can be performed during restart by specifying the ``SpinFlip`` keyword in the :ref:`Restart <keyscheme RESTART>` input block as shown below: 

.. _keyscheme SPINFLIP: 

::

   Restart 
      File HighSpin.results/adf.rkf
      ! SpinFlip keyword is followed by the indices of the 
      ! atoms for which the flipping will be performed
      SpinFlip 1
   End

.. seealso::

   The example :ref:`Broken spin-symmetry: Fe4S4<example Fe4S4_BrokenSymm>` and the AMS-GUI tutorial `Spin Coupling in Fe4S4 Cluster <../../Tutorials/ElectronicStructureModelHamiltonians/SpinCouplingInFe4S4Cluster.html>`__ demonstrate the use of the spin-flip option.


Modify the starting potential
-----------------------------

In some applications you may want to modify the initial potential (from the restart file or the fragment files), see also the previous section. This is achieved with the block ``ModifyStartPotential``. It allows you to scale the potential as to represent user-chosen amounts of spin-:math:`\alpha` and spin-:math:`\beta` density on some or all of the fragments. This will adjust the spin-:math:`\alpha` and spin-:math:`\beta` initial potentials. 

This option applies only to *unrestricted* calculations of course. It may be used to help the program find a particular state. This might, for instance, be hard to find otherwise due to the a-b symmetry in the start-up situation. It may also be useful to speed up the SCF convergence in case you know what the final distribution of spin-:math:`\alpha` and spin-:math:`\beta` density over the molecule will approximately be. 

.. _keyscheme MODIFYSTARTPOTENTIAL: 

::

   ModifyStartPotential {specification}
   { frag alfa // beta
    frag alfa // beta
    ...}
   end


``specification``
   Must be *two numbers*, ASPIN and BSPIN, if provided at all. They specify the (relative) amounts of spin-:math:`\alpha` and spin-:math:`\beta` fit density to define the spin-dependent potential at the first SCF cycle. The coefficients retrieved from the fragment files (or from the restart file in case of a SCF restart) are scaled accordingly. This will not affect the *total* amount of fit density: the absolute values of ASPIN and BSPIN play no role, only their ratio. In case of a restart run the restart file must have been generated in a *restricted* calculation, while the continuation run must be an *unrestricted* one. 

If no argument is given a data block must be supplied with records frag alfa // beta. This is very much similar to the main option with ASPIN and BSPIN: you specify ASPIN and BSPIN now separately for each fragment. This involves somewhat more input but increases the possibilities to tune the initial potential. Again this can be applied only in an unrestricted calculation. It cannot be used in a restart: the affected fit coefficients are those from the fragment files, while in an SCF restart run these are ignored and replaced by the coefficients on the adf.rkf (TAPE21) restart file. 

Each line specifies a frag with its corresponding ASPIN and BSPIN fit partitioning. If frag is the name of a fragment *type*, the specified ASPIN-BSPIN is applied to all individual fragments of that type. Alternatively an *individual* fragment can be specified, using the format fragtype/n, where *n* is an index between one and the total number of fragments of that type. In such a case the ASPIN-BSPIN data applies only to that particular fragment while different values may be supplied for the other fragments of the same type. 

It is allowed to specify for certain fragment types individual fragments and for other fragment types only the type. Duplicate specifications are not allowed; an individual fragment must not be specified if its fragment type is also specified as a whole. If the data block form is used, only the fit coefficients of the referenced fragments are affected. For the not-referenced fragments the fit densities are used as they are defined on the corresponding fragment files. 

The SCF convergence of a spin-unrestricted calculation usually improves when you start with potentials that correspond to the correct ratio of spin-:math:`\alpha` and spin-:math:`\beta` electrons. By default ASPIN=BSPIN=0.5, as implied by the spin-restricted start density of the fragments or restricted molecule.  

The total amount of fit density used on the first iteration is defined by the sum-of-fragment densities (or the density on the restart file). This may be different from the total nr. of electrons in the actual calculation. On the second SCF cycle the fit density will internally be normalized so as to represent the correct number of electrons. 

.. index:: broken symmetry 

The block-form of the key makes the start up of broken symmetry calculations easy. For example one may want to start a calculation in broken symmetry with spin-:math:`\alpha` density on one fragment and spin-:math:`\beta` density on another, e.g. in a spin-unrestricted calculation of H\ :sub:`2`  at large separation. It is particularly useful for larger systems, e.g. for magnetic coupling between spin-polarized magnetic centers, as in Fe-S complexes [#ref7]_: start with oppositely polarized Fe centers, but with, for instance, the remaining bridge and terminal ligands unpolarized. 

.. seealso::

   The example :ref:`Localized Hole: N2+ <example ModStPot_N2+>` demonstrates the use of the ``ModifyStartPotential`` option.


.. index:: unrestricted fragments 

Unrestricted fragments
======================

In ADF you can use spin-unrestricted fragments if the key UNRESTRICTEDFRAGMENTS is used.

.. _keyscheme UNRESTRICTEDFRAGMENTS: 

::

   UNRESTRICTEDFRAGMENTS
   UNRESTRICTED

If spin-unrestricted fragments are used the full complex must also be calculated spin-unrestricted, which means
that the key UNRESTRICTED is required, and in addition the SPINPOLARIZATION key and/or the IRREPOCCUPATIONS block key must be included.
The key FRAGOCCUPATIONS should not be included.
The spin-:math:`\alpha` and spin-:math:`\beta` occupations are read from the spin-unrestricted fragment files.
For spin-restricted fragments the spin-:math:`\alpha` and spin-:math:`\beta` occupations will be set equal and sum up to the spin-restricted occupation numbers.

The unrestricted fragments can be self-consistent: different numbers of spin-:math:`\alpha` and spin-:math:`\beta` electrons usually result in different spatial orbitals and different energy eigenvalues for spin-:math:`\alpha` and spin-:math:`\beta` when you go to self-consistency.

Prepared for bonding
--------------------

Typically an unrestricted electron configuration for the fragments is used, such that the Pauli repulsion between the fragments is minimal, which means that the fragments are
so called 'prepared for bonding'.
For example if one has two fragments which both have one unpaired electron, one would put the unpaired electron of the first fragment in the spin-:math:`\alpha` orbital and the unpaired electron of the second fragment in the spin-:math:`\beta` orbital.
If one wants to calculate separately the electron pair bonding see key :ref:`REMOVEALLFRAGVIRTUALS<keyscheme REMOVEALLFRAGVIRTUALS>`.

Simulated unrestricted fragments with key FRAGOCCUPATIONS
=========================================================

In the method that simulates unrestricted fragments with the key FRAGOCCUPATIONS, the fragments from which the molecule is built must be spin-restricted, that is: the fragment files must be result files of spin-restricted calculations. For purposes of analysis, however, it may be desirable in some applications to build your molecule from fragments that have an *un*\ restricted electronic configuration. This can be simulated as follows. 

You tell ADF that you want to *treat* the fragments as if they were unrestricted; this causes the program to duplicate the one-electron orbitals of the fragment: one set for spin-:math:`\alpha` and one set for spin-:math:`\beta`. You can then specify occupation numbers for these spin-unrestricted fragments, and occupy spin-:math:`\alpha` orbitals differently from spin-:math:`\beta` orbitals. 

Of course, the unrestricted fragments that you use in this way, are not self-consistent: different numbers of spin-:math:`\alpha` and spin-:math:`\beta` electrons usually result in different spatial orbitals and different energy eigenvalues for spin-:math:`\alpha` and spin-:math:`\beta` when you go to self-consistency, while here you have spatially identical fragment orbitals. Nevertheless it is often a fair approximation which gives you a considerable extension of analysis possibilities. 

Prepared for bonding
--------------------

Typically an unrestricted electron configuration for the fragments is used, such that the Pauli repulsion between the fragments is minimal, which means that the fragments are
so called 'prepared for bonding'.
For example if one has two fragments which both have one unpaired electron, one would put the unpaired electron of the first fragment in the spin-:math:`\alpha` orbital and the unpaired electron of the second fragment in the spin-:math:`\beta` orbital.
If one wants to calculate separately the electron pair bonding see key :ref:`REMOVEALLFRAGVIRTUALS<keyscheme REMOVEALLFRAGVIRTUALS>`.

FRAGOCCUPATIONS
---------------

.. _keyscheme FRAGOCCUPATIONS: 


::

   FRAGOCCUPATIONS
    fragtype
      irrep spin-a // spin-b
      irrep spin-a // spin-b
      ...
    subend
    fragtype
      irrep spin-a // spin-b
      ...
    subend
   end

``fragtype``
   One of the fragment types and functions as a (block type) subkey. The data block for the subkey ends with the standard end code for block type subkeys (subend). 

``irrep``
   One of the irreducible representations (irreps) for the point group symmetry that was used in the computation of that fragment. 

``spin-a // spin-b``
   Two sequences of occupation numbers, which will be applied to the spin-:math:`\alpha` and spin-:math:`\beta` versions of the Fragment Orbitals. The sequences must be separated by a double slash (//).

The sum of spin-:math:`\alpha` and spin-:math:`\beta` occupations must, for each fragment orbital in each irrep separately, be equal to the total (restricted) occupation of that orbital as it is stored on the fragment file. In other words: you can only change the distribution over spin-:math:`\alpha` and spin-:math:`\beta` electrons within one orbital. 

(Without this restriction the spatial distribution of the total (sum over spins) fragment charge density would be changed, leading to an incorrect bonding energy analysis after the calculation). 

Be aware that in more-dimensional irreps (E, T) the number of electrons in a fully occupied orbital is input as the dimension of the irrep times the one-electron orbital occupation. Compare the key IRREPOCCUPATIONS. 

For irreps that are not mentioned in this input block, and hence for all irreps of fragment(type)s that are not mentioned at all, the spin-:math:`\alpha` and spin-:math:`\beta` occupations will be set equal, which is of course what they in fact are on the (restricted) fragment file. 

For an example of applying this option see ref. [#ref8]_. 

.. _REMOVEALLFRAGVIRTUALS:
.. index:: remove fragment orbitals 
.. index:: CSOV analysis 
.. index:: constrained space orbital variation 


Remove Fragment Orbitals 
========================

By default all fragment orbitals (the MOs of the fragment computation), which are stored on the fragment file, are used as basis functions for the overall molecule. You can remove one or more of these fragment orbitals from the basis set of the molecule.
This may be useful for special analyzes, like calculating the electron pair bonding in case one has open shell fragments, or
for instance to study the effect of deleting all virtual MOs of a particular fragment (CSOV analysis, Constrained Space Orbital Variation). It may also enhance the efficiency since you effectively reduce the size of the basis set, but you should be aware of the potential effects on the results. 

The pure orbital interaction effect of forming electron pair bonding between open shell molecules can approximately be calculated with a bond energy analysis in which all virtual orbitals are removed from the fragments, see Ref. [#ref9]_.
For calculating the effect of electron pair bonding best is to specify an unrestricted electron configuration for the fragments, such that the Pauli repulsion is minimal.
Removing of all virtuals from an open shell fragment, that is calculated spin-restricted, means that all fragment orbitals with zero occupation are removed.
Thus, for example, a singly occupied fragment orbital will not be removed. This singly occupied fragment orbital will result in a
spin-:math:`\alpha` and a spin-:math:`\beta` fragment orbital. In combination with other singly occupied fragment orbitals they may form an electron pair bonding combination, but also an anti-bonding combination.
In practice this means that the orbital interaction calculated with a bond energy analysis in which all virtual orbitals are removed from open shell fragments might be due to more than electron pair bonding.
The situation is not much different if one uses unrestricted fragments, because technically always the same number of alpha and beta orbitals must be removed,
and the removed orbitals must all have zero occupation.

If one wants to remove all virtual fragment orbitals use the key REMOVEALLFRAGVIRTUALS.


.. _keyscheme REMOVEALLFRAGVIRTUALS:

::

   REMOVEALLFRAGVIRTUALS

If one does not want to remove all virtual fragment orbitals then one should use the block key REMOVEFRAGORBITALS.

.. _keyscheme REMOVEFRAGORBITALS: 

::

   REMOVEFRAGORBITALS
    fragtype
      subspecies nremove
      subspecies nremove
      ...
    subend
    fragtype
      subspecies nremove
      ...
    subend
    ...
    (etc.)
    ...
   end

``fragtype``
   One of the fragment types in the system. Any subset of the available fragment types can be used here as subkey. The subkeys are block type keys; their data blocks end subend. 

``subspecies``
   One of the subspecies of the irreducible representations of the point group symmetry that was used in the calculation of the fragment itself. This requires of course that one knows the symmetry that has been used for the fragment calculation. 

``nremove``
   The number of fragment orbitals of the pertaining representation that will not be used as basis functions for the overall system. The *highest* (in energy eigenvalue) nremove orbitals are discarded. You must not remove *occupied* fragment orbitals. 

By default (omission of the key) all fragment orbitals are used in the basis set for the system. 

**Important Note** 

It is imperative that any removal of fragment orbitals will not break the symmetry of the molecule. This consideration is relevant when for instance two different subspecies of a fragment irrep contribute to different partner subspecies in one of the irreps of the molecule. In such a case, when one removes an orbital in such a fragment subspecies, its partner orbital should also be removed. If this is violated an error may occur or the results will simply be wrong. Quite likely, the program will detect the error, but this may occur only in the final (analysis) stage of the calculation so that a lot of CPU time may have been wasted. 

Example: consider a single-atom fragment, computed in atom symmetry, used as fragment in a c(lin) molecule and assume that the p:x and p:y fragment orbitals contribute to respectively the pi:x and pi:y subspecies of the molecule. Then, when you remove one or more p:x fragment orbitals, you should also remove the same number of p:y fragment orbitals. Practical cases may be more complicated and whenever you use this key, make sure that you've fully analyzed and understood how the fragment irreps combine into the molecular symmetry representations. Hint: run the molecule, without removing any fragment orbitals, and stop at an early stage after the program has computed and printed the build-up of the molecular SFOs from the fragment orbitals. To control early aborts via input, use the key STOPAFTER. 

.. _CDFT: 
.. _XCDFT: 
.. index:: CDFT
.. index:: constrained DFT

CDFT: Constrained Density Functional Theory
===========================================

CDFT is a tool for carrying out DFT calculations in the presence of a constraint. The nature of the constraint is general in theory, however, in the current implementation the user can constrain the CHARGEs or the SPINs of a set of moieties (as identified by sets of atoms) to be a specific real number given in input. 
Note that the use of CDFT as implemented in ADF is an **expert option**, and it is a **work in progress**.
Implemented in ADF by M. Pavanello and P. Ramos [#ref11]_, based on the method described in Ref. [#ref10]_.
At the moment SYMMETRY NOSYM and an all electron basis set are required.

The simplest way to run CDFT is using the following keyword combination

.. _keyscheme CDFT: 

::

  CDFT
    NCONSTRAINTS 1
    NATOMSPERSET N
    THEATOMS atom1 atom2 ... atomN
    CONSTRAINTS charge
  END

All the CDFT block key options are:

.. scmautodoc:: adf CDFT

.. only:: html

  .. rubric:: References


.. [#ref1] R.E. Bulo, A.W. Ehlers, S. Grimme and K. Lammertsma, *Vinylphosphirane.Phospholene Rearrangements: Pericyclic [1,3]-Sigmatropic Shifts or Not?* `Journal of the American Chemical Society 124, 13903 (2002) <https://doi.org/10.1021/ja027925u>`__ 

.. [#ref2] R.\  Pauncz, *Spin Eigenfunctions*, ISBN13: 9780306401411, 1979, New York: Plenum Press 

.. [#ref3] A.\  Szabo and N.S. Ostlund, *Modern Quantum Chemistry*, ISBN13: 9780070627390, 1st ed. revised ed. 1989: McGraw-Hill 

.. [#ref4] H.\  Eschrig and V.D.P. Servedio, *Relativistic density functional approach to open shells*, `Journal of Computational Chemistry 20, 23 (1999) <https://doi.org/10.1002/(SICI)1096-987X(19990115)20:1%3C23::AID-JCC5%3E3.0.CO;2-N>`__ 

.. [#ref5] C.\  van Wüllen, *Spin densities in two-component relativistic density functional calculations: Noncollinear versus collinear approach*, `Journal of Computational Chemistry 23, 779 (2002) <https://doi.org/10.1002/jcc.10043>`__ 

.. [#ref6] S.G. Wang and W.H.E. Schwarz, *Simulation of nondynamical correlation in density functional calculations by the optimized fractional orbital occupation approach: Application to the potential energy surfaces of* O\ :sub:`3` and SO\ :sub:`2`, `Journal of Chemical Physics 105, 4641 (1996) <https://doi.org/10.1063/1.472307>`__ 

.. [#ref7] L.\  Noodleman, and E.J. Baerends, *Electronic Structure, Magnetic Properties, ESR, and Optical Spectra for 2-Fe Ferredoxin Models by LCAO-Xa Valence Bond Theory*, `Journal of the American Chemical Society 106, 2316 (1984) <https://doi.org/10.1021/ja00320a017>`__ 

.. [#ref8] F.M. Bickelhaupt, N.M. Nibbering, E.M. van Wezenbeek and E.J. Baerends, *The Central Bond in the Three CN* Dimers NC_CN, CN-CN, and CN-NC: Electron Pair Bonding and Pauli Repulsion Effects*, `Journal of Physical Chemistry 96, 4864 (1992) <https://doi.org/10.1021/j100191a027>`__ 

.. [#ref9] F.M. Bickelhaupt, M. Solà, C. Fonseca Guerra, *Highly polar bonds and the meaning of covalency and ionicity -- structure and bonding of alkali metal hydride oligomers*, `Faraday Discussions 135, 451 (2007) <https://doi.org/10.1039/B606093E>`__ 

.. [#ref10] Q.\  Wu, T. Van Voorhis, *Direct optimization method to study constrained systems within density-functional theory*, `Physical Review A 72, 024502 (2005) <https://doi.org/10.1103/PhysRevA.72.024502>`__ 
.. [#ref11] P.\  Ramos, M. Pavanello, *Constrained subsystem density functional theory*, `Physical Chemistry Chemical Physics 18, 21172 (2016) <https://doi.org/10.1039/C6CP00528D>`__

.. [#ref12] P.\  Ramos, M. Pavanello, *Low-lying excited states by constrained DFT*, `Journal of Chemical Physics 148, 144103 (2018) <https://doi.org/10.1063/1.5018615>`__
