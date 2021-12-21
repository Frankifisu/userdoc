.. _viscosity_benzene:

Viscosity of benzene
********************

This tutorial will show how to calculate the **viscosity of liquid benzene using the Green-Kubo relation**:

.. math::

    \eta = \frac{V}{k_{\rm{B}}T} \int_0^\infty <P_{\alpha\beta}(0)P_{\alpha\beta}(t)> \rm{d} t

where :math:`\eta` is the viscosity, :math:`V` is the cell volume,
:math:`k_{\rm{B}}` is the Boltzmann constant, :math:`T` is the temperature,
:math:`P_{\alpha\beta}` is an off-diagonal component of the pressure tensor,
and :math:`t` is time.  The function
:math:`<P_{\alpha\beta}(0)P_{\alpha\beta}{t}>` is an **autocorrelation
function** with the average taken over all time origins and off-diagonal
components (*αβ* is *yz*, *xz*, or *xy*).

The pressure tensor equals the stress tensor plus a kinetic contribution.

Step 1: Create a box of benzene
=========================================

Create a box of 16 benzene molecules with density 0.875 g cm\ :sup:`-3`
(experimental room-temperature density of benzene) using the **Builder** in AMSinput,
or download and import a premade :download:`xyz file <../downloads/benzene_bulk_16.xyz>`.

.. rst-class:: steps

  \
    | Start AMSinput
    | **Edit → Builder**
    | Enter ``13.333`` on the diagonal to change the box to a cube of 13.333 Å
    | **Fill box with:** ``16`` copies of: start typing ``benzene`` and then click the ``Benzene (ADF)`` entry in the list that pops up.
    | Click the **Generate Molecules** button
    | Click the **Close** button at the bottom of the Builder window

The molecules are generated at random positions and orientations, with constraint  that all atoms (between different molecules) are at least the specified distance (2.5 Å) apart.

Step 2: Set up the benzene MD simulation
==================================================

The next step is to set up the details of the simulation.

.. rst-class:: steps

  \
    | Switch to the ForceField panel: |ADFPanel| → |ForceFieldPanel|
    | Set **Periodicity → Bulk**
    | Set **Type → GAFF**
    | Check the **Automatic atom typing** checkbox
    | **Edit → Crystal → Map atoms to 0..1** will place the atoms inside the unit cell (optional)
    | At the bottom right, click the **Pre-optimize** button and wait for the pre-optimization to finish
    | Set **Task → Molecular Dynamics**

For the MD simulation, we will set up a room-temperature simulation
thermostatted with a Nose-Hoover thermostat.  It is important to set **Sample
frequency** to a small number. It will save not only the atomic coordinates but
also the pressure tensor at that sample frequency, and the pressure tensor
needs to be saved frequently to calculate the integral accurately.

.. rst-class:: steps

  \
    | **Model → MD**
    | Number of steps: ``100000``
    | Time step: ``1`` fs
    | Sample frequency: ``5`` (or smaller)
    | Initial temperature: ``298`` K
    | Click on |MoreBtn| next to **Thermostat**
    | Click on the |AddButton| to add a thermostat
    | Thermostat: ``NHC``
    | Temperature(s): ``298``
    | Damping constant: ``100`` fs

We **must** also tell the AMS driver to **calculate the pressure** (if you use a barostat, that
will happen automatically).  **To save disk space**, we can also turn off most of
the things usually saved to the trajectory file, e.g. velocities and molecular
bonds.

.. rst-class:: steps

  \
    | **Details → Expert AMS**
    | Scroll down to **MolecularDynamics Trajectory**:
    | Uncheck **Write velocities**
    | Uncheck **Write charges**
    | Uncheck **Write bonds**
    | Uncheck **Write molecules**
    | Scroll down to **MolecularDynamics** 
    | Check **Calc pressure**


Step 3: Run the simulation
===================================

Now we will run your set-up:

.. rst-class:: steps

  \
    | Use the **File → Run** command
    | When asked to save your input, save it with the name ``Benzene``

.. important::

    **Double-check that the pressure is calculated**. At the start of the
    simulation, open the logfile (SCM → Logfile), and make sure that numerical
    values (and not "n/a") is printed for the pressure. If there is no
    pressure, then stop the simulation and go back to Step 2.

.. note::

  Running this calculation takes approximately 20 minutes. 

Step 4: Analyze the simulation results
========================================

Wait until the calculation has finished, and then open it in AMSmovie.

.. rst-class:: steps

  \
    | Start AMSmovie: **SCM → Movie** in the logfile window
    | Press the Play button (the triangle pointing right at the left bottom of the AMSmovie window)


The pressure tensor autocorrelation function should only be calculated after the simulation has equilibrated.

.. rst-class:: steps

  \
    | In the AMSmovie window:
    | Use the **MD Properties → Potential Energy** command
    | Use the **MD Properties → Time** command

The simulation seems to equilibrated quite quickly. After frame 4000 (time 20
ps) the potential energy seems to fluctuate around a constant value, indicating
that the simulation as likely equilibrated at that point.

Frame 4000 corresponds to 20 ps because the time step was 1 fs and the sample
frequency 5: 4000*5*1 fs = 20000 fs = 20 ps.

.. rst-class:: steps

  \
   | **MD Properties → Autocorrelation function**
   | Change the starting step from ``1`` to ``4000`` (this will discard the first 20 ps of the simulation)
   | **Property → Pressure Tensor**
   | **Vector elements**: ``4 5 6`` (these are the off-diagonal elements :math:`P_{yz}`, :math:`P_{xz}`, and :math:`P_{xy}`)
   | **Max ACF Step**: ``3000`` (corresponding to a maximum correlation time of 15 ps)
   | Press the button **Generate ACF**
   | Close the Autocorrelation Function window


This brings up several graphs in AMSmovie. The bottom graph contains the
integral of the pressure tensor autocorrelation function as a function of upper
integrand limit:

.. math::

    y(t) = \int_0^{t}<P_{\alpha\beta}(0)P_{\alpha\beta}(\tau)> d\tau

In the ideal case this graph will converge to a constant
value as t → :math:`\infty`. This usually requires very long simulations. Your
graph may look different.

In this case, the integral seems to converge to a value of 1.35 × 10\ :sup:`-9` hartree\ :sup:`2` fs bohr\ :sup:`-6`.

To calculate the viscosity, we also need the volume :math:`V = 13.333^3 = 2370` Å\ :sup:`3`.

Converting everything to SI units (where 1 hartree bohr\ :sup:`-3` = 2.942 × 10\ :sup:`13` Pa), we get

.. math::

    \eta = \frac{2370 \times 10^{-30}}{1.38 \times 10^{-23} \times 298} \times 1.35 \times 10^{-9} \times 2.942 \times 10^{13} \times 2.942 \times 10^{13} \times 10^{-15} 

.. math::
    
    \eta = 0.00067 \rm{\ Pa\ s} = 0.67 \rm{\ mPa\ s}

The experimental room-temperature viscosity of benzene is about 0.5 mPa s.

Important considerations
=============================

* The simulation needs to be **well equilibrated**

* The **viscosity is often sensitive to the supercell size**. Use a larger supercell with more benzene molecules for a better value.

* The **integral must converge in the long time-limit**. You may want to increase the maximum correlation time (above given as 3000 frames or 15 ps) to a larger value, and increase the simulation time.

* The biggest contribution to the integral comes at short correlation times. It is therefore necessary **set the Sample frequency to a small number**, ideally even smaller than the 5 fs we used here.


Python script
=======================

Both the MD simulation and the calculation of the autocorrelation function integral can be scripted with our PLAMS scripting framework. In the example script :download:`viscosity.py <../downloads/viscosity.py>` the viscosity will be calculated using the same routine described above, using the :download:`benzene_bulk_16.xyz <../downloads/benzene_bulk_16.xyz>` file. It will then output a table of the temperatures and viscosities. The results below were obtained using 200,000 steps and a sampling frequency of 2 steps. The last 40% of the temperature and ACF were used in calculating the viscosities. 
Example output::

  All simulations are now done
  Temperature (K) | Viscosity (mPa s)
  100.03          | 1.75110
  149.55          | 0.53409
  199.77          | 0.31666
  250.30          | 0.89774
  297.80          | 0.36593
  350.04          | 0.37296
  400.27          | 0.99588
  451.20          | 0.59105

Of course, the quality and accuracy of the results depend on the settings and system you provide. Also note that the density should in principle also depend on the temperature however that is ignored in this example.


