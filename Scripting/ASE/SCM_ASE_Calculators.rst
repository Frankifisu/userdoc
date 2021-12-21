SCM Calculators in ASE
######################

ASE calculators are implemented for `ADF <../../ADF/index.html>`_, `BAND <../../BAND/index.html>`_, `DFTB <../../DFTB/index.html>`_ and `ReaxFF <../../ReaxFF/index.html>`_.

The options for the programs in the Amsterdam Modeling Suite are  controlled by a single string containing all the information required to set up the respective calculations with :ref:`AMSprep <AMSPREP>`.

Technical Notes
---------------

New Interface Design in ADF2017
```````````````````````````````

ADF2017 ships new, simplified versions of all calculator interfaces to ASE.
The interfaces for setting up these new classes are not compatible to those in earlier versions of the Amsterdam Modeling Suite, but support now all calculation options accepted by :ref:`AMSprep <AMSPREP>`.
Examples on the usage of the new classes are shown below.

Interfaces to Individual Programs
`````````````````````````````````

The ASE calculators for the programs of the Amsterdam Modeling Suite derive from a common parent class (basically an interface to :ref:`AMSprep <AMSPREP>` and :ref:`AMSreport <AMSREPORT>`) and differ from each other only in some program-specific filename internals.
All of SCM's ASE interfaces can therefore be constructed in the following fashion

.. code-block:: python

  myCalculator = CalculatorName(label, amsprep_options, ...)

where ``CalculatorName`` can be any of the following:

:ADF: ``ADFCalculator``
:BAND: ``BANDCalculator``
:DFTB: ``DFTBCalculator``
:ReaxFF: ``ReaxFFCalculator``

Usage and Examples
------------------

Import
``````

Within the ASE repository, the SCM calculator classes are all implemented in `calculators/scm.py` and can be imported via

::

  from ase.calculators.scm import ADFCalculator


Interface Keywords
``````````````````

The constructors of the SCM's calculator classes include the following keywords 

:``label``:

  (default: ``label=None``) calculation tag used for calculation directory and prefix for calculation files: ``label='dir1/abc'`` will create a directory `dir1` and name the calculation files therein as `abc.XXX` while ``label=abc`` will use the current directory and create calculation files as `abc.XXX` in it during runtime.


:``amsprep_options``:

  (default: ``amsprep_options=None``) string containing a sequence of options accepted by :ref:`AMSprep <AMSPREP>`.
  Please consult the :ref:`AMSprep manual <AMSPREP>` for further details.
  Also **note** that the calculator will explicitly add the options ``-j calculationFile``, ``-sym NOSYM``, ``-importangstrom``, and ``-gradientsonly`` to the option list before invoking the amsprep command.


Examples
````````

Single point energy and gradients calculation with ADF

::

  from ase.io.scmio import *
  from ase.calculators.scm import *

  myAtoms = read_scmxyz('myAtoms.xyz')

  myCalculator = ADFCalculator(label='myCalculation', amsprep_options='-t ADF-EG')

  myAtoms.set_calculator(myCalculator)
  print(myAtoms.get_potential_energy())

