.. include:: /includes.rst.txt
.. _code-rst-ref-include:

===============
Including Files
===============

Each ``.rst`` or ``.md`` file will result in a url of its own. 
At parsing level these files are processed independently. 
``.. toctree::`` directives are controlling the menu hierarchy of the contents. 
For each file intermediate results are stored and each file will be processed during build.

Some documentation projects have the same snippet of text appear in several places. 
In this case it may make sense to include text snippets. The :rst:`.. include::` directive does this. 
What you need to know about including files:

Syntax
======

.. code-block:: rst

   .. include:: <path-to-file>

.. note:: 

   To reduce problems when including files, use path relative to where ``conf.py`` is located. That is: ``/Doc/...``.
   For example:

   .. code-block:: rst

      .. include:: /Doc/_Templates/package.rst.txt

Advantages
==========

#. Includes are performed on a textual basis and therefore processed in a very fast manner when the parent file is parsed.
#. Includes do not lead to intermediate results that need to be resolved during build.

Disadvantages
=============

#. Since includes are treated as if the text had been written exactly where the include is done the text needs to fit with respect to the section levels.
#. You cannot see the source of included text directly.
#. When Sphinx reports warnings and errors the exact text location can be much harder to spot.

Recommendations
===============

.. attention:: 

   Includes can easily cause trouble. Think well before using them.

.. important:: 

   Do not use the file endings ``.rst`` or ``.md`` for include files to prevent Sphinx from treating them as individual source files!
   In case you have many include files this would lead to many warnings and slow down the build process considerably, use ``*.rst.txt`` ending instead to define a reST file type.

.. warning:: 

   You cannot include files from outside the ``Doc/`` folder.

----

Include Markdown files into an rST file
=======================================

The :rst:`.. include::` directive acts as *copy & paste* that directly insert raw text. 
Since Markdown has a different syntax to reStructuredText, including ``.md`` into ``.rst`` will cause rendering or formatting issues. 

Hence, use the :rst:`parser` option with ``myst_parser`` as shown:

.. code-block:: rst

   .. include:: /path/to/file.md
      :parser: myst_parser.docutils_

----

Literalinclude
==============

Sometimes one may want to include the file and display it as a block of code like :rst:`code-block`, use :ref:`literalinclude <code-rst-ref-code-blocks-literalinclude>` instead.

.. code-block:: rst

   .. literalinclude:: /Doc/_Templates/project.rst.txt
      :language: rst

----

Reference
=========

* `Markedly Structured Text <https://myst-parser.readthedocs.io/en/latest/>`__
