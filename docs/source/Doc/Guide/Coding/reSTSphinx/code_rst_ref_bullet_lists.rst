.. _code-rst-ref-bullet-lists:

============
Bullet Lists
============

A text block which begins with a ``*``, ``+`` or ``-``, followed by a whitespace, is a bullet list item.

* Each item of a list should start with a ``*``, ``+`` or ``-`` and a space after it.
* Lists should have an empty line before and after
* Sublists should also have an empty line before and after
* Indent sublists with 3 spaces

.. note:: 

   Although the standard syntax states that only a whitespace is required after the bullet symbol, 
   we do recommend using two spaces instead to keep the raw text more tidy as the default indent is set to three spaces.

.. important:: 

   A blank line is required before the first item and after the last, but is optional between items.

Example
=======

.. code-block:: rst

   *  item 1
   *  item 2 is a longer text with line breaks. We can format and
      indent like this
   *  item 3

      *  subitem 3.1
      *  subitem 3.2

   *  item 4


**How it looks**

*  item 1
*  item 2 is a longer text with line breaks. We can format and
   indent like this
*  item 3

   *  subitem 3.1
   *  subitem 3.2

*  item 4

----

Wrong Example
=============

.. error:: 

   The extra lines for the sublist are missing.

.. code-block:: rst

   *  item 1
   *  item 2
   *  item 3
      *  subitem 3.1
      *  subitem 3.2
   *  item 4


**How it looks**

*  item 1
*  item 2
*  item 3
   *  subitem 3.1
   *  subitem 3.2
*  item 4
