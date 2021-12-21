.. _KF: 
.. _PKF: 
.. _CPKF: 
.. _DMPKF: 
.. _UDMPKF: 
.. index:: KF command line utilities 
.. index:: pkf module 
.. index:: cpkf module 
.. index:: dmpkf module 
.. index:: udmpkf module 

KF command line utilities
=========================

There are four utility programs for manipulating files in the so-called Keyed File (KF) format from the command shell.
Two of them convert KF files from binary to ASCII and vice versa.
See the pkf and dmpkf utilities for a description of the ASCII format of a kf file.
Such a readable version of a KF file can be useful to inspect its contents in detail.

All programs from the package will convert a KF file to the binary format native to this platform if necessary.
In such a case, the original file will be renamed to a file with tilde "~" appended to its name and a message will printed on the standard output.

The KF software was developed at the Vrije Universiteit Amsterdam as a general-purpose package for storing data and re-accessing it via keyword-driven procedures.

**pkf**

:: 

  pkf file1 { file2 ... filen }


pkf prints a summary of the contents of the kf files file1... filen.

All variables are listed by name, type (integer, real, character, logical), and size (number of array elements) and bundled into named sections.

To put the results in an ASCII file for later inspection::

  pkf file > ascii_result


Each section on the file contains an index of its variables and their associated values.
All data are organized in blocks.
Each section may have any number of index blocks and any number of data blocks (this depends simply on the amount of data to be stored in such a block).
In addition there is one special section, the SuperIndex, which is an index of all sections on the file.

The output of pkf consists of:

* General information about the file (name of the file, internally used unit numbers during processing the file...)

* A summary of the SuperIndex, hence an index of blocks in the file and the associated sections.

* A summary: total numbers of blocks associated with the different types of blocks.

* For each section a list of its variables. For each variable in the list the following is displayed

  * The variable name.

  * Its length, i.e. the storage requirements of the variable within the file.

  * Its 'used' size, hence the file storage associated with the variable (in units off 8 Bytes for double precision real numbers, 4 for integers, etc.).

  * The number of actual elements within the variable (for real, integer, and logical data types) or the number of characters in a string.

  * The (logical) index of the data block it is stored in.

  * The off-set of the data within its data block.

  * Its value or the first element of an array variable, respectively.

**cpkf**

::

  cpkf file1  file2 {key1 .. keyn}

cpkf copies the sections and/or variables key1 .. keyn from file1 to file2.

If a referenced section or variable already exists on file2 it is overwritten, else it is created.
Sections and variables which are already present on file2 but which are not referenced in the command are not affected.

If no sections and/or variables are explicitly mentioned at all the copying is carried out for all sections and variables on file1.

As a side effect of this operation any 'holes' eventually present in the original due to the formal deletion of obsolete sections and variables are not copied.
Note that the KF file is not rearranged upon deletion of data.
Rather only the corresponding entries in the index tables are removed in this case.
During the copying process the data is however rearranged for optimum storage efficiency and the resulting file copy may therefore be smaller than the corresponding original.

Skipping specific sections during the copying process can be manually controlled as follows::

  cpkf file1 file2 -rm section1 ...

In this form, all sections will be copied except for the ones specified on the command line, thus effectively removing them from the file.

To copy and rename a section::

  cpkf file1 file2  "section_name --rename new_section_name" 



**dmpkf**

A utility to extract information from a KF file and make it available in ASCII format::

  dmpkf file {key1 .. keyn}

dmpkf prints the sections and/or variables from the file file indicated by key1 .. keyn on standard output.
The complete file is printed if no sections or variables are specified.

The format to be used for the individual keys::

  Sec%Var

where Var the variable of interest present in section Sec.
The complete section is dumped if no variable name is specified.

By redirecting the result to another file a human readable output is obtained::

  dmpkf file > ascii_result

The output contains for each printed variable:

* One line with the name of the section it belongs to;

* One line with the name of the variable itself;

* One line with three integers:
  
  * The amount of space reserved for the variable on the file which is, however, relevant for programs operating with KF files only;
  * The amount of data associated with the variable: for reals, integers, logicals: the number of such elements; for strings: the number of characters;
  * An integer code for the data type of the variable: 1=integer, 2=real, 3=character, 4=logical;

* The values of the variable (on as many lines as necessary): for scalar variables only one value, for arrays as many values as the array contains.

**udmpkf**

A utility to put information read from standard input into a KF file::

  udmpkf file

udmpkf reads an ASCII file in the format created by dmpkf from standard input and creates the binary KF file therefrom.
If such a KF file is already present the sections and variables in the input file are appended to the existing KF file.
Whenever a section or variable already exists in target file it will be overwritten.
Other data on the target file are not affected.

The combination of dmpkf and udmpkf makes it easy to modify KF files with a normal text editor::

  dmpkf TAPE21 > t21_ASCII

After the desired modifications within t21_ASCII this file may be reconverted into a binary KF file::

  udmpkf < t21_ASCII TAPE21_new
  
Also note that dmpkf and udmpkf only require a single argument here, respectively, as "< t21_ASCII" passes the content of the edited file via the standard input.