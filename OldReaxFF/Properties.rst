
Properties and Analysis
#######################


Vibrational Frequencies
***********************

See `AMS documentation <../AMS/index.html>`__


.. _atomicstresstensor:

Per-atoms Stress Tensor
***********************

The per-atom stress tensor is calculated according to `Thompson, Plimpton, Mattson, J Chem Phys, 131, 154107 (2009) <https://doi.org/10.1063/1.3245303>`__ . 
when the lstres control parameter is set to a non-zero value. 

The calculated stress tensor is stored in the rxkf file in the "History%Atomic stress xxxx" variable, where xxxx corresponds to 
a step number, in units of MPa or MPa * A3, depending on the lstres value in the ReaxFF control file:

+ ``1 lstres`` (GUI: *Stress energy*) the stress times volume value per atom Sαβ is calculated as a sum of the per-atom virial and the kinetic energy term: Sαβ=mvαvβ + Fαrβ. 
+ ``2 lstres`` (GUI: *Stress*) the result is equal to Sαβ/V, where V is atomic volume calculated using the Voronoi partitioning scheme. 

The temporal average atomic stress values are stored in "History%Average atomic stress xxxx". 
The tensors are saved as follows: six components (xx, yy, zz, yx, zx, zy) for the 1st atom followed those for the 2nd one, and so on.

See the ReaxFF `stress strain tutorial <../Tutorials/MolecularDynamicsAndMonteCarlo/PolymersMechanicalProperties.html>`__  for an application of the per-atom stress tensor.


.. _tnemd:

NEMD Methods for Thermal Conductivity 
*************************************

There are different methods to study thermal conductivity using non-equilibrium molecular dynamics (NEMD). In ReaxFF, two methods are implemented. A common feature of these methods is that they require the system to be divided into three or more zones, each with its own thermostat and/or other properties. Both methods make use of the *tregime.in* file to define the zones and their properties. The first method maintains the temperature of the heat source and the heat sink zones at the given temperature using two different thermostats and measures the amount of heat transferred. This method is invoked by setting the *itdmet* control parameter to 2, which is the default value. The format of the *tregime.in* file for this method is as follows::

  # A hash sign starts comment
  # First equilibrate the system at 400K
  #start_step nzones zone1: start end Tset damp dT
        0       1             1  7840  400  100 0.0
  # Switch to NEMD starting from step 10000
  #start_step nzones zone1: start end Tset damp dT   | zone2: start end Tset damp  dT | zone3: start end Tset damp  dT
    10000       3             1  7520   0   0  0.0            7521 7680  500  100 0.0          7681 7840  300  100 0.0

In this example, atoms 1-7520 form the heat conduction zone, zone1. This zone is not thermostatted (the NVE ensemble is used), which is specified by a zero value for the temperature damping parameter damp. The zone2 (atoms 7521-7680) is a heat source and its temperature, 500K in this case, is maintained by the thermostat specified by the *imdmet* control parameter (1 for Berendsen and 2 for NHC). The zone3 (atoms 7681-7840) is the heat sink whose temperature is maintained at 300K. In the steady state, a temperature gradient will evolve through the conduction zone and the amount of heat transferred through it per unit of time should be equal to the amount of heat added to the heat source zone, and to the heat removed from the heat sink zone. The total heat added or removed for each zone by the corresponding thermostat is written to the fort.75 file. 

The second method (which is available in two variants) is invoked by setting *itdmet* to 8 or 9. There is no thermostat as such involved here, which means that the *imdmet* control parameter must be set to 3 (NVE ensemble). Instead of controlling the zone's kinetic energy based on the temperature, the heat source zone is added (and the heat sink is subtracted) a fixed amount of kinetic energy each step. Currently there are two variants of this method implemented: a simple heat pump (*itdmet* = 8), where atom velocities are simply scaled when adding or removing the kinetic energy, and the HEX method by Ikeshoji and Hafskjold in which the velocities are scaled in such a way as to keep the velocity of the center of mass of the zone constant. It should be noted that the HEX introduces a small energy drift. The format of the *tregime.in* file for these two method is almost the same as for the first method with some differences: the Tset and damp parameters are ignored and the dT value becomes dQ (in kcal/mol per MD step)::

  # NEMD heat flow parameters starting from the very first step. 
  # In practice this should be restarted from an equilibrated system
  # nzones conduction zone:start end          | heat source: start end      dQ  | heat sink: start end      dQ
  0   3                     1   7520 0 0 0.0                 7521 7680 0 0 0.01              7681 7840 0 0 -0.01

The zone assignment in this example is the same as in the previous one. One should be careful when choosing values for dQ because a too large positive value may lead to pyrolysis of the heat source and a too large negative value may lead to abnormal termination when all kinetic energy of the heat sink has been drained. 

For all these methods, in order to calculate the thermal conductivity value one needs to divide the heat flow rate by the temperature gradient and by the flow cross-section area: :math:`k = W/(S \cdot grad(T))`. In the first method the heat flow rate can be calculated from the thermostat energy values found in the fort.75 file (or rather their derivative w.r.t. the time). In the heat pump and the HEX methods the heat flow rate is defined by the dQ value andby the time step parameter directly: :math:`W[Watt] = 6.94122 \cdot 10^{-6} dQ / dt`, where dQ is given in kcal/mol/step and dt is the time-step in fs. See below on how to determine the temperature gradient along an axis.

.. _tprofile:

Temperature Profile along Coordinate Axis
*****************************************

The temperature profile along the simulation box axes will be calculated when ianaly=2 is set in the control file. In the tprofile.out file found in the results directory, the average temperatures along each box axis are listed in the following format::

  Temperature profiles along unit cell coordinate axes, averaged over time per axis. MD step       1000
  Cell coord|  N(sample)    T(ave)   |  N(sample)    T(ave)   |  N(sample)    T(ave)   |
            |            a           |            b           |            c           |
      0.0050     22809      326.57722     14475      237.18337     24784      260.64395
  ...

Here, "Cell coord" is the coordinate of the middle point of the corresponding length interval (the bin), N(sample) is the number of samples used in the averaging (which is done over the time and the atoms in the bin), and T(ave) is the average temperature in the bin over the time interval. The time interval and the number of bins are determined by the iout7 and tprofp control parameters, respectively. It should be noted that the binning of atoms is done in fractional coordinates, which means that the plane separating two bins, for example, along the **c** crystal axis is always parallel to the (**ab**) plane and may thus not be orthogonal to the **c** axis itself.

The profile is also saved to the KF result file. The corresponding variables in the History section are "T profile X YYYY", when "X" specifies the profile axis and is one of "a", "b", or "c" and "YYYY" is the MD step number.


.. _localt:

Local Atomic Temperature
************************

ReaxFF can calculate atomic temperatures and spatial averages thereof. Individual atomic temperatures are saved with the trajectory by default and these can be visualized by AMSmovie. However temperatures of individual atoms can vary significantly, which may result in a not so clear picture. To see trends in the spacial distribution of the temperature across the system it may be useful to display an average temperature of the atom and its neighbors instead. 
The spacial averaging is activated by specifying the following keywords in the control file::

      1 localt     Request local temperature averaging between atoms 
   10.0 localr     Set the awareness radius to 10.0 angstrom (Default 5.0)

See also: `How to visualize local atomic temperatures in the GUI <https://www.scm.com/news/visualization-local-temperatures-atomic-properties-amsmovie/>`__ . 

.. _adsorptionanalysis:

Adsorption Analysis
*******************

Analysis of the molecular composition of the system under study normally includes all atoms. In the original ReaxFF, it was already possible to ignore a certain type of atoms when performing the analysis, which may help analyze surface dissociation reactions. For example, in an Al-H2O system, one can distinguish a physisorbed water molecule from a surface-dissociated one by excluding all aluminum atoms from the molecular analysis. However, this feature cannot be used for surfaces consisting of atoms of more than one type and it will also not distinguish a surface reaction from the same reaction taking place off the surface. 

The new type of analysis is intended to fill this gap. This analysis is triggered by specifying a range of atoms as a "support" in the input geometry (in the BGF format)::

  SUPPORT startAtom endAtom


Here, startAtom and endAtom are indices of the first and the last atoms of the range constituting the support (surface+bulk) part of the model system. Multiple SUPPORT keys are allowed in the input file, in which case they will all be merged into one "support" entity. If this key is present, the molfra.out file will contain something like this (taking again the Al-H2O system as an example and treating the Al slab as a support)::

  Iteration    Freq.   Molecular formula                 Molecular mass
         0      120 x  Al                                      26.9820
         0       61 x  H2O                                     18.0150
         0       14 x  H2O(ads)                                18.0150


The "H2O(ads)" must be understood as a water molecule adsorbed on a surface via its oxygen atom. During dynamics one may also see molecules such as HH(ads)O(ads), where both H and O atoms interact with the support. In other words, the "(ads)" suffix applies to the atom preceding it and, through this atom, to the whole molecule. As usual in this kind of analysis in ReaxFF, two atoms are considered connected if the order of the bond between them is greater than the cutof3 control parameter.

.. _reactionanalysis:

On-the-fly Analysis of Reaction Events
**************************************

Built-in reaction detection and analysis in reaxff is enabled by setting the *ibocha* control parameter to a non-zero value. This method is based on keeping track of the number of bonds of atoms in the system at set intervals, which guarantees a very low overhead in almost all cases. When the number of bonds around an atom changes this atom becomes an atom of interest and the output is written to bondchange.out and possibly reactions.xyz. The molecular composition analysis is performed every iout7 steps and results are both saved as part of the trajectory and used for the analysis described here. For this reason the kf-file sampling interval parameter iout7 also defines the frequency of the on-the-fly reaction detection. 

Two ibocha values are currently supported: 1 and 2. The ibocha=1 does the same as in the original reaxff version: printing to bondchange.out a one-line message for each atom with changed number of bonds, like this::

  MD-step:     11780 Atom N        15 has lost bond(s): 3->2, moved from C5H8O12N4 to O2N

The ibocha=2 option is an extension to ibocha=1 and it tells reaxff to also dump the xyz coordinates of molecules mentioned above to the reactions.xyz file. For the example above, two molecules would be written::

  29
  Step 11780 reactant C5H8O12N4
     1  N            2.69656838          5.12589261          0.97180852
     2  O            4.15730086          4.99047544          1.27822949
     3  O            2.22159806          4.44324905          0.03576820
     4  O            1.96584976          5.93167910          1.72665822
     5  H            3.95163594          6.25753755          3.15184024
     6  H            5.44777765          6.49477803          2.46494613
     7  C            6.41416826          3.90121980          2.65835254
     8  N            8.24612020          4.30823059          1.11141846
     9  O            7.66154742          4.55735751          2.58464023
    10  O            8.79263162          5.29595371          0.49362056
    11  O            8.80963036          3.13719696          1.11070541
    12  H            6.40826369          3.18493699          3.51002413
    13  H            5.74405149          3.41353259          1.73612946
    14  C            4.42001493          3.68879837          4.30184825
    15  N            4.37449815          1.82746861          6.38489303
    16  O            5.14915771          2.89762593          5.05416466
    17  O            4.99604438          1.65830747          0.48544462
    18  O            3.20940517          1.45602335          6.22444281
    19  H            3.86848640          2.95960033          3.60488579
    20  H            3.39984332          4.11318335          4.66083432
    21  C            5.87896652          5.70360041          4.73680165
    22  N            5.55108399          7.52510417          6.10594010
    23  O            4.91172061          6.76799249          4.93853789
    24  O            4.75311340          7.58235081          0.10430559
    25  O            6.80961357          7.76560552          6.07934918
    26  H            6.91649734          6.15363498          4.61919911
    27  H            6.21346007          4.91150861          5.55644182
    28  C            4.60495584          5.65630445          2.50946344
    29  C            5.45265424          4.77567020          3.49485932
  3
  Step 11780 product O2N
    15  N            4.36602590          1.82312814          6.39657912
    17  O            4.99790591          1.64883276          0.48915935
    18  O            3.22220332          1.46348009          6.23717031


In the example above, the first molecule, C5H8O12N4 denoted as "reactant", is the molecule that contained atom N 15 at the previous sampling step. The second molecule, NO2 denoted as "product", is the molecule that contains the atom at the current step. Thus, the xyz coordinates of the "reactant" molecules is always iout7 steps behind the coordinates given for the "products". 

.. Note ::

   The choice of the iout7 sampling frequency is very important for a correct analysis. Too small iout7 value (frequent sampling) may lead to many forth-and-back "reactions" detected, which are merely stretched bonds due to some very hot vibrations. A too large iout7 value (rare sampling) meay lead to some elementary reactions being missed and merged into "collective" events. 

.. Note ::

   The low-overhead bonding analysis method used here may miss events that do not result in the change of the number of bonds on an atom. For example, concerted reaction of proton  transfer in a ring of water molecules will likely go unnoticed because the number of bonds remains the same on every atom, even though the bonds do change. 

Trajectory Analysis
*******************

.. toctree::
   :maxdepth: 2

   ChemTraYzer
   travis
