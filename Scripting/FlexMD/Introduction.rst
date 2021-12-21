Introduction
************

.. _metatag INTRODUCTION: 

FlexMD is a python package providing molecular dynamics (MD) simulations using the energy evaluation methods made available by the ADF suite. A set of example scripts can be found in the examples/scmlib directory of a standard ADF installation. 

FlexMD can be accessed interactively by running amspython, followed by a standard python import command for the package scm.flexmd. The python help function can be used to obtain detailed documentation about all FlexMD classes. In the following example, an inquiry of one class (the MDMolecule class) can be performed. 

::

   $ amspython
    from scm import flexmd
    help(flexmd.MDMolecule)

To leave the interactive help, press q. The help function can also be used to list the contents of the FlexMD package: 

::

   $ amspython
    from scm import flexmd
    help(flexmd)

Python can also give the help documentation as plain text: 

::

   $ amspython
    from scm import flexmd
    import pydoc
    print pydoc.render_doc(flexmd.ForceJob, "Help on %s")

