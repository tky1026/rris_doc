.. _code-rst-ref-numbered-lists:

==============
Numbered Lists
==============

A text block which begins with a ``number.``, ``letters.`` or ``#.``, followed by a whitespace, is a numbered (enumerated) list item.

* Each item of a list should start with a ``number``, ``letter``, 
  ``#``, followed by a period ``.``, right bracket ``)`` or surrounded by brackets ``( )``, 
  and a space after it.
* Lists should have an empty line before and after
* Sublists should also have an empty line before and after
* Indent sublists with 3 spaces
* Use ``#.`` for automatic numbering

Example
=======

.. code-block:: rst
   :caption: Automatic numbering

   #. item1
   #. item2
   #. item3

#. item1
#. item2
#. item3


.. code-block:: rst
   :caption: Manual numbering

   3. item1
   4. item2
   5. item3
   #. This item is auto-enumerated

1. item1
2. item2
3. item3
#. This item is auto-enumerated


.. code-block:: rst
   :caption: Letters numbering

   A. upper-case letters
      and it goes over many lines

   #. This item is auto-enumerated

   j. lower-case letters

      1) with a sub-list starting at a different number
      2) make sure the numbers are in the correct sequence though!

   #. This item is auto-enumerated

A. upper-case letters
   and it goes over many lines

#. This item is auto-enumerated

j. lower-case letters

   3) with a sub-list starting at a different number
   4) make sure the numbers are in the correct sequence though!

#. This item is auto-enumerated

