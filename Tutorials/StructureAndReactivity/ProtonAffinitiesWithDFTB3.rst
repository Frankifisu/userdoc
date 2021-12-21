.. This tutorial has been recorded: examples/tutorials/proton-affinities-dftb3
.. Keep the recording in sync so it may be used to generate the images!

.. _dftb_dftb3:

Proton affinities with DFTB3
****************************

In this tutorial we will use the `DFTB engine <../../DFTB/index.html>`__ to calculate a proton affinity, defined as the negative gas phase enthalpy for the protonation reaction A\ :sup:`-`  + H\ :sup:`+`  → AH.   `Gaus, Cui and Elstner <http://pubs.acs.org/doi/abs/10.1021/ct100684s>`__ have shown that third-order terms (`DFTB3 <../../DFTB/DFTB_Model_Hamiltonian.html#model-hamiltonian>`__) generally improve the proton affinities with respect to second order self-consistent charges (SCC).

We will calculate the proton affinity of the acetate anion, CH\ :sub:`3` COO\ :sup:`-` . In the first step of this tutorial, we will optimize acetic acid at the DFTB3 level. The second step will perform the computation on the anionic species, and compute its proton affinity.

Step 1: Optimization of the neutral molecule
============================================

.. rst-class:: steps

  \
    | **1.** Start AMSjobs.
    | **2.** **SCM → New Input**.
    | **3.** Switch to **DFTB**: |ADFPanel| **→** |DFTBPanel|

Now we need to obtain an acetic acid molecule and set up a |GO| at the DFTB3 level.

.. rst-class:: steps

  \
    | **1.** Use the **Structure tool** (hexagon in the bar below the molecule view), select **Solvents → Acetic acid**.
    | **2.** Click anywhere in the visualization pane. The acetic acid molecule will appear.
    | **3.** Make sure **Geometry optimization** is selected as the task to perform.
    | **4.** Select **DFTB3** as the model.
    | **5.** Select the **DFTB.org/3ob-3-1** parameter directory.
    | **6.** Save and run the job either through **File → Run** or by pressing ``ctrl+r``. You will be asked to give your job a name.

.. image:: /Images/ProtonAffinitiesWithDFTB3/t_DFTB3acetic_neutral.png

When the optimization is complete (it should not take longer than a second), AMSinput will ask if you want to update your geometry with the optimized geometry.
For this tutorial it does not matter if you load the new geometry or not, as we are not going to run any calculations with the optimized geometry.

.. rst-class:: steps

  \
    | **1.** Open the output file through **SCM → Output**.
    | **2.** Scroll down through the steps of the geometry optimization until you find the section: **CALCULATION RESULTS**
    | **3.** Below that you find a printout of the energies, gradients, Mulliken charges and orbitals. Look for the line with **Total energy (Hartree)** and write down the value.

The total energy of the acetic acid molecule should be close to E(HAc) = -11.5755 Hartree. In order to calculate the proton affinity we now need to detach a proton and calculate the energies of the acetate ion and the lone proton.

Step 2: Optimization of the acetate and the hydrogen ions
=========================================================

In order to perform the calculation on the acetate ion, we will remove the hydrogen ion from the previously computed acetic acid molecule.

.. rst-class:: steps

  \
    | **1.** In AMSinput, select the hydrogen in the COOH group by clicking on it.
    | **2.** Press the Backspace key on your keyboard. This will delete the hydrogen atom.
    | **3.** Set the **Total charge** to **-1**.
    | **4.** Use **File → Save As...** to save your new job under a different name. Use **File → Run** or ``ctrl+r`` to run it.
    | **5.** Look for the **Total energy (Hartree)** in the output like you did for the neutral molecule.

.. image:: /Images/ProtonAffinitiesWithDFTB3/t_DFTB3acetate_ion.png

You should obtain an energy of about E(Ac\ :sup:`-` ) = -11.2458 Hartree for the acetate ion.

Finally we also need the energy of a lone proton. There is no point in performing a geometry optimization for a single proton, so here we simply perform a single point calculation.

.. rst-class:: steps

  \
    | **1.** Select and delete every atom of the molecule, except one hydrogen atom.
    | **2.** Set the task to **Single Point**.
    | **3.** Set the charge to **1**.
    | **4.** Use **File → Save As...** to save your new job under a different name. Use **File → Run** or ``ctrl+r`` to run it.
    | **5.** Look for the **Total energy (Hartree)** in the output.

.. image:: /Images/ProtonAffinitiesWithDFTB3/t_DFTB3hydrogen_ion.png

The total energy of the proton should be close to E(H\ :sup:`+` ) = 0.2407 Hartree.

The proton affinity is computed as PA = E(Ac\ :sup:`-` ) + E(H\ :sup:`+` ) - E(HAc), resulting in a final proton affinity of 0.5704 Hartree, or 357.93 kcal/mol.

We leave it as an example to calculate the PA with DFTB2 (SCC-DFTB), and compare it with the high-level ab initio results that are also quoted in the `DFTB3 paper. <http://pubs.acs.org/doi/abs/10.1021/ct100684s>`__


.. |GO| replace:: `geometry optimization <../../AMS/Tasks/Geometry_Optimization.html>`__
