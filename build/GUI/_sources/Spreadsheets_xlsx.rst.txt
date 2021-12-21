.. _spreadsheet_export:

Spreadsheets (.xlsx)
#####################

Export AMS results to spreadsheet format
******************************************************

Starting from AMS2021.1, you can export the results of an AMS calculation to spreadsheet (.xlsx) format.

You can

* convert a single AMS results folder to spreadsheet format

* compare multiple AMS results in a single table

Create a .xlsx file for a single AMS result
---------------------------------------------

In AMSjobs, select a finished job and go to **Tools → Build spreadsheet**. This
will create a file called ``jobname.xlsx`` in the ``jobname.results`` folder, and open it
in your default spreadsheet viewer.

You can also double-click on the file in AMSjobs to open it. 

.. note::

   Your spreadsheet viewer **must be able to evaluate formulas**. We recommend that
   you use **Microsoft Excel** (for Windows, Mac) or **LibreOffice Calc** (for Windows, Mac,
   Linux). Other spreadsheet programs (such as Apple's Numbers, Google Docs, and Gnumeric) may not be able to calculate all
   formulas, or may lack some features like conditional formatting.

You can also choose to generate the spreadsheet when setting up the job in
AMSinput. Select **Details → Summary as Spreadsheet (.xlsx)**, and set the
output and unit options to your preferences.

To generate a spreadsheet file from the **command line**, run

.. code-block:: none

   "$AMSBIN/amspython" "$AMSHOME/scripting/scm/xlsx/amsresults2xlsx.py" /path/to/jobname.results

You can also pass a ``--help`` flag to the above script to see some customization options.

Generate spreadsheet by default for all jobs
-----------------------------------------------

To automatically generate a spreadsheet at the end of every job that you set up via AMSinput, 

* select **SCM → New Input**, 
* select **Details → Summary as Spreadsheet (.xlsx)**,
* set **Output** to **job.results/job.xlsx** to place the spreadsheet in the AMS results folder, or **job.xlsx** to place the spreadsheet in the same folder as the input file.
* select the units that you prefer
* select **File → Preset → Save as preset**
* save it with the name ``Defaults``
* restart AMSinput

This will place a line creating the spreadsheet at the end of the .run file.

Compare multiple AMS calculations in a spreadsheet
-----------------------------------------------------

**Graphical user interface**: Select multiple jobs in AMSjobs, by holding Shift while clicking on the job names. Select **Tools → Build spreadsheet**.

This creates a spreadsheet containing a table that you can filter or sort based on a number of properties, for example

* Job name
* Engine, task
* Elapsed time, termination status
* Energy, zero-point energy
* HOMO, LUMO, band gap
* Dipole moments
* Excitation energies, oscillator strengths
* Lattice vectors and parameters
* Reaction energies and barriers

**Command-line**:

.. code-block:: none

   "$AMSBIN/amspython" "$AMSHOME/scripting/scm/xlsx/amsresults2xlsx.py" --multi \
      jobname1.results jobname2.results [jobname3.results...]

Pass the ``--help`` flag to the script to see more options.


Units
----------

The generated spreadsheet contains a worksheet called **Units**. Under the
heading **Current units**, you can see and change the units used throughout the
spreadsheet. By clicking on one of the yellow cells, a drop-down list 
appears with the available options.

.. csv-table::
   :header: Unit, Comment

   Angles, degrees; cannot be changed
   Dipole moment,
   Electronic energy, "Orbital energies, excitation energies, band gaps, ..."
   Energy, "Potential energy, kinetic energy, ..."
   Entropy, expressed in energy_unit/K
   Frequency, cm⁻¹; cannot be changed
   Gradients (forces)
   Heat capacity, expressed in energy_unit/K
   "Hessian, 2D stress",
   Length
   Mass,
   "Pressure, 3D stress",
   Quadrupole moment, atomic units; cannot be changed
   Temperature, Kelvin; cannot be changed
   Time, ps; cannot be changed


Distributions and spectra
------------------------------

A spectrum (e.g. the IR spectrum) is calculated in the spreadsheet using
**Gaussian broadening**. If you prefer a different type of broadening (e.g.
Lorentzian), you can do this in the GUI module AMSspectra.

Evaluate formulas with LibreOffice
----------------------------------------

The LibreOffice Calc spreadsheet program does not by default recalculate formulas in .xlsx files. If you use LibreOffice Calc, we recommend that you (in LibreOffice Calc) go to **Tools -> Options -> LibreOffice calc -> Formulas** and set **Excel 2007 and newer** to **Always recalculate**.

Results available in spreadsheet format
******************************************************

The Amsterdam Modeling Suite can calculate thousands of different types of
results. Only the most common ones are exported to spreadsheet format (see the below tables).

If you cannot find a result in the spreadsheet file, open the output file or use KFbrowser to inspect the binary .rkf results files.

Engines
----------------------------

.. csv-table::

   ADF,✔
   BAND,✔
   COSMO-RS,❌
   DFTB,✔
   ForceField,✔
   ReaxFF,✔
   ML Potential,✔
   Hybrid,✔
   Quantum ESPRESSO, ❌
   VASP via AMS, ✔ (partial)
   
Tasks
----------------------------

.. csv-table::

   COSMO-RS Compound, ❌
   Conformers,❌
   GCMC, ❌
   Geometry optimization, ✔
   IRC, ✔
   Molecular Dynamics, ✔
   NEGF, ❌
   Nudged elastic band (NEB), ✔
   PES Exploration, ✔
   PES Scan, ✔
   Single point, ✔
   Transition state search, ✔
   Vibrational Analysis, ❌


Single-point properties
------------------------

These properties are also given for the final frame of a geometry optimization or
molecular dynamics simulation, or for the highest-energy image in an NEB
calculation.

.. csv-table::
   :header: Property,

   Atomic charges, ✔
   "Bader analysis, QTAIM", ❌ 
   Band gap, ✔
   Band structure, ❌
   Bonds and bond orders, ❌
   Bulk modulus, ✔
   Density of states (DOS), ✔
   Diffusion coefficient, ❌
   Dipole moment, ✔
   Distance matrix, ✔ (color-coded)
   Eigenvalues and occupations per k-point, ❌
   Elastic tensor, ✔
   Electron density at nuclei, ✔ (ADF only)
   Electrostatic potential at nuclei, ✔ (ADF only)
   Energy, ✔
   Enthalpy, ✔
   Entropy, ✔
   Excitations (UV/VIS), "✔ (types, energies, spectrum)"
   Fermi energy, ✔
   Gibbs free energy, ✔
   Heat capacity, ✔
   Hessian, ❌
   HOMO, ✔
   HOMO-LUMO gap, ✔
   Internal energy, ✔
   k-point coordinates, ✔
   LUMO, ✔
   MDC-d charges and spins, ✔
   MDC-m charges and spins, ✔
   MDC-q charges and spins, ✔
   Molecules, ❌
   Mulliken charges and spins, ✔
   NMR, ❌
   Normal modes (IR spectrum), "✔ (symmetries, frequencies, spectrum)"
   Nuclear gradients (forces), ✔
   Orbitals, "✔ (symmetries, energies, occupations)"
   "Partial energies (Coulomb, ...)", ✔
   PES point character, ✔
   Partial DOS (PDOS), ❌
   Phonon DOS, ✔
   Pressure, ✔
   Quadrupole moment, ✔
   Radial distribution function (RDF), ❌
   Raman, ❌
   Shear modulus, ✔
   Statistical thermal analysis (thermodynamics), ✔
   Stress tensor, ✔ 
   Velocity autocorrelation function, ❌
   Young's modulus, ✔
   Zero point energy (ZPE), ✔

Geometry optimization properties
----------------------------------

**Geometry optimization summary**

.. csv-table::

   Convergence, ✔ (see Termination status)
   Final maxGrad, ✔
   Final maxStressEnergyPerAtom, ✔
   Final rmsGrad, ✔
   Number of iterations, ✔

**Per-frame information**: These are plotted vs. the frame number. For some of the properties, the plots only show data near the end of the optimization.

.. csv-table::

   Energy, ✔
   Frame number, ✔
   "Lattice parameters (a, b, c)", ✔
   maxGrad, ✔
   maxStressEnergyPerAtom, ✔
   Relative energy, ✔
   rmsGrad, ✔

NEB properties
---------------------------------

.. csv-table::
   
   Left barrier, ✔
   Number of images, ✔
   Number of iterations, ✔
   Plot of energy vs. image, ✔
   Right barrier, ✔


**Per-frame information**: See geometry optimization per-frame information.

MD properties
------------------------------------------

.. csv-table::

   Timestep, ✔
   Number of steps, ✔
   Simulation time, ✔
   Start and end step, ✔
   Start and end time, ✔

**Per-frame information**: These (except for Step) are plotted vs. time.

If the trajectory file contains more than 2000 structures, two worksheets are created:

* The first contains data for the first 2000 frames

* The second gives 2000 evenly spaced data points spanning the entire trajectory. Example: The trajectory contains 10000 frames, data is then given for frames 1, 6, 11, ..., 9991, 9996.

This is done to limit the size of the .xlsx file if the trajectory is very long.

.. csv-table::

    Cell volume, ✔
    Conserved energy, ✔
    Kinetic energy, ✔
    "Lattice parameters (a, b, c)", ✔
    Number of atoms, ✔
    Potential energy, ✔
    Pressure, ✔
    Step, ✔
    Temperature, ✔
    Time, ✔
    Total energy, ✔

**Block averages**: The total trajectory is divided into 5 equally sized
blocks, and for each block the mean and standard deviation of all per-frame
quantities are reported. Currently you cannot change the number of blocks.

System
-----------
.. csv-table::

   Atomic masses, ✔
   Atomic positions (xyz coordinates), ✔
   Cell volume, ✔
   Charge, ✔
   Chemical formula, ✔
   Density, ✔
   Job name, ✔
   "Lattice parameters (a, b, c, α, β, γ)", ✔
   Lattice vectors, ✔
   Net spin, ❌
   Number of atoms, ✔
   Mass, ✔
   Periodicity, ✔
   Picture, ✔ [#picture]_
   Reciprocal lattice vectors, ❌
   Symmetry, ✔ (only for ADF)
   Velocities, ✔

.. [#picture] A picture is generated if it is possible to start the AMS GUI.



General
-----------
.. csv-table::

   AMS version, ✔
   CPU time, ✔
   Elapsed time, ✔
   Errors, ✔
   Names of compute nodes, ❌
   Number of compute nodes, ❌
   Start and end time, ❌
   Text input, ✔
   Termination status, ✔
   Warnings, ✔


