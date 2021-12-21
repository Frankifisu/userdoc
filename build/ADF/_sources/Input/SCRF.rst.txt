.. _SCRF: 
.. index:: SCRF 


SCRF: Self-Consistent Reaction Field
====================================

The following sections describe the SCRF method and explain the related ADF input options. SCRF may not be available in the standard distribution on all platforms, contact SCM ( `support@scm.com <mailto:support@scm.com>`__) to request SCRF on your platform. 

**Introduction**

*by Donald Bashford, St. Jude Children's Research Hospital Memphis, updated October 26, 2011.* 

SCRF (Self-Consistent Reaction Field) is a method of accounting for the effect of a polarizable solvent (and optionally, a classical macromolecular system) on the quantum system.  Consider first the case with only a polarizable solvent. The solvent is modeled as a dielectric continuum with a dielectric constant, EPSSOL, that fills the space outside the quantum system.  The boundary between the interior (where the dielectric constant is unity) and the higher-dielectric exterior is the molecular surface, as defined by Connolly [#ref1]_.  The charges of the quantum system cause polarization of this continuum, giving rise to a reaction field which then acts back on the quantum system potentially altering its charge distribution.  The SCRF algorithm calculates the reaction field through solutions to the Poisson or Poisson--Boltzmann equation, and iteratively obtains self-consistency between the reaction field and charge distribution of the quantum system.  These ideas have their roots in Onsager's consideration of a dipole and a molecule with point-dipole polarizabilities inside a sphere [#ref2]_, and have also been developed in the Polarizable Continuum Model of Tomasi and co-workers [#ref3]_ [#ref4]_. The first use of these ideas in DFT calculations using ADF was by Chen et al. [#ref5]_  and Mouesca et al. [#ref6]_.  At around the same time the Tomasi group also used the PCM model with DFT [#ref7]_.  In the past, SCRF calculations with ADF were done in the research groups of Noodleman, Bashford and Case using custom modifications of ADF. Now the method is available in a standardized form.   

More recently, the ability to include a classical representation of a macromolecular environment, such as a protein around an enzyme active site, has been added to ADF.  In what follows, we refer to the macromolecule surrounding the QM system as 'the protein' for historical reasons.  It should be understood that the QM region and the protein region are distinct.  For example, if the QM region includes some protein sidechain moieties, these are part of the QM system, and **not** the protein. 

The protein exerts its effect in two ways: (1) The protein region can be assigned a dielectric constant (EPSPROT) that is different from either the QM region (1.0) or the solvent region (EPSSOL). This changes the reaction field that arises from the polarization of the environment by the charges of the QM atoms. (2) The protein has charges of it's own, which interact with the QM region in a way that is mediated by the complex dielectric environment described above. Calculations of this kind were first done by Li et al. [#ref8]_. 

The specific algorithm is: 

+ Solve for the electronic structure in vacuum by the usual QM methods.

+ Nucleus-centered partial charges are derived from the electronic structure   using a least-squares potential-fitting SVD algorithm [#ref6]_, which is somewhat similar to the CHELPG algorithm [#ref10]_.

+ *Only in calculations with a surrounding protein:* Calculate the electrostatic potential due to the partial charges of the protein in the three-dielectric environment defined by the protein and QM-region coordinates and radii.  We refer to this field as the 'protein field' :math:`\phi`\ :sub:`prot` . 

+ Using the nucleus-centered partial charges:

+ Solve the Poisson equation (or, if an ionic strength is specified, the Poisson-Boltzmann equation) for   :math:`\phi`\ :sub:`sol` , the electrostatic potential in the presence of the above-described solvent dielectric environment.   

+ Solve the Poisson equation for :math:`\phi`\ :sub:`vac` , the electrostatic potential in a uniform vacuum environment.   

+ The reaction field potential :math:`\phi`\ :sub:`rf`  is the    difference between these two potentials: :math:`\phi`\ :sub:`rf`  =    :math:`\phi`\ :sub:`sol`  - :math:`\phi`\ :sub:`vac` .   

+ Recalculate the electronic structure in the presence of the reaction field, and the protein field (if a protein field is present).  This is done by adding the potentials :math:`\phi`\ :sub:`rf`  (and possibly :math:`\phi`\ :sub:`prot` ) to the total potential evaluated   on the numerical integration grid when calculating Fock matrix elements.

+ Check changes in energy for convergence, and if not converged, return to step 4.  Note that because :math:`\phi`\ :sub:`prot`  does not depend on electronic structure in the QM region, there is no need to return to step 3. 

The algorithm also includes a correction for the small difference between the fit and true electron densities. 

At this time, the SCRF procedures are only available for single-point calculations.  No geometry optimization or frequency calculations can be done together with SCRF. 

Several user-settable options can affect the SCRF procedure. 

It is important the the QM calculation be done without use of molecular symmetry, as the finite-difference Poisson solver involves approximations that do not respect symmetry.  Therefore, one should specify SYMMETRY NOSYM in the general input. 

The choice of atomic radii and the probe radius determines the location of the dielectric boundary.  This molecular surface comprises spherical patches of the contact surface generated by a solvent-sized probe rolling over the atomic radii, the toroidal surfaces swept out as the probe roles in grooves between pairs of atoms, and the inverse spherical patches generated when the probe simultaneously touches three or more [#ref1]_ [#ref12]_.  In volumetric terms, the In volumetric terms, the molecular surface divides the space of all points that are accessible to any part of a probe sphere that cannot penetrate into any of the atomic spheres, for the space that is not accessible [#ref13]_.  The solvent accessible volume is assigned the solvent dielectric constant, while the inaccessible volume is assigned a dielectric constant of unity (the vacuum dielectric constant).  Smaller radii move the dielectric surface closer to the atomic nuclei which typically leads to stronger calculated solvent effects. 

The routine for calculating atomic partial charges chooses charges that best reproduce the potential outside the molecule that is generated by the nuclei and the electron density.  It sets up a grid of potential-sampling points in a region outside the molecule, calculates the potential on this grid due to the electron density and nuclei, and finds the set of nucleus-centered charges that provides the best fit, in a least-squares sense, to the potential on the sampling points.  The charge optimization is done using a singular value decomposition (SVD) method described by Mouesca et al. [#ref6]_. These calculations can be affected by user options concerning constraints on total charge and dipole, charge-fitting grid spacing and SVs to be deleted. 

.. index:: MEAD 

The solution of the Poisson or Poisson--Boltzmann equation utilizes libraries from Donald Bashford's MEAD programming suite.  These use a finite-difference method that involves setting up cubic lattices around the molecule.  Finer grids can be nested inside coarser ones to help manage trade-offs between accuracy and computational cost.  The finest grid should cover the entire quantum system (that is, regions of significant electron density), and for good accuracy of :math:`\phi`\ :sub:`rf`  should be no coarser than about 0.15 Å. The outermost grid should extend 10 to 15 Å into the space beyond the model so that boundary conditions are accurate. A reasonable scheme for grid selection based on atomic coordinates is implemented as the default, but the MEAD grids are also user-adjustable. 


The SCRF method should not be used in the same ADF run with other solvation modeling methods such as COSMO or DRF.  However, it is often useful to do geometry optimization with COSMO to get the single-point geometry for an SCRF run. 

**Additional considerations with a protein environment**

The special considerations that apply when a protein environment is specified are similar to those in QM/MM calculations. The classical macromolecular region is specified by a .pqr file that provides the Cartesian coordinates, partial charges and radii of all the atoms of the region, as well as atom identifiers such as residue and atom numbers, in a format similar to PDB format.   The QM atoms are specified in the ADF input file in the usual way. In contrast to the QM/MM situation, the ATOM block in the ADF input should specify only QM atoms, while the .pqr file should specify only the atoms of the protein. It is essential that no symmetry be used in the QM calculation (i.e. SYMMETRY NOSYM) even if the QM system possesses symmetries.  The protein surroundings, as well as the numerical asymmetries of the finite-difference Poisson solver, will break any symmetry that might exist, but the QM part of the calculation has no way to know in advance about this broken symmetry. 

**Classical--QM bonds**

If there is no covalent linkage between atoms in the QM region and the protein,  the situation is straightforward.  If there is such a linkage, some of the same considerations regarding capping atoms and link atoms as in QM/MM calculations apply. One must typically add capping hydrogen atoms to the QM system to satisfy valence requirements.  Because the interaction between the regions is purely electrostatic, we do not encounter the classical-side valency issues or van der Waals interaction issues that one finds in the QM/MM case. This is because this model involves no concept of bonds among the protein atoms. However, the link atom will typically be only a few tenths of an Angstrom from the capping hydrogen atom, so if the link atom has a significant partial charge, it could perturb the QM system in strange ways.  Therefore we typically choose the link atom to be one that would normally only have a small partial charge (such as an aliphatic carbon) and then set its charge to zero in the .pqr file, perhaps with some minor adjustments of nearby partial charges to maintain the correct total charge. 

**Generation of the .pqr file**

Typically one has at hand a PDB-format file of the macromolecule that one would like to include as the 'protein' part of the environment, and one needs to generate a suitable pqr file from this.  PDB files usually lack hydrogen atoms, and often have missing heavy atoms at chain termini and in flexible loops.  These problems need to be addressed in much the same way as for standard molecular mechanics calculations, although the requirements for a pqr file are less rigorous given the lack of classical bonds in the model. Although there are no specific tools for generating PQR files in the ADF distribution, a number of tools are available in the molecular modeling community.  Amber users can use the usual LEaP tool to prepare prmtop and coordinate files, and then the utility, ambpdb can be used with the -pqr flag to generate a pqr file.  Users of CHARMM can generate a structure file (PSF file) for the protein and a CHARMM-generation PDB file (containing hydrogens and using CHARMM naming conventions) and then use a perl script provided by the MEAD suite (available from  `http://stjuderesearch.org/site/lab/bashford <http://stjuderesearch.org/site/lab/bashford>`__) to generate a pqr file from the CHARMM-generated files.  Another option is to use pdb2pqr either as a downloaded program or as web server.  Information about pdb2pqr can be found at  `http://www.poissonboltzmann.org/pdb2pqr <http://www.poissonboltzmann.org/pdb2pqr>`__. 

Once the initial version of the pqr file is generated, it is likely that some hand editing will be needed, particularly if there are covalent linkages between the protein and QM atoms.  In cases with no linkages, such as a (QM) drug in a (classical) protein binding site, the most straightforward procedure is to leave the drug out during generation of the pqr file.  Then no pqr-editing needs to be done, but it is necessary that the QM coordinates and the coordinates in the pqr file be compatible, e.g., that the drug is correctly positioned in the binding site.  If there are covalent links between the QM and protein regions, for example if some sidechains in an enzyme active site are part of the QM region, then the pqr file will probably have been prepared with these sidechains included. *Any atoms that will be part of the QM region must be removed from the pqr file*. If this is not done, the QM region will *feel* protein partial charges that sit on top of the QM-region nuclei; this will generate unphysical results or outright program crashes.  There is no need to worry about dangling valences in the pqr file, but it may be necessary to edit link-atom charges, as noted above.  The QM atom set may need to include capping atoms, (typically hydrogen) to satisfy valence requirements where bonds cross the QM--protein boundary. 

**Format of the pqr file**

A pqr file is similar to a PDB (Protein Data Bank) file but with atomic charge and radii in the occupancy and B-factor columns, respectively.  More specifically, lines beginning with either 'ATOM' or 'HETATM' (no leading spaces) are interpreted as a set of tokens separated by one or more spaces or TAB characters.  Other lines are ignored.  The tokens (including the leading ATOM or HETATM are interpreted as follows::

  ignored ignored atName resName resNum x y z charge radius chainID

The first two (ignored) tokens must be present, or the line will not be parsed correctly. The chainID token is optional, and any tokens beyond that are ignored. Tokens can be of arbitrary length, but must not contain spaces or tabs. Lines that do not begin with "ATOM" or "HETATM" are ignored. The programs make no distinction between ATOMs and HETATMs. *No atname-resnum-chainid combination can occur more than once.* 

Note that the .pqr format does not support some PDB-isms such as a altLoc fields, and a one-character chainID between resName and resSeq. Doing so would break the whitespace separated tokens convention that allows for easy processing with perl scripts, etc.  Instead we put 'chainID' in a position more or less analogous with the PDB segID. (Note that the pdb2pqr program differs on this point, and pqr files with chainIDs between resName and resSeq may need to be modified. 

**SCRF Input**

The SCRF input is contained in an SCRF input block as shown below, optional keywords being surrounded by curly brackets. 

.. _keyscheme SCRF: 


::

   SCRF
     MEADGRID string integer real
     RADIUS string real
     {CYCLES integer}
     {TOLERANCE real}
     {ATOM_MAXR real}
     {CHGFIT_CONSTRAIN string}
     {DELATOM N Iat1 Iat2 ... IatN}
     {GRID_SPACING real}
     {SVD_CONDITION real}
     {SV_DELETE integer}
     {EPSSOL real}
     {IONIC_STR real}
     {SOLRAD real}
     {PROTEIN string}
     {EPSPROT real}
     {SAVESTATE string}
   END

The SCRF block contains two mandatory keys: MEADGRID and RADIUS. All other keys are optional. 

``MEADGRID string integer real``
   Specifies the centering style, dimension and spacing for the MEAD grid. Recognized centering  styles are "ON_ORIGIN" and "ON_GEOM_CENT". The grid dimension specifies the number of points on  one edge of a cubic grid. The grid spacing is given in Angstroms. The edge length of the grid is  the product of the dimension minus 1 and the spacing. Multiple records may be used to specify  sequentially finer grid levels, but finer grids must fit within the coarsest grid. 

``RADIUS string real``
   Specifies the radius in Angstroms for an atom type. Used in fitting the ADF electronic structure  to partial atomic charges and for defining the boundary between regions of low and high dielectric  in MEAD. The atom types should be the same as those used in the ATOMS input block. There must be  one RADIUS record for each atom type in the ATOMS input block. 

``CYCLES integer``
   Specifies the maximum number of cycles of SCRF to perform. Whether or not the SCRF run has  converged, it will terminate when the number of cycles exceeds the value specified by CYCLES. 

``TOLERANCE real``
   Specifies convergence criterion in kcal/mol for SCRF. For each cycle of SCRF the sum of ADF energy,  reaction energy, the energy correction and nuclear reaction energy is calculated. If the  difference in subsequent sums is less than the TOLERANCE value, SCRF is considered to have  converged. Defaults to 0.01. 

``ATOM_MAXR real``
   Specifies the outer atomic radius in Angstroms for the system. For each atom, grid points that lie  between the atomic radius specified by the RADIUS keyword and the outer atomic radius specified  here are included in charge fitting. Defaults to 5.0. 

``CHGFIT_CONSTRAIN string``
   Specifies the type of constraints to be used in charge fitting. Recognized constraints are "NONE",  "CHARGE" or "DIPOLE". NONE specifies no constraints will be applied, CHARGE specifies that only  the molecular charge will be constrained and DIPOLE specifies that both the molecular charge and  dipole will be constrained. Default is DIPOLE. 

``DELATOM N Iat1 Iat2 ... IatN``
   Specifies which atoms should be excluded from the charge fitting procedure. N is the number of atoms to be excluded, followed by a space separated list of atoms numbers Iat1, .., IatN, that should be excluded from the charge fitting procedure. The input order in the ATOMS input block is used to identify the excluded atoms.

``GRID_SPACING real``
   Specifies the grid spacing in Angstroms for the charge fitting grid. The default is 0.2. 

``SVD_CONDITION real``
   Specifies a condition number threshold for inclusion of singular values (SV) in singular value  decomposition (SVD) during charge fitting. The default is 0.000001. 

``SV_DELETE integer``
   Instead of using a condition number threshold for deciding which SV to include in charge fitting,  SV_DELETE may be used to specify how many SV should be excluded. The smallest SV are excluded  first. The default is to use a condition number threshold. If both SV_DELETE and SVD_CONDITION are  specified, the SV_DELETE value will take precedence. 

``EPSSOL real``
   Specifies the solvent dielectric for MEAD. Defaults to the dielectric of water: 80.0. 

``IONIC_STR real``
   Specifies an ionic strength in mol/L for the solvent in MEAD. Defaults to 0.0. 

``SOLRAD real``
   Specifies the radius in Angstroms of a solvent-sized probe that rolls along the surface of the  molecular system to define the dielectric boundary. Defaults to a water-sized probe size of 1.4. 

``PROTEIN string``
   Use of this keyword turns on the SCRF solinprot option by specifying the prefix of a pqr file  containing the protein definition for MEAD solinprot. The filename suffix must be pqr. Pqr format  contains one line per atom and begins with the ATOM keyword followed by 10 fields separated by  white space and in the order: atom number, atom name, residue name, residue number, x, y and z  coordinates, partial atomic charge and atomic radius. The atoms of the quantum mechanical system  should NOT be included in the pqr file. 

``EPSPROT real``
   Specifies the protein dielectric for MEAD. Defaults to 4.0. 

``SAVESTATE string``
   Specifies a filename in which ground state data for a subsequent VSCRF calculation will be saved.  The data is saved in a binary KF file. 

.. only:: html

  .. rubric:: References

.. [#ref1] M.L. Connolly, *Solvent-accessible surfaces of proteins and nucleic acids*, `Science, 221, 709 (1983) <https://doi.org/10.1126/science.6879170>`__ 

.. [#ref2] L.\  Onsager, *Electric moments of molecules in liquids*, `Journal of the American Chemical Society 58, 1486 (1936) <https://doi.org/10.1021/ja01299a050>`__ 

.. [#ref3] S.\  Miertus, E. Scrocco and J. Tomasi, *Electrostatic interaction of a solute with a continuum: a direct utilization of ab initio molecular potentials for the prevision of solvent effects*, `Chemical Physics 55, 117 (1981) <https://doi.org/10.1016/0301-0104(81)85090-2>`__ 

.. [#ref4] J.\  Tomasi, R. Bonaccorsi, R. Cammi and F.J. Olivares del Valle, *Theoretical chemistry in solution. Some results and perspectives of the continuum methods and in particular of the polarizable continuum model*, `Journal of Molecular Structure: THEOCHEM 234, 401 (1991) <https://doi.org/10.1016/0166-1280(91)89026-W>`__ 

.. [#ref5] J.L. Chen, L. Noodleman, D.A. Case and D. Bashford, *Incorporating solvation effects into density functional electronic structure calculations*, `Journal of Physical Chemistry 98, 11059 (1994) <https://doi.org/10.1021/j100094a013>`__ 

.. [#ref6] J.-M. Mouesca, J.L. Chen, L. Noodleman, D. Bashford and D.A. Case, *Density functional/Poisson-Boltzmann calculations of redox potentials for iron-sulfur clusters*, `Journal of the American Chemical Society 116, 11898 (1994) <https://doi.org/10.1021/ja00105a033>`__ 

.. [#ref7] A.\  Fortunelli and J. Tomasi, *The implementation of density functional theory within the polarizable continuum model for solvation*, `Chemical Physics Letters 231, 34 (1994) <https://doi.org/10.1016/0009-2614(94)01253-9>`__ 

.. [#ref8] J.\  Li, M.R. Nelson, C.Y. Peng, D. Bashford, and L. Noodleman, *Incorporating Protein Environments in Density Functional Theory: A Self-Consistent Reaction Field Calculation of Redox Potentials of [2Fe2S] Clusters in Ferredoxin and Phthalate Dioxygenase Reductase*, `Journal of Physical Chemistry A 102, 6311 (1998) <https://doi.org/10.1021/jp980753w>`__ 

.. [#ref10] C.M. Breneman and K.B. Wiberg, *Determining atom-centered monopoles from molecular electrostatic potentials. the need for high sampling density in formamide conformational analysis*, `Journal of Computational Chemistry 11, 361 (1990) <https://doi.org/10.1002/jcc.540110311>`__ 

.. [#ref12] F.M. Richards, *Areas, volumes, packing and protein structures*, `Annual Review of Biophysics and Bioengineering 6, 151 (1977) <https://doi.org/10.1146/annurev.bb.06.060177.001055>`__ 

.. [#ref13] T.\  You and D. Bashford, *An analytical algorithm for the rapid determination of the solvent accessibility of points in a three-dimensional lattice around a solute molecule*, `Journal of Computational Chemistry 16, 743 (1995) <https://doi.org/10.1002/jcc.540160610>`__ 
