.. index:: Franck-Condon factors 
.. index:: Fluorescence 
.. index:: Phosphorescence 
.. index:: FCF
.. index:: Adiabatic Hessian Franck-Condon
.. _AH-FC:

AH-FC: Adiabatic Hessian Franck-Condon
======================================

Electronic spectra, such as absorption, emission, phosphorescence, and ionization, may contain a vibrational structure.

In the Adiabatic Hessian Franck-Condon (AH-FC) method one needs to do a frequency calculation both at the ground state as well as the excited state of interest.
The model makes the following assumptions:

* 1. It employs the adiabatic (Born-Oppenheimer) approximation and treats the nuclei as moving in an effective potential defined by the electronic configuration.
* 2. It works at the Franck-Condon (FC) point and assumes that the transition occurs at the ground state equilibrium structure for absorption and at the excited state equilibrium structure for emission.
* 3. It applies the harmonic approximation to both the ground and excited state potential energy surfaces.

Franck-Condon factors can be calculated for the transition between the two electronic states, which can be done with the :ref:`FCF Module<FCF>`, described below.
These Franck-Condon factor can then be used to predict the relative intensities of absorption or emission lines in the electronic spectra. Note that the Herzberg-Teller effect is not taken into account.

In the vertical gradient Franck-Condon (VG-FC) method some extra assumptions are made compared to the AH-FC method.
This approach is particularly effective for large molecules as it shows linear scaling with the number of normal modes.

* See the documentation of the :ref:`VG-FC method <VG-FC>`.

.. index:: FCF module 
.. _FCF: 

FCF module: Franck-Condon Factors
---------------------------------

*fcf* is an auxiliary program which can be used to calculate Franck-Condon factors from two vibrational mode calculations [#ref1]_. The program assumes that the starting vibrational wavefunction is in the ground state, as is the case for most spectroscopic experiments performed at room temperature.

*fcf* requires an ASCII input file where the user specifies the .rkf files from two vibrational mode calculations, carried out for two different electronic, spin or charge states of the same molecule.
These calculations can be either numerical or analytical.

*fcf* produces a (binary) KF file TAPE61, which can be inspected using the KF utilities. Furthermore, *fcf* writes the frequencies, vibrational displacements and electron-phonon couplings for both states too the standard output, including any error messages. 

In AMS2022 the algorithm for the calculation of the Franck-Condon factors has been changed in order to improve the precision, increase the speed, and lower the memory requirements.

Theory
^^^^^^

Franck-Condon factors are the squares of the overlap integrals of vibrational wave functions. Given a transition between two electronic, spin or charge states, the Franck-Condon factors represent the probabilities for accompanying vibrational transitions. As such, they can be used to predict the relative intensities of absorption or emission lines in spectroscopy or excitation lines in transport measurements. 

When a molecule makes a transition to another state, the equilibrium position of the nuclei changes, and this will give rise to vibrations. To determine which vibrational modes will be active, we first have to express the displacement of the nuclei in the normal modes: 

.. math::

   \mathbf{k} =  \mathbf{L'}^T \mathbf{m}^{1/2} (\mathbf{B}_0 \mathbf{x}_0 - \mathbf{x'}_0)

Here, :math:`\mathbf{k}` is the displacement vector, :math:`\mathbf{L}` is the normal mode matrix, :math:`\mathbf{m}` is a matrix with the mass of the nuclei on the diagonal, :math:`\mathbf{B}` is the zero-order axis-switching matrix and :math:`\mathbf{x}_0`  is the equilibrium position of the nuclei. For free molecules, depending on symmetry constraints, the geometries of both states may have been translated and/or rotated with respect to each other. To remove the six translational and rotational degrees of freedom, we can center the equilibrium positions around the center of mass and rotate one of the states to provide maximum overlap. The latter is included with the zero-order axis-switching matrix :math:`\mathbf{B}`, implemented according to [#ref2]_. 

When we have obtained the displacement vector, it is trivial to calculate the dimensionless electron-phonon couplings. They are given by: 

.. math::

   \mathbf{\lambda} = (\mathbf{\Gamma}/2)^{1/2} \mathbf{k}

Here, :math:`\mathbf{\Gamma} = 2 \pi \mathbf{\omega} / h` is a vector containing the reduced frequencies. [#ref3]_. The Huang-Rhys factor :math:`\mathbf{g}` is related to :math:`\mathbf{\lambda}` as: 

.. math::

   \mathbf{g} = \mathbf{\lambda}^2

The reorganization energy per mode is  

.. math::

   \mathbf{E} = (h / 2 \pi) * \mathbf{\omega} \mathbf{\lambda}^2
   
When the displacement vector :math:`\mathbf{k}`, the reduced frequencies :math:`\mathbf{\Gamma}` and :math:`\mathbf{\Gamma}'`, and the Duschinsky rotation matrix :math:`\mathbf{J} = \mathbf{L'}^T \mathbf{B}_0 \mathbf{L}` have been obtained, the Franck-Condon factors can be calculated using the two-dimensional array method of Ruhoff and Ratner [#ref3]_. 

There is one Franck-Condon factor for every permutation of the vibrational quanta over both states. Since they represent transition probabilities, all Franck-Condon factors of one state which respect to one vibrational state of the other state must sum to one. Since the total number of possible vibrational quanta, and hence the total number of permutations, is infinite, in practice we will calculate the Franck-Condon factors until those sums are sufficiently close to one. Since the number of permutations rapidly increases with increasing number of vibrational quanta, it is generally possible to already stop after the sum is greater than about two thirds. The remaining one third will be distributed over so many Franck-Condon factors that their individual contributions are negligible. 

In the limiting case of one vibrational mode, with the same frequency in both states, the expression for the Franck-Condon factors of transitions from the ground vibrational state to an excited vibrational state are given by the familiar expression: 


.. math::

   |l_{0,n}|^2 = e^{-\lambda^2} \lambda^{2n} / n!


Algorithm
^^^^^^^^^

The algorithm for the calculation of the FC integrals is based on the work by Santoro et al. [#ref4]_ which is here summarized.
There are in principle infinite FC factors that should be computed in order to achieve 100% convergence in the spectrum.
This number is reduced by dividing the vibrational into classes.

A class is defined based on the number of simultaneously excited vibrational modes, thus a class 3 state has exactly 3 modes which are simultaneously excited, while all the remaining modes have zero quanta.
The *fcf* program first evaulates the class 1 e 2 FC up to a fairly large vibrational quantum number and uses these results to infer how much each mode should be excited for the calculation of the integrals involving states of higher classes.
We refer to the original paper for the details of the algorithm.

The convergence of the results after each class can be estimated by summing all FC factors, which should converge to 1 in the limit of a complete set.
The program is terminated when the maximum allowed class is reached, when there is little gain from one class to the next, or when a sufficient convergence criterion is met.
It should be noted that if one is interested in the overall shape of the spectrum then in most cases it isn't necessary to reach a convergence that is close to 100%.


Input
^^^^^

The input for *fcf* is keyword-oriented and is read from the standard input. *fcf* recognizes several keywords, but only the states have to be specified to perform the calculation. All input therefore contains at least the following lines: 

.. _keyscheme fcf: 


::

   $AMSBIN/fcf << eor
      STATE1 state1
      STATE2 state2
   eor

The spectrum is always calculated from the ground vibrational state belonging to the potential energy surface specified by *state1* to the vibronic states belonging to *state2*.
Documentation for all keys of *fcf*:

::

   $AMSBIN/fcf << eor
      State1 state1
      State2 state2
      Lambda float
      Modes first last
      Rotate [True | False]
      Translate [True | False]
      NumericalQuality ["Basic" | "Normal" | "Good" | "Excellent"]
      Prescreening
         Class1   integer
         Class2   integer
         MaxClass integer
         MaxFCI   integer
      End
      Spectrum FreqMin FreqMax NFreq
         LineShape ["Stick" | "Gaussian" | "Lorentzian" ]
         SpcMin float
         SpcMax float
         SpcLen integer
         HWHM   float
      End
      Printing
         Verbose
         FCFThresh float
      End
   eor

.. scmautodoclist:: fcf

Only a few keys from the .rkf file are used for the calculation of the Franck-Condon factors. Disk space usage can be significantly reduced by extracting just these keys from the .rkf file before further analysis. The following shell script will extract the keys from the KF file specified by the first argument and store them in a new KF file specified by the second argument using the *cpkf* utility: 

::

   #!/bin/sh
   cpkf $1 $2 General Molecule Vibrations

Result: TAPE61
^^^^^^^^^^^^^^

After a successful calculation, *fcf* produces a TAPE61 KF file. All results are stored in the Fcf section: 

.. csv-table:: 
   :widths: 250,350

   **contents of TAPE61**,**comments**
   lambda,the minimum value of the electron-phonon coupling
   "translate, rotate",whether the TRANSLATE and ROTATE options were specified in the input
   natoms,number of atoms in the molecule
   mass,atomic mass vector (**m**)
   "xyz1, xyz2",equilibrium geometries of both states (**x**\ :sub:`0`  and **x**\ :sub:`0` ')
   b0,zero-order axis-switching matrix matrix (**B**\ :sub:`0` )
   nmodes,number of vibrational modes with a non-zero frequency
   "gamma1, gamma2",reduced frequencies of both states (Γ and Γ')
   "lmat1, lmat2",mass-weighted normal modes of both states (**L** and **L**')
   jmat,Duschinsky rotation matrix (**J**)
   "kvec1, kvec2","displacement vectors for both states (**k** and **k'**, kvec1 is used for the calculation of the Franck-Condon factors)"
   "lambda1, lambda2",electron-phonon couplings for both states (λ and λ')
   i0,"ground state to ground state overlap integral (I\ :sub:`0,0` )"
   
In addition to producing a binary TAPE61 file, *fcf* also writes the frequencies, displacement vectors and electron-phonon couplings for both states to the standard output. 


FCF example absorption and fluorescence
---------------------------------------

In this example it is assumed that the molecule has a singlet ground state S\ :sub:`0` , and the interesting excited state is the lowest singlet excited state S\ :sub:`1` . First one needs to a the ground state geometry optimization, followed by a frequency calculation.
For the ground state frequency calculation we will use AMS_JOBNAME=S0.
Next one needs to do an excited state geometry optimization. Here it is assumed that the lowest singlet excited state S\ :sub:`1`  is of interest: 

::

   AMS_JOBNAME=S1_GEO $AMSBIN/ams <<eor
      ...
      Task GeometryOptimization
      Engine ADF
         ...
         Excitation
            Onlysing
            Lowest 1
         End
         ExcitedGO
            State A 1
            Singlet
         End
      EndEngine
   eor

To get the frequencies for this excited state, numerical frequencies need to be calculated, at the optimized geometry of the first excited state:

::

   AMS_JOBNAME=S1 $AMSBIN/ams <<eor
      ...
      LoadSystem
         File S1_GEO.results/adf.rkf
      End
      Task SinglePoint
      Properties
         NormalModes True
      End
      Engine ADF
         ...
         Excitation
            Onlysing
            Lowest 1
         End
         ExcitedGO
            State A 1
            Singlet
         End
      EndEngine
   eor

Next for the absorption spectrum, we look at excitations from the lowest vibrational state of the electronic ground state to the vibrational levels of the first singlet excited state S\ :sub:`1`  (S\ :sub:`1`  :math:`\leftarrow`  S\ :sub:`0` ), using the   :ref:`FCF program<FCF>`, which calculates the Franck-Condon factors between the vibrational modes of the two electronic states, with input 

::

   $AMSBIN/fcf << eor
      STATE1 S0.results/adf.rkf
      STATE2 S1.results/adf.rkf
      TRANSLATE
      ROTATE
   eor

See  :ref:`the description of FCF program<FCF>` for more details. 

For the fluorescence spectrum, we look at excitations from the lowest vibrational state of the first singlet excited state  S\ :sub:`1`  to the vibrational levels of the singlet ground state state  S\ :sub:`0`  (S\ :sub:`1`  →  S\ :sub:`0` ). Input for the  :ref:`FCF program<FCF>` is in this case: 

::

   $AMSBIN/fcf << eor
      STATE1 S1.results/adf.rkf
      STATE2 S0.results/adf.rkf
      TRANSLATE
      ROTATE
   eor

Note that the FCF program calculates the spectrum relative to the 0-0 transition. Thus one should add to spectrum calculated with FCF the difference in energy of the lowest vibrational state of the ground state S\ :sub:`0`  and the lowest vibrational state of the electronically singlet excited state S\ :sub:`1` . 


FCF Example phosphorescence
---------------------------

In this example it is assumed that the molecule has a singlet ground state S\ :sub:`0` , and the interesting excited state is the lowest triplet excited state T\ :sub:`1` . Emission from a triplet state to a singlet state is spin forbidden, however, due to spin-orbit coupling such transitions may occur. In the following we assume that the geometry of the triplet excited state is not influenced much by spin-orbit coupling. 

First one needs to a the ground state geometry optimization, followed by a frequency calculation, using AMS_JOBNAME=S0. Next one needs to do an excited state geometry optimization of the lowest triplet excited state, followed by a frequency calculation. 


::

   AMS_JOBNAME=T1 $AMSBIN/ams <<eor
      ...
      Task GeometryOptimization
      Properties
         NormalModes True
      End
      Engine ADF
         Unrestricted
         SpinPolarization 2.0
      EndEngine
   eor

For the phosphorescence spectrum, we look at excitations from the lowest vibrational state of the first triplet excited state  T\ :sub:`1`  to the vibrational levels of the singlet ground state state  S\ :sub:`0`  (T\ :sub:`1`  →  S\ :sub:`0` ). Input for the  :ref:`FCF program<FCF>` is in this case: 

::

   $AMSBIN/fcf << eor
      STATE1 T1.results/adf.rkf
      STATE2 S0.results/adf.rkf
      TRANSLATE
      ROTATE
   eor

Note that the FCF program calculates the spectrum relative to the 0-0 transition. Thus one should add to spectrum calculated with FCF the difference in energy of the lowest vibrational state of the ground state S\ :sub:`0`  and the lowest vibrational state of the electronically triplet excited state T\ :sub:`1` . 

Zero field splitting (ZFS) and the radiative rate constants (i.e. radiative phosphorescence lifetimes) could be calculated  with spin-orbit coupled ZORA time-dependent density functional theory (ZORA-TDDFT). With the ADF engine spin-orbit coupling can be treated self-consistently (i.e. non perturbatively) during both the SCF and TDDFT parts of the computation.

An alternative to the use of the unrestricted formalism to calculate the lowest triplet excited state is to use the TDDFT formalism: 

::

   AMS_JOBNAME=T1_GEO $AMSBIN/ams <<eor
      ...
      Task GeometryOptimization
      Engine ADF
         Excitation
            Onlytrip
            Lowest 1
         End
         ExcitedGO
            State A 1
            Triplet
         End
      EndEngine
   eor

To get the frequencies for this excited state, numerical frequencies need to be calculated, at the optimized geometry of the first excited state. 

::

   AMS_JOBNAME=T1 $AMSBIN/ams <<eor
      ...
      LoadSystem
         File T1_GEO.results/adf.rkf
      End
      Task SinglePoint
      Properties
         NormalModes True
      End
      Engine ADF
         ...
         Excitation
            Onlytrip
            Lowest 1
         End
         ExcitedGO
            State A 1
            Triplet
         End
      EndEngine
   eor

.. only:: html

  .. rubric:: References

.. [#ref1] J.S. Seldenthuis, H.S.J. van der Zant, M.A. Ratner and J.M. Thijssen, *Vibrational Excitations in Weakly Coupled Single-Molecule Junctions: A Computational Analysis*, `ACS Nano 2, 1445 (2008) <https://doi.org/10.1021/nn800170h>`__ 

.. [#ref2] G.M. Sando and K.G. Spears, *Ab Initio Computation of the Duschinsky Mixing of Vibrations and Nonlinear Effects*, `Journal of Physical Chemistry A 105, 5326 (2001) <https://doi.org/10.1021/jp004230b>`__ 

.. [#ref3] P.T. Ruhoff and M.A. Ratner, *Algorithms for computing Franck-Condon overlap integrals*, `International Journal of Quantum Chemistry 77, 383 (2000) <https://doi.org/10.1002/(SICI)1097-461X(2000)77:1%3C383::AID-QUA38%3E3.0.CO;2-0>`__ 

.. [#ref4] F.\  Santoro, R. Improta, A. Lami, J. Bloino, V. Barone, *Effective method to compute Franck-Condon integrals for optical spectra of large molecules in solution*, `J. Chem. Phys. 126, 084509 (2007) <https://doi.org/10.1063/1.2437197>`__ 
