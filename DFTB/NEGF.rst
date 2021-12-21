.. index:: NEGF
.. index:: Electronic transport


Electronic transport (NEGF)
===========================

.. seealso::

  - `DFTB-NEGF GUI tutorials <../Tutorials/ElectronicTransport/index.html>`__
  - :ref:`example Conductance`

Transport with NEGF in a nutshell
---------------------------------

The **Non-Equilibrium Green's Functions** formalism (**NEGF**) is a theoretical framework for modeling electron transport through nano-scale devices.
Electron transport is treated as a one-dimensional coherent scattering process in the "scattering region" for electrons coming in from the electrodes:

.. image:: /Images/NEGF_regions.png

Our goal is to compute the **transmission function** :math:`T(E)`, which describes the rate at which electrons of energy :math:`E` are transferred from the left electrode to the right electrode by propagating through the scattering region.
From the transmission function we can calculate the electric current for given **Bias Voltage** :math:`V` applied between the electrodes:

.. math::

   I(V) = \frac{2e}{h} \int_{-\infty}^\infty T(E) \left( f(E - \mu_L) - f(E - \mu_R) \right) dE


where :math:`f(E)` is the Fermi-Dirac distribution function for a given temperature, and :math:`\mu_L` (:math:`\mu_R`) is :math:`\epsilon_F + eV/2` (:math:`\epsilon_F - eV/2`), :math:`\epsilon_F` being the Fermi energy of the electrodes.

The transmission function :math:`T(E)` can be computed from the **Green's function** of our system.

The Green's function :math:`G(E)` of the scattering region is obtained solving the following equation:

.. math::

   (E S - H) G(E) = I

where :math:`S` is the overlap matrix, :math:`H` is the Hamiltonian and :math:`I` is the identity matrix.
The Hamiltonian is composed as follows (**L**, **C** and **R** denote the **left lead**, the **central region** and the **right lead** respectively):

.. math::

   H = \left( \begin{array}{ccc}
   H_L + \Sigma_L  & H_{LC}  & 0 \\
   H_{LC}          & H_C     & H_{RC} \\
   0               & H_{RC}  & H_R + \Sigma_R
   \end{array} \right)

The two *self-energies* :math:`\Sigma_L` and :math:`\Sigma_R` model the two semi-infinite electrodes.

The transmission function :math:`T(E)` can be calculated from the Green's function :math:`G(E)` and the so-called *coupling matrices* :math:`\Gamma_L(E)` and :math:`\Gamma_R(E)` (which are related to :math:`\Sigma_L` and :math:`\Sigma_R`):

.. math::

   T(E) = Tr[G(E) \Gamma_R(E) G(E) \Gamma_L(E)]


.. seealso::

  `PhD Thesis <https://opus.jacobs-university.de/frontdoor/index/index/docId/478>`__ of Mahdi Ghorbani-Asl (DFTB-NEGF developer)


Simulations work flow
---------------------

The computation of the transmission function :math:`T(E)` within the DFTB-NEGF formalisms requires three individual simulations.

.. tip::

   Use ADFInput (GUI) to set up your DFTB-NEGF calculation (see the `DFTB-NEGF GUI tutorials <../Tutorials/ElectronicTransport/index.html>`__)


1): DFTB leads calculation
  A 1D-periodic DFTB calculation of the leads (:ref:`StoreMatrices <dftb-key-StoreMatrices>`: yes, :ref:`KSpace <dftb-key-KSpace>` sampling 13):

  .. image:: /Images/NEGF_lead_calc.png

  The Hamiltonian matrices :math:`H_L` and :math:`H_{R}` and the Fermi energy of the electrode :math:`\epsilon_F` are computed in this calculation (:math:`H_L`, :math:`H_{R}` and :math:`H_{LR}` are also used to compute the surface Green's functions :math:`g_L` and :math:`g_R` of the semi-infinite electrodes).

2): DFTB scattering-region calculation
  A a 1D-periodic DFTB calculation of the scattering region (:ref:`StoreMatrices <dftb-key-StoreMatrices>`: yes, gamma-only, *i.e.*, no :ref:`KSpace <dftb-key-KSpace>` sampling):

  .. image:: /Images/NEGF_scattering_region_calc.png

  The Hamiltonian matrices :math:`H_{LC}` and :math:`H_{RC}` and :math:`H_{C}` are computed in this calculation.

3): Conductance calculation
   The **Conductance program** computes the NEGF transmission function :math:`T(E)` using the Hamiltonians and Overlap matrices from the previous two DFTB calculations.



Conductance input options
-------------------------

The **Conductance** program computes the transmission function using the NEGF approach.
This is the input structure of the **conductance** program::

   $AMSBIN/conductance <<EOF > conductance.out

     EnergyGrid
        Min value
        Max value
        Num value

     Files
        Leads       /path/DFTB_lead_filename.rkf
        Scattering  /path/DFTB_scattering_filename.rkf
     End

     Technical
        Eta                   value
        OverwriteLeads        [True|False]
        SetOffDiagonalToZero  [True|False]
     End

     end input
   EOF


.. scmautodoc:: conductance EnergyGrid
  :nosummary:

.. scmautodoc:: conductance Technical
  :nosummary:

.. scmautodoc:: conductance Files Leads Scattering
  :nosummary:


Miscellaneous remarks on DFTB-NEGF
----------------------------------

* You should make sure that your results are converged with respect to the number of lead repetitions; the results should not change significantly if you increase the number of lead repetitions.
* It's good practice to include at least one lead repetition in the central region.
* The transmission function is computed at zero bias voltage. The zero-bias transmission function is then used for computing the electric current for non-zero bias voltage.
