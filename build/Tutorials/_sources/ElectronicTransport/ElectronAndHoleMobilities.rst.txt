.. _ElectronHoleMobilities:

Electron and hole mobilities in organic electronics: charge transfer integrals
******************************************************************************

Calculation of charge mobilities
================================

Charge mobility is of crucial importance for efficiency in organic electronic devices such as field-effect transistors (OFETs), light-emitting diodes (OLEDs) and photovolatic cells (OPVs). In the so-called hopping regime, charges move incoherently from site to site, with a rate determined by the charge transfer integrals, which are straightforwardly calculated with the unique fragment-based approach in ADF.

This guided example explains how to calculate charge mobility with ADF.

.. seealso::
    
    * `PLAMS script for computing charge transfer integrals with ADF <../../plams/examples/ChargeTransferIntegralsADF.html>`__
    * `PLAMS recipe for computing reorganization energies <../../plams/examples/ReorganizationEnergy.html>`__
    * `ADF manual on charge transfer integrals <../../ADF/Input/Charge_transfer_integrals.html>`__


Define the fragments for charge transfer
========================================

As a simple example we will study electron and hole mobility between two naphthalene molecules. Let us start with downloading the :download:`.xyz file <../downloads/naphthalene_dimer.xyz>` of the naphthalene dimer, which was cut out from the experimental crystal structure (for your own organic semiconductor material, you can just import the cif file, :ref:`generate a supercell <supercell>`, and cut out dimers to calculate the charge mobility in different directions)

.. rst-class:: steps

 \
  | **1.** Start up **AMSinput**
  | **2.** Select **File** → **Import Coordinates** in the menu bar and import the .xyz file you just downloaded
  | **3.** In the **panel bar**, select **Model** → **Regions**
  | **4.** Select all the atoms (e.g. by clicking **Select → Select All** in the **menu bar**) and add a new region by clicking on |AddButton|
  | **5.** Click on the selection arrow for the newly create region and select **Split by molecule**

.. image:: /Images/ElectronAndHoleMobilities/adf_electron_hole_regions.png

.. rst-class:: steps

 \
  | **1.** In the panel bar, select **Multilevel** → **Fragments**
  | **2.** Tick the **Use fragments** check box

.. image:: /Images/ElectronAndHoleMobilities/adf_electron_hole_fragments.png

You can read more about ADF's fragments approach in the `ADF manual <../../ADF/Input/Molecular_fragments.html>`__ or in the :ref:`ADF fragments tutorial <FRAGMENT>`.

Transport properties and settings
---------------------------------

.. rst-class:: steps

 \
  | **1.** In the panel bar, select **Properties** → **Other: Etot, Charge Transport, ...**
  | **2.** Tick the check box **Charge transfer integrals (for transport properties)**
  | **3.** Go back to the **Main** panel
  | **4.** Select the XC functional **GGA:PW91**
  | **5.** Select Relativity **None**
  | **6.** Select the **TZP** basis set
  | **7.** Set the Frozen core at **None**
  | **8.** Run the calculation (Ctrl/cmd + r) (Save file and acknowledge use of NOSYM)

When using molecular fragments in ADF, multiple calculations will be (automatically) performed: first, each fragment is computed individually (in this case, the individual naphthalene molecules). Then the calculation of the full system is performed in which the Hamiltonian matrix elements are expressed in the basis of the molecular orbitals of the fragments. It is within this framework that the site energies, charge transfer integrals and overlap integrals between fragment orbitals are computed. More information on this can be found in the `charge transfer integrals section <../../ADF/Input/Charge_transfer_integrals.html>`__  of the ADF manual and in the following publications by Senthilkumar et al. [#senthilkumar_1]_ [#senthilkumar_2]_.

When the job is finished, we search for the charge transfer integrals in the output:

.. rst-class:: steps

  \
   | Open the output file by clicking at **SCM** → **Output**
   | In the **menu bar**, select **Properties** → **Charge transfer integrals**


Generalized Charge Transfer Integrals
-------------------------------------

The electronic coupling V (also known as effective or generalized charge transfer integral J\ :sub:`eff`) that goes into Marcus theory is calculated as (see e.g. Wen et al. [#wen]_ )

.. math::

   V = \frac{J - \frac{S(\varepsilon 1 + \varepsilon 2)}{2}}{1 - S^2}

J is the transfer integral, S the overlap, and ε the site energy.

The generalized charge transfer integrals  and the components are printed in the output:

.. image:: /Images/ElectronAndHoleMobilities/adf_electron_hole_output.png

The electronic coupling between these two naphthalene molecules is thus calculated as 0.00766 eV for hole transport and 0.03780 eV for electron transport.

Look at the t\ :sub:`ab` results in Coropceanu et al. [#coropceanu]_ for more information. The signs of J and S depend on the phase of orbitals (which is arbitrary). Since V\ :sup:`2` is used in the Marcus equation, the sign does not affect the hopping rates.

Reorganization energies
=======================

The reorganization energy λ is defined as the energy difference between the charged and neutral systems at the two different geometries (adiabatic PES). E.g. for electron transfer:

.. math::

   \lambda = (E^\text{anion}_\text{neutral geometry} - E^\text{neutral}_\text{neutral geometry}) + (E^\text{neutral}_\text{anion geometry} - E^\text{anion}_\text{anion geometry})

We therefore need to perform four calculations: two geometry optimizations and two single point calculations.

First, set up the **geometry optimization for the neutral naphthalene** (from which we will obtain :math:`E^\text{neutral}_\text{neutral geometry}`):

.. rst-class:: steps

 \
  | Open a new **AMSinput**
  | **1.** Select **File** → **Import Coordinates** in the menu bar and import :download:`naphthalene_dimer.xyz <../downloads/naphthalene_dimer.xyz>`
  | **2.** Delete one of the two naphthalene molecules
  | **3.** Symmetrize the molecule by clicking on |SymmTool|
  | **4.** We will use the same calculation settings as in the charge-transfer integrals job: in the main panel, set the XC functional to **GGA:PW91**, the basis to **TZP** and the frozen core to **None**
  | **5.** Change the task to **Geometry Optimization**
  | **6.** Click on **File → Save as** and save it as **neutral_geometry_optimization**


.. image:: /Images/ElectronAndHoleMobilities/adf_electron_hole_GO.png

Then, set up the **geometry optimization for the anion** (from which we will obtain :math:`E^\text{anion}_\text{anion geometry}`):

.. rst-class:: steps

 \
  | In **AMSinput** (main panel)
  | **1.** Set the **Total charge** to ``-1``
  | **2.** Tick the **Unrestricted** check box
  | **3.** Set the **Spin Polarization** to ``1``
  | **4.** Click on **File → Save as** and save it as **anion_geometry_optimization**

Run the two geometry optimizations:

.. rst-class:: steps

 \
  | Open **ADFJob**
  | **1.** Select the jobs **neutral_geometry_optimization** and **anion_geometry_optimization** and click on **Job** → **Run** 

We now need to run the two single point calculations:

.. rst-class:: steps

 \
  | **1.** Run a **single point** calculation for a neutral naphthalene (i.e. **Total charge = 0** and **Spin Polarization = 0**) at the optimized geometry of the anion (i.e. the final geometry of the **anion_geometry_optimization** calculation). From this we will obtain :math:`E^\text{neutral}_\text{anion geometry}`
  |
  | **2.** Run a **single point** calculation for the naphthalene anion (i.e. **Total charge = -1** and **Spin Polarization = 1**) at the optimized geometry of the neutral naphthalene (i.e. the final geometry of the **neutral_geometry_optimization** calculation). From this we will obtain :math:`E^\text{anion}_\text{neutral geometry}`


Collect the four bonding energies from either the output files or the log files:

:math:`E^\text{anion}_\text{anion geometry} = -119.3514 \text{[eV]}`

:math:`E^\text{anion}_\text{neutral geometry} =  -119.2451 \text{[eV]}` 

:math:`E^\text{neutral}_\text{neutral geometry} = -119.4217 \text{[eV]}` 

:math:`E^\text{neutral}_\text{anion geometry} = -119.3142 \text{[eV]}`

and calculate λ which is around 0.21 eV at this level of theory.

Hopping rates from Marcus theory
================================

The Marcus rate for charge hopping between two sites is:

.. math::

   k = \frac{V^2}{\hslash}  \sqrt{\frac{\pi}{\lambda k_{b}T}}   e^{ \left( \frac{-\lambda}{4k_{b}T} \right) }

In our example (V = 6.06 10\ :sup:`-21` J, λ = 3.36 10\ :sup:`-20` J) the Marcus hopping rate for electrons is 6.9 10\ :sup:`12` s\ :sup:`-1` at 300K.

Macroscopic charge mobilities can be obtained from these hopping rates via Monte Carlo (e.g. Kwiatkowski et al. [#kwiatkowski]_ ) or analytical approaches to calculate the diffusion coefficient that goes into the Einstein relation (e.g. Wen et al. [#wen]_ ).


Further considerations for charge mobilities
============================================

As shown by Sutton et al. [#sutton]_ , the transfer integrals depend strongly on the amount of exact exchange. The GGA functional PW91 has often been used with good results.
Likewise, the site energies and reorganization energies will also depend on the functional used. For λ often hybrids are used in the literature. Other technical settings may affect the accuracy of the calculation as well: basis sets, numerical quality...

Pavanello et al. [#pavanello]_ have implemented electronic couplings with the frozen-density embedding framework in ADF. This approach also allows the inclusion of multiple molecules which will affect the electronic couplings. It is formally linear-scaling with the number of subsystems, hence enabling the study of environment effects on electronic transport in amorphous crystals.
You can watch `Pavanello’s web presentation on electronic couplings with FDE. <https://www.scm.com/wp-content/uploads/Videos/ChargeMobilitiesWithFDE.wmv>`__

When many charge transfer integrals are needed (e.g. an amorphous crystal with many different dimer orientations), the calculation may be speeded up. Energy decomposition may be switched off, the SCF cycles can be set to 0 (with typically a small effect on the integrals), and the preparation and analysis can be streamlined by using PLAMS or the AMSprep and AMSreport tools.

References
==========

.. [#senthilkumar_1] K.\  Senthilkumar, F.C. Grozema, F.M. Bickelhaupt, and L.D.A. Siebbeles, *Charge transport in columnar stacked triphenylenes: Effects of conformational fluctuations on charge transfer integrals and site energies*, `Journal of Chemical Physics 119, 9809 (2003) <https://doi.org/10.1063/1.1615476>`__. 

.. [#senthilkumar_2] K.\  Senthilkumar, F.C. Grozema, C. Fonseca Guerra, F.M. Bickelhaupt, F.D. Lewis, Y.A. Berlin, M.A. Ratner, and L.D.A. Siebbeles, *Absolute Rates of Hole Transfer in DNA*, `Journal of the American Chemical Society 127, 14894 (2005) <https://doi.org/10.1021/ja054257e>`__ 

.. [#wen] \ S. Wen, A. Li, J. Song, W. Deng, K. Han, W.A. Goddard III, *First-Principles Investigation of Anistropic Hole Mobilities in Organic Semiconductors*, `The Journal of Physcial Chemistry B 113, 8813 (2009) <https://pubs.acs.org/doi/10.1021/jp900512s>`__

.. [#coropceanu] \ V. Coropceanu, R.S. Sánchez-Carrera, P. Paramonov, G.M. Day, J. Brédas, *Interaction of Charge Carriers with Lattice Vibrations in Organic Molecular Semiconductors: Naphthalene as a Case Study*, `The Journal of Physcial Chemistry C 113, 4679 (2009) <https://pubs.acs.org/doi/10.1021/jp900157p>`__

.. [#kwiatkowski] \ J.J. Kwiatkowski, J. Nelson, H. Li, J.L. Bredas, W. Wenzel, C. Lennartz, *Simulating charge transport in tris(8-hydroxyquinoline) aluminium (Alq3)*, `Physical Chemistry Chemical Physics 10, 1852 (2008) <https://pubs.rsc.org/en/content/articlelanding/2008/CP/b719592c#!divAbstract>`__

.. [#sutton] \ C. Sutton, J.S. Sears, V. Coropceanu, J. Brédas, *Understanding the Density Functional Dependence of DFT-Calculated Electronic Couplings in Organic Semiconductors*, `The Journal of Physical Chemistry Letters 4, 919 (2013) <https://pubs.acs.org/doi/abs/10.1021/jz3021292>`__

.. [#pavanello] \ M. Pavanello, T. Van Voorhis, L. Visscher, J.Neugebauer, *An accurate and linear-scaling method for calculating charge-transfer excitation energies and diabatic couplings*, `The Journal of Chemical Physics 138, 054101 (2013) <https://aip.scitation.org/doi/10.1063/1.4789418>`__
