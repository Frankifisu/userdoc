
.. index:: VG-FC
.. index:: Vertical gradient Franck-Condon
.. index:: Independent mode displaced harmonic oscillator
.. index:: IMDHO
.. _VG-FC:
.. _IMDHOVibronicStructure:

VG-FC: Vertical Gradient Franck-Condon
======================================

Electronic spectra, such as absorption, emission, phosphorescence, and ionization, may contain a vibrational structure.

In the vertical gradient Franck-Condon (VG-FC) method some extra assumptions are made compared to the Adiabatic Hessian Franck-Condon (AH-FC) method.
VG-FC is also called the Independent Mode Displaced Harmonic Oscillator (IMDHO) model.
The AH-FC model (used in the :ref:`FCF Module <FCF>`) makes the following assumptions:

* 1. It employs the adiabatic (Born-Oppenheimer) approximation and treats the 
  nuclei as moving in an effective potential defined by the electronic configuration.
* 2. It works at the Franck-Condon point and assumes that the transition occurs at
  the ground state equilibrium structure for absorption and at the excited state equilibrium structure for emission.
* 3. It applies the harmonic approximation to both the ground and excited state
  potential energy surfaces.

The VG-FC model makes following additional assumptions:

* 4. It assumes the excited state PES has the same shape as that of the ground state, 
  but it is displaced from it, i.e. both states have the same normal modes
  and frequencies but different equilibrium geometries. 
* 5. The excited state equilibrium structure is found from a Newton-Raphson step from
  the ground state geometry using the excited state gradient at this point.

Under these simplifying approximations we can reduce the ingredients necessary for a spectrum calculation to an excited state gradient and a set of ground state normal modes. Furthermore it uses a time-domain description of the absorption cross-section (this introduces no further approximations) so we do not need any explicit Franck-Condon factors as is done in the :ref:`FCF Module <FCF>`. This approach is particularly effective for large molecules as it shows linear scaling with the number of normal modes. Further details on how to use this method, and the VG-FC model in general can be found below.

The approximations we make remove the need for an excited state geometry optimization and frequency analysis. This means the most expensive step in a typical calculation is actually the ground state frequency analysis. The ability of Mode Tracking to generate a set of approximate normal modes, without performing a full frequency analysis can be applied to the calculation of vibrationally resolved optical spectra. This is exactly what is done in :ref:`Vibronic-Structure Tracking<VibronicStructureTracking>`. On the other hand, the ability of Mode Refinement to refine entire spectral regions at once means this method can be transferred to calculating vibrationally resolved optical spectra from a select number of (vibronically active) approximate normal modes. This idea is applied in :ref:`Vibronic-Structure Refinement<VibronicStructureRefinement>`. Under suitable assumptions, the computational cost of calculating an approximation of the vibronic-structure can be reduced significantly through the use of these two methods, allowing for application to large molecules inaccessible to more detailed methods. While they are clearly best suited for these large molecules, they can also serve as an efficient method to obtain quick, first approximations for more moderately sized molecule.

With the VG-FC model one can calculate the 0-0 energy difference between the ground state and excited state.
In this VG-FC method the vibrationally resolved emission spectrum will be a mirror image of the vibrationally resolved absorption spectrum, in which the 0-0 transitions are the same.

.. note::
    The VG-FC model uses certain approximations which may not always be valid. Something to look out for that may affect the reliability of VG-FC results are large changes in conformation upon excitation. In this case the normal modes of the excited state may be completely different from those of the ground state, at which point the model is not expected to produce reliable results. Should non-adiabatic effects become important, the BO approximation could potentially break down as well. In these cases the :ref:`FCF Module <FCF>` may provide a more suitable alternative to the VG-FC model.

.. seealso::

  Tutorials: `Resonance Raman <../../../Tutorials/VibrationalSpectroscopy/ResonanceRaman.html>`__, `Vibrationally resolved electronic spectra with ADF <../../../Tutorials/VibrationalSpectroscopy/VibrationallyResolvedElectronicSpectraADF.html>`__, `Vibrationally resolved electronic spectra with DFTB <../../../Tutorials/VibrationalSpectroscopy/VibrationallyResolvedElectronicSpectraDFTB.html>`__

Theory
------

Here we will introduce the theory behind the model used to compute vibronic couplings. We use the so-called Vertical Gradient Franck-Condon (VG-FC) method, also called Independent Mode Displaced Harmonic Oscillator model (IMDHO). The VG-FC model as used here works as follows: The PES in the ground state is assumed parabolic (the harmonic approximation). Upon excitation, we assume that the only change to the PES that occurs is a shift in origin (i.e. no stretching or rotation of the parabolic well). This means, both the normal modes and their frequencies remain the same in both the ground and excited state. The result is that a spectrum can be calculated using only a single excited state gradient at the optimized ground state geometry. Hence we avoid the expensive excited state geometry optimization and frequency analysis used by methods such as the :ref:`FCF Module <FCF>`.

Moving to a slightly more detailed discussion, we can start with an expression for the absorption cross-section in terms of a sum over contributions from different Franck-Condon factors, each homogeneously broadened with an assumed Lorentzian of linewidth :math:`\Gamma`. For excitation from the vibrational ground state of electronic state m, to electronic state n we get the following expression (Hartree atomic units are used throughout):

.. math::

   \sigma_{n\leftarrow m}(\omega) = \frac{4\pi\omega}{3c}|\mu_{mn}|^2 \sum_{l_{n,1}}...\sum_{l_{n,N_{modes}}} \frac{\Gamma\prod_{i=1}^{N_{modes}}|\langle l_{n,i}|0_{m,i}\rangle|^2}{\bigg(E_{n,0}+\sum_i^{N_{modes}}\omega_i l_{n,i}-E_{m,0}-\omega\bigg)^2+\Gamma^2}

Here the :math:`\mu_{mn}` is the transition dipole moment and the :math:`\prod_{i=1}^{N_{modes}}|\langle l_{n,i}|0_{m,i}\rangle|^2` denote the Franck-Condon factors for excitation from the vibrational ground state to the vibrationally excited state of the excited state PES, with quantum numbers :math:`l_{n,i}`. This sum-over-states formulation is what is also used to compute the spectrum in the :ref:`FCF Module <FCF>`. While efficient pre-screening and thresholding techniques can make this method applicable to moderately sized molecules, it is still quite expensive for large molecules. We can derive an expression which is equivalent to the one above, but which enjoys significant computational benefits. This is done by writing the cross-section as an integral over time:

.. math::
    \sigma_{n\leftarrow m}(\omega) = \frac{4\pi\omega}{3c}|\mu_{mn}|^2 Re\int_{0}^{\infty} \langle i|i_n(t)\rangle e^{i[\omega + E_{m,0}]t}\cdot e^{-\Gamma t}dt

Here, :math:`\langle i|i_n(t)\rangle` denotes the overlap of the initial state, propagated along the excited state PES with itself at time :math:`t=0`. This expression is still completely general, however, using the :ref:`assumptions of the VG-FC model<VibrationallyResolvedElectronicSpectra>`, this overlap admits a simple closed form expression:

.. math::
    \langle i|i_n(t)\rangle = \prod_{j=1}^{N_{modes}}\exp\left[-\frac{\Delta_{n,j}^2}{2}(1-e^{-i\omega_jt})\right]e^{-i E_{n,0} t}

This expression can be derived by different methods and admits a few interpretations, the details of which we will not go into here. The interested reader is referred to reference [#ref1]_. Instead we will focus on its numerical implementation. The great computational advantage of this expression is that it scales only weakly with the number of degrees of freedom. Compare this with the sum-over-states formalism above, where the number of FCF's needed to have a converged sum proliferates for large molecules and the advantage becomes clear.

The :math:`\Delta_{n,j}` appearing in the expression are the dimensionless normal mode displacements at the equilibrium geometry in state n, compared to state m along normal mode j which has angular frequency :math:`\omega_j`. They represent the change in origin of the PES along a particular normal mode. These are the parameters which control the shape of the spectrum. Under the assumptions we listed above they can be calculated from the excited state energy gradient at the ground state equilibrium structure as:

.. math::
    \Delta_{j} = \frac{q^m_j \cdot \nabla_m E}{\omega_j^{3/2}}

Where we have suppressed the n subscript. The gradient is with respect to mass weighted coordinates and the :math:`q^m_j` denote the mass-weighted normal modes.

Essentially, we use the (assumed) parabolic shape of the PES in the harmonic approximation along each of the normal modes to determine the displacement from the gradient projection along that mode. An important consequence of the simplified VG-FC model is that the Franck-Condon factors can be expressed in closed form:

.. math::
    |\langle l_i|0_i\rangle|^2 = \frac{\bigg(\frac{\Delta_i}{2}\bigg)^2}{l_i !} e^{-\frac{\Delta_i^2}{2}}

Modes with the largest displacement are then expected to also have the largest impact on the structure of the vibrational progression in the spectrum. This gives us an obvious candidate for a tracking method to be used with the Mode Tracking protocol. This approach is taken in the :ref:`Vibronic-Structure Tracking<VibronicStructureTracking>` module.

.. _VibronicStructureTracking:

Theory: Vibronic-Structure Tracking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vibronic-structure tracking (VST) is a method for obtaining quick and approximate vibrationally resolved optical spectra for larger sized molecules. It is based on the mode-tracking algorithm and works by tracking those modes that are expected to have the largest impact on the vibronic-structure of the spectrum. Its AMS implementation follows that in reference [#ref1]_.

The modes that are tracked by the mode tracking routine are used to generate a UV/vis spectrum. This is done using the Vertical Gradient Franck-Condon (VG-FC) method, also called the Independent Mode Displaced Harmonic Oscillator (IMDHO) model as described on the :ref:`Vibronic-Structure<IMDHOVibronicStructure>` page. This model reduces the necessary TD-DFT calculations to a single excited state gradient performed at the ground state equilibrium geometry. At this point it is typically the ground state frequency analysis which becomes the bottleneck for large molecules. Through the use of Mode Tracking we can circumvent this step and calculate only those modes which will significantly impact the vibronic fine structure. This yields a very cheap and efficient method for obtaining vibrationally resolved optical spectra.

The use of Mode Tracking within the context of vibronic-structure calculations proceeds as follows: from an initial guess for a normal mode, we construct a new basis vector which we hope will improve the quality of our initial guess. We then iteratively expand the basis by refining those modes which have the largest impact on the vibronic fine structure. We keep iterating until we deem the spectrum to be converged. We'll address the technical details of this procedure in this section.

Let us first consider how we can gauge which modes will have a large impact on our spectrum. Over on the :ref:`Vibronic-Structure<IMDHOVibronicStructure>` page, we showed that according to the VG-FC model, the Franck-Condon factors can be written as:

.. math::
    |\langle l_i|0_i\rangle|^2 = \frac{\bigg(\frac{\Delta_i}{2}\bigg)^2}{l_i !} e^{-\frac{\Delta_i^2}{2}}

This expression implies modes with large displacements :math:`\Delta_j` will have the largest Franck-Condon factors. Thus, we expect that modes with large oscillator displacements will contribute most strongly to the vibronic fine structure of the spectrum. This suggests a tracking method in addition to those described in the :ref:`Mode Tracking<ModeTracking>` documentation. Namely, to track the mode with the largest :math:`\Delta_j`. This is the only setting for the ``TrackingMethod`` supported by Vibronic-Structure Tracking and is automatically set when choosing Vibronic-Structure Tracking as the Vibrational Analysis type. As a reminder, the oscillator displacements can be obtained from the assumed parabolic shape of the excited state PES and the known excited state gradient:

.. math::
    \Delta_{j} = \frac{q^m_j \cdot \nabla_m E}{\omega_j^{3/2}}

This expression for our normal mode displacements suggests that a reasonable guess for a hypothetical normal mode with a large effect on the spectrum is given by the normalized excited state gradient, as this maximizes the projection. 

The choice of preconditioner is of course an important one. While better preconditioners such as the Jacobi-Davidson method can lead to fast and tightly directed convergence of the modes, this may not be ideal in the case of Vibronic-Structure Tracking, as we are not necessarily focused on obtaining converged modes but rather obtaining a converged spectrum. By default the method does not use any preconditioner for generating normal modes from the residual vectors to allow the procedure to more freely explore the entire space of modes. This means that the new basis vector produced on each iteration is the (normalized) residual vector of that iterations selected mode. Note that this is different from using the Davidson method with an identity matrix as guess for the Hessian. The user is still able to use any of the pre-conditioning options provided by the stand-alone mode tracking method, however we suggest the user uses the default ``I`` (for identity) as the ``UpdateMethod``. This also conveniently means no approximate Hessian is required.

It is important to choose a suitable convergence criterion. When using Vibronic-Structure Tracking, the aim is to get an approximation of the progression in the spectrum. The convergence of the modes then takes a backseat to the convergence of the spectrum. Although the two usually go hand in hand, requiring that all modes be converged in the usual mode-tracking sense is likely to be far too restrictive. Thus the convergence criterion used for VST is the following: at every iteration, the previous iteration's spectrum is subtracted from the new one. The absolute difference is then integrated on the requested frequency range. Convergence is achieved once the so-obtained number drops below a pre-set convergence threshold. The result is that it may not be the case that all modes are exact normal modes yet, however further refinement will have a limited effect on the resulting spectrum, for example due to these modes having very small Franck-Condon factors. 

Convergence according to this criterion is affected by the other options that the user chooses, see the section on how the adiabatic excitation energy is calculated.

.. _VibronicStructureRefinement:

Theory: Vibronic-Structure Refinement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vibronic-Structure Refinement takes the idea of Mode Refinement, and applies it to the calculation of vibrationally resolved optical spectra. Under the assumptions of the Vibronic-Structure application, the most time-consuming step becomes the calculation of the ground state normal modes. However, we may not be interested in all normal modes that contribute to the Vibronic fine structure of a spectrum. By using Mode Refinement we can limit ourselves to the spectral region of interest, or to modes which we expect to have the largest impact on the fine structure. The details of the Mode Refinement protocol can be found on the relevant :ref:`documentation page<ModeRefinement>`.

Theory: Adiabatic excitation energy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last aspect we will comment on here is the calculation of the adiabatic excitation energy. The number we get from an excited state calculation is the vertical excitation energy (:math:`\Delta E_{vert}`), this number is generally unobservable in spectra. The more interesting quantity is the adiabatic excitation energy (:math:`\Delta E_{ad}`). The former is the difference in energy between the two PES'es at the ground state geometry, the latter is the difference in energy between the ground and excited state vibrational ground states. Since we assumed both PES'es to have the same frequencies, the zero-point energy of the two states are the same and hence, the adiabatic energy difference is the same as the 0-0 energy difference (:math:`\Delta E_{0-0}`). This is simply the difference between the bottom of the two PES'es. It can be reconstructed from the excited state gradients projected onto our normal modes, as well as their frequencies. For a molecule with N modes we obtain:

.. math::
    \Delta E_{ad} = \Delta E_{vert} - \sum_j^{N_{modes}}\frac{1}{2}\omega_j\Delta_j^2

Where the sum represents the reorganization energy stored in the excited oscillator modes. Depending on the desired information, one can use two different representations of the spectrum. The first is to simply plot the spectrum against an energy range with the ground state energy as an offset. This would represent a true absorption spectrum that can be compared directly with experiment. However, the energy difference :math:`\Delta E_{vert} - \Delta E_{ad}` in the VG-FC model is reconstructed only from the ground state equilibrium structure and can thus be somewhat unreliable. If the user is primarily interested in the shape of the spectrum, using the 0-0 excitation energy as an offset may be a more suitable choice. The latter is the default setting in AMS, but the method supports both options.

Note that in case of a Vibronic-structure tracking (VST) calculation we only have access to a small set of approximate normal modes, we will have an approximation of :math:`\Delta E_{ad}` that changes from iteration to iteration as new normal modes are introduced and the old normal modes are refined. If a spectrum relative of the 0-0 energy is requested, the shift caused by the iterative convergence of :math:`\Delta E_{ad}` is not taken into account, although it will still have some effect on the spectrum as it also appears in the integral that defines the spectrum. If one is interested in a converged approximation of :math:`\Delta E_{0-0}` it may be more reliable to provide an absolute frequency range for the spectrum as the shift in the peak locations will then also affect convergence.

.. _VG-FC_VS:

Input: Vibronic-Structure all modes
-----------------------------------

As mentioned, we need both a set of ground state normal modes as well as an excited state gradient. All the normal modes are calculated using the AMS engine that was selected, or, in case the user has a pre-calculated set of normal modes, these can be read from a .rkf file using the ``ModeFile`` key in the ``NormalModes`` sub-block. In this latter case, the engine is not used. One can then use the keys in the ``ModeSelect`` block to filter out specific modes, or, simply select all modes using the ``Full`` key in this block. For further details on how to use the Mode Select block for more specialized selection options, see the :ref:`Mode Select<ModeSelect>` documentation. As for the excited state information, this is passed to the application via the ``ExcitationSettings`` block. Additionally there are (optional) settings related to the appearance of the spectrum under the ``AbsorptionSpectrum`` block. For an overview of the input options see the list of keys at the end of this page.

For completeness we provide an example of what the user input may look like::

   Task VibrationalAnalysis
   VibrationalAnalysis
      Type VibronicStructure
      NormalModes
        # Select all modes present in the .rkf file
        ModeSelect
          Full True
        End
      End
      ExcitationSettings
        ExcitationInfo File
        ExcitationFile ./your_excitation.t21
        Singlet
          B1.u 2
        End
      End
      AbsorptionSpectrum
        LineWidth 100.0
        AbsorptionRange -500.0 4000.0
      End
   End

.. _VG-FC_VST:

Input: Vibronic-Structure Tracking
----------------------------------

VST is notably the only Vibrational Analysis task that does not support the ``NormalModes`` block as no initial normal modes are necessary. The excited state gradient fills this role instead. Furthermore, the recommended default of using the identity matrix as a preconditioner means that no approximate Hessian is required either.

One thing to note regarding the Mode Tracking settings is that VST features a convergence criterion not present in standard Mode Tracking. The tolerance for the convergence of the spectrum is set using the ``ToleranceForSpectrum`` keyword in the ``ModeTracking`` block. The default is set to 0.01 and should be sufficient for most purposes, but :ref:`restarting<VSTRestart>` with a lower value may improve the reliability of the convergence. 

.. note::

  The usual Mode Tracking tolerances are still present in addition to the spectral tolerance mentioned above. This is so we do not track modes that have already converged. Instead, once a mode is converged in the usual mode tracking sense, we switch to the next mode that satisfies our tracking criterion. The defaults should normally apply, but may be loosened a bit to allow for more free subspace exploration.

A typical Vibronic-Structure Tracking run may be setup as follows::

   Task VibrationalAnalysis
   VibrationalAnalysis
      Type VibronicStructureTracking
      # Select our excited state energy+gradient from a previous calculation
      ExcitationSettings
        ExcitationInfo File
        ExcitationFile ./your_excitation.t21
      End
      # Tuning how our spectrum will look
      AbsorptionSpectrum
        LineWidth 250.0
        AbsorptionRange -500.0 6000.0
      End
      ModeTracking
        UpdateMethod I
      End
   End

.. _VSTRestart:

Input: Restarting VST
^^^^^^^^^^^^^^^^^^^^^

The Vibronic-Structure Tracking task is fully restartable from a previously completed VST run. The main reason why it may be useful to perform a restart is related to the way the spectrum is generated. Most modules/applications in AMS that calculate a spectrum usually produce a stick spectrum. This stick spectrum is then convoluted against either a gaussian or lorentzian of specified width or area. This allows one to tweak the homogeneous broadening post-calculation to improve agreement with experiments. VST operates differently, in that the Lorentzian linewidth is specified at the start of the calculation as an essential input parameter. If upon convergence it becomes clear that a different linewidth would have been better suited for the spectrum at hand, one can restart the calculation with this new linewidth. The program then computes a new spectrum using these new settings and repeats the last iteration of the previous run. The latter is done because the linewidth directly influences the convergence (larger linewidths tend to converge more easily as the features are not as sharply resolved). If the spectrum does not change after the first iteration the program terminates as usual and the new spectrum is now available to the user. However, if this additional iteration does not pass the convergence test, the program keeps iterating until the spectrum converges for this new linewidth.

In addition to changing the linewidth post-calculation, the user is also free to change the spectral range that is to be computed as well as its resolution through the ``FrequencyGridPoints`` keywords. Alternatively, the tolerance used may be lowered if tighter convergence is required. Importantly however, none of the previous run's input settings are retrieved upon restart, so any settings the user doesn't want to change have to be same in the new run script as in the old. The easiest way to restart is to simply re-use the previous run's runscript under a new name and then changing the relevant settings.

The restart functionality is controlled by the ``RestartPath`` keyword. One simply states the path to a previous calculation's .rkf file from which the relevant data is to be read. The .rkf file of any VST runs contains a section labeled ``VSTRestart`` which contains the data needed to restart from that run. Restarting is then a simple one-liner in the ``VibrationalAnalysis`` block::

  VSTRestartFile ./previous_run.results/ams.rkf


.. _VG-FC_VSR:

Input: Vibronic-Structure Refinement
------------------------------------

Vibronic-Structure Refinement (VSR) assumes that the modes relevant to the vibronic-structure are, at least in an approximate sense, known a priori.
The VSR method takes these approximate modes and refines them via the Mode Refinement algorithm.
The approximate normal modes should thereby span a subspace containing the exact normal modes and, the more similar they are to the exact mode, the better they allow to reproduce the spectrum of a full ground state frequency analysis.
Naturally, the refinement becomes more accurate with increasing dimensionality of the spanned subspace, although this this increases the computational costs.
In any case, the subspace needs to contain those modes that are most relevant for the vibronic progression for the entire approach to work, which leads to the question, how do we select such modes?

This is done using familiar ``ModeSelect`` block from the mode selective analysis tasks tasks. While all the usual options are available, for which further details can be found on the :ref:`Vibrational Analysis<ModeSelect>` page, there are two selection methods that are geared specifically towards VSR. Within the VG-FC model, the parameters defining the effect a mode will have on the spectrum are the oscillator displacements :math:`\Delta_j`. We can determine these values from the projection of the approximate normal modes onto the gradient in combination with their respective frequencies. We are then interested in those modes with the largest displacement. To select these, two options are available:

::

   Task VibrationalAnalysis
   VibrationalAnalysis
      Type VibronicStructureRefinement
      NormalModes
         ModeSelect
            LargestDisplacement integer
            DisplacementBound float
            ...
         End
         ...
      End
      ...
   End

``LargestDisplacement integer``
  sets an integer value N, to select the N modes with 
  the largest displacements as calculated within the VG-FC model. This method limits the total number of modes we refine and thus places an upper bound on the computational cost required by the method, but it does not ensure that all relevant modes have been selected. In particular there may still be modes with large displacements that have been omitted and as such peaks or progressions may be missing from the spectrum.

``DisplacementBound float``
  Alternatively this selects all approximate modes with a
  displacement greater than the supplied lower bound. An appropriate choice for this value ensures all modes which visibly affect the spectrum (at least at the lower level of theory used to produce the approximate modes) are included in the subspace basis used for Mode Refinement. The displacements :math:`\Delta_j` are dimensionless and the largest ones will typically be of order one. Based on this, a value of ``0.01`` for this parameter will generally select all relevant modes. This of course comes at the trade-off that for general molecules it is not known how many such modes there will be and the computational cost may be larger than expected. But, if one is not discouraged by this, this will of course yield the most accurate results. Values up to ``0.05`` may still provide reasonable results while minimizing computation times. Using larger linewidths (``AbsorptionSpectrum%LineWidth``) for the homogeneous broadening can help to correct for the non-resolved modes.

The calculation setup for Vibronic-Structure Refinement is essentially the same as that for Vibronic-Structure, the only difference being that the modes that we provide will first be refined, before a spectrum is computed. A detailed description is given on the :ref:`Vibronic-Structure<IMDHOVibronicStructure>` page. A typical VSR calculation can be setup as follows::

   Task VibrationalAnalysis
   VibrationalAnalysis
      Type VibronicStructureRefinement
      # Select our normal modes from a previous calculation
      NormalModes
        ModeFile ams.rkf
        ModeSelect
           # select all modes with VG-FC displacements over 0.01
           DisplacementBound 0.01
        End
      End
      # Select our excited state energy+gradient from a previous calculation
      ExcitationSettings
        ExcitationInfo File
        ExcitationFile ./your_excitation.t21
        # Select second singlet excitation with symmetry label A
        Singlet
          A 2
        End
      End
      # Tuning how our spectrum will look
      AbsorptionSpectrum
        LineWidth 250.0
        AbsorptionRange -500.0 6000.0
      End
   End

.. _ExcitationSettings:

Input: Excited State
--------------------

Both the excited state gradient at the ground state equilibrium structure as well as the vertical excitation energy are necessary to obtain a spectrum. These can be provided by most TD-DFT programs, including ADF. Unfortunately, the AMS driver does not yet support computing these properties on the fly. As a result they are currently required as user input. One can use ADF or DFTB to compute them and then either read them from the produced output file, or copy and paste them to an inline input block.

::

   Task VibrationalAnalysis
   VibrationalAnalysis
      Type ...
      ExcitationSettings
         ExcitationInputFormat [File | Inline]
         ExcitationFile string
         EnergyInline float
         GradientInline # Non-standard block. See details.
            ...
         End
         Singlet # Non-standard block. See details.
            ...
         End
         Triplet # Non-standard block. See details.
            ...
         End
      End
   End

``ExcitationInputFormat [File | Inline]``
  this keyword is used to specify whether the gradient and 
  energy are to be read from a kf file or if one chooses to use the inline block for them. Currently, no TD-DFT engine is implemented in the AMS driver. Furthermore, ADF uses the old tape21 format for its output which is quite different from the more streamlined AMS format. The ``inline`` option allows one to bypass any possible confusion here. The ``File`` option requires the specification of the specific excitation to read, which we will discuss below.

``GradientInline``
  is the block where the gradient can be specified if the
  inline option is selected. The format can be either a N by 3 block (N rows, 3 columns) or a 3N long column vector if one happens to have a gradient in this format.
  The gradient values should be in the unit Hartree/Bohr.

``EnergyInline float``
  is used to specify the excitation energy.
  This will just be a single floating point number (in Hartree).

The resulting input would look like::

   Task VibrationalAnalysis
   VibrationalAnalysis
      Type ...
      ...
      ExcitationSettings
        ExcitationInfo Inline
        # Excited state gradient for transhexatriene 14 atoms x 3 coordinates (to be provided in Hartree/Bohr)
        GradientInline
           -0.03786125        0.01786798        0.00003833
            0.05322148       -0.00798712       -0.00004152
           -0.06658803        0.01373495        0.00004727
            0.06656379       -0.01374825        0.00002398
           -0.05318451        0.00799875       -0.00002097
            0.03783718       -0.01786722        0.00001362
            0.00382226        0.00327391        0.00001046
           -0.00046176       -0.00499971       -0.00003583
            0.00014312        0.00534412       -0.00001335
            0.00011081       -0.00558254       -0.00002107
           -0.00011074        0.00558350       -0.00000933
           -0.00014517       -0.00534330        0.00000839
           -0.00381513       -0.00327314       -0.00000248
            0.00046796        0.00499807        0.00000250
        End
        # The vertical excitation energy is simply a float (to be provided in Hartree)
        EnergyInline 0.17062882
      End
   End

``ExcitationFile string``
  If ``ExcitationInputFormat`` is set to ``File`` one also has to set the ``ExcitationFile`` keyword to provide a path to the file from which the info should be read.

``Singlet or Triplet``
  In case the excited state information should be read directly from a file,
  one should specify which excitation AMS should read. This is done analogously to how this is done for excited state gradients in ADF. One chooses either the ``Singlet`` or ``Triplet`` blocks (for singlet-singlet or singlet-triplet excitations respectively). Once such a block is chosen, a line containing the symmetry label, followed by the number of the excitation of that symmetry. As for the symmetry labels, the notational convention used can be found in the `ADF manual appendix <../../../ADF/Appendices/Symmetry.html#schonfliess-symbols-and-symmetry-labels>`__ on symmetry labels. If symmetry was disabled, either explicitly by the user or when using TD-DFTB which does not support symmetry, when calculating the excited state properties, the symmetry label ``A`` should be used. Vibronic-structure calculations are only supported for one excitation at a time.

The resulting input block looks something like this::  

   ExcitationSettings
      ExcitationInputFormat File
      ExcitationFile ./ExcitedState.results/myengine.rkf
      Singlet
        A 1
      End
    End

Input: Producing the spectrum
-----------------------------

To go from normal modes to an actual spectrum, we have to solve the integral that we introduced in the first section, the details of which will be discussed here.

For long times, the integrand is dominated by the exponential damping term. We can define a suitable cut-off by demanding that this damping term be smaller than some threshold. As mentioned, the integral is evaluated using a Chebyshev quadrature. The number of Chebyshev nodes used for the integral can then be determined from this integration limit and the time step size. This time step size should be large enough to accurately represent the highest frequencies that are present in the highly oscillatory integrand. The Nyquist frequency can be used as a guide here: the highest frequency should be represented by at least two samples each period. Note however, that in principle there is no upper bound to the frequencies present in the integrand due to the fact that modes can be excited to arbitrarily high energy levels. Fortunately, the Franck-Condon factors will quickly act to dampen these high frequencies, restricting their significance. The user may either supply a time step size directly or leave this up to the program to determine. If the latter is chosen the highest relevant frequency is estimated by assuming that oscillator excitations are relevant up to about twice the Huang-Rhys parameter (which follow directly from the displacements). This default should in most cases be sufficient to produce a converged integral.

The keywords associated with the different input parameters are collected under the ``AbsorptionSpectrum`` block. It contains the following keys:

::

   Task VibrationalAnalysis
   VibrationalAnalysis
      Type ...
      ...
      AbsorptionSpectrum
         AbsorptionRange float_list
         FrequencyGridPoints integer
         LineWidth float
         SpectrumOffset [absolute | relative]
      End
   End

``LineWidth float``
  sets the lorentzian line width and thus has a large impact on
  the appearance of the final spectrum. It may be used to improve the agreement of the computed spectrum with experiment.
  Another purpose that the linewidth may serve is that some low frequency modes may not be represented very accurately within the VG-FC model. However, these modes do not result in particularly distinct vibronic progressions but rather cause an unspecific broadening of existing peaks. Applying a homogeneous peak broadening by increasing the value of :math:`\Gamma` may be an effective (albeit a little ad hoc) way of resolving such issues, should they occur. The default value is :math:`200  cm^{-1}` but it is recommended to do some experimentation with this value.

``AbsorptionRange float_list``
  keyword specifies the frequency range (in :math:`cm^{-1}`) that is to be computed by VST. 

``SpectrumOffset [absolute | relative]``
  specifies whether the range provided by the ``AbsorptionRange`` keyword is relative to the 0-0 excitation energy 
  (``Relative``), or relative to the vertical excitation energy (``Absolute``).
  Due to the limited accuracy of the VG-FC model at predicting :math:`\Delta E_{0-0}` the default is ``Relative`` with a ``AbsorptionRange`` of [-500,4000].

``FrequencyGridPoints integer``
  sets the number of points we use on our frequency 
  grid. It is set to 400 by default which generally produces a smooth looking spectrum.

The current implementation of VG-FC vibronic-structure supports only spectra for one excitation at a time. The spectrum is normalized such that the highest peak is equal to 1 in arbitrary units. For this reason the prefactor of the integral is irrelevant and transition dipole moments do not affect the appearance of the spectrum. 

.. only:: html

  .. rubric:: References

.. [#ref1] J.R. Reimers, K.R. Wilson and E.J. Heller, *Complex time dependent wave packet technique for thermal equilibrium systems: Electronic spectra* `The Journal of Chemical Physics 79, 4749 (1983) <https://doi.org/10.1063/1.445618>`__
