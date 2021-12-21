AMSinput
########

This version of the GUI has unified the input modules for ADF, BAND, ReaxFF and other packages. The new input module, typically called AMSinput, can now prepare the input for  all of the old methods, as well as for new methods like DFTB, Mopac, UFF and so on.

After starting AMSinput, you will notice a bright colored menu 'ADF' on the left of the panel bar. Depending on your license, it might read ADF, or BAND, or one of the other methods. If you click there, you will get a pull-down menu that allows you to switch the method. Thus effectively you can turn AMSinput into BANDinput, or ReaxFFinput, and so on.

In the SCM menu you will a New Input command. This command will start AMSinput. Next you can switch to BAND mode, etc, as just described.

The unified interface makes it possible to do things like reading a crystal structure file (which will cause AMSinput to switch one of the methods supporting periodicity automatically). Next you can build super cells, cut out clusters,  and switch back to ADF without periodicity. No need for extra licenses, and no need to copy/paste between GUI modules.

The Main panel for some methods (like DFTB and UFF) contain a 'Run' button. If you press that, the current method will be started interactively, with the geometry of your system updating on the fly. The main use for this is as a pre-optimizer, no files will be saved and only the geometry will be
updated.

.. toctree::
   :maxdepth: 2

   Input_options
   Input_shortcuts_and_buttons
   Searching
   Crystals_and_slabs
   packmol
   Building_molecules
   TuneGeometry
   Importing_your_molecule
   Regions
   Proteins
   Presets_and_Defaults
   Update_geometry_results_from_finished_calculation



