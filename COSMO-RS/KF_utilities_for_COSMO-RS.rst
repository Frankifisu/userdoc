.. _KF:

KF utilities for COSMO-RS
*************************

KF browser
==========

With the GUI module kfbrowser one can browse through the raw data on KF files (like the .crskf COSMO-RS result files). 

.. _keyscheme kfbrowser: 


::

   $AMSBIN/kfbrowser file.crskf

.. index:: cosmo2kf 
.. index:: kf2cosmo

kf2cosmo and cosmo2kf
=====================

The two COSMO-RS command line utility programs *kf2cosmo* and *cosmo2kf* convert COSMO kf files from binary to ASCII and vice versa. 

::

   kf2cosmo file.coskf file.cosmo

*kf2cosmo* reads from the kf file file.coskf (should exist) the section 'COSMO' and writes to the ASCII file file.cosmo (should not exist). Instead of a .coskf file, the file can also be a TAPE21 file which is a result file from an ADF COSMO calculation. 

::

   cosmo2kf file.cosmo file.coskf

*cosmo2kf* reads from the ASCII file file.cosmo (should exist) and writes a section 'COSMO' to the kf file file.coskf (should not exist). Note that only a section 'COSMO' is written to the kf file, which means that this file can not be used like an ordinary adf.rkf file (previously ADF<=2019 TAPE21 file or .t21 file). 

::

   cosmo2kf file.cos file.coskf

*cosmo2kf* can also read a MOPAC COSMO result file file.cos (should exist and should have the file extension .cos) and writes a section 'COSMO' to the kf file file.coskf (should not exist). 

pkf, cpkf, dmpkf, udmpkf
========================

::

   pkf file.crskf

pkf prints a summary of the contents of a kf file

::

   cpkf adf.rkf file.coskf COSMO

With the ADF kf utility *cpkf* one can copy the section 'COSMO' from an adf.rkf (should exist) to a file.coskf (should not exist). The file file.t21 should be a result of an ADF COSMO calculation. The file file.coskf is much smaller than adf.rkf. This file file.coskf can not be used like an ordinary adf.rkf file, but it contains all necessary information such that it can be used as input for a COSMO-RS calculations. 

With the ADF kf utilities *dmpkf* and *udmpkf* one can also convert COSMO kf files from binary to ASCII and vice versa.
Note that the ASCII files in this case are not so called .cosmo files.

::

   dmpkf file.coskf > ascii_result
   udmpkf < ascii_result newfile.coskf

