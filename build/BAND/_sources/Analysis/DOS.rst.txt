.. index:: DOS

.. _DOS:

Density of States (DOS)
=======================

.. scmautodoc:: band DOS

An example input::

   DOS
      Enabled     True
      Energies    500   
      Min        -0.35   
      Max         1.05
      File        plotfile
   End 

According to this example, DOS values will be generated in an equidistant mesh of 500 energy values, ranging from 0.35 a.u. below the Fermi level to 1.05 a.u. above it. All information will be written to a file plotfile. The information on the plot file is a long list of pairs of values (energy and DOS), with some informative text-headers and general information. DOS values are generated for the total DOS and optionally also for some partial DOS (see the keys :ref:`GrossPopulations<band-key-GrossPopulations>` and :ref:`OverlapPopulations<band-key-OverlapPopulations>`).

.. index:: PDOS

In the **DOS** and **Band Structure** **GUI modules**, it is possible to visualize partial density of states (**p-DOS**). The partial contributions are obtained from the total DOS by following the **Mulliken population analysis** partitioning prescription (`see wikipedia <https://en.wikipedia.org/wiki/Mulliken_population_analysis>`_). 

.. tip::
  
  The tutorial `Calculation of Band Structure and COOP of CsPbBr3 with BAND <../../Tutorials/Analysis/BandsAndCOOP.html>`_ contains some advanced usage of the **DOS** and **BAND Structure** **GUI modules**.

Gross populations
-----------------

.. scmautodoc:: band GrossPopulations

Syntax::

   GrossPopulations   
      {iat lq}   
      {FragFun jat ifun}
      {Frag kat}
      {Sum       
       ...
       EndSum}
   End

``iat``
  pDOS is generated for atom *lq*.

``FragFun``
  pDOS is generated for atom *jat* with all real spherical harmonics belonging to :math:`l`-value *ifun*.

``Frag``
  pDOS of the functions belonging to atom *kat* will be calculated.

``Sum``
  sum all pDOS, specified in this block.

Example::

   GrossPopulations   
      FragFun 1 2:: Second function of first atom   
      Frag 2 :: Sum of all functions from second atom   
      SUM:: sum following PDOSes      
         Frag 1::Atom nr.1      
         FragFun 2 1::First function of second atom      
         5 1:: All pfunctions of fifth atom   
      EndSum
   End

.. index:: COOP
.. index:: OPWDOS

Overlap populations
-------------------

.. scmautodoc:: band OverlapPopulations

*Overlap population weighted* DOS are generated for the overlap populations listed::

  OVERLAPPOPULATIONS  
     Left      
        { iat lq }      
        { FragFun jat ifun }      
        { Frag kat }  
     Right      
        ...
  End

You can use this to get the OPWDOS of two functions, or, if you like, one bunch of functions with another bunch of functions. The key-block should consist of left-right pairs. After a line with left you enter lines that specify one or more functions (according to :ref:`GrossPopulations<band-key-GrossPopulations>`), followed by a similar structure beginning with right, which will produce the OPWDOS of the left functions with the right functions. 

Example::

  OVERLAPPOPULATIONS   
     LEFT::First OPWDOS      
        Frag 1  
     RIGHT      
        Frag 2  
     LEFT:: Next OPWDOS      
        FragFun 1 1  
     RIGHT      
        2 1      
        FragFun 3 5
  End
