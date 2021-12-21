.. _DIRAC: 
.. index:: relativistic core potentials 

Dirac program: relativistic core potentials
===========================================

In all relativistic calculations - scalar as well as spin-orbit - the relativistic atomic core densities and the relativistic atomic potentials *must* be made available to ADF on a file specified with the key COREPOTENTIALS. This is necessary only in the 'create' run of the atoms. In the molecular calculation this key is not required anymore. If supplied then the file must contain data for *all* atom types in the molecule, even for those atoms where relativistic aspects are expected to be negligible or that may not have a frozen core at all (such as Hydrogen). Excepted are any Ghost atoms (for instance for a BSSE calculation): these can not have any core potentials. This is tested by the program, internally, by looking at the nuclear charge and at the number of electrons belonging to an atom: if both numbers are zero, no (relativistic or other) core potential is allowed. Also the potential used in the ZORA kinetic energy operator in the MAPA (the Minumium of neutral Atomical potential Approximation) method should be present on this file (which will be the case if the program DIRAC is used to generate this file). 

Relativistic potentials can and should be generated with the auxiliary program dirac, see the next section, and the examples (in particular :ref:`example green_Au`). 

The recommended way to generate atomic fragments and relativistic potentials is by using the :ref:`BASIS<keyscheme BASIS>`  keyword.


The auxiliary program DIRAC, which is installed in the Amsterdam Modeling Suite, serves to compute relativistic frozen core potentials (and densities), necessary to apply the (scalar) relativistic option in ADF. ``$AMSHOME/atomicdata`` has a subdirectory ``Dirac``, which contains input files for DIRAC for all atoms of the periodic table of elements. The *names* of the input files indicate the frozen core level: *Ag.3d* for instance is the input file for a calculation on a Silver atom with a frozen core up to and including the 3d shell (i.e.: 1s, 2s, 2p, 3s, 3p, and 3d). The frozen core level used in the DIRAC calculation defines the core data computed and should therefore match the frozen core level in the ADF Create run for the atom that it will be used for. 

A DIRAC run with the inputs provided in the ``$AMSHOME/atomicdata/Dirac/`` involves a fully relativistic calculation on the atom (spin-orbit coupling, double group symmetries). It generates a file TAPE12 with the corresponding core potential and density (a table of values for a sequence of radial distance values). Other files produced by DIRAC should be removed after the DIRAC run; they are needed for other applications of the program but play no role here. 

If you run DIRAC while a file TAPE12 already exists the computed core data will be written at the end of it, after the existing data. The program will assume, however, that the existing data on the file are also core-data from DIRAC runs, and may abort otherwise. 

Starting from ADF2006.01 it is not necessary anymore to make one big TAPE12 which contains data for all atoms involved in the molecular calculation. Instead only in the ADF Create run for each atom one needs a TAPE12 which contains data for the atom that is created. The corresponding core data is written to the adf.rkf of this atomic fragment. In the molecular ADF run one then should not include the CorePotentials key, such that ADF will read core data on the adf.rkf's of the atomic fragments. One can still use the CorePotentials key, but then one should proceed as in previous releases. 

**Implied options**

The DIRAC calculations imply the *local* Density Functional in its simple X-alpha approximation without any gradient corrections. Not the *scalar* relativistic but the *fully* relativistic Hamiltonian is used, including spin-orbit coupling. In ADF you may use the *scalar* relativistic Hamiltonian and most users will employ a more sophisticated lda than X-alpha, such as the default vwn (Vosko, Wilk, Nusair) formulas, and may in addition routinely apply gradient corrections. The core potential may not exactly match the Fock operator applied in the molecular calculation. The effect is very small and one can neglect the discrepancy. 

**Input**

The ASCII input files for DIRAC, as available in the directory ``$AMSHOME/atomicdata/Dirac`` (point nucleus) and ``$AMSHOME/atomicdata/Dirac.gaussian`` (finite nucleus), have a structure as described below. With this information you should be able to construct alternative input files, with other frozen cores for instance. 

1. Title (60 characters at most). Plays no role 

2. Ngrid, Nshell, rmin, rmax, Z, Xion, Anuc Ngrid=number of radial grid points, in which the core potentials are computed. Nshell=number of atomic orbital shells rmin, rmax=minimum and maximum radial grid values Z=nuclear charge Xion=net charge of the 'atom' Anuc=atomic weight 

3. Pinit, Pfinal, eps, del, delrv Pinit, Pfinal= initial and final density iteration averaging factors. Each iteration cycle changes the actual averaging factor by taking the average of the previous and the final one, starting with the 'initial' one. eps=Exp(-sqrt(eps)) is set to zero, so eps determines the exponential underflow control. del=absolute convergence criterion for orbital eigenenergies. delrv=convergence criterion on the potential (multiplied by the radial distance *r*). 

4. Idirc, Nmax, Ndebu, Nprin, Ipun, Ircor, Iwcor Idirc=zero for non-relativistic, otherwise one. Nmax=maximum number of iterations allowed to reach convergence. Ndebu=non-zero for additional output (for debugging purposes mainly) Nprin=print parameter. Use 2 or larger to get the orbitals printed. Ipun=punched output is produced if Ipun is non-zero. (out-of-date) Ircor=number of core orbitals from the fully relativistic run, to be kept frozen in the subsequent (if any) first-order perturbation calculation. Iwcor=number of core orbitals used to construct the core density and core potential, that are output on TAPE12. So, here you specify the relativistic core.  

5. Xalph, Xlatt, Rnuc Xalph= Exchange parameter in the Xalpha formalism. Xlatt=Coulomb tail parameter Rnuc=size of nuclear radius, in bohr. If set to 1.0 or larger, it is recomputed as 0.0000208*Anuc**(1/3) 

6. For each orbital shell: N, L, J, E, Z, D N, L, J = The usual orbital quantum numbers. J is used only for relativistic runs. E = Initial estimate of orbital energy, in atomic units. Z = Number of electrons on the shell D = Initial estimate of the error in the orbital energy 

7. Icorp, Npcl, Demp, Peps Icorp = If 1 (one): Do a first order perturbation calculation after the fully relativistic run. This option plays no role in the current application for ADF. Npcl = Maximum number of cycles in the perturbation calculation. Demp = Damping factor in the perturbation iterations Peps = Convergence criterion in the perturbation iterations. 

