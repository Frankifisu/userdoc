.. index:: SCF 
.. _SCF:

SCF
===

The SCF procedure is regulated with keys that set the maximum number of iterations, the convergence criterion, and various items that control the iterative update method. Molecules may display wildly different SCF-iteration behavior, ranging from easy and rapid convergence to troublesome oscillations. We expect that the default settings take care of most cases, but one should realize that this is a difficult and tricky subject. The user has a few (main) options to adapt the procedure to the situation at hand: simple damping or one of the SCF acceleration schemes. 

.. seealso::

  In case of SCF convergence problems, see :ref:`scf recommendations`

At each cycle the electron density is computed as a sum of occupied orbitals squared; the new density defines the  potential from which the orbitals are re-computed. The cycle is repeated until convergence is reached. To speed-up convergence and to avoid non-convergent oscillatory behavior the values at the next iteration are constructed as a mixture of the computed new data and those used at the cycles before. This may involve only the previous cycle and is then called *damping*. Alternatively some sort of DIIS (direct inversion in iterative space) or LIST (LInear-expansion Shooting Technique) procedure can be invoked, which is a generalization of damping to include more previous iterations. 

Starting from ADF2016, the SCF module has been rewritten from scratch. The old SCF is still available and it can be switched on using the ``OldSCF`` keyword. The description below refers to the new SCF code only. User documentation for the OldSCF module is available in the ADF2014 User's Guide.

.. index:: DIIS 
.. index:: LISTb, LISTf, LISTi 
.. index:: SCF accelerators
.. _DIIS:

There are various SCF acceleration techniques implemented in ADF. By default the mixed ADIIS+SDIIS method by Hu and Wang [#ref1]_ is used, unless the number of DIIS expansion vectors is set to zero (see the ``DIIS N`` key below) or ``NoADIIS`` is specified. Here, SDIIS stands for the original Pulay DIIS scheme. Other available methods mostly belong to the ``LIST`` family developed in the group of Y.A. Wang. The ARH and Energy-DIIS methods are available with the ``OldSCF`` method only.


Main options
------------

Subkeys in the data block of the master key SCF control the aspects mentioned above. Each subkey is optional. Curly brackets are not part of the key. Omission means the application of default values. Omission of the SCF block altogether implies defaults for all subkeys. 

.. _keyscheme SCF: 


::

   SCF
    Iterations Niter
    Converge SCFcnv { sconv2 }
    AccelerationMethod { ADIIS | LISTi | LISTb | fDIIS | LISTf | MESA | SDIIS }
    MESA [NoFDIIS] [NoLISTb] [NoLISTf] [NoLISTi] [NoSDIIS] [NoADIIS]
    ADIIS 
      {THRESH1 a1} 
      {THRESH2 a2}
    End
    NoADIIS
    DIIS 
      {N n} 
      {OK ok} 
      {cyc cyc}
    End
    Mixing mix
    Mixing1 mix1
    OldSCF
   End

``Iterations Niter``
   ``Niter``
      The maximum number of SCF cycles allowed. In case of Geometry Optimizations it applies separately to each of the SCF procedures that are executed. Default is 300. The program executes at least one cycle, even if you specify a non-positive number. 

``Converge SCFcnv { sconv2 }``
   ``SCFcnv``
      The criterion to stop the SCF updates. The tested error is the commutator of the Fock matrix and the P-matrix (=density matrix in the representation of the basis functions) from which the F-matrix was obtained. This commutator is zero when absolute self-consistency is reached. Convergence is considered reached when the maximum element falls below SCFcnv and the norm of the matrix below 10*SCFcnv. The default is 1e-6 (in Create mode: 1e-8). 

   ``sconv2``
      A second criterion which plays a role when the SCF procedure has difficulty converging. When in any SCF procedure the currently applicable criterion does not seem to be achievable, the program stops the SCF. When the secondary criterion (sconv2) has been met, only a warning is issued and the program continues normally. If the secondary criterion was not met either, the program terminates any further geometry optimizations, frequency steps, etc. You can prevent the program from terminating in such a case with the key ALLOW. The default for sconv2 is 1e-3. 

.. index:: SCF acceleration method
.. _AccelerationMethod:
.. _LISTi:

``AccelerationMethod`` 
   Specify which SCF acceleration method must be invoked. By default the ADIIS+SDIIS method (denoted as ADIIS) is used and normally it results in optimal performance. In some cases it may be useful to use one of the methods from the LIST family or fDIIS. The LIST family methods have been implemented following publications by the group of Y.A. Wang [#ref2]_ [#ref3]_. The number of vectors to store specified by ``DIIS N`` also applies to the LIST methods. This number is a very important parameter and it is worthwhile increasing or decreasing it in case of SCF convergence problems. A word of caution: do not just blindly increase the number for every system. Testing showed that a large number breaks convergence for some, mainly small, systems.

.. index:: MESA 
.. _MESA:

``MESA``
   The MESA method has also been developed in the group of Y.A. Wang [#ref3]_. It combines several other acceleration methods (currently ADIIS, fDIIS, LISTb, LISTf, LISTi, and SDIIS). In order to improve the method's performance, some of the components can be disabled by specifying the corresponding "No" argument. For example, to remove SDIIS from MESA specify ``MESA NoSDIIS``. Specifying this key invokes the MESA method regardless of the AccelerationMethod's value.

``ADIIS``
   This key has effect only if ADIIS acceleration method is used. The THRESH1 and THRESH2 arguments correspond to values of the maximum element of the [F,P] commutator matrix, ErrMax. If ErrMax :math:`\geq` *a1* then only A-DIIS coefficients are used to determine the next Fock matrix. If ErrMax :math:`\leq` *a2* then only SDIIS coefficients are used. For ErrMax between *a2* and *a1* the total DIIS coefficients are calculated from SDIIS and A-DIIS values weighted proportionally according to the ErrMax value. Thus, the weight of A-DIIS coefficients decreases as the ErrMax value becomes smaller. The default values for a1 and a2 are 0.01 and 0.0001, respectively. In difficult SCF cases, especially when the Pulay DIIS appears to be unstable, it may be worth trying to decrease the thresholds and let A-DIIS approach the final solution on its own. 

``NoADIIS``
   If OldSCF is not set, specifying NoADIIS has the same effect as setting AccelerationMethod to SDIIS. it disables A-DIIS and switches SCF to a damping+SDIIS scheme. In this scheme, SCF starts with simple damping (a.k.a. mixing) and continues until the maximum element value of the [F,P] commutator drops below the ``DIIS OK`` parameter but for no more than ``DIIS Cyc`` iterations. After this, the pure SDIIS scheme becomes effective till the end of the SCF procedure. If OldSCF is set then specifying NoADIIS disables the automatic switching to ADIIS+SDIIS in case of a difficult SCF convergence.

``DIIS``
   The DIIS sub-block specifications can be given to control the SCF acceleration procedure. All these specifications are optional. Normally, ADIIS+SDIIS is activated starting from the 2nd iteration regardless of the ``OK`` and ``Cyc`` settings below. The two settings become effective only when ``NoADIIS`` is specified.

   ``N``
      The number of expansion vectors used for accelerating the SCF. The number of previous cycles taken into the linear combination is then n-1 (the new computed potential is also involved in the linear combination). By default n=10. An input value smaller than 2 disables the DIIS. Note that this number applies not only to Pulay DIIS scheme but also to other DIIS-like methods, such as A-DIIS and LIST methods. 
      It should be noted that methods from the LIST family are quite sensitive to the number of expansion vectors used. For this reason, these methods have a built-in limit on the number depending on the iteration number and the degree of convergence. The number of vectors in LIST increases when approaching convergence but it is always limited by ``DIIS N``, which is a hard limit. It may be useful to set ``DIIS N`` to a value larger than 10 when using a LIST method with a difficult to converge system. A value between 12 and 20 can sometimes get the job done.

   ``OK``
      The SDIIS starting criterion, when A-DIIS is disabled, by default 0.5 a.u..

   ``Cyc``
      When A-DIIS is disabled, the SDIIS will start at this iteration (by default 5) irrespective of the ``DIIS OK`` value above.

``Mixing mix``
   ``mix``
      When none of the SCF acceleration methods is active, the next Fock matrix is determined as :math:`F = mix F_{n} + (1-mix) F_{n-1}`.
      The default value is 0.2. 

``Mixing1 mix1``
   ``mix1``
      A different mixing parameter value for the first SCF cycle. By default, equal to ``Mixing``.

``OldSCF``
   Enforce the old SCF procedure. It will also be used automatically when one of the following is true:
   ``Occupations Steep`` is specified, level-shifting is enabled (see the ``Lshift`` key below), the augmented Roothaan-Hall method is enabled (see the ``ARH`` key below), the Energy-DIIS method is enabled (see the ``EDIIS`` key below), the SIC-OEP method is used, the ``RESTOCC`` key is specified.

.. _Lshift:

``Lshift vshift``
   Level shifting is currently not implemented in the new SCF, therefore specifying ``Lshift`` enables ``OldSCF`` automatically.

   ``VShift``
      The level shifting parameter. The diagonal elements of the Fock matrix, in the representation of the orbitals of the previous iteration, are raised by vshift hartree energy units for the virtual orbitals. This may help to solve convergence problems when during the SCF iterations charge is sloshing back and forth between different orbitals that are close in energy and all located around the Fermi level. Level shifting is not supported in the case of Spin-Orbit coupling. **At the moment properties that use virtuals, like excitation energies, response properties, NMR calculations, will give incorrect results if level shifting is applied.** 

``Lshift_err Shift_err``
   ``Shift_err``
      Specifies that level shifting will be turned off by the program as soon as the SCF error drops below a threshold; default value: 0. 

``Lshift_cyc Shift_cyc``
   ``Shift_cyc``
      Specifies that level shifting is not turned on before the given SCF cycle number (for the start-up geometry); default value: 1. 

.. note::

   *Electron smearing*, may be used to overcome convergence difficulties. The idea is to distribute electron occupations fractionally over the states around the Fermi level using the Fermi distribution function. This aspect is controlled by the Smear or the ElectronTemperature option of the Occupations key. See the Occupations key for more details. 

.. note:: 

   A-DIIS is not compatible with enforced non-aufbau electronic configurations and it is disabled in such a case automatically. A non-aufbau electronic configuration may be enforced using a block form of the Occupations key, but it may also result from the KeepOrbitals (a.k.a. orbital tracking) feature.

.. index:: Energy-DIIS 
.. index:: EDIIS 
.. _energy DIIS:


Energy-DIIS
-----------

::

   SCF
    EDIIS
    ...
   End


Energy-DIIS is implemented following the paper by Kudin, Scuseria, and Cances  [#ref4]_. The method is invoked by specifying an EDIIS keyword in the SCF block. Please note that similar to ARH and unlike the standard SCF procedure in ADF this method requires energy evaluation at each SCF cycle, which makes it significantly slower compared to energy-free SCF. You might need a higher integration accuracy to get an accurate total energy. The same restrictions apply as for the key  :ref:`TOTALENERGY<keyscheme TOTALENERGY>`. The EDIIS method will start at the 2nd SCF cycle, and the size of the DIIS space will be the same as for the normal DIIS. This subkey EDIIS can be used in addition to the other subkeys of the block key SCF. This method has been superseded by A-DIIS and the LIST family methods.


.. index:: ARH 
.. index:: Augmented Roothaan-Hall 
.. _ARH:


Augmented Roothaan-Hall (ARH)
-----------------------------

The Augmented Roothaan-Hall method has been developed by T. Helgaker and coworkers and is  extensively discussed in Ref.  [#ref5]_. The basic idea of the method is that the density matrix is optimized directly to minimize total  energy. At each step, the new density matrix is parametrized in terms of matrix exponent:  

P\ :sub:`new`  = exp(-X) P\ :sub:`old`  exp(X),  

here, X is an anti-symmetric step matrix subject to the following conditions: 

X = argmin{E(P(X))}  - X minimizes the energy     

\|X\| < h            - length of X is smaller than or equal to some trust radius 

The optimal X is found using a Conjugate Gradient method, possibly with pre-conditioning. The trust radius is updated based on how well the energy change is predicted. 

.. _keyscheme ARH: 

**ARH Input**

The ARH procedure is invoked by including the ARH block in the SCF input block. This subkey ARH can be used in addition to the other subkeys of the block key SCF. 


::

   SCF
     ARH 
       {CONV conv} 
       {ITER iter} 
       {NSAVED nsaved} 
       {START start}
       {FINAL} ...
     End
     ...
   End
   SYMMETRY NOSYM

All parameters in the ARH keyword are optional.  The following arguments determine the main parameters of the ARH procedure. 

``CONV conv``
   ARH convergence criterion. When the RMS gradient and its maximum  components are both lower than the criterion, the ARH procedure will be considered converged.  The default value is 10\ :sup:`-4` . 

``ITER iter``
   Maximum number of ARH iteration to perform. Please note that in difficult cases a huge number of iterations may be required for complete SCF convergence. The default value is 500. 

``FINAL``
   Determines whether SCF is continued after ARH has completed. If this option is set,  one Fock matrix diagonalization will be performed to get orbitals and the SCF procedure will be  halted. By default this option is OFF. 

``START start``
   Sets the SCF cycle number on which the ARH method is invoked. The default value is 2.  Using a larger value may provide a better starting guess for the ARH minimization. 

``NSAVED nsaved``
   Sets the number of saved density and Fock matrices used for augmentation of the electronic Hessian.  The default value is 8. A larger nsaved value should be used in difficult cases when the number  of orbitals very close to the Fermi level is large.  

The default minimization method is Untransformed Pre-conditioned Conjugate Gradient. The following two parameters may be used to change this. 

``NOPRECOND``
   Disables pre-conditioning during the CG minimization.  This option should not be used if atoms heavier than the second-row elements are present. 

``TRANSPCG``
   Specifying this option will enable the use of the Transformed Pre-conditioned CG method,  which may result in better SCF convergence in some cases. 

At each SCF step, the procedures begins by performing usual CG minimization keeping track of the  total step length. If at some micro-iteration the step length exceeds the trust radius, the procedure switches to  trust-radius optimization in the reduced space, which, in turn, is halted as soon as the level-shift  parameter *mu* has converged. The final step is then calculated as a Newton step in the reduced space  of all the trial vectors generated during CG minimization. The following options may be used to modify  this behavior. 

``NOSWITCHING``
   Setting this option turns OFF the switching from the normal CG to a trust-radius  minimization in reduced space. Using this option helps to reduce the total number of SCF cycles  is some cases. 

``SHIFTED``
   Setting this option will turn ON the trust-radius optimization from the first micro- iteration. 

``CGITER=cgiter``
   Sets the maximum number of micro-iterations. 

The next two options determine the trust radius. 

``TRUSTR=trustr``
   Initial value for the trust radius. Default: 0.5 

``MAXTRUSTR=maxtrustr``
   The maximum trust radius value. This is set to 0.5 by default and should never be changed. 

**ARH Notes and Recommendations**

**Restriction:** The method currently works for symmetry NOSYM calculations only. The NOSYM  requirement comes from the fact that during direct optimization of the density matrix  it may have a symmetry lower than that of the molecule. 

The method requires the total energy to be calculated at each step, which makes it much more  expensive compared to the standard SCF procedure that does not need the energy. Therefore, the method should only be used when the standard SCF procedure fails.  Another complication caused by the use of the total energy is that somewhat higher  integration accuracy may be required to get stable SCF convergence, and that the method may not be applicable in all cases. It is also recommended to use the :ref:`ADDDIFFUSEFIT<keyscheme ADDDIFFUSEFIT>`  keyword  or a higher ZlmFit quality setting to increase accuracy of the total energy and, thus, improve convergence.  Please refer to the  :ref:`TOTALENERGY<keyscheme TOTALENERGY>` keyword for more information. 


.. only:: html

  .. rubric:: References


.. [#ref1] X.\  Hu and W. Yang, *Accelerating self-consistent field convergence with the augmented Roothaan-Hall energy function*, `Journal of Chemical Physics 132, 054109 (2010) <https://doi.org/10.1063/1.3304922>`__ 

.. [#ref2] Y.A. Wang, C.Y. Yam, Y.K. Chen, G. Chen, *Communication: Linear-expansion shooting techniques for accelerating self-consistent field convergence*, `Journal of Chemical Physics 134, 241103 (2011) <https://doi.org/10.1063/1.3609242>`__ 

.. [#ref3] M.A. Garcia Chavez, *Numerical methods in quantum chemistry to accelerate SCF convergence and calculate partial atomic charges*, PhD Thesis, `University of British Columbia, (2018), <http://dx.doi.org/10.14288/1.0372885>`__

.. [#ref4] K.N. Kudin, G.E. Scuseria and E. Cances, *A black-box self-consistent field convergence algorithm: One step closer*, `Journal of Chemical Physics 116, 8255 (2002) <https://doi.org/10.1063/1.1470195>`__ 

.. [#ref5] S.\  Høst, J. Olsen, B. Jansík, L. Thøgersen, P. Jørgensen and T. Helgaker, *The augmented Roothaan-Hall method for optimizing Hartree-Fock and Kohn-Sham density matrices*, `Journal of Chemical Physics 129, 124106 (2008) <https://doi.org/10.1063/1.2974099>`__ 
