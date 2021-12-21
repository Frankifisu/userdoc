.. This tutorial has been recorded: examples/tutorials/adf-spincoupling-fe4s4
.. Keep the recording in sync so it may be used to generate the images!

.. _SPIN_FE4S4: 

Spin Coupling in Fe4S4 Cluster
******************************

This `ADF <../../ADF/index.html>`__ tutorial will help you to: 

+ control the spin coupling in multi-center radical systems in two different ways (|SpinFlip|  and |ModifyStartPotential|),   

+ tweak the SCF convergence in the iron-sulfur cubane case,   

+ visualize the distribution of spin densities in 3D.   

Create the Fe\ :sub:`4` S\ :sub:`4` cubane model
================================================

Embedded into proteins and coordinated by cysteine ligands, iron-sulfur cubanes are often used by nature in electron transfer   and catalysis. While their native structures can be extracted from protein data bank (PDB) files, we will use a model of the Fe\ :sub:`4` S\ :sub:`4`  cubane in this example. 

In this step are the instructions to build the system. If you just want the final system go to the end of this step, there you can copy-paste the coordinates.
 
.. rst-class:: steps

  \ 
    | **1.** Start AMSinput
    | **2.** Select |StructTool| **→ Polyhedra → Cube** structure
    | **3.** Click anywhere in the empty structure drawing area 

The cube built is constructed of carbon atoms. We will now change four of these atoms to iron (Fe), and next the remaining four atoms into sulfur (S). 

.. rst-class:: steps

  \ 
    | Via Shift-click, select four carbon atoms in the corners of the cubane

.. figure:: /Images/SpinCouplingInFe4S4Cluster/macFeS_selected_atoms.png
  :align: center

.. rst-class:: steps

  \ 
    | In the **menu bar**:
    | **1.** **Atoms → Change Atom Type → Fe**: change the four atoms into Fe
    | **2.** **Select → Invert Selection**
    | **3.** **Atoms → Change Atom Type → S**: change the other atoms into S

.. figure:: /Images/SpinCouplingInFe4S4Cluster/macFeS_atoms.png
  :align: center

Now you should see the Fe\ :sub:`4` S\ :sub:`4`  cubane in the   structure drawing area of AMSinput. 
The proper coordination to Fe atoms is important in modeling their electronic structure. 
In proteins, iron-sulfur cubanes are coordinated by cysteine ligands to the Fe sites. 
Here, we will model these four cysteines by \ :sup:`-` SH ligands. The procedure to add these ligands is described below. 

.. rst-class:: steps

  \ 
    | **1.** Select all Fe atoms (for example by inverting the selection)
    | **2.** Use the **Atoms → Details (Color, Radius, Mass, ...)** menu command
    | **3.** Change the valency (**# v**) of all Fe atoms from 10 into 4

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_changeatomconns.png

.. rst-class:: steps

  \ 
    | **1.** Switch to the Main panel
    | **2.** Add hydrogens to the (still selected) Fe atoms using the **Atoms → Add Hydrogen** menu command
    | **3.** Select the (newly added) hydrogens 
    | **4.** Use the **Atoms → Replace By Structure → Ligands → OH** menu command

.. tip::

    The Add Hydrogen command operates on the selected atoms only, if any.

This will replace hydrogen atoms into OH ligands. 

.. figure:: /Images/SpinCouplingInFe4S4Cluster/macFeS_OH_added.png
  :align: center

.. rst-class:: steps

  \ 
    | **1.** Select one of the O atoms
    | **2.** Use the **Select → Select Atoms Of Same Type** command to select them all
    | **3.** Use the **Atoms → Change Atom Type → S** to change them into S
    | **4.** Symmetrize the structure by clicking on |SymmTool|

Your Fe\ :sub:`4` S\ :sub:`4` cubane model should look like this, and have ``T(D)`` symmetry: 

.. figure:: /Images/SpinCouplingInFe4S4Cluster/final_built_cubane.png
  :align: center

Instead of building the structure using the instructions above, you can also copy-paste the following coordinates:

::

    Fe      0.92466000       0.92466000      -0.92466000
    S       0.92466000       0.92466000       0.92466000
    Fe      0.92466000      -0.92466000       0.92466000
    S       0.92466000      -0.92466000      -0.92466000
    S      -0.92466000       0.92466000      -0.92466000
    Fe     -0.92466000       0.92466000       0.92466000
    S      -0.92466000      -0.92466000       0.92466000
    Fe     -0.92466000      -0.92466000      -0.92466000
    H       2.61053000       2.61053000      -2.61053000
    H       2.61053000      -2.61053000       2.61053000
    H      -2.61053000       2.61053000       2.61053000
    H      -2.61053000      -2.61053000      -2.61053000
    S      -2.03318000      -2.03318000      -2.03318000
    S      -2.03318000       2.03318000       2.03318000
    S       2.03318000      -2.03318000       2.03318000
    S       2.03318000       2.03318000      -2.03318000


Optimize the structure with ADF
===============================

The next step is to `optimize <../../AMS/Tasks/Geometry_Optimization.html>`__ this structure. It is a difficult system, and the pre-optimizers will fail. So we will use ADF to optimize the geometry. 

.. rst-class:: steps

  \ 
    | **1.** Set the charge to -2
    | **2.** Select the **Geometry Optimization** task
    | **3.** Symmetrize the structure by clicking on |SymmTool| (it should have ``T(D)`` symmetry)

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_geopt.png

.. rst-class:: steps

  \ 
    | **1.** **File → Run** (enter FeS as name)
    | **2.** Wait for the calculation to finish...
    | **3.** When ready, click **Yes** in "Update coordinates and bonds with data from... " to load the optimized geometry in AMSinput
    | **4.** **SCM → Movie**
    | **5.** Click the Play button

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_optmovie.png

.. rst-class:: steps

  \ 
    | Close the movie window: **File → Close**

Obtain the solution for the high-spin (HS) state of the cubane
==============================================================

In Fe\ :sub:`4` S\ :sub:`4`  systems, the iron sites are   commonly high-spin ferrous (Fe\ :sup:`3+` , S = 5/2) or   ferric (Fe\ :sup:`2+` , S = 2). For the present   example, we will use the iron-sulfur cubane oxidation state where   the two sites are ferric and the remaining two are ferrous. This   oxidation level of Fe\ :sub:`4` S\ :sub:`4`  is well-defined   and occurs, for example, in rubredoxin and high-potential   iron-sulfur proteins (HIPIPs). For our model system,   Fe\ :sub:`4` S\ :sub:`4` (SH)\ :sub:`4` , this implies the   total charge of -2. 

The relative directions, or coupling, of the individual site spin   vectors is a very important issue in obtaining the desired   density functional solution in Fe\ :sub:`4` S\ :sub:`4` , as   well as many other systems which display a multi-center radical   character. 

Within the common open-shell approach, the spin vectors are   either parallel or anti-parallel. The case when all the spins are   parallel is called high-spin (HS). Obtaining self-consisted field   (SCF) solution for the HS case is normally simpler because the   program does not need to resolve the ambiguity of distribution   the sites spin vectors. While the ferromagnetic HS solution   commonly does not correspond to the lowest energy electronic   state, this solution can be used to obtain the electron density   corresponding to the lower energy spin-coupled state. In this   step, we will obtain the HS solution for the iron-sulfur cubane,   which will be used later in the tutorial. The HS solution for the   [Fe\ :sub:`4` S\ :sub:`4` (SH)\ :sub:`4` ]\ :sup:`2-`  model   corresponds to S = 2 × 5/2 + 2 × 2 = 9. 

.. rst-class:: steps

  \ 
    | **1.** Select the AMSinput window
    | **2.** Select the **Single Point** task
    | **3.** Keep the total charge at -2
    | **4.** Check the unrestricted box
    | **5.** Set the spin polarization to 18 (corresponds to S = 9)
    | **6.** **File → Save As...**
    | **7.** Enter FeS_HS as filename and save 
    | **8.** **File → Run**

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_HS.png

Click on the progress lines so that AMStail window will pop up showing the progress of the job: 

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_finished_HS_2.png

Check in the logfile that the SCF procedure converged.

Couple the spins in Fe\ :sub:`4` S\ :sub:`4`  using the   SpinFlip option
=========================================================================

While SCF solution for the high-spin (HS) state of a multi-center   spin system can often be easily found, this solution does not   necessarily correspond to the lowest energy state. 

To generate the solution with the desired collinear spin   arrangement, one option is to use the |SpinFlip| concept that has   been earlier introduced by L. Noodleman and coworkers. In this   two step procedure: 

+ first the spin-unrestricted HS solution is generated with all   the site spins ferromagnetically coupled in one direction (all spins up, :math:`\uparrow` ).   

+ Next the α (:math:`\uparrow` ) and β (:math:`\downarrow` ) electron densities centered at the   sites which are expected to be antiferromagnetically coupled   (spins down, :math:`\downarrow` ) to the total spin vector are exchanged for the   earlier obtained HS solution, using the SpinFlip option, and the   calculation is restarted.   

Because this approach often results in lowering the electronic   symmetry of the system while retaining its structural symmetry, a   solution obtained in such way is often called the broken symmetry   (BS) state. In such cases you will need to make sure that your BS   calculation is done with lower symmetry. 

The concept of SpinFlip and BS state can be illustrated   considering our iron-sulfur cubane case with two ferrous   (Fe\ :sup:`3+` , S = 5/2) and two ferric   (Fe\ :sup:`2+` , S = 2) sites. One of the   well-characterized BS states for this level of   Fe\ :sub:`4` S\ :sub:`4`  oxidation corresponds to S =   (5/2 + 2) - (5/2 + 2) = 0, :math:`2 \uparrow :2 \downarrow`. 

.. rst-class:: steps

  \ 
    | **1.** Select the AMSinput window with your FeS_HS calculation
    | **2.** Make sure the 'Main' panel is visible
    | **3.** Change the spin polarization from 18 to 0

This spin polarization setting corresponds to S = 0 zero spin of the BS electronic state. 

The Spin Flip option only works when restarting, so set up the restart calculation from the HS results: 

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Restart**
    | **2.** Click folder icon in front of the **Engine restart** field, 
    | **3.** Select the **Fe_HS.results/adf.rkf** file 

.. figure:: /Images/SpinCouplingInFe4S4Cluster/macFeS_restart.png
    :align: center

The above will instruct ADF to read the converged HS solution we obtained in the previous step of the tutorial. This solution has been saved in the file ``Fe_HS.results/adf.rkf``. 

.. rst-class:: steps

  \ 
    | **1.** Panel bar **Model → Spin and Occupation**
    | **2.** Select the two (out of four) arbitrary Fe sites in the drawing area
    | **3.** Click **+** next to the **Spin Flip on Restart For:** line.

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_spinflip.png

To achieve the desired BS solution, the SpinFlip procedure should   be applied to 2 out of 4 Fe sites of Fe\ :sub:`4` S\ :sub:`4` .   In the above example, we selected sites Fe(2) and Fe(4). This   will instruct SpinFlip algorithm to interchange α (:math:`\uparrow` ) and β (:math:`\downarrow` )   electron densities associated with these two Fe sites when the   job will be restarted, changing the HS :math:`4 \uparrow :0 \downarrow` spin state to the BS :math:`2 \uparrow :2 \downarrow` spin state. 



.. rst-class:: steps

  \ 
    | **1.** Panel bar **Details → Symmetry**
    | **2.** Set the symmetry symbol to NOSYM
    | **3.** **File → Save As**, save the job as FeS_BS_SPINFLIP
    | **4.** **File → Run**

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_spinflip_tail.png

Check in the logfile that the SCF procedure converged.


Coupling the spins using the ModifyStartPotential option
========================================================

There is an alternative to SpinFlip available in ADF, which is aimed to achieve a specific spin-coupled solution in a single calculation only. This is done using the MODIFYSTARTPOTENTIAL key in ADF: it allows you to create a spin-polarized potential at the very start of the calculation. 

Please read the page of `ADF manual on the MODIFYSTARTPOTENTIAL key <../../ADF/Input/Electronic_Configuration.html#modify-the-starting-potential>`__ prior to proceeding with this step of the tutorial. As follows from the MODIFYSTARTPOTENTIAL description, this key allows to control the ratio of spin-α and spin-β electrons associated with fragments via 'alpha' and 'beta' numbers. For the purpose of the present tutorial, we will consider the four Fe sites as fragments. 'Alpha' and 'beta' numbers will correspond to the number of spin-α and spin-β electrons, respectively, associated with a Fe site. 

So follow these instructions to obtain the BS solution via the   MODIFYSTARTPOPTENTIAL option: 

.. rst-class:: steps

  \ 
    | **1.** Open your FeS_HS calculation in AMSinput
    | **2.** Change the spin polarization from 18 to 0
    | **3.** Panel bar **Details → Symmetry**
    | **4.** Set the symmetry to NOSYM
    | **5.** Panel bar **Model → Spin and Occupations** 
    | **6.** Select the four Fe atoms
    | **7.** Click the '+' in front of 'Modify Start Potential'
    | **8.** Set the alpha and beta occupations, for the four Fe atoms:
    |
    | Alpha: 14, Beta: 10
    | Alpha: 14, Beta:  9
    | Alpha: 10, Beta: 14
    | Alpha: 9, Beta: 14

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_ModStartPot.png

For the spin-up Fe\ :sup:`3+` , S = 5/2, the alpha and   beta numbers would be 14 and 9, correspondingly, and for the   spin-up Fe\ :sup:`2+` , S = 2, these numbers are 14 and   10. For the spin-down Fe sites, alpha and beta numbers should be   apparently transposed. Also, our desired BS state for this level   of Fe\ :sub:`4` S\ :sub:`4`  oxidation corresponds to   S = (5/2 + 2) - (5/2 + 2) = 0, :math:`2 \uparrow :2 \downarrow`. 

Note that SCF procedure might be problematic. 

You can play with several options to help the convergence. In the   SCF panel (in Details) you can experiment with several methods like LISTi, A-DIIS, E-DIIS, ARH and the option to enable the old SCF algorithm. In the SCF convergence   details panel further options are available, like mixing, level   shifting, orbital freezing and DIIS details. 

In this particular case, the default method works but it needs a lot of iterations. So no need to make changes.

.. rst-class:: steps

  \ 
    | **1.** **File → Save As**: save the job as FeS_BS_MODIFYSTARTPOTENTIAL
    | **2.** **File → Run**

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_finished_MSP.png

Hopefully you will be able to converge the job, to the same energy and state as the SpinFlip job. 

Thus both the SpinFlip and the ModifyStartPotential option allow you to obtain a desired Fe spin coupling pattern in the   Fe\ :sub:`4` S\ :sub:`4`  case. While SpinFlip is a two-step   approach and ModifyStartPotential works as in a single step, the SpinFlip approach shows a better performance during SCF (much   better and faster SCF convergence). 

View the spin density of the broken symmetry (BS)   solutions
=============================================================

In the two previous steps of this tutorial, we have generated the broken symmetry (BS) solution for the Fe\ :sub:`4` S\ :sub:`4` cubane using alternatively the SpinFlip and ModifyStartPotential   options. Here, we will analyze this BS solution viewing the Fe spin densities using AMSview, and confirm that the spin alignment of the iron sites is :math:`2 \uparrow :2 \downarrow`. This type of analysis can also be useful for presentations and scientific illustrations. 

.. rst-class:: steps

  \ 
    | **1.** Select your FeS_BS_MODIFYSTARTPOTENTIAL calculation in AMSjobs
    | **2.** Use the **SCM → View** menu command to activate AMSview

You should see the   [Fe\ :sub:`4` S\ :sub:`4` (SH)\ :sub:`4` ]\ :sup:`2-`  system   in the AMSview window. 

The spin-density is available as a short-cut in the Properties   menu: 

.. rst-class:: steps

  \ 
    | **Properties → Spin Density** 

You should see now the two Fe ions surrounded by blue blobs (spin up, :math:`\uparrow` ) and the other two by red blobs (spin down, :math:`\downarrow`): 

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_isosurface_double_C-1.png

Note that you now have two visualization lines: one is a calculated field that actually calculates the difference between the alpha and beta spin density. The other is an isosurface with phase that visualized the calculated field. You can use these calculated fields for many purposed. For example, by changing the '-' into a '+' you are visualizing the total density instead of the spin difference density. 

In the same way you can also check the spin densities for the FeS_HS and FeS_BS_SPINFLIP results. 
The FeS_BS_SPINFLIP should look the same as the FeS_BS_MODIFYSTARTPOPTENTIAL, the FeS_HS should look like:

.. image:: /Images/SpinCouplingInFe4S4Cluster/macFeS_hs_isosurface_double_C-1.png


.. |SpinFlip| replace:: `SpinFlip <../../ADF/Input/Electronic_Configuration.html#spin-flip-method-for-broken-symmetries>`__

.. |ModifyStartPotential| replace:: `ModifyStartPotential <../../ADF/Input/Electronic_Configuration.html#modify-the-starting-potential>`__
