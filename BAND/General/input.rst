
Input
=====

The input options for Band are specified in a text file consisting of a series of key-value pairs, possibly nested in blocks.
The input is usually embedded in an executable shell script. This is the content of a typical shell script for running a Band calculation:

.. code-block:: none

   #!/bin/sh

   $AMSBIN/ams <<eor
      # This is the beginning of the input.
      # The input consists of key-value pairs and blocks.
      # Here we define the input option for the AMS driver:

      Task GeometryOptimization

      System
         Atoms
            H 0.0 0.0 0.0
            H 0.9 0.0 0.0
         End
      End

      # Next comes the Band "Engine" block. The input options for Band, which are 
      # described in this manual, should be specified in this block:

      Engine Band
         Basis
            Type DZP
         End

         XC
            GGA PBE
         End
      EndEngine
   eor


To run the calculation above from command-line you should:

1. Create a text file called, for example, ``test.run`` and copy-paste the content of the script above
2. Make the script executable by typing in your shell ``chmod u+x test.run``
3. Execute the script and redirect the output to a file: ``./test.run > out``

The program will create a directory called ``ams.results``. Inside it, you will find the *logfile* ``ams.log`` (which can be used to monitor the progress of the calculation) and the binary results files ``ams.rkf`` and ``band.rkf``. 
After the calculation is completed, you can examine the output file ``out``. For more details, see the `AMS documentation <../../AMS/General.html>`__.

.. seealso:: 
   
   The :ref:`Examples <Examples>` section contains a large number of input examples. 


.. important::

   All options described in this manual should be specified in the Band Engine block::

      # All Band keywords should be specified inside the 'Engine Band' block 
      Engine Band
         Basis
            Type DZP
         End

         XC
            GGA PBE
         End
      EndEngine


.. include:: ../../shared/input.rst
.. include:: ../../shared/input_units.rst