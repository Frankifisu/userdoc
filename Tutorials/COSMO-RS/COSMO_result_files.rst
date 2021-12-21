.. _crs1:

COSMO result files
******************

If you already have COSMO result files for all the compounds that you are interested in you can skip this tutorial, without problems of continuity. For example, ADF has a database of COSMO result files, the `COSMO-RS compound database ADFCRS-2018 <../../COSMO-RS/COSMO-RS_Databases.html>`__.

The purpose of this tutorial is to teach you how to make data for a compound using the ADF program such that it can be read by COSMO-RS. COSMO-RS expects so called COSMO result files, which are results of quantum mechanical calculation using COSMO. In ADF such a COSMO result file is called a TAPE21 (.t21) file, RKF (.rkf), or a COSKF (.coskf) file. For example the `COSMO-RS compound database ADFCRS-2018 <../../COSMO-RS/COSMO-RS_Databases.html>`__ consists of .coskf files. In other programs such a file can be a .cosmo file. For example, at `https://apps.che.vt.edu/Liu-2013/VT-Databases.html <https://apps.che.vt.edu/Liu-2013/VT-Databases.html>`__  a database of .cosmo files can be found, which were made with a different program. Note that the optimal COSMO-RS parameters may depend on the program chosen.

Please read through the first GUI tutorial before starting with this tutorial.
Even better: try using the AMS-GUI yourself, especially :ref:`the Getting started Tutorial<GO_ETHANOL>`.

In this tutorial an ADF COSMO result file, a MOPAC COSMO result file, and a Fast Sigma (using QSPR) COSMO file is made.
For ADF COSMO-RS calculations the recommended choice is to use ADF COSMO result files.
For very fast calculations, in which one avoids doing a quantum mechanical calculation for a compound, the Fast Sigma method is recommended.

Step 1: Start AMSinput
======================

For this tutorial we prefer to work in a separate directory, for example a directory called Tutorial, as was explained in :ref:`the Getting started Tutorial<GO_ETHANOL>`.

Start :ref:`AMSjobs<ADFJOBS>` (in your home directory), and move to the Tutorial directory:

.. rst-class:: steps

  \
    | Start amsjobs
    | If the Tutorial directory does not exist, **File → New Directory**, and create a directory called Tutorial
    | Click on the Tutorial folder icon

Next start AMSinput using the SCM menu.

.. rst-class:: steps

  \
    | Select the **SCM → New input** menu command.

Step 2: Create the molecule
===========================

First we construct a water molecule, and preoptimize its geometry:

.. rst-class:: steps

  \
    | Select the O-tool by clicking on the button with the 'O'
    | Click somewhere in the drawing area to create an oxygen atom
    | Select the select-tool by clicking on the button with the arrow
    | Click once in empty space so nothing is selected
    | Select **Atoms → Add Hydrogen**
    | Click the preoptimizer button |PreOptimTool|
    | Symmetrize the system by clicking on |SymmTool|

Note that ADF does not symmetrize molecular coordinates by default anymore, which it used to do (ADF<=2019).
By symmetrizing the system ADF will use symmetry.
Your water molecule should look something like this:

.. image:: /Images/COSMO_result_file/t1_wateramsinput.png
   :width: 5 cm

Step 3: ADF COSMO result file
=============================

The next step is to optimize the gas geometry using ADF, and perform the ADF COSMO calculation at the optimized gas phase geometry,
using **Task: COSMO-RS Compound**. Note that this task is now at a different location than in ADF2019.

.. rst-class:: steps

  \
    | On the **main panel**, set **Task → COSMO-RS Compound**

.. image:: /Images/COSMO_result_file/t1_watergo.png
   :width: 10 cm

For your information, the proper settings for the gas phase geometry optimization are: the Becke Perdew exchange correlation functional (GGA:BP86), use of the scalar relativistic ZORA Hamiltonian, a TZP small core basis set (for Iodine a TZ2P small core basis set), and an integration accuracy with a good quality.
Like for Iodine for heavier elements than Krypton, a TZ2P small core basis set is recommended. Note that these settings were used for the optimization of the COSMO-RS parameters.

With the proper options selected, now run ADF:

.. rst-class:: steps

  \
    | Select **File → Run**
    | In the file select box, choose a name for your file (for example 'water')
    | and click 'Save'

Now ADF will start automatically, and you can follow the calculation: AMSjobs will show the progress of the calculation with the last few lines of the logfile.

.. rst-class:: steps

  \
    | Wait until the optimization and ADF-COSMO calculation are ready (should take very little time)
    | Click 'Yes' in the pop-up to read the coordinates from a .rkf file.

Now the geometry of the water molecule is the optimized one, and the ADF COSMO calculation has been performed. The result file water.coskf, which is an ADF COSMO result file, can be used as input for a COSMO-RS calculation.

Note that a .coskf file is not a complete .rkf file. For example, if one has such a .coskf file, only the COSMO surface charge density can be viewed with AMSview. Thus a .coskf file is mostly useful for COSMO-RS calculations.

More details on parameters used in the COSMO calculation can be found in the run script: **Details → Run Script**. See also `the COSMO-RS manual <../../COSMO-RS/index.html>`__.

Step 4: Lowest Conformer
========================

The AMS-GUI does have some basic support for handling conformers.
This includes the generation of conformers and the refinement of conformers using different theoretical methods,
see the :ref:`AMS-GUI tutorial on Conformers <Conformers>` for more details.
In the step in this tutorial that does a refinement of the structures of the conformers
one can use ADF with the Task 'COSMO-RS Compound'.
Next one can select the conformer with the lowest energy to be used as an ADF COSMO result file.

Note that this step does not involve a calculation, but only shows one way to find the lowest conformer.

Step 5: Polymers
================

The AMS-GUI supports the making of a polymer. However, the calculation of a full polymer is very expensive.
Instead of this very expensive calculation, here an "average monomer" COSMO result file is calculated.
The full polymer result could then be calculated by multiplying the "average monomer" result by a factor equal to the number of repeat units in the polymer.

In practice a trimer is calculated from 3 units of the monomer, in which the trimer is capped with 2 methyl groups.
Next an ADF COSMO result file is generated, in which only the COSMO charges of the center monomer will be used in the COSMO-RS calculations.


.. rst-class:: steps

  \
    | Select the **SCM → New input** menu command.
    | Select **Edit → Polymer...**
    | Click the **Add monomer:** search box
    | Enter 'styrene' (without quotes)

.. image:: /Images/COSMO_result_file/t1_polymerbuilder.png
   :width: 5 cm

.. rst-class:: steps

  \
    | Select 'styrene' from the pull-down menu

This will create a Polystyrene monomer. The 2 dummy atoms will later be replaced with 2 other monomers to form a Polystyrene trimer.

.. image:: /Images/COSMO_result_file/t1_styrenemonomer.png
   :width: 5 cm

Next we will not use the Polymer builder window, but instead use a specialized button that generates a trimer, adds 2 methyls as capping groups, and selects the center monomer atoms as so called 'COSKF atoms'.

.. rst-class:: steps

  \
    | Click the **Close** button at the bottom of the Polymer builder window
    | Select **Task → COSMO-RS Compound**
    | Go to the **Model → Solvation** panel
    | Click the 'COSKF trimer:' **Generate** button

.. image:: /Images/COSMO_result_file/t1_styrenetrimer.png
   :width: 10 cm

If one would select **File → Run** an "average monomer" COSMO result file would be created, which an be used for polymer calculations.
The calculation can take up quite some time, therefore we skip this part in this step.

Step 6: MOPAC COSMO result file
===============================

MOPAC is a faster method than ADF for the generation of COSMO result files. However, we recommend to use the Fast Sigma method described in the next step if you want get an estimate of a COSMO result file very quickly and which has a better quality.

A MOPAC COSMO result file can be created in almost the same way as an ADF COSMO result file.  We will change the program from ADF to MOPAC, and select the COSMO solvation method.

.. rst-class:: steps

  \
    | Select the **SCM → New input** menu command.
    | Create a water molecule
    | Select |ADFPanel| **→** |MopacPanel|
    | Select **Model → Solvation**
    | Tick the **Use COSMO** checkbox
    | Select **CRS** from the **Solvent** dropdown menu


.. image:: /Images/COSMO_result_file/t1_watermopacmenu.png
   :width: 10 cm

For sake of clarity we will save the COSMO calculation under a different name, and run the calculation

.. rst-class:: steps

  \
    | Select the 'Save As...' command from the 'File' menu
    | In the file select box, choose 'water_mopac' as name for your file and click 'Save'
    | Select **File → Run**
    | Wait until the optimization is ready (should take very little time)
    | Click 'Yes' in the pop-up to read the coordinates from a .rkf file.

After the calculation has finished the file water_mopac.results/mopac.coskf, which is a MOPAC COSMO result file, can be used as input for a COSMO-RS calculation.

Note that MOPAC is a semi-empirical quantum chemistry program, whereas ADF is based on density functional theory (DFT). Thus the MOPAC COSMO result files will not be of the same quality as the ADF COSMO result files.


Step 7: Fast Sigma: QSPR COSMO result file
==========================================

A QSPR (Quantitative Structure-Property Relationship) estimated COSMO result file (in fact a COSMO-RS sigma-profile) can be created without doing a quantum mechanical calculation.
This very fast QSPR method, which is called Fast Sigma, can provide estimates of COSMO-RS sigma profiles in milliseconds.
This allows for a drastically expedited search through candidate molecular structures as compared to the full-fledged COSMO-RS strategy, which needs QM calculations that will take much longer.
Input required is a SMILES string or a compound on a .xyz file. Here we will use as compound Ibuprofen, which has SMILES string ``CC(Cc1ccc(cc1)[C@@H](C(=O)O)C)C``.

.. rst-class:: steps

  \
    | Select the **SCM → COSMO-RS** menu command.
    | Select **Compounds → List of Added Compounds**
    | Enter ``CC(Cc1ccc(cc1)[C@@H](C(=O)O)C)C`` for
    | **Add Compound using QSPR (Fast Sigma) → SMILES**
    | Select the **Add** button at the right of the SMILES string
    | In the pop-up in the file select box, choose a name for your file (for example 'ibuprofen')

.. image:: /Images/COSMO_result_file/t1_ibuprofengcmenu.png
   :width: 10 cm

In the right part of the COSMO-RS GUI window one should see something like:

.. image:: /Images/COSMO_result_file/t1_ibuprofengc.png
   :width: 10 cm

Fast Sigma does not create a COSMO surface, but creates a so called sigma-profile, which can be used in COSMO-RS calculations.
The parameters in Fast Sigma are fitted to COSMO-RS sigma-profiles of organic closed shell neutral molecules.
The created sigma-profile can not be used in COSMO-SAC calculations.
The created file contains a SMILES string, thus it can be used in UNIFAC calculations.
Not recommended to be used for radicals or charged molecules.

One can visualize the molecule in 2D (a .html file will be created) with

.. rst-class:: steps

  \
    | Press 'Show 2D' at the top of the right window
    | In the pop-up in the file select box, choose a name for your html file (for example 'ibuprofen')

.. image:: /Images/COSMO_result_file/t1_ibuprofenhtml.png
   :width: 10 cm

Openbabel is used to translate the SMILES string into a picture.

