.. index:: Single point calculation

.. _SinglePoint:

Single point calculations
=========================

A single point calculation is the simplest task available in the AMS driver. It
simply runs the :ref:`engine<Engines>` once for the given geometry. In other
words, the AMS driver does not explore the potential energy surface (PES), but
simply samples a "single point" of it.

A single point calculation is performed by selecting it with the ``Task``
keyword::

   Task SinglePoint

Note that a single point calculation in AMS includes the calculation of
:ref:`PES point properties<PESPointProperties>`. Many of these, such as the
nuclear gradients and the Hessian, are derivatives at this PES point with
respect to nuclear displacements. These derivatives might be done numerically by
the AMS driver, in which case it would technically run the engine multiple times
and sample PES points around the initial point. However, in AMS this is still
considered a single point calculation. Take for example the calculation of the
normal modes of vibration of a molecule. This used to be a separate task in the
2017 release of the DFTB program, but in AMS is just a single point calculation
with a request for normal modes::

   Task SinglePoint

   Properties
      NormalModes True
   End

See the manual section on :ref:`PES point properties<PESPointProperties>` for an
overview of which properties can be calculated with the ``SinglePoint`` task in
AMS.
