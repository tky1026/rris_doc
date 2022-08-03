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

The most important conventions are summarized on this page, the rest can be found in the subchapters.


#. **Title capitalization**

   Use title case - ...

#. **Spelling**

   Use common spelling for British English. Some specific terms have a special speeling. See :ref:`spelling-ref`.

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

   Documentation/doc_spelling
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

