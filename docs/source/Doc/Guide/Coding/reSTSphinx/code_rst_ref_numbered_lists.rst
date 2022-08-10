.. _code-rst-ref-numbered-lists:

==============
Numbered Lists
==============

A text block which begins with a ``number.`` or ``#.`` or ``-``, followed by a whitespace, is a numbered list item.

* Each item of a list should start with a ``number.``, ``#.`` and a space after it.
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

**How it looks**

#. item1
#. item2
#. item3


.. code-block:: rst
   :caption: Manual numbering

   3. item1
   4. item2
   5. item3
   #. This item is auto-enumerated

**How it looks**

3. item1
4. item2
5. item3
#. This item is auto-enumerated

