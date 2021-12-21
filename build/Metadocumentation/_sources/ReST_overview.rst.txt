reST cheat sheet
################

.. seealso::

  This document is by no means an exhaustive guide to **Sphinx** and **reStructuredText (reST)**. Additional resources:

  * `Our wiki page <https://wiki.scm.com/index.php/Editing_User_Documentation>`__ 
  * `Sphinx website <https://www.sphinx-doc.org>`__ 
  * `reStructuredText primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__ (a lot of stuff in this document is taken from here)
  * `reStructuredText doc <http://docutils.sourceforge.net/rst.html>`__
  * `super useful page <https://rest-sphinx-memo.readthedocs.io/en/latest/>`__ (or `<https://github.com/marczz/rest-sphinx-memo/blob/master/source/ReST.rst>`__)

Our documentation is a **collection of several Sphinx projects** (ADF, AMS, Band, Tutorials,...). All the projects import ``global_conf.py`` from the local ``conf.py``.


External links
==============

.. important::

   For cross-links between different SCM documentation projects, see :ref:`inter-projects_links`. 

This ```Search engine <https://duckduckgo.com>`__`` creates an external link like this: `Search engine <https://duckduckgo.com>`__

This ```<https://duckduckgo.com>`__`` creates an external link like this: `<https://duckduckgo.com>`__


Internal links
==============

For internal links standard reST **labels** are used. The are two ways of doing this:

* If you place a label directly before a section title, you can reference to it with ``:ref:`label-name```. For example.

  .. code-block:: rst

    .. _label-name:

    Section to cross-reference
    --------------------------
 
    This is the text of the section.

    It refers to the section itself, see :ref:`label-name`.

* Labels that aren’t placed before a section title can still be referenced, but you must give the link an explicit title, using this syntax 

  .. code-block:: rst

    .. _label-name:

    Some random text, see :ref:`link title <label-name>`.


.. _inter-projects_links:

Inter-project links
===================

For links from one documentation project to another one (e.g. links from the AMS manual to the Tutorials or vice versa) use **external links with relative paths**. To make a link from page_A (in project_A) to page_B (in project_B) you should use the relative path from page_A to page_B. 

For example, to make a link from this page to a page in the `Tutorials <../Tutorials/StructureAndReactivity/ZN-PES-Scan_TST.html>`__:

.. code-block:: rst

  Link to a page in the Tutorials: `AMS Tutorial <../Tutorials/AMS/ZN-PES-Scan_TST.html>`__

Do **not** use an absolute link starting with ``www.SCM.com/doc`` for inter-project links.


Citations / References
======================

For citations we use footnotes.

**Example:**

.. code-block:: rst

  Cite a paper here [#ref1]_ and another one here [#ref2]_.

  .. Then, at the bottom of the page: 

  .. [#ref1] \G. te Velde, F.M. Bickelhaupt, E.J. Baerends, C. Fonseca Guerra, S.J.A. van Gisbergen, J.G. Snijders, T. Ziegler, *Chemistry with ADF*, `Journal of Computational Chemistry 22, 931 (2001) <https://doi.org/10.1002/jcc.1056>`__ 

  .. [#ref2] \E. J. Baerends and P. Ros, *Evaluation of the LCAO Hartree-Fock-Slater method: Applications to transition-metal complexes*, `International Journal of Quantum Chemistry 14, S12, 169 (1978) <https://doi.org/10.1002/qua.560140814>`__  

**Result:** Cite a paper here [#ref1]_ and another one here [#ref2]_.

.. note::
  In the example above, the ``\`` before ``G. te Velde`` at the beginning of the line is to prevent sphinx from interpreting ``G.`` that as an enumerated list!


Equations
=========

For equation we use MathJax. The syntax is essentially the same as for latex equations.

**Example:**

.. code-block:: rst

  The current :math:`I(V)` can be computed using the following equation:

  .. math:: 
     
    I(V) = \frac{2e}{h} \int_{-\infty}^\infty T(E,V) f(E) dE

**Result:**

The current :math:`I(V)` can be computed using the following equation:

.. math:: 
   
  I(V) = \frac{2e}{h} \int_{-\infty}^\infty T(E,V) f(E) dE


Images
======

For images we use the ``figure`` directive. Simple usage:

.. code-block:: rst

  .. figure:: Images/NEGF.png

**Example** (with some options):

.. code-block:: rst

  .. figure:: Images/NEGF.png
    :width: 80%
    :align: center

    Optionally, you can put your caption here.

**Result:**

.. figure:: Images/NEGF.png
  :width: 80%
  :align: center

  Optionally, you can put your caption here.


.. _download:

File download
=============

**Example:**

.. code-block:: rst

  Download the file :download:`link-title <downloads/file.txt>`

**Result:** Download the file :download:`link-title <downloads/file.txt>` 


Videos
======

This is how you can embed videos:

.. code-block:: rst

  .. raw:: html

    <center>
      <video controls src="../_downloads/burning_isooctane.mp4"></video>
    </center>

  You can download the movie :download:`here </downloads/burning_isooctane.mp4>`.

You **must** include a have a :ref:`download link <download>` to the video file, otherwise the video will not be copied over when the documentation is built. (also, note that there is an underscore in the video controls link)


Index
=====

Before section titles you generally want to use many index directives with plausible alternative names. 

**Example:**

.. code-block:: rst

  .. index:: Excitations
  .. index:: TDDFT
  .. index:: UV/Vis
  .. index:: Other reasonable names people might search for...

  Excitations with TDDFT
  ----------------------


Tables
======

For tables I advise using ``csv-table`` (they are much easier to maintain than ``grid tables`` and ``Simple tables``). See also `<http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables>`__. Example:

**Example:**

.. code-block:: rst

  .. csv-table:: Optional title
     :header: "Animal", "Furry", "Pettability [a.u.]"

     "Cat", "Yes", 9
     "Dog", "Yes", 9
     "Naked mole rat", "No",  5

**Result:**

.. csv-table:: Optional title
   :header: "Animal", "Furry", "Pettability [a.u.]"

   "Cat", "Yes", 9.5
   "Dog", "Yes", 9.8
   "Naked mole rat", "No",  2.7


Code and input snippets
=======================

For snippets of code or run-scripts use the ``code-block`` directive. 

**Example:**

.. code-block:: rst
  
  Some python code:

  .. code-block:: python
    :emphasize-lines: 3,4

    def some_function():
      interesting = False
      print 'This line is highlighted.'
      print 'This one as well...'
      print '...but not this one.'

  Some ADF input block example:

  .. code-block:: none
    
    Excitations
      Lowest 5
      FullKernel
      OnlySing
    End

**Result:**

Some python code:

.. code-block:: python
  :emphasize-lines: 3,4

  def some_function():
    interesting = False
    print 'This line is highlighted.'
    print 'This one as well...'
    print '...but not this one.'

Some ADF input block example:

.. code-block:: none
  
  Excitations
    Lowest 5
    FullKernel
    OnlySing
  End


.. [#ref1] \G. te Velde, F.M. Bickelhaupt, E.J. Baerends, C. Fonseca Guerra, S.J.A. van Gisbergen, J.G. Snijders, T. Ziegler, *Chemistry with ADF*, `Journal of Computational Chemistry 22, 931 (2001) <https://doi.org/10.1002/jcc.1056>`__ 

.. [#ref2] \E. J. Baerends and P. Ros, *Evaluation of the LCAO Hartree-Fock-Slater method: Applications to transition-metal complexes*, `International Journal of Quantum Chemistry 14, S12, 169 (1978) <https://doi.org/10.1002/qua.560140814>`__  
