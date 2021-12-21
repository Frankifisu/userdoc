.. _VSCRF: 
.. index:: VSCRF 


VSCRF: Vertical Excitation Self-Consistent Reaction Field
=========================================================

**Introduction**

*by Donald Bashford, St. Jude Children's Research Hospital Memphis, October 26, 2011.* 

VSCRF is a method of accounting for the effect of the solvent environment (and possibly a macromolecular environment) on the energy of absorption/emission transitions between electronic states.  It is built on the *Delta* SCF method of calculating electronic transition energies and a continuum dielectric model of the environment in a way that is consistent with the Franck--Condon principle.  The original development and application of the procedure can be found in the papers of Liu et al. [#ref1]_ and Han et al. [#ref2]_. 

Suppose one is calculating the energy for a transition between an initial state *i* with total density (including nuclei) :math:`\rho`\ :sub:`i`  and a final state *f* with total density :math:`\rho`\ :sub:`f` . State *i* has existed long enough that the dielectric environment surrounding it has had time to fully respond, including changes in the distributions of nuclear coordinates and solvent-molecule dipole moments. The density :math:`\rho`\ :sub:`i`  has therefore given rise to a reaction field :math:`\phi`\ :sup:`(r)` \ :sub:`i,eq`  and is self-consistent with it according to the ideas described in the SCRF part of the documentation, therefore the energy in solvent of the initial system is 

.. math::

    G^i ( \rho_i ) = E_0 ( \rho_i ) +  1/2  \int \rho_i (x) \phi^{(r)}_{i,eq} (x)  d^3 x 

where E\ :sub:`0`  is the vacuum density functional.  During the excitation process, the change in density :math:`\Delta` :math:`\rho`\ :sub:`fi`  = :math:`\rho`\ :sub:`f`  - :math:`\rho`\ :sub:`i`  must work against the non-optical component of the pre-existing equilibrium reaction field as well as the optical reaction field arising in response to :math:`\Delta` :math:`\rho` itself. The full theoretical development is given in the paper of Liu et al. [#ref1]_ and the result is that the excitation energy is: 

.. math::

   \Delta G^{if}_{ex}  = E_0 (\rho_i) - E_o (\rho_f) 1/2 \int \Delta \rho_i (x) [2 \phi^{(r)}_{i,eq} (x) \Delta \phi^{(r)}_{op} (x)] d^3 x 

where :math:`\Delta` :math:`\phi`\ :sup:`(r)` \ :sub:`op`  is the reaction field that arises from the *optical* dielectric constant which is related to the index of refraction: :math:`\epsilon`\ :sub:`op`  = n\ :sup:`2`  :math:`\approx` 2 for organic liquids. 

In the following description of the VSCRF algorithm, we adopt the language of an optical absorption calculation.  The initial state is therefore referred to as the ground state, and the final state as the excited state.  For emission calculations, these roles would be reversed. If there is a macromolecular environment surrounding the protein that modeled by macroscopic dielectric theory as described in the SCRF documentation in this manual, this is referred to as the 'protein'. With these definitions in mind, the VSCRF algorithm is: 

+ An SCRF calculation for the ground state, either with or without   a surrounding protein, is a prerequisite for a VSCRF calculation. 

+ The electronic structure of the excited state (with occupations   initially selected by the user) is calculated in vacuum. 

+ The ground-state reaction field, the protein field (if any) and   electron density   are read in from the results of the previous ground-state calculation.  It   is essential that the excited-state and ground state calculations   use exactly the same geometry, ADF grids, basis functions, XC   functionals, MEAD grids and so on. 

+ The excited-state electron density calculated in step 1  is subtracted from the stored ground-state density to   obtain :math:`\Delta`:math:`\rho`. 

+  Nucleus-centered partial charges are derived from :math:`\delta`:math:`\rho`  using a least-squares potential-fitting SVD algorithm  [#ref4]_  which is somewhat similar to the CHELPG algorithm  [#ref5]_. 

+ Set the exterior dielectric environment to the optical     dielectric constant of the solvent, and the optical dielectric     constant of the protein.  These are equal to the square of the     index of refraction of these materials, and are typically :math:`\approx` 2 (the default value).   

+  Using the nucleus-centered partial charges for :math:`\Delta`:math:`\rho`, solve the     Poisson equation using the finite-difference method in the above     dielectric environment to obtain :math:`\Delta`:math:`\phi`\ :sub:`sol` .   

+  Set the exterior dielectric constant to 1 everywhere and solve     the Poisson equation by the finite-difference method to obtain     :math:`\Delta`:math:`\phi`\ :sub:`vac`  

+ The optical reaction field to the excitation,      :math:`\Delta`:math:`\phi`\ :sup:`(r)` \ :sub:`op`  is the difference between     :math:`\Delta`:math:`\phi`\ :sub:`sol`  and :math:`\Delta`:math:`\phi`\ :sub:`vac` .  In this     subtraction, artifacts related to the finite difference method     cancel out.   
+ Recalculate the electronic structure in the presence of the   optical reaction field, as well as the previously stored   ground-state reaction field and the protein field (if any).  This is   done by placing these potentials on the ADF numerical integration   grid when calculating Fock matrix elements. 

+ Check changes in energy for convergence, and if not converged,   return to step 6. 

It should be noted that some additional calculations may be needed to obtain a proper excited-state energy.  For example, if the first excited singlet state is prepared by promoting one of the :math:`\alpha` electrons from the HOMO to the LUMO, the resulting (single-determinant) wave function is not a pure singlet state but actually a mixture of singlet and triplet states [#ref6]_. Calling this mixed state S'\ :sub:`1` , the resolution of the problem is to also calculate the energy of a corresponding triplet state, T\ :sub:`1`  (prepared, for example, by adding one :math:`\alpha` electron to the LUMO and removing one :math:`\beta` electron from the HOMO) and using the formula [#ref6]_: 

.. math::

   E_{S_1}  = 2_{S'_1}  - E_{T_1}

See Liu et al. [#ref1]_ or Han et al. [#ref2]_. for specific examples of this in the ADF/VSCRF context. 

**VSCRF Input**

The VSCRF input is contained in a VSCRF input block as shown below, optional keywords being  surrounded by curly brackets. 

.. _keyscheme VSCRF: 


::

   VSCRF
     MEADGRID string integer real
     RADIUS string real
     INITIAL_STATE string
     {CYCLES integer}
     {TOLERANCE real}
     {ATOM_MAXR real}
     {CHGFIT_CONSTRAIN string}
     {DELATOM N Iat1 Iat2 ... IatN}
     {GRID_SPACING real}
     {SVD_CONDITION real}
     {SV_DELETE integer}
     {EPS_OPT_SOL real}
     {SOLRAD real}
     {PROTEIN string}
     {EPS_OPT_PROT real}
   END

The VSCRF block contains three mandatory keys: MEADGRID, RADIUS and INITIAL_STATE. All other keys  are optional. It is highly recommended that the parameters specifying the MEAD grid and the  details of the charge-fitting SVD procedure be the same for both the SCRF initial state and the  VSCRF final state calculations. These procedures involve some numerical error, and keeping  parameters the same will promote cancellation of these errors as energy differences are taken as  the final results. 

``MEADGRID string integer real``
   Specifies the centering style, dimension and spacing for the MEAD grid. Recognized centering  styles are "ON_ORIGIN" and "ON_GEOM_CENT". The grid dimension specifies the number of points on  one edge of a cubic grid. The grid spacing is given in Angstroms. The edge length of the grid is  the product of the dimension minus 1 and the spacing. Multiple records may be used to specify  sequentially finer grid levels, but finer grids must fit within the coarsest grid. It is highly  recommended that the parameters specifying the MEAD grid be the same for both the SCRF initial  state and the VSCRF final state calculations. 

``RADIUS string real``
   Specifies the radius in Angstroms for an atom type. Used in fitting the ADF electronic structure  to partial atomic charges and for defining the boundary between regions of low and high dielectric  in MEAD. The atom types should be the same as those used in the ATOMS input block. There must be  one RADIUS record for each atom type in the ATOMS input block. 

``INITIAL_STATE string``
   Specifies the filename of a binary KF file containing the ground state data for VSCRF. The KF file  is created by a preliminary SCRF calculation using the SAVESTATE option. It is highly recommended  that the parameters specifying the MEAD grid and the details of the charge-fitting SVD procedure  be the same for both the SCRF initial state and the VSCRF final state calculations. 

``CYCLES integer``
   Specifies the maximum number of cycles of VSCRF to perform. Whether or not the VSCRF run has  converged, it will terminate when the number of cycles exceeds the value specified by CYCLES. 

``TOLERANCE real``
   Specifies convergence criterion in kcal/mol for VSCRF. For each cycle of VSCRF the sum of ADF  energy, Potential Term, and Response Term is calculated. If the difference in subsequent sums is  less than the TOLERANCE value, VSCRF is considered to have converged. Defaults to 0.01. 

``ATOM_MAXR real``
   Specifies the outer atomic radius in Angstroms for the system. For each atom, grid points that lie  between the atomic radius specified by the RADIUS keyword and the outer atomic radius specified  here are included in charge fitting. It is highly recommended that the parameters specifying the  details of the charge-fitting SVD procedure be the same for both the SCRF initial state and the  VSCRF final state calculations. Defaults to 5.0. 

``CHGFIT_CONSTRAIN string``
   Specifies the type of constraints to be used in charge fitting. Recognized constraints are "NONE",  "CHARGE" or "DIPOLE". NONE specifies no constraints will be applied, CHARGE specifies that only  the molecular charge will be constrained and DIPOLE specifies that both the molecular charge and  dipole will be constrained. It is highly recommended that the parameters specifying the details of  the charge-fitting SVD procedure be the same for both the SCRF initial state and the VSCRF final  state calculations. Default is DIPOLE. 

``DELATOM N Iat1 Iat2 ... IatN``
   Specifies which atoms should be excluded from the charge fitting procedure. N is the number of atoms to be excluded, followed by a space separated list of atoms numbers Iat1, .., IatN, that should be excluded from the charge fitting procedure. The input order in the ATOMS input block is used to identify the excluded atoms. It is highly recommended that the parameters specifying the details of the charge-fitting SVD procedure be the same for both the SCRF initial state and the VSCRF final state calculations.

``GRID_SPACING real``
   Specifies the grid spacing in Angstroms for the charge fitting grid. It is highly recommended that  the parameters specifying the details of the charge-fitting SVD procedure be the same for both the  SCRF initial state and the VSCRF final state calculations. The default is 0.2. 

``SVD_CONDITION real``
   Specifies a condition number threshold for inclusion of singular values (SV) in singular value  decomposition (SVD) during charge fitting. It is highly recommended that the parameters specifying  the details of the charge-fitting SVD procedure be the same for both the SCRF initial state and  the VSCRF final state calculations. The default is 0.000001. 

``SV_DELETE integer``
   Instead of using a condition number threshold for deciding which SV to include in charge fitting,  SV_DELETE may be used to specify how many SV should be excluded. The smallest SV are excluded  first. The default is to use a condition number threshold. If both SV_DELETE and SVD_CONDITION are  specified, the SV_DELETE value will take precedence. It is highly recommended that the parameters  specifying the details of the charge-fitting SVD procedure be the same for both the SCRF initial  state and the VSCRF final state calculations. 

``EPS_OPT_SOL real``
   Specifies the dielectric constant of the solvent at optical frequencies for MEAD. This value is  equal to the square of the index of refraction of the solvent. Defaults to the value for water:  2.0. 

``SOLRAD real``
   Specifies the radius in Angstroms of a solvent-sized probe that rolls along the surface of the  molecular system to define the dielectric boundary. Defaults to a water-sized probe size of 1.4. 

``PROTEIN string``
   Use of this keyword turns on the VSCRF solinprot option by specifying the prefix of a pqr file  containing the protein definition for MEAD solinprot. This option can only be used if the ground  state SCRF calculation also used a protein. The filename suffix must be pqr. Pqr format contains  one line per atom and begins with the ATOM keyword followed by 10 fields separated by white space  and in the order: atom number, atom name, residue name, residue number, x, y and z coordinates,  partial atomic charge and atomic radius. The atoms of the quantum mechanical system should NOT be  included in the pqr file. 

``EPS_OPT_PROT real``
   Specifies the dielectric constant of the protein at optical frequencies for MEAD. This value is  equal to the square of the index of refraction of the protein. Defaults to the value for organic  liquids: 2.0. 

.. only:: html

  .. rubric:: References

.. [#ref1] T.\  Liu, W.-G Han, F. Himo, G.M. Ullmann, D. Bashford, A. Toutchkine, K.M. Hahn, and L. Noodleman, *Density Functional Vertical Self-Consistent Reaction Field Theory for Solvatochromism Studies of Solvent-Sensitive Dyes*, `Journal of Physical Chemistry A 108, 3545 (2004) <https://doi.org/10.1021/jp031062p>`__ 

.. [#ref2] W.-G. Han, T. Liu, F. Himo, A. Toutchkine, D. Bashford, K.M. Hahn, L. Noodleman, *A Theoretical Study of the UV/Visible Absorption and Emission Solvatochromic Properties of Solvent-Sensitive Dyes*, `ChemPhysChem 4, 1084 (2003) <https://doi.org/10.1002/cphc.200300801>`__ 

.. [#ref4] J.-M. Mouesca, J.L. Chen, L. Noodleman, D. Bashford and D.A. Case, *Density functional/Poisson-Boltzmann calculations of redox potentials for iron-sulfur clusters*, `Journal of the American Chemical Society 116, 11898 (1994) <https://doi.org/10.1021/ja00105a033>`__ 

.. [#ref5] C.M. Breneman and K.B. Wiberg, *Determining atom-centered monopoles from molecular electrostatic potentials. the need for high sampling density in formamide conformational analysis*, `Journal of Computational Chemistry 11, 361 (1990) <https://doi.org/10.1002/jcc.540110311>`__ 

.. [#ref6] T.\  Ziegler, A. Rauk and E.J. Baerends, *On the calculation of Multiplet Energies by the Hartree Fock Slater method*, `Theoretica Chimica Acta 43, 261 (1977) <https://doi.org/10.1007/BF00551551>`__ 
