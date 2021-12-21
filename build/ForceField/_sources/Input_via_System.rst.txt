Input via the AMS system block
##############################

.. The input style for the ForceField engine is similar to the input structure of the other parts in the AMS package. Some helpful examples can be found in the $AMSHOME/examples/forcefield directory. The input can also be studied by setting up a job with the ForceField tab in the GUI, followed by clicking on "Details" - "Run Script". The ForceField input can have multiple forms, via the System block. Depending on what information is given. The main options are:

While usually options for an AMS engine are defined in its engine block, for the ForceField engine three ingredients are defined via the AMS system block: bonds, atom types and (partial) charges.

Here are some logical options

+ 1) Specify Everything: elements, coordinates, MM atom types, charges, and bonds
+ 2) Specify elements, coordinates, and bonds (UFF only)
+ 3) Specify elements and coordinates (UFF only, most convenient)

Currently, for most force fields, everything needs to be specified (option 1).
UFF and GAFF allow the automatic determination of bonds and atom types (option
2 and 3). For GAFF this option is considered experimental as of the 2020
release and is disabled by default, see :ref:`Antechamber integration <antechamber>` below.
See also the :ref:`BondsUsage <forcefield-key-BondsUsage>` key on how bond
information can be tweaked.

ForceField input example
************************

**1) Specify Elements, coordinates, MM Atom Types, Charges, and bonds:**

::

  $AMSBIN/ams << eor

  Task GeometryOptimization

  System
      Atoms
          C   1.36012328  -0.14520095   0.60144543    ForceField.Type=C_3     ForceField.Charge=0.000000
          C   0.00000000   0.00000000   0.00000000    ForceField.Type=C_2     ForceField.Charge=0.000000
          H   2.09833847  -0.46327872  -0.16560721    ForceField.Type=H_      ForceField.Charge=0.000000
          H   1.32657807  -0.90546800   1.40917410    ForceField.Type=H_      ForceField.Charge=0.000000
          H   1.67935140   0.82750664   1.02977296    ForceField.Type=H_      ForceField.Charge=0.000000
          H  -0.83486863   0.30434056   0.62258487    ForceField.Type=H_      ForceField.Charge=0.000000
          O  -0.18030374  -0.22462371  -1.18585739    ForceField.Type=O_2     ForceField.Charge=0.000000
      End
      BondOrders
           1 5 1.0
           1 4 1.0
           1 3 1.0
           1 2 1.0
           2 6 1.0
           2 7 2.0
      End
  End

  Engine ForceField
  EndEngine

  eor

The format in the bonds section is: atom A, atom B, bond order.

**2) Specify Elements, coordinates, and bonds (UFF only):**

If we leave out the MM atom types and charges, UFF will determine the MM atom types automatically from the bond information:

::

  $AMSBIN/ams << eor

  Task GeometryOptimization

  System
      Atoms
          C  1.36012328 -0.14520095  0.60144543
          C  0.00000000  0.00000000  0.00000000
          H  2.09833847 -0.46327872 -0.16560721
          H  1.32657807 -0.90546800  1.40917410
          H  1.67935140  0.82750664  1.02977296
          H -0.83486863  0.30434056  0.62258487
          O -0.18030374 -0.22462371 -1.18585739
      End
      BondOrders
           1 5 1.0
           1 4 1.0
           1 3 1.0
           1 2 1.0
           2 6 1.0
           2 7 2.0
      End
  End

  Engine ForceField
  EndEngine

  eor


**3) Specify Elements and coordinates (UFF only):**

The third input format is similar to the second, but without a Bonds section in System:

::

  $AMSBIN/ams << eor

  Task GeometryOptimization

  System
      Atoms
          C  1.36012328 -0.14520095  0.60144543
          C  0.00000000  0.00000000  0.00000000
          H  2.09833847 -0.46327872 -0.16560721
          H  1.32657807 -0.90546800  1.40917410
          H  1.67935140  0.82750664  1.02977296
          H -0.83486863  0.30434056  0.62258487
          O -0.18030374 -0.22462371 -1.18585739
      End
  End

  Engine ForceField
  EndEngine

  eor

The GUI generates inputs of the second or third type, depending on the "Use existing bonds" setting in the ForceField main tab.
Note that to specify the MM Atom Types, the charges also need to be set. UFF has automatic bond guessing and a very simple automatic charge guessing only assigning charges to atoms of water molecules.


.. index:: antechamber
.. _antechamber:

Antechamber integration
***********************

For the GAFF force field there is an experimental integration of the
`Antechamber toolkit <http://ambermd.org/antechamber/antechamber.html>`_ for
automatic atom typing. This allows the GAFF force field to be used with option
2 (only bonds and coordinates specified) and option 3 (coordinates only). As of
the 2020 release of AMS, this option is still considered experimental and
disabled by default. It can be enabled and configured from the input:

.. scmautodoc:: forcefield AntechamberIntegration
.. scmautodoc:: forcefield AntechamberTask
