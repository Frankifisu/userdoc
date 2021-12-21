
.. _3DFieldVisualization:

3D field visualization with BAND
================================

With `AMSview <../../GUI/AMSview.html>`__ you can visualize three-dimensional fields from the results of a BAND Calculation (**runkf** file).

Following is a list of relevant fields, with a short explanation and illustrative pictures (from a simple non-periodic H\ :sub:`2` calculation).
All fields are in `atomic units (a.u.) <https://en.wikipedia.org/wiki/Atomic_units>`__.

Total_Density (rho)
   The electronic density :math:`\rho (r)`. The integral of the electronic density over the whole space (or, for periodic systems, over the unit cell) equals the total number of electrons (valence + core).

   .. image:: ../Images/Total_Density.png


Deformation density (rho(deformation))
   The deformation density is the difference between total density :math:`\rho (r)` and reference density :math:`\rho_\text{reference} (r)`

   .. math::

      \rho_\text{deformation} (r) =  \rho (r) - \rho_\text{reference} (r)

   The reference density :math:`\rho_\text{reference} (r)` is defined as the sum of densities of spherical spin-unrestricted isolated atoms.

   The deformation density is electrically neutral, i.e. its integral over the whole space (or, for periodic systems, over the unit cell) is zero.
   Positive values of deformation density indicate density accumulation wrt isolated atoms; negative values represent density depletion. 
   In our H\ :sub:`2` example, the deformation density shows how there is electron accumulation in the bonding region between the two hydrogen atoms.
   
   .. image:: ../Images/Deformaion_density.png


SCF_CoulombPot (v(coulomb))
   The total Coulomb potential (nuclear + electronic potentials). 
   BANDs convention for the Coulomb potential: the potential of positive charges (like nuclei) is **negative**, while the potential of negative charges (like electrons) is **positive**. In our example, the nuclear potential (negative) is larger than the electronic potential (positive) in the region of space near the H\ :sub:`2` molecule.

   .. image:: ../Images/SCF_CoulombPot.png

   .. note::

      The sign convention for potentials in **BAND** is the opposite to the **ADF** sign convention.


SCF_CoulombDeformation (v(coulomb/deformation))
   The Coulomb potential originating from the (overall neutral) deformation density.

   .. image:: ../Images/SCF_CoulombDeformation.png

xc pot (vxc(rho))
   The Exchange Correlation (XC) potential. Electrons are *attracted* by negative XC potentials (just like they are *attracted* by the negative nuclear Coulomb potential)

   .. image:: ../Images/xc_pot.png


Orbitals (occupied/virtual)
   The Kohn-Sham orbitals. 

   .. note::

     Be aware that there is an over-all arbitrariness in the sign of the orbitals

   Here we show the occupied and first virtual orbital of H\ :sub:`2`. 

   .. image:: ../Images/orbital_bonding.png

   .. image:: ../Images/orbital_antibonding.png

