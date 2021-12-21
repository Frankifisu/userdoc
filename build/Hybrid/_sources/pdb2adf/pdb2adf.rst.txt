pdb2adf: transform PDB file to QMMM input file
##############################################

.. _metatag PDB2ADF: 

The pdb2adf utility program was written by Marcel Swart. 

Overview
********

General description
===================

Starting from the ADF2005.01 version the utility pdb2adf is available in the official release. Previously this utility could be found on the contributed software page.
Starting from AMS2020 the default is to make an amsified ADF input, which can not be used with previous versions.
One can get the old style input if the environment variable SCM_PDB2ADF is set to OLD (only to be used with ADF<=2019).
One can get the NEWQMMM style input input if the environment variable SCM_PDB2ADF is set to NEW (only to be used with ADF<=2019).

The pdb2adf utility was written to read a  `PDB file <http://www.pdb.org>`__, which contains the atomic coordinates of a protein structure, and transform it into an ADF inputfile, particularly for use with QMMM calculations. It can also be used for setting up a solvent shell around a solute molecule. 

The PDB files are generally used for protein structures, and are formatted according to certain rules, see:  `http://www.wwpdb.org/docs.html <http://www.wwpdb.org/docs.html>`__, and the part about the official PDB format below. 

For every residue/molecule present in the PDB file, there should be a fragment file available, either in the general AMS library ($AMSHOME/atomicdata/pdb2adf directory), or in the local directory where the pdb2adf program is being called. Fragment files in the local directory take higher priority than those in the general AMS library. The fragment files are formatted, based loosely on AMBER parameter files, and contain information about the residues; e.g., the atoms present, with their general and forcefield atomnames, atomic charges, connections to other atoms for creating their positions when not found on the PDB file, etc.; see part about fragment files below. Available in the AMS library are fragment files for amino acid residues, including those at the N- or C-terminal residue, three solvents (water, methanol, chloroform), some ions that are present frequently in protein structures (copper, fluoride), etc. 

Also present in the AMS library are solvent box files that can be used to place a layer of solvents surrounding the protein, or a solute. Available are the three solvents mentioned above. 

After reading the PDB and corresponding fragment files, the program tries to figure out which atoms are missing, and will add those; it uses the information provided on the fragment files to do so. For certain amino acid residues, there are several protonation states possible, e.g. histidine can be protonated at the N-delta position, at the N-epsilon position, or on both. The default option is to choose the fully charged option for aspartate (Asp), glutamate (Glu), lysine (Lys) residues, and decide for each histidine (His) and cysteine (Cys) residue individually what the protonation state should be. In those individual cases, the distances of neighboring molecules/residues are given that may help determine the protonation state. See the protein example below. 

After all that is setup properly, a list is given with residue names/numbers, from which you can choose those that should be placed in the QM system; afterwards, for each of the selected QM residues, a choice should be made where to cut-off the QM part. The most appropriate point to cut-off seems to be at the C-alpha position, except when dealing with a proline (Pro). The latter residue is cyclic, e.g. the sidechain is connected to the C-alpha carbon ! For that residue, it may be better to include the C-alpha, H-alpha, and backbone carbonyl group of the preceding residue in the QM part. 

The program will try to use to replace the ".pdb" extension of the PDB file by ".pdb2adf" for the AMS inputfile to be made; for convenience, the program also writes out an ".p2a.pdb" file with the complete system as it being made by the program. This file can then be visualized by conventional viewer programs (such as iMol, VMD, Molekel, AMSview) for visual inspection if everything has been carried out correctly. 

Given below are two examples, one for the application of a protein, the other how to set up a solvent shell run. 

Things to notice
================

+ The QMMM implementation in AMS2020 is new. It uses the AMS Hybrid engine.

+ By default pdb2adf makes an AMS Hybrid Engine input format.

+ The pdb2adf program uses AMBER parameter files, and is setup to work with the AMBER force field, version AMBER95, which is designed for and works well for biosystems.

+ For questions, remarks, contact:  `support@scm.com <mailto:support@scm.com>`__.


For ADF<=2019 only:

+ The old style QMMM input format is used if the environment variable SCM_PDB2ADF is set to OLD.

+ The NEWQMMM style QMMM input format is used if the environment variable SCM_PDB2ADF is set to NEW.

Official PDB format
===================

.. csv-table:: 
   :widths: 70,100,150,230

   "Columns","Data Type","Field","Definition"
   1 -  6,Record name,'ATOM' or 'HETATM', 
   7 - 11,Integer,serial,Atom serial number.
   13 - 16,Atom,name,Atom name.
   17,Character,altLoc,Alternate location indicator.
   18 - 20,Residue name,resName,Residue name.
   22,Character,chainID,Chain identifier.
   23 - 26,Integer,resSeq,Residue sequence number.
   27,AChar,iCode,borderleft for insertion of residues.
   31 - 38,Real(8.3),x,Orthogonal coordinates for X in Angstroms.
   39 - 46,Real(8.3),y,Orthogonal coordinates for Y in Angstroms.
   47 - 54,Real(8.3),z,Orthogonal coordinates for Z in Angstroms.
   55 - 60,Real(6.2),occupancy,Occupancy.
   61 - 66,Real(6.2),tempFactor,Temperature factor.
   73 - 76,LString(4),segID,"Segment identifier, left-justified."
   77 - 78,LString(2),element,"Element symbol, right-justified."
   79 - 80,LString(2),charge,Charge on the atom.
   
Typical examples from PDB-files: 

::

            1         2         3         4         5         6         7         8
   12345678901234567890123456789012345678901234567890123456789012345678901234567890
   
   ATOM     76  O   GLY    A9       6.671  55.354  35.873  1.00 14.75      A
   ATOM     77  N   ASN   A10       6.876  53.257  36.629  1.00 16.09      A
   ATOM     62  O   GLY A   9       6.791  55.214  35.719  1.00 15.61      4AZU 153
   ATOM     63  N   ASN A  10       6.892  53.135  36.555  1.00 12.64      4AZU 154

The pdb2adf utility is flexible, and should be able to read most PDB files, even those with incomplete or erroneous line formats. From every ATOM/HETATM line, it tries to read: 

+  atom number 

+  atom name 

+  residuename 

+  chain identifier 

+  residue number 

+  X,Y,Z coordinates 

Hints for proper formatting: 

+  always group together atoms that belong to one residue

+  always give the atom name on columns 13-16

+  when specifying a chain-id use only letters (or a blank)

Contents of fragment file
=========================

Given below is the contents of the fragment file for water. The first line is a comment line, the only important parameter is the NOCONNECT keyword, which indicates that the program should not try to make any connections to other residues/molecules. Then follow three lines, that define the orientation in space of the residue; they are not used for general fragments, but are relevant and important for amino acid residues and DNA nucleotides. Finally, for each atom in the molecule, there should be a line with its number in the fragment; its name to be used in PDB files; the AMBER forcefield atomtype; a dummy atomname; connections and coordinates (bond, angle, dihedral angle) to other atoms in the molecule that can be used to give the position of the atom if it is not present in the PDB file; the atomic charge; and after the exclamation mark (!) the connections to other atoms in this fragment, or other fragments in case of amino acid residues/DNA nucleotides. The current version does not use the latter connections yet, but the next version will probably use them. 

::

   HOH  Water molecule  NOCONNECT
      1   DUMM  DU    M      0   0   0       0.0000      0.0000      0.0000
      2   DUMM  DU    M      1   0   0       1.4490      0.0000      0.0000
      3   DUMM  DU    M      2   1   0       1.5220    111.1000      0.0000
      4   O     OW    O      0   0   0       0.0000      0.0000      0.0000  -0.8340  !  5  6
      5   H1    HW    H      4   0   0       0.9572      0.0000      0.0000   0.4170  !  4
      6   H2    HW    H      4   5   0       0.9572    104.5200      0.0000   0.4170  !  4

Contents of solvent box files
=============================

The first line is a comment line, followed by a line with the total number of atoms in the solvent box and the dimensions of the box (in Angstroms); then for each atom in the box, the atom name, which must match the PDB atomname, and the Cartesian coordinates, again in Angstroms. 

Usage of pdb2adf
****************

Short description
=================

The program works interactively, and should be straightforwardly to use. However, for some of the stages in the output a short description is given below. 

::

                                     P D B 2 A D F - program
                                        version 2008.01
                                 Written by: Marcel Swart, 2008
   
                            This program uses AMBER parameter files
                               see: http://amber.scripps.edu
   
   Do you want a logfile to be written (Y/n) ?

This option exists to create a logfile of what pdb2adf does. However, it should normally be used only for debugging purposes. 

::

   Ignoring atom on line: 
   ATOM    974   OH LYS A 128     -10.073 42.775 15.690 1.00 38.79     5AZU1065 

This is a warning that the atom on that particular line is ignored, should normally occur only few times  (less than ten). Depends also on how well the PDB file follows the PDB format rules. 

::

   Data Processed:
        Nat:       2519
       Nmol:        196
    NChains:          1

Information about what has been read on the PDB file: the total number of atoms (Nat), number of  molecules/residues (Nmol) and number of protein chains (Nchains). 

::

   Please wait, making connection tables

At this point, the connections between the atoms are being made by looking at atom distances. It may  take a while, depending on the size of the system. 

::

   Do you want to make separate files for each chain (Y/n) ?

You have the option to make different inputfiles for different protein chains, but you can also make  one inputfile for all of them together. 

::

   Found the following terminal amino acid residues : (C-term) 128 (N-term) 1 
   Do you want to use these as terminal residues (Y/n) ? 

Info is given about the C- and N-terminal residue of each chain. Reported for making sure they are  chosen correctly. Note, if the C- and N-terminal residues are connected (rarely the case probably),  enter N here. 

::

   Multiple AMBER options for HIS :
     0         Decide every time differently
     1   HID   Histidine Delta Hydrogen
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens
   
   Suggested option: 0

For a number of residues (His, Glu, Asp, Lys and Cys) there is more than one option available in the  AMBER95 force field, depending on the protonation state (His, Glu, Asp and Lys) or the existence of a  sulphur bridge/connection to a metal atom (Cys). The default is to choose a different option for the His  and Cys residues, and use one option for Glu, Asp and Lys (fully charged). However, if wanted you can  make a choice for all residues. 

::

   Multiple AMBER options for CYS    3 (    3) :
     1   CYS   Cysteine (SH)
     2   CYM   Deprotonated Cysteine (S-)
     3   CYX   Cystine (S-S bridge)
   
     Connections and Nearest Atoms for SG CYS    3 SG  ( P2A #   41 PDB#   20 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.82      38      19  CB  CYS    3  CB       1       3.79    2382     980  O   HOH  151  O
    2    2.02     461     193  SG  CYS   26  SG       2       3.80      22       0  HC  GLN    2
                                                      3       4.04    2391     983  O   HOH  154  O
                                                      4       4.15     509     206  O   GLN   28  O
                                                      5       4.18     522       0  HA  PHE   29
   Suggestion: 3

The options for Cys3 are given, with information about the atoms bonded to the SG sulphur atom (on  the left), as well as the closest five non-bonded atoms (on the right). This information may help you  decide which choice to make for this particular residue. Also given (on the bottom) is the suggested  choice, which is based, in this case, on the presence of a sulphur bridge. 

::

   Multiple AMBER options for HIS   46 (   46) :
     1   HID   Histidine Delta Hydrogen
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens
   
     Connections and Nearest Atoms for ND HIS   46 ND1 ( P2A #  844 PDB#  347 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.37     843     346  CG  HIS   46  CG       1       2.62    2166       0  H1  MET  121
    2    1.33     846     349  CE  HIS   46  CE1      2       3.23    2080     863  ND  HIS  117  ND1
    3    2.04    2318     959  CU  CU   130  CU       3 HB    3.33    2163     900  S   MET  121  SD
                                                      4       3.40    2164     901  CT  MET  121  CE
                                                      5       3.57    2082     865  CE  HIS  117  CE1
   
     Connections and Nearest Atoms for NE HIS   46 NE2 ( P2A #  848 PDB#  350 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.32     846     349  CE  HIS   46  CE1      1 HB    2.70     162      67  O   ASN   10  O
    2    1.37     850     348  CD  HIS   46  CD2      2       2.83     814       0  H1  MET   44
                                                      3       3.23    2166       0  H1  MET  121
                                                      4       3.52     822     332  O   MET   44  O
                                                      5       3.74     813     334  CT  MET   44  CG
   Suggestion: 2

For His residues, the information is given for both the delta- and the epsilon nitrogen atoms. Also  indicated (by HB) is the presence of a hydrogen bond with another atom. The definition used here is  that two atoms are hydrogen bonded if they are both non-carbon/non-hydrogen atoms, and the  distance between them is less than the sum of the van der Waals radii of the atoms. It is a simple  definition, but seems to be effective. In this case, as the N(delta) is bonded to copper, the proton  should be attached to the N(epsilon). 

::

   Making choice for which molecules should be QM, which MM

Now we come to the part where the division in the QM and MM systems is made. 

::

   Residues belonging to chain  0
   Option  Molecule    Option  Molecule    Option  Molecule    Option  Molecule    Option  Molecule
        1: ALA    1        28: GLN   28        55: ASP   55        82: ALA   82       109: ALA  109
        2: GLN    2        29: PHE   29        56: LYS   56        83: HIS   83       110: TYR  110
   etc

All molecules/residues belonging to chain 0 are given, with an option number. 

::

   Give option number of molecules to be put in QM region (or 'c' to continue):
   Note: by specifying a negative number a molecule is removed from the QM region

Here you are asked to enter the option numbers of the residues you want to put in the QM system. 

::

   Putting GLY   45 in QM region
   Putting HIS   46 in QM region

In this case, Gly45 and His46 have been put in the QM system. 

::

   Make a choice for the QM/MM treatment of GLY   45
    0:  Put completely in QM region
    1:  Cut off at C-alpha (put NH in QM region, CO in MM region)  
    2:  Cut off at C-alpha (put NH in MM region, CO in QM region)
    3:  Cut off at C-alpha (put NH and CO in MM region)
    4:  Cut off at C-alpha (put NH and CO in QM region,  sidechain in MM region)
    5:  Put only part of sidechain in QM region
       
   Suggestion: 2
   Give choice:  

A choice should be made for where to cut-off the QM system. Normally this is done at the C(alpha)  position, and you should simply choose the Suggestion. 

::

   Solvent molecules (SOL/HOH) belonging to this chain:
       1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20
      21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40
      41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59   60
      61   62   63   64   65   66
   
   Give the number of the molecule to be put in QM region (or 'c' to continue):

Also water molecules can be put in the QM system. 

::

   Box Shape options:
    1  Spherical box
    2  Cubic box
   Make a choice:

Type of box to be used. 

::

   Maximum atomic distance (Angs) from center       25.62
   Give boxsize (def.:    28.62 Angs)

Size of box to be used to put a layer of solvent molecules around the system. Max. dist. is the maximal  distance of any protein atom from the center of mass of the protein. Usually you should choose a  boxsize at least 6 Angstrom larger (so at least two solvent molecules are surrounding the system). 

...

::

   Using BOXSIZE value of  30.0000
   Adding atoms for box     1  Added (Box):     0 (Total):     0  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box     2  Added (Box):     9 (Total):     9  Excl. (1):   639  Excl. (2):     0 
   Adding atoms for box    63  Added (Box):     3 (Total):  7635  Excl. (1):   645  Excl. (2):     0
   Adding atoms for box    64  Added (Box):     0 (Total):  7635  Excl. (1):   648  Excl. (2):     0
   Writing inputfile for chain   1

A total amount of 7635 atoms (2545 water molecules) has been added.

::

   Inputfile(s) written, everything processed, work has been done.
   Thank you for using the PDB2ADF program.     
   
   ================================
   Normal ending of PDB2ADF program
   ================================

ADF inputfile(s) have been written, the PDB-file has been processes. Everything is done. 

An example on protein structure
===============================

The idea of this example is to make an adf-input file using a PDB of an azurin (:download:`1DYZ.pdb.txt <1DYZ.pdb.txt>`). The result of this example should be that in the adf-input file the active site of azurin (Figure 1) is in the QM part, and the rest of the protein is in the MM part, and that the solvent water is added (in a box), which is also in the MM part. 

.. image:: /Images/azurin.png
   :width: 10 cm

**Figure 1:** the active site of azurin 

Usage of pdb2adf
----------------

The program works interactively. Given below in **bold** are the parts that the user has to type. In cases where the user agrees with the suggestion given by the program, the user can press the Enter key indicated with **Enter**. 

::

                                     P D B 2 A D F - program
                                        version 2008.01
                                 Written by: Marcel Swart, 2008
   
                            This program uses AMBER parameter files
                               see: http://amber.scripps.edu
   
   Please give name of PDB-file

**1DYZ.pdb.txt** 

::

   Do you want a logfile to be written (Y/n) ?

**Enter** 

::

    read fragments
   
   Data Processed:
        Nat:       2519
       Nmol:        196
    NChains:          1
   
   Please wait, making connection tables
   Now finding nearby atoms
   Assigning chain ID to all residues
   Completing residues for which only option is available
   
   Found the following terminal amino acid residues : (C-term)   129 (N-term)     1
   Do you want to use these as terminal residues (Y/n) ?

**Enter** 

::

   Refinding nearby atoms (including atoms added in residue completion)
   
   Multiple AMBER options for HIS :
     0         Decide every time differently
     1   HID   Histidine Delta Hydrogen
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens
   
   Suggested option: 0

**Enter** 

::

   Using 0: Decide every time differently
   
   Multiple AMBER options for GLU :
     0         Decide every time differently
     1   GLU   Glutamic acid (COO-)
     2   GLH   Neutral Glutamic acid (COOH)
   
   Suggested option: 1

**Enter** 

::

   Using 17   GLU   Glutamic acid (COO-)
   
   Multiple AMBER options for ASP :
     0         Decide every time differently
     1   ASP   Aspartic acid (COO-)
     2   ASH   Neutral Aspartatic acid (COOH)
   
   Suggested option: 1

**Enter** 

::

   Using 18   ASP   Aspartic acid (COO-)
   
   Multiple AMBER options for LYS :
     0         Decide every time differently
     1   LYS   Charged Lysine (NH3+)
     2   LYN   Neutral Lysine (NH2)
   
   Suggested option: 1

**Enter** 

::

   Using 19   LYS   Charged Lysine (NH3+)
   
   Multiple AMBER options for CYS :
     0         Decide every time differently
     1   CYS   Cysteine (SH)
     2   CYM   Deprotonated Cysteine (S-)
     3   CYX   Cystine (S-S bridge)
   
   Suggested option: 0

**Enter** 

::

   Using 0: Decide every time differently
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
              Making Choices for Chain      0
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
   
   Multiple AMBER options for CYS    3 (    3) :
     1   CYS   Cysteine (SH)
     2   CYM   Deprotonated Cysteine (S-)
     3   CYX   Cystine (S-S bridge)
   
     Connections and Nearest Atoms for SG CYS    3 SG  ( P2A #   41 PDB#   20 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.82      38      19  CB  CYS    3  CB       1       3.79    2382     980  O   HOH  151  O
    2    2.02     461     193  SG  CYS   26  SG       2       3.80      22       0  HC  GLN    2
                                                      3       4.04    2391     983  O   HOH  154  O
                                                      4       4.15     509     206  O   GLN   28  O
                                                      5       4.18     522       0  HA  PHE   29
   Suggestion: 3

**Enter** 

::

   Multiple AMBER options for CYS   26 (   26) :
     1   CYS   Cysteine (SH)
     2   CYM   Deprotonated Cysteine (S-)
     3   CYX   Cystine (S-S bridge)
   
     Connections and Nearest Atoms for SG CYS   26 SG  ( P2A #  461 PDB#  193 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.82     458     192  CB  CYS   26  CB       1       3.41     522       0  HA  PHE   29
    2    2.02      41      20  SG  CYS    3  SG       2       3.43     411     168  O   ASP   23  O
                                                      3       3.60    2322     960  O   HOH  131  O
                                                      4       3.91     403     169  CB  ASP   23  CB
                                                      5       4.15     387       0  HC  VAL   22
   Suggestion: 3

**Enter** 

::

   Multiple AMBER options for HIS   32 (   32) :
     1   HID   Histidine Delta Hydrogen
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens      
              
     Connections and Nearest Atoms for ND HIS   32 ND1 ( P2A #  581 PDB#  244 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.39     580     243  CG  HIS   32  CG       1       3.41     545       0  HC  THR   30
    2    1.33     583     246  CE  HIS   32  CE1      2       3.43      76      33  O   ALA    5  O
                                                      3       3.58      90      40  OH  THR    6  OG1
                                                      4       3.99      91       0  HO  THR    6
                                                      5       4.17      68       0  H   ALA    5
     
     Connections and Nearest Atoms for NE HIS   32 NE2 ( P2A #  585 PDB#  247 ) 
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.31     583     246  CE  HIS   32  CE1      1       2.86     544       0  HC  THR   30
    2    1.37     587     245  CD  HIS   32  CD2      2       3.00     545       0  HC  THR   30   
                                                      3       3.14    1677       0  HO  SER   94   
                                                      4       3.42     542     229  CT  THR   30  CG2
                                                      5       3.65    1676     688  OH  SER   94  OG
   Suggestion: 1

**3** 

::

   Multiple AMBER options for HIS   35 (   35) :
     1   HID   Histidine Delta Hydrogen  
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens
     
     Connections and Nearest Atoms for ND HIS   35 ND1 ( P2A #  649 PDB#  271 ) 
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.38     648     270  CG  HIS   35  CG       1       2.46     682       0  H   GLY   37   
    2    1.32     651     273  CE  HIS   35  CE1      2       2.69    1604       0  H1  GLY   89   
                                                      3       3.31     681     282  N   GLY   37  N 
                                                      4       3.56    1602     653  CT  GLY   89  CA
                                                      5       3.67     152       0  H1  ASN   10
   
     Connections and Nearest Atoms for NE HIS   35 NE2 ( P2A #  653 PDB#  274 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.33     651     273  CE  HIS   35  CE1      1 HB    2.91     822     332  O   MET   44  O
    2    1.37     655     272  CD  HIS   35  CD2      2       3.24     814       0  H1  MET   44
                                                      3       3.24     850     348  CD  HIS   46  CD2
                                                      4       3.34    1593       0  H1  GLY   88
                                                      5       3.75     848     350  NE  HIS   46  NE2
   Suggestion: 2

**3** 

::

   Multiple AMBER options for HIS   46 (   46) :
     1   HID   Histidine Delta Hydrogen
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens
   
     Connections and Nearest Atoms for ND HIS   46 ND1 ( P2A #  844 PDB#  347 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.37     843     346  CG  HIS   46  CG       1       2.62    2166       0  H1  MET  121
    2    1.33     846     349  CE  HIS   46  CE1      2       3.23    2080     863  ND  HIS  117  ND1
    3    2.04    2318     959  CU  CU   130  CU       3 HB    3.33    2163     900  S   MET  121  SD
                                                      4       3.40    2164     901  CT  MET  121  CE
                                                      5       3.57    2082     865  CE  HIS  117  CE1
   
     Connections and Nearest Atoms for NE HIS   46 NE2 ( P2A #  848 PDB#  350 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.32     846     349  CE  HIS   46  CE1      1 HB    2.70     162      67  O   ASN   10  O
    2    1.37     850     348  CD  HIS   46  CD2      2       2.83     814       0  H1  MET   44
                                                      3       3.23    2166       0  H1  MET  121
                                                      4       3.52     822     332  O   MET   44  O
                                                      5       3.74     813     334  CT  MET   44  CG
   Suggestion: 2

**Enter** 

::

   Multiple AMBER options for HIS   83 (   83) :
     1   HID   Histidine Delta Hydrogen
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens
   
     Connections and Nearest Atoms for ND HIS   83 ND1 ( P2A # 1494 PDB#  613 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.39    1493     612  CG  HIS   83  CG       1       2.67    1317       0  HC  VAL   73
    2    1.33    1496     615  CE  HIS   83  CE1      2       3.63    1315     542  CT  VAL   73  CG2
                                                      3       3.74    1310       0  HC  VAL   73
                                                      4       3.82    1316       0  HC  VAL   73
                                                      5       3.86    1313       0  HC  VAL   73
   
     Connections and Nearest Atoms for NE HIS   83 NE2 ( P2A # 1498 PDB#  616 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.32    1496     615  CE  HIS   83  CE1      1       3.09    1313       0  HC  VAL   73
    2    1.38    1500     614  CD  HIS   83  CD2      2       3.44    1317       0  HC  VAL   73
                                                      3       3.88    2385     981  O   HOH  152  O
                                                      4       3.93    1311     541  CT  VAL   73  CG1
                                                      5       4.03    1309     540  CT  VAL   73  CB
   Suggestion: 2

**3** 

::

   Multiple AMBER options for CYS  112 (  112) :
     1   CYS   Cysteine (SH)
     2   CYM   Deprotonated Cysteine (S-)
     3   CYX   Cystine (S-S bridge)
   
     Connections and Nearest Atoms for SG CYS  112 SG  ( P2A # 2001 PDB#  828 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.82    1998     827  CB  CYS  112  CB       1       2.53     858       0  H   ASN   47
    2    2.14    2318     959  CU  CU   130  CU       2       2.65    2023       0  H   PHE  114
                                                      3       3.00    2028       0  HC  PHE  114
                                                      4       3.29     868       0  H   ASN   47
                                                      5       3.39    2027       0  HC  PHE  114
   Suggestion: 2

**Enter** 

::

   Multiple AMBER options for HIS  117 (  117) :
     1   HID   Histidine Delta Hydrogen
     2   HIE   Histidine Epsilon Hydrogen
     3   HIP   Histidine E & D Hydrogens
   
     Connections and Nearest Atoms for ND HIS  117 ND1 ( P2A # 2080 PDB#  863 )
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.37    2079     862  CG  HIS  117  CG       1       2.82    2028       0  HC  PHE  114
    2    1.34    2082     865  CE  HIS  117  CE1      2       3.23     844     347  ND  HIS   46  ND1
    3    1.99    2318     959  CU  CU   130  CU       3       3.26    2031       0  HA  PHE  114   
                                                      4       3.27     832     340  O   GLY   45  O  
                                                      5       3.43     846     349  CE  HIS   46  CE1
     
     Connections and Nearest Atoms for NE HIS  117 NE2 ( P2A # 2084 PDB#  866 ) 
         Dist  P2A Nr  PDB Nr  Label                 Near     Dist  P2A Nr  PDB Nr  Label
    1    1.31    2082     865  CE  HIS  117  CE1      1       2.57     209       0  H1  MET   13
    2    1.37    2086     864  CD  HIS  117  CD2      2       2.65    2031       0  HA  PHE  114   
                                                      3 HB    2.74    2406     988  O   HOH  159  O  
                                                      4       3.34    2030     841  CA  PHE  114  CD1
                                                      5       3.41     204       0  H1  MET   13
   Suggestion: 2

**Enter** 

::

    - - - - - - - - - - - - - - - - - - - - - - - - - - -
              Making Choices for Chain      1 
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
   
   Completing residues with multiple options available, and solvent molecules
   
   Checking positions of newly added atoms
   
   Making choice for which molecules should be QM, which MM
   
   Residues belonging to chain  0
   Option  Molecule    Option  Molecule    Option  Molecule    Option  Molecule    Option  Molecule
        1: ALA    1        28: GLN   28        55: ASP   55        82: ALA   82       109: ALA  109
        2: GLN    2        29: PHE   29        56: LYS   56        83: HIS   83       110: TYR  110
        3: CYS    3        30: THR   30        57: GLN   57        84: THR   84       111: PHE  111
        4: GLU    4        31: MET   31        58: ALA   58        85: LYS   85       112: CYS  112
        5: ALA    5        32: HIS   32        59: VAL   59        86: VAL   86       113: SER  113
        6: THR    6        33: LEU   33        60: ALA   60        87: ILE   87       114: PHE  114
        7: VAL    7        34: LYS   34        61: THR   61        88: GLY   88       115: PRO  115
        8: GLU    8        35: HIS   35        62: ASP   62        89: GLY   89       116: GLY  116
        9: SER    9        36: VAL   36        63: GLY   63        90: GLY   90       117: HIS  117
       10: ASN   10        37: GLY   37        64: MET   64        91: GLU   91       118: TRP  118
       11: ASP   11        38: LYS   38        65: GLY   65        92: SER   92       119: ALA  119
       12: ALA   12        39: MET   39        66: ALA   66        93: ASP   93       120: MET  120
       13: MET   13        40: ALA   40        67: GLY   67        94: SER   94       121: MET  121
       14: GLN   14        41: LYS   41        68: LEU   68        95: VAL   95       122: LYS  122
       15: TYR   15        42: VAL   42        69: ALA   69        96: THR   96       123: GLY  123
       16: ASN   16        43: ALA   43        70: GLN   70        97: PHE   97       124: THR  124
       17: VAL   17        44: MET   44        71: ASP   71        98: ASP   98       125: LEU  125
       18: LYS   18        45: GLY   45        72: TYR   72        99: VAL   99       126: LYS  126
       19: GLU   19        46: HIS   46        73: VAL   73       100: SER  100       127: LEU  127
       20: ILE   20        47: ASN   47        74: LYS   74       101: LYS  101       128: GLY  128
       21: VAL   21        48: LEU   48        75: ALA   75       102: ILE  102       129: SER  129
       22: VAL   22        49: VAL   49        76: GLY   76       103: ALA  103       130: CU   130
       23: ASP   23        50: LEU   50        77: ASP   77       104: ALA  104
       24: LYS   24        51: THR   51        78: THR   78       105: GLY  105
       25: SER   25        52: LYS   52        79: ARG   79       106: GLU  106
       26: CYS   26        53: ASP   53        80: VAL   80       107: ASN  107
       27: LYS   27        54: ALA   54        81: ILE   81       108: TYR  108
   
   Give option number of molecules to be put in QM region (or 'c' to continue):
   Note: by specifying a negative number a molecule is removed from the QM region
   
**45 46 112 117 121 130** 

::

   Putting GLY   45 in QM region
   Putting HIS   46 in QM region
   Putting CYS  112 in QM region
   Putting HIS  117 in QM region
   Putting MET  121 in QM region
   Putting CU   130 in QM region
   
   Give option number of molecules to be put in QM region (or 'c' to continue):
   Note: by specifying a negative number a molecule is removed from the QM region
   
**c** 

::

   Make a choice for the QM/MM treatment of GLY   45
    0:  Put completely in QM region
    1:  Cut off at C-alpha (put NH in QM region, CO in MM region)  
    2:  Cut off at C-alpha (put NH in MM region, CO in QM region)  
    3:  Cut off at C-alpha (put NH and CO in MM region)  
    4:  Cut off at C-alpha (put NH and CO in QM region,  sidechain in MM region)      
    5:  Put only part of sidechain in QM region
       
   Suggestion: 2 
   Give choice:  

**Enter** 

::

   Make a choice for the QM/MM treatment of HIS   46
    0:  Put completely in QM region  
    1:  Cut off at C-alpha (put NH in QM region, CO in MM region) 
    2:  Cut off at C-alpha (put NH in MM region, CO in QM region) 
    3:  Cut off at C-alpha (put NH and CO in MM region)  
    4:  Cut off at C-alpha (put NH and CO in QM region,  sidechain in MM region)
    5:  Put only part of sidechain in QM region
       
   Suggestion: 1
   Give choice:

**Enter** 

::

   Make a choice for the QM/MM treatment of CYS  112
    0:  Put completely in QM region
    1:  Cut off at C-alpha (put NH in QM region, CO in MM region)
    2:  Cut off at C-alpha (put NH in MM region, CO in QM region)
    3:  Cut off at C-alpha (put NH and CO in MM region)
    4:  Cut off at C-alpha (put NH and CO in QM region,  sidechain in MM region)
    5:  Put only part of sidechain in QM region
   
   Suggestion: 3
   Give choice:

**Enter** 

::

   Make a choice for the QM/MM treatment of HIS  117
    0:  Put completely in QM region
    1:  Cut off at C-alpha (put NH in QM region, CO in MM region)
    2:  Cut off at C-alpha (put NH in MM region, CO in QM region)
    3:  Cut off at C-alpha (put NH and CO in MM region)
    4:  Cut off at C-alpha (put NH and CO in QM region,  sidechain in MM region)
    5:  Put only part of sidechain in QM region
   
   Suggestion: 3
   Give choice:

**Enter** 

::

   Make a choice for the QM/MM treatment of MET  121
    0:  Put completely in QM region
    1:  Cut off at C-alpha (put NH in QM region, CO in MM region)
    2:  Cut off at C-alpha (put NH in MM region, CO in QM region)
    3:  Cut off at C-alpha (put NH and CO in MM region)
    4:  Cut off at C-alpha (put NH and CO in QM region,  sidechain in MM region)
    5:  Put only part of sidechain in QM region
   
   Suggestion: 3
   Give choice:

**Enter** 

::

   Make a choice for the QM/MM treatment of CU   130
    0:  Put completely in QM region
    1:  Put only part of molecule in QM region
   
   Suggestion: 0
   Give choice:

**Enter** 

::

   Total formal charge on molecule CU    130      2.0000
   
   Solvent molecules (SOL/HOH) belonging to this chain:
       1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20
      21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40
      41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59   60
      61   62   63   64   65   66
   
   Give the number of the molecule to be put in QM region (or 'c' to continue):

**c**  

::

   Residues belonging to chain  1
    
   Do you want to add solvent to your system (Y/n) ?

**Enter** 

::

   Solvent (box) available:
      1:  HOH     HOH  Water molecule
      2:  MOH     MOH  Methanol molecule            
      3:  CHL     CHL  Chloroform molecule

**1**  

::

   Reading contents of solvent box p2abox.HOH                                                                                           
    
   Box Shape options:
    1  Spherical box
    2  Cubic box
   Make a choice:

**1** 

::

   Writing inputfile for chain   0
    
   Using total charge   1.0 and total spin   1.0
   
   Maximum atomic distance (Angs) from center       25.62
   Give boxsize (def.:    28.62 Angs)

**30.0** 

::

   Using BOXSIZE value of  30.0000
   Adding atoms for box     1  Added (Box):     0 (Total):     0  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box     2  Added (Box):     9 (Total):     9  Excl. (1):   639  Excl. (2):     0 
   Adding atoms for box     3  Added (Box):     3 (Total):    12  Excl. (1):   645  Excl. (2):     0 
   Adding atoms for box     4  Added (Box):     0 (Total):    12  Excl. (1):   648  Excl. (2):     0 
   Adding atoms for box     5  Added (Box):     6 (Total):    18  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box     6  Added (Box):   228 (Total):   246  Excl. (1):   420  Excl. (2):     0
   Adding atoms for box     7  Added (Box):   219 (Total):   465  Excl. (1):   429  Excl. (2):     0
   Adding atoms for box     8  Added (Box):     9 (Total):   474  Excl. (1):   639  Excl. (2):     0
   Adding atoms for box     9  Added (Box):     0 (Total):   474  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box    10  Added (Box):   225 (Total):   699  Excl. (1):   423  Excl. (2):     0
   Adding atoms for box    11  Added (Box):   216 (Total):   915  Excl. (1):   432  Excl. (2):     0
   Adding atoms for box    12  Added (Box):     6 (Total):   921  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    13  Added (Box):     0 (Total):   921  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box    14  Added (Box):     6 (Total):   927  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    15  Added (Box):    12 (Total):   939  Excl. (1):   636  Excl. (2):     0
   Adding atoms for box    16  Added (Box):     0 (Total):   939  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box    17  Added (Box):    12 (Total):   951  Excl. (1):   636  Excl. (2):     0
   Adding atoms for box    18  Added (Box):   210 (Total):  1161  Excl. (1):   438  Excl. (2):     0
   Adding atoms for box    19  Added (Box):   219 (Total):  1380  Excl. (1):   429  Excl. (2):     0
   Adding atoms for box    20  Added (Box):     3 (Total):  1383  Excl. (1):   645  Excl. (2):     0
   Adding atoms for box    21  Added (Box):   216 (Total):  1599  Excl. (1):   417  Excl. (2):    15
   Adding atoms for box    22  Added (Box):   381 (Total):  1980  Excl. (1):     3  Excl. (2):   264
   Adding atoms for box    23  Added (Box):   261 (Total):  2241  Excl. (1):     3  Excl. (2):   384
   Adding atoms for box    24  Added (Box):   183 (Total):  2424  Excl. (1):   423  Excl. (2):    42
   Adding atoms for box    25  Added (Box):   189 (Total):  2613  Excl. (1):   426  Excl. (2):    33
   Adding atoms for box    26  Added (Box):   186 (Total):  2799  Excl. (1):     3  Excl. (2):   459
   Adding atoms for box    27  Added (Box):   351 (Total):  3150  Excl. (1):     3  Excl. (2):   294
   Adding atoms for box    28  Added (Box):   222 (Total):  3372  Excl. (1):   420  Excl. (2):     6
   Adding atoms for box    29  Added (Box):     9 (Total):  3381  Excl. (1):   639  Excl. (2):     0
   Adding atoms for box    30  Added (Box):   162 (Total):  3543  Excl. (1):   429  Excl. (2):    57
   Adding atoms for box    31  Added (Box):   219 (Total):  3762  Excl. (1):   426  Excl. (2):     3
   Adding atoms for box    32  Added (Box):     6 (Total):  3768  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    33  Added (Box):     6 (Total):  3774  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    34  Added (Box):   219 (Total):  3993  Excl. (1):   426  Excl. (2):     3
   Adding atoms for box    35  Added (Box):   216 (Total):  4209  Excl. (1):   432  Excl. (2):     0
   Adding atoms for box    36  Added (Box):     6 (Total):  4215  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    37  Added (Box):   219 (Total):  4434  Excl. (1):   426  Excl. (2):     3
   Adding atoms for box    38  Added (Box):   279 (Total):  4713  Excl. (1):     6  Excl. (2):   363
   Adding atoms for box    39  Added (Box):   231 (Total):  4944  Excl. (1):     0  Excl. (2):   417
   Adding atoms for box    40  Added (Box):   195 (Total):  5139  Excl. (1):   432  Excl. (2):    21
   Adding atoms for box    41  Added (Box):   231 (Total):  5370  Excl. (1):   414  Excl. (2):     3
   Adding atoms for box    42  Added (Box):   324 (Total):  5694  Excl. (1):     0  Excl. (2):   324
   Adding atoms for box    43  Added (Box):   408 (Total):  6102  Excl. (1):     6  Excl. (2):   234
   Adding atoms for box    44  Added (Box):   204 (Total):  6306  Excl. (1):   435  Excl. (2):     9
   Adding atoms for box    45  Added (Box):     6 (Total):  6312  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    46  Added (Box):   177 (Total):  6489  Excl. (1):   435  Excl. (2):    36
   Adding atoms for box    47  Added (Box):   219 (Total):  6708  Excl. (1):   429  Excl. (2):     0
   Adding atoms for box    48  Added (Box):     6 (Total):  6714  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    49  Added (Box):     0 (Total):  6714  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box    50  Added (Box):     3 (Total):  6717  Excl. (1):   645  Excl. (2):     0
   Adding atoms for box    51  Added (Box):     6 (Total):  6723  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    52  Added (Box):     0 (Total):  6723  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box    53  Added (Box):     9 (Total):  6732  Excl. (1):   639  Excl. (2):     0
   Adding atoms for box    54  Added (Box):   222 (Total):  6954  Excl. (1):   426  Excl. (2):     0
   Adding atoms for box    55  Added (Box):   213 (Total):  7167  Excl. (1):   426  Excl. (2):     9
   Adding atoms for box    56  Added (Box):     6 (Total):  7173  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    57  Added (Box):     3 (Total):  7176  Excl. (1):   645  Excl. (2):     0
   Adding atoms for box    58  Added (Box):   219 (Total):  7395  Excl. (1):   423  Excl. (2):     6
   Adding atoms for box    59  Added (Box):   219 (Total):  7614  Excl. (1):   429  Excl. (2):     0
   Adding atoms for box    60  Added (Box):     6 (Total):  7620  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box    61  Added (Box):     0 (Total):  7620  Excl. (1):   648  Excl. (2):     0
   Adding atoms for box    62  Added (Box):    12 (Total):  7632  Excl. (1):   636  Excl. (2):     0
   Adding atoms for box    63  Added (Box):     3 (Total):  7635  Excl. (1):   645  Excl. (2):     0
   Adding atoms for box    64  Added (Box):     0 (Total):  7635  Excl. (1):   648  Excl. (2):     0

   Total spin   1.0

   Writing inputfile for chain   1
   There are no atoms in this chain, ignoring it
   
   Inputfile(s) written, everything processed, work has been done.
   Thank you for using the PDB2ADF program.     
   
   ================================
   Normal ending of PDB2ADF program
   ================================

Contents of the 1DYZ.pdb2adf file generated by pdb2adf
------------------------------------------------------

The file is not given completely, since it contains more than 9000 atoms. 

.. include:: 1DYZ.pdb2adf
   :literal:

An example on solvent shell run
===============================

The idea of this example is to make an adf-input file using a PDB file of water (:download:`hoh.pdb.txt <hoh.pdb.txt>`), in the solvent methanol. The water molecule in the adf-input file should be in the QM part, and the solvent methanol (in a box) is in MM part. 

Contents of the hoh.pdb file
----------------------------

.. include:: hoh.pdb.txt
   :literal:

Usage of pdb2adf
----------------

The program works interactively. Given below in **bold** are the parts that the user has to type. In cases where the user agrees with the suggestion given by the program, the user can press the Enter key indicated with **Enter**. 

::

                                     P D B 2 A D F - program   
                                        version 2008.01
                                 Written by: Marcel Swart, 2008
   
                            This program uses AMBER parameter files
                               see: http://amber.scripps.edu
   Please give name of PDB-file

**hoh.pdb.txt**

::
   
   Do you want a logfile to be written (Y/n) ?

**Enter** 

::

    read fragments
   
   Data Processed:
        Nat:          3
       Nmol:          1
    NChains:          0
   
   Please wait, making connection tables
   Now finding nearby atoms
   Assigning chain ID to all residues
   Completing residues for which only option is available
   
   Refinding nearby atoms (including atoms added in residue completion)
   
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
              Making Choices for Chain      0
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
   
   Completing residues with multiple options available, and solvent molecules
   
   Checking positions of newly added atoms
   
   Making choice for which molecules should be QM, which MM
   
   Residues belonging to chain  0
   
   Solvent molecules (SOL/HOH) belonging to this chain:
       1
   
   Give the number of the molecule to be put in QM region (or 'c' to continue):

**1** 

::

   Putting HOH    1 in QM region
   
   Give the number of the molecule to be put in QM region (or 'c' to continue):

**c** 

::

   Do you want to add solvent to your system (Y/n) ?

**Enter** 

::

   Solvent (box) available:
      1:  HOH     HOH  Water molecule
      2:  MOH     MOH  Methanol molecule
      3:  CHL     CHL  Chloroform molecule

**2** 

::

   Reading contents of solvent box p2abox.MOH                                                          
    
   Box Shape options:
    1  Spherical box
    2  Cubic box
   Make a choice:

**1** 

::

   Writing inputfile for chain   0
   
   Using total charge   0.0 and total spin   0.0
   
   Maximum atomic distance (Angs) from center        0.92
   Give boxsize (def.:    15.00 Angs)

**14.0** 

::

   Using BOXSIZE value of  14.0000
   Adding atoms for box     1  Added (Box):    84 (Total):    84  Excl. (1):   660  Excl. (2):     6
   Adding atoms for box     2  Added (Box):   102 (Total):   186  Excl. (1):   642  Excl. (2):     6
   Adding atoms for box     3  Added (Box):   102 (Total):   288  Excl. (1):   642  Excl. (2):     6
   Adding atoms for box     4  Added (Box):   108 (Total):   396  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box     5  Added (Box):   120 (Total):   516  Excl. (1):   630  Excl. (2):     0
   Adding atoms for box     6  Added (Box):    96 (Total):   612  Excl. (1):   654  Excl. (2):     0
   Adding atoms for box     7  Added (Box):   108 (Total):   720  Excl. (1):   642  Excl. (2):     0
   Adding atoms for box     8  Added (Box):   102 (Total):   822  Excl. (1):   642  Excl. (2):     6
   
   Inputfile(s) written, everything processed, work has been done.
   Thank you for using the PDB2ADF program.
   
   ================================
   Normal ending of PDB2ADF program
   ================================

Contents of the hoh.pdb2adf file generated by pdb2adf
-----------------------------------------------------

The file is not given completely, since it contains more than 800 atoms. 

.. include:: hoh.pdb2adf
   :literal:
