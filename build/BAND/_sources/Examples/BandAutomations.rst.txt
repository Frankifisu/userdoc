.. _example BandAutomations:

Example: Speed up SCF during geometry optimization
==================================================

Generally the SCF converges more quickly when using a finite electronic temperature.

In this example it is shown (for a toy system that does not need the trick) how this can be done.

The report shows how the value of kT varies during a geometry optimization.

:download:`Download report BandAutomations.txt <../../../examples/band/BandAutomations/BandAutomations.txt>` 

.. literalinclude :: ../../../examples/band/BandAutomations/BandAutomations.txt
   :language: none

:download:`Download BandAutomations.run <../../../examples/band/BandAutomations/BandAutomations.run>` 

.. literalinclude :: ../../../examples/band/BandAutomations/BandAutomations.run 
   :language: bash 
