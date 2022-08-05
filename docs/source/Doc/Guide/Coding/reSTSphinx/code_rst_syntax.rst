.. _code-rst-syntax:

==========================
Basic reST & Sphinx Syntax
==========================

The ``.rst`` files are written in reStructuredText (reST) format. 
This page list out some basic common syntax to write in reST format. 
For more details, refer to :ref:`code-rst-ref`.

Paragraphs
==========

New paragraphs in the output are created by an empty line between two paragraphs in your reST file::

   This is a paragraph.

   This is another paragraph.

Comments
========

Comments can be written like this::

   .. this is a comment
   .. with another line

Or like this::

   .. this is a comment
      with another line

Indentation
===========

In reST, the indentation of a block of lines is often important. The exact number of spaces, which are used to indent a block of text, does not matter. 
But what does matter, is that all lines of the block are indented with exactly the same number of spaces.

Hence, in this documentation, We use the convention of **3 spaces** per indenting level (see :ref:`doc-cgl-rest-indent`).

For example:

The following directive inserts an image in the rendered page. All lines beginning with line two must be indented to the same leve. The convention is to use three spaces for one level of indentation.

.. code-block:: rst

   .. image:: someimage.png
      :class: with-border with-shadow
      :alt: Textual alternative to the image

Escape characters
=================

If you want to use a character, which would create some special reST markup, with its normal meaning, you must escape it with a prepended ``\``.

For example asterik symbol ``*`` within the text normally makes text shows up in italics::

   *non-italic*

* *non-italic*

By escaping the special characters ``\*``, the asterik symbol displays as normal text characters::

   \*non-italic\*

* \*non-italic\*