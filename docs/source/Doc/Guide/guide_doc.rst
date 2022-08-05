===================
Documentation Guide
===================

This manual covers writing documentation. This includes, contributing to this documentation, documentation 
coding guidelines, conventions, and provide links to `GitHub issues`_.

.. _`GitHub issues`: https://github.com/tky1026/rris_doc/issues

----

Build this documentation
========================

This documentation is rendered using Sphinx, and hosted on `Read the Docs <https://rris-doc-testing.readthedocs.io/en/latest/>`_.

To build this documentation locally, please follow the instruction below:

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_building.rst

----

Documentation content style guide
=================================

This contains conventions, coding guidelines and best practices for contributing to this documentation.
In general, the documentation follows the conventions as described in the following sections.

We mainly uses :term:`reStructuredText(reST) <reST>` markup language for writing docuementation, the file ending of reST files is ``.rst``.
However, :term:`Markdown` format with file ending ``.md`` is acceptable as well.

The most important conventions for writing reST files are summarized on this page, the rest can be found in the subchapters.


#. **Title capitalization**

   Use :ref:`title case <doc-sgl-title-case>` for the title of each documentation page and :ref:`sentence case <doc-sgl-sentence-case>` for headers within the document.
   This means the sections and subsections will be capitalized like normal sentences,  first word is always capitalized and the rest is spelled as they would in “normal text”.

   .. seealso:: 
      * :ref:`doc-sgl-rules-title`

#. **Spelling**

   Use common spelling for British English. Some specific terms have a special spelling. See :ref:`spelling-ref`.

#. **Coding guide for headers**

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

#. **Refer to elements in the GUI with** ``:guilabel:``

   When describing GUI elements, follow :ref:`doc-cgl-refer-gui`.

   Example:

   .. code:: rest
      
      :guilabel:`ADMIN TOOLS > Extensions`

   This will look like this: :guilabel:`ADMIN TOOLS > Extensions`

**Table of contents**

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_writing
   Documentation/doc_structure
   Documentation/doc_format
   Documentation/doc_guide_rst
   Documentation/doc_commit

----

Writing new documentation
=========================

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_boilerplate

----

reStructuredText & Sphinx
=========================

.. toctree:: 
   :maxdepth: 1

   TODO <../Test/file3>

----

Hosting this documentation
==========================

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_hosting.rst

----

Contribution Guide
==================

.. toctree:: 
   :maxdepth: 1

   Documentation/doc_contribution.rst

