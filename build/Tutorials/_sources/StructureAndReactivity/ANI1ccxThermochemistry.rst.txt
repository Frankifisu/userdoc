.. This tutorial has been recorded: examples/tutorials/ani-1ccx-thermochemistry
.. Keep the recording in sync so it may be used to generate the images!

.. _ANI1ccxThermochemistry:

ANI-1ccx Thermochemistry
************************************

**This tutorial will teach you how to**: 

* Download and install the **ANI-1ccx machine learning (ML) potential parameter set** [#refani1ccx]_ for organic molecules containing H, C, N, and O. ANI-1ccx was fitted to DLPNO-CCSD(T) reference data, which is a good approximation to CCSD(T).

* Calculate a gasphase reaction energy for an isomerization reaction using ANI-1ccx.

.. image:: /Images/ANI1ccxThermochemistry/reaction.png
   :width: 60%
   :align: center

The above reaction is part of the ISOL benchmark set [#refisol24]_ for organic
isomerization reactions. The **CCSD(T)-calculated reaction (isomerization)
energy is +5.30 kcal/mol**. [#refreactionenergy]_

.. seealso::

   `MLPotential documentation <../../MLPotential/index.html>`__

Set up and run ANI-1ccx calculations
------------------------------------------------

You can set up and run the calculations for this tutorial using either the
Graphical User Interface (GUI) or the python library `PLAMS
<../../plams/index.html>`__. First run the tutorial with the GUI, as that will
install all necessary dependencies automatically.

.. tabs::

   .. tab:: GUI

      .. rst-class:: steps
      
        \
          | **1.** Start AMSinput.
          | **2.** Switch to **ML Potential**: |ADFPanel| **→** |MLPotentialPanel|
          | **3.** Set the **Task** to **Single Point**.
          | **4.** Set the **Model** to **ANI-1ccx**.
          | **5.** Import the coordinates for Molecule **1** (see below), either using **File → Import coordinates** or by copy-pasting the coordinates into the AMSinput window. 
      
      .. image:: /Images/ANI1ccxThermochemistry/ani1ccx_tutorial.png
         :width: 100%
         :align: center

      **Molecule 1**  (:download:`download e_14.xyz <../../../examples/TestMLPotential/TorchANI_opt/e_14.xyz>`) [#refisol24]_
      
      .. IUPAC name 1-(2-hydroxyphenyl)-2-methylbutane-1,3-dione, SMILES string ``CC(C(C)=O)C(=O)C1=CC=CC=C1O``
      
      .. literalinclude:: <../../../../../examples/TestMLPotential/TorchANI_opt/e_14.xyz
      

                   
      .. rst-class:: steps
      
        \
          | **6.** Save the job with the name ``mol1singlepoint.ams``.
          | **7.** If this is the **first time** you save a job with ANI-1ccx, you will be prompted whether to download and install the **torchani** backend. Select **yes**. It may take some time for the installation to complete. The installation requires a working internet connection.
          | **8.** Run the job.
          | **9.** Open the output file with AMSoutput: **SCM → Output**
      
      Locate the energy in the section ``CALCULATION RESULTS``:
      
      .. code-block:: none
      
         CALCULATION RESULTS
      
      
         Energy (hartree)          -651.36347065
      
      
      Repeat the above steps for **Molecule 2** (:download:`download p_14.xyz <../../../examples/TestMLPotential/TorchANI_opt/p_14.xyz>`, or copy-paste the below coordinates)
      
      ..   IUPAC name 2-propanoylphenyl acetate, SMILES string ``CCC(=O)C1=CC=CC=C1OC(C)=O``
      
      .. literalinclude:: <../../../../../examples/TestMLPotential/TorchANI_opt/p_14.xyz
      
      The output for **Molecule 2** should read
      
      
      .. code-block:: none
      
         CALCULATION RESULTS
      
      
         Energy (hartree)          -651.35251657
      
      which gives a **reaction energy** of (-651.35251657)-(-651.36347065) = 0.010954 Hartree = **+6.9 kcal/mol**.

   .. tab:: Python

      .. rst-class:: steps

        \
          | **1.** Download 
                   :download:`e_14.xyz <../../../examples/TestMLPotential/TorchANI_opt/e_14.xyz>`
                   and 
                   :download:`p_14.xyz <../../../examples/TestMLPotential/TorchANI_opt/p_14.xyz>`, 
                   which correspond to molecules **1** and **2**, respectively.
          | **2.** Save the below script with the name ``reaction.py``.
          | **3.** Run the script using PLAMS: in a terminal, type ``$AMSBIN/plams reaction.py``. It will print the reaction energy.
          | **4.** Your calculation results are saved in the ``plams_workdir/`` directory.

      In the following python script (using the `PLAMS
      <../../plams/index.html>`__ library) we set up two single-point
      calculations using the MLPotential engine with ``Model ANI-1ccx``, and
      calculate the reaction energy.

      .. literalinclude:: <../../../../../examples/TestMLPotential/TorchANI_opt/ANI1ccxReactionEnergy.plms
         :language: python

         
      .. note::

         It may take a few seconds to initialize the ANI-1ccx model, and in the above script it is initialized two times. If you have two or more identical single point or geometry optimization calculations for different molecules, consider running them via a `PLAMS AMSWorker <../../plams/interfaces/amsworker.html>`__:

         .. literalinclude:: <../../../../../examples/TestMLPotential/TorchANI_opt/ANI1ccxReactionEnergyAMSWorker.plms
            :language: python

         With a PLAMS AMSWorker, you can run calculations for many molecules while only running the initialization once. **That can save a lot of time** for fast methods like ANI-1ccx.





Estimating reliability
----------------------

Machine learning potentials give accurate predictions **only** for molecules or
systems similar to those that were used during the parameterization of the
machine learning potential. For other systems, the predictions may be very
inaccurate.

The prediction (i.e., the energy, as calculated above) from the ANI potentials,
like ANI-1ccx, **are averages over 8 separately trained neural networks (a neural
network ensemble)**. The standard deviation of the 8 separate predictions can
be used as a measure for estimating how reliable a prediction is. If all
predictions are very similar (small standard deviation), similar molecules to
the calculated one should have appeared in the training set. If the predictions
are very different (large standard deviation), then the potential has likely not
been trained to the type of molecule it is being used for.

You can see the standard deviation of predicted energies for your molecule in
the auxiliary output file ``jobname.results/worker.0/mlpotential.txt``.
For example, for **Molecule 1**, you will see

.. code-block:: none

                           Energy     -651.363471 Ha
                  Number of atoms              26
                    Ensemble size               8
   
               Standard deviation        2.128358 mHa
                                         0.081860 mHa per atom
                                         0.417405 mHa per sqrt(atom)


In this case, the standard deviation for **Molecule 1** is 2.128 mHa = 1.3
kcal/mol. For **Molecule 2**, it is 1.8 kcal/mol. It is up to you to decide
whether you consider these numbers to be "small" (good) or "large" (bad). For
more information, see for example Refs [#refani1ccx]_ and [#refani1x]_.

.. note::

   The standard deviation grows with the square root of the number of atoms
   (assuming per-atom prediction errors follow a normal distribution). When
   comparing standard deviations for molecules with different number of atoms,
   it is a good idea to consider the ``standard deviation per sqrt(atom)``
   shown above.


Free energies, vibrational normal modes, and more
---------------------------------------------------

The given structures had been optimized at a high level of theory.
[#refisol24]_ You can also (re-)optimize them with ANI-1ccx: 

.. rst-class:: steps

  \
    | **1.** Start AMSjobs.
    | **2.** Open the mol1singlepoint job with AMSinput.
    | **3.** Set the **Task** to **Geometry Optimization**.
    | **4.** Tick the **Frequencies** checkbox.
    | **5.** Save as mol1geo and run. 

.. image:: /Images/ANI1ccxThermochemistry/gibbsinput.png
   :width: 60%
   :align: center

Look for **Gibbs free energy** in the output (see the `Thermo keyword
<../../AMS/Vibrational_Spectroscopy.html#gibbs-free-energy-change-for-a-gas-phase-reaction>`__).

.. rst-class:: steps

  \
    | **1.** In AMSjobs select the mol1geo job.
    | **2.** Open it with the **SCM → Output** menu command.
    | **3.** In the search field at the bottom type 'Gibbs' and observe the Gibbs free energy.
    | **4.** Visualize the normal modes in AMSspectra: **SCM → Spectra**.

.. image:: /Images/ANI1ccxThermochemistry/normalmode.png
   :width: 60%
   :align: center

.. tip::

   ANI-1ccx geometry optimization jobs **can be run interactively in
   AMSinput**. Right-click on the pre-optimizer button |PreOptimTool|, and
   select ANI-1ccx.

.. note::

   The reaction energy above was calculated for particular conformations of the
   molecules **1** and **2**. To explore all conformational isomers
   (conformers), see the :ref:`Conformers tutorial <Conformers>`.

.. tip::

   If your organic molecules contain F, S, and/or Cl, you can run calculations
   using the `ANI-2x model
   <../../MLPotential/general.html#included-pre-parameterized-models>`__.

.. tip::

   Consider using ANI-1ccx or ANI-2x to calculate a full approximate Hessian,
   and then use ADF to :ref:`refine the vibrational modes <AMS_mode_refinement>`
   that interest you.

.. tip::

   By default the ANI calculations will use all available cpu on your machine. To run a serial calculation, on the **Details → Technical** panel, set **Number of threads** to **1**. 
   
   On the same panel, you can also choose to run calculations on a CUDA-enabled GPU. See the `parallelization section of the MLPotential manual <../../MLPotential/general.html#cpu-and-gpu-cuda-parallelization>`__ for more details.

References
----------

.. [#refani1ccx]  \J. S. Smith et al., Nat. Commun. 10 (2019) 2903. `<https://doi.org/10.1038/s41467-019-10827-4>`__

.. [#refisol24] \R. Huenerbein et al. Phys. Chem. Chem. Phys. 12 (2010) 6940-6948. `<https://doi.org/10.1039/C003951A>`__

.. [#refreactionenergy] \S. Luo, Y. Zhao, D.G. Truhlar. Phys. Chem. Chem. Phys. 13 (2011) 13683-13689. `<https://doi.org/10.1039/C1CP20834A>`__

.. [#refani1x] \J. S. Smith et al., J. Chem. Phys. 148 (2018) 241733. `<https://doi.org/10.1063/1.5023802>`__

