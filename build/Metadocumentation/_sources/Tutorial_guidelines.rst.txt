.. _tutorial-guidelines:

Tutorial guidelines
###################


Steps in GUI tutorials
======================

For steps in tutorials use the ``rst-class:: steps``.

**Example:**

.. code-block:: rst

  .. rst-class:: steps

    \
      | Optionally some context here
      | **1.** The first step, e.g. click on **Edit → Builder**
      | **2.** The seconf step.

**Result:**

.. rst-class:: steps

  \
    | Optionally some context here
    | **1.** The first step, e.g. click on **Edit → Builder**
    | **2.** The second step

GUI icons
=========

In the Tutorials, you can refer to some GUI buttons/icons by using the following substitutions (these substitutions are defined in ``global_conf.py``, but that you have to initialize it in the ``conf.py`` of your specific project. See the ``Tutorials/conf.py``).

.. csv-table::
   :header: "Icon", "Substitution", "Name"

   |InfoBtn|,              "\|InfoBtn\|", More-info button
   |MoreBtn|,              "\|MoreBtn\|", Details
   |SCMMenu|,              "\|SCMMenu\|", SCM menu
   |Search|,               "\|Search\|", Search box
   |PointerTool|,          "\|PointerTool\|", Pointer tool
   |CTool|,                "\|CTool\|", Carbon tool
   |OTool|,                "\|OTool\|", Oxygen tool
   |HTool|,                "\|HTool\|", Hydrogen tool
   |XTool|,                "\|XTool\|", Element tool
   |StructTool|,           "\|StructTool\|", Structure tool
   |CrystalTool|,          "\|CrystalTool\|", Periodic structure tool
   |SymmTool|,             "\|SymmTool\|", Symmetrize tool
   |BondTool|,             "\|BondTool\|", Bond tool
   |PeriodicViewTool|,     "\|PeriodicViewTool\|", Periodic display
   |SliceTool|,            "\|SliceTool\|", Slice tool
   |PreOptimTool|,         "\|PreOptimTool\|", Pre-optimizer button
   |ADFPanel|,             "\|ADFPanel\|",  ADF panel
   |ADFviaAMSPanel|,       "\|ADFviaAMSPanel\|",  ADF via AMS panel
   |BANDPanel|,            "\|BANDPanel\|",  BAND panel
   |ConformersPanel|,      "\|ConformersPanel\|",  Conformers panel
   |DFTBPanel|,            "\|DFTBPanel\|",  DFTB panel
   |MMPanel|,              "\|MMPanel\|",  MM panel
   |MopacPanel|,           "\|MopacPanel\|",  Mopac panel
   |QMMMPanel|,            "\|QMMMPanel\|",  QMMM panel
   |QuantumESPRESSOPanel|, "\|QuantumESPRESSOPanel\|",  Quantum ESPRESSO panel
   |QuildPanel|,           "\|QuildPanel\|",  Quild panel
   |ReaxFFPanel|,          "\|ReaxFFPanel\|",  ReaxFF panel
   |ForceFieldPanel|,      "\|ForceFieldPanel\|",  ForceField panel
   |VASPPanel|,            "\|VASPPanel\|",  VASP panel
   |AddButton|,            "\|AddButton\|",  Add button
   |DeleteButton|,         "\|DeleteButton\|",  Delete button


**Example:**

.. code-block:: rst

  .. rst-class:: steps

    \
      | In **ADFInput**
      | **1.** Switch to the **BAND panel**: |ADFPanel| **→** |BANDPanel| 
      | **2.** In the **search box** |Search| search for ``Diamond`` and select **Crystal → C**

**Result:**

.. rst-class:: steps

  \
    | In **ADFInput**
    | **1.** Switch to the **BAND panel**: |ADFPanel| **→** |BANDPanel| 
    | **2.** In the **search box** |Search| search for ``Diamond`` and select **Crystal → C**



Conventions for step descriptions
=================================

How to phrase common tasks:

.. rst-class:: steps

  \
    | Switch to **BAND** by clicking on |ADFPanel| **→** |BANDPanel|
    | In the **search box** |Search| search for ``Diamond`` and select **Crystal → C**
    | In the **panel bar**, select **Properties → Excitations (UV/Vis), CD**
    | In the **menu bar**, select **View → Reset View**
    | Select **Task → Geometry Optimization**
    | In **Total charge** enter ``-1``
    | Check/Uncheck the **Unrestricted** checkbox
    | Select the Carbon tool |CTool| and click in the **molecule drawing area**
