
.. _DIMQM: 
.. index:: DIM/QM 
.. index:: QM/MM
.. index:: solvent effects


DIM/QM: Discrete Interaction Model/Quantum Mechanics
====================================================

The Discrete Interaction Model/Quantum Mechanics (DIM/QM) method facilitates calculating the optical properties of molecules under the influence of a discrete solvent or a metal nanoparticle, see for example Ref. [#ref1]_. DIM/QM relies on one of three descriptions of the system: Discrete Reaction Field (DRF), where the atoms interact via induced dipoles and static charge, Capacitance Polarizability Interaction Model (CPIM), where the atoms interact via induced dipoles and induced charges, and Polarizability Interaction Model (PIM), where the atoms interact via induced dipoles only. DRF is best for solvents, CPIM is best for small metal nanoparticles, and PIM is best for large metal nanoparticles. 

The DRF module is now a part of DIM/QM, so DRF is now a submodule of DIM/QM. 

To perform a DIM/QM calculation, two block keys are required.  The first is the DIMQM block which activates the DIM/QM module.  The parameters for each DIM atom must also be given, and they can be given with either the DIMPAR block which is most convenient for metal nanoparticles, or with the EXTERNALS block which is designed for DRF. 

In ADF2019 the bond energies calculated with DIM/QM in ADF have been corrected.

.. _DRF: 

.. index:: DRF 

.. index:: discrete solvent RF model 

DRF
---

The Discrete Solvent Reaction Field (DRF) model is a hybrid Quantum mechanical and Molecular Mechanics (QM/MM) model for studying solvation effects on (time-dependent) molecular properties such as dipole moments, excitation energies and (hyper)polarizabilities [#ref7]_ [#ref8]_ [#ref9]_ [#ref10]_ [#ref11]_. The classical solvent molecules are represented using distributed atomic charges and polarizabilities. 

With the ADF-GUI it is simple to setup a DRF calculation.
Another possibility is to use and/or modify a python script that is explained in the example :ref:`DIMQM_DRF_plams<example DIMQM_DRF_plams>`.
Both the ADF-GUI and the DRF python script have default settings which can be easily modified if this is required.
In the simplest case the user just needs to provide the QM and DRF regions.
By default, atomic charges that are used, in case of the ADF-GUI or the DRF python script, for the DRF are computed with LDA functional, DZP basis set and normal numerical quality.
Also by default, atomic polarizabilities (computed with the Thole's model) are taken from a inner database including H, C, N, O, F, S, Cl, Br, I atoms [#ref2]_.
If one does not use the ADF-GUI or the DRF python script, the user has to specify this by hand.

Within the Discrete Solvent Reaction Field model the QM/MM operator is 

.. math::
   
  H_\text{QM/MM} = \sum_i v_\text{DRF} (r_i, \omega) = \sum_i V^\text{el} (r_i) + V^\text{pol} (r_i, \omega) 

where the first term, v\ :sup:`el` , is the electrostatic operator and describes the Coulombic interaction between the QM system and the permanent charge distribution of the solvent molecules. The second term, v\ :sup:`pol` , is the polarization operator and describes the many-body polarization of the solvent molecules, i.e. the change in the charge distribution of the solvent molecules due to interaction with the QM part and other solvent molecules. The charge distribution of the solvent is represented by atomic point charges and the many-body polarization by induced atomic dipoles at the solvent molecules. The induced atomic dipole at site *s* is found by solving a set of linear equations 

.. math::
   
  \mu^\text{ind}_{s,\alpha} (\omega) = \alpha_{s,\alpha \beta} \left( F^\text{init}_{s,\beta} (\omega) + \sum_{t \neq s} T^{(2)}_{st,\beta \gamma} \mu^\text{ind}_{t,\gamma} (\omega) \right)


where :math:`\alpha_{s,\alpha \beta}`  is a component of the atomic polarizability tensor at site *s*. The screened dipole interaction tensor is given by 

.. math::

  T^{(2)}_{st,\beta \gamma} = 3f^T_{st} R_{st,\alpha} R_{st,\beta} / R^5_{st} - f^E_{st} \delta_{\alpha \beta} / R^3_{st}


where the damping functions f\ :sup:`T` \ :sub:`st`  and f\ :sup:`E` \ :sub:`st`  have been introduced, see also [#ref2]_. A smeared-out point charge model [#ref3]_ is used for short-range damping of the QM/MM operator 

.. math::

  1/R_{st}  \rightarrow 1/S_{st}  = erf(R_{st})/R_{st}  

The scaled distance, S\ :sub:`st` , then replaces the normal distance, R\ :sub:`st` , in the QM/MM operator. 

In order to perform a DRF calculation two types of parameters (model atomic charges and atomic polarizabilities) for each type of atom in the MM part are required. The point charges should represent at least the permanent molecular dipole moment, and the distributed atomic polarizabilities the full molecular polarizability tensor. The atomic charges can straightforward be obtained using e.g. Multipole Derived Charges (MDC) [See  :ref:`section on MDC<MDC>` and the distributed polarizabilities by adopting standard parameters or refitting them to match the calculated polarizability tensor [#ref2]_ [#ref3]_. This allows for a simple procedure to obtain the solvent model parameters which subsequently can be used in the DRF calculation. 

DRF gradients can be calculated by using the DRF2 keyword in the DIMQM block. This is an expert option and should be used with great caution. The DRF2 keyword uses DRF but with Gaussian screening like that of the PIM method. It also allows for input of parameters by atom type like the PIM method. The user must specify a radius and charge for the atom type like seen below.

::

  DIMPAR
    O
      rad=0.9028
      char=-0.6690 
      STATIC
    SUBEND
    H
      rad=0.2479
      char=0.3345
      STATIC
    SUBEND
    Ag
      rad=1.445
      char=0.0000
    SUBEND
  END

Here, the STATIC keyword is used to tell DIM/QM to ignore the frequency dependent response for those atom types. 

.. index:: SERS
.. index:: SEHRS
.. index:: PETPA

Surface-enhanced response properties
------------------------------------

In addition to the calculation of solvation effects on response properties,
DIM/QM can also be used for simulating nonlinear optical properties of molecules near metal surfaces of a nanoparticle.
A TDDFT description of the molecule is coupled to an electrodynamical treatment of the nanoparticle, including electrostatics and polarization of the atoms.
In this way DIM/QM can be used to study surface-enhance Raman scattering (SERS) [#ref1]_, surface-enhanced Raman optical activity (SEROA)
[#ref4]_, and plasmon-enhanced photochemistry.

Starting from ADF2018 the Polarizability Interaction Model (PIM) can be used to calculate damped first hyperpolarizabilities :math:`\beta` and damped second hyperpolarizabilities :math:`\gamma`.
Different types of :math:`\beta`-tensors can be calculated, such as STATIC, OPTICALR, EOPE, and SHG.
This allows for simulation of surface-enhanced hyper-Raman scattering (SEHRS) [#ref5]_.
All the (sub)keywords for regular damped :math:`\beta`, such as BETA and QUADRATIC, can also be used.
Also different types of :math:`\gamma`-tensors can be calculated, such as STATIC, EFIOR, OKE, IDRI, EFISHG, THG and TPA.
This allows for simulation of plasmon-enhanced two-photon absorption (PETPA).
Except CUBIC, all the other (sub)keywords for regular damped :math:`\gamma` can also be used.

Input options
-------------

.. _keyscheme DIMQM: 

.. _keyscheme DRF: 


::

  DIMQM
    <DRF|PIM|CPIM>
    NOPOL
    NOCHAR
    NOCROSS
    DDA
    FULLGRID
    LOCALFIELD <Resp|All|Static>
    EFIELD x y z
    SCREEN <ERF|EXP|ESP|GAU|NONE> {length}
    :: FREQUENCY-DEPENDENT PARAMETERS
    FREQUENCY
    OM_H value
    OM_C value
    OM_O value
    OM_N value
    :: CONTROL OVER SOLVER
    ALGORITHM <BEST|DIRECT|BRUTE|SINGLE|MULTI>
    TOLERANCE tol
    NITER iterations
    VOLUME vol_in_nm^3
    MULTIPLIER aterm bterm cterm
    GRID <COARSE|MEDUIM|FINE>
    :: GRADIENT OPTIONS
    FORCEFIELD
    CHEMBOND qmindex dimindex
    COORDDEPEND
    CHEMISORPTION
    COORDPAR atomtype e0 e1 r0 r1 CNmax Rmax Rmin
    CHEMPAR atomtype e0 e1 r0 r1 cutoff
    PROJECTIONMATRIXPOINTS <ALL|CUTOFF radius|OFF>
    :: OUTPUT CONTROL
    PRINTATOMICDIPOLES
    PRINTLJPAR
    DEBUG
    LOCALDIM
    LOCALDIRECT
    DIMBUFFER
    QMBUFFER
    CUTOFFDIST
  END

``<DRF|CPIM|PIM>``
  DIM/QM relies on one of three descriptions of the system: Discrete Reaction Field (DRF), where the atoms interact via induced dipoles and static charge, Capacitance Polarizability Interaction Model (CPIM), where the atoms interact via induced dipoles and induced charges, and Polarizability Interaction Model (PIM), where the atoms interact via induced dipoles only.  DRF is best for solvents, CPIM is best for small metal nanoparticles, and PIM is best for large metal nanoparticles. One and only one of these three keys must be included in every DIM/QM calculation. However, in ADF2019 there is also the expert DRF2 possibility, which allows for DRF gradients but should be used cautiously.

``NOPOL``
  The NOPOL key turns off the polarization terms, and thus all induced dipoles are zero.  This key is only valid for DRF or CPIM calculations. 

``NOCHAR``
  The NOCHAR key turns off the charge terms, and thus all induced or static charges are zero.  This key is only valid for DRF or CPIM calculations. 

``NOCHOSS``
  The NOCROSS key turns off the charge-dipole interactions.  This key is only valid for CPIM calculations. 

``DDA``
  By default, the dipole-dipole, charge-dipole and charge-charge interactions are screened to take into account that atoms are not point charges.  The DDA key will turn off this screening so that the results can be compared directly to the discrete dipole approximation (DDA). 

``FULLGRID``
  This is used in conjunction with the frozen density approximation. 

.. index:: SEROA

.. index:: plasmonic CD

``LOCALFIELD <Resp|All|Static>``
  Default is All, when no option is specified. When the molecule interacts with a (for example) metal nanoparticle, there are two types of interactions: the image field and the local field. The image field is caused by the dipoles induced into the nanoparticle by the molecule's electron density. This is always taken into account in a DIM/QM calculation. The local field arises by direct interactions of the nanoparticle with an external field. Addition of the LOCALFIELD key causes the DIM/QM calculation to include this effect, but by default this is not included in a DIM/QM calculation. In ADF2016 the correct behavior with local fields for the electric dipole-dipole, electric dipole-quadrupole, and electric dipole-magnetic dipole response tensors in the velocity gauge is implemented. This allows for correct calculation of surface-enhanced Raman optical activity (SEROA) (Ref. [#ref4]_) and plasmonic circular dichroism (Ref. [#ref6]_).

  Default option should be used in most situations as other options are expert options. In effort to speed up calculation times, one can request to just calculate the Local Fields during the response section of the calculation by using the Resp keyword after local fields. All will calculate the local field for both ground state calculations and the response calculations, while static will calculate the local field during the ground state only. 

``EFIELD x y z``
  The EFIELD key is used to include an external static electric field in the vector x y z.  Internally, the static charges used in a DRF calculation use AMS's System%ElectrostaticEmbedding, and therefore use of the AMS System%ElectrostaticEmbedding is not allowed icw the DIMQM block. This key is included so the user may include an external static electric field.

``SCREEN <ERF|EXP|ESP|GAU|NONE> {length}``
  The SCREEN key indicates what functional form is used to screen the interactions between each DIM atom and the QM density.  The choices are ERF (error function), EXP (exponential), ESP (error function for potential operator only), GAU (Gaussian), or NONE.  For CPIM and PIM the default is GAU; for DRF, the default is ESP.  In all cases, the default screening length is 1.0, but this may be changed with the optional length parameter. 

``FREQUENCY``
  The FREQUENCY key turns on frequency-dependent parameters.

``OM_[HCON] value``
  The OM_H, OM_C, OM_O, and OM_N keys provide the resonance frequency (in atomic units) for the elements H, C, O and N, respectively.  These keys are only for use with DRF and only when the older EXTERNALS block is used. 

``ALGORITHM <BEST|DIRECT|BRUTE|SINGLE|MULTI>``
  DIM/QM can choose between several solver algorithms.  The DIRECT method solves the linear system of equations directly with a LAPACK routine; this should be considered the most robust method, but scales poorly with the number of atoms (O(N\ :sup:`3` ) where N is the number of atoms in the system).  The other three methods use an iterative technique, The BRUTE method (brute force) takes into account all atoms in the matrix-vector multiply step, and scales as O(N\ :sup:`2` ).  The SINGLE method uses the single-level cell-multipole-method (CMM), wherein dipoles that are spatially similar are collected into a multipole moment which effectively reduces the system size.  This also scales as O(N\ :sup:`2` ) but with a lower prefactor than BRUTE.  The MULTI method uses the multi-level cell-multipole-method, which uses larger and large multipole the farther apart the dipoles are.  This is the fastest method and scales as O(N log N). 

  Due to technical limitations, CPIM can only use DIRECT.  Further, depending on the system size DIRECT or SINGLE may be more efficient than MULTI.  To simplify choosing the solving algorithm, there is a BEST option that chooses the best algorithm for the particular system.  BEST is the default option for algorithm. 

``TOLERANCE tol``
  The TOLERANCE key allows the user to specify a tolerance for the iterative solver.  By default the tolerance is based on ADF's INTEGRATION key.  This has no effect with the DIRECT solver. 

``NITER iterations``
  The NITER key allows the user to specify the maximum number of iterations for the iterative solver.  By default this is MAX(N/100, 200) where N is the number of DIM atoms. 

``VOLUME vol_in_nm3``
  The VOLUME key is used to specify the DIM system volume.  The volume is used to determine how to partition the system for the cell multipole method (ALGORITHM options SINGLE or MULTI), and is also use to determine the scattering efficiencies for frequency-dependent polarizability calculations.  The volume does not need to be supplied; if it is missing, it will be calculated based on each atom's radius and the MULTIPLIER key. 

``MULTIPLIER aterm bterm cterm``
  An efficient way to get a approximation for the volume of the system is to sum the volume of each atom in the system, modified to account for the space between the atoms.  This is done by modifying the atomic radius by a formula that takes into account the number of DIM atoms so that the effective radius changes with surface-to-bulk ratio.  This formula is given by  

  *r*\ :sub:`eff`  = -*ar*/N\ :sup:`b`  + *c* 

  where *r* is the atomic radius, *r*\ :sub:`eff`  is the effective radius, N is the number of atoms, and the *a*, *b*, and *c* terms are the three parameters defined by the MULTIPLIER key. If the MULTIPLIER key is missing, the default values are 0.7, 0.5, and 1.13, respectively.  

``GRID <COARSE|MEDIUM|FINE>``
  In the cell multipole method (ALGORITHM options SINGLE or MULTI), a certain number of the closest atom interactions must be calculated explicitly.  The GRID key controls how many atoms must be calculated this way, with COARSE being the least and FINE being the most. COARSE will be the fastest to calculate but may be numerically unstable.  FINE is slowest to calculate but is the most stable.  If the GRID key is missing, the default is MEDIUM. 

``FORCEFIELD``
  The FORCEFIELD key indicates that the DIM/QM calculation will include the DIM/QM force field. Currently the only maintained potential is the Lennard-Jones 12-6 potential (see  Ref. [#ref1]_). This key is required to perform a DIM/QM geometry optimization and vibrational frequencies. By default, the DIM/QM force field is not included into the calculation. DRF gradients are not implemented.

  Currently, DIM/QM geometry optimizations must be done in Cartesian coordinates which is specified in the GEOMETRY block. The user should be aware that ADF's default convergence criterion for a geometry optimization are relatively low, thus it is strongly suggested for a DIM/QM calculation to set the numerical integration quality (BeckeGrid) to good and change the convergence criterion of the max gradient to 1E-4. It is not possible to do geometry optimization with DRF.

``COORDDEPEND``
  The COORDDEPEND key indicates that the DIM/QM force field will be coordination dependent. This only effects the Lennard-Jones parameters for DIM atoms (see Ref. [#ref1]_). By default, the DIM/QM force field is not coordination dependent. 

``CHEMISORPTION``
  The CHEMISORPTION key will include chemisorption corrections for all atoms that have chemisorption parameters within a given cutoff radius. By default, the DIM/QM force field does not included chemisorption corrections. 

``COORDPAR atomtype e0 e1 r0 r1 CNmax Rmax Rmin``
  The COORDPAR key allows the user to add additional coordination dependent parameter for a selected element type. atomtype specifies the element type (i.e., Ag for silver) for the given parameter set. e0, e1, r0, and r1 are the coordination dependent Lennard-Jones parameters; see Ref. [#ref1]_) for more details. The coordination numbers of the DIM atoms are computed as an effective coordination number. This scheme requires a maximum and minimum cutoff distances, Rmax and Rmin respectively, and a maximum coordination number, CNmax. All parameters need to be in atomic units.  

``CHEMPAR atomtype e0 e1 r0 r1 CUTOFF``
  The CHEMPAR key allows the user to add additional chemisorption dependent parameter for a selected element type. atomtype specifies the element type (i.e., N for nitrogen) for the given parameter set. e0, e1, r0, and r1 are the coordination dependent Lennard-Jones parameters; see Ref. [#ref1]_) for more details. The code determines if there is a chemical bond by a cutoff distance parameter, CUTOFF. If the QM-DIM bond is within the cutoff, the code uses the chemisorption parameter; otherwise, the code uses the standard parameter set. All parameters need to be in atomic units. 

``CHEMBOND qmindex dimindex``
  The CHEMBOND key indicates that there will a chemisorption correction used for the bond between the specified QM and DIM atoms. The user may repeat the CHEMBOD key up to 50 times to specify up to 50 different chemical bonds for the force field. The qmindex is an integer based on the order of atoms in the ATOMS block; i.e. the fifth QM atom in the ATOMS block would have qmindex = 5. The dimindex is the same but corresponds to the DIM atom involved in the bond. This key should only be used when the CHEMISORPTION key is also specified. When using CHEMBOND, the cutoff distance parameter for chemisorption correction parameter key will be ignored. It is suggested to use CHEMBOND if the user is generating a potential energy surface with a chemisorbed QM system.

``PROJECTIONMATRIXPOINTS <ALL|CUTOFF radius|OFF>``
  The PROJECTIONMATRIXPOINTS key specifies what DIM atoms to include for the projection matrix when removing rigid motions out of the gradient. The methods available are ALL, CUTOFF, or OFF.  The ALL option causes PROJECTIONMATRIXPOINTS to include all DIM atoms. OFF will turn off the removal of rigid motions. CUTOFF includes any DIM atom points within a cutoff radius from the center of mass of the QM system to the DIM atom points and requires a cutoff radius to be given in Angstrom. This key only applies to a geometry optimization.  If the PROJECTIONMATRIXPOINTS key is not given, the option CUTOFF with a cutoff radius of 25.4 Angstrom is assumed. 

``PRINTATOMICDIPOLES``
  The PRINTATOMICDIPOLES key causes all the induced dipole moments of each DIM atom to be printed at the conclusion of each SCF cycle and each RESPONSE or AORESPONSE polarizability calculation. Because DIM/QM is typically used with many thousands of atoms, this can result in a large output file, but they may be useful for debugging purposes or to calculate electric fields. By default these are not printed. 

``PRINTLJPAR``
  The PRINTLJPAR key specifies that all Lennard-Jones parameters used for the calculation will be printed in the output file. The QM atoms' Lennard-Jones parameters are also printed with the DEBUG key. 

``DEBUG``
  The DEBUG key will print out extra information in the process of the calculation. 

``LocalDIM``
  LocalDIM performs the calculation fully for a specified CutOffDist (in Bohr) but ignores the image dipoles from atoms outside of this distance. This option should converge to the full simulation and the distance should be chosen wisely. Must have LocalDirect keyword as well.

``LocalDirect``
  Tells LocalDIM calculation to use the direct solver for the DIM dipoles. This solver is generally much faster than the other solvers available when the system is small. Currently, LocalDIM only works with the intention of using this faster solver, so this option must be used with LocalDIM

``DIMBUFFER``
  Default value = 0.85. This keyword tells DIM how to decide for DRF2 calculations which atoms are in the same molecular grouping. This grouping decides if the charges polarize other atomic dipoles. For example, the charge for atoms in the same molecule will not polarize each other but they will polarize atomic dipoles in other molecules. This value should be adjusted based on the XYZ you supply and checked in the output file to ensure proper grouping behavior. 

``QMBUFFER``
  Default value = 0.85. This keyword tells DIM how to decide if the QM atoms are “bonded” to one another to determine the force field parameters needed calculations requiring DIM/QM gradient terms. As with the DIMBUFFER keyword, this value should be adjusted for each system and checked in the output file to ensure proper behavior. 

``CutOffDist``
  Distance in Bohr that determines if the image dipoles of a DIM atom is included in a LocalDIM calculation. Any DIM atom that is inside the supplied distance from any QM atom will be fully included in the calculation.


DRF atomic parameters
---------------------

The EXTERNALS block key controls the input data for the MM atoms. The EXTERNALS block is designed for DRF calculations.  For each MM atom the following data are required: 

.. _keyscheme EXTERNALS: 


::

  EXTERNALS
   atm num grp-nam grp-num, char, x, y, x, pol
   ...
   GROUP
   {...}
  end

``atm``
  Type of atom, i.e., H, O, ... 

``num``
  number of atoms (optional) 

``grp-nam``
  Name of the group to which the atom belongs 

``grp-num``
  Number of the group to which the atom belong 

``char``
  atomic charge (in atomic units) 

``x``
  x-coordinate 

``y``
  y-coordinate 

``z``
  z-coordinate 

``pol``
  atomic polarizability (in atomic units) 

``GROUP``
  Indicates the end of group 

The separation of molecules into GROUP's are important. Since in the many-body polarization operator only inter-molecular interactions, i.e. only interaction between sites which do not belong to the some group, are included. Therefore, it is important that the combined string (grp-nam + grp-num) is unique for each GROUP. 

An example of a EXTERNALS block for two water molecules:

::

  EXTERNALS
   O 4 water 2, -0.6690, -11.380487, -11.810553, -4.515226, 9.3005
   H 5 water 2,  0.3345, -13.104751, -11.837669, -3.969549, 0.0690
   H 6 water 2,  0.3345, -10.510898, -12.853311, -3.320199, 0.0690
   GROUP
   O 7 water 3, -0.6690,  -1.116350,   9.119186, -3.230948, 9.3005
   H 8 water 3,  0.3345,  -2.822714,   9.717033, -3.180632, 0.0690
   H 9 water 3,  0.3345,  -0.123788,  10.538199, -2.708607, 0.0690
   GROUP
   {...}
  end


.. _keyscheme DIMPAR: 

DIM atomic parameters
---------------------


In this block, the parameters for the DIM atoms are defined.

::

  DIMPAR
    Element
      RAD val
      POL val
      CAP val
      CHAR val
      OM val
      OM1 val
      OM2 val
      GM1 val
      GM2 val
      SIZE val
      BOUND val
      STATIC
      EXP /path/to/experimental/dielectric/file
      DRUDE plasma damping {EV}
      FERMI val
      <LRTZ|LRTZ1> osc res damp {EV}
      LRTZ2 osc pls res damp {EV}
      LRTZ3 pls res damp {EV}
    SUBEND
    XYZ
      {/absolute/path/to/coordinates.xyz}
      {natoms
       elem x.xxx y.yyy z.zzz
       elem x.xxx y.yyy z.zzz
       elem x.xxx y.yyy z.zzz
       ...}
    SUBEND
    LCLFLD /absolute/path/to/localfields.txt
      {freq1 freq2 freq3 ..
       .....
      }
    GROUP groupname
      natoms
       elem x.xxx y.yyy z.zzz {pol=pol} (cap=cap} {char=char} {..}
       elem x.xxx y.yyy z.zzz {pol=pol} (cap=cap} {char=char} {..}
       elem x.xxx y.yyy z.zzz {pol=pol} (cap=cap} {char=char} {..}
       ...
    SUBEND
  END

``Element``
  Within the DIMPAR block, you will need a sub-block that defines the parameters for each element that is in your DIM system.  You will need to replace 'Element' with the element you are assigning parameters to, as in::

   Ag
    ...
   SUBEND

  if you are assigning parameters to Ag.  Note that the first letter MUST be capitalized and the second MUST be lowercase. 

  ``RAD val``
     RAD specifies the atomic radius in the unit defined by the input file.  RAD is required for all PIM calculations, all calculations with ALGORITHM options SINGLE or DIRECT, and all frequency-dependent calculations where the AORESPONSE LIFETIME key is given. 

  ``POL val``
    POL specifies the polarizability parameter (in a.u.) used in DRF or CPIM.   

  ``CAP val``
    CAP specifies the capacitance parameter (in a.u.) used in CPIM.   

  ``CHAR val``
    CHAR specifies the atomic charge (in a.u) used in DRF.   

  ``OM val``
    OM specifies the resonance frequency (in a.u) used in DRF.  This replaces the OM_[HCON] key in the DIMQM block. 

  ``OM1 val``
    OM1 specifies the :math:`\omega`\ :sub:`1`  parameter (in a.u) used in CPIM. 

  ``OM2 val``
    OM2 specifies the :math:`\omega`\ :sub:`2`  parameter (in a.u) used in CPIM. 

  ``GM1 val``
    GM1 specifies the :math:`\gamma`\ :sub:`1`  parameter (in a.u) used in CPIM. 

  ``GM2 val``
    GM2 specifies the :math:`\gamma`\ :sub:`2`  parameter (in a.u) used in CPIM. 

  ``SIZE val``
    SIZE specifies the size-dependent parameter used in CPIM. 

  ``STATIC``
    Calculate the response properties for this atom type as static during a frequency dependent calculation.

  ``EXP /absolute/path/to/experimental/dielectric/file``
    In PIM, the atomic polarizabilities are calculated from the dielectric constant. If you have access to the experimental dielectric constant, this may be supplied directly to DIM/QM.  The values will be splined, so it is not necessary to ensure that each frequency at which you are calculating be in the file.  DIM/QM expects the file to be formatted with the wavelength (in nm) in the first column, the real part of the dielectric in the second column, and the imaginary part of the dielectric in the third column.  All other columns that may exist will be ignored, as well as lines beginning with the hash (#) symbol. 

  ``BOUND val``
    A Drude function is typically written as 

    .. math::

      \epsilon_\infty - \frac{\omega_p^2}{\omega (\omega + i \gamma)}

    with the second term being the Drude function, and the first term accounting for bound electrons.  For a conductor with no bound electrons, :math:`\epsilon`\ :sub:`∞`  = 1 which is the default value for BOUND.  To account for bound electrons you may set BOUND to a value greater than 1.  This key only affects PIM. 

  ``DRUDE plasma damping {EV}``
    The formula for a Drude function is 

    .. math::
      
      \epsilon_\infty - \frac{\omega_p^2}{\omega (\omega + i \gamma)}

    where :math:`\epsilon`\ :sub:`∞` represents the bound electrons (as discussed for BOUND), :math:`\omega`\ :sub:`p`  (plasma) is the plasma frequency, and :math:`\gamma` (damping) is the damping parameter (decay rate).  Optionally, EV may be added to specify the values be read in units of electron volts, otherwise they are read in units of a.u. This key only affects PIM. 

  ``FERMI val``
    The FERMI key is used to specify a Fermi velocity (in m/s) so that the Drude function may be size-corrected using a modified Drude function: 

    .. math::
      
      \epsilon_\infty - \frac{\omega_p^2}{\omega (\omega + i (\gamma + v_\text{fermi}/R_\text{eff}))}


    where +v\ :sub:`fermi`  is the Fermi velocity and R\ :sub:`eff`  is the effective nanoparticle radius.  This can also be used in conjunction with EXP and DRUDE to size-correct experimental dielectric parameters.  This key only affects PIM::

      <LRTZ|LRTZ1> osc res damp {EV} 
      LRTZ2 osc pls res damp {EV} 
      LRTZ3 pls res damp {EV}

    There are three forms of the Lorentzian function seen in the literature: 

    .. math::

     & \sum_n \frac{f_n \Omega_{0,n}^2}{\Omega_{0,n}^2 - \omega^2 - i \Gamma_n \omega} \\
     & \sum_n \frac{f_n \omega_{p}^2}{\Omega_{0,n}^2 - \omega^2 - i \Gamma_n \omega} \\
     & \sum_n \frac{\Omega_{p,n}^2}{\Omega_{0,n}^2 - \omega^2 - i \Gamma_n \omega}


    where :math:`\Omega`\ :sub:`0,n`  (res) is a bound electron resonance frequency, f\ :sub:`n`  (osc) is a bound electron oscillator strength, :math:`\Gamma`\ :sub:`n`  (damp) is a bound electron excited state decay rate (or damping parameter), :math:`\omega`\ :sub:`p`  (pls) is the free electron plasma frequency, and :math:`\Omega`\ :sub:`p,n`  (pls) is the bound electron plasma frequency.  You may choose the Lorentzian for against which your parameters were parametrized.  The top form is LRTZ1, the middle is LRTZ2, and the bottom is LRTZ3.  Because LRTZ1 is the most common, it is also aliased as LRTZ.  Optionally, EV may be added to specify the values be read in units of electron volts, otherwise they are read in units of a.u. This key only affects PIM.  You may give any of the form of the LRTZ key up to 50 times supply up to 50 Lortenzian functions to make a Drude-Lorentz function. 

``XYZ``
  The XYZ sub-block is where the DIM atom coordinates are given.  Two methods of supplying coordinates are allowed. 

  ``In-File Coordinates``
    As an example of how to supply coordinates in-file, imagine you wish to calculate a Au dimer system on the Z-axis.  You might define your coordinates as::

      XYZ
       2
       Au 0.0 0.0 0.0
       Au 0.0 0.0 3.0
      SUBEND

    The first line gives the number of atoms to follow.  Every line after that contains the element in the first column (first letter MUST be capitalized, second MUST be lowercase), then the x-component, then the y-component, then the z-component.  You may not number the atoms. 

  ``External File Coordinates``
    When the DIM system size becomes large, it is often more convenient to keep the DIM coordinates in a separate file.  The XYZ block would then look like::

      XYZ
       /absolute/path/to/coordinates.xyz
      SUBEND

    Note that you MUST include the absolute path to your file and the file name must end with ``.xyz``. 

    The .xyz file is set up identically to the in-file table, except that there is a comment line between the number of atoms and the first atom.  The .xyz file for our dimer system would be::

      2
      A gold dimer (this line will be ignored)
      Au 0.0 0.0 0.0
      Au 0.0 0.0 3.0

``LCLFLD /absolute/path/to/localfields.txt``
  Text file of the local field induced dipoles that can be read in to reduce calculation time. The file must be in the following format::

      freq1 freq2 freq3  ...
      1
      X
      Atom1R-DipoleX    Atom1R-DipoleY    Atom1R-DipoleZ
      Atom1I-DipoleX    Atom1I-DipoleY    Atom1I-DipoleZ
      Atom2R-DipoleX    Atom2R-DipoleY    Atom2R-DipoleZ
      Atom2I-DipoleX    Atom2I-DipoleY    Atom2I-DipoleZ
      ...
      Y
      Atom1R-DipoleX    Atom1R-DipoleY    Atom1R-DipoleZ
      Atom1I-DipoleX    Atom1I-DipoleY    Atom1I-DipoleZ
      Atom2R-DipoleX    Atom2R-DipoleY    Atom2R-DipoleZ
      Atom2I-DipoleX    Atom2I-DipoleY    Atom2I-DipoleZ
      ...

  Here freq1 freq2 freq3 ... are the frequencies that are being used in the response calculation and 1 tells the program that the following dipoles are to be used with the first frequency. X and Y tell the program that these are the induced dipoles from perturbations in the X and Y Cartesian direction respectively. 


``GROUP groupname``
  The GROUP sub-block is where the DIM atom coordinates and parameters are given. Combines the XYZ subblock and Element subblock. A (unique) groupname is required (maximum 10 characters).

  Example for a water molecule::

     GROUP water1
     3
     O  0.00000  0.00000  0.59372  pol=5.7494  char=-0.6690
     H  0.00000  0.76544 -0.00836  pol=2.7927  char=0.3345
     H  0.00000 -0.76544 -0.00836  pol=2.7927  char=0.3345
     SUBEND

  The first line gives the number of atoms to follow.  Every line after that contains the element in the first column (first letter MUST be capitalized, second MUST be lowercase), then the x-component, then the y-component, then the z-component.  You may not number the atoms. At the end of the line for each element you can specify the DIM/QM parameters, as in the format in the example. The DIM/QM parameters can be 'POL', 'CAP', 'CHAR', 'OM1', 'OM2', 'GM1', 'GM2', 'SIZE', 'RAD', 'SPILLOUT', 'BOUND', 'DRUDE', 'FERMI', 'LRTZ', or 'EXP'.

.. only:: html

  .. rubric:: References

.. [#ref1] J.L. Payton, S.M. Morton, Justin E. Moore, and Lasse Jensen, *A discrete interaction model/quantum mechanical method for simulating surface-enhanced Raman spectroscopy*, `Journal of Chemical Physics 136, 214103 (2012) <https://doi.org/10.1063/1.4722755>`__ 

.. [#ref2] P.T. van Duijnen and M. Swart, *Molecular and Atomic Polarizabilities: Thole's Model Revisited*, `Journal of Physical Chemistry A 102, 2399 (1998) <https://doi.org/10.1021/jp980221f>`__ 

.. [#ref3] L.\  Jensen, P.-O. Astrand, A. Osted, J. Kongsted and K.V. Mikkelsen, *Polarizability of molecular clusters as calculated by a dipole interaction model*, `Journal of Chemical Physics 116, 4001 (2002) <https://doi.org/10.1063/1.1433747>`__ 

.. [#ref4] D.V. Chulhai and L. Jensen, *Simulating Surface-Enhanced Raman Optical Activity Using Atomistic Electrodynamics-Quantum Mechanical Models*, `Journal of Physical Chemistry A 118, 9069 (2014) <https://doi.org/10.1021/jp502107f>`__ 

.. [#ref5] Z.\  Hu, D.V. Chulhai, and L. Jensen, *Simulating Surface-Enhanced Hyper-Raman Scattering Using Atomistic Electrodynamics-Quantum Mechanical Models*, `Journal of Chemical Theory and Computation 12, 5968 (2016) <https://doi.org/10.1021/acs.jctc.6b00940>`__

.. [#ref6] D.V. Chulhai and L. Jensen, *Plasmonic Circular Dichroism of 310- and α-Helix Using a Discrete Interaction Model/Quantum Mechanics Method*, `Journal of Physical Chemistry A 119, 5218 (2015) <https://doi.org/10.1021/jp5099188>`__ 

.. [#ref7] L.\  Jensen, P.T. van Duijnen and J.G. Snijders, *A discrete solvent reaction field model within density functional theory*, `Journal of Chemical Physics 118, 514 (2003) <https://doi.org/10.1063/1.1527010>`__ 

.. [#ref8] L.\  Jensen, P.T. van Duijnen and J.G. Snijders, *A discrete solvent reaction field model for calculating molecular linear response properties in solution*, `Journal of Chemical Physics 119, 3800 (2003) <https://doi.org/10.1063/1.1590643>`__ 

.. [#ref9] L.\  Jensen, P.T. van Duijnen and J.G. Snijders, *A discrete solvent reaction field model for calculating frequency-dependent hyperpolarizabilities of molecules in solution*, `Journal of Chemical Physics 119, 12998 (2003) <https://doi.org/10.1063/1.1627760>`__ 

.. [#ref10] L.\  Jensen, M. Swart and P.T. van Duijnen, *Microscopic and macroscopic polarization within a combined quantum mechanics and molecular mechanics model*, `Journal of Chemical Physics 122, 34103 (2005) <https://doi.org/10.1063/1.1831271>`__ 

.. [#ref11] L.\  Jensen, `Modelling of optical response properties: Application to nanostructures, <http://downloads.scm.com/Doc/jensen.pdf>`__ PhD thesis, Rijksuniversiteit Groningen, 2004. 
