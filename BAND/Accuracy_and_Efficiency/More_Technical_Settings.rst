More Technical Settings
=======================

There are of course many other settings influencing the precision and performance. Usually the user does not need to care about them. 



Linear Scaling
--------------

.. scmautodoc:: band Tails


Dependency
----------

.. scmautodoc:: band Dependency


Screening
---------

Band performs many lattice summations which are in practice truncated. The two prime examples are the construction of the Bloch basis and the calculation of the solvation potential. The precision of the lattice summations is controlled by the ``Screening`` key 

.. scmautodoc:: band Screening


.. index:: Direct Method

Direct (on the fly) calculation of basis and fit
------------------------------------------------

BAND usually calculates basis functions and theirs derivatives on the fly. However, for small bulk systems it can be faster to write the information to disk. Then one can set the ``DirectBas`` key to false. (**Default = true**)

::

   Programmer
      DirectBas bool
   End


Fermi energy search
-------------------

.. scmautodoc:: band Fermi


Block size
----------

.. scmautodoc:: band CPVector

.. scmautodoc:: band KGrpX
