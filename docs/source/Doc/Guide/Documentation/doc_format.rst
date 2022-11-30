=============================
File Formats (reST, Markdown)
=============================

.. _doc-format-rest:

reST
====

.. important:: 
   The entire official documentation uses reST only. Use reST for writing documentation whenever possible.
   However, :ref:`doc-format-markdown` is also supported.

The rendering chain and tools are built and optimized to process :term:`reST` markup. Please go ahead and use that format.

The file ending of reST files is ``.rst``.


.. _doc-format-markdown:

Markdown
========

Currently, you can also use :term:`Markdown` for documentation.

One problem with markdown is that there are many dialects. Since a while there is a standard **commonmark**.
At `Read the Docs <https://readthedocs.org>`_ poeple are trying to make commonmark available.
See `http://blog.readthedocs.com/adding-markdown-support/ <http://blog.readthedocs.com/adding-markdown-support/>`_ for the details.
We use `myst-parser <https://www.sphinx-doc.org/en/master/usage/markdown.html>`_ for Markdown support in :term:`Sphinx` project.

Our documentation has also been configured to detect Markdown files as well, with ``.md`` as file ending.

If you're encountering problems with the rendering of your Markdown files, consider switching to :ref:`doc-format-rest`.

reST vs Markdown
================

Victor Zverovich makes the comparison::

   According to John Gruber, the inventor of Markdown, “Markdown’s syntax is intended for one
   purpose: to be used as a format for writing for the web.” and, in particular, it supports inline HTML.
   reStructuredText on the other hand is specifically designed for writing technical documentation.

Read the Docs::

   "It should be noted that Commonmark doesn’t support a lot of the concepts that RST lets you represent.
   In particular, there is no standardized way in Commonmark to represent inline or block levels constructs.
   So things like the toctree directive and :ref: markup don’t have an analog."

**reST (with Sphinx toolchain)**

``+``
   * extendable
   * semantic markup
   * cross-references across manuals (links still work if text is moved - unless moved to a different manual)
   * richer feature set

``-``
   * Syntax may be unusual and rendering breaks if not done correctly, for example

     * indenting is important
     * new lines are important, for example before, after and between bullet lists
     * :ref:Common ptifalls.

**Markdown**

``+``
   * in general better tool support
   * widely supported
   * syntax is simpler and easier to read

``-``
   * various flavours (unless **commonmark** is used)
   * less features

Additional information
----------------------

* Victor Zverovich: `reStructuredText vs Markdown for documentation <https://www.zverovich.net/2016/06/16/rst-vs-markdown.html>`_ (2016)
* Read the Docs: `Read the Docs & Sphinx now support Commonmark <https://blog.readthedocs.com/adding-markdown-support/>`_ (2015)