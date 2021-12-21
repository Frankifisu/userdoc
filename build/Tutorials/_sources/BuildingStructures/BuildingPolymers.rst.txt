.. This tutorial has been recorded: examples/tutorials/building-polymers
.. Keep the recording in sync so it may be used to generate the images!

.. _BuildingPolymers:


Building Polymers
*****************

In this tutorial you will learn how to build polymers from monomers using the polymer builder tool of AMS.

As an example polymer we are going to build `high-impact polystyrene (HIPS) <https://en.wikipedia.org/wiki/Graft_polymer#High_impact_polystyrene>`__, a low cost thermoplastic that is easy to fabricate and often used for low strength structural applications where impact resistance and machinability are required. HIPS is a graft polymer consisting of a polystyrene backbone with polybutadiene chains branching from it in each direction.


Loading the monomers from the database
======================================

.. rst-class:: steps

  \
    | **1.** Start **AMSinput**.
    | **2.** Open the polymer builder tool by clicking **Edit → Polymer...**.

In principle we could build the monomers ourselves using the normal building tools and the molecule viewport on the left. We would then also have to designate the link points at which the monomers can link up. However, in practice it is easier to just load them from the monomer database that comes with the Amsterdam Modeling Suite.

.. rst-class:: steps

  \
    | **1.** Type **styrene** into the **Add monomers** field and press the **Enter** key.
    | **2.** Type **buta** into the **Add monomers** field and select **1,4-butadiene** from the drop down menu.
    | **3.** Use the **right mouse button** in the molecule viewport to **drag** the butadiene monomer away from the styrene.
    | **4.** **Left click** into the molecule viewport to deselect all atoms.

You should now see the two monomers in the molecule viewport.

.. figure:: /Images/BuildingPolymers/polymer_builder_1.png
  :align: center

Note that each of the two monomers has two link points, designated by the small light blue spheres and the label, e.g. ``1A``. The number in the label designates the monomer that this link point belongs to (in the order they were loaded/built), while the letter labels the different link points on each monomer.


Growing polymers
================

Let us first set up the polystyrene back bone. We would obtain pure polystyrene if we just linked the styrene monomers via ``1A ↔ 1B``. Let us actually do that now.

.. rst-class:: steps

  \
    | **1.** Click the **+** next to **Links**.
    | **2.** Make sure the appearing link specification has ``1A`` and ``1B`` selected.
    | **3.** Set **Monomer repeats** to **20**.
    | **4.** Click the **Generate** at the bottom of the polymer builder panel.

.. figure:: /Images/BuildingPolymers/polymer_builder_1int.png
  :align: center

As you can see, we now have a pure polystyrene chain, while the butadiene monomer was not used at all. This is simply because we did not set up a linking rule that included any of its link points. Let us fix this now and grow real high-impact polystyrene.

.. rst-class:: steps

  \
    | **1.** Use **Edit → Undo** (or the **ctrl/cmd+z** hotkey) to undo the polystyrene generation.

In order to attach polybutadiene side chains to the polystyrene backbone, we first need to add more link points to the styrene monomer. Otherwise there is just no place to attach the side chains without terminating the backbone.

.. rst-class:: steps

  \
    | **1.** Select both hydrogen atoms on the outer carbon atom of the styrene monomer, i.e. the one which also has the ``1A`` link. (**Shift + left click** adds atoms to a selection.)
    | **2.** Click the **Replace** button next to **Set link point**.

The last carbon atom in the tail of the styrene monomer should now have three link points. We already used ``1A`` to make backbone link to ``1B``. Ergo we can not use this link to attach the butadiene chains since it might terminate our backbone. However, we can use the newly created links ``1C`` and ``1D`` to grow the side chains.

.. rst-class:: steps

  \
    | **1.** Click the **+** next to **Links**.
    | **2.** Set the new link specification to ``1C`` and ``2A``.
    | **1.** Click the **+** next to **Links** again.
    | **2.** Set the new link specification to ``1D`` and ``2A``.

This allows the attachment of butadiene monomers to our backbone. However, we also want these side chains to be able to grow into polybutadiene. Ergo we need to set up one last link, which allows linking of the butadiene monomers to each other.

.. rst-class:: steps

  \
    | **1.** Click the **+** next to **Links**.
    | **2.** Set the new link specification to ``2A`` and ``2B``.

The polymer builder grows the polymers by randomly making the links according to the weight we have set for each link. As our backbone grows we get more and more open ended side chains, to which more butadiene monomers could be linked. On the other hand, the number of link points at which the backbone can be grown is constant: one at each end of the backbone chain! Randomly picking new links with equal weights would therefore lead to a very short backbone with extremely long side chains, which is probably not what we want. We will therefore decrease the weight of the link between butadiene monomers in order to control the length of the side chains.

.. rst-class:: steps

  \
    | **1.** Set **Monomer repeats** to **100**.
    | **2.** Set the weight of the new link to **0.1**.

.. figure:: /Images/BuildingPolymers/polymer_builder_2.png
  :align: center

This is all we need. We are now ready to start growing the high-impact polystyrene polymer.

.. rst-class:: steps

  \
    | **1.** Click the **Generate** at the bottom of the polymer builder panel.
    | **2.** Watch your polymer grow. It might take a minute or so.

.. figure:: /Images/BuildingPolymers/polymer_builder_3.png
  :align: center

As the polymer is growing you can see the labels of the currently still open link points. As mentioned above these are mostly the open ``2B`` link points, hence the lower weight for the ``2A`` to ``2B`` linking.


Optimizing the structure with UFF
=================================

Once the entire polymer has been built, we should optimize its geometry with UFF. The polymer builder is relatively aggressive in linking together the monomers, and while it will make sure the result is sterically not completely unreasonable, it might still have groups from different monomers unphysically close to each other. A quick optimization with UFF is perfect to resolve these situations, as it will use the topology set up by the polymer builder and not form or break bonds during the optimization. The UFF forcefield is the default forcefield in the ForceField module.

.. tip::

  Always optimize the output of the polymer builder with UFF.
  As of AMS2020, the UFF forcefield is now part of the ForceField module.

.. rst-class:: steps

  \
    | **1.** **Close** the polymer builder tool.
    | **2.** Select the ForceField panel: **ADF → ForceField**
    | **3.** Make sure the **Task** is set to **Geometry Optimization**.

.. figure:: /Images/BuildingPolymers/polymer_builder_4.png
  :align: center

.. rst-class:: steps

  \
    | **1.** Run the job using **File → Run**.
    | **2.** Select your job in the upcoming AMSjobs window and click **SCM → Movie**.
    | **3.** Watch the running optimization in **AMSmovie**. It should only take a couple of minutes.

You will probably see the energy decrease *a lot* in the first few optimization steps where UFF resolves all the steric conflicts. Once the optimization is complete you should have a beautiful polymer:

.. figure:: /Images/BuildingPolymers/polymer_builder_5.png
  :align: center


.. seealso::

   In practice you may also want to build periodic boxes full of (cross-linked) polymers.
   Building these is harder, but can be done with biased molecular dynamics calculations using reactive force fields, see the tutorial:

   * :ref:`ReaxFF_polymers_bond_boost`.

   More tutorials on mechanical properties of polymers can be found here:

   * :ref:`ReaxFF_polymers_mechanical_properties`
   * :ref:`ReaxFF_thermal_expansion_coefficient`
   * :ref:`ReaxFF_glass_transition_temperatures`
