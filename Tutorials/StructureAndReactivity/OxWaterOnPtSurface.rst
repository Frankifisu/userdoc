.. _AMS_OxWaterOnPtSurface:

Oxidation of water on a Pt(111) surface
**********************************************************************

This tutorial will teach you how to

* Optimise the lattice constants of a bulk material, cut a surface from it and optimize adsorbates
* Do a thermochemical analysis for |H2| and use these properties to estimate the potential for water oxidation over a Pt(111) surface

If at any point during the tutorial calculations fail, please consult the troubleshooting sections of either `BAND <../../BAND/Troubleshooting/TOC.html>`__ or `ADF <../../ADF/Rec_problems_questions/Rec_problems_questions.html>`__.

Bulk Pt
===============================================

We begin by setting up a geometry optimization job to build and optimize bulk Pt(111).

To create the Pt lattice structure

.. tabs::
  
  .. tab:: Import geometry from xyz file
    
    .. rst-class:: steps
    
      \
        | **1.** Download the :download:`xyz file of bulk Pt<../downloads/PtBulk.xyz>`
        | **2.** In **AMSinput** select **File** |arrow| **Import Coordinates** and select the downloaded file

  .. tab:: Build a new structure
    
    .. seealso::
      If you are not familiar with the editing tools in **AMSinput**, take a look at our introduction to :ref:`building_structures`. Also refer to our introduction to :ref:`Crystals_Surfaces` for more information on how to build crystals and lattice structures.
  

    .. rst-class:: steps
      
      \
        | In **AMSinput**
        | **1.** Switch to the **BAND panel**: |ADFPanel| |arrow| |BANDPanel|
        | **2.** Click the |CrystalTool| button and select **Cubic** |arrow| **fcc**
        | **3.** Select **Pt** under **Presets**

    .. image:: /Images/OxWaterOnPtSurface/OxWater_PtCrystal.png
       :scale: 50 %
       :align: center

    .. hint::
      Using the **Periodic display** |PeriodicViewTool| you can get a better view of the system you are creating using the crystal manipulation tools offered by **BAND**.
       

For the geometry optimization we will use the **revPBE-D4(EEQ) XC-functional**:

.. rst-class:: steps
  
  \
    | In the **Main panel**
    | **1.** Select **XC functional** |arrow| **GGA-D** |arrow| **revPBE-D4(EEQ)**
    | **2.** Select **Task** |arrow| **Geometry Optimization**
    | **3.** Set **Relativity (ZORA)** to **Scalar**
    | **4.** Click the |MoreBtn| button next to **Task** or in the **panel bar** open **Details** |arrow| **Geometry Optimization**
    | **5.** Check the **Yes** checkbox next to **Optimize lattice**

We can now run the calculation using **File** |arrow| **Run**. This will prompt you to save the job somewhere if you have not saved it already. The progress can be viewed in the log file viewer (**SCM** |arrow| **Logfile**)

Once the calculation has finished, a pop-up will appear asking you to read in the new coordinates. Click **Yes**.
Under **Model** |arrow| **Lattice** you can find the new lattice constant. Check that it is close to the literature value of (3.92 |angstrom|). You can try to see for yourself that omission of relativistic effects will cause the lattice to expand quite significantly. For more accurate relativistic effects, one could employ spin-orbit coupling effects as well, however these are more computationally demanding. You can visualize the band structure and density of states (DOS) by clicking on **SCM** |arrow| **Band Structure** and **SCM** |arrow| **DOS** respectively while in the output viewer.




|OH| and |H2O| on a Pt(111) surface
=====================================

Next we cut a (111) surface from the optimized bulk structure.

.. tabs::

  .. tab:: Import geometry from xyz file
    
    .. rst-class:: steps
    
      \
        | **1.** Download the :download:`xyz file<../downloads/PtSlab.xyz>` of the Pt(111) surface
        | **2.** In **AMSinput** select **File** |arrow| **Import Coordinates** and select the downloaded file
  
  .. tab:: Build the Pt slab yourself

    .. rst-class:: steps

      \
        | Starting from the optimised bulk Pt lattice structure
        | **1.** Click the |SliceTool| button or choose in the **menu bar**, **Edit** |arrow| **Crystal** |arrow| **Generate Slab**
        | **2.** Click the **Convert To Conventional Cell** button
        | **3.** Enter ``1`` ``1`` ``1`` for the **Miller indices** field
        | **4.** Enter ``3`` in the **Number of layers** field
        | **5.** Click the **Generate Slab** button
        | **6.** Click |CrystalTool| |arrow| **Convert To Conventional Cell**


Save this as a new file and run a single point calculation (change the **Task** from **Geometry Optimization** to **Single Point**) using the same settings as before.

Now we will put one monolayer (ML) of |OH| on the surface in the top position and set up the run.

To set up the geometry:

.. tabs::

  .. tab:: Import geometry from xyz file

    .. rst-class:: steps

      \
        | **1.** Download the :download:`xyz file<../downloads/PtSlabOH.xyz>` of the |OH| monolayer on a Pt(111) surface
        | **2.** In **AMSinput** select **File** |arrow| **Import Coordinates** and select the downloaded file

  .. tab:: Build the |OH| monolayer yourself
    
    .. rst-class:: steps
  
      \
        | **1.** Select a top Pt atom and click on the |OTool| button
        | **2.** Click somewhere above the surface to add an oxygen atom
        | **3.** Press Esc to exit the O-building tool
        | **4.** Go to the **Model** |arrow| **Coordinates** panel and move the oxygen atom to ``0`` ``0`` ``2`` |angstrom|
        | **5.** Press Ctrl/Cmd + E or click **Atoms** |arrow| **Add Hydrogens** to add hydrogens to the system

    The new structure should look something like this:

    .. image:: /Images/OxWaterOnPtSurface/OxWater_PtSlabOH.png
      :scale: 50 %
      :align: center

And to set up the calculation:

.. rst-class:: steps
  
  \
    | **1.** Go to the **Main panel** and select **Geometry Optimization** as **Task**
    | **2.** Click the |MoreBtn| button next to **Task** or in the **panel bar** open **Details** |arrow| **Geometry Optimization**
    | **3.** Deselect the **Yes** checkbox next to **Optimize lattice**
    | **4.** Select the Pt atoms by clicking them while holding Shift
    | **5.** In the **panel bar**, select **Model** |arrow| **Geometry Constraints and PES Scan** and press the top |AddButton| (fixed position) button to freeze the atoms in place


Run the job. It will take a few cycles to finish. In the meantime we will prepare the optimization for a monolayer of water on Pt(111).

.. tabs::

  .. tab:: Import geometry from xyz file
    
    .. rst-class:: steps

      \
        | **1.** Download the :download:`xyz file<../downloads/PtSlabH2O.xyz>` of the |H2O| monolayer on a Pt(111) surface
        | **2.** In **AMSinput** select **File** |arrow| **Import Coordinates** and select the downloaded file


  .. tab:: Build the |H2O| monolayer yourself

    .. rst-class:: steps
      
      \
        | **1.** In the |OH| @Pt(111) window, select both the top Pt and O atom (holding shift).
        | **2.** Change the Pt-O distance to ``280`` pm (2.8 |angstrom|) by typing it in the white box at the bottom of the molecule drawing area, or use the scroll bar just below it.
        | **3.** Select the Pt-O bond and click Delete to remove the bond.
        | **4.** Add another hydrogen to the oxygen atom to form |H2O|..
        | **5.** In the **panel bar**, select **Model** |arrow| **Coordinates** and edit the hydrogenic coordinates to read ``0`` ``0`` ``3.8`` and ``0`` ``1`` ``2.5`` |angstrom|.
        
    .. image:: /Images/OxWaterOnPtSurface/OxWater_PtSlabH2O.png
      :scale: 50 %
      :align: center


Note that neither the 1 ML |H2O| nor the |OH| geometries are physically (chemically) meaningful. Water will typically adopt a hexagonal bilayer structure. Check out the references at the end of the tutorials for a starting point on more realistic geometries.

Save as a different file and run the job. The |OH| calculation should be done by now, but the |H2O| calculation will take slightly longer than the |OH| one. In the meantime, we will prepare calculations on free |H2|, |H2O| and |OH|, so that we can calculate their thermodynamic properties using ADF.

|H2|, |H2O| and |OH| molecules
================================

We now continue with calculations on free H2, H2O and OH molecules. The general workflow is as follows:

.. rst-class:: steps

  \
    | **1.** Open a new AMSinput window and ensure that you are in the |ADFPanel| panel
    | **2.** Click the |HTool| button and click anywhere in the molecule drawing area to place a hydrogen atom
    | **3.** With the first hydrogen selected, press anywhere else to create |H2|
    | **4.** Preoptimize the molecule by pressing the |PreOptimTool| button at the bottom of the molecule drawing area. By right-clicking you may choose a different engine for preoptimization
    | **5.** In the **Main Panel**, select **XC-functional** |arrow| **GGA-D** |arrow| **revPBE-D4(EEQ)**
    | **6.** Select **Relativity** |arrow| **Scalar**
    | **7.** Set **Task** to **Geometry Optimization** and check the **Frequencies** checkbox below **Task**

Selecting **Frequencies** will ensure that vibrational and thermodynamic properties of the systems are also calculated.

.. image:: /Images/OxWaterOnPtSurface/OxWater_H2O.png

Run the job and repeat for |H2O| and |OH| by changing the structure of the molecule. For the |OH| calculation, please note that |OH| is a radical (doublet) species and you should ensure that you select the **Unrestricted** checkbox in the **Main panel** and enter ``1`` in the **Spin polarization** field.


Estimated water oxidation potential on Pt(111) surface from thermodynamical properties
=========================================================================================

We now have all the pieces available to estimate the minimum potential at which water can get oxidized over a Pt(111) surface:

.. math::
  \text{H}_2\text{O}^* \rightarrow \text{OH}^* + \text{H}^+ + \text{e}^-

where the starred species denote adsorbed molecules on the Pt(111) surface. Following Nørskov et al. (J. Phys. Chem. B, **108**, 17886-17892 (2004)) we choose the standard hydrogen electrode as a reference potential, such that 

.. math::
  \text{H}_2(g) \rightleftharpoons 2\text{H}^+ + 2\text{e}^-

is in equilibrium. 
We get the overall reaction

.. math::
  \text{H}_2\text{O}^* \rightarrow \text{OH}^* + \frac{1}{2} \text{H}_2

The free energy of the reaction is then:

.. math::
  \Delta G = \Delta G(\text{OH}^*) + \frac{1}{2} \Delta G(\text{H}_2(g)) - \Delta G(\text{H}_2\text{O}^*)

The electrode potential :math:`U` is incorporated as a linear energy shift :math:`qU = -U \text{eV}` for every electron, giving

.. math::
  \Delta G(U) = \Delta G(\text{OH}^*) + \frac{1}{2} \Delta G(\text{H}_2(g)) - \Delta G(\text{H}_2\text{O}^*) + eU

As a first approximation for the Gibbs free energies of |OHstar| and |H2Ostar| we will just use the formation energies (from the atomic fragments). By far the largest contribution to the (difference in the) thermodynamic properties of the adsorbed species will be the zero-point energies (ZPEs), which can be crudely estimated from the gas phase frequency calculations for |OH| and |H2O|.

From the log file of the |OH| and |H2O| on Pt(111), write down the energy of formation near the end. (If necessary, look in the list of jobs in the AMSJobs window and click on the triangle in front of the job name so that all related files are listed. Double click on the .logfile files to open the appropriate logfile.)

.. math::
  E(\text{OH}^*) = -26.8375 \text{ eV} \\
  E(\text{H}_2\text{O}^*) = -30.3399 \text{ eV}

from the |H2| geometry optimization:

.. math::
  E(\text{H}_2) = -6.6884 \text{ eV}

For the rotation and vibration contributions to :math:`\Delta G(\text{H}_2)`, we examine the more detailed output file (.out or **Output** from the **SCM** menu). The menu bars for the output viewer enable quick jumping through the calculation output. In this case we want the Gibbs free energy from  **Statistical Thermal Analysis** which is located in the **Other Properties menu**.

.. math::
  \Delta G^{298.15}(\text{H}_2(g)) = -6.7060 \text{ eV}

and thus:

.. math::
  \Delta G(U) = 0.1494 \text{ eV} - eU

Consequently, the reaction over a Pt(111) layer will only take place when :math:`\Delta G < 0`. This is only true when we set the potential to at least :math:`U = 0.1494 \text{ V}`.

The calculated value is quite far from the experimental value of 0.8 V (Markovic and Ross, Surf. Sci. Rep. **45**, 117 (2002)). Will including ZPE effects improve things? No: look in the output of the frequency calculations **Other Properties** |arrow| **Zero-Point Energy**: 

.. math::
  \text{ZPE}(\text{H}_2\text{O}(g)) = 0.5306 \text{ eV} \\
  \text{ZPE}(\text{OH}(g)) = 0.2041 \text{ eV}

so that the estimated :math:`\Delta\text{ZPE} = -0.3265 \text{ eV}` for the gas phase species. Therefore, including :math:`\text{ZPE}` would make it easier to oxidize water over Pt(111), reducing the oxidation potential.
However, if you have some time left at the end of this tutorial, you can convince yourself that lower coverages will improve agreement with experiment: 

Supercells for lower adsorbate coverage
==========================================

.. rst-class:: steps

  \
    | Starting from the Pt(111) slab
    | **1.** In the **menu bar**, select **Edit** |arrow| **Crystal** |arrow| **Generate Super Cell**
    | **2.** In the **Preset** drop-down menu, select the **sqrt(3) x sqrt(3)** option and click the OK button
    | **3.** Add a |OH| or |H2O| group in the same way as done before
    | **4.** Freeze the Pt atoms in the same was as before

Alternatively, you could have started from the optimized |OHstar| and |H2Ostar| 1 ML structures, making supercells from these and then removing two adsorbate molecules in the super cell. In this way we create a cell which has a third of the coverage of the 1ML layer.

These calculations should take about 2 and 6 hours to complete, so just run them overnight and read back the last formation energies from the logfile when you return tomorrow. These values (-77.9892 and -82.2107 eV for |OH| and |H2O| respectively) predict a much better water oxidation potential of about 0.8685 eV (with the same estimated gas phase :math:`\Delta \text{ZPE}`). 


.. image:: /Images/OxWaterOnPtSurface/OxWater_PtSupercellOH.png


Note
======

that this tutorial was just a short introduction to illustrate the calculation of thermodynamical properties of electrochemical half-reactions. In general for these kind of calculations you would want to converge carefully with respect to basis set, k-point sampling, and slab thickness. One should also carefully consider the adsorption geometry, e.g. water will want to form hexagon overlayers (necessitating √3 x √3 supercells).

All this goes too far to cover in a short tutorial session, but there are plenty of good literature examples where they have carefully considered these and more subtleties involved in these kind of calculations. Useful starting point are the papers by Nørskov and coworkers, for instance addressing oxygen reduction (`2004 <https://pubs.acs.org/doi/10.1021/jp047349j>`_) and water redox reactions on Pt(111) (`2006 <https://pubs.acs.org/doi/10.1021/jp0631735>`_).

BAND can also perform frequency calculations (more computationally demanding than ADF), so that ZPE effects can also be included for the adsorbed species rather than estimated from the gas phase.
Finally, note that in BAND, uniquely, both solvation effects (COSMO) and homogeneous electric fields can be included properly (true 2D periodic systems). Both these effects will influence the adsorbate energies, and thereby the calculated oxidation potential. 


.. |H2| replace:: H\ :subscript:`2`
.. |H2O| replace:: H\ :subscript:`2`\ O
.. |H2Ostar| replace:: H\ :subscript:`2`\ O*
.. |OHstar| replace:: OH*
.. |OH| replace:: OH
.. |angstrom| replace:: Å
.. |arrow| replace:: **→**
