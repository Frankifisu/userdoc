.. _metatag scripting_cocrystal: 

Screening for cocrystals
************************

In this section, we provide an example application that can be used as a template for many high-throughput screening scripts.  Cocrystals are crystals formed from two or more compounds in a defined stoichiometry.  There are many uses for cocrystals, especially for pharmaceutical applications where one compound is an active pharmaceutical ingredient (API).  This example problem screens multiple compounds for their potential as components of a (1:2) cocrystal with Itraconazole.  This problem uses the excess enthalpy for a hypothetical supercooled liquid phase as a proxy for cocrystallization affinity.  The rankings of the solvents are in good agreement with model and experimental results for this problem given in [#ref1]_ .


Python code
===========

.. raw:: html

   <details>
   <summary style="color:#008000;cursor:pointer">[show/hide code]</summary>


.. code-block:: python

     import os
     import matplotlib.pyplot as plt
     from scm.plams import *

     ##################  Note: Be sure to add the path to your own AMSCRS directory here  ##################
     database_path = os.getcwd()

     if not os.path.exists(database_path):
         raise OSError(f'The provided path does not exist. Exiting.')

     init()
     #suppress plams output
     config.log.stdout = 0

     # temperature
     sys_temp   = 298.15 # K

     # the solute we are trying to find a co-crystal for (Itraconazole)
     solute =  ["itz_1.coskf"]
             
     # a list of different conformers for the screening
     # each line contains 3 conformers of the same molecule
     solv_list=[
                ["tartaric_acid_1.coskf","tartaric_acid_2.coskf","tartaric_acid_3.coskf"],
                ["fumaric_acid_1.coskf","fumaric_acid_2.coskf","fumaric_acid_3.coskf"],
                ["succinic_acid_1.coskf","succinic_acid_2.coskf","succinic_acid_3.coskf"],
                ["malic_acid_1.coskf","malic_acid_2.coskf","malic_acid_3.coskf"],
                ["glutaric_acid_1.coskf","glutaric_acid_2.coskf","glutaric_acid_3.coskf"],
                ["malonic_acid_1.coskf","malonic_acid_2.coskf","malonic_acid_3.coskf"],
                ["adipic_acid_1.coskf","adipic_acid_2.coskf","adipic_acid_3.coskf"],
                ["maleic_acid_1.coskf","maleic_acid_2.coskf","maleic_acid_3.coskf"]
             ]


     print("Solvent".ljust(30),"Excess enthalpy (kcal/mol)")
     excess_h = []
     for solv in solv_list:

         name = "_".join(solv[0].split("_")[:-1])
         
         # initialize settings object
         settings = Settings()
         settings.input.property._h = 'VAPORPRESSURE'

         # set the number of compounds
         num_compounds = 2
         compounds = [Settings() for i in range(num_compounds)]
         compounds[0].name = "solvent"

         form_s = [Settings() for i in range(len(solv))]
         for j in range(len(solv)):
             form_s[j]._h = os.path.join( database_path, solv[j] )

         compounds[0].form = form_s

         compounds[1].name = "Itraconazole"

         form_sol = [Settings() for i in range(len(solute))]
         for j in range(len(solute)):
             form_sol[j]._h = os.path.join( database_path, solute[j] )

         compounds[1].form = form_sol
         # this is the stoichiometric ratio of the co-crystal
         compounds[0].frac1 = 0.33333
         compounds[1].frac1 = 0.66667

         # to change to the COSMOSAC2013 method
         settings.input.method = 'COSMOSAC2013'

         #temperature
         settings.input.temperature = str(sys_temp)
         # specify the compounds as the compounds to be used in the calculation
         settings.input.compound = compounds
         # create a job that can be run by COSMO-RS
         my_job = CRSJob(settings=settings)

         out = my_job.run()
         res = out.get_results()

         excess_h.append((res["excess H"],name))
         print (name.ljust(30),round(res["excess H"],5))

     plt.xlabel("Excess enthalpy (kcal/mol)")
     plt.barh([i for i in range(len(excess_h))],[x[0] for x in excess_h],zorder=3)
     plt.yticks([i for i in range(len(excess_h))],[x[1] for x in excess_h])
     plt.grid(axis='x',ls="--",zorder=0)
     plt.gca().invert_xaxis()

     plt.show()

     finish()


.. raw:: html

     </details>


This figure (produced by the code) shows the excess enthalpy values of all solvents in a supercooled liquid mixture with Itraconazole.  The lowest 4 excess enthalpy values correspond to 4 solvent for which a stable co-crystal with Itraconazole is known [#ref1]_ .

.. figure:: ../Images/as_cocrystal.png
 :width: 80%
 :align: center

References
==========

.. [#ref1] Abramov, Yuriy A., Christoph Loschen, and Andreas Klamt. "Rational coformer or solvent selection for pharmaceutical cocrystallization or desolvation." Journal of pharmaceutical sciences 101.10 (2012): 3687-3697.




