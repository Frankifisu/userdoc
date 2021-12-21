.. index:: Symmetry

Symmetry
========

The symmetry of the system is automatically detected. Normally the symmetry of the initial system is maintained. One can lower the symmetry with the ``Symmetry`` key. In such cases the keyword ``POTENTIALNOISE`` can force the solution away from the initial symmetry. 

Whether or not symmetry should be used can be controlled vial the ``UseSymmetry`` key

.. scmautodoc:: band UseSymmetry

One can also select a sub set of symmetry operators:

.. scmautodoc:: band SubSymmetry

To get the indices of the symmetry operators, you should first run the calculation with the following options added to your input::

   print symmetry    
   stopafter gemtry     

  and then you look in the output for (here the first four operators are listed)     


  ::         

      64    SYMMETRY OPERATORS:          

   NO               MATRIX              TRANSL        AXIS    DET   ROTATION     
   --------------------------------------------------------------------------          

   1)        1.000   0.000   0.000       0.000       0.000    1.0       1                
             0.000   1.000   0.000       0.000       0.000                
             0.000   0.000   1.000       0.000       1.000          

   2)        1.000   0.000   0.000       0.000       0.000    1.0       1                
             0.000   1.000   0.000       5.400       0.000                
             0.000   0.000   1.000       0.000       1.000          

   3)        1.000   0.000   0.000       5.400       0.000    1.0       1                
             0.000   1.000   0.000       0.000       0.000                
             0.000   0.000   1.000       0.000       1.000          

   4)        1.000   0.000   0.000       5.400       0.000    1.0       1                
             0.000   1.000   0.000       5.400       0.000                
             0.000   0.000   1.000       0.000       1.000     

from this list you should select the desired operators and use that in your final calculation, for example::     

   SubSymmetry 1 7 21 31     

Symmetry breaking for SCF
^^^^^^^^^^^^^^^^^^^^^^^^^

.. scmautodoc:: band PotentialNoise