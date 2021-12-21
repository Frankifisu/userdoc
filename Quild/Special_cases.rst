Special cases
#############

Because the QUILD program serves as a wrapper around the ADF, NEWMM and ORCA programs, it has additional capabilities that may not be present within these programs themselves. A numerical evaluation of the energy gradients in QUILD enables the use of geometry optimization techniques for any methodology within either of these programs, also for those for which only the energy expression is known or implemented (for instance meta-GGA or hybrid functionals, or excited states within ADF) and for which geometry optimizations are otherwise out of reach (see for example ref.  [:ref:`27<reference 27>`]  for geometry optimizations with meta-GGA functionals, and ref. [:ref:`2<reference 2>`] for optimizations of excited state and spin-orbit geometries). It should be noted that because of the numerical evaluation of the gradients, requiring 6N+1 energy calculations per geometry step (with N the number of atoms), these calculations do require a significantly larger CPU-time. Note that the capabilities of ADF will change during the years, and some of the remarks above may not be completely true anymore. Spin-orbit coupled optimizations in ADF are possible in ADF2007. In ADF2009 some hybrid, meta-GGA and meta-hybrid functionals can be used during the SCF and for optimizations (analytical gradient). 

A second additional capability is the possibility to perform a geometry optimization for the pure spin states in systems that suffer from spin contamination. The spin contamination is simply projected out, not only for the energy but also for the gradient (and Hessian), by performing two consecutive jobs, one for the contaminated spin state, a second with the multiplicity increased (that is mixed in into the contaminated job). For instance, the following example gives an example input: 

::

   QUILD
   
     INTERACTIONS
       TOTAL  description 1
       S2CORR description 2
     SUBEND
   
     DESCRIPTION 1
       CHARGE 0.0 1.0
       Unrestricted
     SUBEND
     DESCRIPTION 2 
       CHARGE 0.0 3.0
       Unrestricted
     SUBEND
   
   END

See ref. [:ref:`25<reference 25>`] for an example of using this setup on a spin-contaminated system.  

