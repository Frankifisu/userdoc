.. index:: Restarts

Restarts
========

The main results of a BAND calculation are stored in the rkf file. If you save this file you can use it to restart your calculation. The input for the restart calculation is essentially the same, except for some extra keys, like ``Restart``, ``Grid``, and ``DensityPlot``. 

Plots of the density (and many other symmetric properties) can can be obtained with the key ``DensityPlot``. Density and orbital plot restarts require the specification of the ``Grid`` key. 
With the subkey ``SCF`` you can start the SCF procedure with the last solution from the restart file. This can be useful if the SCF did not converge or if you want to compute some post-SCF properties (e.g. the :ref:`DOS<band-key-DOS>` or the :ref:`band structure <band-key-BandStructure>`). Similarly, a geometry optimization can be restarted with the subkey ``GeometryOptimization`` You can use the geometry of a previous calculation.  

Usually the input for a restarted job is the same as for the original calculation, with some extra options, described in this section. 

Some examples are available in the ``$AMSHOME/examples/band`` directory and are discussed in the Examples section.

.. csv-table:: 

  :ref:`example RestartProperties`
  :ref:`example RestartSCF`
  :ref:`example BeO_tape41`

Restart key
^^^^^^^^^^^

.. scmautodoc:: band Restart File SCF DensityPlot OrbitalPlot NOCVdRhoPlot NOCVOrbitalPlot UseDensityMatrix


Grid
^^^^


The Grid block is used for restart options ``OrbitalPlot``, ``DensityPlot``, ``NOCVOrbitalPlot`` and ``NOCVdRhoPlot``. There are two ways to define your grid. The most easy way is to use the Type key, which automatically generates a grid around the atoms in the unit cell:

.. scmautodoc:: band Grid Type


One alternative is to specify everything by hand via the 'UserDefined' sub-block. 

.. scmautodoc:: band Grid UserDefined
  :noref:

The following input would create a cube from (-1,-1,-1) to (1,1,1)::

  Grid
    UserDefined 
       -1 -1 -1 ! Starting point
       1 0 0 0.1   ! vec1 and dvec1
       0 1 0 0.1   ! vec2 and dvec2
       0 0 1 0.1   ! vec3 and dvec3
       20 20 20    ! nr. of steps along three directions
    End
  End


One can also specify a text file from which the grid is imported:

.. scmautodoc:: band Grid FileName
  :noref:



.. index:: Plotting Densities

Plots of the density, potential, and many more properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. index:: ELF

.. scmautodoc:: band DensityPlot

The DensityPlot block goes together with the ``Restart%DensityPlot`` and ``Grid`` keys. Example input::

    ...
    Restart
       File my_file.rkf
       DensityPlot
    End

    Grid
       Type Coarse
    End

    DensityPlot
       rho(fit)
       vxc[rho]
    End
    ...


After such a run you get a TAPE41 file that you should rename to my.t41, and view with AMSview. 

.. _ELF:

The most common properties to plot are: 

+ ``rho(fit)``  The fitted density. 
+ ``v(coulomb)``  The Coulomb potential. 
+ ``vxc[rho(fit)]``  the XC potential (using the fitted density) 
+ ``vxc[rho]`` XC potential of the exact density 
+ ``rho``  The density 
+ ``|gradRho|``  The norm of the gradient of the density 
+ ``tau``  The symmetric kinetic energy density 
+ ``LDOS``  The local density of states. (See :ref:`LDOS key<band-key-LDOS>`)
+ ``elf[rho]`` The electron localization function  
+ ``X`` The electron energy density. Equivalently ``X(fit)`` may be used as an approximation, employing the density fit.

The electron energy density is defined as

:math:`X(r) = -\left\{ \frac{1}{2} \sum_i^\text{occ} \nabla \psi_i \cdot \nabla \psi_i - V_\text{effective} \rho   \right\}`


Some more specialized options are: 

+ ``rho(deformation/fit)`` the fitted deformation density  
+ ``rho(atoms)``  The density of the startup atoms 
+ ``v(coulomb/atoms)``  The Coulomb potential of the start density  
+ ``s[rho]``  Reduced density gradient. Common ingredient for XC functionals  
+ ``s[rho(fit)]``  Same as above, now for the fit density  
+ ``alpha[rho]``  Ingredient for some meta-GGAs

In the BAND example directory there is the :ref:`Frags_COCu <example Frags_COCu>` example which shows how this can be used in combination with the ``Fragment`` key.


.. index:: Plotting Crystal Orbitals

Orbital plots
^^^^^^^^^^^^^

.. scmautodoc:: band OrbitalPlot

The OrbitalPlot block goes together with the ``Restart%OrbitalPlot`` and ``Grid`` keys. Example input::

    ...
    Restart 
       File my_file.rkf
       OrbitalPlot
    End

    Grid
       Type Coarse
    End

    OrbitalPlot
       1 Band 5 8  ! for k-point 1 plot bands 5 to 8
       5 Band 6    ! for k-point 5 plot band 6
       6 -0.2 +0.3 ! for k-point 6 plot bands between -0.2 and +0.3 a.u. w.r.t Fermi level
    End
    ...

After such a run you get a TAPE41 file that you should rename to my.t41, and view with AMSview. 


.. index:: Plotting Crystal Orbitals

Induced Density Plots of Response Calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. scmautodoc:: band ResponseInducedDensityPlot


``ResponseInducedDensityPlot (block-type)``
The ResponseInducedDensityPlot block goes together with the ``Restart%ResponseInducedDensityPlot`` and ``Grid`` keys. In the BAND example directory there is the :ref:`TD-CDFT for MoS2 Monolayer<example NewResp_2DMoS2Restart>` example that shows how this can be used. Example input::

    ...
    Restart 
       File my_file.rkf
       ResponseInducedDensityPlot
    End

    Grid
       Type Coarse
    End

    ResponseInducedDensityPlot
       XCOMPONENT 5 8  ! plot x component of induced densities 
                       ! for frequencies number 5 to 8 
       YCOMPONENT 6    ! plot y component of induced densities 
                       ! for frequency number 6
       ZCOMPONENT 1    ! plot z component of induced densities 
                       ! for frequency number 1 
    End
    ...

After such a run you get a TAPE41 file that you should rename to my.t41, and view with AMSview. 

.. attention::
   
   The plotting capability works only with response calculation RUNKF files based on the :ref:`NewResponse<band-key-NewResponse>` method!

.. index:: Plotting NOCV Orbitals


NOCV Orbital Plots
^^^^^^^^^^^^^^^^^^

.. scmautodoc:: band NOCVOrbitalPlot


The NOCVOrbitalPlot blockg oes together with the ``Restart%NOCVOrbitalPlot`` and ``Grid`` keys. See example :ref:`PEDANOCV_MgO+CO<example PEDANOCV_MgO+CO>`. Example input::

      ...
      Restart 
         File my_file.rkf
         NOCVOrbitalPlot
      End

      Grid
         Type Coarse
      End

      NOCVOrbitalPlot
         1 Band 5 8 ! for k-point 1 plot NOCV Orbitals 5 to 8
      End
      ...

After such a run you get a TAPE41 file that you should rename to my.t41, and view with AMSview. 

.. index:: Plotting NOCV Deformation Densities

NOCV Deformation Density Plots
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. scmautodoc:: band NOCVdRhoPlot


The NOCVdRhoPlot blockg oes together with the ``Restart%NOCVdRhoPlot`` and ``Grid`` keys. See example :ref:`PEDANOCV_MgO+CO <example PEDANOCV_MgO+CO>`. Example input::

    ...
    Restart 
       File my_file.rkf
       NOCVdRhoPlot
    End

    Grid
       Type Coarse
    End

    NOCVdRhoPlot
       1 Band 5 8 ! for k-point 1 plot NOCV deformation densities 5 to 8
    End
    ...

After such a run you get a TAPE41 file that you should rename to my.t41, and view with AMSview. 

.. index:: LDOS
.. index:: STM

.. _LDOS:

LDOS (STM)
^^^^^^^^^^

The local density of states (LDOS) represents a partial density,  (`see wikipedia <https://en.wikipedia.org/wiki/Density_of_states#Local_density_of_states>`_): it is the density arising from states within an energy window. 


.. scmautodoc:: band LDOS

Integrating from minus infinity (DeltaNeg=1e6) to the fermi level (DeltaPos=0) produces the total (valence) density.


The local density of states is integrated over the resulting interval. Example of an LDOS restart::

      Restart 
         File my_file.rkf
         DensityPlot
      End

      Grid
         Type Coarse
      End

      DensityPlot
         LDOS
      End
      
      LDOS
         Shift    0.1 
         DeltaNeg 0.001 
         DeltaPos 0.0
      End

According to this example, we restart from the result file of a previous calculation. The calculation will generate a file TAPE41 which can be viewed with AMSview. (Rename the file to my.t41) 

See also :ref:`Restart <band-key-Restart>`, and :ref:`DensityPlot <band-key-DensityPlot>`. 


Save
^^^^

.. scmautodoc:: band Save
