
.. _example green_WBL: 


Example: Benzenedithiol junction: Wide-Band-Limit
=================================================

:download:`Download green_WBL.run <../../../examples/adf/green_Al/green_WBL.run>`

In the wide-band limit (WBL) the coupling to the leads is assumed to be independent of energy. Therefore one does not need to calculate any self-energies. This also means that the eigenspace of the Green's function is independent of energy. It can therefore be diagonalized in advance, greatly speeding up the calculation of the DOS and the transmission. 

In the example $AMSHOME/examples/adf/green_Al/green_WBL/green_WBL.run of *green*, the transmission of  :ref:`benzenedithiol junction<example green_BDT>` in the wide-band limit (WBL) is calculated. In order to model the molecule-metal interface, we do need to include a few gold layers in the calculation. However, unlike  :ref:`before<example green_Au>`, only a single atomic layer as the principal layer is used. 

Because a single atomic layer is an unnatural configuration for gold, a minor amount of smearing is necessary to make the calculation converge. The molecule is sandwiched in between the electrodes just like before (see Fig. 2 in  :ref:`the example for benzenedithiol<example green_BDT>`). However, this time each atomic layer of gold gets its own fragment. The reason for this configuration is that if the WBL is used on the entire gold contact the result is an an unphysical coupling to the leads; even the gold atoms contacting the molecule would have a direct coupling to the environment. A much better result can be obtained by only using the WBL on the back-most atomic layer and letting the electrons propagate naturally through the rest of the contact. Because the WBL is computationally so inexpensive, we can easily calculate the DOS and transmission for 10,000 points instead of 1000. 

A comparison of the resulting transmission with the calculation with self-energies is shown in the following figure: 

.. image:: Images/green_WBL.png
   :width: 10 cm

The WBL shows good agreement with the non-WBL transmission around the Fermi energy (-0.195 Hartree or -5.306 eV). Note that the quality of the WBL depends on the choice of the coupling (ETA). For this particular contact geometry we obtain good agreement for ETA = 0.02 Hartree, but a better value may be found for other electrodes. Finally, the WBL can be incrementally improved by adding more gold layers to the extended molecule. For many layers it converges to the calculation with full self-energies. 

.. literalinclude :: ../../../examples/adf/green_Al/green_WBL.run
   :language: bash
