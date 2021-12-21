.. _AMSPREP: 
.. index:: amsprep module 

AMSprep: construct an ADF COSMO results file
********************************************

The module amsprep is intended to facilitate scripting.
More details on amsprep can be found in the `AMSprep section in the Scripting manual <../Scripting/Commandline_Tools/AMSprep.html>`__.
For COSMO-RS the most relevant is the ADFCRS template.
The template ADFCRS will perform a gas phase geometry optimization,
and next a COSMO calculation at the gas phase optimized geometry.

In the next example the result of the ADF calculation is a file called adfwater.coskf, which is an ADF COSMO result file, that can be used as input for a COSMO-RS calculation, see also the :ref:`Example: COSMO-RS Tutorial 1<Tutorial COSMO files>`.

::

   cat << eor > water.xyz
   3
   
   H       0.00000000       0.77121000       0.18071000
   O       0.00000000      -0.00000000      -0.36142000
   H       0.00000000      -0.77121000       0.18071000
   eor

   "$AMSBIN/amsprep" -t ADFCRS -m water.xyz -j adfwater >job
   chmod +x job
   ./job
