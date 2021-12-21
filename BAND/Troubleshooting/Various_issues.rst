Various issues
**************

Understanding the logfile
=========================

In practice you will look often at the logfile to see whether the calculation is going fine. Here is a logfile for a single point calculation. 

::

<Oct16-2019> <11:44:37>  AMS 2019  RunTime: Oct16-2019 11:44:37  Nodes: 1  Procs: 4
<Oct16-2019> <11:44:37>  BAND 2019  RunTime: Oct16-2019 11:44:37  Nodes: 1  Procs: 4
<Oct16-2019> <11:44:37>  All basis functions smoothly confined at radius: 10.0
<Oct16-2019> <11:44:37>  >>>> RADIAL
<Oct16-2019> <11:44:38>  >>>> POINTS
<Oct16-2019> <11:44:38>  >>>> KPNT
<Oct16-2019> <11:44:39>  >>>> CELLS
<Oct16-2019> <11:44:39>  >>>> NUMGRD
<Oct16-2019> <11:44:39>  >>>> ELSTAT
<Oct16-2019> <11:44:39>  >>>> ATMFNC
<Oct16-2019> <11:44:39>  CalcAtomicProperties
<Oct16-2019> <11:44:39>  >>>> PREPAREBAS
<Oct16-2019> <11:44:39>  ------ K ..   1
<Oct16-2019> <11:44:39>  >>>> PREPAREHAM
<Oct16-2019> <11:44:39>  ------ K ..   1
<Oct16-2019> <11:44:39>  >>>> PREPAREFIT
<Oct16-2019> <11:44:39>  calling scf
<Oct16-2019> <11:44:39>  start of SCF loop
<Oct16-2019> <11:44:39>  initial density from psi
<Oct16-2019> <11:44:40>  cyc=  0 err=0.00E+00 cpu=   0s ela=   0s
<Oct16-2019> <11:44:40>  cyc=  1 err=5.88E-01 meth=m nvec= 1 mix=0.0750 cpu=   0s ela=   0s fit=9.96E-03
<Oct16-2019> <11:44:40>  cyc=  2 err=5.35E-01 meth=d nvec= 2 mix=0.2000 cpu=   0s ela=   0s fit=6.79E-03
<Oct16-2019> <11:44:41>  cyc=  3 err=8.63E-02 meth=d nvec= 3 mix=0.2000 cpu=   0s ela=   0s fit=8.05E-03
<Oct16-2019> <11:44:41>  cyc=  4 err=2.10E-02 meth=d nvec= 3 mix=0.2200 cpu=   0s ela=   0s fit=8.19E-03
<Oct16-2019> <11:44:42>  cyc=  5 err=1.46E-02 meth=d nvec= 3 mix=0.2420 cpu=   0s ela=   0s fit=8.29E-03
<Oct16-2019> <11:44:42>  cyc=  6 err=9.90E-03 meth=d nvec= 4 mix=0.2420 cpu=   0s ela=   0s fit=8.28E-03
<Oct16-2019> <11:44:42>  HALFWAY
<Oct16-2019> <11:44:42>  cyc=  7 err=5.85E-04 meth=d nvec= 4 mix=0.2662 cpu=   0s ela=   0s fit=8.28E-03
<Oct16-2019> <11:44:43>  cyc=  8 err=3.76E-04 meth=d nvec= 5 mix=0.2662 cpu=   0s ela=   0s fit=8.29E-03
<Oct16-2019> <11:44:43>  cyc=  9 err=7.20E-05 meth=d nvec= 3 mix=0.2928 cpu=   0s ela=   0s fit=8.29E-03
<Oct16-2019> <11:44:43>  cyc= 10 err=2.80E-05 meth=d nvec= 4 mix=0.2928 cpu=   0s ela=   0s fit=8.29E-03
<Oct16-2019> <11:44:44>  cyc= 11 err=9.03E-06 meth=d nvec= 5 mix=0.2928 cpu=   0s ela=   0s fit=8.29E-03
<Oct16-2019> <11:44:44>  SCF CONVERGENCE
<Oct16-2019> <11:44:44>  cyc= 12 err=1.59E-06 meth=d nvec= 5 mix=0.3221 cpu=   0s ela=   0s fit=8.29E-03
<Oct16-2019> <11:44:44>  cyc= 13 err=1.59E-06 meth=d nvec= 1 mix=1.0000 cpu=   0s ela=   0s fit=8.29E-03
<Oct16-2019> <11:44:44>  ENERGY OF FORMATION:   -1.1620 A.U.
<Oct16-2019> <11:44:44>                        -31.6196 E.V.
<Oct16-2019> <11:44:44>                       -729.1660 KCAL/MOL
<Oct16-2019> <11:44:44>  FERMI ENERGY:          -0.2051 A.U.
<Oct16-2019> <11:44:44>                         -5.5801 E.V
<Oct16-2019> <11:44:44>  Band gap:               0.2204 A.U.
<Oct16-2019> <11:44:44>                          5.9986 E.V
<Oct16-2019> <11:44:44>  >>>> CHARGE
<Oct16-2019> <11:44:44>  >>>> HIRSH
<Oct16-2019> <11:44:44>  >>>> CM5CHARGES
<Oct16-2019> <11:44:44>  >>>> DOS
<Oct16-2019> <11:44:44>  Storing all partial DOS
<Oct16-2019> <11:44:44>  Integrate over delta E
<Oct16-2019> <11:44:44>  partial dos
<Oct16-2019> <11:44:44>  copy T(V/VOC)
<Oct16-2019> <11:44:44>  copy eigensystem
<Oct16-2019> <11:44:45>  NORMAL TERMINATION

There are three different phases. The first phase is the preparation phase. The second phase is the SCF procedure. The third part is the properties phase. Particularly important are the SCF CONVERGENCE and NORMAL TERMINATION messages. 

The preparation phase is the part up to "start of SCF loop". The first entries are usually not very costly. The section PREPAREBAS is about the overlap matrix, core orthogonalization, and the transformation to the orthogonal basis. In PREPAREHAM the fixed part of the Hamiltonian is calculated (mostly kinetic energy).

Let us take a closer look at a line during the SCF. 

::

    <Jul10-2018> <18:24:59>  cyc=  3 err=4.35E-02 meth=d nvec= 2 mix=0.2200 cpu=   1s ela=   1s fit=1.60E-02

The meaning of cyc is the iteration number, so it is the third iteration. The self consistent error (err) is 4.35E-02. The method (meth) to guess the density for the next cycle is d, meaning DIIS, being a linear combination (nvec) of two vectors. The density is biased (mix) by 0.2 towards output densities. The SCF cycle took 1 second of cpu time (per core), and needed 1 seconds of real time. Finally the error of the density fitting was 1.60E-02

.. index:: Broken Symmetry

Breaking the symmetry
=====================

In some cases you want to break the symmetry. An example of this is when you want to get the antiferromagnetic state of Fe. Another common example is when you want to apply geometry constraints on atoms. 

The easiest way to do this is of course to disable all symmetry, see :ref:`UseSymmetry key <band-key-UseSymmetry>`, but this might make your calculation more expensive than is needed. A bit more elegant way is to define separate types for the equivalent atoms. Here follows an example input for antiferromagnetic iron 

::

  ! The two iron atoms have different "types" to break the symmetry
  System
      Atoms 
        Fe.a   0.0    0.0    0.0
        Fe.b  -1.435 -1.435  1.435
      End
  End

  Lattice
     -1.435  1.435  1.435
      1.435 -1.435  1.435
      2.87   2.87  -2.87
  End

  ...
  ...

  Band Engine

    ...
    CONVERGENCE
        CRITERION 1.0e-4
        Degenerate default
        SpinFlip 2  ! Flip (startup) spin density at second atom
    END
    ...
  EndEngine


Another solution is to use the expert SYMMETRY keyword. 

Labels for the basis functions
==============================

You see the labels for the basis functions in for instance the DOS section of the output. The labels are also used in combination with options like ``Print Eigens`` and ``Print OrbPop``. 

What do the labels look like? A normal atomic basis function, i.e. a numerical orbital or a Slater type orbital, gets a label like <atom number>/<element>/<orbital type>/<quantum numbers description>/<exp in sto> 

Example with a Li and a H atom: 

::

    1/LI/NO/1s           
    1/LI/NO/2s           
    1/LI/STO/2s/1.4           
    1/LI/STO/2p_y/1.3           
    1/LI/STO/2p_z/1.3           
    1/LI/STO/2p_x/1.3           
    2/H/NO/1s           
    2/H/STO/1s/1.9           
    ...

Core states will just get simple numbers as labels: 

::

    CORE STATE 1           
    CORE STATE 2

With the ``Fragment`` key you can give meaningful names to the fragment option, see ``Fragment%Labels`` and ``DosBas``. 

Reference and Startup Atoms
===========================

The formation energy of the crystal is calculated with respect to the reference atoms. BAND gives you the formation energy with respect to the spherically symmetric spin-*restricted* LDA atoms. If you want the program to do the spin-unrestricted calculation for the atoms you can give key Unrestricted the extra option Reference. We do not recommend this as it would give you the false (except in special cases) feeling that you've applied the right atomic correction energy so as to obtain the 'true' bonding energy with respect to isolated atoms. The true atomic correction energy is the difference in energy between the used artificial object, i.e. the spherically symmetric, spin-restricted atom with possibly fractional occupation numbers, and the appropriate multiplet state. The spin-*un*\ restricted reference atom would still be spherically symmetric, with possibly fractional occupations: it would only have the probably correct (Hund's rule) net spin polarization. 

The startup density is normally the sum of the restricted atoms. In case you do an unrestricted calculation you may want to get the sum of the unrestricted atoms as startup density by giving key Unrestricted the extra option StartUp. This does not always provide a better startup density since all atoms will have their net-spins pointing up. If a frozen core is used this option can sometimes lead to a negative valence density, because the frozen core is derived from the restricted atom. The program will stop in such a case. 

No matter what reference or startup atoms you use, core orbitals and NOs originate always from the restricted free-atom calculation, because we don't want a spatial dependence of the *basis functions* on spin. 

Numerical Atoms and Basis functions
===================================

The program starts with a calculation of the free atoms, assuming spherical symmetry. The formation energy is calculated w.r.t such atoms. You have to specify the configuration (i.e. which orbitals are occupied) in the Dirac subkey of the block key AtomType, and you can for instance use the experimental configuration. Keep in mind, however, that this is not necessarily the optimal configuration for your density functional. For instance, Ni has experimentally two electrons in the 4s shell, but with LDA you will find that it is energetically more profitable to move one electron from the 4s to the 3d. The configuration of the reference atoms does not (i.e. should not) affect the final (SCF) density. 

Besides the available basis sets in $AMSHOME/atomicdata/band, you could in principle use the basis functions from the database of the molecular ADF program (see the documentation of ADF for how this database is organized). The functions you will find there are STOs, which is not optimal since BAND offers you the option to use NOs from the numerical atom. The most efficient approach is to use the NOs and remove from the ADF basis set those STOs that are already well described by the NOs. 

As an example we will construct a basis for the Ni atom with orbitals frozen up to the *2p* shell, derived from a triple-zeta ADF basis. In the Dirac subkey of the block key AtomType you specify that the NOs up to *2p* should be kept frozen and that the 3d and *4s* NOs be included in the valence basis. Copy from the ADF database all *3d*, *4s* and the polarization functions into the BasisFunctions subkey of the block key AtomType and remove the middle STOs of the *3d* and the *4s*. 

Usually it is already quite adequate for a good-quality basis to augment each NO with one STO. You could then take a double zeta ADF basis and remove one of the 3d and one of the 4s STOs. We often find that such a basis, with one STO added per NO, has a quality that is comparable to *triple* zeta STO sets. We strongly recommend that you use combined NO/STO bases. Of course, you may want to verify the quality of the basis set by calculations on a few simple systems. 

