.. This tutorial has been recorded: examples/tutorials/hybrid-framework
.. Keep the recording in sync so it may be used to generate the images!

.. _Hybrid_ElectrostaticEmbedding:

QM/MM: Inorganic linker in organic framework
********************************************

Introduction
============

The `hybrid engine <../../Hybrid/index.html>`__ is about applying different engines or settings to different regions. There are several different reasons to do so, but the most common one is performance. 
We will here look at inserting an organic linker in a system comprised of otherwise organic material.

Covalent organic frameworks
---------------------------

Covalent organic frameworks are built of small organic units. As anyone with a little bit of LEGO experience knows: there are infinite many ways to assemble small units. Understandably this a hot topic in material science. Organic systems are reasonably well described by the fast |DFTB| method. But what if we want to  introduce a new inorganic block, for which DFTB fails?

Solution
--------

Apply the fast method (DFTB) to most of the system, and only use DFT for the inorganic linker and it's direct surrounding.


Setup with AMSinput
===================

.. rst-class:: steps

    \
     | **1.** Download the :download:`xyz file of the <../downloads/COF-3.xyz>` system
     | **2.** In **AMSinput** select **File → Import coordinates** and select the file you just downloaded


This is what the structure looks like

.. image:: /Images/HybridMechanicalEmbedding/pic1.png
   :width: 80%
   :align: center

Most of the rings are made of organic material, except for the (inorganic) linker in the middle.


Define the QM region
--------------------

We want our linker in the QM region but also the two directly neighboring organic rings. Make the selection as shown in the picture.


.. image:: /Images/HybridMechanicalEmbedding/pic2.png
   :width: 70%
   :align: center

Using shift and click-dragging you can fairly easily select the three building blocks. In the end 21 atoms should be selected.

.. tip::
   When there are bonds sticking out of the QM region, capping atoms will be added to the QM region to satisfy dangling bonds. The main rule is that you better not break very strong bonds, and it is recommended to use the menu item **Selection → Make selection cappable**. In this case nothing happens, as the selection was already sensible.

Now define the QM region. Use **Model → Regions**, and click on the plus region, and rename it to "qm"

.. image:: /Images/HybridMechanicalEmbedding/pic3.png
   :align: center

Setup the Hybrid Engine
-----------------------

Switch the engine from |BAND| to Hybrid. As you can see there is a **Method** being either "Energy Terms" or "QMMM". See the `hybrid engine documentation <../../Hybrid/Introduction.html>`__ for more details. 

.. rst-class:: steps

    \
     | **1.** Click the "QMMM" radio button
     | **2.** Set "Embedding" to "Mechanical"
     | **3.** Set the engine for the qm region to "Band"
     | **4.** Set the engine for the remaining region to "DFTB"

The panel should look like this

.. image:: /Images/HybridMechanicalEmbedding/pic4.png
   :width: 50%
   :align: center

At the bottom you see the names of the two engines.

.. rst-class:: steps

    \
     | **1.** Click at the bottom on "BAND 1"
     | **2.** Enable "Unrestricted"
     | **3.** Set the basis set to TZP


The panel should look like this

.. image:: /Images/HybridMechanicalEmbedding/pic5.png
   :width: 50%
   :align: center

And that is it.

Results
-------

Running this calculation will take quite while. It is interesting to compare the results for three different calculations

+ 1) The whole system with the cheap DFTB engine
+ 2) The system with the Hybrid engine
+ 3) The whole system with the BAND (DFT) engine


The first calculation is quick, the second one a bit more expensive, and the last one is a lot more expensive.

Here are the final geometries for the three calculations

+ :download:`DFTB xyz file <../downloads/COF-3-dftb.xyz>`
+ :download:`Hybrid xyz file <../downloads/COF-3-hybrid.xyz>`
+ :download:`BAND xyz file <../downloads/COF-3-band.xyz>`

The **DFTB** result displays a symmetric solution (plane tilted a bit) From exactly above the linker looks flat.

.. image:: /Images/HybridMechanicalEmbedding/dftbresult.png
   :width: 60%
   :align: center

The **Hybrid Engine** produces an asymmetric solution

.. image:: /Images/HybridMechanicalEmbedding/hybridresult.png
   :width: 60%
   :align: center


Also the **Band engine** shows the asymmetric solution.

.. image:: /Images/HybridMechanicalEmbedding/hybridresult.png
   :width: 60%
   :align: center


.. rst-class:: steps

    \
     | Examine the three geometries (from the xyz files) with either AMSinput or AMSView from several angles


Conclusions
-----------

+ For this system full DFTB gives very a different geometry as compared to DFT.
+ The hybrid result resembles closely the full DFT one (at one tenth of the time).
+ With the hybrid engine we can fix the inorganic part, wrongly described by the DFTB method.


.. |DFTB| replace:: `DFTB <../../DFTB/index.html>`__
.. |BAND| replace:: `BAND <../../BAND/index.html>`__
