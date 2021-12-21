.. _ReaxFF_polymers_bond_boost:

Polymer structures with the bond boost acceleration method
**********************************************************

In this tutorial we will show how the `bond boost acceleration method <../../AMS/Tasks/Molecular_Dynamics.html#bond-boost-method>`__ can be used to drive the non-catalyzed epoxide - amine polymerization reaction with the aim of generating highly crosslinked epoxy polymer structures:

.. _epoxy_crosslinked_reaction:

.. figure:: /Images/PolymersBondBoost/bond_boost_crosslinking.png

   Epoxide - amine polymerization reaction

The goal is not to capture or simulate the kinetics of the polymerization reaction, but rather to generate realistic atomistic models of epoxy polymers which can used in further simulations (e.g. for prediction of :ref:`mechanical properties <ReaxFF_polymers_mechanical_properties>`)

This advanced ReaxFF tutorial is loosely based on the following publications:

+ `A. Vashisth, C. Ashraf, W. Zhang, C. E. Bakis, and Adri C. T. van Duin, J. Phys. Chem. A 2018, 122, 32, 6633-6642 (2018) <http://dx.doi.org/10.1021/acs.jpca.8b03826>`__

+ `M.S. Radue, B.D. Jensen, S. Gowtham, D.R. Klimek-McDonald, J.A. King and G.M. Odegard, J. Polym. Sci. B, 56, 255-264 (2018) <https://doi.org/10.1002/polb.24539>`__

More details and information on other acceleration methods can be found in the ReaxFF manual:

+ `Bond boost method <../../AMS/Tasks/Molecular_Dynamics.html#bond-boost-method>`__
+ `Accelerating Molecular Dynamics <../../AMS/Tasks/Molecular_Dynamics.html#accelerated-dynamics>`__

.. tip::
  See also the tutorial :ref:`ReaxFF_polymers_mechanical_properties`


Setting up
----------

The cross linking polymerization reaction occurs between the epoxy and the amine groups. The reaction is depicted in its simplest, non-catalyzed form in :numref:`epoxy_crosslinked_reaction`.

Throughout this tutorial the epoxy resin will be BisF whilst DETDA will be used as the hardener (amine):

.. image:: /Images/PolymersBondBoost/bond_boost_bisF_DETDA.png

You can either draw the 3D structures of these molecules with the GUI or download the xyz files:

.. rst-class:: steps

  \
    | Click to download :download:`here <../downloads/BisF.xyz>` the .xyz file **BisF.xyz**
    | Click to download :download:`here <../downloads/DETDA.xyz>` the .xyz file **DETDA.xyz**

Use the builder functionality in AMSinput to fill a periodic box with one DETDA and two BisF molecules:

.. rst-class:: steps

  \
    | In AMSinput, select the ReaxFF panel: |ADFPanel| **→** |ReaxFFPanel|.
    | Go to **Edit → Builder** to open the Packmol dialog
    | Enter ``20``, ``20`` , ``20`` on the diagonal for the lattice vectors
    | Click on the **Folder icon** and select the file **BisF.xyz** you just downloaded
    | Click on **+** button and open the file **DETDA.xyz**
    | Enter ``2`` and ``1`` for BisF and DETDA respectively
    | Click on **Generate Molecules**

.. image:: /Images/PolymersBondBoost/bond_boost_packmol.png


To accelerate a reaction with the bond boost method, ReaxFF needs to be provided with a set of atom distances that define a preliminary complex which
could lead up to the transition state of the reaction. If this complex is formed during the dynamics, external forces are
applied to support bond breaking and bond formation for a user defined set of bonds. This 'boost' lasts for user defined time during which the reaction may or may not occur.

For the current reaction, a simple, yet effective set of atom distances are those between the N atom and the terminal C-atom of the epoxy group as well as the distance between the O-atom of the epoxy group to whichever H-atom of the amine group is closest:

.. image:: /Images/PolymersBondBoost/bond_boost_non_catalyzed.png

It is possible to distinguish atoms depending on their chemical environment, e.g. the terminal C-atom of the epoxy group, but the information needs to be provided via the regions model of ReaxFF by the user.
To distinguish the terminal C-atom from all other C-atoms in the system, a CT region needs to be setup:

.. rst-class:: steps

  \
    | Go to **Model → Regions**
    | Click **+** button next to Regions on the top
    | Enter a suitable name for the new region ``CT``
    | Select a terminal C-atom in the molecule panel
    | Click on the **+** button next to the ``CT`` region

.. image:: /Images/PolymersBondBoost/bond_boost_regions_1.png

Repeat steps **3.** and **4.** to add all other terminal C-atoms to the new CT region

.. image:: /Images/PolymersBondBoost/bond_boost_regions_2.png

.. tip::
  You can hold down the SHIFT key to select multiple atoms in the molecule view.

.. tip::
  If you have multiple identical molecules, the region can be copied over in the Regions panel
  using the 'Apply To Identical Molecules' option from the dropdown menu on the right.

Now the subset of terminal C-atoms can be distinguished via referring to the region CT as we'll see later.
The other regions are consisting of all N-,O- and H-atoms. To set up a region with all N-atoms:

.. rst-class:: steps

  \
    | Create a new region: Click **+** button next to Regions
    | Enter a suitable name: ``allN``
    | Select one N-atom
    | Go to **Select → Select Atoms Of Same Type**
    | Click on the **+** button next to the ``allN`` region

.. image:: /Images/PolymersBondBoost/bond_boost_regions_3.png

.. tip::
  Make sure that the atoms of the previous region assignment are not selected anymore when assigning
  a new region. Trying to assign one atom to multiple regions is a common source of error.

Continue setting up regions containing all O- and H-atoms respectively:

.. image:: /Images/PolymersBondBoost/bond_boost_regions_4.png

Once the regions are set up, we can use them to define a tracking regime for the bond boost.
The set of atom distances that will switch on the boost once all criteria are met is

.. image:: /Images/PolymersBondBoost/bond_boost_tracking.png

to set this up in the GUI

.. rst-class:: steps

  \
    | Go **Model → Bond boost**
    | Click on the **+** button next to **Bond boost**
    | Enter ``10000`` for the Boost lifetime
    | Click on the **+** button next to **Detect initial configuration**
    | From **Atom types with regions** menu, select **N-allN** and **C-CT**
    | Set **Rmin** to ``2.4`` and **Rmax** to ``4.0``


.. image:: /Images/P olymersBondBoost/bond_boost_tracking_gui.png
  :width: 60%
  :align: center

Continue with assigning the other tracking options:

+ **C-CT** / **O-allO**    ``1.2`` -  ``3.0``
+ **O-allO** / **H-allH**  ``3.0`` -  ``5.5``
+ **H-allH** / **→1**  ``0.8`` -  ``1.5``

.. Note::
  Note the last atom type is set to be **→1** to specify that it must be the initially
  detected Nitrogen atom, i.e. the one close to CT.

.. image:: /Images/PolymersBondBoost/bond_boost_tracking_gui_2.png
  :width: 60%
  :align: center

The boost settings are chosen such that the following logic is implemented

.. image:: /Images/PolymersBondBoost/bond_boost_boosting.png

the aim is to support the breaking and forming of bonds but still allow the reaction to fail.

.. Note::
  The above settings have been chosen empirically.
  A more thorough assessment of energetics based on ab initio calculations is presented in the
  publication by `A. Vashisth et al <http://dx.doi.org/10.1021/acs.jpca.8b03826>`__.

The bond boost options are defined in the lower part of the bond boost panel

.. rst-class:: steps

  \
    | Click on the **+** next to **Add restraint**
    | Choose the atoms **1** and **2** from the dropdown menu
    | Set R\ :sub:`0`\ (target bond length) to ``1.5``
    | Set k to ``0.04``, the type to **Erf** and the max. force F\ :sub:`∞`\  to ``0.4``

.. Note::
  The maximum allowed Force, F\ :sub:`∞`\, is the most important parameter.
  It is important that it's not too large because it may just rip the reactants apart if the force is too large
  We found, for example, that with 0.5 it's often ripping them apart, while with 0.3 it's much less likely but still possible. With 0.2 the reaction takes longer but should give more reasonable results in the end.
  The force constant value seems to be much less essential.

Continue with assigning two more boosts:

+ **3** / **4**  ``1.5`` , ``0.03`` , ``0.30``
+ **2** / **3**  ``2.5`` , ``0.03`` , ``0.30``

.. image:: /Images/PolymersBondBoost/bond_boost_boosting_2.png
  :width: 60%
  :align: center

Execution and visualization
---------------------------

After completing the setup of the bond boost in the previous chapter, we can test the boost by running a small NVT trajectory.
Choose the following general ReaxFF settings from the main panel

.. rst-class:: steps

  \
    | **Task → Molecular Dynamics**
    | **Force field** ``dispersion/CHONSSi-lg.ff``

.. image:: /Images/PolymersBondBoost/bond_boost_trajectory_settings.png
  :width: 60%
  :align: center

.. Note::
  This tutorial employs the dispersion corrected force field, that has not been optimized for usage with the bond boost.
  This force field has been used successfully in the study by `M.S. Radue et al. <https://doi.org/10.1002/polb.24539>`__
  The results might be improved by using the force field ``CHON2017_weak_bb.ff`` fitted for usage with the bond boost method (`A. Vashisth et al. <http://dx.doi.org/10.1021/acs.jpca.8b03826>`__ ).
  However, note that switching the force field will require tweaking the bond boost settings.

Open the MD settings:

.. rst-class:: steps

  \
    | Click on  |MoreBtn| next to **Molecular Dynamics**
    | For **Number of steps:** enter ``40000``

.. image:: /Images/PolymersBondBoost/bond_boost_trajectory_settings-2.png
  :width: 60%
  :align: center

Open the thermostat settings:

.. rst-class:: steps

  \
    | Click on  |MoreBtn| next to **Thermostat**
    | Click on  |AddButton| next to **Thermostat**
    | Select **Thermostat** → **Berendsen** and **Damping constant** ``100.0``
    | Set **Temperature** ``500.0``

.. image:: /Images/PolymersBondBoost/bond_boost_trajectory_settings-3.png
  :width: 60%
  :align: center

Save and run the calculation:

.. rst-class:: steps

  \
    | **File** → **Save**
    | **File** → **Run**

Open AMSmovie and follow the calculation of the trajectory, you should see at least one successful cross linking reaction.
The boost periods are visible as kinks in the energy graph

.. image:: /Images/PolymersBondBoost/bond_boost_amsmovie.png


Scaling it up: Generate large Polymer structures
------------------------------------------------

For simulation of polymer properties much larger structures are needed.
In the following chapter, we will explain how to scale up the bond boost simulation to more realistic systems up to several thousand atoms.

Open a new AMSinput window

.. rst-class:: steps

  \
    | From the SCM Menu **SCM** select **New Input**
    | Change to |ReaxFFPanel|

open the Packmol builder to create a larger initial structure.
Set up a periodic box with with 20 BisF epoxy and 10 DETDA hardener molecules.
Make sure that the density displayed in the bottom panel of builder panel is around 0.4 g/mL otherwise packing the molecules will become a hard task and some might even not fit at all. With that criterion in mind, a good box size seems to 32 Å.

.. rst-class:: steps

  \
    | **Edit → Builder**
    | Put ``32.0`` on diagonal of the **lattice vectors** panel
    | Click to download :download:`here <../downloads/BisF.xyz>`  the .xyz file **BisF.xyz**
    | Click to download :download:`here <../downloads/DETDA.xyz>` the .xyz file **DETDA.xyz**
    | Click on the Folder to import ``20`` BisF molecules
    | Click on the |AddButton| next to Molecules, and import another ``10`` DETDA molecules
    | Click on the **Generate Molecules** button

.. image:: /Images/PolymersBondBoost/bond_boost_packmol-big.png
  :width: 60%
  :align: center

Next we need to assign regions to one BisF and one DETDA molecule. One molecule of each species will suffice. It's possible to translate regions to identical molecules across the whole periodic as we shall see now.

Assign the following regions to one of the DETDA and one of BisF molecules:

.. image:: /Images/PolymersBondBoost/bond_boost_big_mol_regions.png
  :width: 60%
  :align: center

To assign the same regions to all other molecules automatically

.. rst-class:: steps

  \
    | Select **Add region in same to...** from the region dropdown menu
    | Repeat this step for all regions you have assigned

.. image:: /Images/PolymersBondBoost/bond_boost_big_mol_regions-menu.png
  :width: 100%
  :align: center

Your periodic box with all the regions automatically assign should now look like this

.. image:: /Images/PolymersBondBoost/bond_boost_big_mol_with-regions.png
  :width: 100%
  :align: center

Next we can assign the tracking for the bond bosst using the same logic as before with the exception of requesting more
bond boost instances and softer restraints. The instances refer to the number of simultaneously boosted reactions. Since we have ten amines, i.e. ten reaction sites, we could in principle expect ten simultaneous reactions (not counting double reactions on the same amine group). The restraints are softened to prevent the molecules from tearing apart when multiple boosts are active at the same time.

.. image:: /Images/PolymersBondBoost/bond_boost_big_mol_boost-settings.png
  :width: 60%
  :align: center

Now only the MD settings need to be set.

.. rst-class:: steps

  \
    | Switch to the **Main** panel
    | **Task → Molecular Dynamics**
    | **Force field** ``dispersion/CHONSSi-lg.ff``

.. image:: /Images/PolymersBondBoost/bond_boost_big_mol_MD-settings.png
  :width: 60%
  :align: center

This time we shall run the simulation for a longer time.
To increase the efficiency of the calculation, we will lower the framerate from writing
a snapshot every 100th to every 1000th MD step.

Open the MD settings:

.. rst-class:: steps

  \
    | Click on  |MoreBtn| next to **Molecular Dynamics**
    | For **Number of steps:** enter ``250000``

.. image:: /Images/PolymersBondBoost/bond_boost_big_mol_MD-settings-2.png
  :width: 60%
  :align: center

We use the same thermostat as before but will add a barostat:

.. rst-class:: steps

  \
    | Click on  |MoreBtn| next to **Thermostat**
    | Click on  |AddButton| next to **Thermostat**
    | Select **Thermostat** → **Berendsen** and **Damping constant** ``100.0``
    | Set **Temperature** ``500.0``

.. image:: /Images/PolymersBondBoost/bond_boost_trajectory_settings-3.png
  :width: 60%
  :align: center

.. rst-class:: steps

  \
    | Click on  |MoreBtn| next to **MD main options**
    | Click on  |MoreBtn| next to **Barostat**
    | Select **Barostat** → **Berendsen** and **Pressure** ``101325`` Pa (1 atm)
    | Set **Damping constant** to ``500.0`` fs

Save and run the calculation:

.. image:: /Images/PolymersBondBoost/bond_boost_big_mol_MD-settings-3.png
  :width: 60%
  :align: center

.. rst-class:: steps

  \
    | **File** → **Save**
    | **File** → **Run**

Analysis: Calculate the density and cross-linking ratio
-------------------------------------------------------

The trajectory can be monitored in AMSmovie, though it becomes increasingly tough to spot the reactions with such huge systems.
For this reason, we provide a special analysis tool that allows you to monitor the progress of the systems cross-linking via the cross-linking ratio.

.. rst-class:: steps

  \
    | Click to download the script :download:`cross-link-density.py <../downloads/cross-link-density.py>`
    | Place the script in the same folder where your .ams inputfile is located
    | on Windows and Mac, open a command line from AMSinput **Help** → **Command line** (windows) or **Help** → **Terminal**
    | type **bash** and hit ENTER

.. Note::
   You can find more information on PLAMS and AMS scripting in the `Getting started <../../Scripting/GettingStarted.html>`__ section of the scripting documentation.

To run the script execute the following command in the command line::

 $AMSBIN/plams cross-link-density.py -v resultsdir=ams.results

The script will print the results onto the command line as follows::

  ...
  ( 241/ 251) 42.000 0.550
  ( 242/ 251) 41.000 0.525
  ( 243/ 251) 41.000 0.525
  ( 244/ 251) 41.000 0.525
  ( 245/ 251) 41.000 0.525
  ( 246/ 251) 42.000 0.550
  ( 247/ 251) 42.000 0.550
  ( 248/ 251) 42.000 0.550
  ( 249/ 251) 43.000 0.575
  ( 250/ 251) 43.000 0.575
  ( 251/ 251) 43.000 0.575

  Final density: 0.407
  Cross-linking ratio: 0.575

Where the values in parentheses refer to the current analyzed frame and the total number of frames. The second column is the total number of C-N bonds found in the system at that frame and the third column is the cross-linking ratio computed as the ratio between newly formed CN-bonds and number of theoretically possible CN bonds (two new bonds per amine group).

.. Note::
   Obviously the density has not yet converged to the experimental value. Wether or not it's possible to just extend the simulated timescale, depends on the system. Often it helps to run one or several simulated annealing runs with such a cross-linked polymer structure to eliminate local density hot spots or vacuum bubbles in the structures.
   An enlightening discussion can be found in computational details of `A. Vashisth, C. Ashraf, W. Zhang, C. E. Bakis, and Adri C. T. van Duin, J. Phys. Chem. A 2018, 122, 32, 6633-6642 (2018) <http://dx.doi.org/10.1021/acs.jpca.8b03826>`__
