
Structure of the restart file
*****************************

All data that may be retrieved from the restart file must be stored in a specific location on the restart file. If you're simply using an adf.rkf (TAPE21) result file or a TAPE13 checkpoint file you don't need to bother about this: ADF has put all data in the right place; the following discussion is primarily for those who want to manipulate the restart file or even construct one themselves. 

Since the restart file must be a kf file, the location of the data is of the form Section%Variable, specifying the section and the variable name. The section and variable names are case sensitive. See the utilities document for general information about kf files. 

If the specified variable is not present in the specified section on the restart file - or if there is no such section at all - the data is not used, usually without an error message. In some cases a few global tests are carried out on the retrieved data; if they fail the tests the data are not used and a warning - in some cases an error abort - may be issued by the program. 

KF files are binary files and so are the adf.rkf result file, the TAPE13 checkpoint file and generally any restart files. If you wish to edit and modify the contents, or just inspect them, the standard KF utilities can be used. Apply pkf to get a survey of the sections and variables on the file, dmpkf to get a complete ASCII version of the file and udmpkf to transform an ASCII version - presumably edited and modified - back into binary format.
Please consult the `Scripting Section <../../Scripting/Commandline_Tools/KF_command_line_utilities.html>`_ for further information about the standard KF utilities.

**AMS tasks**

In ADF2020 AMS is handling tasks related to exploring the PES.
For restarts related to, for example, a Linear Transit, Transition State, IRC or IR Frequencies run, one should look in the `AMS manual <../../AMS/index.html>`__.
