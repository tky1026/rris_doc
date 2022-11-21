===================
Documentation Guide
===================

This manual covers writing documentation. This includes, contributing to this documentation, documentation 
writing guidelines, conventions, and provide links to `GitHub issues`_.

.. _`GitHub issues`: https://github.com/tky1026/rris_doc/issues

----

Building documentation
======================

This documentation is rendered using Sphinx, and hosted on `Read the Docs <https://rris-doc-testing.readthedocs.io/en/latest/>`_.

To build this documentation locally, please follow the instruction below:

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_building.rst

----

Documentation content style
===========================

This section contains conventions, coding guidelines and best practices for contributing to this documentation.
In general, the documentation follows the conventions as described in the following sections.

We mainly uses :term:`reStructuredText(reST) <reST>` markup language for writing docuementation, the file ending of reST files is ``.rst``.
However, :term:`Markdown` format with file ending ``.md`` is acceptable as well.

For syntax and reference of reStructuredText, refer to next section: `reStructuredText & Sphinx`_.

**Table of contents**

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_writing
   Documentation/doc_guide_rst
   Documentation/doc_structure
   Documentation/doc_format
   Documentation/doc_commit

The most important conventions for writing reST files for this documentation are summarized:

#. **Title underlining**

   For consistency throughout the documentation, we defined the :ref:`heading underlining <code-rst-ref-headline-section>` for each section. 
   
   Every ``.rst`` file should have a “document title” (doctitle), always use underlining plus overlining with ``===`` for doctitle.

   .. code-block:: rst

      =========
      Doc Title
      =========

#. **Title capitalization**

   Use :ref:`title case <doc-sgl-title-case>` for the title of each documentation page and :ref:`sentence case <doc-sgl-sentence-case>` for headers within the document.
   This means the sections and subsections will be capitalized like normal sentences,  first word is always capitalized and the rest is spelled as they would in “normal text”.

   .. seealso:: 
      * :ref:`doc-sgl-rules-title`

#. **Spelling**

   Use common spelling for British English. Some specific terms have a special spelling. See :ref:`spelling-ref`.

#. **Headers underlining**

   Headline underline should follow :ref:`doc-cgl-headline-underline`.

   .. code-block:: rst

      ==========
      Page Title
      ==========

      First header level
      ==================

      Second header level
      -------------------

      Third header level
      ~~~~~~~~~~~~~~~~~~

   .. seealso:: 

      * :ref:`doc-cgl-rest`

#. **Whitespace and indentation**
   
   Always use **three spaces** for one level of indentation, and do not insert *Tab* character for indentation.

----

reStructuredText & Sphinx
=========================

Syntax and reference for reStructuredText (also referred to as reST) and Sphinx.

* :ref:`code-rst`

----

Writing new documentation
=========================

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_boilerplate

----

Hosting this documentation
==========================

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_hosting.rst

----

Contribution Guide
==================

Read the :ref:`contribution guide <howto-contribute-doc>` on how to contribute to this documentation.

TODO: report issues
