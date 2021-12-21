Multiple molecules, conformers, multiple methods
************************************************

The AMS-GUI can handle multiple molecules, or multiple methods, or both, with one relatively simple setup.
It also can generate and handle conformers. The handling of the conformers is actually an example of handling multiple molecules at once.


.. _MultipleMolecules:

Multiple molecules
==================

With AMSinput you can set up a calculation, and then run your set up for multiple molecules automatically.
At run time the molecules are then taken from an .sdf file that has the same name as your .ams file (except for the extension obviously).
This SDF file may come from somewhere else, from a Conformer-generation job for example, or you can actually create and edit multiple molecules
inside AMSinput.

After the calculation the result is a new .sdf file. That .sdf file is a standard SDF file, with the calculated energy in the title for each molecule.
It also contains references to the calculation results for the individual molecules.
And it may contain some extra information per molecule (depending on the calculation).

As an example, let's calculate the H-NMR spectra for methane and ethane with one single set-up.

Step 1: Set up methane and ethane in AMSinput
---------------------------------------------

.. rst-class:: steps

  \
    | Start AMSinput
    | Create methane

Next we will add an extra molecule (ethane) to AMSinput:

.. rst-class:: steps

  \
    | Use the **Edit → New Molecule** menu command
    | Create ethane
    | Switch between the two molecules using the arrows at the bottom
    | Adjust the names of the molecules to methane and ethane (click on the name, it becomes editable)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-twomolecules.png


Step 2: H-NMR calculation
-------------------------

Next we will set up the calculation of an H-NMR:

.. rst-class:: steps

  \
    | Go to the NMR panel (in the Properties section)
    | Check the Shielding for all H atoms check box
    | Use the **File → Run** menu, save your job as NMR
    | When asked to run all 2 molecules, click Yes

In the AMSjobs window you should see the job running.
Also note that it gives you the information that the job uses the nmr.sdf file.
When you open the job you will see the results for two different molecules in the .results folder:

.. rst-class:: steps

  \
    | Wait for the calculation to finish
    | Click on the triangle before the job name to see the files belonging to that job

.. image:: /Images/MultipleMoleculesConformersMethod/t13_results_twomolecules.png

Use AMSspectra to see the calculated NMR spectra.
When opening the job, it will show an averaged spectrum. Use the View menu to adjust what curves to see:

.. rst-class:: steps

  \
    | **SCM → Spectra**
    | In the AMSspectra window: **View → Average/All Curve**
    | Change the width of peaks to 0.01

.. image:: /Images/MultipleMoleculesConformersMethod/t13_spectra_twomolecules.png

You can also open the result files for the individual calculations:

.. rst-class:: steps

  \
    | In AMSjobs click once on results/mol_1.results/adf.rkf to select it
    | **SCM → Spectra**
    | Change the width of peaks to 0.01


.. image:: /Images/MultipleMoleculesConformersMethod/t13_spectra_onemolecule.png

.. rst-class:: steps

  \
    | Close AMSinput and AMSspectra

.. _Conformers:

Conformers
==========

The AMS-GUI does have some basic support for handling conformers.
This includes the generation of conformers, the refinement of conformers using different theoretical methods,
and the calculation of properties like spectra (UV/Vis, IR, NMR, and others).
These spectra are the weighted spectra of the individual conformers, typically using a Boltzmann weighting.

The different conformers are stored in a .sdf file. The conformer handling is an example of handling multiple molecules.

The main steps to follow are:

+ Generate and view the conformers (and thus the .sdf file that contains them)

+ Refine the structures of the conformers, for example with ADF

+ Calculate the spectrum of interest for selected conformers

+ View the Boltzmann averaged spectrum

Each step will do something for all (or the selected) conformers.
At the end of each step a new .sdf file is generated based on the results of the calculations.
The original .sdf file is kept in the .results directory, with a timestamp, as a backup.

For this tutorial we will do this for a small example molecule: propanoic acid.

Step 3: Set up propanoic acid in AMSinput
-----------------------------------------

.. rst-class:: steps

  \
    | Start AMSinput
    | Build propanoic acid (or search using the AMSinput search |Search|)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-propanoic-acid.png

Step 4: Generate the conformers
-------------------------------

.. rst-class:: steps

  \
    | Switch to the Conformers mode (use the orange ADF pull-down menu, used to switch methods)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformers.png

In this panel you set up how to generate the conformers (using RDKit).

The defaults should work fine: generate 600 random conformations, filter them with an RMS filter to avoid duplicate structures.
Next optimize with RDKit-UFF so each conformation runs into some local minimum (conformer), and again filter with an RMS filter to avoid duplicate structures.

Note that the starting geometry does not matter, RDKit just looks at the connectivity and not at atom positions.
The conformations are generated using distance-geometry conformation generator. For more info, see the `RDKit web site <http://www.rdkit.org/>`__.

.. rst-class:: steps

  \
    | Use **File → Run** (and save your molecule as 'propanoicacid')
    | Wait until the job is ready
    | In AMSjobs check that the propanoicacid job now contains a .sdf file (propanoicacid.sdf)
    | Use the **SCM → Movie** menu to view the conformers (it will automatically load the .sdf file)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-energy.png

Using AMSmovie you can now examine the generated conformers. Note that the energy is the UFF energy as calculated by RDKit.

Step 5: Refine the conformer geometries with ADF
------------------------------------------------

Next step is to improve the geometries of the conformers.
If there are many conformers this may be expensive, so you may want to limit the conformers to be optimized to those with a certain energy range from the lowest conformer.
Note that this energy range is a crude estimate by UFF. In the AMSmovie window you can see the energies of the conformers.

.. rst-class:: steps

  \
    | Close the AMSmovie window
    |
    | In the AMSinput window switch to ADF mode and select the **Geometry Optimization** task
    | Switch to the Coordinates panel in the Model section
    | Use 'Selected File'
    | Select the propanoicacid.sdf file in the 'Molecule from' field
    | Go to the 'SDF Filter' panel under the Details tab
    | Select all conformers with energy below 10 kcal/mol
    |
    | Set the post-processing options: Sort, Remove duplicates between 0.1 Angstrom, and Align
    |
    | Other options: move the mouse over them and check the balloons, the default values are correct

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-panel.png

These settings in the Coordinates panel will run your job (whatever you specify in AMSinput to do, a geometry optimization right now) for all selected conformers
(in the SDF filter panel): the conformers within 10 kcal/mol from the lowest conformer. In this case that is all conformers we have.
If you have many conformers you may wish to restrict the energy range to reduce computation time.

The Use 'Selected File' option will create a job for the geometry/geometries in the selected file. In this example a .sdf file is used with multiple molecules,
but you could also have selected any other file that the AMS-GUI knows and which contains a molecule (a .t21, .rkf, .xyz, ...).

If you would not have adjusted the options in the Coordinates panel, AMSinput will note that an .sdf file is present when saving the job.
It will ask you if you want to use it or not.

After the calculations have been done, a new .sdf file will be created, the conformers will be sorted (by energy), filtered to avoid duplicates, and aligned.
Normally you would use a better basis set, but for the tutorial we stick to the DZ basis set (to get some results fast).

.. rst-class:: steps

  \
    | Save your setup as propanoicacid_ADF
    | Run your setup **File → Run**
    |
    | Once the job is running, follow it with AMSmovie (in AMSjobs **SCM → Movie**)
    | in AMSmovie show the energy (**Graph → Energy**)
    |
    | Wait until the calculations have finished (around 7 minutes on a recent desktop machine)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-optimization.png

.. rst-class:: steps

  \
    | Close AMSmovie (showing the logfile)
    | Open AMSmovie  (now it should show the new .sdf file, see title)
    |
    | In the AMSjobs window open the details by clicking on the triangle
    | Locate the original .sdf file in the .results folder (with time stamp)
    | Click on it to select it
    | Open it in AMSmovie (**SCM → Movie**):
    |
    | Show energy panel in AMSmovie window (**Graph → Energy**)

As you can see the conformer geometries and energies as optimized   by ADF differ greatly from the UFF results:

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-optimization-old.png

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-optimization-new.png

In the AMSjobs window you could also select the results for individual conformers: select the result file of interest,
and use the SCM menu (Output, Spectra, KF Brower, ...) to examine it.

Step 6: Calculate the IR spectrum
---------------------------------

To calculate the IR spectrum for all conformers (in the current .sdf file, with optimized ADF geometries),
just set up an IR calculation in AMSinput as you would for a single molecule.
And, just as for the geometry optimization in the previous step, the Coordinates panel will tell AMSinput to do this for all conformers.

As we also want to keep the current conformers (for example, to calculate different spectra),
we will save the setup with a new name:

.. rst-class:: steps

  \
    | Close the AMSmovie windows
    |
    | In AMSinput, use the **Single Point** task, check **Frequencies** (in the Main panel)
    |
    | Select the **Model → Coordinates panel**
    | Make sure the "Use Selected File" is still selected
    | select the propanoicacid_ADF.sdf file from the previous step

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-sdf.png

.. rst-class:: steps

  \
    | **File → Save As...** and save the job with a new name (propanoicacid_IR)
    | **File → Run**
    | Wait until the calculations have finished (around 7 minutes on a recent desktop machine)

Step 7: Visualize the Boltzmann weighted IR spectrum
----------------------------------------------------

.. rst-class:: steps

  \
    | **SCM → Spectra**

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-ir.png

.. rst-class:: steps

  \
    | Change the temperature to 0 K

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-ir-0k.png

Obviously you can also select a high temperature, but the spectrum will be missing contributions from conformers that have   been filtered away.

You can select what weights to use Boltzmann, Uniform or User defined:

.. rst-class:: steps

  \
    | Select "User" from the weights pull down underneath the graph
    | (the menu labeled "Boltzmann" at this moment. You may need to increase the size of your AMSspectra window for it to be visible.)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-weights.png

In the Conformer Weights window you can set the weight explicitly   as you like for each conformer. You can use the buttons at the   bottom to preset values. Move the mouse over the buttons and   check the balloon help for more information. The multiplicity is   the number of random RDKit conformations generated that ended up   in the same conformer after optimization.

You can also see the IR spectra of the individual conformers all at the same time (in one graph):

.. rst-class:: steps

  \
    | Switch back to "Boltzmann"
    | Use the **View → Average/All curve** menu command to toggle between the average and all of the individual curves

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-ir-all.png

Step 8: H-NMR, UV/Vis
---------------------

By now it should be evident how to set up calculations for all of   the conformers. Two more examples: the H NMR spectrum and the   UV/Vis spectrum.

.. rst-class:: steps

  \
    | Open the previous IR job in AMSinput
    | Change the Task to **Single Point**
    | Go to the NMR panel (in the Properties section)
    |
    | Check the 'Shielding for all H atoms' option
    |
    | Go to the Coordinates panel
    | Make sure the propanoicacid_ADF.sdf file is still used as source of conformers
    |
    | **File → Save As...** and save it as propanoicacid_NMR
    | **File → Run**
    |
    | Wait for the calculation to finish (around 1 minute)
    |
    | **SCM → Spectra**
    | Change the width to 0.01

The final spectra (at 0K and at 300K) should like this:

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-1h-0k.png

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-1h-300k.png

.. rst-class:: steps

  \
    | Calculate the UV/Vis spectrum (do not forget to turn off the calculation of the NMR spectrum)
    | Wait for the calculations to finish (around 3 minutes).

The final spectra (at 0K and at 300K) should like this:

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-uv-0k.png

.. image:: /Images/MultipleMoleculesConformersMethod/t13-conformer-uv-300k.png


Multiple Methods
================

.. _MultipleMethods:

You can also set up a series of calculations with different methods, and run them automatically one after each other.
The geometries will automatically be passed from one job to the next.

As examples we first show how to set up a series like: DFTB optimization, ADF optimization and ADF UV/Vis spectrum for the optimized structure.
We will then run this set up twice: once for the specified molecule, and once for a set of molecules.

Step 9: Set up a series of calculations
---------------------------------------

The first step in the series is a DFTB calculation on a molecule, we will use Acetone as an example:

.. rst-class:: steps

  \
    | Start AMSinput
    | Make (or find) an Acetone molecule
    | Switch to DFTB mode
    | Select the 'SCC-DFTB' model
    | Select the 'Dresden' parameter set
    | Save as 'dftb'
    | Close AMSinput

The second step in the series is an ADF geometry optimization of the optimized structure from the first step:

.. rst-class:: steps

  \
    | Start AMSinput
    | Select the **Geometry Optimization** task
    | Switch to the Coordinates panel
    | Use Job Result
    | Molecule from dftb.ams

.. image:: /Images/MultipleMoleculesConformersMethod/t13-coords-dftb.png

We now use the Job Result option in the Coordinates panel: this will make sure that the selected job is run first,
and that the resulting geometry of that job will be used as input geometry for the current calculation.

.. rst-class:: steps

  \
    | Save as 'adf-geo'
    | Close AMSinput

The third step in the series is an ADF UV/Vis calculation for the ADF-optimized structures:

.. rst-class:: steps

  \
    | Start AMSinput
    | Set up an UV/Vis calculation
    | Switch tot the Coordinates panel
    | Use Job Result
    | Molecule from adf-geo.ams

.. image:: /Images/MultipleMoleculesConformersMethod/t13-coords-adf-geo.png

.. rst-class:: steps

  \
    | Save as 'adf-uvvis'
    | Close AMSinput

Step 10: Run a series of calculations for a single molecule
-----------------------------------------------------------

To run the just created series of calculation all we need to do is to start the final job (adf-uvvis).
AMSjobs will detect that it uses results of other jobs, and start those jobs automatically:

.. rst-class:: steps

  \
    | Start AMSjobs (or make it active if it is still running)
    | Select the adf-uvvis job

In the AMSjobs window you can see on which jobs the selected job depends:

.. image:: /Images/MultipleMoleculesConformersMethod/t13-multijobs.png

.. rst-class:: steps

  \
    | Run the job

In AMSjobs you should now see all the jobs in the job series running, one by one, in the proper order.
If you wish you can examine the results of each job step as you would for normal independent jobs.

Lets now just check the final UV/Vis spectrum:

.. rst-class:: steps

  \
    | Select the adf-uvvis job in AMSjobs
    | **SCM → Spectra**

.. image:: /Images/MultipleMoleculesConformersMethod/t13-uv-spectra.png

Remember that in the adf-uvvis job no molecule was specified, the geometry has been imported from the result of the adf-geo job.
And that job in turn got the geometry from the dftb job.

Step 11: Create an SDF file, and Run a series of calculations for a set of molecules
------------------------------------------------------------------------------------

The series of calculations in the previous steps can also be run with molecules from a .sdf file as input.
Any SDF file can be used, for example the earlier sdf files from this tutorial.

In this case we will make a new SDF file just to show how to do that as well.
First we make two .ams files, one for benzene and one for water:

.. rst-class:: steps

  \
    | Start AMSinput
    | Make benzene
    | Save as benzene.ams
    |
    | **File → New**
    | Make water
    | Save as water.ams
    | Close AMSinput

Next we make an SDF file containing the two molecules we just made:

.. rst-class:: steps

  \
    | Go to AMSjobs
    | Select the benzene and water jobs you just made (use control click to select multiple items)
    | **Tools → Add To SDF...**

.. image:: /Images/MultipleMoleculesConformersMethod/t13-addtosdf.png

\
   | In the Append to file option select a name for the .sdf file to create: mols.sdf
   | Click OK

A new SDF file with the specified name will be created, containing the structures you selected.
You can also add extra molecules to the .sdf file using the same method (just select an existing .sdf file instead of a new one).
You can also include structures resulting from calculation results you have (.t21, .rkf files etc), or even from simple .xyz or .mol files and so on/

Next we want to run the series of jobs (DFTB - ADF geometry optimization - ADF UV/Vis) for all molecules in the mols.sdf file.
In the first job of the series (DFTB) specify to use molecules from the .sdf file:

.. rst-class:: steps

  \
    | Open the dftb.ams file in AMSinput again (click No when asked to update coordinates)
    | Go to the coordinates panel
    | Use Selected File
    | Molecule From: select the mols.sdf file just created

.. image:: /Images/MultipleMoleculesConformersMethod/t13-coords-mols.png

.. rst-class:: steps

  \
    | **File → Save**
    | In AMSjobs select the last job in the series (adf-uvvis)
    | **Job → Run**

You should see all jobs running again in AMSjobs, but now multiple times.
In the .results directories you will find the results for the individual jobs,
and the final geometries are always collected in new .sdf files.

.. rst-class:: steps

  \
    | In AMSjobs show the details of the adf-uvvis job (click on the triangle)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-uv-results.png

As before you can see the average or individual spectra via AMSspectra, or the geometries using AMSmovie:

.. rst-class:: steps

  \
    | **SCM → Spectra** (with the adf-uvvis job selected)
    | In the AMSspectra window: **View → Average/All Curve**
    | **SCM → Movie** (with the adf-uvvis job selected)

.. image:: /Images/MultipleMoleculesConformersMethod/t13-uv-average.png

.. image:: /Images/MultipleMoleculesConformersMethod/t13-uv-movie.png



