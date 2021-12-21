.. _trainset_in:

trainset.in
***********

.. _TS_description:

Description of the trainset.in file
===================================

The trainset.in file contains the training set data and tells the program how to calculate the cost function :math:`F = \Sigma ((y_i - y^{ref}_i) / acc_i)^2` , which can be used to optimize the :ref:`force field <ffield>` parameters. The **trainset.in** uses molecule identifiers, or keys, defined in the DESCRP field of  the geo file (in BGF format), or in the models.in file, to compare force field derived geometries and energy differences to the reference values. The **trainset.in** has a free format as far as numbers concerned, although it does require that fields are space-separated. Besides, the "-", "+" and "/" symbols have a special meaning in the **trainset.in** file and should not be used in identifiers.  The **trainset.in** file is divided into 5 sections listed below. Each section begins with a start keyword and ends with the corresponding end keyword. The words in "CELL PARAMETERS" and "ENDCELL PARAMETERS" must be separated by exactly one space. 

.. _TS_sections:

Sections format
===============

.. csv-table:: 
   :widths: 100,100,100,100

   **Block name**, **Start keyword**, **End keyword**, **Format**
   charges, CHARGE, ENDCHARGE, Key Acc Atom Ref
   geometries, GEOMETRY, ENDGEOMETRY, Key Acc [Atom1 [Atom2 [Atom3 [Atom4]]] Ref]
   forces, FORCES, ENDFORCES, Key Acc Atom Ref
   cell parameters, CELL PARAMETERS, ENDCELL PARAMETERS,Key Acc Type Ref
   energy differences, ENERGY, ENDENERGY, Acc [+-] Key1/n1 ... [+-] Key5/n5 Ref
   heat of formation, HEATFO, ENDHEATFO, Key Acc Ref

"**Key**" is the molecule name from the geo file. "**Atom**" is an atom index in the corresponding molecule. "**Acc**" is a value of the target accuracy desired for the given error function contribution. This value is often called "**weight**" although in practice it is 1/weight. "**Ref**" is the reference value. 


.. _TS_format:

Format description
==================

In the all sections except "ENERGY" each data line starts with the structure identifier (the **Key**), followed by the "**Acc**" of the data point. This is followed by a type identifier. Each section contains following data entries:

+ CHARGE
    In the CHARGE section the type identifier is the number of the atom in the molecule and the reference value is its charge. 
    Example::

        CHARGE
        #Key     Acc Atom  Ref
        chexane 0.1    1   -0.15
        ENDCHARGE

+ GEOMETRY
    In the GEOMETRY section the type ID is the list of atoms defining an internal coordinate (two for an interatomic distance, three for a valence and four for a torsion angle). 
    When there is only one atom index specified, then the Eucledian distance for the given atom between the two geometries is calculated. 
    When the index is -1 then an average Eucledian distance quantity between the two geometries is used instead. Please note that any reference value different from zero for the Eucledian distances does not make much sense. 
    Besides, since these distances are computed in the Cartesian coordinates, which means that a simple translation of the molecule as a result of energy minimization may result in large Eucledian distances for otherwise similar geometries.
    If there is no identifier provided then it means that the ReaxFF RMS force will be compared with the reference (which should probably be zero in most cases). Example::

        GEOMETRY
        #Key      Acc At1 At2 At3 At4  Ref
        chexane  0.01   1              0.0    # Eucledian distance between atom in the reference and the trial structure
        chexane  0.01  -1              0.0    # Average Eucledian distance between atoms in the two structures 
        chexane  0.01   1   2          1.5    # Interatomic distance
        chexane  1.00   1   2   3      120.0  # Valence angle
        chexane  1.00   1   2   3   4  180.0  # Torsion angle
        chexane  1.00                  0.0    # RMS force
        ENDGEOMETRY

+ CELL PARAMETERS
    In the CELL PARAMETERS section the type IDs are names of the corresponding lattice parameters. Example::

        CELL PARAMETERS
        #Key         Acc   Type     Ref
        chex_cryst  0.01    a      11.20
        chex_cryst  0.01    b      11.20
        chex_cryst  0.01    c      11.20
        chex_cryst  0.01    alpha  90.00
        chex_cryst  0.01    beta   90.00
        chex_cryst  0.01    gamma  90.00
        ENDCELL PARAMETERS

+ HEATFO
    The HEATFO section does not require a type ID as compares the ReaxFF heat of formation with the reference value. Example::

        HEATFO
        #Key      Acc   Ref
        methane  2.00 -17.80
        ENDHEATFO

+ ENERGY
    This section allows comparison of ReaxFF energy differences between structures to the reference data. In this case, each data line starts with the **Acc** of the data point, followed by up to five operator/identifier/divider parts and finishes with the reference value. The operator is either ‘**+**’ or ‘**-**‘ (‘+’ is the default). The energy associated with the identifier is divided by the divider, allowing comparison of condensed structures to monomers. The ‘/’ character in the ENERGY section data lines is optional. Example::

        ENERGY
        #Acc op1  Key1  n1 op2  Key2   n2     DeltaE
        1.5   + butbenz/1  -  butbenz_a/1     -90.00
        1.5   + butbenz/1  -  butbenz_b/1     -71.00
        1.5   + butbenz/1  -  butbenz_c/1     -78.00
        ENDENERGY
