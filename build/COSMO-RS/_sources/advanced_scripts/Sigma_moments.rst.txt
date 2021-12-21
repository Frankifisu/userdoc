.. _metatag scripting_sigma_moments: 

Sigma Moments
*************

Sigma moments are useful chemical descriptors derived from the sigma profile.  They are analogous to moments of a statistical distribution and can be thought of as a way to reduce the high-dimensional information present in a sigma profile to a smaller number of descriptors that characterize that sigma profile.  Sigma moments are known to be valuable descriptors in QSPR and are thought to represent the solvent space well [#ref1]_.

The following script will calculate the first several sigma moments as well as a H-bond acceptor and H-bond donor moment for a few common molecules.


Python code
===========


.. code-block:: python

     import os
     import numpy as np
     from scm.plams import *
     ##################  Note: Be sure to add the path to your own AMSCRS directory here  ##################
     database_path = os.getcwd()

     if not os.path.exists(database_path):
         raise OSError(f'The provided path does not exist. Exiting.')


     init()

     #suppress plams output
     config.log.stdout = 0

     class SigmaMoments:

         def __init__(self,filenames,hb_cutoff=0.00854):
             self.filenames = filenames
             self.hb_cutoff = hb_cutoff


         def calculate_moments(self) -> dict:
             self.moments = {}
             self.calc_profiles_and_chdens()
             self.calc_standard_moments()
             self.calc_hb_moments()
             return self.moments


         def calc_profiles_and_chdens(self):

             # initialize settings object
             settings = Settings()
             settings.input.property._h = 'PURESIGMAPROFILE'
             # set the cutoff value for h-bonding
             settings.parameters.sigmahbond = self.hb_cutoff
             compounds = [Settings() for i in range(len(self.filenames))]
             for i,filename in enumerate(filenames):
                 compounds[i]._h = os.path.join(database_path, filename)

             settings.input.compound = compounds
             # create a job that can be run by COSMO-RS
             my_job = CRSJob(settings=settings)
             # run the job
             out = my_job.run()
             # convert all the results into a python dict
             res = out.get_results()
             # retain profiles and charge density values
             self.tot_profiles = res["profil"]
             self.hb_profiles  = res["hbprofil"]
             self.chdens       = res["chdval"]


         def calc_standard_moments(self,max_power=3):
             for i in range(max_power+1):
                 tmp_moms = []
                 for prof in self.tot_profiles:
                     tmp_moms.append( np.sum(prof*np.power(self.chdens,i)) )
                 self.moments["MOM_"+str(i)] = tmp_moms


         def calc_hb_moments(self):
             self.moments["MOM_hb_acc"] = []
             self.moments["MOM_hb_don"] = []
             zeros = np.zeros(len(self.chdens))
             for prof in self.hb_profiles:
                 self.moments["MOM_hb_acc"].append(np.sum( prof * np.maximum(zeros,self.chdens-self.hb_cutoff) ))
                 self.moments["MOM_hb_don"].append(np.sum( prof * np.maximum(zeros,-self.chdens-self.hb_cutoff) ))


     # the files we want to use to calculate sigma moments
     filenames = ["Water.coskf", "Hexane.coskf","Ethanol.coskf","Acetone.coskf"]

     sm = SigmaMoments(filenames)
     moms = sm.calculate_moments()
     max_mom_len = max([len(m) for m in moms])

     print()
     print( (" "*5).join(["Moment".ljust(max_mom_len)]+filenames))
     lens = [len(fn) for fn in filenames]
     for mom_name in moms:
         print( (" "*5).join([mom_name.ljust(max_mom_len)]+[('{0:.5g}'.format(m)).rjust(l) for m,l in zip(moms[mom_name],lens)]))

     finish()


References
==========

.. [#ref1] A.\  Klamt,  *COSMO-RS From Quantum Chemistry to Fluid Phase Thermodynamics and Drug Design, Elsevier.* Amsterdam (2005), ISBN 0-444-51994-7. 



