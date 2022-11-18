.. _code-rst-ref-hierarchy-structure:

==================================================
Toctree and the Hierarchical Structure of a Manual
==================================================

You can define what should be included in the menu with the `.. toctree:: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`__ directive. 
Only ``.rst`` and ``.md`` files that are included in a toctree, are included in the menu.

The ``.. toctree::`` directive can also be used to display a table of contents on current page (if ``:hidden:`` is not added in ``.. toctree::``).

The first headline of an ``.rst`` file is its "doctitle". That is the document's title property. 
The title and the following headlines are used for cross-references and appear in menus and table of contents.

General rules for using ``.. toctree::``
========================================

#. Each ``.rst`` file should have a doctitle:

   .. code-block:: rst

      ==========
      Some Title
      ==========

#. Every ``.rst`` file must be included in ``.. toctree::``.

#. Within ``.. toctree::``, include files by specifying relative path to the files. File extensions ``.rst`` or ``.md`` are optional.

   By default, the file's doctitle will be used when displaying in table of contents.

   .. code-block:: rst

      .. toctree::

         path/to/file1
         path/to/file2

   Can also replace the title by doing so:

   .. code-block:: rst

      .. toctree::

         Some Other Title <path/to/file1>
         path/to/file2

.. #. Do not use any additional :ref:`headlines <code-rst-ref-headline-section>` in the file if it contains a ``.. toctree::`` directive.

Examples
========

Example: hidden
---------------

This will create a menu, using the header of Introduction/Index.rst and Configuration/Index.rst. 
The menu structure is not displayed as a table of contents on the current page as it is being "hidden".

.. code-block:: rst

   .. toctree:: 
      :hidden:

      Introduction/Index
      Configuration/Index

Example: glob, not hidden, titlesonly
-------------------------------------

This will read all files and create a menu. 
It will also render the menu structure on the current page. 
It will read the files using globbing ``*``, meaning you do not need to explicitly write the file names. 
If new files are added, the menu will be updated automatically. 
Only the doctitle (first header in file) will be displayed since ``:titlesonly:`` is added.

.. code-block:: rst

   .. toctree:: 
      :glob:
      :titlesonly:

      *

Example: maxdepth, caption
--------------------------

This will show header of up to level as spicified in ``:maxdepth:`` in the menu structure, and ``Table of Contents`` specified in ``:caption:`` will appear as title of this table of contents.

.. code-block:: rst

   .. toctree:: 
      :maxdepth: 2
      :caption: Table of Contents

      Introduction/Index
      Configuration/Index




Additional information
======================

* **Sphinx**: explaining `toctree directive <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`__