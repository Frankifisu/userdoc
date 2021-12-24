General
#######

Introduction
************

This document will provide background information for the Graphical User Interface, part of the AMS package.  

The purpose of this document is to give more detailed background information on how the GUI operates. It will not explain how to use it in detail. For that reason, we strongly suggest that before reading this document, you first check the `GUI tutorials <../Tutorials/index.html>`_. 

Release 2022.1
**************

In comparison to AMS-GUI 2021.1, the 2022.1 release offers many bug fixes and the following new main functionality:

* General:

  * All GUI modules transfer job to ParAMS GUI via menu command (cmd/ctrl-T)

* AMSinput:

  * Open .run files
  * AMS Lattice scan
  * GFNFF engine
  * Lennard-Jones engine
  * FCF support updated
  * GW support updated
  * QTAIM / IQA support updated

* AMSspectra:

  * Support for GW improved

* AMSmovie:

  * ChemTraYzer 2:

    * Input

      * setup input (based on json description and .def file
      * AMSinput style unit changes and revert to default (right click)
      * when opening the GUI, update the input fields with values as found in the chemtrayzer2/job file, if it exists

    * Running

      * run ChemTraYzer 2, job
      * output and results are in chemtrayzer2 folder next to the ams.rkf file
      * progress dialog while running, cancel button to interrupt
      * errors from run are reported
    
    * Output
    
      * automatically show the results in tables when available
      * right bottom of table: button with name of table, click it to open by the OS (on MacOS open the .csv file in Numbers for example)
      * tables can be sorted per column
      * tables can be searched, with some advanced search options. use help balloon to get info on search syntax
      * feedback on search in status line (number of items found, column searched)
      * click, shift-click, control (or right) click to adjust selection in tables
      * selection in upper table searches for matching evens in lower table
      * selection in lower table shows corresponding atoms (hiding other atoms) in corresponding (first) frame in the Movie window
      * left-right arrow keys to skip through movie frames
      * up-down arrow keys to move selection up or down (thus go through different events for example)
      * escape clears selection, or the search if it has focus
      * if no selection, escape clears the search

* ParAMS GUI:

  * General

    * 'All', 'Jobs', 'Training Set', 'Validation Set', 'Engines': table with training data
    * Molecule window: show system for selected entries
    * 'Info': detailed info for any entry in job collection or training data
    * 'Parameters': table with parameters, ranges and other details to be optimized
    * 'Params Configuration': show and set up the ParAMS job details
    * 'Graphs': results of optimization in graphs
    * 'Results': text output files
    * import old style reaxff geo/params files
    * revert option to ditch changes due to editing or handling results

  * Running

    * run the ParAMS job via AMSjobs
    * opening a ParAMS job will automatically read the results if available
    * live update of the results
    * running and live update also work for running on remote machines (as all other jobs in AMSjobs)
    * restart a previous run when  using the CMA optimizer
  
  * Training Data

    * different tabs to show all of these or just one subset (‘All’, ‘Jobs’, Training Set’, ‘Validation Set’, ‘Engines’)
    * filter by type of entries (Energies, Bonds, PES, Jobs, Engines, …)
    * when multiple systems are relevant for an entry, use arrow left-right to move through them
    * add jobs from inside the Params GUI, or via any other GUI module (cmd/ctrl - T)
    * use the ParAMS importers to generate training set entries when importing a job
    * select atoms to set the proper index when creating some expressions
    * menu commands to add most common expressions in the training set
    * edit all (non-output) items in all tables
    * editing via AMSinput for jobs and engines
    * smart editing of multiple items in many cases (expressions for multiple items like relative energies, or deactivate all selected parameters for example)
    * tab-completion to quickly enter Job IDs
    * energy expressions may be balanced automatically (as they correspond to a reaction typically)
    * set up training set and validation set (manual or random)
    * merge training sets / job collections
    * edit all JobIDs at once: prefix or change
    * when results are available the contribution to errors is shown with the matching item
    * results are live-updating

  * Parameters

    * ReaxFF, xTB and Lennard-Jones parameters supported
    * detailed information about meaning of parameter and optimization range etc
    * adjust parameter optimization range Min and Max
    * generate new ReaxFF blocks, initialize ReaxFF blocks
    * parameters are live-updating

  * ParAMS Configuration

      * set up the params.conf.py file to use for running
      * predefined common options via menus 
      * fully editable by user if desired

  *  Graphs

    * relevant graphs are shown automatically when running
    * graphs are live-updating
    * validation and training set graphs together, compare with first iteration
    * graphs of PES data (like energy vs distance or angle etc)
    * interaction in graphs (click on an item to select matching training set entries, and select relevant atoms in molecule display if applicable)
  
  * Results

    * show text output easily accessible via menus
    * text is live-updating

  * Tables
    
    * tables can be sorted per column
    * tables can be searched. use help balloon to get info on search syntax
    * feedback on search in status line (number of items found, column searched)
    * click, shift-click, control (or right) click to adjust selection in tables
    * up-down arrow keys to move selection up or down
    * escape clears selection, or the search if it has focus
    * if no selection, escape clears the search

