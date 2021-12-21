
eReaxFF, ACKS2, LG dispersion
###############################################################

.. note::

   Only the :ref:`ReaxFF force fields <forcefields>` that mention eReaxFF and ACKS2 support those features.
   The LG dispersion correction is only implemented by force fields in the ``dispersion`` subdirectory.

.. _eReaxFF:

eReaxFF: classical treatment of the explicit electron
****************************************************************************

eReaxFF calculations treat one or more electrons or holes explicitly [#refereaxff]_.

An eReaxFF calculation **requires the following additional force-field parameters to be defined** (equation numbers are referring to the eReaxFF paper [#refereaxff]_):

* The header of the force-field file must begin with the "[ ereaxff acks2 ]" string,
* General parameter 27: the currently reserved :math:`p_{elho}` parameter in the unpublished electron-hole interaction equation (which is still highly experimental and is subject to change),
* General parameter 37: the Gauss exponent parameter :math:`p_{val}` describing the free electron, Eq(3),
* General parameter 41: a different taper radius for electron and hole interactions can be specified here,
* Atomic parameter 24: the :math:`\alpha` parameter in Eq(2),
* Atomic parameter 27: the :math:`\beta` parameter in Eq(2),
* Atomic parameter 13: the :math:`p_{ij}^{xel2}` parameter in Eq(4d),
* Bond parameter 16: the :math:`p_{ij}^{xel1}` parameter in Eq(4d).

Additionally, since the eReaxFF method is usually coupled to the :ref:`ACKS2 charge equilibration method <ACKS2>`, the ACKS2-related parameters should also be defined.

In the input geometry file, the explicit electrons are called ``El`` and the holes are called ``Eh``.

**The eReaxFF implementation is considered experimental**, so users are advised to contact Adri van Duin regarding its use.

.. [#refereaxff] \M. M. Islam et al., *eReaxFF: A Pseudoclassical Treatment of Explicit Electrons within Reactive Force Field Simulations*. J. Chem. Theory Comput. 12, 3463 (2016) `<https://doi.org/10.1021/acs.jctc.6b00432>`__

.. _ACKS2:

ACKS2 charge equilibration
****************************************************************

The ACKS2 charge equilibration scheme has been implemented following the original paper [#refacks2]_.

**Using the ACKS2 scheme requires a suitable force-field**, which is recognized by 
"[ acks2 ]" at the start of the first line of force field file (note: the spaces around "acks2" are important!). 

.. Besides, the `icharg` parameter in the control file must be set to 7.

In addition to the general EEM parameters the ACKS2 scheme needs 
the general force-field parameter #35 ("Xamp") and the atomic cut-off parameter #23 ("softcut").



.. [#refacks2] \T. Verstraelen et al. *ACKS2: Atom-condensed Kohn-Sham DFT approximated to second order*. J. Chem. Phys. 138 (2013) 074108. `<https://doi.org/10.1063/1.4791569>`__


.. _LG_dispersion:

LG dispersion correction
************************

The LG dispersion correction was implemented following the paper Liu et al. [#reflgdisp]_

The LG dispersion correction is turned on when using a suitable forcefield, which is recognized by the “[ lgDispersion=1 ]” key in the file header.

.. [#reflgdisp] \L. Liu at al. *ReaxFF-lg: Correction of the ReaxFF Reactive Force Field for London Dispersion, with Applications to the Equations of State for Energetic Materials*. J. Phys. Chem. A, 2011, 115 (40), pp 11016–11022. `<https://doi.org/10.1021/jp201599t>`__

