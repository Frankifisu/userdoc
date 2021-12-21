
.. index:: Excited States

Advanced Occupation Options
===========================


By default the levels are occupied according to the aufbau principle. In some cases it is possible to create holes below the Fermi level or uneven occupation for alpha and beta electrons with the ``Occupations`` (:math:`\Gamma`-only) and alternatively the ``EnforcedSpinPolarization`` (for an arbitrary number of k-points) key.

.. scmautodoc:: band Occupations

Example::

    OCCUPATIONS   
       1 occupations_alpha {// occupations_beta}
    End

+ ``occupations_beta`` and the separating double slash (//) must not be used in a spin-restricted calculation. 

+ ``occupations_alpha/beta`` is a sequence of values assigned to the states ('bands') in energy ordering. 


.. scmautodoc:: band ElectronHole

See the example :ref:`Si_ElectronHole <example Si_ElectronHole>`