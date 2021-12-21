.. _ACCURACY:
.. index:: precision

.. _keyscheme BECKEGRID:

Numerical Integration
=====================

Many integrals in ADF are calculated via numerical integration. The integration grid used for computing these integrals is therefore an important technical aspect of an ADF calculation, affecting both the accuracy of the results and the computation time.


Becke Grid
----------

The default numerical integration grid is a refined version of the fuzzy cells integration scheme developed by Becke [#ref1]_. The implementation in ADF is described in Ref. [#ref2]_.

The quality of the Becke integration grid can be changed within the BECKEGRID block key::

  BECKEGRID
     Quality [basic|normal|good|verygood|excellent]
  End

``Quality``
  **Default: Normal**. For a description of the various "qualities" and the associated numerical accuracy, see Ref. [#ref2]_.
  The integration grid quality defined in the BECKEGRID block key overrules the :ref:`NumericalQuality <keyscheme NUMERICALQUALITY>`.

**Advanced options:**

::

  BECKEGRID
    {QualityPerRegion
       Region myregion
       Quality {Basic|Normal|Good|VeryGood|Excellent}
    End}
    {qpnear qpnear}
    {RadialGridBoost boost}
  End

``QualityPerRegion``
   One can overwrite the integration grid quality for atoms in a particular region. :ref:`example Multiresolution_H2O` illustrates how to use this option.

``qpnear``
   **Default: 4.0 Angstrom**. Only relevant if you have specified point charges in the input file. ADF generates grids only about those point charges that are close to any real atoms. The criterion, input with the qpnear subkey, is the closest distance between the point charge at hand and any real atom. Any input value is interpreted in the unit-of-length specified with the Units key.

``RadialGridBoost``
  **Default: 1.0** (or 3 if a numerically sensitive functional is used). The number of radial integration points will be boosted by this factor. Some XC functionals require very accurate radial integration grids, so ADF will automatically *boost* the radial grid for the following numerically sensitive functionals: ``LibXC M05``, ``LibXC M05-2X``, ``LibXC M06-2X``, ``LibXC M06-HF``, ``LibXC M06-L``, ``LibXC M08-HX``, ``LibXC M08-SO``, ``LibXC M11-L``, ``LibXC MS0``, ``LibXC MS1``, ``LibXC MS2``, ``LibXC MS2H``, ``LibXC MVS``, ``LibXC MVSH``, ``LibXC N12``, ``LibXC N12-SX``, ``LibXC SOGGA11``, ``LibXC SOGGA11-X``, ``LibXC TH1``, ``LibXC TH2``, ``LibXC WB97``, ``LibXC WB97X``, ``MetaGGA M06L``, ``MetaHybrid M06-2X``, ``MetaHybrid M06-HF``, ``MetaGGA MVS``

.. _keyscheme NOBECKEGRID:

**Notes:**

+ The space-partition function used in ADF differs from the one described in Ref. [#ref2]_. The unnormalized partition function used in the program is defined as (:math:`\Omega_I` is an element-dependent parameter: 0.1 Bohr for H, 0.3 Bohr for He-Xe and 0.6 Bohr for Cs-Og):

.. math::

  \mathcal{P}_{i,U} = \begin{cases}
                        1 & \text{if  $r_{i,U}<\Omega_I$} \\
                        0 & \text{if  $\exists j : r_{j,U}<\Omega_J$ } \\
                        \eta_i \frac{e^{-2 (r_{i,U}-\Omega_I) / a_0}}{(r_{i,U}-\Omega_I)^2} &  \text{elsewhere}
                \end{cases}

+ If either the (block) key ``INTEGRATION`` or the key ``NOBECKEGRID`` are used in the input, the Voronoi grid is used::

    NOBECKEGRID

+  A Becke grid of normal quality is roughly equivalent (in both absolute accuracy and computation time) to INTEGRATION 4 (Voronoi scheme), and a Becke grid of good quality is roughly equivalent to INTEGRATION 6 (Voronoi scheme).

+  The Becke grid is not very well suited to calculate Voronoi deformation density (VDD) charges. For accurate calculation of VDD charges the Voronoi integration scheme is recommended.







Voronoi grid (deprecated)
-------------------------

In ADF2012 and previous versions the default integration scheme was the cellular Voronoi quadrature scheme, implemented by te Velde and Baerends [#ref5]_,  [#ref6]_. Starting from ADF2013 this method is no longer the default scheme for integration. The so called Becke grid is the default, see the key BECKEGRID. If the key INTEGRATION is used, the Voronoi scheme will be used. Thanks to a smoother behavior of the relative integration error as a function of the nuclear coordinates, the Becke grid is better suited for geometry optimization and TS search compared to the Voronoi scheme.

The Voronoi integration method requires only one input parameter which determines the precision of numerical integrals and derives from that the number of integration points.

.. _keyscheme INTEGRATION:

::

   INTEGRATION
     accint value
   End

``accint``
   A positive real number: the numerical integration scheme generates points and weights such that a large number of representative test integrals are evaluated with an accuracy of accint significant digits. The default accint is 4.0 (10.0 in Create runs).

The *number* of integration points varies strongly with accint, and this determines to a large extent the computational effort. Decreasing accint from 4.0 to 3.0 for instance roughly halves the number of points (this depends somewhat on the molecule).

The defaults should yield good precision for the very large majority of applications. Lower values (3.0 or even 2.0) can be used if precision is not crucial and the purpose is to get an impression. We recommend that you experiment for yourself to get a feel for how results may vary in quality and computing time.

The default in Create mode is very large: 10.0. This is computationally no problem thanks to the simplicity of the single atom case, in particular due to the high symmetry. There is no reason to override the default integration settings when creating basic atoms.

We've now only explained the normal, simple application of the Integration key, which we hope and expect is adequate for all your computations. Next additional details will be discussed. The distribution of points over space is internally regulated by quite a few parameters. Each of these parameters can be controlled in input. By default they depend on one another, and all of them depend on the main parameter accint. Advanced users may wish to experiment and override the default relations between the parameters.

You may also have rather non-standard applications where the default relations are less adequate. A thorough understanding of the underlying method is required to make a sensible choice for all parameters [#ref6]_,  [#ref8]_.


More options can be defined in the ``Integration`` block. Consult the literature for detailed information about the various schemes.

::

   INTEGRATION
     data
     data
     ...
   end

The block form is used to override default relations between various parameters that are applied in the generation of the integration grid in the polyhedron method [#ref6]_. All these parameters are accessible with subkeys in the data block of Integration. Most of the subkeys are simple keys with one single value as argument; a few subkeys are block-type (sub) keys themselves and hence require the usual format of a data block closed by subend.

``accint``
   The main precision parameter Its value defines the number of significant digits by which an internal set of standard integrals must be evaluated. The number and distribution of integration points is tuned accordingly. For normal applications this should yield a nearly optimal (given the underlying method) generation of points and weights. The default depends on the run type.

``accsph``
   The polyhedron method of generating integration points partitions space in atomic polyhedrons, partitioned in pyramids with their tops at the atom in the center of the polyhedron. A core like atomic sphere is constructed around the atom; this truncates the tops of the pyramids. accsph specifies the test precision for the generation of points within the spheres. By default accsph=accint.

``accpyr``
   Similarly this subkey sets the test level for the parts of the pyramids outside the atomic sphere. Default: accpyr=accint.

``accpyu, accpyv, accpyw``
   The truncated pyramids are mathematically transformed into unit cubes. A product Gauss integration formula is applied to the cubes, with three (test precision) parameters for the three dimensions. Accpyw controls the direction that is essentially the radial integration from the surface of the atomic sphere to the base of the pyramid. The other two control the orthogonal directions (angular). By default all three equal accpyr.

``accout``
   The region of space further away from the atoms, outside the polyhedrons, has its own precision parameter. By default accout=accint.

``nouter``
   This outer region is treated by a product formula: outwards times parallel. The latter involves two dimensions: the surface of the molecule say. The outward integration is performed with Gauss-Legendre quadrature, in a few separate steps. The lengths of the steps are not equal, they increase by constant factors. The total length is fixed. The number of steps is controlled with this subkey; default: 2.

``outrad``
   The parameter that defines the number of Gauss-Legendre integration points for each outward step. The precise relation between the actual number of points and this subkey, and the default relation between outrad and accout can be found in the implementation.

``outpar``
   Similarly the integration in the directions parallel to the surface of the atomic system is controlled by a parameter. See the implementation for details.

``dishul``
   Sets the distance between the outermost nuclei of the molecule and the boundary planes that define the boundary between the polyhedrons and the outer region. By default dishul=2.3*R, where Ris the radius of the largest atomic sphere in the molecule.

``frange``
   The outward range of the *outer region*: integration is not performed to infinity but to a distance frange from the outermost atoms, where all functions can be assumed to be essentially zero. By default frange is derived both from accint, the general precision parameter, and from the present chemical elements: heavier atoms have longer-range functions than hydrogen say. The precise relations can be found in the implementation.

``linrot``
   This parameter is significant only for symmetries with an axis of infinite rotational symmetry: Cand D It is the highest rotational quantum number around this axis that occurs among the integrands. This depends on the employed basis functions and fit functions. By default the program finds this out for itself.

``qpnear``
   If you specify point charges in the input file, there are two considerations implied for the numerical integration grid. First, since the point charges create a Coulomb singularity. The integrands (of for instance the basis function products against the Coulomb potential) can only be evaluated with high precision if the grid around the point charges has spherical symmetry and uses local spherical coordinates, exactly as is done for the atomic nuclei. Second, the point charges do not carry fit or basis functions, hence they play only a role in the more diffuse tails of the actual functions involved in integrals. Therefore, a relative low precision of the integral part close to the point charge may have little effect on the total integration accuracy. Since additional 'spherical centers' with their own surrounding grids increase the total number of points significantly, typically a few thousands *per Coulomb center*, this may result in high computational effort. Therefore, the program generates spherical grids only about those point charges that are close to the other atoms. The criterion, input with the qpnear subkey, is the closest distance between the point charge at hand and any real atom. Default 4.0 Angstrom. Any input value is interpreted in the unit-of-length specified with the Units key.

Next come the subkeys that require a list of data. The subkey must be placed on one line, the data on the next. This somewhat peculiar structure suggests that the subkeys are block keys; however their data blocks have no end code (subend) as for normal block type subkeys.

The list of data for such a subkey contains one value for each atom type. The data must be in the order in which the atom types were defined under atoms, implicitly or explicitly: remember that atoms belonging to different fragment types automatically have different atom types, even if their atom type *names* have been specified as identical under atoms.

``rspher``
   gives the radii of the atomic spheres, one value for each atom type. By default, the radii are derived from the chemical element (heavier atoms get larger spheres) and from the environment: the sphere must not be too large for the atomic cell (polyhedron).

``linteg``
   The maximum angular momentum quantum number of integrands centered on an atom of that type (one value for each atom type). This depends on the basis functions and on the fit functions. By default the program checks the function sets and sets the linteg values accordingly. This subkey is applied for the generation of grid points in the atomic spheres.

Items that relate to geometric lengths (dishul, frange, rspher) must be given in bohr (=atomic units), irrespective of the unit of length defined with units.


Atomic radial grid
------------------

For each atom the charge densities and the coulomb potentials of frozen core and valence electrons are computed in a radial grid and stored on adf.rkf. The values in the points of the molecular numerical integration grid are then evaluated by interpolation from the table of radial values.

The radial grid consists of a sequence of r-values, defined by a smallest value, a constant multiplication factor to obtain each successive r-value, and the total number of points. Equivalently it can be characterized by the smallest r-value, the largest r-value, and the number of points; from these data the program computes then the constant multiplication factor. The characteristics are set with

.. _keyscheme RADIALCOREGRID:


::

   RADIALCOREGRID {nrad=points} {rmin=rmin} {rmax=rmax}

``points``
   The number of radial grid points; default: 5000.

``rmin``
   The shortest distance used in the radial grid; default 1e-6 Angstrom

``rmax``
   The largest distance in the radial grid; default: 100 Angstrom.

rmin and rmax, when specified, are interpreted as specified in units of length defined by units.

The keyword name radialcoregrid has historical reasons: in earlier releases the radial grid was used only for the frozen core density and potential.

.. only:: html

  .. rubric:: References

.. [#ref1] A.D. Becke, *A multicenter numerical integration scheme for polyatomic molecules*, `Journal of Chemical Physics 88, 2547 (1988) <https://doi.org/10.1063/1.454033>`__

.. [#ref2] M.\  Franchini, P.H.T. Philipsen, L. Visscher, *The Becke Fuzzy Cells Integration Scheme in the Amsterdam Density Functional Program Suite*, `Journal of Computational Chemistry 34, 1818 (2013) <https://doi.org/10.1002/jcc.23323>`__.

.. [#ref5] P.M. Boerrigter, G. te Velde and E.J. Baerends, *Three-dimensional Numerical Integration for Electronic Structure Calculations*, `International Journal of Quantum Chemistry 33, 87 (1988) <https://doi.org/10.1002/qua.560330204>`__

.. [#ref6] G.\  te Velde and E.J. Baerends, *Numerical Integration for Polyatomic Systems*, `Journal of Computational Physics 99, 84 (1992) <https://doi.org/10.1016/0021-9991(92)90277-6>`__

.. [#ref8] G.\  te Velde, *Numerical integration and other methodological aspects of bandstructure calculations*, in *Chemistry*. 1990, Vrije Universiteit: Amsterdam.

