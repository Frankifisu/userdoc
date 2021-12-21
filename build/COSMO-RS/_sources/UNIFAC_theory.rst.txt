.. index:: UNIFAC
.. index:: theory UNIFAC

UNIFAC theory
*************

Below some of the UNIFAC method is explained, but a more complete description can be found in Ref. [#ref1]_.

The UNIFAC method is an activity coefficient model derived from the UNIQUAC model.  Both UNIFAC and UNIQUAC are thermodynamic models based on local composition theory, which holds that the local environment of a molecule in solution can be used to calculate the probabilities of molecular configurations in the bulk solution.  While UNIQUAC requires parameters for every compound in solution and interaction parameters for every pair of compounds, UNIFAC estimates these parameters as functions of the number of occurrences of various molecular substructures, or groups, in a molecule.  This means that UNIFAC can be applied to estimate activity coefficients for arbitrary systems, so long as every group is defined and an interaction parameter exists for every pair of groups in the composition.  

The UNIFAC method calculates the activity coefficient as a function of two contributions: (1) the residual contribution, meant to account for the interactions of groups in the mixture; and (2) the combinatorial contribution, meant to account for entropic effects due to differences in molecular shape.  Using these two components, the activity coefficient for each compound *i* is calculated as follows:

.. math::
    \ln\gamma_i = \ln\gamma_i^R + \ln\gamma_i^C

where :math:`\ln\gamma_i^R` corresponds to the residual contribution to the activity coefficient and :math:`\ln\gamma_i^C` to the combinatorial contribution.

Residual term
=============

In the UNIFAC method, we first define :math:`n_i^k` to be the number of times group *k* occurs in molecule *i*.  Using this with the mole fraction :math:`x_i` of each compound *i*, we calculate the group mole fraction, :math:`X_k`, or the amount of groups of type *k* as a fraction of the total groups:

.. math::
    X_k = \frac{\sum\limits_i x_i n_i^k}{\sum\limits_i\sum\limits_j x_i n_i^j }

We use the :math:`X_k` values to then determine the relative surface area each group represents in the mixture.  This is done by taking an average of the :math:`X_k` values weighted with the surface area contributions, :math:`Q_k`, of each group *k*.  We define the result as the area fraction of group *k*:

.. math::
    \Theta_k = \frac{ X_k Q_k }{\sum\limits_m x_m Q_m }

the surface area and volume of a molecule is estimated as a linear function of the number and types of groups that are present.  Each group *k* occurs a :math:`n_i^k` times in molecule *i*.  

Additionally, between every pair of groups, *k* and *m* an interaction energy is defined as :math:`a_{km}`.  This energy is given in Kelvin and is used to calculate the group interaction paramter :math:`\Psi_{km}`:

.. math::
    \Psi_{km} = \exp\left(\frac{-a_{km}}{T}\right)

where *T* is the temperature of the system in Kelvin.  Note that :math:`\Psi_{km} \neq \Psi_{mk}`.

These parameters are then used to calculate the residual contribution to the activity coefficient for each group *k*:

.. math::
    \ln\Gamma_k = Q_k \left( 1 - \ln\sum\limits_m\Theta_m\Psi_{mk} - \sum\limits_m\frac{\Theta_m\Psi_{km}}{\sum\limits_n \Theta_n\Psi_{nm}} \right)

Additionally, one must also calculate :math:`\ln\Gamma_k^{(i)}`, which follows the same procedure as above for each compound assuming it exists in a pure form, i.e., :math:`x_i=1`.  Then, the residual contribution to the activity coefficient is calculated as follows:

.. math::
    \ln\gamma_i^R = \sum\limits_k n_i^k \left( \ln\Gamma_k - \ln\Gamma_k^{(i)} \right)


Combinatorial term
==================

To estimate the combinatorial contribution to the activity coefficient, first the surface area, :math:`q_i`, and volume, :math:`r_i`, of molecule *i* are estimated as follows:

.. math::
    q_i = \sum_i Q_k n_i^k \qquad r_i = \sum_i R_k n_i^k

where :math:`Q_k` is the surface area contribution of group *k* and :math:`R_k` is the volume contribution.  Using these parameters we can define the relative surface area and relative volume (also called fractional surface area and fractional volume) corresponding to molecule *i* in solution.  This is simply an average of the surface areas/volumes of each compound weighted by the mole fraction of that compound in solution:

.. math::
    \theta_i = \frac{ x_i q_i }{\sum\limits_j x_j q_j } \qquad \phi_i = \frac{ x_i r_i }{\sum\limits_j x_j r_j }

Additionally, we calculate the parameter :math:`L_i`:

.. math::
    L_i = \frac{ z }{2} (r_i-q_i)-(r_i-1)

where *z* is the coordination number and is usually taken to be equal to 10.  All of these parameters are then used to calculate the combinatorial contribution to the activity coefficient:

.. math::
    \ln\gamma_i^C = \ln\frac{\phi_i}{x_i} + \frac{z}{2} q_i \ln \frac{\theta_i}{\phi_i} + L_i - \frac{\phi_i}{x_i} \sum\limits_j x_j L_j


.. only:: html

  .. rubric:: References

.. [#ref1] A.\  Fredenslund, R.L. Jones, and J.M. Prausnitz, *Group-contribution estimation of activity coefficients in nonideal liquid mixtures*, `AIChE Journal 21, 1086 (1975) <https://doi.org/10.1002/aic.690210607>`__
