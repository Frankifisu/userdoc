.. _keyscheme TEMPERATURE: 

Temperature
***********

::

   TEMPERATURE temperature {temperature_high ntemp}

``temperature``
   Temperature (Kelvin) at which temperature the COSMO-RS calculation should take place. Default room temperature 298.15. The first temperature in case of a range of temperatures. 

``temperature_high``
   The last temperature (Kelvin) in case of a range of temperatures. Only used in case of solvent vapor pressure calculations or solubility calculations. 

``ntemp``
   The number of temperatures in case of a range of temperatures. 

