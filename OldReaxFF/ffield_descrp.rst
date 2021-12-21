
.. _ffield:

The Force Field File
********************

Each force field file consist of following sections: 


.. csv-table:: 
   :widths: 100,100,100,100, 100

   Section name, N of params, N of header lines, N of block keys, block keys
   General,      41,  1, 
   Atoms,        32,  4, 1, atom type name
   Bonds,        16,  2, 2, atom type index
   Off-diagonal,  6,  1, 2, atom type index
   Angles,        7,  1, 3, atom type index
   Torsions,      7,  1, 4, atom type index
   Hydrogen bonds,4,  1, 2, atom type index

Format
======

The force field file begins with a description line that, in turn, may optionally begin with a list of keywords between square brackets, for example (for an ACKS2+eReaxff force-field)::

  [ ereaxff acks2 ] Reactive MD-force field for Ethylene Carbonate and Li

Each section starts with one or more header line containing, on the first line, the number of blocks in the section, possibly followed by description of the parameters. The number of header lines is supposed to match the number lines in a block of the corresponding section (4 in atoms, 2 in bonds and 1 in every other section). The additional header lines after the first are skipped when reading the force field file.


**General parameters**

The header of this section starts with *npar*, the number of general parameters present in the force field file. The ehader is followed by *npar* lines each containing a parameter value followed by a comment, for example::

     39     ! Number of general parameters
    50.0000 !Overcoordination parameter


**Atoms**

The atomic parameters section starts with the number of atom types present in the force field, followed by three additional header lines and the blocks of parameters, one block per atom type. Each block consists of 4 lines starting with a line containing the atom name and 8 parameter values with the (1x,a2,8f9.4) format followed by three lines with 8 parameter values each, with the (3x,8f9.4) format, for example::

    3    ! Nr of atoms; cov.r; valency;a.m;Rvdw;Evdw;gammaEEM;cov.r2;#
           alfa;gammavdW;valency;Eunder;Eover;chiEEM;etaEEM;n.u.               
           cov r3;Elp;Heat inc.;n.u.;n.u.;n.u.;n.u.                            
           ov/un;val1;n.u.;val3,vval4 
     C    1.3817   4.0000  12.0000   1.8903   0.1838   0.   9000   1.1341   4.0000
          9.7559   2.1346   4.0000  34.9350  79.5548   5.   9666   7.0000   0.0000
          1.2114   0.0000 202.5551   8.9539  34.9289  13.   5366   0.8563   0.0000
         -2.8983   2.5000   1.0564   4.0000   2.9663   0.   0000   0.0000   0.0000
     H    0.7853   1.0000   1.0080   1.5904   0.0419   1.0206  -0.1000   1.0000     
          9.3557   5.0518   1.0000   0.0000 121.1250   5.3200   7.4366   1.0000     
         -0.1000   0.0000  62.4879   1.9771   3.3517   0.7571   1.0698   0.0000     
        -15.7683   2.1488   1.0338   1.0000   2.8793   0.0000   0.0000   0.0000     
    ... one more block ...


**Bonds, angles, etc.**

In the remaining sections, a block key consists of two or more integer numbers, each of them referring to the atomic block with this index. The number of integers in the key depends on the block type (two for bonds, three for valence angles, etc.).
For instance, the bond parameters block below corresponds to the C-H bond for the atoms block shown above.

The bond parameters section starts with the number of bond types followed by one additional comment line. The first line of the block has the (2i3,8f9.4) format and the second (6x,8f9.4)::

      6      ! Nr of bonds; Edis1;  LPpen;n.u.;pbe1;pbo5;13corr;pbo6
              pbe2;pbo3;pbo4;n.u.;pbo1;pbo2;ovc  orr
      1  1 156.5953 100.0397  80.0000  -0.8157  -0.4591   1.0000  37.7369   0.4235  
             0.4527  -0.1000   9.2605   1.0000  -0.0750   6.8316   1.0000   0.0000  
    ... five more blocks ...


For the rest of the sections, the format remains similar to the bonds section, except that they do not have additional header lines and the Fortran format may be slightly different: (2i3,6f9.4) for off-diagonal,(3i3,7f9.4) for valence angles, (4i3,7f9.4) for torsion angles, and (3i3,4f9.4) for hydrogen bonds.


Equation Reference
==================

In the tables below the ReaxFF parameters are listed with their corresponding equation numbers from the SCM developer notes which have mostly technical relevance. 
For a good introduction to the meaning of ReaxFF parameters we advise the initial ReaxFF publication `ReaxFF: A Reactive Force Field for Hydrocarbons, A.C.T. van Duin, S. Dasgupta, F. Lorant, W.A. Goddard, J. Phys. Chem. A. 2001 105 41 9396-9409. <https://doi.org/10.1021/jp004368u>`__  

**General**

Of particular interest are the upper taper radius parameter (#13), which describes the non-bonded cutoff radius, and the bond order cutoff (#30), which describes the bond order threshold, above which atoms are considered connected. Both these parameters may have a major impact on the ReaxFF calculation speed; decreasing the taper radius or increasing the bond order cutoff can make ReaxFF run considerably faster. These parameters, however, have a significant impact on the force description and should not be changed without re-parameterization of other parts of the force field.

.. csv-table:: 
   :widths: 100,100,100,200

   Index, Name in Eq, Equation, Comment
   1,p_boc1,4c,Overcoordination parameter
   2,p_boc2,4d,Overcoordination parameter  
   3,-p_coa2,15,Valency angle conjugation parameter                                 
   4,p_trip4,20,Triple bond stabilization parameter                                 
   5,p_trip3,20,Triple bond stabilization parameter                                 
   6,k_c2,19,C2-correction                                                       
   7,p_ovun6,12,Undercoordination parameter                                         
   8,p_trip2,20,Triple bond stabilization parameter                                 
   9,p_ovun7,12,Undercoordination parameter                                         
   10,p_ovun8,12,Undercoordination parameter
   11,p_trip1,20,Triple bond stabilization energy
   12,n/a,21,Lower Taper-radius
   13,R_cut,21,Upper Taper-radius
   14,p_fe1,6a,Fe dimer correction                                                         
   15,p_val6,13c,Valency undercoordination                                           
   16,p_lp1,8,Valency angle/lone pair parameter                                   
   17,p_val9,13f,Valency angle parameter
   18,p_val10,13g,Valency angle parameter                                             
   19,p_fe2,6a,Fe dimer correction                                                           
   20,p_pen2,14a,Double bond/angle parameter                                         
   21,p_pen3,14b,Double bond/angle parameter: overcoord                              
   22,p_pen4,14b,Double bond/angle parameter: overcoord                              
   23,p_fe3,6a,Fe dimer correction                                                       
   24,p_tor2,16b,Torsion/BO parameter                                                
   25,p_tor3,16c,Torsion overcoordination                                            
   26,p_tor4,16c,Torsion overcoordination                                            
   27,p_elho,26a,eReaxFF                                       
   28,p_cot2,17b,Conjugation                                                         
   29,p_vdW1,23b,VdW shielding
   30,cutoff * 100,"3a,b",Cutoff for bond order (* 100)
   31,p_coa4,15,Valency angle conjugation parameter                                 
   32,p_ovun4,11b,Overcoordination parameter                                          
   33,p_ovun3,11b,Overcoordination parameter                                          
   34,p_val8,13d,Valency/lone pair parameter                                         
   35,X_soft,25,ACKS2 softness parameter                                                            
   36,unused,n/a, n/a
   37,p_val, 27 via n_el,eReaxFF
   38,n/a,13d,if 1: remove delta_j term for non-C-C-C angles and where none of the atoms is N
   39,p_coa3,15,Valency angle conjugation parameter
   40,n/a,20,Condition to turn triple bond option: vpar(40) == 1
   41,n/a,26 via Tap(R),eReax-specific taper radius for interactions with/between electrons and holes


**Atoms**

If negative values are provided to either of the three bond radii (**sigma, pi, and double pi**) the bond order contributions are ignored for that atom.

.. csv-table:: 
   :widths: 100,100,100,200

   Index, Name in Eq, Equation, Comment
   1,r_0^sigma,2, **Sigma bond covalent radius** 
   2,Val_i,"3a, 4b, 5, 9a",Valency
   3,n/a,9a,Atomic mass
   4,r_vdW,23a,van der Waals radius
   5,D_ij,23a,van der Waals dissociation energy
   6,gamma_i,24,gammaEEM; EEM shielding
   7,r_0^pi,"2", **Pi bond covalent radius**
   8,Val_i^e,"7, 8, 9",Number of valence electrons
   9,alpha_ij,23b,van der Waals parameter
   10,1/gamma_w,23b,van der Waals shielding
   11,Val_j^angle,"16c, 13c","Valency for 1,3-BO correction"
   12,p_ovun5,12,Undercoordination energy
   13,p_i^xel2,26,"eReaxFF, atom type parameter"
   14,chi_i,"24, 25",EEM electronegativity
   15,eta_i,"24, 25",EEM hardness
   16,n/a,n/a,Donor or acceptor switch in H-bonds
   17,r_0^pi,2, **Double pi bond covalent radius**
   18,p_lp2,10,Lone pair energy
   19,n/a,n/a,Atomic heat of formation
   20,p_boc4,"4e,f",Bond order correction
   21,p_boc3,"4e,f",Bond order correction
   22,p_boc5,"4e,f",Bond order correction 
   23,C_i,25,Atomic softness cutoff parameter             
   24,"alpha, alpha_i","26, 26a","eReaxFF, constant, dependent on atom type"
   25,p_ovun2,12,Valence angle parameter
   26,p_val3,13b -> 13a,Valence angle parameter
   27,"beta, beta_i",26a,"eReaxFF, constant, dependent on atom type"
   28,Val_i^'boc,3b,Number of lone pairs
   29,p_val5,13b,Valence angle parameter
   30,p_c1,23c,Inner wall vdW repulsion parameter
   31,p_c2,23c,Inner wall vdW repulsion parameter
   32,p_c3,23c,Inner wall vdW repulsion parameter
   33,C_i,23d,Lg dispersion parameter
   34,R_eij,23d,VdW Radius for Lg dispersion correction


**Bonds**

.. csv-table:: 
   :widths: 100,100,100,200

   1,D_e^sigma,"6, 11a",Sigma-bond dissociation energy
   2,D_e^pi,6,Pi-bond dissociation energy 
   3,D_e^pipi,6,Double pi-bond dissociation energy 
   4,p_be1,6,Bond energy parameter
   5,p_bo5,2,Double pi bond parameter
   6,Val'_i^boc,3b,"1,3-Bond order correction"
   7,p_bo6,2,Double pi bond order 
   8,p_ovun1,11a,Overcoordination penalty
   9,p_be2,6,Bond energy parameter
   10,p_bo3,2,Pi bond order parameter
   11,p_bo4,2,Pi bond order parameter
   12,unused,n/a, n/a
   13,p_bo1,2,Sigma bond order
   14,p_bo2,2,Sigma bond order
   15,delta'_i,3a,Uncorrected BO overcoordination
   16,p_ij^xel1,27,e ReaxFF param; for adjusting number of electrons available to host atom 

**Off-diagonal**

This section allows for the definition of off-diagonal values for both bond order and van der Waals pair interactions. By default, ReaxFF calculates these terms from the combination rules and the atom parameters (i.e. the default C-H van der Waals radius is (RvdW[C]*RvdW[H])0.5), but the off-diagonal section allows for the definition of different values. Any value given in the off-diagonal section overrules that obtained from the combination rules.

.. csv-table:: 
   :widths: 100,100,100,200

   1,D_ij,23a,VdW energy
   2,r_vdW,23a,VdW radius
   3,alpha_ij,23a,VdW parameter
   4,r_0^sigma,2,Sigma bond length
   5,r_0^pi,2,Pi bond length
   6,r_0^pipi,2,PiPi bond length
   7,"C_i, C_lg,ij",23d,Lg dispersion parameter


**Angles**

.. csv-table:: 
   :widths: 100,100,100,200

   1,"Theta_0,0",13g,180o-(equilibrium angle)
   2,p_val1,13a,Valence angle parameter
   3,p_val2,13a,Valence angle parameter
   4,p_coa1,15,Valence conjugation
   5,p_val7,13c,Undercoordination 
   6,p_pen1,14b -> 14a,Penalty energy 
   7,p_val4,13b,Valence angle parameter

**Torsions**

.. csv-table:: 
   :widths: 100,100,100,200

   1,V_1,16a,V1-torsion barrier
   2,V_2,16a,V2-torsion barrier
   3,V_3,16a,V3-torsion barrier 
   4,p_tor1,16a,Torsion angle parameter
   5,p_cot1,17a,Conjugation energy
   6,unused, n/a, n/a
   7,unused, n/a, n/a

**Hydrogen bonds**

.. csv-table:: 
   :widths: 100,100,100,200

   1,r_hb^0,18,Hydrogen bond equilibrium distance
   2,p_hb1,18,Hydrogen bond energy
   3, -p_hb2,18,Hydrogen bond/bond order 
   4, -p_hb3,18,Hydrogen bond parameter

