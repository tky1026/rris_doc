.. _code-rst-ref-headline-section:

======================
Headlines and Sections
======================

reStructuredText (reST) does not exactly have the notion of "headlines". 
Text is split into "sections" instead. 
Those sections are identified by titles which - in the end - appear as headlines as we know them.

To break longer text up into sections, you use section headers. 
These are a single line of text (one or more words) with adornment: an underline alone, or an underline and an overline together, in dashes ``-----``, equals ``======``, tildes ``~~~~~~`` 
or any of the non-alphanumeric characters ``=`` ``-`` ````` ``:`` ``'`` ``"`` ``~`` ``^`` ``_`` ``*`` ``+`` ``#`` ``<`` ``>`` that you feel comfortable with.

An underline-only adornment is distinct from an overline-and-underline adornment using the same character. 
All sections marked with the same adornment style are deemed to be at the same level. 
In addition, the underline/overline must be at least as long as the title text.

.. note:: 

   reStructuredText heading levels are actually determined by the order (that underlining character) appears in the document, and not just by what character appears under the header.

In order to be consistent throughtout the whole documentation, we use the following conventions: 

#. The title of the whole document is distinct from section titles and may be formatted somewhat differently.

   Use underlining plus overlining with ``===`` for the first section title of a file. 
   The first section title is the "document title" (doctitle) of that file and will appear in the menu. 
   Every ``.rst`` file should have a doctitle

   .. code-block:: rst

      =========
      Doc Title
      =========

#. For the rest of the sections within the document:

   .. code-block:: rst

      1. ======= for the first  level
      2. ------- for the second level
      3. ~~~~~~~ for the third  level
      4. """"""" for the fourth level

#. More levels will be rarely used. 
   For sake of completeness here is the whole hierarchy the automatic conversion tools uses. 
   Stick to this order if more levels are needed:

   .. code-block:: rst

      5. '''''''
      6. ^^^^^^^
      7. #######
      8. *******
      9. $$$$$$$
      10. ``````
      plus: + ; . , _ / % & !  in that order

Example
=======

.. code-block:: rst

   =========
   Doc Title
   =========

   About this document ...

   Topic 1
   =======
   Here we go.

   Subtopic 1.1
   ------------
   Here we dive deeper

   Subsubtopic 1.1.1
   ~~~~~~~~~~~~~~~~~
   And this is even more specific.

   Topic 2
   =======
   ...

Syntax
======

Length of underlines
--------------------

The length of the underlines must at least have the length of the text. It may bet longer, not shorter

**Example 1: This works**

.. code-block:: rst

   Example 1
   =========

**Example 2: This works too**

.. code-block:: rst

   Example 1
   ====================

**Example 3: This does not work**

.. code-block:: rst

   Example 1
   ========

Additional information
======================

* **Docutils**: Read about `sections <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#sections>`__ in the Docutils documentation for the most fundamental description.
* **Sphinx**: explaining `sections <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections>`__ as well.