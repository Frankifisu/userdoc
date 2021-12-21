.. This tutorial has been recorded: examples/tutorials/adf-ip-ea-g0w0
.. Keep the recording in sync so it may be used to generate the images!

.. _ADF_GW: 

Accurate Ionization Potential and Electron Affinity with |G0W0|
***************************************************************

Ionization potential (IP) and electron affinity (EA) of molecules can be predicted with reasonable accuracy using the |G0W0| method [#ref1]_ [#ref2]_.
One can also do eigenvalue-only self-consistent GW (evGW) with ADF, which is typically a factor 5 to 10 more expensive than |G0W0|, but which has the advantage that it is less starting-point dependent.

In this tutorial we will show how to compute the IP and EA of Azulene with ADF using |G0W0|\ \@PBE0.

.. seealso::
    
    * `ADF manual on GW <../../ADF/Input/GW.html>`_
    * `Recommendations <../../ADF/Input/GW.html#recommendations>`_ for |G0W0| and evGW calculations


Set up and run the calculation
==============================


Let's start by importing the structure of the Azulene molecule from our molecules database:

.. rst-class:: steps

  \
    | **1.** Start **AMSinput** (**SCM → New Input**)
    | **2.** In the **search box** |Search| search for ``Azulene`` and select **C10H8: Azulene**

Let's now set up the calculation details in the main panel:

.. rst-class:: steps

  \
    | **1.** **Task → Single Point**
    | **2.** **XC functional → Hybrid → PBE0**
    | **3.** **Basis set → TZ2P**
    | **4.** **Frozen core → None**

.. image:: /Images/GW/MainPanel.png


To enable the |G0W0| calculation:

.. rst-class:: steps

  \
    | **1.** In the panel bar select **Properties →** GW
    | **2.** In the GW panel, check the **Calculate** GW **quasi-particle energies** checkbox 
    | **3.** **Self consistency → G0W0**


.. figure:: /Images/GW/GWCheckbox.png
    :align: center

We are now ready to run the calculation:

.. rst-class:: steps

  \
    | **1.** **File → Save** and give the job an appropriate name, e.g. "Azulene" (note that symmetry will be automatically disabled for |G0W0| calculations)
    | **2.** **File → Run**
    | **3.** Wait for the calculation to finish (you can monitor the progress via the logfile, **SCM → Logfile**)


Results
=======

The results of the calculation are written both to the text output file and to the binary ``adf.rkf`` file.

You can use AMSspectra to examine the results from the binary file:

.. rst-class:: steps

  \
    | **1.** **SCM → Spectra**

.. figure:: /Images/GW/spectra.png
    :align: center

To see the |G0W0| results in the output file:

.. rst-class:: steps

  \
    | **1.** **SCM → Output**
    | **2.** In AMSoutput, search for "GW" and go the the second hit

.. figure:: /Images/GW/output.png
    :align: center

The ionization potential (IP) equals the negative of the |G0W0| quasi-particle HOMO energy:

.. math::

  \text{IP} = -\text{HOMO}_{\text{G}_0\text{W}_0} = 7.15 \text{[eV]}

The electron affinity (EA) equals the negative of the |G0W0| quasi-particle LUMO energy:


.. math::

  \text{EA} = -\text{LUMO}_{\text{G}_0\text{W}_0} = 0.54 \text{[eV]}


These values are in good agreement with the CCSD(T) results from [#ref1]_ (IP=7.55 [eV] and EA=0.54 [eV]) and with experimental results cited in [#ref1]_ (IP=7.42-7.44 [eV] and EA=0.69-0.80 [eV]).


.. |G0W0| replace:: G\ :sub:`0`\ W\ :sub:`0`

.. [#ref1] Joseph W. Knight, Xiaopeng Wang, Lukas Gallandi, Olga Dolgounitcheva, Xinguo Ren, J. Vincent Ortiz, Patrick Rinke, Thomas Körzdörfer, and Noa Marom, *Accurate Ionization Potentials and Electron Affinities of Acceptor Molecules III: A Benchmark of GW Methods*, `J. Chem. Theory Comput. 2016, 12, 2, 615–626 <https://doi.org/10.1021/acs.jctc.5b00871>`__ 

.. [#ref2] Arno Förster, Lucas Visscher, *Low-order scaling G0W0 by pair atomic density fitting*, `arXiv.org (2020) <https://arxiv.org/abs/2007.01581>`__ 

