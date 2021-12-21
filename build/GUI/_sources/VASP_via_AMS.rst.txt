############
VASP via AMS
############


********************************************
VASP support in the Amsterdam Modeling Suite
********************************************

General
==========================

With AMS2019.3, the graphical user interface supports setting up, running and visualizing some
results from calculations run using the `Vienna Ab initio Simulation Package,
VASP <https://www.vasp.at>`__, version 5.X.  VASP itself is *not* included in
the Amsterdam Modeling Suite, but needs to be obtained and installed
separately.  As the VASP code has not been developed by SCM, we cannot give
support for VASP issues other than use via our GUI or PLAMS.

**This feature is currently under active development**, and should be
considered experimental. We encourage users to
report any problems they encounter, and to inform us about what type of
features they would like to see added.

VASP as an external engine
==========================

The GUI supports setting up calculations with VASP as an `external engine
<../AMS/Engines.html#external-programs-as-engines>`__ to the `AMS driver
<../AMS/General.html>`__, hence "VASP via AMS". This means that the
AMS driver handles all changes to the system's geometry during for example a
geometry optimization, NEB calculation, or molecular dynamics simulation.  The
energy and forces at each step are calculated by a single point VASP
calculation. Efficient use of restart files minimize the resulting overhead.

VASP can also natively perform geometry optimizations, NEB calculations, and
molecular dynamics simulations, but the VASP-via-AMS feature only supports
those types of calculations via the AMS driver.

AMS driver tasks that change the number of atoms from one step to the next, for
example Grand-Canonical Monte Carlo, Molecule Gun, or the numerical calculation
of phonons (via a supercell), are currently not supported by the VASP-via-AMS
interface.


Tutorials
=========
There are `tutorials <../Tutorials/ExternalPrograms/VASPTiO2SurfaceRelaxation.html>`__ that show
how to use VASP via the GUI, and via the python scripting toolkit PLAMS.


*****************************
Setting up a VASP calculation
*****************************

VASP executable and number of processes (parallelization)
==========================================================

There needs to be a working VASP installation on the machine where the calculation is run.
Specify the exact command you would like to execute to run VASP as the **Command to execute VASP**
on the main VASP page in AMSinput.  For example, set it to
``mpirun -np 16 vasp``, if you use mpirun to launch VASP and would like to
parallelize over 16 processes.

.. note::

   The environment variable NSCM must be set to ``1``. This is automatically done by AMSinput.

Pseudopotentials and PAW potentials (POTCAR)
============================================

VASP requires that pseudopotentials or PAW potentials be used for each element.
Such potentials are distributed with VASP in files called POTCAR or POTCAR.Z.
For example, the following files might exist for PAW potentials intended for use with
the PBE density functional:

.. code-block:: none

   /some/path/PBE_PAW/H/POTCAR
   /some/path/PBE_PAW/O/POTCAR
   /some/path/PBE_PAW/O_h/POTCAR
   /some/path/PBE_PAW/O_s/POTCAR

In this case, ``/some/path/PBE_PAW`` would be a **POTCAR Library**, that can be
entered on the main VASP in AMSinput.  That would by default use
the ``/some/path/PBE_PAW/H/POTCAR`` and ``/some/path/PBE_PAW/O/POTCAR`` files
for H and O, respectively. To specify other POTCAR files, for example the
harder (O_h) or softer (O_s) PAW potentials for O, select those files on the
**Details → Pseudopotentials** page.

If you set a POTCAR library, it will be remembered for the next time you launch AMSinput.

Note: The POTCAR library is a path on the machine running AMSinput, which need not be the
same machine as where the calculation is eventually run.

Tip: If as an example you frequently use the ``O_h/POTCAR`` file for O atoms, consider
creating a custom POTCAR library where this file is instead moved to ``O/POTCAR``,
so that it is automatically selected if you specify the custom POTCAR library.

k-point sampling (KPOINTS)
==========================

You can specify the grid sizes for Monkhorst-Pack or Gamma-centered k-point
grids, together with fractional k-point coordinate displacements, on the main page
in AMSinput.  If you would
like to use a custom KPOINTS file (to be read by VASP), select your file under
**Details → Expert VASP → KPOINTS File**. That file will override any
other specified k-point settings.

Currently, to specify a path through the Brillouin zone for band structure calculations,
or to use some manually specified set of k-points, you must generate such a KPOINTS file yourself.

Other settings (INCAR)
==========================

Many calculation settings can be set using the GUI, for example,

* The planewave energy cutoff (**main panel**)
* The exchange-correlation functional (**main panel**)
* Fractional occupation scheme (smearing) (**main panel**)
* van der Waals corrections (**Model → Van der Waals correction**)
* Hubbard U parameters for different elements (**Model → Hubbard U**)
* WAVECAR or CHGCAR files for restarting or initializing a calculation (**Details → Expert VASP**)

Moreover, you can set arbitrary settings as "Additional INCAR options" on the **Details → Expert VASP page**. In case of any conflict
between these and other INCAR-related settings set in the GUI, the "Additional INCAR options" take precedence.

You can also use your own INCAR file (**Details → Expert VASP**). That will ignore all INCAR-related settings in the GUI.

Note: the INCAR tags NSW, IBRION, ISIF, and LWAVE are automatically set by the AMS driver before VASP is executed.

********************
Running VASP via AMS
********************

Running VASP with AMSjobs
=========================

You can run a VASP-via-AMS job just like any other job using `AMSjobs <AMSjobs.html>`__. If a
geometry optimization, molecular dynamics simulation, or NEB calculation was
performed, you can visualize the results in AMSmovie.

Note that the AMS driver enforces that LWAVE be set to .TRUE., thus leaving
the WAVECAR file on disk. This file can become rather large, so if
you do not need it for post-analysis, or for initializing another calculation,
you could consider removing this file after the calculation has completely finished.

Preprocessing the input
=======================

You can also choose to only do the necessary preprocessing of a job before VASP
is executed, by selecting "Only preprocess" on the **Details → Expert VASP** page.
By running such a job, the INCAR, POSCAR, POTCAR, KPOINTS, and any other
auxiliary input files will be left on disk in the folder
``jobname.results/external``, but VASP will not be executed.  It may be useful
to manually inspect the contents of these files, to see exactly what the input
to VASP is. For the preprocessing step, no working installation of VASP is needed.


Scripting support
=================

Using VASP-via-AMS via the Python scripting framework PLAMS is fully supported,
see the `tutorial <../Tutorials/ExternalPrograms/VASPTiO2SurfaceRelaxation.html>`__.


****************************
VASP via AMS without the GUI
****************************
This section describes how to set up a VASP-via-AMS calculation without the
GUI. Please note that the keyword names, and the syntax for setting up a
VASP-via-AMS calculation, may change in future versions of the Amsterdam Modeling Suite.
For this reason, we recommend setting up the calculation via the GUI.

Before ams is executed, the pertinent POTCAR (as read by VASP) must be created in $AMS_RESULTSDIR.

VASP runs as an external engine to the AMS driver. The engine block to the AMS input file should read:

.. code-block:: none

   Engine External
      InputDefinition $AMSBIN/input_def/vasp.json
      Execute "$AMSBIN"/amspython "$AMSHOME"/scripting/standalone/external_engines/vasp.py
      Input
         ...
      EndInput
   EndEngine

where ``$AMSHOME`` and ``$AMSBIN`` are replaced by their respective values, and
where the allowed settings in the Input block are the following:

.. scmautodoclist:: vasp

