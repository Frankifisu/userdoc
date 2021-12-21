.. _EXCITEDGO: 
.. index:: excited state optimizations 

Excited state (geometry) optimizations
**************************************

.. seealso::
  
  * Tutorial `UV/Vis spectrum of ethene <../../Tutorials/GettingStarted/ExcitationsAndUVVisOfEthene.html>`__


It is possible to do excited state geometry optimizations, see Ref. [#ref1]_. Note that not all aspects of such calculations have been tested thoroughly. 

With the keyword EXCITEDGO the gradients of the TDDFT excitation energy can be calculated. The :ref:`EXCITATIONS <keyscheme EXCITATIONS>` block must also be included in the input. The excitation energy gradients will only be calculated if the ground state gradients are calculated. 

The gradients of the excitation energy are combined with the ground state gradients to give the gradients of the excited state. These gradients can be used in much the same way as ground state gradients are used. The type of calculation is chosen in the same way as for a ground state calculation. Examples of possible run types are: 

+ Geometry optimization
+ Transition state search 
+ Frequency analysis with numerical second derivatives: (analytical second derivatives  are not possible).

In general, an option that applies to a ground state geometry optimization will also apply to an excited state geometry optimization. A TDDFT geometry optimization will proceed in very much the same way as a ground state geometry optimization. The major difference will be that a TDDFT calculation will take place after the SCF and before the ground state gradients are evaluated. TDDFT gradients are calculated after the ground state gradients. 

Gradients for closed-shell singlet-singlet, closed shell singlet-triplet, conventional open shell and spin-flip open-shell TDDFT calculations can be evaluated. The FORCEALDA option and TDA options should be used with spin-flip calculations. 

Not all functionals can be used in combination with TDDFT gradients. The following should work: 

LDA: VWN, XALPHA 

GGA: Any allowed combination of the Perdew86, LYP and PBEc correlation functionals and the Becke88, revPBEx, RPBEx, PBEx and OPTx exchange functionals. 

Hybrid: B1LYP, B3LYP, B3LYP*, BHANDHLYP, BHANDH, O3LYP, X3LYP, B1PW91, MPW1PW, PBE0, OPBE0.

Most LibXC GGA and hybrid functionals.

RS Hybrid icw XCFUN: CAMY-B3LYP and more (starting form ADF2018).

QM/MM TDDFT gradients can be calculated. 

COSMO TDDFT gradients can be calculated (starting from ADF2018).

Scalar relativistic effects can be included with the ZORA or mass-velocity-Darwin Hamiltonians. 

At this time, gradients involving frozen cores and spin-orbit TDDFT can not be calculated. 

TDDFT gradients can take advantage of symmetry but if the point group of interest includes degenerate irreducible representations then all grid points are needed in integration (equivalent to the ALLPOINTS keyword). This situation is detected automatically. This use of the full grid may make it more efficient to use a point group with only one-dimensional irreducible representations where only the symmetry-unique slice is utilized. 

Degenerate excitations can be optimized. However, since in reality such degeneracies will be split by a Jahn-Teller distortion it is recommended that the symmetry of the chosen point group be lowered so that the transition of interest is no longer labeled by a degenerate representation. A Jahn-Teller distortion will not occur when the degeneracy cannot be broken by nuclear motion, e.g. for a diatomic molecule. 

The EXCITEDGO block key has the following form: 

.. _keyscheme EXCITEDGO: 


::

   EXCITEDGO
    {STATE Irreplab nstate}
    {SINGLET/TRIPLET}
    {OUTPUT n}
    {CPKS EPS=err PRECONITER=precon NOPRECONITER=noprecon ITEROUT=iter}
    {EIGENFOLLOW}
   END

``STATE Irreplab nstate``
   Choose the excitation for which the gradient is to be evaluated.

   ``Irreplab``
      Irreplab is the label from the TDDFT calculation. NOTE: the TDDFT module uses a different notation for some representation names, for example, A' is used instead of AA, A'' (A two apostrophes) instead of AAA, A1' instead of AA1, A2'' instead of AAA2. The excitations output gives the irrep levels that one should use here.

   ``nstate``
      This value indicates that the nstate-th transition of symmetry Irreplab is to be evaluated. Default is the first fully symmetric transition. 

   Note that in a numerical FREQUENCIES calculation symmetry is turned off except to reduce the number of points calculated so irrespective of the specified point group Irreplab is A in this case. Care should be taken to ensure that nstate is correct in a frequencies calculation as this number can change when the point group is changed. 

``SINGLET/TRIPLET``
   SINGLET: A singlet-singlet excitation is considered. The default. TRIPLET: A singlet-triplet excitation is considered. 

``OUTPUT n``
   The amount of output printed. A higher value requests more detailed output. Default: n=0 

``CPKS EPS=err PRECONITER=precon NOPRECONITER=noprecon ITEROUT=iter``
   Some control parameters for the CPKS(Z-vector) part of the TDDFT gradients calculation. 

   ``EPS=err``
      err is a real number that gives the convergence requirement of the CPKS. Default is 0.0001 

   ``PRECONITER=precon``
      precon is the maximum number of iterations allowed for the preconditioned solver. Default = 30. 

   ``NOPRECONITER=noprecon``
      noprecon is the maximum number of iterations allowed for the unpreconditioned solver. Default=200. 

   ``ITEROUT=iter``
      Details of the CPKS calculation are printed every iter iterations. Default is 5. 

``EIGENFOLLOW``
   This key tries to follow the eigenvector in excited state geometry optimizations. In the initial implementation the target state of an excited state geometry optimization was indicated by a number and a symmetry, e.g. A2g 3 or the 3rd state of A2g symmetry. This approach becomes problematic when states cross and the state you are interested in become the 4th A2g state for example. An eigenvector-following option has been added that attempts to alleviate this problem. This option is off by default. If the subkeyword EIGENFOLLOW in is included, the state of interest in the first iteration is the same as before. In the second and subsequent iterations the state for which gradients are determined is decided on the basis of the overlap between the transition density of the transition from the previous iteration and the transition densities available in the current iteration. The same symmetry is maintained. Note that this method is not full proof. It assumes that the transition density changes only because of the contributions from the various occupied-virtual orbital pairs change but that the orbitals remain unchanged. This is not necessarily the case. Secondly, the sign of the transition density components is not taken into account. 

At each iteration of a TDDFT-gradients calculation the (relaxed) excited state electric dipole moment is also calculated.


Nuclear gradients only
^^^^^^^^^^^^^^^^^^^^^^

In some cases one only needs the nuclear gradients of 1 or more excited state in a single point calculation.
This can be calculated by requesting the gradients in the AMS driver part of the input icw the EXCITEDGO keyword.

::
  
  Task SinglePoint

  Properties
    Gradients Yes
  End

  ...
  ...

  Engine ADF
     ...
     ...
     
     EXCITEDGO
       AllGradients
       SING_GRADS
          {IRREP1 integer_list}
          {IRREP2 integer_list}
       End
       TRIP_GRADS
          {IRREP3 integer_list}
          {IRREP4 integer_list}
       End
     End
   EndEngine

``AllGradients``
   calculate the nuclear gradient for all excitations that are calculated.

``SING_GRADS``
   Calculate the nuclear gradient for the singlet-singlet excitations that are specified.
   The excitation numbers per irrep should be specified.

``TRIP_GRADS``
   Calculate the nuclear gradient for the singlet-triplet excitations that are specified.
   The excitation numbers per irrep should be specified.

.. [#ref1] M.\  Seth, G. Mazur, and T. Ziegler, *Time-dependent density functional theory gradients in the Amsterdam density functional package: geometry optimizations of spin-flip excitations*, `Theoretical Chemistry Accounts 129, 331 (2011) <https://doi.org/10.1007/s00214-010-0819-2>`__ 
