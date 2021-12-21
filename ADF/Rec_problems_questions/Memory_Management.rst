
Memory Management
=================

***Problem***: The program aborts with an error message "MEMORY ALLOCATION ERROR". This message is issued both in the logfile and in the output file. 

***Cause***: Memory allocation may fail due to: 

+ Insufficient virtual (i.e. total RAM + swap) memory

+ On Unix: too low values for per-process memory limits

+ Restrictions of the 32-bit architecture

***Cure***:  Problem 1: add more physical RAM or increase the size of the swap space (page file).  Problem 2: add one or more ulimit commands to your run script setting relevant limits  to "unlimited". Problem 3: Perform your calculations on a 64-bit system. ADF version for the most common 64-bit operating systems are available so use them! 

All the three problems above can be avoided by reducing the size of the calculation. The most  important parameter defining the amount of used memory is the size of the basis set or,  more precisely, the total number of Cartesian Slater functions, naos. Current value can  always be found in the out file of the calculation, just search for the "naos" string.  The amount of memory used by a particular calculation depends on the naos value and of the  type of the calculation and, for large naos, it scales as naos\ :sup:`2` . For example,  a non-relativistic calculation during SCF can use up to 40 naos\ :sup:`2`  bytes of memory.  Using spin-orbit coupling may double this amount and using a hybrid or a meta-GGA XC functional  will add extra on top of it. Also TDDFT calculations require additional memory.  

What can be done to reduce memory usage? First of all, reducing the basis set size for non-critical  parts of the molecule will reduce the memory requirement without reducing the quality of the results. Secondly, performing a calculation with a pure GGA instead of B3LYP will not only reduce the amount  of memory used but also make the calculation faster. The latter especially applies to  geometry optimizations because there B3LYP does not perform any better than some of the GGAs. 

***Note***: If workspace problems occur for relatively small calculations, there might be a bug. Notify your ADF contact: send us the output file so that we can have a look and check things out. 

