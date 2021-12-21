General remarks on input structure and parsing
----------------------------------------------

- Most keys are optionals. Defaults values will be used for keys that are not specified in the input

- Keys/blocks can either be *unique* (*i.e.* they can appear in the input only once) or *non-unique*. (i.e. they can appear multiple times in the input)

- The order in which keys or blocks are specified in the input does not matter. Possible exceptions to this rule are a) the content of non-standard blocks b) some non-unique keys/blocks)

- Comments in the input file start with one of the following characters: ``#``, ``!``, ``::``::

   # this is a comment
   ! this is also a comment
   :: yet another comment

- Empty lines are ignored

- The input parsing is **case insensitive** (except for string values)::

   # this:
   UseSymmetry false
   # is equivalent to this:
   USESYMMETRY FALSE

- Indentation does not matter and multiple spaces are treaded as a single space (except for string values)::

   # this:
        UseSymmetry     false
   # is equivalent to this:
   UseSymmetry false


Keys
----

Key-value pairs have the following structure::

   KeyName Value


Possible types of keys:

bool key
   The value is a single Boolean (logical) value. The value can be ``True`` (equivalently ``Yes``) or ``False`` (equivalently ``No``.). Not specifying any value is equivalent to specifying ``True``. Example::

      KeyName Yes

integer key
   The value is a single integer number. Example::

      KeyName 3

float key
   The value is a single float number. For scientific notation, the E-notation is used (e.g. :math:`-2.5 \times 10^{-3}` can be expressed as ``-2.5E-3``). The decimal separator should be a dot (``.``), and **not** a comma (``,``). Example::

      KeyName -2.5E-3

   Note that fractions (of integers) can also be used::

      KeyName 1/3    (equivalent to: 0.33333333333...)

string key
   The value is a string, which can include white spaces. Only ASCII characters are allowed. Example::

      KeyName Lorem ipsum dolor sit amet

multiple_choice key
   The value should be a single word among the list options for that key (the options are listed in the documentation of the key). Example::

      KeyName SomeOption

.. _ranges_in_input:

integer_list key
   The value is list of integer numbers. Example::

      KeyName 1 6 0 9 -10

   Note that one can also specify ranges of integers by specifying the interval and (optionally) the step size separated by colons::

      KeyName 1:5       (equivalent to: 1 2 3 4 5)
      KeyName 2:10:2    (equivalent to: 2 4 6 8 10)
      KeyName 20:10:-2  (equivalent to: 20 18 16 14 12 10)

   Note also that ranges can be freely combined with individual numbers::

      KeyName 1:5 10 20  (equivalent to: 1 2 3 4 5 10 20)

float_list key
   The value is list of float numbers. The convention for float numbers is the same as for Float keys. Example::

      KeyName 0.1 1.0E-2 1.3

   Float lists can also be specified as a range with equidistant points, by specifying the interval's boundaries (inclusive) as well as the number of desired subintervals separated by colons::

      KeyName 1.0:1.5:5  (equivalent to: 1.0 1.1 1.2 1.3 1.4 1.5)

   Range specifications can be freely combined with each other and single numbers::

      KeyName 0.0 1.0:1.5:5 2.0:3.0:10


Blocks
------

Blocks give a hierarchical structure to the input, grouping together related keys (and possibly sub-blocks).
In the input, blocks generally span multiple lines, and have the following structure::

   BlockName
      KeyName1 value1
      KeyName2 value2
      ...
   End

**Headers**

For some blocks it is possible (or necessary) to specify a *header* next to the block name::

   BlockName someHeader
      KeyName1 value1
      KeyName2 value2
      ...
   End

**Compact notation**

It is possible to specify multiple key-value pairs of a block on a single line using the following notation::

   # This:
   BlockName KeyName1=value1 KeyName2=value2

   # is equivalent to this:
   BlockName
      KeyName1 value1
      KeyName2 value2
   End

Notes on compact notation:

- The compact notation cannot be used for blocks with headers.
- Spaces (blanks) between the key, the equal sign and the value are ignored. However, if a value itself needs to contain spaces (e.g. because it is a list, or a number followed by a unit), the entire value must be put in either single or double quotes::

      # This is OK:
      BlockName Key1=value Key2 = "5.6 [eV]" Key3='5 7 3 2'
      # ... and equivalent to:
      BlockName
         Key1  value
         Key2  5.6 [eV]
         Key3  5 7 3 2
      End

      # This is NOT OK:
      BlockName Key1=value Key2 = 5.6 [eV] Key3=5 7 3 2


**Non-standard Blocks**

A special type of block is the *non-standard block*. These blocks are used for parts of the input that do not follow the usual key-value paradigm.

A notable example of a non-standard block is the ``Atoms`` block (in which the atomic coordinates and atom types are defined).


Including an external file
--------------------------

You can include an external ASCII file in the input with the ``@include``
directive::

   @include FileName.in
   @include "file name with spaces.in"

The file name should include the path, either absolute or relative to the
run-directory.  The content of the file is included in the input at the point
where the ``@include`` directive occurs. The ``@include`` directive may occur
any number of times in the input.

The ``@include`` feature makes it easy to pack your preferred settings in one
file and use them in every run with minimum input-typing effort.
