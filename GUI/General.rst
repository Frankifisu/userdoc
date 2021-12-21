General
#######

Introduction
************

This document will provide background information for the Graphical User Interface, part of the AMS package.  

The purpose of this document is to give more detailed background information on how the GUI operates. It will not explain how to use it in detail. For that reason, we strongly suggest that before reading this document, you first check the `GUI tutorials <../Tutorials/index.html>`_. 

Release 2021.1
**************

In comparison to AMS-GUI 2020.3, the 2021.1 release offers many bug fixes and the following new main functionality:

* General:

  * Windows menu (in SCM menu) to switch between any open GUI module (also from with other jobs)
  * Easier to select a range of atoms in the Coordinates and Atom Details panels
  * Atom Details window now has filter options
  * Improve handling of Dark mode on MacOS
  * Improve handling of displays with higher dpi or with larger fonts
  * Replaced default file dialog on Linux by a more feature rich version. Can be reverted by setting SCM_DEFAULT_DIALOG to 1.

* AMSjobs:

  * (user) comments with jobs, savid in .pid files, including dynamic fields (which may for example show calculation results)
  * Generate .xlxs spreadsheet with summary of results for selected jobs with default options using the Build Spreadsheet menu command, or with full control via Scripting menu
  * Move jobs to a different directory via Jobs -> Move To Directory... command
  * Support Request Early Stop AMS feature (via the interactive.in file in the .results folder)

* AMSinput:

  * Multiple molecule UI improved, and added option to see all molecules superimposed or multiple views (synced cameras or not, use pulldown menu). New cmd/ctrl shift N shortcut for new molecule
  * Opening an AMSinput where results are available with a new geometry: ask what to do with more options (update geo, update geo for new job, ignore, restarts).
  * Remember window size and position
  * Add ReaxFF charge constraints to Model menu
  * Builder now offers the NLoop Packmol option
  * XC menu now has rSCAN, r2SCAN, r2SCAN-D4, revSCAN and revSCAN0 libxc shortcuts
  * Support Sinkbox and Safebox for MD
  * Excitations panel now has same defaults as the AMS program (in particular, NTOs are not calculated any more by default)
  * AMSinput POSCAR or AMSinput CONTCAR from the command line now imports those files (same as other file types that can be imported)
  * Help balloons now show name of corresponding input key
  * Generate .xlxs spreadsheet with summary of results at end of job  (details can be configured in a Details panel)
  * Adjusting dihedrals: respect groups as defined by regions (just as when adjusting length and angle)
  * Installing extra packages (lfdft, Quantum ESPRESSO, ML potentials) now uses AMSpackages, also available via SCM menu
  * Improve symmetrize 3D system, it will no longer be converted to a primitive cell, this can be done separately
  * Option to convert 2D systems to a conventional or primitive cell
  * Atom Details properties can filled by pasting a list of values
  * Support charged periodic BAND setup
  * Support LFDFT_MCD
  * Support FQ/QM
  * Support PES Exploration (setting up jobs and using states or populating bindingsites from a previous exploration)

* AMSspectra:

  * Much faster when handling many conformers at one time (with Boltzmann averaged spectra)
  * Zooming and double clicking in spectra improved
  * Support LFDFT_MCD

* AMSmovie:

  * Support PES Exploration
  * Improved performance for large trajectories in concatenated XYZ format 
  * Visualize regions that are added later (e.g. from a molecule gun)
  * Option to always let the GUI guess bonds instead of using the bonds from the result file

* AMSbands:

  * Improved performance and memory consumption when visualizing bands colored by character ("fatbands")
