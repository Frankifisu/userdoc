.. _GUI:
.. _introduction:


Getting Started
###############

This document collects a set of hands-on tutorials showing how to use the AMS-GUI. 

The AMS-GUI is the graphical interface of the Amsterdam Modeling Suite, and can be used with ADF, BAND, DFTB, ReaxFF, Mopac, Quantum ESPRESSO and more.

The AMS-GUI consists of several modules: AMSinput to set up calculations, AMSview to visualize orbitals, and many more. 
These modules work together, but you can also use them as stand-alone tools from the command line.

We estimate that you will need about half an hour for each part of the tutorial, for reading and performing the hands-on activities. Typically the calculations should give results that are very close to the results shown in the tutorials. However, in some cases minor changes may occur depending on hardware  and software versions. 

Additional information on the graphical interface may be found in the `GUI manual <../../GUI/index.html>`__.

.. toctree::
   :maxdepth: 1
   
   KeyboardShortcuts
   GUIModules
   GeometryOptimizationOfEthanol
   ExcitationsAndUVVisOfEthene
   10WaysToGetTheEnergy
   RunJobFromTheCommandLine


.. panels::
    :column: col-lg-12 p-0

    ---

    .. image:: /Images/GeometryOptimizationOfEthanol/preview.png
        :width: 250px
        :target: GeometryOptimizationOfEthanol.html
        :align: left

    :ref:`GO_ETHANOL`

    **Keywords:** ADF, DFT, building molecules, geometry optimization, orbital, energy levels, electron density

    ---

    .. image:: /Images/ExcitationsAndUVVisOfEthene/preview.png
       :width: 250px
       :target: ExcitationsAndUVVisOfEthene.html
       :align: left

    :ref:`EXCITATION_ETHENE`

    **Keywords:** ADF, UV/Vis, TDDFT, singlet and triplet excitation, orbital level, DOS, Natural Transition Orbitals (NTOs), Transition Density, excited state geometry optimization, export results

    --- 

    .. image:: /Images/GUIModules/preview.png
       :width: 250px
       :target: GUIModules.html
       :align: left

    :ref:`Modules`

    **Keywords:** AMSinput, AMSoutput, AMSview, AMSmovie, AMSlevels, logfile, AMSouptut, AMSspectra, BandStructure, AMSdos, KFBrowser, AMSjobs
