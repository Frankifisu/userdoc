Quantum ESPRESSO
################

.. _metatag QUANTUMESPRESSO: 

The GUI also supports setting up, running and visualizing results from Quantum ESPRESSO.
For installation of Quantum ESPRESSO see the :ref:`Set up<metatag SETUP>` section in this manual.

Quantum ESPRESSO is an open source package that can perform plane wave SCF calculations, among other things.
See `www.quantum-espresso.org <http://www.quantum-espresso.org>`__ for details.

Quantum ESPRESSO is *not* included in the ADF distribution.
The GUI works with the standard Quantum ESPRESSO distribution (version 6.2), no changes have been made.

As the Quantum ESPRESSO code has not been developed by SCM, we cannot give support for Quantum ESPRESSO issues other then use via our GUI.

Tutorials
=========

There are some `tutorials <../Tutorials/ExternalPrograms/index.html>`__ that show how to use Quantum ESPRESSO via the GUI.

Input
=====

AMSinput can make run scripts for Quantum ESPRESSO. To do that just go to the Quantum ESPRESSO section in AMSinput, it should be self-explaining how to run jobs.

On the Main panel you can set the task type (with Geometry Optimization doing the same as the relax and vc_relax options in Quantum ESPRESSO).

The XC, Type and Relativity options are used to select pseudo potentials. They work by filtering all pseudo potentials available to match the selected options,
for your current system. Thus it depends on your system what options are available in the XC and Type menus.
Click on the ... next to Type, or go to the Pseudopotentials details page to have ultimate control: select any file as a pseudo potential file.

When you save your setup, AMSinput will generate a run script. You can preview this script in the Run Script panel (in Details).
You can even edit it, and then your editted run script will be used (note that this will block other changes you may make in AMSinput until you turn Auto update
back on).

Running
=======

You should run the job preferably via AMSjobs, in the usual way. 

That way you can also run on remote machines, and AMSjobs takes care to copy the files needed to the remote machine. 
The selected pseudo potential files will also be copied to the remote machine, unless they live in upf_files (then it is assumed they are already on the remote machine). 
Obviously you should install Quantum ESPRESSO on the remote machine as well if you want to run jobs there.

Note that while the job is running you can monitor its progress in AMSjobs, or via the logfile (which in this case is identical to the output file).

Visualization of results
========================

After the calculation the Quantum ESPRESSO results are parsed to generate an RKF file. Preferably data from the data-file.xml is used, but many pieces of information
are taken from the standard output file as they are not available on the xml file. For that reason there is a chance that things will fail to use if you use a different
version of Quantum ESPRESSO.

The RKF result file can be used by all the SCM GUI modules to visualize results.
Thus you can use the SCM menu to:

* View: visualize the system and fields (density, potential, deformation potential, spin density, ...). AMSview uses the post processing tools from Quantum ESPRESSO to generate the fields. For that the Quantum ESPRESSO results need to be available (in the .results folder), not just the RKF file. When your calculation is a remote calculation AMSview will automatically generate jobs to calculate fields as needed on the remote machine (thus no need to transfer the other big .results directory)
* Movie: the geometry changes during your calculation (for geometry optimizations with or without lattice optimization). As usual you can plot the energy as function of the geometry step, or any geometric data (distances, angles, cell axes, etc).
* Logfile: the standard text output.
* Output: the standard text output.
* Band Structure: visualize the band structure and (partial) DOS, if calculated
* DOS: visualize the (partial) DOS
* KF Browser: many pieces of output results collected, ready to copy to some spreadsheet or make graphs inside KF Browser

Scripting support
=================

Using Quantum ESPRESSO via amsprep and amsreport is fully supported.

Use ``$AMSBIN/amsprep -h`` and ``$AMSBIN/amsreport -h`` for details.
For more information on what QE results are available via amsreport, specify the result file name (the .rkf file) as well.

For example: ``$AMSBIN/amsreport -h qejob.rkf``
