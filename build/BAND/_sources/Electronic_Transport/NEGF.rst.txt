.. index:: NEGF
.. index:: Electronic Transport

.. _NEGF: 

Electronic Transport (NEGF)
===========================

.. seealso:: 

  `BAND-NEGF GUI tutorial <../../Tutorials/ElectronicTransport/index.html>`__


Some examples are available in the ``$AMSHOME/examples/band`` directory and are discussed in the Examples section.

.. csv-table:: 

  :ref:`example NEGF_Cr_wire`
  :ref:`example NEGF_bias`



.. note:: 

  In the BAND-GUI it is possible to choose between three NEGF methods (*flavors*):

  Self consistent
    This is the internal BAND-NEGF implementation, which is described in this page. 

  Self consistent + align
    This is the internal BAND-NEGF implementation with an extra alignment-run (workflow step 3a)

  Non self consistent
    Computationally cheap method, equivalent to the `DFTB-NEGF <../../DFTB/NEGF.html>`__ approach with :math:`H` and :math:`S` matrix elements computed by BAND (instead of DFTB). 


Transport with NEGF in a nutshell
---------------------------------

The **Non-Equilibrium Green's Functions** formalism (**NEGF**) is a theoretical framework for modeling electron transport through nano-scale devices. 
Electron transport is treated as a one-dimensional coherent scattering process in the "scattering region" for electrons coming in from the electrodes:

.. image:: /Images/NEGF_regions.png

Our goal is to compute the **transmission function** :math:`T(E)`, which describes the rate at which electrons of energy :math:`E` are transferred from the left electrode to the right electrode by propagating through the scattering region.
From the transmission function we can calculate the electric current for given **Bias Voltage** :math:`V` applied between the electrodes:

.. math:: 
   
   I(V) = \frac{2e}{h} \int_{-\infty}^\infty T(E,V) \left( f(E - \mu_L) - f(E - \mu_R) \right) dE


where :math:`f(E)` is the Fermi-Dirac distribution function for a given temperature, and :math:`\mu_L` (:math:`\mu_R`) is :math:`\epsilon_F + eV/2` (:math:`\epsilon_F - eV/2`), :math:`\epsilon_F` being the Fermi energy of the electrodes. 

The transmission function :math:`T(E)` can be computed from the **Green's function** of our system.

The Green's function :math:`G(E)` of the scattering region is obtained solving the following equation:

.. math::

   (E S - H) G(E) = I

where :math:`S` is the overlap matrix, :math:`H` is the Hamiltonian and :math:`I` is the identity matrix.
The Hamiltonian is composed as follows (**L**, **C** and **R** denote the **left lead**, the **central region** and the **right lead** respectively): 

.. math::

   H = \left( \begin{array}{ccc}
   H_L + \Sigma_L  & H_{LC}  & 0 \\
   H_{LC}          & H_C     & H_{RC} \\
   0               & H_{RC}  & H_R + \Sigma_R
   \end{array} \right)

The two *self-energies* :math:`\Sigma_L` and :math:`\Sigma_R` model the two semi-infinite electrodes.

The transmission function :math:`T(E)` can be calculated from the Green's function :math:`G(E)` and the so-called *broadening matrices* :math:`\Gamma_L(E)` and :math:`\Gamma_R(E)`:

.. math::
   
   T(E) = Tr[G(E) \Gamma_R(E) G(E) \Gamma_L(E)]

The broadening matrix being

.. math::
   \Gamma_L(E) = -2 \Im \Sigma_L(E)



Self consistency
^^^^^^^^^^^^^^^^

The density matrix is determined self consistently [#ref1]_:

.. math::

   P_\text{in} \rightarrow H_{KS} \stackrel{\mbox{shifts}}{\longrightarrow} H_\text{aligned} + \Sigma_L(E)  + \Sigma_R(E) \rightarrow G(E) \stackrel{\int de}{\longrightarrow} P_\text{out}

From a guess of the density matrix the corresponding KS Hamiltonian is calculated. This Hamiltonian is aligned, and then the NEGF Hamiltonian in the complex plane is constructed by adding the self energies, representing the influence of the electrodes. From the resulting Green's function a new density matrix follows.

From the difference between input and output density a next input is guessed. This is repeated until the input and output densities converge.

For the alignment of the Hamiltonian there are two shifts. The first shift aligns the potential in the leads to the electrodes.

.. math::

  \mbox{shift 1} = \frac{1}{n} \sum_\text{i in lead}^n \frac{H^{TB}_{ii} - H^{KS}_{ii}}{S_{ii}}

The second and usually smaller shift results from the alignment run. A shift :math:`\Delta` is applied globally

.. math::

  H_{ij}^\text{aligned} = H_{ij} + \Delta S_{ij}

Contour integral
^^^^^^^^^^^^^^^^

Without bias the density matrix follows from

.. math::

   P(\mu) = -\frac{1}{\pi} \int_{-\infty}^{\infty} de \; f(e,\mu) \; \Im G(e)


As the Green's function is singular on the real axis we add a small imaginary value (**eta**) to the energy. Still, the integrand will be very wild function, and it is numerically better to do a contour integral instead.


.. figure:: /Images/NEGF_DensityContour.png

  Figure: BAND uses a rectangular contour in the complex energy plane to integrate the (integrand of the) density matrix. The integrand also needs to be evaluated in the enclosed FD poles (three in this picture).

Gate potential
^^^^^^^^^^^^^^

There is no direct key for the gate potential. You can model this with the :ref:`FuzzyPotential <band-key-FuzzyPotential>` key. Setting up the gate potential for NEGF is most conveniently done with the GUI.


Bias potential
^^^^^^^^^^^^^^

.. figure:: /Images/NEGF_Bias.png

When there is a bias specified there are two important things to keep in mind. 

First of all you need to define a ramp potential. In the negative lead this should have the value +V/2 and in the negative lead -V/2. The ramp should smoothly go from one to the other value. For metals one could start the ramp at the surface atoms of the lead material. For semi-conductors it is less clear. The ramp potential can be specified with the :ref:`FuzzyPotential <band-key-FuzzyPotential>` key. The GUI can be helpful here.

Secondly, the expression for the density is different from the zero-bias case:

.. math::
  \rho = \rho_\text{eq}(\mu_+) + \rho_\text{neq}


The first (equilibrium) term is calculated with a contour integral as before, the second (non-equilibrium) part cannot be calculated with a contour integral. Instead, an integral in the complex plane (close to the real axis) is performed, the range covering the bias energy window.

.. seealso::

  `PhD Thesis <https://www.scm.com/wp-content/uploads/Verzijl2012.pdf>`__ of C. Verzijl (BAND-NEGF developer)


Workflow
--------

The computation of the transmission function :math:`T(E)` within the BAND-NEGF [#ref1]_ formalisms requires three or four individual simulations.

.. tip:: 

   Use ADFInput (GUI) to set up your BAND-NEGF calculation (see the `BAND-NEGF GUI tutorial <../../Tutorials/ElectronicTransport/index.html>`__)


1): Lead calculation
  A 1D-periodic BAND calculation of the lead (including :ref:`StoreHamiltonian2 <band-key-StoreHamiltonian2>`):

  .. image:: /Images/NEGF_lead_calc.png
   
  A tight binding (TB) representation is calculated for the overlap (:math:`S(R=0)` and :math:`S(R=a)`) and Fock matrix (:math:`H(R=0)` and :math:`H(R=a)`).  This is not an approximation provided that the functions do not extend beyond the neighboring cells. You should choose a sufficiently large super cell for this to be true. For this reason we recommend setting the :ref:`SoftConfinement <band-key-SoftConfinement>` Quality to Basic, thus reducing the range of the functions.

2): SGF calculation
  A small program that determines the fermi energy :math:`\epsilon_F` corresponding to the TB representation, and the specified temperature. This fermi energy is typically a bit higher than the one from the lead calculation. This also tests the contour integration.

3a): Alignment run (optional)
  The idea is to fill the central region with bulk material. Then one expects to have zero charge in the central region. In practice this is not exactly true. In the alignment run the shift is determined that makes the central region neutral. This global shift is to be used in the next run.

3b): Transport calculation
  Computes the NEGF transmission function :math:`T(E)`. The density matrix is determined fully self-consistently. Without alignment (3a) one should set ``NEGF%ApplyShift2`` to ``False``.
   
To get the current as a function of bias potential you need to repeat calculation 3b for a various bias potentials.   

Input options
-------------


SGF Input options
^^^^^^^^^^^^^^^^^

SGF is a small separate program. An input looks like::

   $AMSBIN/sgf   << eor
   TITLE Test for NEGF inputs
   SAVE SIGMA
   SURFACEGF
      SCMCode True
      KT 0.001
      ContourQuality normal
   END
   eor

It looks for a file ``RUNKF`` and the output is a file named ``SigmaSCM``. The only important parameter is KT which is the Boltzmann constant times the temperature in Hartree. The other parameter of interest is the ContourQuality, which can be set to Basic,Normal,Good,VeryGood, or Excellent.


NEGF Input options (no bias)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The NEGF functionality is controlled by the NEGF block key.

.. scmautodoc:: band NEGF LeadFile SGFFile ContourQuality EMin EMax NE

The following are expert / technical options:

.. scmautodoc:: band NEGF CheckOverlapTol Eta ApplyShift1 ApplyShift2 YContourInt DEContourInt
  :noref:

NEGF Input options (with bias)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With a bias potential there are some extra keys.


.. scmautodoc:: band NEGF BiasPotential NonEqDensityMethod BoundOccupationMethod YRealaxisInt DERealAxisInt
  :noref:


``NonEqDensityMethod``
  Let us introduce some terms [#ref2]_. First of all the total density in the bias window (ignoring occupation)
  
  .. math::
  
    D = \frac{1}{2\pi}  \int A \; (f_--f_+) 

  And then there are the side resolved densities
  
  .. math::
  
    D_{+/-} = \frac{1}{2\pi}  \int A_{+/-} \; (f_--f_+) 

  The issue here is that the side resolved densities do not sum to the total one  

  .. math::
  
    D = D_{+} + D_{-} + D_\text{bound states}
  
  The NonEqDensityMethod is about how these integrals are calculated . With option 1, or 2 a contour integral is used for D: they are essentially the same. However, when choosing option 2, you can choose a BoundOccupationMethod, leading to other physics. If set to 3, the total density in the bias window (D) will be calculated near the real axis: this way one avoids the possibility of a negative nr. of bound states (deviating from [#ref2]_).

``BoundOccupationMethod``
  Only relevant with NonEqDensityMethod equal 2 or 3. If set to one, the density of bound states (ignoring occupation) is simply multiplied by a half. If set to two, atoms closer to the negative lead will get a higher occupation [#ref2]_. Atoms coupled to the right lead will have a low occupation. For this we recommend setting NonEqDensityMethod to 3, to avoid a possible negative number of bound states.


  .. figure:: /Images/NEGF_BoundStates.png
  
     Figure: The non-equilibrium density consists of three parts: the left and right parts (ρ-/neq and ρ+/neq) and the bound states (ρbound). We want to know the occupied part.

  Setting the method BoundOccupationMethod to 1, leads to

  .. math:: 
   
    \rho = \rho(\mu_+) +  \rho_\text{-/neq}  + \frac{1}{2}\rho_\text{bound} 

  By setting the method to 2, each atom gets its own weight in the density matrix

  .. math:: 
   
    \rho_{ij} = \rho_{ij}(\mu_+) +  \rho_\text{-/neq}  + \sqrt{w_i w_j} \rho^\text{bound}_{ij}

  with [#ref2]_
  
  .. math::
  
    w_i = \frac{\text{Tr} [D_-]_i}{\text{Tr} [D_-]_i + \text{Tr} [D_+]_i}

  These weights are the same for all functions on an atom. The intended effect is: bound states that are coupled more strongly to the negative electrode get a higher occupation than the ones that are coupled more strongly to the positive electrode.
  
  To summarize here are three reasonable settings
  
  .. csv-table:: 

   NonEqDensityMethod,BoundOccupationMethod,intention
   1,1,Multiply the bound states with a half
   2,2,Occupy bound states with atom-resolved :math:`w_i`
   3,2,... and prevent a negative nr. of bound states





To get the current from a calculation you can use amsprep::

      $AMSBIN/amsreport RUNKF 'NEGF%current'

NEGF Input options (alignment)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the (optional) alignment run there are some extra keys.

.. scmautodoc:: band NEGF DoAlignment Alpha AlignChargeTol CDIIS
  :noref:


Troubleshooting
---------------

The self consistent approach, unique to BAND, may be difficult to converge.  If this is true for the alignment run it can be decided to skip this run. For the final transport run, here are some tips / considerations.

+ Use a SZ basis for the metal atoms

+ Restart (the density matrix) from the result of a smaller (such as the SZ) basis. (See ":ref:`Save <band-key-Save>` DensityMatrix" and the :ref:`Restart <band-key-Restart>` key)

+ Restart (the density matrix) from the result obtained with a smaller bias (only relevant for calculations with bias potential).

+ Setting NEGF%BoundOccupationMethod to 2 (and NEGF%NonEqDensityMethod to 3) might help. Note that this affects the physics: you are differently occupying the bound states.

+ Use a better NEGF%ContourQuality (there comes a computational price tag with this). 

If everything fails it is possible to use BAND in a **non-self consistent way**, similar to the way DFTB-NEGF works. This option is available via the GUI.

Miscellaneous remarks on BAND-NEGF
----------------------------------

* You should make sure that your results are converged with respect to the number of lead repetitions; the results should not change significantly if you increase the number of lead repetitions.
* It's good practice to include at least one lead repetition in the central region.


Store tight-binding Hamiltonian
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: Tight binding

Let us consider a Fourier transformation of a 1D Bloch matrix

.. math::

  S(R=na) = \int_k e^{-ikR} S(k)

In (the tight-binding) case that the functions do not extend beyond the neighboring cells only S(R=0) and S(R=a) are nonzero. (And S(R=-a) is equivalent to S(R=a))

.. scmautodoc:: band StoreHamiltonian2

Adding StoreHamiltonian2 to the input cause band to determine the tight-binding representation of the overlap an fock matrix. Currently this only works for 1D periodic systems. For the overlap matrix you will get two parts. The first :math:`S(R=0)` is the (symmetric) overlap matrix of atoms in the unit cell. The second :math:`S(R=a)` is a non symmetric matrix describing the coupling of functions in the central cell with functions in its right neighboring cell. On the RUNKF file you will find the TB representations of the overlap and Hamiltonian stored in the 'Matrices' section as "S(R)" and "H(R)", being dimensioned (nBas,nBas,2).


.. only:: html

  .. rubric:: References

.. [#ref1] C.\  J. O. Verzijl and J. M. Thijssen *DFT-Based Molecular Transport Implementation in ADF/BAND*, `J. Phys. Chem. C, 2012, 116 (46), pp 24393–24412 <https://doi.org/10.1021/jp3044225>`__.

.. [#ref2] Rui Li, Jiaxing Zhang, Shimin Hou,  Zekan Qian, Ziyong Shen, Xingyu Zhao, Zengquan Xue, *A corrected NEGF + DFT approach for calculating electronic transport through molecular devices: Filling bound states and patching the non-equilibrium integration*, `Chemical Physics 336 (2007) 127-135 <https://doi.org/10.1016/j.chemphys.2007.06.011>`__.
