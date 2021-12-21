
Molecules built from fragments
******************************

ADF analyzes the results in terms of user-specified subsystems from which the total system is built. The program tells you how the 'Fragment orbitals' (FO's) of the chemically meaningful sub-units mix with FO's on other fragments to combine to the final molecular orbitals.  

ADF builds a molecule from user-defined fragments, which may be single atoms or larger moieties, for example, ligands, functional groups, or complete molecules in a donor-acceptor complex. In practice, this means that the results of the ADF calculation on a fragment are saved on a file and that the fragment files are then used in setting up the calculation on the overall system. The fragment orbitals (FOs), i.e., the MOs from the calculations on the fragments, are employed as basis functions in the new calculation. This does not imply a basis set truncation or contraction because the virtual FOs are included: the FOs constitute only a transformation of the basis set. If there are symmetry-equivalent fragments, for example, the six CO molecules in octahedral Cr(CO)\ :sub:`6` , the program generates symmetry combinations of the FOs and uses the symmetrized fragment orbitals (SFOs) as basis functions. The SFOs transform as the irreducible representations (irreps) of the molecule, allowing a symmetry-driven analysis of the results. In absence of any symmetry the SFOs are identical to the FOs. 

The fragment approach offers considerable advantages. It enhances the interpretative power of ADF as it leads to a more transparent picture of bonding, which reduces from a complicated mixing of many primitive basis functions (possessing little physical relevance) to a few key interactions between meaningful fragment (frontier) orbitals. The fragment approach also improves the numerical precision. In ADF, energies are calculated directly, with respect to the fragments, by one single numerical integral of the difference energy density :math:`\epsilon[\rho,\mathbf{r}] - \sum_A \epsilon_A[\rho_A,\mathbf{r}]` between the overall molecule and the constituting fragments. 

.. math::
   
   \Delta E[\rho] = \int d\mathbf{r} \left( \epsilon[\rho,\mathbf{r}] - \sum_A \epsilon_A[\rho_A,\mathbf{r}] \right) 


In other words, we evaluate the energy of the overall molecule, :math:`E[\rho] = \int d\mathbf{r} \epsilon[\rho,\mathbf{r}]`, and the energies of each of the fragments, say the atoms that constitute the overall molecule, :math:`E_A[\rho] = \int d\mathbf{r} \epsilon_A[\rho_A,\mathbf{r}]`, in the same numerical integration grid. This provides more accurate relative energies than subtracting total energies from separate calculations, because the same relative numerical integration error applies to a much smaller quantity, yielding, in turn, a much smaller absolute error. 

Note that the user has the freedom to make his own choice of fragments. This is, however, not a matter of plain arbitrariness, and it does not make the analysis tools less meaningful. On the contrary, this freedom simply reflects the many perspectives from which a particular chemical phenomenon can be viewed. 

In practice, many calculations are performed using as fragments the so-called basic atoms, which are the smallest possible building blocks in ADF. The basic atoms are not necessarily physically realistic objects - indeed, usually they are not, as they must be spin-restricted and spherically symmetric. The computed (bonding) energy w.r.t. basic atoms, then, does not yield quantities that can be compared to experimental data directly. Rather, one must correct for the true ground state of the isolated single atoms. 

Text is mostly taken from: *Chemistry with ADF* G. te Velde, F.M. Bickelhaupt, E.J. Baerends, C. Fonseca Guerra, S.J.A. van Gisbergen, J.G. Snijders, T. Ziegler `Journal of Computational Chemistry 22, 931 (2001) <https://doi.org/10.1002/jcc.1056>`__. 

Link: :ref:`How to make molecular fragments<MOLECULARFRAGMENTS>` 

Tutorial: `ADF fragment analysis <../../Tutorials/Analysis/FragmentAnalysis.html>`_

Examples: :ref:`analysis options <examples analysis>` 

