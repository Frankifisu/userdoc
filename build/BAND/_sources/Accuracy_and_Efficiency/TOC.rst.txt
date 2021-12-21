.. index:: Accuracy

Accuracy and Efficiency
***********************

Given a :ref:`Model Hamiltonian <ModelHamiltonian>`, the most important aspects determining the accuracy of a Band calculation are:

* :ref:`basis Set`
* :ref:`k-space`

Also important, but to a lesser degree, are the following aspects:

* :ref:`Numerical Integration (BeckeGrid)<numerical_integration>`
* :ref:`Density fitting (ZlmFit)<band-key-ZlmFit>`
* :ref:`Basis-set confinement (SoftConfinement)<band-key-SoftConfinement>`
* :ref:`SCF convergence (Convergence)<band-key-Convergence>`
* :ref:`Hartree–Fock Resolution of the Identity (RIHartreeFock)<band-key-RIHartreeFock>` (only for hybrid functionals)

The CPU time and memory requirements strongly depends on these options, as does the accuracy of the results.

**General NumericalQuality**

A simple way of tweaking the accuracy of the calculation is via the **NumericalQuality** key. This sets the quality of several technical aspects of a Band calculation (with the notable exception of the :ref:`basis set <basis set>`)

.. scmautodoc:: band NumericalQuality

.. toctree::
   :maxdepth: 2

   Basis_Set
   K-Space_Integration
   Numerical_Integration
   Density_Fitting
   Hartree-Fock_RI
   SCF
   More_Technical_Settings





