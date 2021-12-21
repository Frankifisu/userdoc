Troubleshooting
***************

.. _scf_does_not_converge: 

SCF does not converge
=====================

Some systems are more difficult to converge than others. A Pd slab for instance is easier to converge than an Fe slab. Generally, what you do in a problematic case is to go for more conservative settings. The two main option are to decrease ``SCF%Mixing`` and/or ``DIIS%Dimix``.    

::

   SCF  
      Mixing 0.05 ! more conservative mixing
   End

   Diis  
      DiMix 0.1 ! also more conservative strategy for DIIS procedure  
      Adaptable false ! disable automatic changing of dimix
   End

   Convergence  
      Degenerate Default ! For most calculations this is quite a good idea anyway
   End

An other option is to first run the system with a SZ basis, which may be easier to converge. Then you can :ref:`Restart <band-key-Restart>` the SCF with a larger basis set from this result.

Sometimes SCF convergence problems are caused by bad precision. An indication of this is when there are many iteration after the HALFWAY message. The simplest thing to try is to see whether increasing the ``NumericalAccuracy`` helps. Specifically an insufficient quality of the **density fit** may cause problems. For systems with heavy elements the quality of the **Becke grid** may also play a role. Another potential problem is using **only one k-point**. 

Next thing to try is the MultiSecant method. This one comes at no extra cost per SCF cycle compared to the DIIS method.
::

   SCF  
     Method MultiSecant
   End

   MultiSecantConfig
      ! put here optional keywords to tweak the MultiSecant method
   End
   
An alternative is to try a **LIST** method. For sure the cost of a single SCF iteration will increase, but it may reduce the number of SCF cycles, see :ref:`Diis%Variant <band-key-DIIS>`. 

::

   Diis
     Variant LISTi ! invoke the LISTi method
   End  

For heavy elements the use of a small or no frozen core may complicate the SCF convergence. 

Finite temperature during geometry optimization
-----------------------------------------------

Often systems are more easy to converge when applying a finite electronic temperature. By doing so your energy will deviate from the ground state. If you are optimizing, say, a fancy molecule over a Ni slab, then you do not care too much about this when the geometry is not nearly converged yet (when the gradients are still big).

Using so-called automations, it is possible to instruct band to use a higher electronic temperature in the beginning of a geometry optimization, and a lower one at the end. Similarly you can allow for more loose SCF convergence at the start of the geometry optimization. You specify such "automations" inside the ams-level GeometryOptimization block, for example

::

  GeometryOptimization

    EngineAutomations
       Gradient variable=Convergence%ElectronicTemperature InitialValue=0.01 FinalValue=0.001 HighGradient=0.1 LowGradient=1.0e-3
       Iteration variable=Convergence%Criterion InitialValue=1.0e-3 FinalValue=1.0e-6 FirstIteration=0 LastIteration=10
       Iteration variable=SCF%Iterations InitialValue=30 FinalValue=300 FirstIteration=0 LastIteration=10
    End
  End


Let us concentrate on the first "automation". What this will do is the following. 

* At the first step Convergence%ElectronicTemperature (kT) will be set to InitialValue, i.e. 0.01. (Temperatures are entered as kT in Hartree.)
* If at any step the gradient is bigger than HighGradient the temperature will be InitialValue
* If at any step the gradient is smaller than LowGradient the temperature will be FinalValue, i.e. 0.001
* If the gradient is in between HighGradient and LowGradient, a linear interpolation is done (on a logarithmic scale)
* At the last calculation FinalValue will be used, even if the geometry did not converge

Another trigger for automation is the number of geometry steps taken, shown in the two automations with "Iteration". 

Let us look at the second automation.

* At the first geometry the Convergence%Criterion is relaxed to 1.0e-3.
* After the tenth geometry step this will be 1.0e-6
* In between an interpolated value will be used

The third automation shows that you can also automate SCF%Iterations. Currently only three band keywords can be automated this way.


.. _go_does_not_converge: 

Geometry does not converge
==========================

One thing that you should make sure is that at least the **SCF converges**. If that is so, then maybe the **gradients are not accurate enough**. Here are some settings to improve the accuracy of the gradients 

::

   RadialDefaults
     NR 10000   ! more radial points 
   End
   
   NumericalQuality Good
   
Negative frequencies in phonon spectra
======================================

When doing a phonon calculation one sometimes encounter unphysical negative frequencies. There are two likely causes: either the **geometry was not in the minimum geometry**, or the **step size** used in the Phonon run is too large. Also **general accuracy** issues may be the cause, such as numerical integration, k-space integration and fit error. 

Basis set dependency
====================

A calculation aborts with the message: dependent basis. It means that for at least one k-point in the BZ the set of Bloch functions, constructed from the elementary basis functions is so close to linear dependency that the numerical accuracy of results is in danger. To check this, the program computes, for each k-point separately, the overlap matrix of the Bloch basis (normalized functions) and diagonalizes it. If the smallest eigenvalue is zero, the basis is linearly dependent. (Negative values should not occur at all!). Given the limited precision of numerical integrals and other aspects in the calculation, you are bound for trouble already if the smallest eigenvalue is very small, even if not exactly zero. The program compares it against a criterion that can be set in input (key ``Dependency`` option *Bas*).  

If you encounter such an error abort, you are strongly advised not to adjust the criterion so as to pass the internal test: there were good reasons to implement the test and to set the default criterion at its current value. Rather, you should adjust your basis set. There are two ways out: using confinement or removing basis functions. 

Using confinement
-----------------

Usually the dependency problem is due to the diffuse basis functions. This is especially so for highly coordinated atoms. One way to reduce the range of the functions is to use the Confinement key. In a slab you could consider to use confinement only in the inner layers, and to use the normal basis to the surface layers. The idea is that basis functions of the surface atoms can describe the decay into the vacuum properly, and that inside the slab the diffuseness of the functions is not needed. If all the atoms of the slab are of the same type, you should make a special type for the inner layers: simply put them in a separate Atoms block. The confinement can be specified per type. 

Removing basis functions
------------------------

You can remove one or more basis functions and maybe modify some of the (other) STO basis functions. The program prints information that helps you determine which basis functions should be modified/removed. Another way to modify your basis set, is to use the confinement keyword. This has the effect of making the diffuse basis functions more localized, thus reducing problematically large overlap with similar functions on neighboring atoms. 

In the standard output file, after the error message, you will find a list of eigenvalues of the overlap matrix. If only the first is smaller than the threshold, you should remove one basis function. If more eigenvalues are very small, it is likely that you have to remove more than one function, although you can of course try how far you can get by eliminating just one. 

Next the program prints the so-called Dependency Coefficients: a list of numbers, one for each basis function. Those with a large value are the suspicious ones. If you find two coefficients that are significantly larger than the others, you should replace the two corresponding functions by one. Easiest is to remove one of them (take the one with the bigger coefficient). If one of them is a numerical orbital from Dirac and the other an STO, remove the STO. If both are STOs, remove one and replace the other by some kind of average (regarding the radial characteristic: exponential factor and power of radial coordinate). 

To identify how the functions in your input correspond to the list the underlies the series of Dependency Coefficients, you have to set up the list of basis functions as follows: 

+ Consider an outer loop over all atom TYPES. These correspond, in order as well as in number, to the sequence of AtomType keys in your input file.

+ For each type, consider a loop over all atoms of that type, i.e. the atoms in the ATOM block corresponding to the AtomType key at hand.

+ For each atom (each AtomType key), first write down all DIRAC basis functions, then all STOs. When writing down the functions, be aware that each entry in your input file specifies a function *set*, by the quantum number L and hence corresponds to 2L+1 actual basis functions.

+ Regarding the DIRAC basis functions: they belong to the list of basis functions only if the key Valence occurs in the pertaining DIRAC input block. If not, no DIRAC functions of that type are included in the basis.     *If* the Dirac functions are included, you must omit the Core functions and include only the Valence functions from that DIRAC block. The first record in your DIRAC block with two numbers defines (by the first number) the total number of function sets in the DIRAC block (which you can verify by simple counting) and (by the second number) the number of Core function sets among them. The Core function sets, if any, are always the first so many in the list in the DIRAC block.

The program stops as soon as it encounters a dependency problem. This may happen for the first k-point. After you have adjusted the basis set following the above guidelines, you will have solved it. However, it may easily happen that the problem shows up again, but now for another (later) k-point, where other entries in the basis set may cause trouble. Do not think you have repaired the first problem incorrectly. Just repeat the procedure until you pass all k-points in the basis set construction without errors. Typically (as a last remark), although not necessarily, the first k-point may have a dependency problem from too many *s*-type functions, while other k-points may be more sensitive to the series of *p*-functions in your basis. 

Frozen core too large
=====================

BAND calculates the overlap matrix of the core functions, and this should approximate the unit matrix. When the deviation is larger then the frozen-core overlap criterion the program stops. The default criterion (0.98) is fairly strict. The safest solution is to choose a smaller frozen core. For performance reasons, however, this may not be the preferred option. In practice you might still get reliable results by setting the criterion to 0.8, see the :ref:Dependency <band-key-Dependency>` block. For the *5d* transition metals, for instance, you can often freeze the 4f orbital, thus reducing the basis set considerably. We strongly advise you to compare these results to a calculation with a smaller core. Such tests can be performed with a smaller unit cell or with a lower quality for the ``KSPACE`` block key. 

