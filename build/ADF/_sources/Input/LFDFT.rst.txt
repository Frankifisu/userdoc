
.. _LFDFT:
.. index:: LFDFT
.. index:: ligand field DFT


Ligand Field and Density Functional Theory (LFDFT)
**************************************************

Introduction
============

Hans Bethe and John Hasbrouck van Vleck have introduced the Ligand Field (LF) model simultaneously in the 1930s.
This theory often plays a central role for molecules containing d- and/or f-elements with open shells.
It is a semi-empirical model with adjustable parameters.
Twenty years later Christian Klixbüll Jorgensen and Klaus Erik Schäffer proposed the Angular Overlap Model (AOM)
that is a transcription of LF theory using molecular orbitals, still using adjustable parameters.
Starting from the very beginning of the twenty first century until nowadays, a new, non-empirical, Density Functional Theory (DFT) based Ligand Field model 
[#ref1]_ [#ref2]_ was developed, called LFDFT.
LFDFT emerged through the collaboration of many European scientists during these years.

The key feature of the LFDFT approach is the explicit treatment of near degeneracy correlation using ad hoc Configuration Interaction (CI) within the active space of Kohn-Sham (KS) orbitals with dominant p-, d- or f-character.
The calculation of the CI-matrices is based on a symmetry decomposition in the full rotation group and/or on a ligand field analysis of the energies of all single determinants (micro-states) calculated according to Density Functional Theory (DFT) for frozen KS-orbitals corresponding to the averaged configuration, possibly with fractional occupations, of the p-, d- or f-orbitals.
In the literature one can find cases where this procedure yields multiplet energies with an accuracy of a few hundred wave numbers and fine structure splitting accurate to less than a tenth of this amount.
This procedure was used to calculate different molecular properties, e.g. Zero Field Splitting (ZFS) [#ref3]_, Zeeman interaction [#ref4]_, Hyper-Fine Splitting (HFS) [#ref5]_, magnetic exchange coupling [#ref5]_ [#ref6]_, and shielding constants [#ref7]_.

Strictly speaking, LF theory is nothing but the consideration of active p-, d- and/or f-electrons moving in the potential of a passive chemical environment.
A rigorous formulation of a passive chemical environment could be given using a frozen density embedding (FDE) scheme.
However, in practice, it turns out that the method described in Ref. [#ref8]_ using an effective Hamiltonian is more advantageous and yields more insights to the experimentalists. 
The LFDFT model was extended to two-open-shell systems [#ref9]_.
This has relevance for inter-shell transitions in lanthanides, important for understanding the optical and magnetic properties of rare-earth materials.
It could also be used, for example, to calculate multiplet effects in X-ray absorption spectroscopy.
Theory and applications for f → d transitions can be found in Refs. [#ref9]_ [#ref10]_ [#ref11]_.

Input description
=================

Average of Configuration run
----------------------------

From a defined atomic structure (for example, obtained from geometry optimization or crystal .cif structure file), run a DFT calculation representing the electron configuration system from which the metal ion belongs.
This DFT run is achieved by the Average of Configuration (AOC) calculation with fractional occupations of s, p, d or f orbitals, i.e. for
3d\ :sup:`7` electron configuration of Co\ :sup:`2+`, 7 electrons are evenly distributed in the molecular orbitals having dominant cobalt character.
Choosing which orbitals have to be fractionally occupied may not always be trivial, since there may be several close-lying levels with different character.
This may lead to problematic SCF convergence.
One should check that the final fractionally occupied molecular orbitals indeed have the expected metal character, since otherwise the subsequent LFDFT calculation will be meaningless.
It is required that the metal ion is placed as first atom in the coordinate system.
Besides, the calculation implies a single-point spin restricted SCF without symmetry constraint (C1 point group = SYMMETRY NOSYM).
A scalar relativistic ZORA Hamiltonian should be used.

For a Co\ :sup:`2+` d\ :sup:`7` electron configuration the input for ADF could be something like:

::

   $AMSBIN/ams << eor

   System
     Atoms
       Co 0.0 0.0 0.0
       ...
     End
   End
   
   ...

   Engine ADF
     ...
     IrrepOccupations
       A 56 1.4 1.4 1.4 1.4 1.4
     End
     relativity level=scalar
     SYMMETRY NOSYM
   EndEngine
   eor

LFDFT atomic database
---------------------

The LFDFT atomic database is *not* included in the ADF distribution.

The easiest way to install it is using the ADF-GUI and open AMSinput and go to the LFDFT section. Then it will automatically be installed via AMSpackages if needed.
You can also install it from the command line using ``$AMSBIN/amspackages install lfdft``, or with the AMSpackages gui ``$AMSBIN/amspackages gui``.

Alternatively, you can download the LFDFT atomic database LDFDT from `http://downloads.scm.com/Downloads/lfdft/LFDFT.zip <http://downloads.scm.com/Downloads/lfdft/LFDFT.zip>`__, and save the unzipped file in the a different location.
If you save this LFDFT atomic database in a different location, make sure to point the environment variable SCM_LFDFT to this directory.

Note that at present available electron configurations for the LFDFT atomic database are:

* s\ :sup:`n`, n=0,..,2
* p\ :sup:`n`, n=0,..,6
* d\ :sup:`n`, n=0,..,10
* f\ :sup:`n`, n=0,..,14
* p\ :sup:`5` d\ :sup:`n`, n=0,..,10
* f\ :sup:`n` d\ :sup:`1`, n=1,..,13
* d\ :sup:`9` f\ :sup:`n`, n=1,..,14

LFDFT run
---------

The adf.rkf (TAPE21) file of the average of configuration (AOC) run should be an input file for the program lfdft.
Results of the LFDFT calculation will be put on adf.rkf.
The input for lfdft is keyword oriented and is read from the standard input.
Spin-orbit coupling is calculated using the ZORA equation by default. In cases where this is an underestimation, the old approximate method (a simple core potential) and/or an extra multiplication factor can be included.
A finite magnetic field can be included.

.. _keyscheme lfdft:

::

   $AMSBIN/lfdft << eor
   ADFFILE adffile
   NSHELL nshell
   NLVAL1 nval1 lval1
   {NLVAL2 nval2 lval2}
   MOIND1 MO#1 MO#2 ... MO#(2*lval1+1)
   {MOIND2 MO#1 MO#2 ... MO#(2*lval2+1)}
   SOC soc1 {soc2}
   SOCTYPE
      shell1 type1
      {shell2 type2}
   End
   BField bx by bz
   DegeneracyThreshold threshold
   eor

``ADFFILE adffile``
   Path to adf.rkf (TAPE21) file from which lfdft reads data and to which lfdft writes data. Default TAPE21.

``NSHELL nshell``
   nshell is the number of shells in the electron configuration system under consideration: for Co\ :sup:`2+` in 3d\ :sup:`7` electron configuration, nshell = 1; for Fe\ :sup:`2+` in 2p\ :sup:`5` 3d\ :sup:`7`, nshell = 2. nshell should be equal to 1 or 2.

``NLVAL1 nval1 lval1``
   nval1, and lval1, are the main quantum number n and l for shell 1, in case of all-electron calculations on the metal atoms.
   For 5d this is '5 2'. For frozen core calculations the number n should be reduced with the number of core levels with angular momentum l that are in the core.
   For example for 5d, with 3d and 4d in the core, one should use '3 2'.

``NLVAL2 nval2 lval2``
   If nshell=2, nval2, and lval2, are the main quantum number n and l for shell 2.

``MOIND1 MO#1 MO#2 ... MO#(2*lval1+1)``
   MO#1, ..., are  the indices of the molecular orbitals which have the most dominant nval1 lval1 character, for example the most dominant 3d character. They should match the fractionally occupied orbitals that are used in the AOC run for shell 1.

``MOIND2 MO#1 MO#2 ... MO#(2*lval1+1)``
   If nshell=2, MO#1, ..., are  the indices of the molecular orbitals which have the most dominant nval2 lval2 character. They should match the fractionally occupied orbitals that are used in the AOC run for shell 2.

``SOC soc1 {soc2}``
   soc1 indicates if spin-orbit coupling is considered (1) or not (0) for shell 1. If nshell=2, same applies for soc2 for shell 2. soc1 and soc2 can also be real numbers, in case one wants to scale the calculated approximate spin-orbit coupling(s) by LFDFT. By default, the spin-orbit coupling is included (soc1 = 1, soc2 = 1).

::

   SOCTYPE
     shell1 type1
     {shell2 type2}
   End

   type1 and type2 can be either 'zora' or 'core' and indicate whether the spin-orbit coupling for the given shell is calculated using the corresponding term in the zora equation (type = zora) or using the old approximation with the core potential only (type = core). The default is set to zora.


``BField bx by bz``
   Include a finite magnetic field (Tesla). For MCD calculations include a magnetic field in the z-direction. For example, ``BField 0.0 0.0 1.0`` is a magnetic field of 1.0 Tesla in the z-direction. Default no magnetic field is included. The DegeneracyThreshold should be small to see the splitting of levels due to the magnetic field.
   
``DegeneracyThreshold threshold``
   Energy difference threshold (eV) to determine degenerate levels.


For example for a 3d\ :sup:`7` electron configuration the input for lfdft could be

::

   $AMSBIN/lfdft <<eor
   ADFFile ams.results/adf.rkf
   NSHELL 1
   NLVAL1 3 2
   MOIND1 29 30 31 32 33
   SOC    1
   SOCTYPE
      shell1 zora
   End
   eor

.. _LFDFT_gtensor:
.. index:: g-tensor LFDFT

EPR (ESR) g-tensor
------------------

LFDFT can be used to calculate the EPR (ESR) g-tensor, see Ref. [#ref4]_.
In the LFDFT implementation in ADF the EPR (ESR) g-tensor will be calculated only for Kramers doublet states.
Results of the calculations should normally only be used for an odd number of electrons.
Spin-orbit coupling should be included, but a finite magnetic field should not be included, and no other keywords are needed.
One should be careful when interpreting the g-tensor if 2 or more Kramer doublets are close in energy.
In that case in the effective Hamiltonian used to interpret EPR (ESR) experiments an effective spin higher than S=1/2 might be used, which is not taken into account in the calculations.

LFDFT intensities
-----------------

One can calculate excitation energies and oscillator strengths between two atomic multiplet states which come from different electron configurations of the same molecule with the module lfdft_tdm.
Note that electronic transitions between two multiplet states which come from the same electron configuration are not dipole allowed.
lfdft_tdm can calculate excitation energies and oscillator strengths (in the dipole approximation)
from the calculated ground state multiplet of one electron configuration to all multiplet states that can be made for the other electron configuration.
The calculated transition dipole moments and oscillator strengths are in arbitrary units.
They are averaged over the degeneracy of the ground state as well as over the degeneracy of the excited state multiplet.
The oscillator strength has to be multiplied with the degeneracy of the excited state multiplet.

The input for lfdft_tdm is keyword oriented and is read from the standard input.

.. _keyscheme lfdft_tdm:

::

   $AMSBIN/lfdft_tdm << eor
   STATE1 file1
   STATE2 file2
   eor

``STATE1 file1``
   Filename file1 should be a result adf.rkf of a lfdft calculation, that contains the ground state electron configuration.

``STATE1 file2``
   Filename file2 should be a result adf.rkf of a lfdft calculation, that contains the excited state electron configuration. Results of the lfdft_tdm calculation will be put on file2.

For example for Pr 4f\ :sup:`2` → Pr 4f\ :sup:`1` 5d\ :sup:`1` the input could be something like:

::

   $AMSBIN/lfdft_tdm <<eor
   STATE1 f2.results/adf.rkf
   STATE2 f1d1.results/adf.rkf
   eor

In this case lfdft_tdm will calculate the excitations from the ground state of Pr 4f\ :sup:`2` to all multiplet states that can be made with the Pr 4f\ :sup:`1` 5d\ :sup:`1` electron configuration.

.. _LFDFT_MCD:
.. index:: MCD LFDFT
.. index:: XMCD LFDFT

MCD
---

LFDFT can be used to calculate Magnetic circular dichroism (MCD) effect in X-ray absorption spectroscopy, see Ref. [#ref12]_.
By using the same methodology as for an X-ray absorption calculation, one needs 2 LFDFT calculations for two atomic multiplet states which come from different electron configurations of the same molecule.
Additionally, in both calculations the same finite magnetic field in the z-direction (for example, Bfield 0 0 1) should be included.
Next the module lfdft_tdm can be used to calculate besides the total intensity, also the polarized part that is perpendicular to the magnetic axis, the circular-left and circular-right part.


.. only:: html

  .. rubric:: References

.. [#ref1] M.\  Atanasov, C.A. Daul, C. Rauzy, *New insights into the effects of covalency on the ligand field parameters: a DFT study*, `Chemical Physics Letters 367, 737 (2003) <https://doi.org/10.1016/S0009-2614(02)01762-1>`__ 

.. [#ref2] M.\  Atanasov, C.A. Daul, C. Rauzy, *A DFT Based Ligand Field Theory*, `Structure & Bonding 106, 97 (2004) <https://doi.org/10.1007/b11308>`__ 

.. [#ref3] A.\  Borel, C.A. Daul, L. Helm, *Hybrid ligand-field theory/quantum chemical calculation of the fine structure and ZFS in lanthanide(III) complexes*, `Chemical Physics Letters 383, 584 (2004) <https://doi.org/10.1016/j.cplett.2003.11.082>`__ 

.. [#ref4] M.\  Atanasov, E.J. Baerends, P. Beattig, R. Bruyndockx, C. Daul, C. Rauzy, *The calculation of ESR parameters by density functional theory: the g- and A-tensors of Co(acacen)*, `Chemical Physics Letters 399, 433 (2004) <https://doi.org/10.1016/j.cplett.2004.10.041>`__ 

.. [#ref5] M.\  Atanasov, C.A. Daul, *A DFT based ligand field model for magnetic exchange coupling in transition metal dimmer complexes: (i) principles*, `Chemical Physics Letters 379, 209 (2003) <https://doi.org/10.1016/S0009-2614(03)01325-3>`__ 

.. [#ref6] M.\  Atanasov, C.A. Daul, *A DFT based ligand field model for magnetic exchange coupling in transition metal dimer complexes:: (ii) application to magnetic systems with more than one unpaired electron per site*, `Chemical Physics Letters 381, 584 (2003) <https://doi.org/10.1016/j.cplett.2003.10.024>`__ 

.. [#ref7] F.\  Senn, C.A. Daul, *Calculation of*   \ :sup:`59`\ Co *shielding tensor* :math:`\sigma`  *using LF-DFT*, `Journal of Molecular Structure: THEOCHEM 954, 105 (2010) <https://doi.org/10.1016/j.theochem.2010.02.027>`__

.. [#ref8] C.\  Daul, *Non-empirical Prediction of the Photophysical and Magnetic Properties of Systems with Open d- and f-Shells Based on Combined Ligand Field and Density Functional Theory (LFDFT)*, `Chimia 68 (2014) <https://doi.org/10.2533/chimia.2014.633>`__

.. [#ref9] H.\  Ramanantoanina, W. Urland, F. Cimpoesu, and C. Daul, *Ligand field density functional theory calculation of the* 4f\ :sup:`2` → 4f\ :sup:`1` 5d\ :sup:`1` *transitions in the quantum cutter* Cs\ :sub:`2`\ KYF\ :sub:`6`\ :Pr\ :sup:`3+`, `Physical Chemistry Chemical Physics 15, 13902 (2013) <https://doi.org/10.1039/C3CP51344K>`__.

.. [#ref10] H.\  Ramanantoanina, W. Urland, A. Garcia-Fuente, F. Cimpoesu, and C. Daul, *Ligand field density functional theory for the prediction of future domestic lighting*, `Physical Chemistry Chemical Physics 16, 14625 (2014) <https://doi.org/10.1039/C3CP55521F>`__.

.. [#ref11] H.\  Ramanantoanina, M. Sahnoun, A. Barbiero, M. Ferbinteanu, F. Cimpoesu, *Development and applications of the LFDFT: the non-empirical account of ligand field and the simulation of the f–d transitions by density functional theory*, `Physical Chemistry Chemical Physics 17, 18547 (2015) <https://doi.org/10.1039/C5CP02349A>`__.

.. [#ref12] H.\  Ramanantoanina, M. Studniarek, N. Daffé, J. Dreiser, *Non-empirical calculation of X-ray magnetic circular dichroism in lanthanide compounds*, `Chemical Communications 55, 2988 (2019) <https://doi.org/10.1039/C8CC09321K>`__.
