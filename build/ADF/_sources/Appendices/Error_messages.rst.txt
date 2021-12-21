Error messages
##############

| **ERROR: STOP GEOMETRY ITERATIONS**
| The SCF procedure did not converge, which caused the geometry optimization to be aborted. See WARNING: SCF NOT COMPLETELY CONVERGED below.

| **ERROR: imo is not occupied PT1W**
| **ERROR: imo is occupied PT1W**
| The electronic structure is not auf-bau, that is the LUMO is lower in energy than the HOMO. Disable the KeepOrbitals option by setting it to a large number and try different SCF version until you get the SCF properly converged. See the SCF Troubleshooting section for details.

| **ERROR: More cycles needed. Geometry NOT CONVERGED**
| **ERROR: GEOMETRY DID NOT CONVERGE**
| **ERROR: GEOMETRY NOT CONVERGED**
| **ERROR: TRANSIT FAILED**
| The geometry optimization did not converge in the allowed number of steps. See the Geometry Optimization Troubleshooting section for recommendations on how to proceed. 

| **ERROR: TAPE12 NOT SUPPLIED with TAPE10**
| **ERROR: Relativistic option is used but no file with core potentials was found**
| Before running a relativistic calculation you need to run the dirac program to create a TAPE12 file. This can be done automatically by adding a Basis block to the input and executing ADF as $AMSBIN/adf instead of adf.exe.

| **ERROR: calculating FDE interactions for the same fragment**
| It's a program bug. Send your input file to SCM

| **ERROR: Abort because one processor has no integration points**
| Repeat the calculation with fewer processors in the MPI job.

| **ERROR: Davidson method not converged**
| The Davidson method did not converge that is used in the calculation of excitation energies. Increase the number of ITERATIONS in the EXCITATIONS block key, or use a larger TOLERANCE.

| **ERROR: EMPTY FIELD FOUND AT END OF ...**
| **ERROR: Cannot read ... even as a string**
| Check the QMMM block in the input. Every simple key in the block (as opposed to a block key) must be followed by a value. See the QMMM Manual for the correct syntax.

| **ERROR: LenRecUnits: reclen units not determined**
| This error is most likely caused by compiler problems or by incorrect compilation flags. See https://www.scm.com/support/downloads/platform-specific-information/ for supported compiler versions and contact SCM for an advice on compilation flags. Do not forget to include the $AMSHOME/buildinfo file in your request.


Warnings
########

| **WARNING: (slightly) inaccurate ETA integral(s)**
| **WARNING: SUSPICIOUS ETA INTEGRALS**
| Eta's are symmetry adapted STO's. This error is usually caused by numerical stability problems in the symmetric matrix eigensolver. On the x86(-64) platforms you can try using a different version of the Intel MKL library (newer is not always better). 

| **WARNING: 1-character identifier(s) in DEFINE**
| The Define input block does not allow single-character identifiers.

| **WARNING: activating keyword SDFTENERGY for the calculation of subsystem DFT energy.**
| For more than two frozen subsystems the sDFT energy needs the corresponding logical switch, which is normally activated via the SDFTENERGY key in the FDE input block.

| **WARNING: AMAT not far from singularity**
| **WARNING: Bmatrix not far from singular**
| Amat and Bmatrix are used in COSMO solvation model. This warning could be printed when the distance between two COSMO surface points is shorter than 0.01 Bohr. You may want to try different COSMO accuracy parameters.

| **WARNING: Atom ( ... ) exceeded the max allowed bonds in DimQMHybridization**
| The number of bonds per atom is exceeded in DimQM. Check your input geometry for correctness (coordinate units, etc.). The bond limit per atom type is currently hardcoded in the program and cannot be increased with recompiling the program.

| **WARNING: inaccurate integration of Core Density**
| **WARNING: BAD CORE INTEGRAL ...**
| The core density must integrate to number of core electrons very accurately. If this is not the case then something is wrong either with the integration grid, with the input geometry or with the core orbitals. In any case, check your input geometry (Angstrom vs. Bohr vs. the Units input block, check bond lengths). Try using a smaller core and/or better grid.

| **WARNING: BAD FIT**
| **WARNING: CANNOT NORMALIZE THE FIT**
| **WARNING: LOSS OF CHARGE**
| These warnings are printed when the accuracy of the STO fit is not high enough. This might, for example, happen for negatively charged molecules for which the electron density cannot be adequately represented by the fit functions. This can be solved by using a larger fit type (e.g. FitType QZ4P in the Basis input block) or using the AddDiffuseFit keyword, or by using the ZlmFit instead of STOfit.

| **WARNING: The use of the SOLVATION option with non-basic fragments is not supported**
| **WARNING: Bond energies are incorrect**
| Do not use the energy decomposition analysis if the fragments are calculated with COSMO solvation.

| **WARNING: C(lin) or D(lin) not supported in Freq runs**
| When performing numerical frequency calculation for a linear molecule you should not set the symmetry explicitly to C(lin) or D(lin). Use something like C(8v) or D(8h) instead.

| **WARNING: CD spectrum for triplex excit. NOT SUPPORTED**
| **WARNING: CD spectrum for triplet excitations is NOT SUPPORTED**
| A CD spectrum calculation has been requested for triplet-only excitations, which is not supported by the program. The excitation rotary strengths will not be calculated.

| **WARNING: In ReadEpsilons: HOMO energy is positive**
| **WARNING: Check if basis or fit sets are dependent**
| The HOMO energy is positive where it should usually be negative. The positive HOMO energy means the solution is not stable and the following TDDFT calculation may produce incorrect results.

| **WARNING: Combination of unrestricted and MODEL potential not extensively tested**
| Using the model XC functionals for spin-unrestricted calculations is not officially supported. Read the literature on the functional used to make sure you do not obtain nonsense results.

| **WARNING: Virtuals almost lin. dependent**
| **WARNING: Consider using keyword DEPENDENCY**
| This warning is printed is when the smallest eigenvalue of the virtual SFO overlap matrix is smaller than 1e-5. You may want to add a Dependency keyword to your input.

| **WARNING: convMCD very small. Achieving convergence is unlikely**
| This warning is printed when the MCD convergence criterion is smaller than 1e-4. You may want to set the CONVMCD parameter in the MCD input block to a larger value if the CG solver does not converge.

| **WARNING: Core orb. en. with MODEL xc pot not implemented**
| Calculation of the core orbital energies in combination with model XC potentials (e.g. LB94) is not implemented.

| **WARNING: Could not find vecdimension excitations on SUBTAPE**
| **WARNING: Trying to find vecdimension in ResponsePmats section ...**
| When performing a Subsystem DFT excitations calculation the excitations must be calculated for each sub-system (fragment).

| **WARNING: Density fitting may not be accurate enough!**
| **WARNING: H12 and Electronic Coupling possibly INACCURATE**
| **WARNING: Diagonal energies and overlap(s) should be accurate**
| These messages are printed together and already contain a hint. To avoid the problem you may want to increase the quality of the fit using one or more of the following options: FitType QZ4P, AddDiffuseFit, NumericalQuality {Good|VeryGood|Excellent}.

| **WARNING: diagonalization error in dvdrvrhf. Results will be incomplete.**
| **WARNING: diagonalization error in dvdrvrhfso. Results will be incomplete.**
| The LAPACK subroutine dsygv (dzhegv in case of dvdrvrhfso) returned a non-zero status for the (A-B)(A+B) matrix. Analysis of the obtained solution will not be done.

| **WARNING: dihedral jumps 180 degrees**
| This warning is printed by the old optimizer branch. Check the optimization results and swtich to the new branch if you encounter any problems.

| **WARNING: DIM dipoles not converged upon SCF convergence**
| Use more tight SCF convergence criteria.

| **WARNING: No default parameters for classical Hirshfeld partitioning**
| **WARNING: Dispersion added with factor 1.0**
| You may want to set the steepness factor ATT0 and the scaling factor BTT0 for the SCBR empirical dispersion.

| **WARNING: doing final FDE cycle - FDE NOT converged**
| The FDE freeze-and-thaw procedure has not converged. You may want to increase the number of the FDE freeze-and-thaw cycles.

| **WARNING: DPERTURB calculation, no CI-type couplings calculated**
| Since the CI-coupling does not make much sense in combination with DPERTURB, the former is disabled.

| **WARNING: ERROR OPENING ONE OF THE NBO DATA FILES. SEE OUTPUT**
| Check the output to see which NBO file is missing and look for clues in the NBO output preceding the calculation.

| **WARNING: Eucledian distance between NEB images is too short. NEB may have problems**
| The total Eucledian distance between two NEB images should be large compared to the Cartesian optimization step size. Otherwise the NEB optimization may result in a zig-zag path and may eventually fail. One way to increase the distance is by reducing the number of images.

| **WARNING: Extra DFT term related to g_xc suspiciously large**
| This warning is printed when the abs(beta(diff)) value is larger than 1e-3 and is larger than abs(beta(total)) in a hyperpolarizability calculation. This may be an indication of a numerical instability.

| **WARNING: FDE in combination with ZlmFit not thoroughly tested. Consider using STOFIT**
| [[[Mirko???]]]

| **WARNING: FILE POSSIBLY TOO BIG IN AORUN**
| This warning is printed when the AORUN input keyword is specified in certain types of TDDFT calculations (e.g. polarizability). In such a case the writing of the orbital values on the grid is disabled because otherwise it would result in a huge TAPE10 file. Note: the AORUN keyword serves no other purpose but to disable writing of the orbitals to TAPE10, so it should be used with care.

| **WARNING: Geometry optimization did not converge - frequencies are not calculated**
| This warning is printed when ADF is instructed to compute the vibrational spectrum of a molecule after geometry optimization but the optimization did not converge. In this case the frequencies are not computed.

| **WARNING: GRADIENT ILL-DEFINED FOR BOND ANGLE 180 OR 0**
| This warning is generated by the old geometry optimization branch when a valence angle gets close to 0 or 180 degrees. Such angles cannot be treated properly by the optimizer so one should avoid them, for example by adding dummy atoms.

| **WARNING: Hessian is incomplete**
| This warning just informs the user that only a fraction of the Hessian matrix has been done, as specified by the NUC keyword of the AnalyticalFreq input block. The missing matrix elements are calculated from an empirical MM forcefield and the combined Hessian matrix is analyzed.

| **WARNING: inaccurate elimination of XX motions, recover**
| This warning is generated by the old geometry optimization branch. Add PRINT FREEMV to your input to get more information.

| **WARNING: Inconsistent relativistic options used**
| This warning is printed when inconsistent relativistic options are used for the fragments and the final calculation and the RELOPTINCONS keyword is used to prevent ADF from stopping the calculation. If you add RELOPTINCONS then you probably know what you're doing.

| **WARNING: Infrared Intensities are wrong**
| **WARNING: Infrared Intensities wrong**
| These warnings are issued when the computed dipole moment derivative is larger than 0.1 a.u. for a normal modes for which it must be zero by symmetry.

| **WARNING: Inter-node communication is slow! You may want to run on fewer nodes (or even one).**
| **WARNING: Intra-node communication is VERY slow! Check CPU affinity, hyperthreading and over-subscription**
| The program tests the latency of the MPI communication at the beginning of each parallel calculation. The overall (i.e. the whole MPI "world" including all processes from all nodes) and the intra-node (i.e. including only the processes within one node) latency are measured separately. The first warning is printed if the overall latency is higher than 1 ms. This usually occurs when running on multiple nodes with a slow interconnect (e.g. 1 Gbps Ethernet), or when running on too many nodes. In this case it is recommended to run on fewer nodes. It is **not** recommended to run multi-node jobs at all if the cluster does not have a fast interconnect. The second warning is printed when the intra-node latency is higher than 1 ms, which should **never** happen. If the intra-node communication is slow the user is advised to stop running further MPI calculations until the issue is resolved. Possible reasons for this are: incorrect CPU affinity settings enforced by the batch scheduler (e.g. more than one process is bound to the same core), host is oversubscribed (i.e. other jobs are running on the same machines and ADF has to compete with them for resources). When two or more MPI jobs have to compete for the same resources both jobs will a low performance because the MPI synchronization calls also consume CPU cycles.

| **WARNING: INVALID SPRING PARAMETER. DEFAULTS ARE ENFORCED.**
| The valid values for the first NEBSPRING parameter are 1 through 6. If a value outside this range is specified it is set to 1 and this warning is printed.

| **WARNING: IRC START REQUEST IMPOSSIBLE: ADJUSTED**
| This warning is printed when the IRC eigevector index specified by the IRC HESS parameter is larger than the number of free coordinates.

| **WARNING: KeepOrbitals on**
| This warning is printed when the MO populations become non-aufbau due to the KeepOrbitals feature. The KeepOrbitals usually kicks in after N/2 SCF iterations, where N is the max number of SCF iterations allowed. See the Occupations keyword for details.

| **WARNING: LB94 XC FUNCTIONAL USED FOR ENERGY GRADIENTS**
| The LB94 XC functional is supposed to be used to calculate spectroscopic properties such as optical excitation spectra and is not intended for the bonding energy (and gradients thereof) calculations.

| **WARNING: LMO beta analysis has nonzero B-field frequency. Check output.**
| This warning is printed when the magnetic perturbation field in the dynamic beta tensor (optical rotation) calculation has a finite frequency. Use the DEBUG keyword of the LOCORB input block to get more information.

| **WARNING: localized MOs: unknown symmetry key ...**
| This warning is printed when there is an unrecognized keyword is found in the LOCORB input block. Check that your input conforms the documentation of the LOCORB input block.

| **WARNING: Low value for "numvec" detected in AllocDavidson**
| **WARNING: Using numvec = [number of excitations] + 5 instead**
| **WARNING: Specify larger value for VECTORS in EXCITATION input block**
| These warnings are printed together and are self-explanatory. 

| **WARNING: GIAOS ARE NOT IMPLEMENTED WITH LIFETIME. SWITCHING OFF GIAOS**
| **WARNING: MAGOPTROT AND QUADRUPOLE OPTIONS ARE MUTUALLY EXCLUSIVE. SWITCHING OFF QUADRUPOLE**
| **WARNING: MAGPERT AND QUADRUPOLE OPTIONS ARE MUTUALLY EXCLUSIVE. SWITCHING OFF QUADRUPOLE**
| **WARNING: MAGPERT AND VROA OPTIONS ARE MUTUALLY EXCLUSIVE. SWITCHING OFF MAGPERT**
| **WARNING: OPTICALROT AND VROA OPTIONS ARE MUTUALLY EXCLUSIVE. SWITCHING OFF OPTICALROT**
| **WARNING: OPTROT AND GIAO AND NBO OPTIONS WITHOUT MAGPERT ARE NOT IMPLEMENTED. SWITCHING OFF NBO**
| **WARNING: OPTROT AND QUADPERT OPTIONS ARE MUTUALLY EXCLUSIVE. SWITCHING OFF QUADPERT**
| **WARNING: VROA OPTION MUST BE USED WITH QUADRUPOLE. SWITCHING ON QUADRUPOLE**
| **WARNING: VELOCITYORD DOES NOT WORK WITH GIAO. SWITCHING OFF GIAO**
| **WARNING: ZLMFIT AND FITAODERIV ARE NOT IMPLEMENTED. SWITCHING OFF FITAODERIV**
| These warnings are results of the AOResponse internal checks.

| **WARNING: max no. of iterations reached**
| This warning is printed when the CPKS procedure did not converge in the given number of steps. This may indicate a numerical stability issue or some other problem. In any case, you should check if the SCF has converged, if the electronic configuration is correct. Increasing the numerical accuracy might also help. Finally, you can try increasing the number of CPKS cycles for the feature in question (TD-DFT, analytical frequencies, etc.).

| **WARNING: maxBlockSize does not divide (maxBasisSize - minRestartSize). Suboptimal performance expected!**
| This warning is printed by the Davidson method using the PRIMME library. The fact that (maxBasisSize - minRestartSize) is not divisible by maxBlockSize does not affect the results so there is no reason to worry. [[[Robert is there any way to influence this?]]]

| **WARNING: MIXED OCCUPATIONS in locmo (localized MO)**
| This warning is printed when occupation numbers of the localized MOs after 2x2 rotations do not match the original ones, which essentially means that the occupied and virtual orbitals have been mixed together.

| **WARNING: mo levels nearly degenerate**
| This warning is usually issued by the CPKS driver routine when the energy difference between an occupied and a virtual orbital is less than 1e-3 a.u.. This usually means that the HOMO-LUMO gap is very small which may lead to problems in the CPKS procedure.

| **WARNING: MODTRC refers to non-existing free variable**
| **WARNING: ... selecting the first mode instead**
| This warning is printed by the old optimization branch in response to an invalid setting for the transition state search vector. In this case the TS procedure will use the eigenvector corresponding to the lowest eigenvalue of the Hessian matrix.

| **WARNING: More iterations needed. MODERATELY CONVERGED**
| **WARNING: More iterations needed. NOT CONVERGED**
| **WARNING: SCF did not converge - frequencies are not calculated**
| **WARNING: SCF NOT COMPLETELY CONVERGED**
| One of these warnings is issued when the SCF procedure did not (completely) converge. See the SCF Troubleshooting section for recommendation on how to improve the SCF convergence.

| **WARNING: More nodes than energies on the contour: this is inefficient**
| This warning is printed by the NEGF code when the number of energies on the contour is smaller than the number of MPI tasks. This means that you can probably perform the calculation in the same time using fewer processors.

| **WARNING: multiple small orbital energy differences found**
| This warning is printed when the undocumented ASYMPCOR keyword is specified and more than one occupied-virtual orbital pair is found for which the energy difference is less than 1e-3 a.u..

| **WARNING: Negative root found. AllocDavidson**
| **WARNING: Negative root found. AllocDavidsonso**
| These warnings are issued when the Davidson procedure finds a negative eigenvalue. This usually indicates a triplet instability.

| **WARNING: negative sqrt in the CI-type coupling parameters**
| **WARNING: the results might be not trustworthy!!!!!**
| This warning is printed by the subsystem TDDFT module when checking requirements for the CI coupling calculation. The latter will not be done if any element of the CI_omega matrix is imaginary. 

| **WARNING: no convergence in svdcmp**
| This is a generic warning from a singular value decomposition routine. When this occurs the SVD procedure will be aborted, which may lead to incorrect results in the module that called the routine.

| **WARNING: No DIM points found for projection matrix.**
| This warning is printed when projecting rigid rotations/translations from the DIM/QM energy gradients in the case there are no DIM points found within the cutoff radius specified by the PROJECTIONMATRIXPOINTS CUTOFF keyword.

| **WARNING: no optimization done in DVDSON: using guess vector results**
| This warning is printed to remind the user that he/she has specified SFGUESS or TRUSTSFGUESS in the input.

| **WARNING: root must be bracketed in rtsafe**
| The rtsafe function finds a root of the given callback-function in the given interval. The requirement is that the function has the opposite signs at the ends of the interval. This warning is printed when the requirement is not fulfilled.

| **WARNING: rtsafe exceeding maximum iterations**
| This warning is printed when the rtsafe function fails to find a root within the allowed number of iterations, currently 100.

| **WARNING: Non Aufbau energies used**
| This warning is printed by the Response code (excitations, polarizabilities, etc.) when the HOMO lies higher than LUMO in energy or when these are degenerate.

| **WARNING: Non-standard use of LAP functional**
| **WARNING: Non-standard use of LYP functional**
| The LAP and LYP functionals already contain a term for correlation at the LDA level. This warning is printed when an LDA functional is specified in addition to LAP or LYP.

| **WARNING: NONRELATIVISTIC RUN WITH RELATIVISTIC COREPOTENTIALS**
| **WARNING: RELATIVISTIC RUN WITHOUT RELATIVISTIC COREPOTENTIALS**
| This warning is printed when the CorePotentials keyword is used (or not used) inconsistently with the Relativistic option. Before running a relativistic calculation you need to run the dirac program to create a TAPE12 file, which then needs to be specified in the CorePotentials keyword. This can be done automatically by adding a Basis block to the input and executing ADF as $AMSBIN/adf instead of adf.exe.

| **WARNING: not all AIM bond paths converged**
| This warning is printed by the AIM bond path search module when some of the paths failed to converge to an attractor (a nucleus).

| **WARNING: not all scratch files were closed**
| This warning probably indicates a programmer error. Send the output to support@scm.com.

| **WARNING: not enough initial estimates**
| **WARNING: Too many initial estimates.?**
| One of these warnings is issued when the number of initial vectors in the Davidson procedure is either too high or too low.

| **WARNING: Number of states in energy window changed**
| This warning is printed when the number of molecular orbitals in the energy window given with the ELTHRES/EUTHRES sub-keys of the VIBRON input block changes during calculation.

| **WARNING: occupations may be NOT AUFBAU**
| This warning is printed during a single-point calculation or the last iteration of a geometry optimization if the HOMO has a higher energy than the LUMO. For fractionally occupied orbitals, the HOMO is the highest MO that is populated by at least 1e-6 electrons and the LUMO is the lowest MO that misses at least 1e-6 electron to be fully occupied. 

| **WARNING: omega and d(omega) incompatible in Verdet run**
| This warning is printed during calculation of the Verdet's constant when the value of the frequency :math:`\omega` is lower than the half-width of the interval used for numerical differentiation :math:`\Delta \omega`.

| **WARNING: Out of parameterized Coulomb radii limits**
| The Coulomb radius parameters used to determine the COSMO sphere radii are currently available for elements up to 105. For heavier elements this warning is printed and the calculation stops.

| **WARNING: partially occupied orbitals**
| This warning is printed at the end of the SCF process if it results in partially occupied orbitals. The user should examine the resulting electronic structure carefully to see if this is the result they expected. One way to avoid fractional occupations is to repeat the calculation as spin-unrestricted with a non-zero total spin. 

| **WARNING: Patchkovskii routines for PBE used. Check output**
| This warning is printed when USESPCODE is specified in the input together with the PBE functional. The bonding energy and other fragment analysis data may be incorrect.

| **WARNING: potential problem with dependency in AOResponse. Check output**
| **WARNING: potential problem with dependency in LOCMO. Check output**
| When using the Dependency keyword, the linearly-dependent orbitals are not removed completely but are effectively excluded from variation by setting the corresponding diagonal matrix element to a large positive value. One of these warnings is issued when the any of the molecular orbitals included in the variation have the energy close to that large value, which probably means there is some bug in the SCF bookkeeping.

| **WARNING: Pressure must be positive, adjusted**
| This warning is printed when the pressure specified in the Thermo keyword is smaller than 1e-4 atmosphere.

| **WARNING: PRIMITIVE FIT COEFFICIENTS A BIT LARGE**
| **WARNING: PRIMITIVE FIT COEFFICIENTS LARGE**
| **WARNING: PRIMITIVE FIT COEFFICIENTS TOO LARGE**
| One or more of these warnings are printed when the number of electrons due to a single STO fit-function exceeds certain limits (20, 200, and 2000 times the largest number of valence electrons on a single atom in the molecule, respectively). This may indicate a linear dependence (over-fitting) problem in the fit or the basis set.

| **WARNING: problem with NEB optimisation. Re-initializing Hessian**
| This warning is printed during an NEB calculation if the Eucledian angle between three images becomes less than 30 degrees. This may indicate that there are too many NEB images for such a short reaction path.

| **WARNING: ReadExSym: found large energy differences**
| This warning is printed in a Vibron calculation when the excitation energy difference between two geometries is larger than 0.2 eV. You should check the results carefully.

| **WARNING: Restricted Open-Shell calculation, Unrestricted setup may be needed**
| This warning is printed when a molecule with an odd number of electrons (a radical) is calculated spin-restricted. This often indicates an error in the input (either wrong geometry or a missing Charge keyword). This warning may safely be ignored if the result of this calculation is to be used as a fragment.

| **WARNING: SchmidtOrth keeps finding noise**
| This warning is printed by the Schmidt orthogonalization procedure when it fails to orthogonalize the input vector to the reference set within 4 attempts. Two normalized vectors are considered orthogonal when their dot product is smaller than 1e-8 in the absolute value. 

| **WARNING: sDFT energies should be used together with the FULLGRID option! Results might not be reliable!**
| Enable the FULLGRID option.

| **WARNING: SLOW SCF**
| **WARNING: ... apply ElectronSmearing**
| In case of really problematic SCF a finite electron temperature (smearing of electrons around the Fermi level) is applied automatically if the user a) has not specified smearing via input and b) has not defined the occupation numbers explicitly. Furthermore, smearing is not automatically turned on in single-point calculations and in the final geometry. That is, it is only allowed during geometry optimization in the intermediate geometries. To disable automatic smearing specify Occupations Smearq=0 in the input.

| **WARNING: small delta epsilon found**
| This warning is printed when the energy difference in an occupied-virtual MO pair is smaller than 0.001 a.u., which means the HOMO and LUMO are nearly degenerate.

| **WARNING: SOLVATION block: DISC is not compatible with C-Mat POT**
| This warning is printed when the DISC option in the Solvation input block is set for the C-Matrix POT (which is the default), where it does not make sense. The user should check their input and either remove the DISC option or set C-Matrix to EXACT or FIT.

| **WARNING: SOMCD indicated but closed-shell calculation**
| The SOMCD feature (used to calculate the C terms of the magnetic circular dichroism spectra) is available only in spin-unrestricted calculation. If SOMCD is specified in a spin-restricted calculation then it is ignored and this warning is printed.

| **WARNING: SSB-D XC FUNCTIONAL USED FOR ENERGY GRADIENTS**
| The use of "GGA SSB-D" in a geometry optimization may lead to numerical issues for some systems. Check carefully that the energy goes down smoothly and continuously. Also compare with a calculation performed with the "METAGGA SSB-D" specified in the XC input block.

| **WARNING: Strange column number EXCITATIONS**
| The second (undocumented) argument of the irrep sub-keys of the Davidson and Exact sub-blocks can optionally specify that the 2nd or 3rd projection of a multi-dimensional irrep should be used to calculate intensities. This warning is printed when the number specified is larger that the dimensionality of the irrep.

| **WARNING: Suspicious delocalized coordinates. Change GEigenvalueThreshold or optimize in Cartesian coords**
| This warning is printed when the number of generated delocalized coordinates is not equal to 3N-6 for a system of 5 atoms and more. This may indicate some problems in generation of internal coordinates for the input geometry, for example because of isolated molecules (which should normally not be a problem). This warning may also be caused by the presence of a block constraint, in which case it may be safely ignored. Otherwise, one should check the number of the generated delocalized coordinates in the output file. If it is larger than 3N-6 then it is advised to look at the "G-matrix eigenvalues" table in the output and set the GEigenvalueThreshold parameter in the Geometry block to an average of the eigenvalues number 3N-6 and 3N-5.

| **WARNING: Symmetry is not yet supported in VCD**
| The vibrational circular dichroism (VCD) intensities are not calculated if the symmetry used in the calculation is other than C:sub:`1` (i.e. NOSYM)

| **WARNING: TDA in FDEc also requires TDA excitations as input**
| Use TDA consistently in coupled frozen density embedding (FDEc).

| **WARNING: Temperature must be positive, adjusted**
| The temperature value specified in the Thermo keyword must be larger than 0.1 K.

| **WARNING: The full TDDFT kernel icw symmetry may give incorrect results.**
| **WARNING: Results can be checked with symmetry NOSYM**
| As this warning already suggest, you can check the results with SYMMETRY NOSYM.

| **WARNING: thin plane error. HULL33**
| **WARNING: thin planes inconsist 1. HULL33**
| These warnings can appear when the Te Velde integration grid is used. Use the Becke grid in this case.

| **WARNING: Unknown GGA functional for UFF dispersion.'**
| The UFF dispersion parameters depend on the XC functional used. Currently the parameters are defined for the PBE, B3LYP, PW91 and B3PW91 functionals. For any other functional the PBE parameters are used and this warning is printed.

| **WARNING: Unknown GGA functional for MBD dispersion.'**
| The MBD dispersion parameters depend on the XC functional used. Currently the parameters are defined for the PBE, PBE0, HSE03 and HSE06 functionals. For any other functional no short-range damping is applied and this warning is printed.

| **WARNING: Unknown GGA used. Dispersion added with factor 1.0**
| The Grimme dispersion corrections are defined per XC functional. For any unknown functional the dispersion is, by default, added with a factor 1.0, which can be changed from input.

| **WARNING: Unknown global optimization type requested. Using Quasi-Newton**
| **WARNING: Unknown NEB optimization type specified. Using default**
| **WARNING: Unknown optimization type requested. Using Quasi-Newton**
| One of these warnings is printed when the NEBOPT sub-key of the Geometry block contains an invalid argument.

| **WARNING: Unknown XC functional for DFT-D3**
| This warning is printed when an unknown XC functional is specified together with "Dispersion Grimme3" keyword in the XC input block. In such a case the PBE parameters are used for the dispersion correction.

| **WARNING: Untested MBD dispersion parameters are used. Check results.**
| **WARNING: Untested dispersion parameters are used. Check results.**
| This warning is printed when the system under study contains atoms with an element index greater than the maximum defined for the given correction. Currently, the limits are set as follows: 54 for Grimme, 86 for MBD, 94 for Grimme3, 102 for sCBR, and 103 for the UFF dispersion type.

| **WARNING: Unrecognized key for Irrep**
| This warning is printed when an unrecognized irreducible representation name is given in the Davidson or Exact sub-blocks of the Excitations block.

| **WARNING: use of multiple fragments not yet allowed !!!**
| **WARNING: Use results from parallel runs with caution!**
| These self-explanatory informative warnings are printed by the (relatively new) SubsystemResponse module. 

| **WARNING: USING >ADIABS< scheme in vibron.**
| **WARNING: DO YOU REALLY KNOW WHAT YOU ARE DOING?**
| The ADIABS scheme in the Vibron module can only be used for totally symmetric modes. Add ONLYSYM to the Vibron block key.

| **WARNING: using LDA-only response. Please check your output**
| This warning is printed by the AOResponse code in cases when the use of the GGA is disabled automatically, usually in open-shell calculations.

| **WARNING: VERY HIGH VALUE FOR FRANGE IN RANG2**
| **WARNING: VERY HIGH VALUE FOR QPNEAR IN RANGQP**
| This warning is printed by the grid generation routine when a basis or an STO fit function has a very long range (>10,000 a.u.). This may occur for an extremely diffuse function when a very high integration accuracy is requested.

| **WARNING: VERY SMALL A(0) IN LOCORB1. Check output!**
| This warning is printed by the routines performing the Pipek-Mezey (PM) and Boys localization on first-order perturbed molecular orbitals when the absolute value of the A(0) denominator becomes smaller than 1e-10.

| **WARNING: VROA OPTION MUST BE USED WITH QUADRUPOLE**
| The AOResponse Quadrupole options is switched on and this warning is printed when the vibrational Raman optical activity (VROA) is to be calculated.

| **WARNING: WRONG COORDINATES**
| This warning is printed by QUILD in the same situations where ADF exits with the same "WRONG COORDINATES" message: the input geometry does not satisfy the point group specified by the Symmetry keyword. This usually happens when the molecule's orientation does not match the symmetry operations. Note that when the point group is set from input, the program does not re-orient the input geometry to match the symmetry. 

| **WARNING: wrong nr of functions deleted. ORTNRM**
| Internal ADF error message. Related to STO fit. Send your input file to SCM. Alternative is to use ZlmFit.

| **WARNING: zero number of filtered transitions found, try larger demax**
| This warning is printed by the approximate TD-DFT module (TD-DFTB, sTDDFT, sTDA, KSSPECTRUM) when there are no transitions found for the given energy range. This should not happen if there is at least one occupied and one virtual orbital present because in ADF the range is by default very large (~1e308 a.u.)

