
Ensembles
#########

Currently the following ensembles are implemented in the ReaxFF program:

* NVE
* NVT with a Berendsen thermostat (see the original reaxff pdf manual for details)
* NVT with a Nose-Hoover chain (NHC) thermostat
* NPT with a Berendsen baro- and thermostat (see the original reaxff pdf manual for details)
* Anderson-Hoover (AH) or Parrinello-Rahman-Hoover (PRH) NPT with NHC thermostats

The ensemble is selected based on the imdmet value in the control file. Currently supported imdmet values are: 

* 1 - Berendsen NVT
* 2 - Nose-Hoover chains NVT
* 3 - Microcanonical ensemble (NVE)
* 4 - Berendsen NPT
* 9 - Isotropic NPT with MTTK NHCP
* 10 - Anisotropic NPT with only the length of the unit cell vectors changing and MTTK NHCP
* 11 - Anisotropic NPT with full cell fluctuations and MTTK NHCP 

The following imdmet values are also recognized by the program but the corresponding functionality has not been tested by SCM and is thus not supported (they come directly from the Adri van Duin's code): 

* 5 - NVE with a switch to NVT when the average system's temperature exceeds a certain target
* 6 - Hugoniostat
* 7 - NVE with shear force
* 8 - non-equilibrium NVE with the ab plane moving every step by a fixed amount

The selected ensemble can further be modified using other control keys: itdmet, inpt (for anisotropic NPT), mdtemp (target temperature, K), tdamp1 (T damping constant, fs), mdpres (target pressure, MPa), pdamp1 (P damping constant, fs), and some other. Furthermore, the NVT ensembles can further be modified using the so-called temperature regimes (T-regimes) specified via a tregime.in file.

Nose-Hoover chains NVT ensemble
*******************************

Both the NHC-NVT and the AH-NPT are implemented following the paper by G.J. Martyna et al. 
[G J Martyna, M E Tuckerman, D J Tobias, M L Klein, Mol. Phys. *87* (1996) 1117]. The following parameters are used: N_c=5, N_ys=5, Nchains=10.
The NHC-NVT ensemble is invoked by setting imdmet=2 in the control file. The tdamp control parameter (:math:`\tau_{t}`) is used to determine the 
first thermostat mass as :math:`Q = N_{free} k T_{set} \tau_{t}^2`. It should be noted that the :math:`\tau_{t}` in the Nose-Hoover method corresponds to the period of the characteristic oscillations of the system, which is different from the :math:`\tau` in the Berendsen thermostat where it determines the relaxation time. Relaxation of the system with a Nose-Hoover thermostat usually takes longer than with the Berendsen one with the same :math:`\tau`.

The temperature regimes and zones specified via the tregime.in file can also be used with the NHC thermostat the same way as with the Berendsen one.


AH and PRH NPT ensemble with NHC
********************************

The Anderson-Hoover NPT ensemble is invoked by setting imdmet=9 in the control file. Everyting written above about the NHC thermostat applies also to the thermostat part of the AH-NPT. The particle thermostat and the barostat are controlled by two different chains. The masses in the barostat thermostat chain are determined by the tdamp parameter as :math:`Q_{p} = k T_{set} \tau_{t}^2`. The pdamp control parameter :math:`\tau_{p}` defines the barostat mass as :math:`W = (N_{free} + 3) k T_{set} \tau_{p}^2`. Similar to the NHC thermostat, the :math:`\tau_{p}` here corresponds to the period of the characteristic pressure fluctuations of the system.

For an anisotropic (Parrinello-Rahman-Hoover) NPT dynamics one should specify imdmet=10 (fixed cell angles) or imdmet=11 (full cell fluctuations). It should be noted that the anisotropic NPT dynamics has not been well tested yet and thus it should be considered experimental. For imdmet=10 one can additionally freeze one or more axes using the inpt control parameter. The supported values are identical to those used for the Berendsen NPT: 1, 2, 3 to keep a, b, or c fixed, respectively, and 4 to keep both a and b fixed. 


Berendsen NVT with separate damping for translational, rotational, and vibrational degrees of freedom
*****************************************************************************************************

It is possible to equilibrate translational, rotational, and vibrational degrees of freedom separately from each other. This may be necessary, for example, in the case where the initial state of the system contains many quickly spinning molecules with a relatively small translational velocity. The usual equilibration of such a system would take a lot of time due to the low translational velocity of the molecules. This mode is invoked by setting imdmet=1 and itdmet=7 in the control file.
