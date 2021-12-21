.. index:: VCDtools module
.. _VCDtools: 

VCD Analysis: VCDtools
======================

The auxiliary program *VCDtools* provides insight regarding the origin of the VCD intensity of a given normal mode. This is done by analyzing and visualizing the various contributions to the total Electric (E) and Magnetic (M) Dipole Transition Moments (DTM). *e.g.*, the contributions from atoms, electrons, nuclei and molecular fragments. 
The *VCDtools* program is accessible through the AMS-GUI and allows one to:


1) Scale the size of the atoms with the magnitude of their atomic EDTM or MDTM contributions.

2) Visualize the various contributions to the EDTMs and MDTMs by arrows.

3) Perform a General Coupled Oscillator (GCO) analysis to evaluate the interactions between the different parts of a molecule.

4) Decompose the total EDTM and MDTM into nuclear and electronic contributions to gain insight into effects induced in the VCD spectra by charge transfer.

5) Perform a VCD robustness analysis.


.. seealso::

  Tutorial: `Analysis of the VCD spectrum of Oxirane with VCDtools <../../Tutorials/VibrationalSpectroscopy/AnalysisOfVCDSpectrumOfOxirane.html>`__

*VCDtools* requires only the standard result file adf.rkf from an VCD calculation using the *ADF* engine. Once this file is opened with *AMSspectra* the *VCDtools* program will be accessible through the standard user interface of *AMSspectra*.

*VCDtools* produces one ASCII file, VCDtools.out where all output from the program is printed. This file will be located in the *.results* folder in the directory of the opened adf.rkf result file. Additionally, VCDtools will run on the background every time a new normal mode is selected. It then computes the atomic EDTM and MDTM which can be displayed inside *AMSspectra* in various ways. 

The following references should be cited when publishing results obtained with VCDtools Refs. [#ref1]_ [#ref2]_ [#ref3]_.


General Theory
**************
The VCD intensity associated with the fundamental vibrational transition for a given normal mode :math:`j`  is given by the rotational strength (RS):

.. math::

   R_{01}(j) = -i \vec{E}^{tot}_{01}(j) \cdot \vec{M}^{tot}_{10}(j)

where :math:`E^{tot}_{01}(j)` and :math:`M^{tot}_{10}(j)` are the total EDTM and MDTM of normal mode :math:`j` , :math:`i`  is the unit imaginary number.

Whiten the harmonic approximation the total EDTM and MDTM can be written as sums of atomic contributions:

.. math::

   \vec{E}^{tot}_{01}(j) = \sum_{\lambda = 1}^N \vec{E}^{\lambda}_{01}(j) \\
   \vec{M}^{tot}_{10}(j) = \sum_{\lambda = 1}^N \vec{M}^{\lambda}_{10}(j)

where :math:`N` is the total number of atoms in the molecule and :math:`\lambda` runs over all atoms.


General Coupled Oscillator Analysis
***********************************

The GCO analysis computes the contribution to total rotational strength from the interaction of two molecular fragments. This information provides important insight regarding the source of the VCD intensity and the robustness of the computed VCD sign. In the following, a brief summary of the GCO theory originally published in Ref. [#ref1]_ is given.

Following the original coupled oscillator VCD mechanism, the atoms of a molecule are grouped into three fragments: **A**, **B**, and **R**. The fragments **A** and **B** represent the important Coupling Oscillator (CO) fragments, while fragment **R** is the ancillary fragment containing the rest of the atoms. As a result, the total RS can be decomposed in three components:

.. math::

   R_{01}(j)  =  R_{01}^{\mathbf{GCO}}(j) + R_{01}^{\mathbf{IF}}(j) + R_{01}^{\mathbf{R}}(j) 


The first contribution :math:`R_{01}^{\mathbf{GCO}}(j)`, is the GCO contribution to the RS and is given by the interaction between the EDTM and MDTM of fragments **A** and **B**: 

.. math:: 

   R_{01}^{\mathbf{GCO}}(j)  =  - i \cdot \left [ \vec{E}^{\mathbf{A}}_{01}(j) \cdot \vec{M}^{\mathbf{B}}_{10}(j)  + \vec{E}^{\mathbf{B}}_{01}(j) \cdot \vec{M}^{\mathbf{A}}_{10}(j) \right]   


The :math:`R_{01}^{\mathbf{IF}}(j)` term represents the contribution from the individual fragments (IF) **A** and **B** without any interaction with other fragments:

.. math::
    R_{01}^{\mathbf{IF}}(j)   = - i \cdot \left [ \vec{E}^{\mathbf{A}}_{01}(j) \cdot \vec{M}^{\mathbf{A}}_{10}(j)  + \vec{E}^{\mathbf{B}}_{01}(j) \cdot \vec{M}^{\mathbf{B}}_{10}(j)  \right]

and the :math:`R_{01}^{\mathbf{R}}(j)` contribution contains all contributions from fragment **R**:

.. math::
    R_{01}^{\mathbf{R}}(j)   = & - i \cdot \left[ \vec{E}^{\mathbf{A}}_{01}(j) \cdot \vec{M}^{\mathbf{R}}_{10}(j)  + \vec{E}^{\mathbf{R}}_{01}(j) \cdot \vec{M}^{\mathbf{A}}_{10}(j) \right] \\
               & - i \cdot \left[ \vec{E}^{\mathbf{B}}_{01}(j) \cdot \vec{M}^{\mathbf{R}}_{10}(j)  + \vec{E}^{\mathbf{R}}_{01}(j) \cdot \vec{M}^{\mathbf{B}}_{10}(j) + \vec{E}^{\mathbf{R}}_{01}(j) \cdot \vec{M}^{\mathbf{R}}_{10}(j) \right] 

In the above equations :math:`\vec{E}^{\mathbf{X}}_{01}(j)` and :math:`\vec{M}^{\mathbf{X}}_{01}(j)`, with :math:`\mathbf{X}=(\mathbf{A}, \mathbf{B}, \mathbf{R})`, are the EDTM and MDTM associated with the three fragments.

Using the origin dependency of the MDTM, the GCO contribution can be rewritten in a form similar to the original CO term:

.. math:: 

   R_{01}^{\mathbf{GCO}}(j)  = \frac{\pi \nu_j}{c} \cdot \vec{Y}^{\mathbf{GCO} }(j) \cdot \left[ \vec{E}^\mathbf{A}_{01}(j) \times \vec{E}^\mathbf{B}_{01}(j) \right]

where :math:`\vec{Y}^{\mathbf{GCO} }(j)` is the general coupled oscillator vector. 


As shown in ref. [#ref1]_ most normal modes of a molecule (i.e. not just the carbonyl stretching modes) can be interpreted in terms of the GCO mechanism. That is, for most normal modes one can define the GCO fragments **A** and **B** fragments in such a way that the :math:`R_{01}^{\mathbf{GCO}}(j)` term represent the dominant contributions to the rotational strengths. This second expression for :math:`R_{01}^{\mathbf{GCO}}(j)` does not depend on the MDTM (which is origin dependent). As such, it allows one to interpret the VCD intensity of a mode in terms of interacting EDTMs that are associated with the various moieties of a molecule and their relative orientation. 


The identification of the GCO fragments (which are normal mode dependent) is not always trivial, especially, in molecules without symmetry. Consequently, *VCDtools* offers several options for dividing the molecule into fragments. In *AMSspectra* these fragments are referred as *'Regions'* in analogy to the regions in the *AMSinput* program. Under the **Regions**-menu there are many options to set, alter and save the fragments. Additionally, *VCDtools* is able to make a guess for fragments **A** and **B** as will be discussed in more detail below.


Available options
*****************

Beside the standard calculation and visualization of the atomic contributions to the normal mode (NM) motion, EDTM and MDTM, *VCDtools* offers three more advanced tools that can be utilized when analyzing VCD spectra inside *AMSspectra:* 

+ GCO Analysis

+ Guess GCO Fragments

+ NM Localization on Regions

The first option, *"GCO Analysis"*, uses the above equations to decompose the RS in its different contributions. Printing both the values and important angles between the vectors. Before this option can be run two regions inside the molecule should be defined as fragments **A** and **B**. It is important that these regions do not contain the same atoms. Also since the decomposition is different for each NM, a specific NM should be selected. 

The second option, *"Guess Fragments"*, guesses which atoms belong the fragments **A** and **B** for a selected normal mode. In doing so the :math:`R_{01}^{\mathbf{GCO}}(j)` is maximized while keeping :math:`R_{01}^{\mathbf{R}}(j)` low. Additionally, it ensures that the fragments are localized on a part of the molecule. 

The third option, *"NM Localization on Regions"*, computes the percentage of the mass-weighed normal mode motion that is located on the atoms in the selected regions. One or multiple regions can be computed at the same time and the localizations are determined for all modes within a selected frequency window.


.. only:: html

  .. rubric:: References

.. [#ref1] V.P. Nicu, *Revisiting an old concept: the coupled oscillator model for VCD. Part 1: the generalised coupled oscillator mechanism and its intrinsic connection to the strength of VCD signals*, `Physical Chemistry Chemical Physics 18, 21202 (2016) <https://doi.org/10.1039/C6CP01282E>`__

.. [#ref2] V.P. Nicu, J. Neugebauer and E.J. Baerends, *Effects of Complex Formation on Vibrational Circular Dichroism Spectra*, `Journal of Physical Chemistry A 112, 6978 (2008) <https://doi.org/10.1021/jp710201q>`__

.. [#ref3] M.A.J. Koenis, O. Visser, L. Visscher, W.J. Buma, V.P. Nicu, *GUI Implementation of VCDtools, A Program to Analyze Computed Vibrational Circular Dichroism Spectra*, `J. Chem. Inf. Model 60, 259 (2020) <https://pubs.acs.org/doi/abs/10.1021/acs.jcim.9b00956>`__

