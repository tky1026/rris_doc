===================
Problems With Lists
===================

If you use lists, make sure there is an empty line before and after the list. If you use lists with sublevels, make sure there is an empty line between the levels and the sublevel items are left-aligned with the parent item text.

The same applies for bullet lists and enumerated lists.

Correct syntax
==============

Example 1: Bullet list
----------------------

.. code-block:: rst

   this is some text

   *  this is a list item
   *  another item

   more text

**How it looks:**

this is some text

*  this is a list item
*  another item

more text

Example 2: List with sublist
----------------------------

.. code-block:: rst

   this is some text

   *  this is a list item

      *  this is a sublevel list item
      *  another item

   this is more text

**How it looks:**

this is some text

*  this is a list item

   *  this is a sublevel list item
   *  another item

this is more text

Wrong syntax
============

.. code-block:: rst

   this is some text
   *  this is a list item
   *  another item
   more text

**How it looks:**

this is some text
*  this is a list item
*  another item
more text


Additional information
======================

* :ref:`code-rst-ref-bullet-lists`
* `Docutils cheat-sheet for reStructuredText: Bullet list <https://docutils.sourceforge.io/docs/user/rst/quickref.html#bullet-lists>`_
* `Docutils cheat-sheet for reStructuredText: Enumerated list <https://docutils.sourceforge.io/docs/user/rst/quickref.html#enumerated-lists>`_