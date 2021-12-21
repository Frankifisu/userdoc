Required Citations
******************

When you publish results in the scientific literature that were obtained with programs of the ADF package, you are required to include references to the program package with the appropriate release number, and a few key publications. 

In addition to these general references, references to special features are mandatory, in case you have used them. 


General References
==================

The ReaxFF software that SCM makes available is based on the ReaxFF program developed by Adri van Duin. 

For calculations with ReaxFF: 

1. A.C.T. van Duin, S. Dasgupta, F. Lorant, and W. A. Goddard,  *ReaxFF: A reactive force field for hydrocarbons*,  `Journal of Physical Chemistry A 105, 9396-9409 (2001) <https://doi.org/10.1021/jp004368u>`__ 

2. K. Chenoweth, A.C.T. van Duin, and W.A. Goddard,  *ReaxFF reactive force field for molecular dynamics simulations of hydrocarbon oxidation*,  `Journal of Physical Chemistry A 112, 1040-1053 (2008) <https://doi.org/10.1021/jp709896w>`__ 

3. ReaxFF |release|, SCM, Theoretical Chemistry, Vrije Universiteit, Amsterdam, The Netherlands,  `http://www.scm.com <http://www.scm.com>`__ Optionally, you may add the following list of authors and contributors: A.C.T. van Duin, W.A. Goddard, M.M. Islam, H. van Schoot, T. Trnka, A.L. Yakovlev 

The ReaxFF GUI (ReaxFFinput and AMSmovie) has been developed within SCM (with O. Visser as primary developer). 

The ReaxFF program has been parallelized, optimized, and extended  by SCM (with A.L. Yakovlev as primary developer). 

If you use one of the included force fields you must also add the :ref:`proper reference for it <forcefields>`. 

Many examples of ReaxFF applications can be found on  `Prof. van Duin's publication list <http://www.engr.psu.edu/adri/Publications.aspx>`__. 


Feature References
==================

When you have used force fields or special features, you should include the reference(s) to the implementation. 

Collective Variable-Driven Hyperdynamics (CVHD)
  K.M. Bal and E.C. Neyts, *Merging Metadynamics into Hyperdynamics: Accelerated Molecular Simulations Reaching Time Scales from Microseconds to Seconds*, `J. Chem. Theory Comput., 11, 4545-4554 (2015) <https://doi.org/10.1021/acs.jctc.5b00597>`__

Force-bias Monte Carlo (fbMC)
  M.J. Mees, G. Pourtois, E.C. Neyts, B.J. Thijsse, A. Stesmans, *Uniform-acceptance force-bias Monte Carlo method with time scale to study solid-state diffusion*,  `Physical Review B 85, 134301 (2012) <https://doi.org/10.1103/PhysRevB.85.134301>`__ 

Grand Canonical Monte Carlo (GCMC)
  Th.P. Senftle, R.J. Meyer, M.J. Janik and A.C.T. van Duin, *Development of a ReaxFF potential for Pd/O and application to palladium oxide formation*,  `J. Chem. Phys. 139, 044109 (2013) <https://doi.org/10.1063/1.4815820>`__ 

  Th.P. Senftle, A.C.T. van Duin, M.J. Janik, *Determining in situ phases of a nanoparticle catalyst via grand canonical Monte Carlo simulations with the ReaxFF potential*,  `Catalysis Communications **volume 52**, 5 July 2014, Pages 72–77 <https://doi.org/10.1016/j.catcom.2013.12.001>`__  

Monte-Carlo force-field optimizer (MCFFOptimizer) 
  E. Iype, M. Huetter, A.P.J. Jansen, S.V. Nedea, C.C.M. Rindt, *Parameterization of a Reactive Force Field Using a Monte Carlo Algorithm*,  `J. Comp. Chem. 34, 1143-1154 (2013) <https://doi.org/10.1002/jcc.23246>`__    

ACKS2
  T. Verstraelen, P.W. Ayers, V. Van Speybroeck, M. Waroquier, *ACKS2: Atom-Condensed Kohn-Sham DFT Approximated to Second Order* `J. Chem. Phys. 138, 074108 (2013) <https://doi.org/10.1063/1.4791569>`__

eReaxFF
  M.M. Islam, G. Kolesov, T. Verstraelen, E. Kaxiras, A.C.T. van Duin, *eReaxFF: A Pseudoclassical Treatment of Explicit Electrons within Reactive Force Field Simulations*, `J. Chem.Theory Comput 12, 3463 (2016) <https://doi.org/10.1021/acs.jctc.6b00432>`__

ReaxFF Force Field References
  When you publish results in the scientific literature that were obtained with one of the included force fields for  ReaxFF, including the proper reference for the force field used is mandatory.

  + :ref:`Forcefields included in the latest release <forcefields>`
  + :ref:`Forcefields included in the development snapshots <forcefields_development>`


Reaction Event Detection (ChemTraYzer)
  M. Döntgen, M.-D. Przybylski-Freund, L.C. Kröger, W.A. Kopp, A.E. Ismail, K. Leonhard 
  `Automated Discovery of Reaction Pathways, Rate Constants, and Transition States Using Reactive Molecular Dynamics Simulations <https://doi.org/10.1021/acs.jctc.5b00201>`__  J. Chem.Theory Comput., 11 (6), 2517–2524, 2015

External programs and Libraries
===============================

`Click here <../Ref_third_party/index.html>`_ for the list of programs and/or libraries used in the ADF package. 
On some platforms optimized libraries have been used and/or vendor specific MPI implementations.

