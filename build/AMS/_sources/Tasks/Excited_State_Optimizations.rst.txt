.. index:: Excited state optimizations

.. _ExcitedStateOptimizations:

Excited state optimizations
===========================

It depends on the engine if it is possible to do an electronically excited state optimization,
like an electronically excited state :ref:`geometry optimization <GeometryOptimization>`,
:ref:`transition state search <TransitionStateSearch>`, :ref:`linear transit, PES scan <PESScan>`, or :ref:`IRC <IRC>`.
Required is that the engine should be able to calculate the nuclear gradient for a particular electronically excited state.
ADF and DFTB are engines that can do such calculation.
If the excited state gradient is available one can also calculate an :ref:`IR spectrum <IRFrequencies>` of the excited state, and
one could calculate a :ref:`vibrationally resolved electronic spectrum <VibrationallyResolvedElectronicSpectra>`.

One should look in the documentation of the engine how to set up the calculation of the excited state gradient.
