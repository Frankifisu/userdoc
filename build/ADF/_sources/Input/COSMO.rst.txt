.. _COSMO: 
.. index:: COSMO 


COSMO: Conductor like Screening Model
=====================================

You can study chemistry in solution, as contrasted to the gas phase, with the implementation in ADF [#ref1]_ of the Conductor like Screening Model (COSMO) of solvation [#ref4]_ [#ref9]_ [#ref10]_. The energy derivatives can also be calculated, so geometry optimization, harmonic frequencies, et cetera are available within this model. 

The COSMO model is a dielectric model in which the solute molecule is embedded in a molecule-shaped cavity surrounded by a dielectric medium with given dielectric constant :math:`\epsilon`. Energy-related terms are computed for a conductor first, then scaled by the function 

.. math::

  f(\epsilon) = \frac{\epsilon-1}{\epsilon + x} \qquad (2.1.1)

The empirical scaling factor *x* is specified in the input data block for the SOLVATION key. The block key SOLVATION turns the solvation calculation on. In most cases default values are available for the involved parameters.
In order to construct the cavity atomic cavity radii are used.
The default COSMO atomic cavity radii used in ADF are the Van der Waals radii from the MM3 method by Allinger  (Ref. [#ref2]_) divided by 1.2.

It is also possible to include a linear parametrization of non-electrostatic terms as a function of surface area. To include such term can be specified in the input data block for the SOLVATION key. The default is to include only the part of this term that is proportional to the surface area (default CAV0=0.0, CAV1=0.0067639): 

.. math::

  E_\text{non-elst} = f(\epsilon) (CAV0 + CAV1 \times \text{area}) \qquad  (2.1.2)

If a calculations was done on a fragment, then the wave function obtained would be optimal for the fragment in solution, but not optimal for gas phase. The energies with the gas phase Hamiltonian would be higher, and the apparent solvation contribution to bonding would also be higher. The net point is that normally the COSMO procedure reports the energy of Esolv(AB), but to get the solvation energy, you need to subtract the E(AB, solv) from E(AB,gas) because the wave function changes (unless you are doing it post-SCF.) For this you need to have the same reference fragments in each case A(g) and B(g). 

Because of precision issues in ADF2016 the default surface has been changed to Delley, instead of Esurf.

.. _keyscheme SOLVATION: 


::

   SOLVATION
    {SURF Surface {NOKEEP}}
    {SOLV {Name=solvent} {Eps=78.4} {Del=1.4} {Rad=1.4}
          {Neql=1.9}{Emp=0.0}{Cav0=0.0}{Cav1=0.0067639} }
    {DIV {Ndiv=3} {NFdiv=1} {Min=0.5} {OFAC=0.8}
         {leb1=23} {leb2=29}{rleb=1.5} }
    {NOASS}
    {RADII
      name1=value1
      name2=value2
      ...
    subend }
    {CHARGED {Method=meth} {Conv=1e-8} {Omega=1.0} {Iter=1000}
             {Corr} {LoCosmo LoCosmoDist}}
    {C-MAT How {SCF} tol=1e-10 }
    {DISC {SC=0.01} {LEG=4} {TOL=0.1} }
    {SCF {When} {How}
    {NOCSMRSP}
    {LPRT}
   End

Presence of the SOLVATION key block triggers the solvent calculation and does not require additional data. With subkeys you can customize various aspects of the model, for instance to specify the type of solute. None of the subkeys is obligatory. Follows a description of the subkeys 

``SURF Surface {NOKEEP}``
   Defines the type of cavity to be used. ``Surface`` can be one of the following: Wsurf, Asurf, Esurf, Klamt, or Delley. **Default: Delley**. The  Wsurf, Asurf, and Esurf surfaces are constructed with the GEPOL93 algorithm [#ref3]_ 

   ``Wsurf``
      Wsurf triggers the Van der Waals surface (VdW), which consists of the union of all atomic spheres. Not recommended to be used. 

   ``Asurf``
      Asurf gives the Solvent-Accessible-Surface (SAS). This is similar to VdW but consists of the path traced by the center of a spherical solvent molecule rolling about the VdW surface or, equivalently, a VdW surface created by atomic spheres to which the solvent radius has been added. These two surface types contain cusps at the intersection of spheres. Not recommended to be used. 

   ``Esurf``
      Esurf gives the Solvent-Excluding-Surface (SES), which consists of the path traced by the *surface* of a spherical solvent molecule rolling about the VdW surface. Primarily, this consists of the VdW surface but in the regions where the spheres would intersect, the concave part of the solvent sphere replaces the cusp.

   ``Klamt``
      The fourth surface option is Klamt as described in [#ref4]_. It excludes the cusp regions also. Note that this surface might give an incomplete COSMO surface in case of more complicated molecules. Not recommended to be used. 

   ``Delley``
      The fifth surface (default surface) is the so called Delley surface, see also Ref. [#ref5]_. This Delley type of cavity construction is recommended to be used in COSMO calculations, which results are used as input for COSMO-RS calculation, see the corresponding `manual for COSMO-RS <../../COSMO-RS/index.html>`_.  This Delley surface is the default COSMO surface in ADF.

   ``NOKEEP``
      The optional parameter NOKEEP controls surface creation during calculation of frequencies by numerical differentiation. By default, the surface is constructed  only once at the central geometry and is used for the rest of the calculation. If the  NOKEEP is specified then ADF will construct a new surface at each displaced geometry. 

``DIV``
   The actual construction of the surface involves a few technical parameters controlled with the subkey DIV 

   ``Ndiv, NFdiv``
      Ndiv controls how fine the spheres that in fact describe the surface are partitioned in small surface triangles, each containing one point charge to represent the polarization of the cavity surface. Default division level for triangles Ndiv=3. Default final division level for triangles NFdiv=1 (NFdiv :math:`\leq` Ndiv). Not used in the Delley surface. 

   ``Min``
      Min specifies the size, in angstrom, of the smallest sphere that may be constructed by the SES surface. For VdW and SAS surfaces it has no meaning. Default Min=0.5. Not used in the Delley surface. 

   ``Ofac``
      Ofac is a maximum allowed overlap of new created spheres, in the construction procedure. Default Ofac=0.8. Not used in the Delley surface. 

   ``leb1, leb2, rleb``
      Only used in the Delley surface. For the Delley type of construction one needs to set the variables leb1 (default value 23), leb2 (default value 29), and rleb (default value 1.5 Angstrom) to set the number of surface points. If the cavity radius of an atom is lower than rleb use leb1, otherwise use leb2. These values can be changed: using a higher value for leb1 and leb2 gives more surface points (maximal value leb1, leb2 is 29). A value of 23 means 194 surface points in case of a single atom, and 29 means 302 surface points in case  of a single atom Typically one could use leb1 for the surface point of H, and leb2 for the surface points of other elements. 

``NOASS``
   By default all new spheres that are created in the surface-construction are assigned to atoms, for the purpose of gradient computations (geometry optimization). Specifying the noass subkey turns this off. It has no argument. 

.. index:: COSMO non-electrostatic term 

``SOLV``
   Solvent details.  

   ``Eps, Rad``
      Eps specifies the dielectric constant (the default relates to water). In ADF an infinite value for Eps is chosen if Eps is specified to be lower than 1.0. Rad specifies the radius of the (rigid sphere) solvent molecules, in angstrom. Instead of specifying Eps and Rad one can specify a solvent name or formula  after 'name='. The following table lists names and formulas that are recognized with the corresponding values for Eps and Rad. The Rad in this table is calculated from the density, the molar mass, and a spherical approximation for the solvent. The names and formulas are case-insensitive. 

      .. csv-table:: 

         Name,Formula,Eps,Rad
         AceticAcid,CH3COOH,6.19,2.83
         Acetone,CH3COCH3,20.7,3.08
         Acetonitrile,CH3CN,37.5,2.76
         Ammonia,NH3,16.9,2.24
         Aniline,C6H5NH2,6.8,3.31
         Benzene,C6H6,2.3,3.28
         BenzylAlcohol,C6H5CH2OH,13.1,3.45
         Bromoform,CHBr3,4.3,3.26
         Butanol,C4H9OH,17.5,3.31
         isoButanol,(CH3)2CHCH2OH,17.9,3.33
         tertButanol,(CH3)3COH,12.4,3.35
         CarbonDisulfide,CS2,2.6,2.88
         CarbonTetrachloride,CCl4,2.2,3.37
         Chloroform,CHCl3,4.8,3.17
         Cyclohexane,C6H12,2,3.5
         Cyclohexanone,C6H10O,15,3.46
         Dichlorobenzene,C6H4Cl2,9.8,3.54
         DiethylEther,(CH3CH2)2O,4.34,3.46
         Dioxane,C4H8O2,2.2,3.24
         DMFA,(CH3)2NCHO,37,3.13
         DMSO,(CH3)2SO,46.7,3.04
         Ethanol,CH3CH2OH,24.55,2.85
         EthylAcetate,CH3COOCH2CH3,6.02,3.39
         Dichloroethane,ClCH2CH2Cl,10.66,3.15
         EthyleneGlycol,HOCH2CH2OH,37.7,2.81
         Formamide,HCONH2,109.5,2.51
         FormicAcid,HCOOH,58.5,2.47
         Glycerol,C3H8O3,42.5,3.07
         HexamethylPhosphoramide,C6H18N3OP,43.3,4.1
         Hexane,C6H14,1.88,3.74
         Hydrazine,N2H4,51.7,2.33
         Methanol,CH3OH,32.6,2.53
         MethylEthylKetone,CH3CH2COCH3,18.5,3.3
         Dichloromethane,CH2Cl2,8.9,2.94
         Methylformamide,HCONHCH3,182.4,2.86
         Methypyrrolidinone,C5H9NO,33,3.36
         Nitrobenzene,C6H5NO2,34.8,3.44
         Nitrogen,N2,1.45,2.36
         Nitromethane,CH3NO2,35.87,2.77
         PhosphorylChloride,POCl3,13.9,3.33
         IsoPropanol,(CH3)2CHOH,19.9,3.12
         Pyridine,C5H5N,12.4,3.18
         Sulfolane,C4H8SO2,43.3,3.35
         Tetrahydrofuran,C4H8O,7.58,3.18
         Toluene,C6H5CH3,2.38,3.48
         Triethylamine,(CH3CH2)3N,2.44,3.81
         TrifluoroaceticAcid,CF3COOH,8.55,3.12
         Water,H2O,78.39,1.93
   
   ``Del``
      Del is the value of Klamt's delta_sol parameter, only relevant in case of Klamt surface. 

   ``Neql``
      If Neql = :math:`\epsilon`\ :sub:`NEQL`  is included a non-equilibrium solvation is used, i.e. that the dielectric constant :math:`\epsilon`\ :sub:`NEQL`  used in RESPONSE is different from the ground state dielectric constant :math:`\epsilon`. Only relevant in case of TDDFT calculations. Default :math:`\epsilon`\ :sub:`NEQL`  = :math:`\epsilon`. The reason for using two different dielectric constants is that the electronic transition can so fast that only the electronic component of the solvent dielectric can respond, i.e., one should use the optical part of the dielectric constant. This is typically referred to as non-equilibrium solvation. The optical dielectric constant can be obtaining from the (frequency dependent) refractive index n of the solvent as: :math:`\epsilon`\ :sub:`NEQL`  = n\ :sup:`2` . 

   ``Emp``
      Emp addresses the empirical scaling factor *x* in the formula 2.1.1 above. 

   ``Cav0, Cav1``
      Other options specify a linear parametrization of non-electrostatic terms as a function of surface area, see the formula 2.1.2 above. Possible values for CAV0 and CAV1 are CAV0 = 1.321 and CAV1 = 0.0067639, see Ref. [#ref6]_). In ADF2010 the default values for CAV0 and CAV1 are  CAV0 = 0.0 and CAV1 = 0.0. However, starting from ADF2012 the default values for CAV0 and CAV1 are CAV0 = 0.0 and CAV1 = 0.0067639, If CAV0 is not zero, Esolv(AB) is not the same as Esolv(A) + Esolv(B) if A and B are far apart. This is the reason why CAV0 is set to zero, by default. By default CAV1 is not set to zero, thus by default there is a solvation energy term that does depend on the size of the cavity (surface area). 

``COSMO Radii``
   In order to construct the surface you have to specify the atomic ('Van der Waals') radii. There are three ways of doing this. In the first method you append 'adf.R=value' to the atomic coordinates record, in the ATOMS key block. This would look like, for instance::

      C 1 2 3 CC CCO CCOH adf.f=C.dz adf.R=2.0

   It assigns a radius of 2.0 to the Carbon atom. In the second method you apply the same format, but specify a symbol (identifier) rather than a value::

      C 1 2 3 CC CCO CCOH adf.f=C.dz adf.R=C-sp3

   The identifiers must be defined in the (optional) RADII subkey block in the Solvation data block (see next). In the third method, you don't modify the Atoms block at all. In this case, the RADII subkey must be used and the 'identifiers' in it must be exactly the atom type names in the Atoms block. 

``RADII``
   This subkey is block type. Its data block (if the subkey is used) must terminate with a record subend. In the Radii data block you give a list of identifiers and values::

      SOLVATION
         ...
         Radii
            name1=value1
            name2=value2
            ...
         Subend
         ...
      End

   The values are the radii of the atomic spheres, in the same units of length as used in the Atoms block (angstrom or bohr). The names specify to which atoms these values apply. As discussed for the Solv subkey this depends on the Atoms block. If in the specification of atomic coordinates you have used the 'adf.R=' construct to assign radii, with identifiers rather than values for the R-value, these identifiers must be defined in the Radii sub block. If no 'adf.R=' construct was applied in the Atoms block, you must use the atom type names as they occurred in the Atoms data block. Referring to the example given in the Solv subkey discussion, you might have::

      Radii
         C-sp3=2.0
         ...
      Subend

   A simple atom type reference might look like::

      Radii
         C=2.0
         ...
      Subend

   When no radius specified a default value is used. The default value  for an atom is the corresponding Van der Waals radius from the MM3 method by Allinger  (Ref. [#ref2]_) divided by 1.2.  

   Another popular choice are the so called Klamt atomic cavity radii (Ref. [#ref8]_), which are optimized for a few elements::

      Radii          
         H  1.30          
         C  2.00          
         N  1.83          
         O  1.72          
         F  1.72          
         Si 2.48          
         P  2.13          
         S  2.16          
         Cl 2.05          
         Br 2.16          
         I  2.32        
      Subend 


``CHARGED {Method=meth} {Conv=1e-8} {Omega=1.0} {Iter=1000} {Corr} {LoCosmo LoCosmoDist}``
   This addresses the determination of the (point) charges that model the cavity surface polarization. In COSMO calculations you compute the surface point charges *q* by solving the equation A*q*=-*f*, where *f* is the molecular potential at the location of the surface charges *q* and A is the self-interaction matrix of the charges. The number of charges can be substantial and the matrix A hence very large. A direct method, i.e. inversion of A, may be very cumbersome or even impossible due to memory limitations, in which case you have to resort to an iterative method. Meth specifies the equation-solving algorithm. Meth=INVER requests direct inversion. Meth=GAUS calls for the Gauss-Seidel iterative method. Meth=Jacobi activates another standard iterative procedure. The latter two methods require a positive-definite matrix (which may fail to be the case in an actual calculation) and can be used with a relaxation technique, controlled by the relaxation parameter OMEGA (1.0=no relaxation). Meth=CONJ (default) uses the preconditioned biconjugate gradient method. This is guaranteed to converge and does not require huge amounts of memory. CONV and ITER are the convergence criterion and the maximum number of iterations for the iterative methods.  Some of the molecular electronic charge distribution may be located outside the cavity. This affects the assumptions underlying the COSMO equations. LOCOSMO can only be used icw FDE.

   Specifying the CORR option to the CHARGED subkey constrains the computed solvent surface charges to add up to the negative of the molecular charge. In ADF2016 this outlying charge correction is also done during the SCF. Note that before ADF2016 it was only a post-SCF correction on the COSMO charges. In ADF2018 a bug that was introduced in ADF2016 in case of this outlying charge correction was fixed for the energy (typically a small effect).

``C-MATRIX``
   How: For the potential *f* we need the Coulomb interaction between the charges *q* and the molecular electronic density (and nuclei). Three methods are available, specified by the first option to the C-Matrix subkey. 

   a) EXACT: compute the straightforward Coulomb potential due to the charge *q* in each point of the molecular numerical integration grid and integrate against the electronic charge density. This is, in principle, exact but may have inaccuracies when the numerical integration points are very close to the positions of a charge *q*. To remedy this, the point charges *q* can be 'smeared out' and represented by a disc, see the next subkey DISC. 

   b) FIT: same as EXACT, but the *q*-potentials are now integrated not against the exact electronic charge density, but against the (much cheaper-to-compute) fitted density. The same DISC considerations apply. 

   c) POT: evaluate the molecular potential at the position of the charge *q* and multiply against the *q*-strength. Since the molecular Coulomb potential is computed from the fit density, any difference in results between the FIT and the POT approach should be attributed to the DISC issue. POT is the default, because it is faster, and is only inadequate if the fit density is very inaccurate, which would be a problem anyway. 

   SCF: If you specify this option, the computation of the Coulomb interaction matrix (between electrons and surface charges) is carried out during the SCF procedure, but this turns out to hamper the SCF convergence behavior. Therefore: not recommended. *IF* you use it, the program will switch to one of the other 3 methods, as given by the 'How' option, as soon as the SCF convergence error drops below TOL: (applies only to the SCF option, which is not recommended). 

``DISC``
   Applies only when the C-matrix method is EXACT or FIT. Note, however, that the default for the C-matrix method is POT, in which case the DISC subkey has no meaning. The DISC key lets the program replace the point charges *q* by a solid uniformly charged spherical surface disc whenever the numerical integration accuracy requires so, i.e. for those charges that are close to numerical integration points. Options: SC defines a shrinking factor, by which the actual disc radius used is reduced from its 'normal' value: an inscribed disc in the triangular surface partitions that define the distribution of surface charges, see the subkey DIV. LEG gives the polynomial expansion order of the disc potentials. The Legendre expansion converges rapidly and the default should be adequate. 

   TOL is a tolerance parameter to control the accuracy of the disc potential evaluations. 

``SCF``
   In COSMO calculations you can include the surface charges in the Fock operator self-consistently, i.e. by recomputing the charges *q* at every SCF cycle and include them in the equations, or in a perturbational manner, i.e. post-SCF. This is controlled with the first option. The When option must be either VAR or PERT, for variational and perturbational, respectively. Default is VAR. The second (HOW) option applies only to the WHEN=VAR case and may affect the speed of SCF convergence. The COSMO calculation implies a considerable increase in CPU time! Values for HOW: 

   - ALL: This includes it in all SCF cycles (except for the first SCF cycle, which is gas-phase) 
   
   - LAST: This lets the program first converge the SCF completely without any solvent effects. Thereafter, the COSMO is turned on, hopefully converging in fewer cycles now, to compensate for the 'double' SCF effort. 
   
   - TOL=0.1 (or another value) is an in-between approach: converge the gas-phase SCF until the SCF error is below TOL, then turn on COSMO. 

.. index:: COSMO TDDFT 

.. index:: TDDFT COSMO 

``NOCSMRSP``
   Relevant only in combination with the time-dependent DFT (TDDFT) applications: the EXCITATION, the RESPONSE, or the AORESPONSE key. If this subkey NOCSMRSP is included the induced electronic charges which are present in the TDDFT calculations, will not influence the COSMO surface charges. No dielectric constant in the response might be closer to the optical dielectric constant than using the full dielectric constant, see also sub-argument NEQL of the subkey SOLV of the key SOLVATION. By default, in absence of this subkey NOCSMRSP, the induced electronic will influence the COSMO surface charges. If one does geometry optimization of the excited state this makes sense, since then the solvent dielectric has time to fully respond.

``LPRT``
   This is a debug switch and triggers a lot more output related to the cavity construction etc. 

**Warning**

Numerical frequencies calculated with COSMO should be checked for stability  with respect to the *disrad*, the numerical differentiation step size. The problem  is that the COSMO surface changes slightly when a nucleus is moved from its  equilibrium position. The change is usually small but in some cases it may result is  creation or annihilation of surface points, which will lead to discontinuities in the  potential energy surface and may result in inaccurate frequencies. 

Thus, when calculating vibrational frequencies numerically with COSMO, one should try  decreasing the *disrad* value until no changes in frequencies are observed.  However, the value should not be too small because then the total numerical noise may become  too large compared to the generated forces. A general recommendation would be to  try to decrease disrad by a factor of 2 at a time. Of course, this procedure may be  very expensive for a large molecule. If this the case, one should use the SCANFREQ  keyword and recalculate only a small number of frequencies. It should be noted that  generally frequencies that have a small force constant are more sensitive to the  numerical noise. 


.. only:: html

  .. rubric:: References

.. [#ref1] C.C. Pye and T. Ziegler, *An implementation of the conductor-like screening model of solvation within the Amsterdam density functional package*, `Theoretical Chemistry Accounts 101, 396 (1999) <https://doi.org/10.1007/s002140050457>`__ 

.. [#ref4] A.\  Klamt and G. Schüürmann, *COSMO: a new approach to dielectric screening in solvents with explicit expressions for the screening energy and its gradient*, `Journal of the Chemical Society: Perkin Transactions 2, 799 (1993) <https://doi.org/10.1039/P29930000799>`__ 

.. [#ref9] A.\  Klamt, *Conductor-like Screening Model for real solvents: A new approach to the quantitative calculation of solvation phenomena*, `Journal of Physical Chemistry 99, 2224 (1995) <https://doi.org/10.1021/j100007a062>`__ 

.. [#ref10] A.\  Klamt and V. Jones, *Treatment of the outlying charge in continuum solvation models*, `Journal of Chemical Physics 105, 9972 (1996) <https://doi.org/10.1063/1.472829>`__ 

.. [#ref2] N.L. Allinger, X. Zhou, J. Bergsma, *Molecular mechanics parameters*, `Journal of Molecular Structure: THEOCHEM 312, 69 (1994) <https://doi.org/10.1016/S0166-1280(09)80008-0>`__ 

.. [#ref3] J.L. Pascual-ahuir, E. Silla and I. Tuñon, *GEPOL: An improved description of molecular surfaces. III. A new algorithm for the computation of a solvent-excluding surface*, `Journal of Computational Chemistry 15, 1127 (1994) <https://doi.org/10.1002/jcc.540151009>`__ 

.. [#ref5] B.\  Delley, *The conductor-like screening model for polymers and surfaces*, `Molecular Simulation 32, 117 (2006) <https://doi.org/10.1080/08927020600589684>`__ 

.. [#ref6] T.N. Truong and E.V. Stefanovich, *A new method for incorporating solvent effect into the classical, ab initio molecular orbital and density functional theory frameworks for arbitrary shape cavity*, `Chemical Physics Letters 240, 253 (1995) <https://doi.org/10.1016/0009-2614(95)00541-B>`__ 

.. [#ref8] A.\  Klamt, V. Jonas, T. Bürger and J.C. Lohrenz,  *Refinement and Parametrization of COSMO-RS.*  `J. Phys. Chem. A 102, 5074 (1998) <https://doi.org/10.1021/jp980017s>`__


