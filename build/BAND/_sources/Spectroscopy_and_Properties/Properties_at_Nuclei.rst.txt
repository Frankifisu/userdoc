.. index:: Properties at Nuclei

.. _properties at nuclei:

Properties at Nuclei
====================

``PropertiesAtNuclei (block-type)``
  A number of properties can be obtained near the nucleus. An average is taken over a tiny sphere around the nucleus. The following properties are available. 
  ::

   PropertiesAtNuclei
     vxc[rho(fit)]
     rho(fit)
     rho(scf)
     v(coulomb/scf)
     rho(deformation/fit)
     rho(deformation/scf)
   End
   
  The electron density, ``rho(scf)``, is physically the most relevant one. 
