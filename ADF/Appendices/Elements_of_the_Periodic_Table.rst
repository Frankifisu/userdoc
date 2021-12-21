.. index:: periodic table 
.. _periodic table:


Elements of the Periodic Table
******************************

A few characteristics are predefined in ADF for all elements of the periodic table, as shown below. 

The electronic configuration defines the default occupation numbers in Create mode. Basis sets for the elements Bk-Ubn (Z=97-120) are only available in ``$AMSHOME/atomicdata/ADF/ZORA/``. 

.. csv-table:: 
   :widths: 50,60,100,200
   :header-rows: 3

   " ",Nuclear ,mass number of ,electronic
   " ",Charge Z,default isotope,configuration
   " ",          ,used for mass  ,
   H,1,1,1s\ :sup:`1` 
   He,2,4,1s\ :sup:`2` 
   Li,3,7,2s\ :sup:`1` 
   Be,4,9,2s\ :sup:`2` 
   B,5,11,2s\ :sup:`2` 2p\ :sup:`1` 
   C,6,12,2s\ :sup:`2` 2p\ :sup:`2` 
   N,7,14,2s\ :sup:`2` 2p\ :sup:`3` 
   O,8,16,2s\ :sup:`2` 2p\ :sup:`4` 
   F,9,19,2s\ :sup:`2` 2p\ :sup:`5` 
   Ne,10,20,2s\ :sup:`2` 2p\ :sup:`6` 
   Na,11,23,3s\ :sup:`1` 
   Mg,12,24,3s\ :sup:`2` 
   Al,13,27,3s\ :sup:`2` 3p\ :sup:`1` 
   Si,14,28,3s\ :sup:`2` 3p\ :sup:`2` 
   P,15,31,3s\ :sup:`2` 3p\ :sup:`3` 
   S,16,32,3s\ :sup:`2` 3p\ :sup:`4` 
   Cl,17,35,3s\ :sup:`2` 3p\ :sup:`5` 
   Ar,18,40,3s\ :sup:`2` 3p\ :sup:`6` 
   K,19,39,4s\ :sup:`1` 
   Ca,20,40,4s\ :sup:`2` 
   Sc,21,45,3d\ :sup:`1` 4s\ :sup:`2` 
   Ti,22,48,3d\ :sup:`2` 4s\ :sup:`2` 
   V,23,51,3d\ :sup:`3` 4s\ :sup:`2` 
   Cr,24,52,3d\ :sup:`5` 4s\ :sup:`1` 
   Mn,25,55,3d\ :sup:`5` 4s\ :sup:`2` 
   Fe,26,56,3d\ :sup:`6` 4s\ :sup:`2` 
   Co,27,59,3d\ :sup:`7` 4s\ :sup:`2` 
   Ni,28,58, "3d\ :sup:`9` 4s\ :sup:`1` , 3d\ :sup:`8` 4s\ :sup:`2` "
   Cu,29,63,3d\ :sup:`10` 4s\ :sup:`1` 
   Zn,30,64,3d\ :sup:`10` 4s\ :sup:`2` 
   Ga,31,69,3d\ :sup:`10` 4s\ :sup:`2` 4p\ :sup:`1` 
   Ge,32,74,3d\ :sup:`10` 4s\ :sup:`2` 4p\ :sup:`2` 
   As,33,75,3d\ :sup:`10` 4s\ :sup:`2` 4p\ :sup:`3` 
   Se,34,80,3d\ :sup:`10` 4s\ :sup:`2` 4p\ :sup:`4` 
   Br,35,79,3d\ :sup:`10` 4s\ :sup:`2` 4p\ :sup:`5` 
   Kr,36,84,3d\ :sup:`10` 4s\ :sup:`2` 4p\ :sup:`6` 
   Rb,37,85,5s\ :sup:`1` 
   Sr,38,88,5s\ :sup:`2` 
   Y,39,89,4d\ :sup:`1` 5s\ :sup:`2` 
   Zr,40,90,4d\ :sup:`2` 5s\ :sup:`2` 
   Nb,41,93,4d\ :sup:`4` 5s\ :sup:`1` 
   Mo,42,98,4d\ :sup:`5` 5s\ :sup:`1` 
   Tc,43,[98],4d\ :sup:`5` 5s\ :sup:`2` 
   Ru,44,102,4d\ :sup:`7` 5s\ :sup:`1` 
   Rh,45,103,4d\ :sup:`8` 5s\ :sup:`1` 
   Pd,46,106,4d\ :sup:`10` 
   Ag,47,107,4d\ :sup:`10` 5s\ :sup:`1` 
   Cd,48,114,4d\ :sup:`10` 5s\ :sup:`2` 
   In,49,115,4d\ :sup:`10` 5s\ :sup:`2` 5p\ :sup:`1` 
   Sn,50,120,4d\ :sup:`10` 5s\ :sup:`2` 5p\ :sup:`2` 
   Sb,51,121,4d\ :sup:`10` 5s\ :sup:`2` 5p\ :sup:`3` 
   Te,52,130,4d\ :sup:`10` 5s\ :sup:`2` 5p\ :sup:`4` 
   I,53,127,4d\ :sup:`10` 5s\ :sup:`2` 5p\ :sup:`5` 
   Xe,54,132,4d\ :sup:`10` 5s\ :sup:`2` 5p\ :sup:`6` 
   Cs,55,133,6s\ :sup:`1` 
   Ba,56,138,6s\ :sup:`2` 
   La,57,139,5d\ :sup:`1` 6s\ :sup:`2` 
   Ce,58,140,4f\ :sup:`1` 5d\ :sup:`1` 6s\ :sup:`2` 
   Pr,59,141,4f\ :sup:`3` 6s\ :sup:`2` 
   Nd,60,142,4f\ :sup:`4` 6s\ :sup:`2` 
   Pm,61,[145],4f\ :sup:`5` 6s\ :sup:`2` 
   Sm,62,152,4f\ :sup:`6` 6s\ :sup:`2` 
   Eu,63,153,4f\ :sup:`7` 6s\ :sup:`2` 
   Gd,64,158,4f\ :sup:`7` 5d\ :sup:`1` 6s\ :sup:`2` 
   Tb,65,159,4f\ :sup:`9` 6s\ :sup:`2` 
   Dy,66,164,4f\ :sup:`10` 6s\ :sup:`2` 
   Ho,67,165,4f\ :sup:`11` 6s\ :sup:`2` 
   Er,68,166,4f\ :sup:`12` 6s\ :sup:`2` 
   Tm,69,169,4f\ :sup:`13` 6s\ :sup:`2` 
   Yb,70,174,4f\ :sup:`14` 6s\ :sup:`2` 
   Lu,71,175,4f\ :sup:`14` 5d\ :sup:`1` 6s\ :sup:`2` 
   Hf,72,180,4f\ :sup:`14` 5d\ :sup:`2` 6s\ :sup:`2` 
   Ta,73,181,4f\ :sup:`14` 5d\ :sup:`3` 6s\ :sup:`2` 
   W,74,184,4f\ :sup:`14` 5d\ :sup:`4` 6s\ :sup:`2` 
   Re,75,187,4f\ :sup:`14` 5d\ :sup:`5` 6s\ :sup:`2` 
   Os,76,192,4f\ :sup:`14` 5d\ :sup:`6` 6s\ :sup:`2` 
   Ir,77,193,4f\ :sup:`14` 5d\ :sup:`7` 6s\ :sup:`2` 
   Pt,78,195,4f\ :sup:`14` 5d\ :sup:`9` 6s\ :sup:`1` 
   Au,79,197,4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`1` 
   Hg,80,202,4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`2` 
   Tl,81,205,4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`2` 6p\ :sup:`1` 
   Pb,82,208,4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`2` 6p\ :sup:`2` 
   Bi,83,209,4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`2` 6p\ :sup:`3` 
   Po,84,[209],4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`2` 6p\ :sup:`4` 
   At,85,[210],4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`2` 6p\ :sup:`5` 
   Rn,86,[222],4f\ :sup:`14` 5d\ :sup:`10` 6s\ :sup:`2` 6p\ :sup:`6` 
   Fr,87,[223],7s\ :sup:`1` 
   Ra,88,[226],7s\ :sup:`2` 
   Ac,89,[227],6d\ :sup:`1` 7s\ :sup:`2` 
   Th,90,232,6d\ :sup:`2` 7s\ :sup:`2` 
   Pa,91,231,5f\ :sup:`2` 6d\ :sup:`1` 7s\ :sup:`2` 
   U,92,238,5f\ :sup:`3` 6d\ :sup:`1` 7s\ :sup:`2` 
   Np,93,[237],5f\ :sup:`4` 6d\ :sup:`1` 7s\ :sup:`2` 
   Pu,94,[244],5f\ :sup:`6` 7s\ :sup:`2` 
   Am,95,[243],5f\ :sup:`7` 7s\ :sup:`2` 
   Cm,96,[247],5f\ :sup:`7` 6d\ :sup:`1` 7s\ :sup:`2` 
   Bk,97,[247],5f\ :sup:`9` 7s\ :sup:`2` 
   Cf,98,[251],5f\ :sup:`10` 7s\ :sup:`2` 
   Es,99,[252],5f\ :sup:`11` 7s\ :sup:`2` 
   Fm,100,[257],5f\ :sup:`12` 7s\ :sup:`2` 
   Md,101,[258],5f\ :sup:`13` 7s\ :sup:`2` 
   No,102,[259],5f\ :sup:`14` 7s\ :sup:`2` 
   Lr,103,[266],5f\ :sup:`14` 6d\ :sup:`1` 7s\ :sup:`2` 
   Rf,104,[267],5f\ :sup:`14` 6d\ :sup:`2` 7s\ :sup:`2` 
   Db,105,[268],5f\ :sup:`14` 6d\ :sup:`3` 7s\ :sup:`2` 
   Sg,106,[269],5f\ :sup:`14` 6d\ :sup:`4` 7s\ :sup:`2` 
   Bh,107,[270],5f\ :sup:`14` 6d\ :sup:`5` 7s\ :sup:`2` 
   Hs,108,[269],5f\ :sup:`14` 6d\ :sup:`6` 7s\ :sup:`2` 
   Mt,109,[278],5f\ :sup:`14` 6d\ :sup:`7` 7s\ :sup:`2` 
   Ds,110,[281],5f\ :sup:`14` 6d\ :sup:`8` 7s\ :sup:`2` 
   Rg,111,[282],5f\ :sup:`14` 6d\ :sup:`9` 7s\ :sup:`2` 
   Cn,112,[285],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 
   Nh,113,[286],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`1` 
   Fl,114,[289],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`2` 
   Mc,115,[290],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`3` 
   Lv,116,[293],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`4` 
   Ts,117,[294],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`5` 
   Og,118,[294],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`6` 
   Uue,119,[315],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`6`  8s\ :sup:`1`
   Ubn,120,[299],5f\ :sup:`14` 6d\ :sup:`10` 7s\ :sup:`2` 7p\ :sup:`6`  8s\ :sup:`2`
   
*Default (most abundant) isotope, used to set atomic mass (nr. of brackets gives mass directly).*
*Default electronic configurations used in Create mode.*

