.. _Modules:

GUI modules
***********

The AMS-GUI is the Graphical User Interface for the Amsterdam Modeling Suite. It consists of several modules for specific tasks. Those modules work together and exchange information.

All the AMS-GUI modules have one common SCM menu on the top left of the window. You can use the commands inside the SCM menu to start other GUI modules (or switch to them). 

In general when selecting a GUI module from the SCM menu it will start and open the current job. If that module is already open with the current job, it will be activated (brought to the foreground). The current job is the selected job in AMSjobs, or the job open in some other GUI module if you use the SCM menu in that module. 

.. tip::

    In AMSjobs: 

    Right click on the left side of a job (like the icon or name) to get a pop-up version of the SCM menu with that job selected.

    Right click on the right side of a job (like the queue or options field) for more pop-up commands (Run, Kill, ...).

The most important exception is opening the New Input module (AMSinput) or AMScrs (COSMO-RS) in AMSjobs. In that case the selected job will be ignored, and you can start working on a new calculation. To open the selected job in AMSinput, you need to click the icon in front of the job or use the Input command from the SCM menu. 

SCM → Preferences
   AMSpreferences ($AMSBIN/amsprefs) allows you to adjust and save numerous GUI preferences, such as color schemes, environmental variables, etc. The preferences will be used by all AMS-GUI modules. 

SCM → New Input
   AMSinput ($AMSBIN/amsinput) helps users to easily create AMS jobs. You can use AMSinput to define your molecule (geometry), pre-optimize it, and to set details of your AMS job using an easy-to-use graphical user interface. AMSinput will generate the basic job script for you. This script takes care of running AMS and property programs as required.  

   The same module can actually create jobs using different methods: ADF, BAND, DFTB, MM, MOPAC, QMMM, QUILD, ReaxFF, ForceField and Quantum ESPRESSO. 
   After starting it, you can simply change the method to use without starting a different module.  Depending on your license, not all options might be available. 

   The New Input command will start a new AMSinput with no job loaded.

SCM → Input
   As New Input, but load the selected / current job.

SCM → COSMO-RS
   AMScrs ($AMSBIN/amscrs) enables ADF users to easily select compounds, create COSMO-RS jobs, run the jobs, and visualize the results. 

SCM → View
   AMSview ($AMSBIN/amsview) displays volume data, such as electron densities, orbitals, electrostatic potentials and more. You can also use it to visualize scalar atomic data like charges, some tensor data, and AIM (Bader) results. 

SCM → Movie
   AMSmovie ($AMSBIN/amsmovie) follows geometry steps as performed by AMS during geometry optimizations, molecular dynamics, IRC calculations, etc. It can be used during the calculation to monitor the progress (based on information from the logfile), or it can be used to analyze the geometry changes after a calculation. It is also used to display normal modes calculated with a frequency calculation. 

SCM → Levels
   AMSlevels ($AMSBIN/amslevels) generates a diagram showing the energy levels of a finished calculation. You can interact with it: show an interaction diagram (how the molecular orbitals are constructed from fragment orbitals), show labels, occupations, orbitals, etc. 

SCM → Logfile
   AMStail ($AMSBIN/amstail) shows the contents of a text file, updating when the text file grows (like the UNIX tail -f command). It is typically used to monitor the 'logfile'. The progress of an AMS calculation is always written to this file. 

SCM → Output
   AMSoutput ($AMSBIN/amsoutput) shows the output of AMS (or any other text file). It will analyze the output and provide quick links to sections of interest. 

SCM → Spectra
   AMSspectra ($AMSBIN/amsspectra) shows spectra calculated by AMS. It can show IR, Raman, excitation and CD spectra, as well as a DOS plot. For some spectra it can also perform additional tasks (using other AMS-GUI modules), like displaying normal modes or orbitals. 

SCM → Band Structure
   AMSbandstructure ($AMSBIN/amsbands) shows dispersion spectra like the band structure of solids, or phonon spectra, as calculated by for example Band or DFTB. 

SCM → Dos
   AMSdos ($AMSBIN/amsdos) shows DOS-like results. You can easily select which partial DOS to show by selecting atoms, and you can even select to show the GPDOS for select atoms and L-shells. 

SCM → KFBrowser
   KFBrowser ($AMSBIN/kfbrowser) is a graphical interface to examine data from the binary KF files produced by most of the computational engines in the Amsterdam Modeling Suite. 
   You can use it to see details, graphs, copy data in table format, or get to the low-level contents of the result files.

.. _ADFJOBS: 

SCM → Jobs
   This utility ($AMSBIN/amsjobs) manages your ADF jobs: run a job on your local machine or on remote machines. It also serves as a interface to all files belonging to your job, and it serves as a convenient launcher of the other AMS-GUI modules. 

