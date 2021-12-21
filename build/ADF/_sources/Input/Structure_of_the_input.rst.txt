.. _input parsing:

Input
=====

The input options for ADF are specified in a text file consisting of a series of key-value pairs, possibly nested in blocks.
Much of the general remarks about input for ADF apply also to related property and analysis programs, which are also described in this document. 
The input for the description of the system, structure and reactivity, vibrational spectroscopy, belongs (mostly) to the |AMS| part of the input.

* `Input, execution and output section of the AMS manual <../../AMS/Input_Output.html>`__

The input is usually embedded in an executable shell script.
This is the content of a typical shell script for running a ADF calculation:

.. code-block:: bash

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

      # Next comes the ADF "Engine" block. The input options for ADF, which are 
      # described in this manual, should be specified in this block:

      Engine ADF
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

The program will create a directory called ``ams.results``. Inside it, you will find the *logfile* ``ams.log`` (which can be used to monitor the progress of the calculation) and the binary results files ``ams.rkf`` and ``adf.rkf``. 
After the calculation is completed, you can examine the output file ``out``. For more details, see

* `Input, execution and output section of the AMS manual <../../AMS/Input_Output.html>`__

.. seealso:: 
   
   The :ref:`Examples <Examples>` section contains a large number of input examples. 


.. important::

   Most options described in this manual should be specified in the ADF Engine block::

      # All ADF keywords should be specified inside the 'Engine ADF' block 
      Engine ADF
         Basis
            Type DZP
         End

         XC
            GGA PBE
         End
      EndEngine


.. include:: ../../shared/input.rst
.. include:: ../../shared/input_units.rst


Title, comment
--------------

::

   TITLE Title

Title may be any string. The program combines it (that is, the first approximately 50 characters) with date and time of the job to construct the* job identification.* The job identification is used to stamp an identification on result files, which will be read and printed if such a file is used again, for instance as a fragment file. 

The job identification will also be echoed in the output header to identify the current run. By default the date and time are combined with a dummy string. In Create mode the title is first read from the data file that supplies the basis functions etc and can then be overwritten via input. 

Note that, contrary to some other programs, ADF does *not* take the first input record as a title.

You can put more remarks in the input file to be echoed in the standard output file; these will not become part of the job identification: 

::

   COMMENT
      text
      ...
   end

The text records are copied to the output header, directly after the job identification.

The key COMMENT may occur any number of times; all text blocks are printed in the output header with a blank line between any two text blocks. 

Amsification of ADF in ADF2020
------------------------------

The standalone program 'adf' does not exist anymore in ADF2020.
The job of AMS driver is to handle all changes in the geometry, e.g. during a geometry optimization, using so-called engines like ADF for the calculation of energies and forces.
Details of this change can be found in the section on the

* :ref:`AMSification of ADF<AMSIFICATION>`

Input parsing changes in ADF2018 and later
------------------------------------------

The input file parsing for ADF and its properties programs has changed from the 2017 to the 2018 version. 


New syntax for a few keywords
+++++++++++++++++++++++++++++

In order to adapt ADF to the new (more strict) input format, the syntax of a few keywords had to be changed.
The following table contains the list of keywords that have changed in ADF2018.
Note that some keywords changed in AMS2020 again, see the `section on ADF amsification <AMSIFICATION>`.
Note also that the block key DEFINE was removed.


.. csv-table:: 
   :header: "key in ADF2017 and before", "key in ADF2018 and later / comments"

      CorePotentials              , :ref:`CorePotentials <keyscheme COREPOTENTIALS>` is now a block (and not an *general* key/block)
      Define                      , removed
      Dependency                  , :ref:`Dependency <keyscheme DEPENDENCY>` is now a block (and not a key)
      EField                      , ADF2020: key 'System%ElectroStaticEmbedding' in |AMS|
      ETSNOCV                     , :ref:`ETSNOCV <keyscheme ETSNOCV>` is now a block (and not a key)
      Excitations -> Davidson     , :ref:`Excitations -> Davidson <keyscheme EXCITATIONS>` is now a block (and not a key)
      Excitations -> Exact        , :ref:`Excitations -> Exact <keyscheme EXCITATIONS>` is now a block (and not a key)
      Geometry                    , ADF2020: key 'Task' and key 'Properties' in |AMS|
      Integration Value           , :ref:`Integration -> Accint Value <keyscheme INTEGRATION>`
      LinearScaling               , :ref:`LinearScaling <keyscheme LINEARSCALING>` is now a block (and not an *general* key/block)
      ModifyStartPotential        , :ref:`ModifyStartPotential <keyscheme MODIFYSTARTPOTENTIAL>` is now a block (and not an *general* key/block)
      Occupations                 , Split into :ref:`Occupations <keyscheme OCCUPATIONS>` and  :ref:`IrrepOccupations <keyscheme IRREPOCCUPATIONS>`
      Relativistic                , ADF2020: block key :ref:`Relativity <adf-key-relativity>`
      Restart -> Value            , :ref:`Restart -> File -> Value <keyscheme RESTART>`
      Response -> Units           , Removed optional units for ``FrqBeg`` and ``FrqEnd`` in ``Response`` block
      SCF -> ADIIS                , :ref:`SCF -> ADIIS <keyscheme SCF>` is now a block (and not a key)
      SCF -> ARH                  , :ref:`SCF -> ARH <ARH>` is now a block (and not a key)
      SCF -> DIIS                 , :ref:`SCF -> DIIS <keyscheme SCF>` is now a block (and not a key)
      SlaterDeterminants          , :ref:`SlaterDeterminants <keyscheme SLATERDETERMINANTS>` is now a block (and not an *general* key/block)
      SOPert                      , :ref:`SOPert <keyscheme SOPERT>` is now a block (and not a key)
      Thermo                      , ADF2020: key 'Thermo' in |AMS|
 
Strict parsing of input file
++++++++++++++++++++++++++++

In ADF2018 and later **exact keyword matching** is used, meaning that **keywords abbreviations (or extensions) are not allowed**. 
In ADF2017 (and previous versions) the parsing of the input file was *tolerant* and it would allow for abbreviations and extension of keywords. 

In the example below, only the first version is allowed in ADF2018 and later, while the second and third version will trigger an input syntax error::

   # This is the proper input syntax:
   SCF
      Converge 1.0E-7
   End

   # In ADF2017 you could (for some keywords) use abbreviations. e.g.:
   SCF
      Conv 1.0E-7
   End

   # or extensions. e.g.:
   SCF
      Convergence 1.0E-7
   End

   # Keywords abbreviations and extensions are NOT ALLOWED in ADF2018 and later.

Execution
=========

See

* `Input, execution and output section of the AMS manual <../../AMS/Input_Output.html>`__


.. |AMS| replace:: `AMS driver <../../AMS/index.html>`__
