Force-bias Monte Carlo (fbMC)
*****************************

The Uniform-acceptance force-bias Monte Carlo (fbMC) method (`Phys. Rev. B 85, 134301 (2012) <https://doi.org/10.1103/PhysRevB.85.134301>`__) has been implemented in ADF ReaxFF by the group of Erik Neyts. 

Usually, ReaxFF optimizations are alternated with fbMC steps to accelerate events such as reactions. The acceleration (MC step) is controlled by the temperature and maximum displacement, which should be balanced to keep close to the real dynamics. fbMC does not scale time uniformly (`J. Chem. Phys. 141, 204104 (2014) <https://doi.org/10.1063/1.4902136>`__). Diffusion coefficients and reaction rates should probably use quartic mass scaling. 

fbMC mass scaling can be set. It defaults to quadratic scaling as in the original fbMC implementation. Setting *imcroo* to 4 would mean quartic mass scaling.

**Input keywords**

These keywords should be set at the end of the *control* file. fbMC control parameters can also be set in the GUI.

+ *drmax* – maximum displacement

+ *imcfrq* – frequency of fbMC steps

+ *imcstp* – number of fbMC steps

+ *imcroo* – mass scaling (defaults to 2, 4 is recommended as per the Bal & Neyts paper)


A worked out example for fbMC versus unaccelerated ReaxFF MD for healing graphene has been made for the `2-day ReaxFF workshop <https://www.scm.com/adf-modeling-suite/adf-hands-on-workshops/advanced-2-day-reaxff-workshop/>`__.
 
