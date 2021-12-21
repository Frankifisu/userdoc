.. index:: molecular fragments 
.. _MOLECULARFRAGMENTS: 


Molecular fragments
*******************

Fragment mode
=============

.. index:: fragment mode 

In Fragment mode you have to specify: (1) the atomic positions and (2) how the total system is built up from fragments. We recommended to specify also (3) the point group symmetry. 

Example of an input file for the C2H4 molecule: 

::

   System
      Atoms
         C   0      0   0.668
         C   0      0  -0.668
         H   0.927  0  -1.203
         H  -0.927  0  -1.203
         H   0.927  0   1.203
         H  -0.927  0   1.203
      end
   End
   
   Engine ADF
      fragments
         C C_dzp.results/adf.rkf
         H H_dzp.results/adf.rkf
      end
   
      symmetry D(2h)
   EndEngine


The :ref:`Atoms block key<keyscheme ATOMS>` is in the AMS driver part of the input.
Two keys are used in the engine ADF part: :ref:`fragments<keyscheme FRAGMENTS>` and :ref:`symmetry <adf-key-symmetry>`.

``atoms``
   defines the atomic positions: each record in the data block contains the chemical symbol of an atom followed by its Cartesian coordinates in Angstroms (Z-matrix type input of atomic positions is also possible).

``fragments``
   lists the fragment files each record contains a fragment *type* followed by the corresponding fragment *file*. In the example the files are *local* files. Files in other directories are addressed by giving the complete file path. Note: if a *parallel* calculation is performed, be sure that each 'kid' finds the specified fragment files. This will usually require that the files are *not* local to the job, but first be moved to some shared volume, and that the references to the fragment files in the input contain the full path. An alternative is to ensure that the (local) files in the parent directory are copied first to the 'kid' directories before the parallel calculation starts. 

``symmetry``
   specifies the point group symmetry by a Schönfliess type symbol. :ref:`schonfliess symbols` contains a complete list of all Schönfliess symbols that are recognized by ADF. If no symmetry is specified ADF will use the true symmetry of the nuclear frame. If :ref:`(electric) fields<EFIELD>` are used, see later, symmetry will be NOSYM. Note that the computed symmetry may not occur in the list of allowed symmetries (see :ref:`appendix symmetry`), in which case you have to explicitly specify the (lower) point group symmetry you wish to apply. 

The atomic coordinates must conform to the point group symmetry; the program will check this and abort if the atomic system does not have the specified symmetry. It is allowed, however, to specify a *lower* symmetry than what is actually present in the set of atomic positions. The *specified* symmetry determines how results are analyzed and how irreducible representations and subspecies are labeled. It also determines various algorithmic aspects: the program runs more efficiently with the highest possible symmetry. 

The spatial orientation of the molecular coordinate system is not arbitrary. ADF requires for each point group symmetry a specific standard orientation. In axial groups for instance, the main rotation axis must be the z-axis. This implies a restriction on how you can define the atomic coordinates under atoms. The orientation requirements for all point groups are listed in  :ref:`appendix symmetry`. If the specified symmetry equals the true symmetry of the nuclear frame ADF will adjust the input orientation of the molecule to the requirements (if necessary). If you have specified a subgroup of the true nuclear symmetry, no such orientation adjustment is carried out and the user has to make sure that his input data yield the correct orientation, lest an error will occur. 

Restrictions apply to the symmetry (as specified) of the molecule, related to the symmetries of the fragments as they were stipulated in the preceding fragment calculations. All symmetry operators of the molecule that internally rotate or reflect a fragment but leave it at the same position in the molecule, must also be operators of the symmetry group in which the fragment has been computed. Furthermore, two fragments must not be symmetry-equivalent in the molecule only by an improper rotation. The implied internal reflection of the fragment must be one of the symmetry operators in the point group symmetry that is used in the fragment calculation *and* the molecular symmetry group must also contain a proper rotation that maps the two fragments onto each other. 

The example of the C2H4 molecule implicitly assumes that all fragments are *single atom* fragments. When the fragments are larger the data records in the atoms key have to be extended: you must specify which atoms belong together in one fragment. 

::

   System
      Atoms
         Ni  0     0     0 
         C  -1.06 -1.06  1.06 adf.f=CO|1
         C  -1.06  1.06 -1.06 adf.f=CO|2
         C  -1.06  1.06 -1.06 adf.f=CO|3
         C   1.06 -1.06 -1.06 adf.f=CO|4
         O   1.71  1.71  1.71 adf.f=CO|1
         O  -1.71 -1.71  1.71 adf.f=CO|2
         O  -1.71  1.71 -1.71 adf.f=CO|3
         O   1.71 -1.71 -1.71 adf.f=CO|4
      End
   End

   Engine ADF
      Fragments
         CO CO_yesterday.results/adf.rkf
         Ni Ni_dzp.results/adf.rkf
      End
   
      SYMMETRY T(D)
   EndEngine

Another sample input file; using a single atom Ni fragment and four molecular CO fragments. The keys symmetry and fragments operate as before. Again we have two types of fragments (here: Ni and CO); for each of them, the fragment file is specified. 

Under the key ATOMS the chemical symbols and the nuclear coordinates are listed. Added is the adf.f=...-part; f stands here for fragment and tells the program that the carbon and oxygen atoms belong to CO fragments. The last part in adf.f=CO|n enumerates the individual CO fragments: here you define which C and O belong together in one CO fragment. 

The record for Ni contains no adf.f= part, implying the *default* for this atom: it is a fragment on its own. In the C2H4 example before the default applied to all atoms. 

Note that one should use the adf.f= part for symmetry equivalent fragments. In the next example, ADF assumes the fragments CO1, CO2, CO3, and CO4, to be of different fragment types, even though they are coming from the same adf.rkf (TAPE21). Therefore ADF will assume symmetry NOSYM in the next calculation, and will not run in T(D) symmetry. 

::

   System
      Atoms
         Ni 0     0     0 
         C -1.06 -1.06  1.06 adf.f=CO1
         C -1.06  1.06 -1.06 adf.f=CO2
         C -1.06  1.06 -1.06 adf.f=CO3
         C  1.06 -1.06 -1.06 adf.f=CO4
         O  1.71  1.71  1.71 adf.f=CO1
         O -1.71 -1.71  1.71 adf.f=CO2
         O -1.71  1.71 -1.71 adf.f=CO3
         O  1.71 -1.71 -1.71 adf.f=CO4
      End
   End

   Engine ADF
      Fragments
         CO1 CO_yesterday.results/adf.rkf
         CO2 CO_yesterday.results/adf.rkf
         CO3 CO_yesterday.results/adf.rkf
         CO4 CO_yesterday.results/adf.rkf
         Ni Ni_dzp.results/adf.rkf
      End
   End

There are more possibilities with the keys atoms and fragments. This is worked out later. The purpose of this section was to provide a quick and easy start. 

.. index:: fragments files 

Fragment files
==============

The adf.rkf (TAPE21) result files from the ADF computations on the fragments that constitute a molecule completely characterize these fragments. The fragment adf.rkf (TAPE21) files must be attached as *fragment files*. This is achieved with the key FRAGMENTS. See also the next section for the relation between Atom type, Fragment type and Fragment file names. 

.. _keyscheme FRAGMENTS: 

::

   Fragments {Directory}
      FragType FragFile
      FragType FragFile
   end

``FragType``
   One of the fragment *types* defined under atoms, either explicitly (adf.f=fragtype|n) or implicitly (fragment type=atom type, if the adf.f= option is not used). 

``FragFile``
   The fragment file: the standard adf.rkf (TAPE21) result file from the computation of that fragment. The file name must contain the complete path relative to Directory (the argument of the key). By default, when no Directory is specified, this is the local directory where the job runs. You may therefore omit the directory and give simple (local) file names if all the files are present in the working directory of the job. 

Obviously, FragFile is **case sensitive**. However, FragType is also treated as case sensitive; see also the :ref:`ATOMS key<keyscheme ATOMS>` discussion (adf.f= option). The reason is that there are shortcuts possible to the effect that the FragType name (in the atoms block) is immediately interpreted as the name of the fragment file. 

The key FRAGMENTS may be used any number of times in the input file. This is convenient if you employ a sizable number of fragment files, with subsets located in different directories. You can then use the key separately for each directory, to avoid typing long path names for all the files. Fragtypes that occur in the fragments block(s), but that are not referred by atoms are ignored. No fragment files must be specified for dummy atoms (xx). 

It is allowed to use one and the same fragment file for different fragment types. Example: 

::

   ATOMS
      C.1 x1 y1 z1
      C.2 x2 y2 z2
   end

   Fragments
      C.1 C.results/adf.rkf
      C.2 C.results/adf.rkf
   end

Two different atom types (and fragment types) C.1 and C.2 are defined. The properties of the two fragment types are now identical since they are characterized by the same fragment file, but from the program's point of view they are different and can therefore not be symmetry equivalent. 

The reason you may want to specify different atom types will usually be related to analysis, in particular symmetry aspects. If you know in advance that the two atom types are not symmetry equivalent, or more generally, that they play a rather different role in the molecule, it can enhance clarity of printed output to assign different atom type names to them. However, see the notes below. 

If you want your fragment file to be the result file of a spin-unrestricted calculation, you should use the :ref:`UNRESTRICTEDFRAGMENTS<keyscheme UNRESTRICTEDFRAGMENTS>` key.
You can also analyze a molecule in terms of simulated unrestricted fragments, in which spin-restricted fragment files are used and the key :ref:`FRAGOCCUPATIONS<keyscheme FRAGOCCUPATIONS>` is specified.

Suppose that you have done a calculation on a molecule *mol*, in which you have defined two different atom types for atoms of the same chemical element. Suppose furthermore, that you want to use that molecule now as a fragment in a new calculation. 

You list under atoms all atoms of the molecule and you specify which atoms belong to the various fragments, among which the molecular fragment *mol*. The program will then have a problem deciding which atoms in your system are associated with the different atom types in the fragment. Normally, ADF analyzes this by comparing the chemical elements. That is not sufficient here because one chemical element corresponds with more than one type of atom in the *mol fragment* type. In such a case it is imperative to use *the same atom type names* in your new calculation as you used in the generation of the fragment. These names are stored in the fragment file, and they are printed in the output file of the calculation of *mol*. 

The names of three items may be related to each other, depending on how you specify input: the *atom type*, the *fragment type*, and the *fragment file*. 

The atom type is defined in the data block to atoms. 

The fragment type is defined also in the data block to atoms: with the adf.f= option. For records in the data block that don't have the adf.f= option, the fragment type name is by definition identical to the atom type name. 

The fragment file is defined in the data block to fragments, each record consisting of a fragment *type* name, followed by the fragment *file*. If a fragment type is not listed in the data block to fragments, so that no fragment file name is specified, the fragment *file* is by definition identical to the fragment *type* name. 

