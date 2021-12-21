
.. index:: multiplet states 

Multiplet States
****************

Calculations with the ADF enine yield results for one-determinant electronic states, which are not always the 'true' states of the molecule. The evaluation of the correct multiplet energies is not trivial in this approach, see further below the section on multiplet energies. The point is to evaluate a specific multiplet state as a linear combination of selected one-determinant functions, each computed in the field of the so-called Average-of-Configuration (AOC). Typically, in an open shell system, the AOC is the spin-restricted system in which all orbitals in the open shell are degenerate and equally occupied. The AOC serves then as a fragment for the subsequent calculations, in which the different open shell orbitals are occupied differently by specifying the appropriate occupation numbers as explained below. 

**Important:** in these follow-up calculations it is imperative that the results are obtained in the AOC field: no SCF convergence must be carried out, because we only want to assign the electrons differently, while keeping exactly the AOC orbitals. To achieve this, the follow-up calculations must use the keyword SCF, and the subkey iterations must be set to 0. 

Since the ADF enine requires that the point-group symmetry matches not only to the nuclear frame but also to the electronic charge density and MO occupations, these calculations must run in a lower point group symmetry. Often you will also want to run the modified calculations spin-*un*\ restricted. For an example, see the set of sample runs that come with the package and the discussion in the :ref:`Examples <examples>`. 

The calculation of the one-determinant states based on the AOC reference state is controlled with the block ``SLATERDETERMINANTS``,

.. _keyscheme SLATERDETERMINANTS: 

::

  SLATERDETERMINANTS file
  End

were the argument must be a file (including the path). The file must be an ASCII file containing data in the same format as you would supply in the data block, see below. All information on the file until the *eof* must be suitable for the data block, but no record 'end' on the file must be specified: only the *contents* of the data block. 

Alternatively, you can use the SLATERDETERMINANTS block as follows

::

  SLATERDETERMINANTS
   title1
      irrep occups
      irrep occups
      ...
   subend
   title2
      irrep occups
      ...
   subend
   title3
      ...
   subend
   ...
  end

Each 'title' functions as a subkey, but is otherwise an arbitrary string to label the resulting one-determinant calculation. Each such subkey block contains the occupation numbers for a single one-determinant calculation. It is necessary that the calculation uses the reference AOC run as its only fragment file. The occupations in the subkey blocks must be re-arrangements of the AOC open-shell electrons. In the Slaterdeterminants calculation you must explicitly specify the point group symmetry in which you want to run; this must be a lower symmetry than the AOC one, otherwise you couldn't rearrange the open shell electrons. See the sections below on multiplet energies. An sample run is included in :ref:`Examples <examples>`. 

Each 'irrep occups' record specifies the occupations for the indicated irrep in the usual way (see for instance the occupations key). The irrep labels must correspond to the (lower) point group symmetry used in the slaterdeterminants calculation. Note that in an unrestricted calculations, occupations numbers must be given for both spins, using the double slash (//) to separate the occupations for spin-:math:`\alpha` and spin-:math:`\beta`. 

In this setup, the program will for each of the subkey blocks under the slaterdeterminants key execute an SCF calculation with only one cycle, i.e. no convergence, where the start-up field is the fragment field, i.e. the AOC field. So all one-determinant states in this calculation are evaluated in the AOC field. The resulting energies for the distinctly computed one-determinant states can then be combined to the desired multiplet values, corresponding to how the multiplet states are combinations of the one-determinant states.


Multiplet energies
==================

The energies of atomic and molecular multiplet states that correspond to a given electron configuration can be calculated approximately with the method suggested in ref. [#ref1]_. There it is indicated that it would not be justified to take an arbitrary configuration-state function (CSF), defined in general as a linear combination of determinants that has specific spin and space symmetry properties, and use the corresponding alpha and beta spin densities in a DFT energy expression. The same holds true for the densities corresponding to the average-of-configuration (see section 'DFT energy of a one-determinantal wave function', the 'procedure' notes).


Therefore, we restrict ourselves to just computing the DFT energies of single-determinant wavefunctions. Usually (but not always) this is sufficient information to obtain the multiplet energies. The procedure, which is explained in [#ref1]_, requires knowledge of the CSFs belonging to a given configuration. This means that a multiplet state with specific L, ML and S, MS values has to be written as a linear combination of the determinant wavefunctions that belong to the given configuration.
In Ref. [#ref3]_ Claude Daul exploited symmetry in order to simplify the relation between the multiplet energies and single-determinant energies.

It is often advantageous to search for CSFs that consist of one determinant only, since the energy of this determinant should correspond directly to the multiplet energy. Sometimes there is redundancy in the information and there may even be some inconsistency: two determinants may exist that both are CSFs belonging to the same multiplet state but yield somewhat different energies. We will illustrate this for the Carbon atom example treated below.

The discrepancies are a measure of 'error bars' associated with the theoretical multiplet energies. As a matter of fact, there are certain symmetry relations between the energies of the determinants of a configuration, calculated as the expectation value of the determinant for the full many-electron Hamiltonian. An example is the equal energy for the determinants of a :math:`p^1` configuration, whether the electron is placed in the :math:`p_0` (= :math:`p_z`) orbital or in the :math:`p_{+1} (=(p_x + i p_y) / \sqrt{2})` orbital. This equality is not obtained with present-day density functionals, leaving an ambiguity ('error bar') in the determination of the energy. A more complete treatment of the symmetry relations between determinant energies is given in [#ref3]_.

**Warning:** However, there have occasionally been found inconsistent results. A comparison to the results obtained by the procedure outlined in [#ref1]_ may show significant differences and the latter seem more accurate and consistent.


**DFT energy of a one-determinantal wave function**

The determinant corresponds to a well defined :math:`\rho^\alpha` and :math:`\rho^\beta`. Suppose we are dealing with a :math:`d^2` configuration and we wish to know the energy of

.. math::

  D_1 = | d_2^\alpha (1) d_1^\alpha (2) |

where :math:`d_m` has the :math:`Y_{2m}` angular part. This determinant is a CSF of the :math:`^3 F` multiplet


.. math::

  D_1 = | ^3 F ; M_L = 3 ; M_S = 1 \rangle

We can easily transform to the real spherical harmonics that are used in the ADF enine:

.. math::

  Z_{lm}^C = \frac{1}{\sqrt{2}} (Y_l^{-m} + Y_l^{-m*}) = \frac{1}{\sqrt{2}} (Y_l^{-m} + (-1^m) Y_l^{m})

.. math::

  Z_{lm}^S = \frac{i}{\sqrt{2}} (Y_l^{-m} + Y_l^{-m*}) = \frac{i}{\sqrt{2}} (Y_l^{-m} + (-1^m) Y_l^{m})


with back transformations:

.. math::

  Y_l^m = & \frac{1}{\sqrt{2}} (-1)^m (Z_{lm}^C + i Z_{lm}^S) \\
  Y_l^{-m} = & \frac{1}{\sqrt{2}} (Z_{lm}^C - i Z_{lm}^S)

Here the superscripts c and s stand for the cosine, respectively sine type of combinations of :math:`exp(-im \phi)` and :math:`exp(im \phi)`. This yields explicitly:


.. math::
   
  d_{z^2} & = d_0    \\
  d_{xz} & = 1/\sqrt{2} (d_{-1} - d_{1})   \\
  d_{yz} & = i/\sqrt{2} (d_{-1} + d_1)   \\
  d_{x^2-y^2} & = 1/\sqrt{2} (d_{-2} + d_2)   \\
  d_{xy} & = i/\sqrt{2} (d_{-2} - d_2)   \\
  d_{0} & = d_{z^2}   \\
  d_{1} & = -1/\sqrt{2} (d_{xz} + i d_{yz})   \\
  d_{-1} & = 1/\sqrt{2} (d_{xz} - i d_{yz})   \\
  d_{2} & = 1/\sqrt{2} (d_{x^2-y^2} + i d_{xy})   \\
  d_{-2} & = 1/\sqrt{2} (d_{x^2-y^2} - i d_{xy})

For :math:`D_1` we obtain:


.. math::

  \rho_\alpha & = |d_2|^2 + |d_1|^2 = 1/2 |d_{x^2-y^2}|^2 + 1/2 |d_{xy}|^2 + 1/2 |d_{xz}|^2 + 1/2 |d_{yz}|^2 \\
  \rho_\beta & = 0

The fractional occupations have to be used in order to generate the densities ρα and ρβ and the corresponding density matrices :math:`\rho_\alpha` and :math:`\rho_\alpha`. The density matrices can be used to calculate the energy of D1 (and :math:`^3 F`) with respect to the energy of the 'master fragment', which should be the restricted atom with :math:`d^2` occupation. Other determinants of this configuration can be treated similarly to obtain more multiplet energies of the :math:`d^2` configuration.

Below is an example of how you can obtain determinant energies 'by hand', i.e. by carrying out a specific sequence of ADF calculations. The ADF enine supports an automatic procedure to do this, using the input key SLATERDETERMINANTS, see the ADF User's Guide, the :ref:`Examples <examples>`, and below.



**Procedure**

1. Determine a set of orbitals belonging to the given configuration. These orbitals are generated in what we call the average-of-configuration (AOC) calculation. This is a spin-restricted SCF calculation where the electrons of the configuration are distributed equally over the subspecies of the open shell irreps in order to retain the A1 symmetry of the total density in the symmetry group of the molecule. For instance, in case of an atomic d\ :sup:`2`  configuration, the AOC calculation can be done in symmetry atom with occupation 2 in the d irrep. In case of an t\ :sub:`2g` \ :sup:`5`  e\ :sub:`g` \ :sup:`1`  configuration of an octahedral complex, the AOC calculation requires an occupation of 5 electrons in the t\ :sub:`2g` , and 1 electron in the e\ :sub:`g` . The result file adf.rkf of the AOC calculation has to be saved, to be used as a fragment file in the subsequent calculations. 

2. The AOC is used as a fragment in all subsequent calculations that are performed to obtain single determinant energies. This means that those single determinant energies are always with respect to the AOC energy. This is a case where there is only one "fragment", which is actually the complete system, but in a different electronic configuration and in possibly a different symmetry group. 

Suppose that a single determinant corresponds to spin-up and spin-down densities :math:`\rho^\alpha`  and :math:`\rho^\beta` , i.e. to specific spin-unrestricted occupations of the AOC orbitals. These densities :math:`\rho^\alpha`  and :math:`\rho^\beta`  correspond to a symmetry group that will in general be a subgroup of the symmetry group of the molecule. For instance, the occupation (p\ :sub:`+1` :math:`\alpha`)\ :sup:`1`  in the case of an atomic p\ :sup:`1`  configuration corresponds to 

.. math::

  \rho^\alpha = 1/2 p_x^2 + 1/2 p_y^2

with D\ :sub:`∞h`  symmetry. 

To obtain the energy of the determinant wave function we must now perform *one* cycle (iterations= 0 in the block key SCF) of a spin-unrestricted calculation, with AOC as (the only) fragment with alpha and beta occupation numbers (using the input key occupations) such that :math:`\rho^\alpha`  and :math:`\rho^\beta`  result. Note that the appropriate (lower) symmetry point group must be specified in the input file. 

Occasionally, the single determinant corresponds to a closed shell configuration in the appropriate lower symmetry, for instance determinant D\ :sub:`10`  = \|0\ :sup:`+`  0\ :sup:`-` \| of the p\ :sup:`2`  configuration of Carbon, with density r=p\ :sub:`z` \ :sup:`2` . In that case the one-cycle calculation can of course be spin-restricted. 

N.B.1. One cycle will regenerate the SCF orbitals of AOC, if the same field is used as the converged AOC field. This will actually be the case because the starting potential is taken from the fragment adf.rkf file. The key modifystartpotential must not be used (the density should be distributed equally over the spins). 

N.B.2. After diagonalization in the one-cycle run, the AOC orbitals have been obtained again and are occupied as specified. The ('bonding') energy is calculated from the resulting charge density. 

Remarks:  

+ If one does not perform just one cycle, but instead converges the unrestricted calculation, the energy will be lowered by 'polarization' of the orbitals. It is theoretically not so clear what the status of such converged energies is. Usually the energy lowering is in the order of 0.1 eV, but it may be quite a bit larger. 

+ It is not necessary to use AOC as fragment in the single-determinant runs. It is also perfectly allowed to run all calculations (ground state, AOC, determinants) from one set of fragments, for instance the standard atomic fragments. Since we must arrange that the one-cycle determinant calculations use the AOC field, so as to reproduce the AOC orbitals, we must then supply the result file adf.rkf of the AOC run as a restart file, using the key restart; see the adf User's Guide. Of course, in such an approach the computed energies are with respect to another reference, for instance the restricted atoms.

**Results for first period atoms**

In one of the next sections tables are given for the energy lowering in going from the converged spherically symmetric spin-restricted atom (the 'master' fragment) to specific one-determinant wavefunctions with the orbital occupations as specified. Note that the p\ :sub:`x`  and p\ :sub:`y`  populations are always equal; only their sum is given. In many cases the determinant corresponds to a specific state, which is then given in the last column. For each atom, the first calculation is for the spherically symmetric spin-*un*\ restricted atom. These tables are now obsolete, all information needed to obtain the atomic reference energies, i.e. the ground state multiplet energy with respect to the AOC, can be found in ref. [#ref6]_. 

Examples worked out for all first period atoms: 

**H**: Configuration (1s)\ :sup:`1`. Only one determinant: \| 1s :math:`\alpha` (1) \| 

**He**: Configuration (1s)\ :sup:`2` . Closed shell. 

**Li**: Configuration (2s)\ :sup:`1` . Only one determinant: \| 2s :math:`\alpha` (1) \| 

**Be**: Configuration (2s)\ :sup:`2` . Closed shell. 

**B**: Configuration (2p)\ :sup:`1` .
  Ground multiplet \ :sup:`2` P. 

  .. math::

    D_1 & = |p_1 \alpha (1) | = | ^2 P ; M_L =1 ; M_S = 1/2 \rangle \\
    \rho^\alpha & = 1/2(p_x-ip_y)(p_x+ip_y) = 1/2(p_x^2+p_y^2)

  The occupation numbers for D\ :sub:`1`  are 

  .. math::

    p_x^\alpha & = p_y^\alpha = 1/2 \\
    p_z^\alpha & = p_x^\beta = p_y^\beta = p_z^\beta = 0

  Another determinant belonging to \ :sup:`2` P is D\ :sub:`2`  = \|..p\ :sub:`0` :math:`\alpha` (1)\| 
  with occupations :math:`p_z^\alpha = 1` and all other p-occupations zero. This determinant is 0.04 eV lower in energy than D\ :sub:`1` for LDA, but 0.15 eV for BP. 

**C**: Configuration p\ :sup:`2` .
  Multiplet states are \ :sup:`3` P, \ :sup:`1` S and \ :sup:`1` D.  We use this atom as an example of the general procedure. First write down all determinants belonging to p\ :sup:`2`  and group them according to M\ :sub:`S`  and M\ :sub:`L`  (1\ :sup:`+`  :math:`\equiv` p\ :sub:`1` :math:`\alpha`, ...) 

  .. csv-table:: 

    **Determinant**, M\ :sub:`S`, M\ :sub:`L`
    D\ :sub:`1`  = \|1\ :sup:`+`  1\ :sup:`-` \|,0,2
    D\ :sub:`2`  = \|1\ :sup:`+`  0\ :sup:`+` \|,1,1
    D\ :sub:`3`  = \|1\ :sup:`+`  0\ :sup:`-` \|,0,1
    D\ :sub:`4`  = \|1\ :sup:`+`  -1\ :sup:`+` \|,1,0
    D\ :sub:`5`  = \|1\ :sup:`+`  -1\ :sup:`-` \|,0,0
    D\ :sub:`6`  = \|1\ :sup:`-`  0\ :sup:`+` \|,0,1
    D\ :sub:`7`  = \|1\ :sup:`-`  0\ :sup:`-` \|,-1,1
    D\ :sub:`8`  = \|1\ :sup:`-`  -1\ :sup:`+` \|,0,0
    D\ :sub:`9`  = \|1\ :sup:`-`  -1\ :sup:`-` \|,-1,0
    D\ :sub:`10`  = \|0\ :sup:`+`  0\ :sup:`-` \|,0,0
    D\ :sub:`11`  = \|0\ :sup:`+`  -1\ :sup:`+` \|,1,-1
    D\ :sub:`12`  = \|0\ :sup:`+`  -1\ :sup:`-` \|,0,-1
    D\ :sub:`13`  = \|0\ :sup:`-`  -1\ :sup:`+` \|,0,-1
    D\ :sub:`14`  = \|0\ :sup:`-`  -1\ :sup:`-` \|,-1,-1
    D\ :sub:`15`  = \|-1\ :sup:`+`  -1\ :sup:`-` \|,0,-2
   
  .. image:: Images/multiplet_image090.png
   :width: 10 cm

  The presence of a determinant with M\ :sub:`L`  = 2, M\ :sub:`S`  = 0 and no M\ :sub:`L`  = 2, M\ :sub:`S`   0 determinant indicates the presence of a \ :sup:`1` D multiplet, and E(\ :sup:`1` D) = E(D\ :sub:`1` ). There is also a \ :sup:`3` P, the determinant with M\ :sub:`S`  = 1, M\ :sub:`L`  = 1. We should have E(\ :sup:`3` P) = E(D\ :sub:`2` ) = E(D\ :sub:`4` ). The two determinants D\ :sub:`3`  and D\ :sub:`6`  in the M\ :sub:`S`  = 0, M\ :sub:`L`  = 1 box will mix, and the solutions of the 2 by 2 secular problem will be E(\ :sup:`1` D) and E(\ :sup:`3` P). Since the sum of the eigenvalues is equal to the sum of the initial diagonal elements, we have E(\ :sup:`1` D) + E(\ :sup:`3` P) = E(D\ :sub:`3` ) + E(D\ :sub:`6` ). We should also have E(D\ :sub:`3` ) + E(D\ :sub:`6` ) = E(D\ :sub:`1` ) + E(D\ :sub:`2` ). Such a relation provides a test on the consistency of the results.   Finally we have the M\ :sub:`S`  = 0, M\ :sub:`L`  = 0 block. The sum of the energies of D\ :sub:`5` , D\ :sub:`8`  and D\ :sub:`10`  should be the sum of the energies of \ :sup:`1` S, \ :sup:`3` P and \ :sup:`1` D. Since E(\ :sup:`3` P) and E(\ :sup:`1` D) are already known, E(\ :sup:`1` S) can be calculated.

  In the appendix we first locate for C the spherical unrestricted atom.
  Next we have E(D\ :sub:`4` ), yielding E(\ :sup:`3` P) = -1.345 eV (LDA + Becke). Next E(D\ :sub:`2` ) = E(\ :sup:`3` P) = -1.189 (always LDA + Becke).
  The difference is substantial: ~ 0.15  Next we have E(D\ :sub:`3` ) = - 0.812.
  Since E(D\ :sub:`6` ) = E(D\ :sub:`3` ), because :math:`\rho^\alpha` (D\ :sub:`6` ) = :math:`\rho^\beta` (D\ :sub:`3` ) and :math:`\rho^\beta` (D\ :sub:`6` ) = :math:`\rho^\alpha` (D\ :sub:`3` ), we should have 2E(D\ :sub:`3` ) = -1.624 = E(\ :sup:`1` D) + E(\ :sup:`3` P).
  Therefore E(\ :sup:`1` D) = -1.624 - (-1.345) = - 0.279 or E(\ :sup:`1` D) = - 1.624 - (-1.189) = - 0.435. These numbers can be checked against E(D\ :sub:`1` ) which also should be E(\ :sup:`1` D): E(D\ :sub:`1` ) =+ 0.044.
  The discrepancy is large! Finally, \ :sup:`1` S can be obtained: E(D\ :sub:`10` ) = + 0.319 (D\ :sub:`8` ) = E(D\ :sub:`1` ) = + 0.044 E(D\ :sub:`5` ) = E(D\ :sub:`1` ) = + 0.044.
  So 0.407 = E(\ :sup:`1` S) + E(\ :sup:`3` P) +E(\ :sup:`1` D).
  Different results for E(\ :sup:`1` S) are obtained depending on the E(\ :sup:`3` P) and E(\ :sup:`1` D) we choose: e.g. E(\ :sup:`1` S) = 0.407 -(-1.345) - (- 0.279) = 2.031 or E(\ :sup:`1` S) = 0.407 - (-1.189) - (0.044) = 1.552.
  Comparing to experiment we might calculate the excitation energies w.r.t. E(\ :sup:`3` P): 

 
  .. csv-table:: 

    ,**calculated**,**experimental**,**HF**
    :sup:`3` P → \ :sup:`1` D:, 1.066 to 1.389,  1.26, 1.55
    :sup:`3` P → \ :sup:`1` S:,   2.741 to 3.376,   2.684,   3.78

**N**: Configuration p\ :sup:`3` .
  Ground multiplet \ :sup:`4` S, corresponds to the spherical unrestricted atom, energy -2.943 eV.
  Other multiplets: \ :sup:`2` P, \ :sup:`2` D.
  According to the printed output for configuration p\ :sup:`3`  we have \|\ :sup:`2` D;M\ :sub:`L` =2;M\ :sub:`S` =1/2 = \|p\ :sub:`1` \ :math:`^\alpha`  p\ :sub:`1` \ :math:`^\beta`  p\ :sub:`0` \ :math:`^\alpha` \| = D\ :sub:`2`   :math:`\rho^\alpha`  =  1/2 p\ :sub:`x` \ :sup:`2`  +  1/2 p\ :sub:`y` \ :sup:`2`  +      p\ :sub:`z` \ :sup:`2`   :math:`\rho^\beta`  =  1/2 p\ :sub:`x` \ :sup:`2`  +  1/2 p\ :sub:`y` \ :sup:`2`  E(D\ :sub:`2` ) = - 0.745 according to the table in the Appendix (LDA + Becke).
  The energy of D\ :sub:`1` , with :math:`\rho^\alpha`  =  p\ :sub:`x` \ :sup:`2`  +  p\ :sub:`y` \ :sup:`2` , :math:`\rho^\beta`  = p\ :sub:`z` \ :sup:`2` , is E(\|1A 2B 3A\|) = -1.9702.
  The energy of D\ :sub:`3` , with :math:`\rho^\alpha`  =  1/2 p\ :sub:`x` \ :sup:`2`  +  1/2 p\ :sub:`y` \ :sup:`2`  +      p\ :sub:`z` \ :sup:`2` , :math:`\rho^\beta`  = p\ :sub:`z` \ :sup:`2`  corresponding to \|1A 2A 2B\| or \|2A 2B 3A\|, is E(D\ :sub:`3` ) = - 0.158.
  Finally, D\ :sub:`4`  has :math:`\rho^\alpha`  =  p\ :sub:`x` \ :sup:`2`  +  p\ :sub:`y` \ :sup:`2` , :math:`\rho^\beta`  =  1/2 p\ :sub:`x` \ :sup:`2`  +  1/2 p\ :sub:`y` \ :sup:`2` , corresponding to \|1A 1B 3A\| and \|1A 3A 3B\|, and E(D\ :sub:`4` ) = - 0.109.
  The M\ :sub:`L` = 1, M\ :sub:`S` =1/2 determinants are \|1A 1B 3A\| and \|1A 2A 2B\|.
  Therefore E(\ :sup:`2` D) + E(\ :sup:`2` P) = E(D\ :sub:`4` ) + E(D\ :sub:`3` ), so E(\ :sup:`2` P) = - 0.109 - 0.158 - (- 0.745) = + 0.478.
  We can use D\ :sub:`1`  in the M\ :sub:`L` =0, M\ :sub:`S` =1/2 block, from which we find E(\ :sup:`4` S) + E(\ :sup:`2` D) + E(\ :sup:`2` P) = 2E(D\ :sub:`2` ) =+ E(D\ :sub:`1` ).
  Hence E(\ :sup:`2` P) = -1.490 - 1.9702 - (- 0.745) - (- 2.943) = + 0.2278. 

**O**: Configuration p\ :sup:`4` .
  Multiplet states \ :sup:`3` P, \ :sup:`1` S, \ :sup:`1` D. D\ :sub:`1` , with :math:`\rho^\alpha`  =  p\ :sub:`x` \ :sup:`2`  +  p\ :sub:`y` \ :sup:`2`  +  p\ :sub:`z` \ :sup:`2` , :math:`\rho^\beta`  =  p\ :sub:`z` \ :sup:`2`  corresponds to \|1A 2A 2B 3A\| , the M\ :sub:`L` =1, M\ :sub:`S` =1 determinant of \ :sup:`3` P: E(\ :sup:`3` P) = -1.836 D\ :sub:`2`  with :math:`\rho^\alpha`  =  p\ :sub:`x` \ :sup:`2`  +  p\ :sub:`y` \ :sup:`2`  +  p\ :sub:`z` \ :sup:`2` , :math:`\rho^\beta`  =  1/2 p\ :sub:`x` \ :sup:`2`  +  1/2 p\ :sub:`y` \ :sup:`2` , corresponds to \|1A 1B 2A 3A\|, the determinant of \ :sup:`3` P: E(\ :sup:`3` P) = -1.568 D\ :sub:`3` , with :math:`\rho^\alpha`  =  1/2 p\ :sub:`x` \ :sup:`2`  +  1/2 p\ :sub:`y` \ :sup:`2`  +  p\ :sub:`z` \ :sup:`2` , :math:`\rho^\beta`  =  p\ :sub:`x` \ :sup:`2`  +  p\ :sub:`y` \ :sup:`2` , corresponds to \|1A 1B 2A 3B\|, and M\ :sub:`L` =1, M\ :sub:`S` =0 belonging to \ :sup:`3` P as well as \ :sup:`1` D. 

**F**: Configuration p\ :sup:`5` . 
  Ground multiplet \ :sup:`2` P. As in B, we have two determinants with different energies belonging to this state: D\ :sub:`1`  = \|...(p\ :sub:`0` \ :math:`^\alpha` )\ :sup:`1`  (p\ :sub:`0` \ :math:`^\beta` )\ :sup:`0` \| → E(D\ :sub:`1` ) = - 0.715. D\ :sub:`2`  = \|(p\ :sub:`-1` )\ :sup:`2`  (p\ :sub:`0` )\ :sup:`2`  (p\ :sub:`1` \ :math:`^\alpha` )\ :sup:`1`  (p\ :sub:`1` \ :math:`^\beta` )\ :sup:`0` \| → E(D\ :sub:`2` ) = - 0.467. 

**Ne**: Configuration p\ :sup:`6` . Closed shell. 

**Ground and Excited State Multiplets**

The computation of multiplets can be carried out with adf, using the input block ``SLATERDETERMINANTS``. 

The method described in [#ref1]_ for the calculation of the energies of proper spin and spatial symmetry adapted Configuration State Functions is based on the calculation of the energies of single determinantal wavefunctions. The densities corresponding to those Slater determinants are inserted in the approximation used for the exchange-correlation energy.  

The procedure as detailed above is somewhat involved. Moreover, one would like to have an easy procedure to calculate many determinants. This is particularly desirable if one wishes to calculate the energies of all Slater determinants of a given configuration, for instance if one wishes to calculate certain averages in view of the inconsistencies of the method.  

We have implemented a semi-automatic procedure, using the block ``SLATERDETERMINANTS``. 

The general idea of this method is to first perform a restricted calculation in the symmetry that is appropriate for the molecule. This is called the average-of-configuration (AOC) calculation. This AOC calculation generates the orbitals which will be used in all the Slater determinants. 

The AOC is the fragment that *must* be used in all subsequent calculations. The subsequent calculations are characterized by having the AOC as the (only) fragment, and by specifying the keyword ``SLATERDETERMINANTS``. If an argument is given this must be a file name. The named file should contain the occupations for the determinants (see below). If no file name is specified, the occupations should be specified in the data block. 

The required information, on file or in the data block, is the specification of the determinant or determinants that are to be calculated in the form of orbital occupation numbers for the AOC orbitals, using the irrep labels of the point group of the AOC calculation, see below for format. All specified determinants will be calculated, and the obtained energy will always be the energy difference with respect to the AOC. Default occupations for all subspecies of the AOC fragment are the occupations of the AOC itself. Therefore, only the open (modified) subspecies have to be specified.  

One has to be careful with respect to the point group symmetry to use in the ``SLATERDETERMINANTS`` calculation. The density belonging to a specific determinant is usually lower than the AOC symmetry (which is the full symmetry group of the system). In that case this lower point group symmetry has to be specified in the ``SLATERDETERMINANTS`` calculation. Everything will always work fine if one just does not use any symmetry at all (nosym). However, if for reasons of computational efficiency one does want to use a subgroup of the system that corresponds to the determinant density or densities, this is perfectly possible. However, all the densities of the determinants specified *must* then have this (or a higher) symmetry. The program does not check on this, it is the user's responsibility to make sure that this condition is satisfied for all the determinants. The only check that is performed is that occupations of equivalent representations (subspecies of one irrep) in the lower point group of the ``SLATERDETERMINANTS`` run, that result from the specified occupations of the subspecies of the AOC symmetry, are equal. 

**Format of the input.** 

**Important**: in the SlaterDeterminants calculations it is imperative that the results are obtained in the AOC field: no SCF convergence must be carried out, because we only want to assign the electrons differently, while keeping the AOC orbitals exactly as they are. To achieve this, the calculations should use the keyword SCF, and the subkey iterations has to be set to 0 in the SCF data block. 

Since adf requires that the point-group symmetry conforms not only to the nuclear frame but also to the electronic charge density and mo occupations, these calculations must run in a lower point group symmetry. Often you will also want to run the modified calculations spin-unrestricted. 

For an example, see the set of sample runs that come with the package and the comments in the examples. 


See: :ref:`SLATERDETERMINANTS block <keyscheme SLATERDETERMINANTS>`. Each 'title' functions as a subkey, but is otherwise an arbitrary string to label the resulting one-determinant calculation. Each such subkey block contains the occupation numbers for a single one-determinant calculation. It is necessary that the calculation uses the reference AOC run as its only fragment file. The occupations in the subkey blocks must be re-arrangements of the AOC open-shell electrons. In the ``SLATERDETERMINANTS`` calculation you must explicitly specify the point group symmetry in which you want to run. The :math:`\rho^\alpha`  and :math:`\rho^\beta` densities of all determinants to be calculated must have this point group symmetry, or a higher symmetry. 

Each 'irrep occups' record specifies the occupations for the indicated irrep in the usual way (see for instance the occupations key). The irrep labels must correspond to the AOC point group symmetry used in the AOC calculation, *not the point group symmetry used in the ``SLATERDETERMINANTS`` calculation!*. Note that in an unrestricted calculations, occupations numbers must be given for both spins, using the double slash (//) to separate the occupations for spin-alpha and spin-beta. 

In this setup, the program will for each of the subkey blocks under the ``SLATERDETERMINANTS`` key execute an SCF calculation with only one cycle, i.e. no convergence, where the start-up field is the fragment field, i.e. the AOC field. So all one-determinant states in this calculation are evaluated in the AOC field. The resulting energies for the distinctly computed one-determinant states can then be combined to the desired multiplet values. 

**Example: Carbon** :math:`p^2`  

::

  SlaterDeterminants
  C(p2) ALFA: s=1, px=py=2/3, pz=2/3; BETA: s=1, p=0 ! title
     S 1 // 1 ! irrep name and occupations
     P:x 0.666666666666666666 // 0 ! another irrep, et cetera
     P:y 0.666666666666666666 // 0
     P:z 0.666666666666666666 // 0
     D:z2 0 // 0
     D:x2-y2 0 // 0
     D:xy 0 // 0
     D:xz 0 // 0
     D:yz 0 // 0
  SUBEND
  C(p2) ALFA: S=1, px=py=1, pz=0; BETA: s=1 !next (Sl.Determinant) title
     S 1 // 1
     P:x 1 // 0
     P:y 1 // 0
     P:z 0 // 0
     D:z2 0 // 0
     D:x2-y2 0 // 0
     D:xy 0 // 0
     D:xz 0 // 0
     D:yz 0 // 0
  SUBEND
  C(p2) ALFA: s=1, px=py=0.5, pz=1; BETA: s=1
     S 1 // 1
     P:x 0.5 // 0
     P:y 0.5 // 0
     P:z 1 // 0
     D:z2 0 // 0
     D:x2-y2 0 // 0
     D:xy 0 // 0
     D:xz 0 // 0
     D:yz 0 // 0
  SUBEND
  C(p2) ALFA: s=1, px=py=0.5, pz=0; BETA: s=1, px=py=0, pz=1
     S 1 // 1
     P:x 0.5 // 0
     P:y 0.5 // 0
     P:z 0 // 1
     D:z2 0 // 0
     D:x2-y2 0 // 0
     D:xy 0 // 0
     D:xz 0 // 0
     D:yz 0 // 0
  SUBEND
  C(p2) ALFA: s=1, px=py=0.5, pz=0; BETA: s=1, px=py=0.5, pz=0
     S 1 // 1
     P:x 0.5 // 0.5
     P:y 0.5 // 0.5
     P:z 0 // 0
     D:z2 0 // 0
     D:x2-y2 0 // 0
     D:xy 0 // 0
     D:xz 0 // 0
     D:yz 0 // 0
  SUBEND
  C(p2) ALFA: s= 1, px=py=0, pz=1; BETA: s=1, px=py=0, pz=1
     S 1 // 1
     P:x 0 // 0
     P:y 0 // 0
     P:z 1 // 1
     D:z2 0 // 0
     D:x2-y2 0 // 0
     D:xy 0 // 0
     D:xz 0 // 0
     D:yz 0 // 0
  SUBEND

In the example the AOC calculation is the Carbon atom in spherical symmetry (symmetry name atom). 

Several spin states can be generated from this AOC set of orbitals, but they all have a lower symmetry than the AOC. In the example the point group D\ :sub:`∞h`  (DLIN) could be used in the ``SLATERDETERMINANTS`` calculation. In D\ :sub:`∞h`  the *p* orbitals split into two sets, *p**\ :sub:`x` * and *p**\ :sub:`y` * occur in :math:`\pi`\ :sub:`x`  and :math:`\pi`\ :sub:`y`  respectively, so their occupations must be identical, and *p**\ :sub:`z` * is a :math:`\Sigma`\ :sub:`u`  orbital. 

In the block ``SLATERDETERMINANTS`` (or in the file) we now specify the occupations for the subspecies of the atom irreps of a specific Slater determinant and the program will sort out the corresponding occupations in the d(lin) symmetry. 

In all cases the orbitals used for the energy calculation(s) will be the self-consistent AOC orbitals. 

In the given example, the first set of occupations does not correspond to a Slater determinant, but is the spin-polarized spherical case with the *p* electrons evenly distributed over all components. 

**LDA results, with and without GGA (Becke-Perdew)**

Energy changes (eV) for atoms going from restricted to (one-cycle) unrestricted. Results between parentheses are for *converged* unrestricted calculations) 

All calculations have been performed in D\ :sub:`∞h`  symmetry, since p\ :sub:`x`  and p\ :sub:`y`  always had equal occupations and therefore could occur as :math:`\pi`\ :sub:`u` -x and :math:`\pi`\ :sub:`u` -y partners of the :math:`\Pi`\ :sub:`u`  irrep. 




+-----+-----------------------------------+-----------------+-----------------+-----------------+
| El. | Occupations                       | LDA             | LDA+Becke       | BP              |
+-----+-----------------+-----------------+-----------------+-----------------+-----------------+
|     | alpha-spin      | beta-spin       |                                                     |
+-----+---+-------+-----+---+-------+-----+-----------------------------------------------------+
|     | s | px+py | pz  | s | px+py | pz  |                                                     |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| H   | 1 | 0     | 0   | 0 | 0     | 0   | -0.868 (-0.898) | -0.758 (-0.837) | -0.889 (-0.948) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| Li  | 1 | 0     | 0   | 0 | 0     | 0   | -0.231 (-0.235) | -0.195 (-0.207) | -0.249 (-0.256) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| Be  | 1 | 0     | 0   | 1 | 0     | 0   | 0.000  (0.000)  | 0.000 (0.000)   | 0.000 (0.000)   |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| B   | 1 | 2/3   | 1/3 | 1 | 0     | 0   | -0.247 (-0.255) | -0.231 (-0.242) | -0.276 (-0.281) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 0     | 1   | 1 | 0     | 0   | -0.295 (-0.321) | -0.436 (-0.474) | -0.448 (-0.485) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 0   | 1 | 0     | 0   | -0.266 (-0.279) | -0.296 (-0.316) | -0.333 (-0.348) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| C   | 1 | 4/3   | 2/3 | 1 | 0     | 0   | -1.163 (-1.203) | -1.109 (-1.158) | -1.252 (-1.285) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 0   | 1 | 0     | 0   | -1.152 (-1.211) | -1.271 (-1.345) | -1.372 (-1.436) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 1   | 1 | 0     | 0   | -1.152 (-1.197) | -1.134 (-1.189) | -1.267 (-1.307) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 0   | 1 | 0     | 1   | -0.462 (-0.506) | -0.726 (-0.812) | -0.778 (-0.868) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 0   | 1 | 1     | 0   | 0.159  (0.150)  |  0.039 (0.044)  |  0.087 (0.086)  |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 0     | 1   | 1 | 0     | 1   | 0.730  (0.668)  |  0.322 (0.319)  |  0.480 (0.450)  |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| N   | 1 | 2     | 1   | 1 | 0     | 0   | -2.936 (-3.032) | -2.827 (-2.943) | -3.101 (-3.190) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 0   | 1 | 0     | 1   | -1.362 (-1.454) | -1.811 (-1.972) | -1.943 (-2.108) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 1   | 1 | 1     | 0   | -0.581 (-0.618) | -0.688 (-0.745) | -0.746 (-0.801) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 1   | 1 | 0     | 1   | 0.178  (0.088)  |-0.104 (-0.158)  | -0.069 (-0.140) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 0   | 1 | 1     | 0   | 0.197  (0.135)  |-0.077 (-0.109)  | -0.011 (-0.053) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| O   | 1 | 2     | 1   | 1 | 2/3   | 1/3 | -1.400 (-1.477) | -1.361 (-1.447) | -1.480 (-1.552) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 1   | 1 | 0     | 1   | -1.442 (-1.583) | -1.698 (-1.836) | -1.816 (-1.957) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 1   | 1 | 1     | 0   | -1.422 (-1.515) | -1.470 (-1.568) | -1.590 (-1.678) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 1   | 1 | 2     | 0   | -0.564 (-0.623) | -0.866 (-0.960) | -0.913 (-1.013) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 1     | 1   | 1 | 1     | 1   | 0.358  (0.321)  | 0.255 (0.237)   |  0.292 (0.266)  |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 0   | 1 | 2     | 0   | 1.323  (1.220)  | 0.825 (0.789)   |  0.992 (0.932)  |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
| F   | 1 | 2     | 1   | 1 | 4/3   | 2/3 | -0.374 (-0.398) | -0.366 (-0.391) | -0.394 (-0.416) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 1   | 1 | 2     | 0   | -0.323 (-0.409) | -0.605 (-0.686) | -0.627 (-0.715) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+
|     | 1 | 2     | 1   | 1 | 1     | 1   | -0.349 (-0.389) | -0.401 (-0.441) | -0.427 (-0.467) |
+-----+---+-------+-----+---+-------+-----+-----------------+-----------------+-----------------+


.. only:: html

  .. rubric:: References

.. [#ref1] T.\  Ziegler, A. Rauk and E.J. Baerends, *On the calculation of Multiplet Energies by the Hartree Fock Slater method*, `Theoretica Chimica Acta 43, 261 (1977) <https://doi.org/10.1007/BF00551551>`__ 

.. [#ref3] C.\  Daul, *DFT applied to excited states*, `International Journal of Quantum Chemistry 52, 867 (1994) <https://doi.org/10.1002/qua.560520414>`__ 

.. [#ref6] E.J. Baerends, V. Branchadell and M. Sodupe, *Atomic reference-energies for density functional calculations*, `Chemical Physics Letters 265, 481 (1997) <https://doi.org/10.1016/S0009-2614(96)01449-2>`__ 
