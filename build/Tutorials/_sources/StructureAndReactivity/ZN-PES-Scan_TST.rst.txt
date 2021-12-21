.. This tutorial has been recorded: examples/tutorials/ts-ziegler-natta
.. Keep the recording in sync so it may be used to generate the images!

.. _AMS_PES_TS_ZN:

Transition state search and characterization of a Ziegler Natta Catalyst
************************************************************************

Introduction
============

Ziegler-Natta catalyzed polymerization
--------------------------------------

In this tutorial, you will learn how to locate the transition state (TS) for the insertion step of ethylene polymerization catalyzed by a homogeneous Ziegler-Natta catalyst.

.. image:: /Images/ZN-PES-Scan/ZN-Thumbnail.png
   :scale: 50 %
   :align: center

Discovered by Karl Ziegler and first applied to polymerization by Giulio Natta, this class of catalysts soon became an industry standard for the production of various polyolefins. Consequently, Ziegler’s and Natta’s work was awarded a Nobel Prize in 1963. Nowadays, the industrial Ziegler-Natta polymerization of polyolefins is among the most important industrial processes.

In the following tutorial, we use the |AMS driver| and |DFTB| to locate and characterize the transition state of a Ziegler-Natta reaction and use these results to calculate an approximate rate constant. You are also encouraged to learn how to reuse these results to expedite follow-up |ADF| calculations for more accurate results.


Strategy
--------

Consider the following Ziegler-Natta reaction:

.. image:: /Images/ZN-PES-Scan/ZNonSingleSite.png
   :scale: 80 %
   :align: center

We will use a two-stage approach to locate the transition state of this reaction:

- Find an initial guess of the TS by scanning the potential energy surface (|PES scan|) along the bonds newly formed during the reaction (we will use a composite coordinate scan).
- Optimize and characterize the initial TS guess (|TS search|).

Geometry Setup with AMSinput
============================

This section shows how to construct the geometry of the ethene-metallocenium (Cp\ :sub:`2`\ Zr\ :sup:`+`\ CH\ :sub:`3`\ - C\ :sub:`2`\ H\ :sub:`4`\) complex in AMSinput.

.. tabs::

  .. tab:: Import geometry from xyz file

    .. rst-class:: steps

        \
         | **1.** Download the :download:`xyz file of the ethene-metallocenium<../downloads/ethene-metallocenium.xyz>` complex
         | **2.** In **AMSinput** select **File → Import coordinates** and select the file you just downloaded
         | **3.** Proceed with the :ref:`engine_settings` section


  .. tab:: Build the structure yourself


    .. seealso::
       If you are not yet familiar with the editing tools in AMSinput, take a look at our Introduction to :ref:`building_structures`.


    .. rst-class:: steps

        \
         | In **AMSinput**
         | **1.** Select the ferrocene structure in the structure tool: |StructTool| **→ Metal complexes → Sandwiches → Ferrocene Sandwich**
         | **2.** Replace Fe with a Zr: **Right-click on the Fe atom → Change atom type → Zr**
         | **3.** Click on the Zr atom, select the **Carbon tool** (|CTool|) and add a carbon atom
         | **4.** Click on **Atoms → Add hydrogens**

    Change the angle between the two benzene rings:

    .. rst-class:: steps

        \
         | **1.** Select one of the dummy atoms in the ring center
         | **2.** **Holding down shift** click on the Zr atom and then on the other dummy atoms in the ring center
         | **3.** Change the **Xx-Zr-Xx** angle to **170** (or use the slider)

    .. image:: /Images/ZN-PES-Scan/ZN-metallocenium-structure.png
       :scale: 50 %
       :align: center

    Finally we can add a ethene molecule:

    .. rst-class:: steps

        \
         | **1.** In the search box |Search| type **ethene**
         | **2.** Select **Molecules → C2H4: Ethene (ADF)**
         | **3.** Position the ethane molecule roughly as shown in the picture below

    .. image:: /Images/ZN-PES-Scan/ZN_ethene_position.png
       :scale: 35 %
       :align: center


    We now want to pre-optimize the structure we just built:

    .. rst-class:: steps

        \
         | **1.** Switch to the **DFTB panel**: |ADFPanel| **→** |DFTBPanel|
         | **2.** Set the **Total charge** to  1
         | **3.** Go to the tab **Model → Solvation** and select **Solvent → Toluene**
         | **4.** Go to the **Main** panel and click on *Pre-Optimize*



.. _engine_settings:

Settings for the Engine
=======================

In the course of this tutorial, the |DFTB| engine with the GFN-1xTB model and implicit Toluene solvation is used. This particular setup provides a good compromise between computational speed and accuracy well suited for this tutorial. Other engines, such as our DFT code |ADF|, will yield more accurate results but will require longer computation time.

Here are possible engine settings for this tutorial

.. tabs::
  .. tab:: DFTB

    For a GFN1-xTB `DFTB <../../DFTB/index.html>`__ calculation with implicit Toluene solvation use the following settings:

    .. rst-class:: steps

        \
         | **1.** Select the **DFTB panel**: |DFTBPanel|
         | **2.** Set the **Total charge** to **1**
         | **3.** Go to the tab **Model → Solvation** and select **Solvent → Toluene**

  .. tab:: ADF

    For a DFT calculation with `ADF <../../ADF/index.html>`__, try the following settings.

    .. rst-class:: steps

        \
         | **1.** Select the **ADF panel**: |ADFPanel|
         | **2.** Set the **Total charge** to **1**
         | **3.** **XC functional → GGA-D → PBE-D4(EEQ)**
         | **4.** **Basis set → DZP**
         | **5.** Go to panel **Model → Solvation**
         | **6.** Select **Solvation method → COSMO**
         | **7.** Select **COSMO Solvent → Toluene**


    The pre-optimized geometries provided throughout this tutorial are optimized with DFTB. Make sure to re-optimize them when you switch to ADF.

    .. tip::
       To just confirm a TS with ADF, do not run a full frequency calculation! Instead use the much faster `PES point characterization <../../AMS/Properties.html#pes-point-character>`__   available under **Properties -> IR (Frequencies) -> Characterize PES point**.

  .. tab:: MOPAC

    For a semiempirical calculation with `MOPAC <../../MOPAC/index.html>`__, we suggest starting with following settings

    .. rst-class:: steps

        \
         | **1.** **Total charge** select **1**
         | **2.** **Method → PM7**
         | **3.** Go to panel **Model → Solvation**
         | **4.** Check the box **Use COSMO**
         | **5.** **Solvent → Toluene**


Settings for the AMS Driver
===========================

First, take a look at the reactants and the product in the following figure to identify the two required scan coordinates:

.. image:: /Images/ZN-PES-Scan/ZN-reactants-products.png
   :scale: 35 %
   :align: center

During the reaction, two bonds will be newly formed:

+ Zirconium-Carbon (between Zr-Ion and the ethene molecule)
+ Carbon-Carbon (between ethene molecule and methyl group)

These two distances will serve as scan coordinates and these will be scanned starting from their present values down to the distance of a typical Zr-C (measured from Zr-Methyl: ~2.3 Å) and Carbon-Carbon single bond (~1.5 Å).

Setup PES scan
--------------

To perform a |PES scan|, change the task in the main panel of the engine:

.. rst-class:: steps

  \
    | **1.** **Task → PES Scan**
    | **2.** Click on |MoreBtn| next to the **Task** to specify the scan settings (or **Model → Geometry Constraints and PES Scan**)

.. image:: /Images/ZN-PES-Scan/ZN-pes-scan-panel.png
   :scale: 35 %
   :align: center

To add a scan coordinate, first select an atom pair

.. rst-class:: steps

  \
    | **1.** Select the Zr (**1**) and C atom (**2**). Hold down **SHIFT** Key for multiple selections.
    | **2.** Press the **+** Button next Zr(..)C(..) distance
    | **3.** Enter ``2.3`` into the second field.
    | **4.** Repeat the process for the two Carbon atoms (**3**) and (**4**).
    | **5.** Enter ``1.5`` into the second field for the Carbon atoms

.. image:: /Images/ZN-PES-Scan/ZN-scan-coords-before.png
   :scale: 60 %
   :align: center

With these settings AMS will scan both coordinates independently, resulting in a 2D projection of the potential energy surface. However, with only one click you can combine the two distances into a single, composite coordinate:

.. rst-class:: steps

  \
    | **1.** Change the **SC-** index for the C-C distance from **2** to **1**
    | **2.** Increase the number of scan points to ``20``

.. note::
   This combination of coordinates implies a concerted formation of bonds. In a situation where this is not known beforehand an independent scan of the two coordinates might yield better results.

.. image:: /Images/ZN-PES-Scan/ZN-scan-coords-after.png
   :scale: 60 %
   :align: center

In the last step, loosen the convergence criteria of the geometry optimizer, since a fully converged path is not required at this point, but only a guess close to the transition state geometry.

.. rst-class:: steps

  \
    | **1.** Click on |MoreBtn| next to **Convergence Details**
    | **2.** Soften the convergence criteria by raising the thresholds to:
    | **-** Gradient Convergence 0.005
    | **-** Energy convergence 5.0e-5

.. image:: /Images/ZN-PES-Scan/ZN-pes-scan-convergence.png
   :scale: 70 %
   :align: center

Now you only need to save and run the calculation. The progress can be monitored with AMSmovie.

.. rst-class:: steps

  \
    | **1.** **File → Save**
    | **2.** **File → Run**
    | **3.** **SCM → Movie**

At runtime, you will see all calculated geometries, including intermediates from the geometry optimizations. Once the PES scan is complete, these intermediates will be hidden. Depending on the AMS version you are using, you might need to close and reopen AMSmovie for this effect to take place. Your plots should roughly look as follows now

.. image:: /Images/ZN-PES-Scan/ZN-pes-scan-result.png
   :scale: 70 %
   :align: center

Use the scroll bar to navigate to the highest energy structure or click on the highest point in the energy curve. This geometry will serve as the initial guess for the transition state optimization!

From AMSmovie, save the structure with the highest energy

.. rst-class:: steps

  \
    | **1.** **File → Save Geometry** and give it the name "TS_initial_guess.xyz"


Transition State search
-----------------------

.. tip::
   To ensure an efficient |TS search| the starting geometry should be close to the expected TS. It furthermore helps to also have a good guess for the local curvature of the potential energy surface, e.g. from a frequency calculation. The Amsterdam Modeling Suite can provide such initial guesses and offers various methods for locating transition states.

   A good overview of further strategies for more specific situations, tips & tricks is given in our slides `Hands-On Transition State Search <https://www.scm.com/news/tips-tricks-for-finding-transition-states-bonding-analysis/>`__.

   See also the `AMS manual page on transition state search <../../AMS/Tasks/Transition_State_Search.html>`__ for more details.

We begin by importing the guess for the transition state saved from the PES scan explained in the previous section into AMSinput.

.. rst-class:: steps

  \
    | **1.** Open a **new AMSinput** window: **SCM → New Input**
    | **2.** Select the **DFTB panel**: |DFTBPanel|
    | **3.** **File → Import Coordinates** and select the "TS_initial_guess.xyz" (the file you exported from AMSmovie in the previous section)
    | **4.** Change **Task** to **Transition State**
    | **5.** Check the **Frequencies** checkbox

.. tip::
   For DFT calculations on large systems, a much faster way of verifying that you found a transition state is the `PES point characterization <../../AMS/Gradients_Stress_Elasticity.html#pes-point-character>`__. This can be enabled in AMSinput in Properties → IR (Frequencies) → Characterize PES point.

The settings for the engine are the same as before: GFN-1xTB with a total charge of 1.0 and implicit Toluene solvation:

.. rst-class:: steps

  \
    | **1.** Set the **Total charge** to **1**
    | **2.** Go to the tab **Model → Solvation** and select **Solvent → Toluene**


.. image:: /Images/ZN-PES-Scan/ZN-TS-search.png
   :scale: 35 %
   :align: center

There exist several (approximate) options for the generation of an initial Hessian that is required for the transition state search. In this case, we shall start from the full Hessian evaluated at the initial guess for the transition state structure. This calculation can be requested with the option **Calculate** in the geometry optimization details panel:

.. rst-class:: steps

  \
    | **1.** Go to **Details → Geometry Optimization**
    | **2.** From the **Initial Hessian** menu, select **Calculate**

.. image:: /Images/ZN-PES-Scan/ZN-TS-search-options.png
   :scale: 70 %
   :align: center


.. rst-class:: steps

  \
    | **1.** File → Save
    | **2.** File → Run

For a well-chosen starting structure, the transition state search should converge to the actual transition state geometry within a few iterations.
Once the calculation is finished, open AMSspectra to inspect the calculated frequencies.

.. rst-class:: steps

  \
    | **1.** SCM → Spectra

.. image:: /Images/ZN-PES-Scan/ZN-TS-search-adfspectra.png
   :scale: 70 %
   :align: center

You should see only a single imaginary frequency indicated by a minus sign in the table of frequencies. If you do, then you have successfully optimized the transition state of this Ziegler-Natta reaction.

.. tip::
   One might encounter additional imaginary modes due to either numerical artifacts or very shallow internal modes. In either case, the corresponding frequencies should be small (i.e. around -5 to -25 cm\ :sup:`-1`\ ), in which case those modes can be ignored.

Results
=======

Energies and barrier height
---------------------------

Once you have optimized a transition state, you can look at the energies to determine the reaction barrier height. You can find the Energy listed in the output file:

.. rst-class:: steps

  \
    | **1.** SCM → Output
    | **2.** Type 'calculation results' into the search field at the bottom, next to the magnifying glass and hit ENTER

.. image:: /Images/ZN-PES-Scan/ZN-TS-search-bond-energy.png
   :scale: 70 %
   :align: center

The Energy for the reactants was already calculated when you ran a geometry optimization of the  ethene-metallocenium (Cp\ :sub:`2`\ Zr\ :sup:`+`\ CH\ :sub:`3`\ - C\ :sub:`2`\ H\ :sub:`4`\)  in the AMSinput Geometry Setup. In the corresponding output file it was found to be E\ :sub:`reactants`\ = -37.6079 Hartree.

The barrier height for this reaction can now be calculated as the difference between these two energies :math:`E_\text{barrier}= E_\text{TS} - E_\text{reactants} =  0.01937 \text{[Hartree]} = 12.26 \text{[kcal/mol]}`

Kinetics and Statistical Thermal Analysis
-----------------------------------------

When asked to calculate frequencies, AMS will automatically calculate some useful  thermodynamic properties such as entropy, internal energy, constant volume heat capacity, enthalpy, and Gibbs free energy from a statistical mechanics partition function. You can find more information on this in the corresponding section of the `AMS manual <../../AMS/Properties.html#thermodynamics-ideal-gas>`__ . For now, we shall use these properties to calculate the rate constant.

Using Gibbs Free Energy of activation we can estimate the rate constant as described by the Eyring-Polanyi equation:

.. math::

  k = \kappa (k_{B}T/h) \cdot \exp \left( \frac{-\Delta G^{‡}}{RT} \right)


with the transmission coefficient :math:`\kappa` assumed to be 1 (By setting :math:`\kappa = 1`, the resulting rate formula is commonly known as the  Transition State Theory rate. This factor corrects for those reactive trajectories that recross the transition state and return without decomposing. It always reduces the reaction rate, so in general :math:`\kappa \le 1`), the rate constant for this single step reaction can be calculated from the Gibbs Free Energy of activation ( :math:`\Delta G^{‡}`).

To calculate :math:`\Delta G^{‡}` we need to know the Gibbs Free Energy of both the transition state and the reactants.

.. image:: /Images/ZN-PES-Scan/ZN-kinetics-Gibbs-Free-E.png
   :scale: 70    %
   :align: center

The Free Energy of the transition state ( :math:`G_{\text{TS}}` ) can be found in the thermodynamic properties section of the TS optimization output file:

.. rst-class:: steps

  \
    | **1.** SCM → Output
    | **2.** Type **Gibbs** into the search field at the bottom, next to the magnifying glass and hit **ENTER**


.. image:: /Images/ZN-PES-Scan/ZN-Gibbs-Free-Energy.png
   :scale: 70 %
   :align: center


.. math::

  G_{\rm{TS}} = -23460.94 \: \textrm{kcal/mol}

For the Gibbs Free Energy of the reactants a frequency calculation has to be carried out. Just download the optimized :download:`ethene-metallocenium<../downloads/ethene-metallocenium.xyz>` structure and run a single point calculation to obtain the frequencies

.. rst-class:: steps

  \
    | **1.** Use same engine settings as with previous calculations
    | **2.** Task -> Single Point
    | **3.** Check the frequencies box under the task menu
    | **4.** Once done, search for **gibbs** in the output file

With a resulting Gibbs Free Energy of

.. math::

  G_{\rm{reacs}} =  -23475.23 \: \textrm{kcal/mol}

the Gibbs Free Energy of activation, :math:`\Delta G^{‡}`, becomes

.. math::

  \Delta G^{‡} =  G_{\rm{TS}} - G_{\rm{reacs}} = 14.29 \: \textrm{kcal/mol}

and the Eyring-Polanyi rate constant at 295.15 K is calculated as

.. math::

  k = 1 \cdot (k_{B}T/h) \cdot \exp \left( \frac{-14.29 \: \textrm{kcal/mol}}{RT} \right) = 214 \, \textrm{s}^{-1}


.. tabs::

      .. tab:: Workflows & Scripting

        This optional section deals with the workflow automation of this tutorial. It assumes basic knowledge about the command line. If you have not used the command line with AMS before, take a look at our information on `how to use the command line <../../Scripting/GettingStarted.html>`__ .

      .. tab:: PLAMS Workflows

        The tutorial splits into two basic steps that can be combined into one but are provided as separate scripts here for the sake of simplicity:

        + :download:`PES-scan.py<../downloads/PES-scan.py>` runs a PES scan and extracts the highest energy structure as xyz file
        + :download:`TS-optimize.py<../downloads/TS-optimize.py>` uses the structure generated by PES-scan.py as initial guess to optimize and characterize the TS.

        To execute the workflow:

        .. rst-class:: steps

            \
                | **1.** Download optimized :download:`ethene-metallocenium<../downloads/ethene-metallocenium.xyz>` complex and place it into an empty directory.
                | **2.** Download :download:`PES-scan.py<../downloads/PES-scan.py>` and :download:`TS-optimize.py<../downloads/TS-optimize.py>` and place into the same directory.
                | **3.** Open the command line and type: ``plams PES-scan.py``
                | **4.** Once the calculation has finished you can run the second script with ``plams TS-optimize.py``

        The scripts are meant to be run after another as the first script generates the input structure for the second script. The results are printed to the command line.

        Some results are printed to the command line. All results are found in the binary **ams.rkf** and **dftb.rkf** results files.

        KF files can be opened and inspected with the GUI program KF Browser. They should only be viewed in Expert Mode:

        .. rst-class:: steps

            \
                | **1.** File → Expert Mode

        The PLAMS scripts provided above demonstrate how to read results from these files.
        A short overview of relevant entries is provided in the tables below.

        The PES scan calculation results are found in the KF file  ``*.results/ams.rkf``

        .. csv-table:: Results in the KF file **ams.rkf**
            :header: "Section", "Variable", "Meaning"

            "PESScan", "nScanCoord", "Number of independently scanned coordinates"
            "PESScan", "nPoints(1-nScanCoord)", "Number of points scanned for every scan coordinate"
            "PESScan","RangeStart(1 until nScanCoord)","Starting values for scan coordinate 1 (in Bohr)"
            "PESScan","RangeEnd(1 until nScanCoord)","End values for scan coordinate 1 (in Bohr)"
            "PESScan","PESCoords","Coordinates of the PES (in Bohr)"
            "PESScan","PES","Energies of the PES scan (in Hartree)"
            "PESScan","History Indices","Index of PES point geometries in section History"

        The frequencies calculated after the transition state optimization are found in the engine specific results file. For DFTB this file is called ``*.results/dftb.rkf``:

        .. csv-table:: Results in the KF file **dftb.rkf**
            :header: "Section", "Variable", "Meaning"

            "AMS results", "Energy", "Final energy of the TS (in Hartree)"
            "Vibrations","Frequencies","Sorted list of final frequencies (in cm-1)"

      .. tab:: Run scripts

            The calculations can be run directly from a console input by executing the following run scripts:

            + :download:`ZN-PES-Scan.run<../downloads/ZN-PES-Scan.run>` for the PES scan
            + :download:`ZN-TS-Opt.run<../downloads/ZN-TS-Opt.run>` for the Transition State optimization

            To run the scripts from the command line use the following commands

            .. rst-class:: steps

                \
                  | **1.** chmod +x ZN-PES-Scan.run
                  | **2.** ZN-PES-Scan.run > ZN-PES-Scan.out
                  | **3.** chmod +x ZN-TS-Opt.run
                  | **4.** ZN-TS-Opt.run > ZN-TS-Opt.out

            The results are then found in the corresponding output files ZN-PES-Scan.out and ZN-PES-TS-Opt.out

            .. note::

               If you running the scripts produces an error like ``/bin/sh^M: bad interpreter: No such file or directory``, you need to convert the .run script from Windows to Unix line endings first. You can easily do that with ``dos2unix ZN-PES-Scan.run``.



.. |AMS driver| replace:: `AMS driver <../../AMS/index.html>`__

.. |ADF| replace:: `ADF <../../ADF/index.html>`__

.. |DFTB| replace:: `DFTB <../../DFTB/index.html>`__

.. |PES scan| replace:: `PES scan <../../AMS/Tasks/PES_Scan.html>`__

.. |TS search| replace:: `transition state search <../../AMS/Tasks/Transition_State_Search.html>`__
