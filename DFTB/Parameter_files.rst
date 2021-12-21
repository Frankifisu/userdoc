Parameterizations
-----------------

.. _metainfo.yaml:

Parameter meta-info
###################

There is a file named ``metainfo.yaml`` in each resources directory (see :ref:`ResourcesDir<dftb-key-ResourcesDir>`), for example *DFTB.org/3ob-3-1/metainfo.yaml*, which contains information about the capabilities of a parameter set.
The file is in accordance with the  `YAML <http://www.yaml.org>`_ syntax convention.
In older versions of AMS this file was optional and its format was slightly different.
Starting with the 2017 release of ADF/AMS, the ``metainfo.yaml`` file is required to use a parameter set.

The following entries ``metainfo.yaml`` specify the capabilities of the parameter set:

``supports: [dftb0, scc-dftb, dftb3, gfn-xtb]``
  A comma-separated list of model Hamiltonians for which the parameter set can be used.
  If the parameter set only supports a single model Hamiltonian, the enclosing ``[ ]`` can be dropped.
  This entry is mandatory. Without it, DFTB will refuse to use the parameter set.

``format: txt|txtq``
  Specifies which format is used for the Slater-Koster files of the parameter set.
  Use ``txt`` for normal text files with extension ``.skf``.
  ``txtq`` is used for the  encrypted Slater-Koster files from the QUASINANO parameter sets.
  Encrypted Slater-Koster files have the extension ``.ske``.
  If the ``format`` entry is not there, normal (unencrypted) text files are assumed.
  Note that this entry is only relevant for Slater-Koster based DFTB and not used by the extended tight-binding model Hamiltonians.

.. _repulsive_potential_metainfo:

``repulsion: no|partial|yes``
  Specifies whether the parameter set has repulsive potentials for all pairs of elements.
  Parameter sets that do not have repulsive potentials (e.g. QUASINANO2013.1) can not be used in geometry optimizations, molecular dynamics or frequency calculations.
  However, they can still be used in single point calculations, e.g. for UV/Vis absorption spectra of molecules or band structures of solids.
  Some parameter sets (e.g. DFTB.org/halorg-0-1) have most, *but not quite all* repulsive potentials.
  If ``repulsion`` is set to ``partial``, DFTB will allow calculations with run-types normally requiring repulsive potentials and will only print a warning about which pairs are missing.
  It is then the user's responsibility to ensure that element pairs for which the repulsion is missing do not get too close during the calculation.
  If the ``repulsion`` entry is not found, DFTB will assume that there are repulsive potentials for all element pairs.

``spin_polarization: no|yes``
  Whether the parameter set supports unrestricted calculations.
  The default value is ``no``.

``orbital_dependence: [ noldep, ldep ]``
  Whether the parameter set supports an atomic and/or shell-resolved SCC cycle.
  If only one of the two is supported, the enclosing ``[ ]`` can be dropped and the ``default_orbital_dependence`` entry (see below) does not need to be specified.
  If the ``orbital_dependence`` key is not found, DFTB assumes that the parameter set only supports atomic SCC cycles.

``default_orbital_dependence: noldep|ldep``
  The default mode for the SCC cycle.

``dispersion: [ uff, ulg, d2, d3-bj, d4 ]``
  A comma-separated list of London dispersion corrections supported by the parameter set.
  If only one method is supported, the enclosing ``[ ]`` can be dropped and the ``default_dispersion`` entry (see below) does not need to be specified.

``default_dispersion: uff|ulg|d2|d3-bj|d4``
  The default dispersion method to be used if the user enables dispersion but does not specify a method explicitly.
  If the ``default_dispersion`` entry is not found and more than one method is supported according to ``dispersion`` entry, **no** dispersion correction will be used by default.
  The user then has to select a dispersion method explicitly in the input file.

In addition to specifying the parameter set's capabilities, the ``metainfo.yaml`` file should also contain references to the scientific publication describing the parameter set:

.. code:: yaml

   url: http://www.scm.com

   reference: |
     M. Wahiduzzaman, A. F. Oliveira, P. Philipsen, L. Zhechkov, E. van Lenthe, H. Witek, T. Heine
     "DFTB Parameters for the Periodic Table: Part 1, Electronic Structure",
     J. Chem. Theory Comput., 9, 2013, 4006-4017, DOI: 10.1021/ct4004959

   short_reference: J. Chem. Theory Comput., 9, 2013, 4006-4017

All these entries are optional and at the moment only the ``reference`` entry is read by DFTB (and reproduced verbatim in its output).
Note that the pipe symbol ``|`` is necessary to start a multiline entry (with preserved line breaks) and that the following lines have to be indented by at least one space.


.. _dftb_parameters:

Slater-Koster based DFTB
########################

The most popular parameter sets for Slater-Koster based DFTB are :ref:`distributed with the AMS package<available_parameter_sets>`.
Other parameter sets can easily be :ref:`added<resource_dir_files>`.

Often parameter files are designed for a specific purpose, which may be different from your application, and therefore may give not the desired accuracy.
Note that parameter files coming from different parameter sets are in general not compatible with each other and should not be mixed.

Additional licenses may be required to use some of the distributed parameter sets.
Please contact us at license@scm.com for details.


.. _available_parameter_sets:

Available parameter sets
************************

DFTB.org
========

The DFTB implementation shipped by SCM provides the most up-to-date parameter sets available on the DFTB.org website.
The following sets are currently shipped:

+ 3ob-3-1 (Br, C, Ca, Cl, F, H, I, K, Mg, N, Na, O, P, S, Zn): general purpose set for the DFTB3 method
+ mio-1-1 (H, C, N, O, S, P): for bio and organic molecules with SCC-DFTB
+ pbc-0-3 (Si, F, O, N, C, H, Fe): for solid and surfaces
+ matsci-0-3 (Al, Si, Cu, Na, Ti, Ba): for various compounds in material science

In addition, we ship the following specific purpose parameter sets:

+ 3ob-freq: modified 3ob parameters for a better description of vibrational frequencies
+ 3ob-hhmod: modified H-H for 3ob (for a better description of H2)
+ 3ob-nhmod: modified N-H for 3ob (improves sp3-N proton affinities)
+ 3ob-ophyd: modified O-P for 3ob (improves description of pentavalent phosphorus species)
+ auorg (Au + mio): for gold-thiolate compounds
+ borg (B, H): boron systems (solids and molecules)
+ chalc-0-1 (As + mio): for chalcogenide glasses
+ halorg (F, Cl, Br, I + mio): for halogens
+ hyb-0-1 (Ag, Ga, As, Si + mio): for organic and inorganic hybrid systems
+ magsil (Mg, Si, O, H, Mg): for chrisotyle nanotubes
+ miomod-hh: contains a modified parameter set for H2
+ miomod-nh: contains a modified parameter set fo N-H to improve N-H binding energies
+ siband (Si, O, H): electronic parameters for accurate silicon and silicon dioxide band structures
+ tiorg-0-1 (Ti + mio): for Ti bulk, TiO2 bulk, TiO2 surfaces, and TiO2 with organic molecules
+ trans3d-0-1 (Sc, Ti, Fe, Co, Ni + mio): transition metal elements for biological systems
+ znorg-0-1 (Zn + mio): for Zn bulk, ZnO bulk, ZnO surfaces, and ZnO with organic molecules

We recommend to visit the `DFTB.org <http://www.dftb.org>`_ web site for more detailed information about each set.
We are committed to shipping all DFTB.org parameter sets in their latest version.
If you miss one of the DFTB.org parameter sets in our distribution, please contact us at support@scm.com.
Please note that our implementation of DFTB currently does not support parameter sets containing f-functions, such as the "rare" set.

QUASINANO
=========

The :ref:`QUASINANO2013.1 <QUASINANO2013.1>` set of DFTB parameter files available in the AMS package is designed by Mohammad Wahiduzzaman et al. contains parameters for a large part of the periodic table (no f-elements).
Note that the QUASINANO2013.1 set only contains the electronic part of the interaction, so that only the spectrum for a given geometry can be calculated, but no total energy, and thus also no forces.
These parameters can be used in TD-DFTB calculations, for example.

The :ref:`QUASINANO2015 <QUASINANO2015>` parameter set extends the QUASINANO2013.1 parameter set, and includes terms that are needed to compute the total energy and its gradient.

Dresden
=======

The so called Dresden set of DFTB parameter files available in the AMS package were designed by J. Frenzel, A.F. Oliveira, N. Jardillier, T. Heine, and G. Seifert, mainly at the Technische Universität in Dresden, Germany, see also some :ref:`additional information about the generation of these parameter files<DRESDEN>`.
These parameter files are kept in the directory $AMSHOME/atomicdata/DFTB/Dresden.


.. _resource_dir_files:

Files in the resources directory
********************************

This section contains a technical description of all the files and their formats which together constitute a DFTB parameter set.
The parameter sets :ref:`distributed with the AMS package<available_parameter_sets>` are ready to be used out-of-the box, and no knowledge about their format should be necessary to run DFTB calculations.
However, users who want to use their own DFTB parameters with our implementation, will need to package them in a way that is understood by it.

DFTB parameter sets in the AMS package have up to four components: The :ref:`Slater-Koster files <slater_koster_files>`, the :ref:`metainfo.yaml file <metainfo.yaml>` and the optionally some :ref:`additional .yaml files <additional_yaml_files>` as well as :ref:`binary .rkf files containing the basis functions <basisfunctions_in_rkf_file>`.


.. _slater_koster_files:

Slater-Koster files
===================

Most of the data constituting a DFTB parameter set is contained in the so called Slater-Koster files.
These are typically text files with the file extension ``.skf``.
For legal reasons, some parameter sets that are shipped with AMS the Slater-Koster files are encrypted though, in which case their file extension is ``.ske``.

There is generally a Slater-Koster file per **pair of elements** supported by the parameter set, e.g. for a set supporting the four elements C,H,O,N there will be 16 Slater-Koster files in total.
The Slater-Koster file names contain the symbols of the elements, e.g. ``C-H.skf``, ``H-O.skf`` and ``C-C.skf``.
Note that files for both element orders, e.g. ``C-H.skf`` and ``H-C.skf``, are needed and differ in general.
The Slater-Koster files contain the matrix elements of the Hamiltonian operator and the overlap between between basis functions centered on two atoms, tabulated for different distances.
They also contain a description of a repulsive potential between the two atoms.
Furthermore the one element Slater-Koster files (like ``H-H.skf`` and ``C-C.skf``) contain some information about the individual atom, e.g. orbital energies of the atomic orbitals.
A `detailed description <http://www.dftb.org/fileadmin/DFTB/public/misc/slakoformat.pdf>`_ of the Slater-Koster file format can be found at `DFTB.org <http://www.dftb.org>`_.


.. _additional_yaml_files:

Additional .yaml files
======================

The `Slater-Koster file format <http://www.dftb.org/fileadmin/DFTB/public/misc/slakoformat.pdf>`_ is relatively old and very inflexible.
Over the years extensions of the DFTB method (e.g. spin-polarization, DFTB3, dispersion corrections) have been developed that require parameters which do not have a place in the Slater-Koster files.
In the AMS implementation of DFTB, these parameters are stored in additional ``.yaml`` files in the resources directory of the parameter set:
The ``additional_parameters.yaml`` file as well as per element ``.yaml`` files, e.g. ``H.yaml`` and ``C.yaml``.

The ``additional_parameters.yaml`` file contains anything that applies to the entire parameter set and does not depend on the individual elements.
At the moment this is:

``grimme_d3bj_params: s6 s8 a1 a2``
  The fitting parameters for Grimme's D3-BJ dispersion correction.
  This entry is mandatory if the ``metainfo.yaml`` file lists D3-BJ as a supported dispersion correction method.

``grimme_d4_params: s6 s8 a1 a2``
  The fitting parameters for Grimme's D4 dispersion correction.
  This entry is mandatory if the ``metainfo.yaml`` file lists D4 as a supported dispersion correction method.

``zeta_Hcorr: zeta``
  A single number ``zeta`` used in the HX-damping usually applied in DFTB3 calculations.

The per element ``.yaml`` files may contain the following entries:

``hubbard: U_atom``
  The atomic Hubbard parameter used in a normal, atomic SCC cycle is specified in the element's ``.yaml`` file as the ``hubbard`` entry.
  It is quite surprising that such a commonly used parameter does not have its place in the Slater-Koster files, which only hold the shell-dependent Hubbard parameters.
  For atomic SCC cycles it is common practice to use the Hubbard parameter of the s-shell as the atomic Hubbard parameter, even though the two values are not strictly related.
  For consistency with other DFTB implementations, AMS DFTB will do the same if the atomic Hubbard parameter is not found in the element's ``.yaml`` file.
  However, it will also notify the user about this potentially questionable behavior.

``hubbard_derivative: dUdq``
  The derivative of the the atomic hubbard parameter with respect to the atomic charge.
  This is information is required to perform DFTB3 calculations.

``magnetic_hubbard`` and ``magnetic_hubbard_ldep``
  The magnetic Hubbard parameters (often abbreviated W in the literature).
  These are required for unrestricted calculations and TD-DFTB singlet-triplet excitations.
  Depending on whether the parameter set allows atomic and/or shell resolved SCC cycles, the magnetic Hubbard parameter is given as a single number and/or a small matrix:

  .. code:: yaml

     magnetic_hubbard: W_atom

     magnetic_hubbard_ldep: >
         W_ss  W_sp
         W_ps  W_pp

  The size of the matrix is determined by the number of basis functions on the element. Note that the ``>`` is essential to start a multiline entry (in which line breaks are ignored).



.. _basisfunctions_in_rkf_file:

Basis function information in .rkf files
========================================

Many parameter sets additionally have per element ``.rkf`` files in the resources directory, e.g. ``H.rkf`` and ``C.rkf``.
These binary files, which can be opened in the GUI with KFBrowser, contain information about the basis functions used to calculate the matrix elements in the Slater-Koster files.
While this information is not needed to perform the DFTB calculation itself, it is used by the GUI in order to visualize properties like molecular orbitals or densities in AMSview.


.. _xtb_parameters:

Extended tight-binding (xTB)
############################

The AMS package comes with the GFN1-xTB parameterization of the extended tight-binding Hamiltonian. This is the parameterization published in the original article on GFN1-xTB, which is optimized for accurate geometries, frequencies and non-covalent interactions.

In contrast to Slater-Koster based DFTB, the extended tight-binding (xTB) method does not store precalculated matrix elements in Slater-Koster files. Instead there is a parameter file which contains information about the basis functions themselves, which is used to calculate matrix elements at run-time. The entire parameterization of GFN1-xTB is stored in simple text files found in ``$AMSHOME/atomicdata/DFTB/GFN1-xTB``. Expert users can copy this directory, modify the parameterization to their needs, and use the :ref:`ResourcesDir<dftb-key-ResourcesDir>` keyword to load their modified parameterization.

``elements.xtbpar``
  Contains most the element specific parameters, e.g. the Hubbard parameters and their derivative, as well as the parameters used for the repulsive potential.

``basis.xtbpar``
  Contains the definition of the used basis functions. Note that one can add or remove basis functions for an element by adding or deleting lines in this file, as long as there is at most one set of basis functions per angular momentum for each element. For example one can not have two sets of p-functions with a different main quantum number on an atom. (The only exception here is hydrogen, which has both a ``1s`` and ``2s`` function. Hydrogen is treated in a special way in the GFN1-xTB implementation in AMS, which allows this. However, one should not change the hydrogen basis by editing the ``basis.xtbpar`` file. DFTB will refuse to run if this is done.)

``atomic_configurations.xtbpar``
  Contains the electron configurations of the isolated atoms.

``electronegativity.xtbpar``
  Contains the Pauling electronegativities for all elements.

``globals.xtbpar``
  Contains the global parameters of the method, see Table 2 of the GFN1-xTB article.

``metals.xtbpar``
  This file defines which elements are considered metals. (The coordination induced scaling of the atomic energy levels is only used for nonmetals.)
