.. _AMS_PESExp_WaterDissociationOnZno:

PES Exploration: Water dissociation on an oxide surface
**********************************************************************

This tutorial will teach you how to

* Use **basin hopping** and **process search** for molecules adsorbed on surfaces
* Find dissociation barriers for water on an oxide surface

.. image:: /Images/PESExpWaterDissociationOnZnO/tocpic.png
   :width: 100 %
   :align: center

.. seealso::

   A more comprehensive introduction to PES exploration can be found in the :ref:`AMS_PESExp_Hydrohalogenation` tutorial
   and the `PES Exploration documentation <../../AMS/Tasks/PES_Exploration.html>`__.

Introduction
===============================================

Water adsorption at metal oxide surfaces is common in heterogeneous catalysis,
electrochemistry, and geochemistry. Water can either adsorb molecularly or
dissociate at the surface, and can donate hydrogen bonds to surface atoms
and/or other water molecules.

One well-studied system is water adsorption on |ZnO1010|. A monolayer of
|water| can adsorb `molecularly, dissociatively, or in a 50/50
(half-dissociated) configuration <https://doi.org/10.1002/anie.200461696>`__.

`Raymand et al. <https://doi.org/10.1016/j.susc.2009.12.012>`__ developed a
ReaxFF force field for |water| adsorption on ZnO. Here, we will use this force
field to illustrate how **basin hopping** and **process search** can be used to
automatically **discover the three most stable types of water monolayer
adsorption, and the barriers for converting from one structure to the other**.

Outline:

* **Step 1**: import a model of two water molecules adsorbed on |ZnO1010|.
* **Step 2**: Run **basin hopping** (a type of **global optimization**) to quickly discover several local minima, including the half-dissociated configuration
* **Step 3**: Run **process search** on the half-dissociated configuration to find the barriers for converting to the fully molecular or fully dissociated configurations.


Step 1: Set up the initial system
===============================================

Import the system into AMSinput
-----------------------------------------

:download:`Download 2H2O_ZnO_10-10_2dl.xyz </downloads/2H2O_ZnO_10-10_2dl.xyz>`
and import it into AMSinput.  The 2D slab was constructed from the
ReaxFF-optimized lattice parameters *a* = 3.28 Å and *c* = 5.28 Å (see Raymand
et al.). It is a (2×1) supercell of the |ZnO1010| surface unit cell, with *x*
|| [:math:`1\bar{2}10`] and *y* || [0001]. The slab is 2 double-layers thick.

The two |water| molecules were manually added to *reasonable* adsorption
positions. This is only a starting point for the global optimization, so it is
not too critical exactly how the water molecules are positioned.

.. seealso::

   More information about creating slabs and orienting molecules on surfaces
   can be found in the :ref:`Crystals and Surfaces tutorial <Crystals_Surfaces>`.

.. note::

   To find the half-dissociated configuration, at least two water molecules must
   be modeled. This is why a (2×1) surface supercell is used.

.. _change_default_colors:

Change the default color of Zn atoms
------------------------------------------------
In AMSinput, the default colors of both Zn and H are white. This can make it difficult to distinguish the atoms. Therefore, we will change the color of Zn to brown.

.. rst-class:: steps

  \
   | **1.** In **SCM → Preferences**, select **Colors → Atom colors**
   | **2.** Click the |AddButton| plus sign next to **Default Atom Colors**.
   | **3.** Select **Zn** in the popup periodic table
   | **4.** Click the white box in the preferences window
   | **5.** Type ``#de6b00`` into the **Selection:** text box and press **Enter**, or use the sliders to choose your own color.
   | **6.** Click **OK**.


Step 2: Basin Hopping
======================================

**PES exploration tasks** like basin hopping and process search benefit greatly
from a **smooth potential energy surface**. ReaxFF contains several `options to
smoothen the potential energy surface
<../../ReaxFF/ReaxFFEngine.html#smoothened-potential-energy-surface>`__.
Here, we will use the option to **taper bond orders**.

ReaxFF settings
-------------------------------

.. rst-class:: steps

  \
   | **1.** Change to the |ReaxFFPanel| panel
   | **3.** Set **Force field → ZnOH.ff**
   | **4.** Set **Taper bond orders → Yes**.


Basin hopping settings
---------------------------------

.. rst-class:: steps

  \
   | **1.** Set **Task → PES Exploration**
   | **2.** Click the |MoreBtn| arrow or go to the **Model → PES Exploration** panel.
   | **3.** Set **Job** to **Basin hopping**.
   | **4.** Set **Number of expeditions** to ``8``.
   | **5.** Set **Number of explorers** to ``8``.

Keep the bottom side of the slab fixed
----------------------------------------------

Keeping the bottom side of the slab (the side without water molecules) fixed
prevents the crystal from becoming completely distorted during the global
optimization.

.. rst-class:: steps

  \
   | **1.** Go to the **Model → Regions** panel.
   | **2.** Select **View → View Direction → Along X-axis**, or press **Ctrl-1**, to get the surface normal direction oriented vertically.
   | **3.** Select the bottom two atomic layers (the bottom double-layer) by holding **Shift** and dragging an area around them while **pressing the left mouse button**.
   | **4.** Click the |AddButton| to add a new region. This will display a shadow around the selected atoms.
   | **5.** Rename ``Region_1`` to ``bottom_side``.

.. image:: /Images/PESExpWaterDissociationOnZnO/regions_panel.png
   :width: 90 %
   :align: center


.. rst-class:: steps

  \
   | **1.** Go to the **Model → Geometry Constraints and PES Scan** panel. 
   | **2.** Select one of the atoms to be fixed, and press the |AddButton| plus sign next to **bottom_side (fixed position)**.

.. image:: /Images/PESExpWaterDissociationOnZnO/constraints_panel.png
   :width: 90 %
   :align: center

Save and run the basin hopping job
--------------------------------------------

.. rst-class:: steps

  \
   | **1.** Select **File → Save** and save your job with the name ``basinhopping.ams``
   | **2.** Run the job with **File → Run**.
   | **3.** Switch to AMSjobs: **SCM → Jobs**.

Wait a few minutes for the job to finish.

View the basin hopping results
------------------------------------------

.. note::

   You may not get exactly the same results as are shown in this tutorial. This
   is because the PES exploration task relies heavily on random numbers.

.. rst-class:: steps

  \
   | **1.** Select your job in AMSjobs
   | **2.** Switch to AMSmovie: **SCM → Movie**

.. image:: /Images/PESExpWaterDissociationOnZnO/basinhopping_results.png
   :width: 90 %
   :align: center

On the right-hand side you see all the states (local minima) found during the basin hopping procedure.
In this example, 19 different local minima were found.

Use either the scrollbar at the left, or click on the state lines on the right,
to browse the states. Each state has a unique number. The state numbers are
sorted with respect to energy, such that **state 1 is the lowest-energy
state**.

.. tip::

   If the structures from different states overlap, use the **Energy Profile → Increase Spacing** command.

**State 1 should correspond to a half-dissociated structure**. One of the water
molecules has dissociated into |hydroxide| adsorbed on a surface Zn, and
|proton| adsorbed on surface O. The other water molecule donates a hydrogen
bond to the |hydroxide| and to a surface O.

Here, **states 1–4 all correspond to the half-dissociated state**. They
have the same energy, but differ in which water molecule is dissociated, or in
which direction the OH bonds point. 

**States 5–6 correspond to fully molecular adsorption**. The states differ in which direction the OH bonds point.

**States 7–8 correspond to a less stable half-dissociated adsorption**. The states differ in which direction the OH bonds point.

**States 9–10 correspond to fully dissociated adsorption**. The states differ in which direction the OH bonds point.

States 11-19 correspond to higher energy (less stable) structures.

Step 3: Process search for reaction barriers
==============================================

For the process search, we will continue from one of the **half-dissociated** states (1-4) from the previous step.

.. tip::

   Use a state where no water molecule crosses a periodic boundary. This makes
   visualization easier. In the above example, states 1 and 4 would be suitable.

Process search finds transition states connecting a seed state to nearby local minima.

Here, we are only interested in transition states and minima close to
the half-dissociated state.  One way to accomplish this is to use the
half-dissociated state as the initial state and to only run a single
expedition.

.. tip::

   For more advanced ways of continuing from a subset of states from previous calculations,
   see the :ref:`AMS_PESExp_Hydrohalogenation` tutorial.

.. rst-class:: steps

  \
   | **1.** Select one of the half-dissociated states (e.g. **state 1**) from the previous step in AMSmovie, by clicking on the line for State 1. It should become highlighted.
   | **2.** **File → Update Geometry in Input**.  This brings up AMSinput.
   | **3.** In AMSinput, **File → Save As** with the name ``process_search.ams``
   | **4.** On the **Model → PES Exploration** panel, set **Job** to **Process Search**.
   | **5.** Set the **Number of expeditions** to ``1``
   | **6.** Set the **Number of explorers** to ``16``.
   | **7.** **File → Run**.


When the calculation has finished, open the results in AMSmovie: **SCM → Movie**.

.. image:: /Images/PESExpWaterDissociationOnZnO/process_search_raw.png
   :width: 90 %
   :align: center


In this example, 

* **state 1** is the half-dissociated state (local minimum)

* **state 2** is the molecular state (local minimum)

* **state 3** is the dissociated state (local minimum)

* **state 4** is the transition state between states 1 and 3

* **state 5** is the transition state between states 1 and 2

* **states 6-9** are less stable structures (minima and transition states).

The energy landscape can be rearranged to better highlight the interesting states 1-5.

.. rst-class:: steps

  \
   | **1.** Double-click on the y-axis and set the **Unit** to **kcal/mol**.
   | **2.** Select any uninteresting state (here for example **state 6**) and press Ctrl+Delete
   | **3.** Select the interesting states (here states 1-5) and move them to the left or right with Ctrl+Left arrow or Ctrl+Right arrow.

.. image:: /Images/PESExpWaterDissociationOnZnO/process_search_tidy.png
   :width: 80 %
   :align: center

.. |ZnO1010| replace:: ZnO(\ :math:`10\bar{1}0`\ )
.. |water| replace:: H\ :subscript:`2`\ O
.. |hydroxide| replace:: OH\ :superscript:`–`
.. |proton| replace:: H\ :superscript:`+`
