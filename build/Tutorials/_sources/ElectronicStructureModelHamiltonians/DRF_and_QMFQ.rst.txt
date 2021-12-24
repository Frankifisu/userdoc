.. _DRF_QMFQ:

QM/MM with polarizable force fields
***********************************

This (technical) example shows how to make an input for the QM/MM methods DRF and QM/FQ in which both polarizable force fields are used.

You can study chemistry in solution, as contrasted to the gas phase, with the implementation of implicit solvation models (continuum solvation) like COSMO and SM12,
or explicit solvation models like molecular dynamics or multi-level methods.
Many multi-level methods exist that can treat solvation effects, like QM/MM with mechanical or electrostatic embedding, QM/MM with polarizable force-fields like DRF and QM/FQ, or frozen density embedding (FDE).
Using implicit solvation models is relatively straightforward.
For explicit solvation models using multi-level methods, like DRF and QM/FQ you will need to define regions.

The geometry for such QM/MM calculations could be taken from snapshots of a molecular dynamics calculation.

DRF
===

To demonstrate how to set up a DIM/QM DRF (Discrete Solvent Reaction Field) calculation using AMSinput, we will use water in water as an example.
DRF is a QM/MM method in which the MM atoms interact with the QM region via induced dipoles and static charges.
DRF facilitates calculating the optical properties of molecules.
One should use the 'Single Point' Task.

.. rst-class:: steps

  \ 
    | Download the following xyz file: file :download:`water_in_water.xyz <../downloads/water_in_water.xyz>`
    | Open AMSinput: **File → Import Coordinates...** and select 'water_in_water.xyz'
    | Select Task **Single Point**
    | Select XC functional **Model:SAOP**
    | Select Basis set **TZ2P** and Core **None**
    | Select Numerical Quality **Good**
    | Use the panel bar **Properties → Excitations (UV/Vis), CD** command
    | For the 'Type of excitations' option, Select 'SingletOnly'
    | Select the middle water molecule 
    | (for example with **Model → Coordinates** and select the first 3 atoms)
    | Use the panel bar **Model → Regions** command
    | click the |AddButton| button next to Regions, and rename Region_1 to ``Solute``
    | Select all other atoms of the complex (by Select → Invert Selection) 
    | click the |AddButton| button again, and rename Region_2 to ``Solvent``
    | Use the panel bar **Model → DIM/QM** command
    | For the 'Method' option, Select 'DRF'
    | Click the check button 'QM part' for the 'Solute' region
    | Click the check button 'DIM part' for the 'Solvent' region

In the next step atomic charges for the DRF region are computed using MDC-Q charges (LDA functional, DZP basis set).
The atomic polarizabilities are taken from a inner database including fitted parameters for the H, C, N, O, F, S, Cl, Br, and I atoms,
and non-optimized parameters for most other atoms.

.. rst-class:: steps

  \ 
    | For the 'Select charges' option, Select 'MDC-Q'
    | Save as 'Water_DRF'
    | **File → Run**

.. image:: /Images/DRF_and_QMFQ/drfinput.png

QM/FQ(Fμ)
=========

To demonstrate how to set up a QM/FQ (Quantum Mechanics/Fluctuating Charges) or QM/FQFμ (if Fluctuating Dipoles are included) calculation using AMSinput, we will use 2-methyloxirane in water as an example.
These are QM/MM methods in which the MM atoms interact with the QM region via induced charges and possibly dipoles.
The MM charges and dipoles are determined self-consistently along with the ground-state QM density.
QM/FQ(Fμ) also facilitates calculating the optical properties of molecules.
Since the charges and dipoles depend on the QM density, explicit terms also appear within response equations that are solved to simulate spectroscopic and excited-state properties of the QM system.

One should use the 'Single Point' Task.

.. rst-class:: steps

  \ 
    | Download the following xyz file: file :download:`methyloxirane_in_water.xyz <../downloads/methyloxirane_in_water.xyz>`
    | Open AMSinput: **File → Import Coordinates...** and select 'methyloxirane_in_water.xyz'
    | Select Task **Single Point**
    | Select XC functional **GGA:PBE**
    | Select Basis set **TZP** and Core **None**
    | Select Numerical Quality **Good**
    | Use the panel bar **Properties → Excitations (UV/Vis), CD** command
    | For the 'Type of excitations' option, Select 'SingletOnly'
    | Select the 2-methyloxirane molecule 
    | Use the panel bar **Model → Regions** command
    | click the |AddButton| button next to Regions, and rename Region_1 to ``Solute``
    | Select all other atoms of the complex (by Select → Invert Selection) 
    | click the |AddButton| button again, and rename Region_2 to ``Solvent``
    | Click on the right arrow at the end of the 'Solvent' line
    | Use the 'Hidden' command from the menu that appears

.. image:: /Images/DRF_and_QMFQ/hiddenregion.png

Hidden here means that the molecules in the 'Solvent' region are hidden.
The 'Solvent' region is still visible because it is colored.
 
The GUI has parameters for QM/FQ in case water is the solvent in the FQ region.

.. rst-class:: steps

  \ 
    | Use the panel bar **Model → QM/FQ** command
    | Check the Enable checkbutton
    | Click the check button 'QM part' for the 'Solute' region
    | Click the check button 'FQ part' for the 'Solvent' region
    | Save as 'methyloxirane_QMFQ'
    | **File → Run**

.. image:: /Images/DRF_and_QMFQ/qmfqinput.png
