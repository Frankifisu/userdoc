
Introduction
############

As per 2020 UFF force fields and simple classical force fields are unified in the ForceField engine. This replaces the old UFF engine and the NewMM functionality from ADF.

Available force fields
**********************

The default force field is UFF, it requires no configuration.
UFF (Universal Force Field) is a full periodic table force field that can be used to calculate single point energies, do geometry optimizations, calculate frequencies, etc. It is also the default pre-optimizer in the Graphical User interface (GUI) to clean up manually drawn structures. For details on the inner workings of the force field, see the 1992 paper by Rappe et al. [:ref:`1<reference 1>`]. By default UFF uses non-zero charges for water molecules only.

Other available force fields managed by this engine include Amber95, Tripos 5.2, GAFF and APPLE&P [:ref:`9<reference 9>`].

ForceField-GUI
**************

Note that the graphical user interface UFF-GUI enables all users to set up force field calculations with a few mouse clicks. Most force fields require atom typing, and this needs to be done by hand. When using UFF, also for pre-optimizing, it is important to remember that any force field method relies on a set of parameters. This means that even though UFF supports all elements up to Z=103, it might not generate the desired structures for uncommon oxidation states in metallic structures. If this is the case, you could add new parameters to UFF or attach dummy hydrogen atoms to the metal atom. 


What's new in ForceField 2021
*****************************

* The engine has been parallelized with MPI using force decomposition.
* The particle mesh Ewald method (implemented through the `helPME library <https://github.com/andysim/helpme>`__) is now used for electrostatic interactions in 3D systems.
* The default non-bonded cutoff has been reduced to 15 Angstrom, a value more typical in the force-field community.
* The engine has been optimized to be on par with the industry standards. The total speed-up compared to version 2020 can be up to factor 500.

What's new in ForceField 2020
*****************************

New features
============

* Periodic support (chains,slabs, and crystals) for all force field types
* Import force field parameters from amber ".dat" files




**shell script without atom typing:**

.. code-block:: none

   #!/bin/sh

   # This is a shell script for the ForceField engine

   # You should use '$AMSBIN/ams' instead.

   $AMSBIN/ams <<eor
      # Input options for the AMS driver: 

      Task GeometryOptimization

      System
         Atoms
            H 0.0 0.0 0.0
            H 0.9 0.0 0.0
         End
      End

      # The input options for the ForceField, which are described in this manual, 
      # should be specified in the 'Engine ForceField' block:

      Engine ForceField
         # the default one is UFF, requiring no options
      EndEngine
   eor


Force field setup for AMS applications
**************************************

When you do a geometry optimization of perform a MD calculation the details of the force field are determined only once and kept constant during the run. This applies to bond orders, partial charges, etc. In case of a polarizable force field (not currently supported) the charges are of course allowed to change.


Classical force fields
**********************

Most force fields require atom typing, as well as atomic charge specifications, see :ref:`examples`.


