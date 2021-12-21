.. _TAPE13:
.. index:: TAPE13

TAPE13
======

TAPE13 is the checkpoint file for restarts after a crash. It is a concise version of adf.rkf, containing only the data the program uses for restarting the calculation. See the restart keyword. 
Note that since the AMSification of ADF in most case this TAPE13 has lost it usefulness.
Instead one should use the file ams.rkf, which is produced by the AMS driver, for restarting a geometry optimization, for example.

Like adf.rkf, TAPE13 is a binary, keyword driven KF file. You can manipulate it with the KF utilities, to get a print-out of its 'table of contents', or a complete ASCII dump of its full contents. 

The calculation that produces TAPE13 determines which section are written on it. The following sections may occur (and if they occur, the listed variables are stored in them). The actual values of the variables should be identical to the corresponding variables on adf.rkf. Also they should have the same names and be located in the same sections. In some cases, TAPE13 contains the complete corresponding section of adf.rkf. 

**Section Fit**

``coef_SCF``
   SCF fit coefficients. Total number of them is nprimf, the number of primitive fit functions (counting all *Cartesian* spherical polynomials: 3 for a *p*-set, 6 for a *d*-set, and so on). If the calculation is spin-unrestricted, each spin has its own set of fit coefficients: first all coefficients of spin-A, then those of spin-B 
