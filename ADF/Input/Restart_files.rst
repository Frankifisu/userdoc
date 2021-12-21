
ADF Restart files
*****************

When an ADF calculation terminates abnormally - not controlled by the program itself, for instance after a core dump due to some bug - there will usually be a file TAPE13, which serves as a checkpoint file. TAPE13 can be used to restart the calculation at a point not too far before the fatal condition occurred. It contains only data for the restart, but none of the special analysis data on adf.rkf that would be useful for analysis, to serve as fragment file, etc. 

TAPE13 is upgraded during the calculation but discarded upon normal termination, namely when all relevant information has been saved on adf.rkf. At that point all info that would have been on TAPE13 is present on adf.rkf. If you wish to keep TAPE13 anyway - for instance because you plan a restart after normal termination and don't intend to keep the substantially bigger adf.rkf - you must use the SAVE key. 

Upon normal (i.e. program-controlled) termination of a calculation, the adf.rkf result file can be used for restart purposes. When a crash occurs, however, chances are that adf.rkf has not correctly been closed and that its data structure is inconsistent: during the calculation large portions of adf.rkf are kept in memory rather than on file, and only at the point of final termination, all data is flushed to file. 

**General remarks**

In all restart calculations a normal input file must be supplied (you can, for instance, simply take the original one), with a specification of the restart file added: the restart file does *not replace* the input file. From the program's point of view, it first reads the 'normal' input file and then inspects whether a restart file is present to replace some of the information read from input. 

The concept of restarts in ADF is rather simple and primarily directed at increasing computational efficiency by providing cost-expensive data. The continuation run is to a large extent independent from the one that generated the restart file. The runtype, the choice of density-functional and other features in the Hamiltonian, precision of numerical integration, thresholds on convergence, et cetera are all determined solely from the input file for the new run: no such data is read from the restart file. Most input items should, therefore, be supplied in the restart run again, even if it is a direct continuation of a previous calculation: omission implies using the standard defaults, which are not necessarily the settings of the calculation that generated the restart file. 

Even the key ATOMS with the list of atomic coordinates must be supplied again: the program needs the information herein to deduce what fragments are used, which coordinates are free or frozen respectively in an optimization, etc. The coordinate *values* may be supplied with the restart file and these will then overwrite those specified in the input file. 

Obviously, the two runs cannot be completely unrelated. To let the restart data make sense the runs should correspond to the same molecule (i.e. its general definition in terms of fragment building blocks). The program does not check all aspects related to this and certain abuses will therefore survive the internal tests, but will surely lead to some error later on: it is the user's responsibility to ensure that the restart data match the calculation one has in mind. 

Interdependencies between data read from the restart file (rather than from input or fragment files) and other items imply that some input keys and some options to specific keys may be inaccessible when restart data are provided. In most cases supplying such inaccessible input options will simply be ignored; in some cases a warning is issued or an error abort occurs. 

A restart file supplies data from a previous run that might be useful in the current one. The applications are (combinations are possible): 

+ Get a better start in the (first) SCF procedure by providing the electronic charge density (in the form of fit coefficients) from the preceding run,

+ Continue an optimization by supplying the latest geometry (coordinates) from a previous run via the restart file (rather than typing them in),

**WARNING:** The SCF and optimization procedures use *history* to improve convergence behavior. Most of such history information is not stored on a restart file. As a consequence, a restart may not continue exactly as the original run would have done if it hadn't terminated. In a SCF restart, for instance, the DIIS procedure has to rebuild the information. The same holds for geometry optimizations, although history plays usually not a very big role there. 

AMS restart file
****************

In ADF2020 AMS is handling tasks related to exploring the PES.
For restarts related to, for example, a Linear Transit, Transition State, IRC or IR Frequencies run, one should look in the `AMS manual <../../AMS/index.html>`__.
