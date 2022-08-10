.. _code-rst-ref-links:

==============================
Hyperlinks & Cross Referencing
==============================

Quick reference
===============

In Sphinx you can use several types of links:

:ref:`code-rst-ref-links-external-links`

   For linking to other sources outside of the documentation.
   
   .. code-block:: rst

      `anchor text <url>`__

:ref:`code-rst-ref-links-cross-ref`

   For linking to other sections within the documentation.

   .. code-block:: rst

      :ref:`anchor text <link-target>`


:ref:`code-rst-ref-links-prevent-links`

   To prevent hyperlinks being automatically generated from simple URLs

   .. code-block:: rst

      :samp:`<url>`

----

.. _code-rst-ref-links-external-links:

External links
==============

.. important:: 

   Do not use this mechanism (external links) for links to sections within the documentation. 
   Use the intersphinx mechanism as described in :ref:`code-rst-ref-links-cross-ref-intersphinx`.
   Explanation of why you should do this can be found within the section.

You can use one or more underscores(``_``) for the link. The difference is as follows:

* Two underscores create an :ref:`anonymous URL <code-rst-ref-links-external-links-1>`
* One underscore creates a :ref:`named reference <code-rst-ref-links-external-links-2>`

For further explaination of the difference between these two, please see `Stackoverflow <https://stackoverflow.com/questions/27420317/restructured-text-rst-http-links-underscore-vs-use>`__.

If in doubt, just use 2 underscores as explained in the next section :ref:`code-rst-ref-links-external-links-1`.

.. _code-rst-ref-links-external-links-1:

External link as anonymous URL
------------------------------

Use double underscores ``__``, if its a one-off (anonymous) URL which you don't intend to reference.

The target URI may directly embedded inline with an anchor text. 
If the link text should be the web address, you don’t need special markup at all, the parser finds links and mail addresses in ordinary text.

**Syntax**

.. code-block:: rst
   
   `Anchor text <URL>`__

* There must always be a space between the anchor text and the URL

**Example**

.. code-block:: rst

   `Sphinx hyperlinks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks>`__
   
   Web address of RRIS: `<https://www.ntu.edu.sg/rris>`__

**How it looks**

`Sphinx hyperlinks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks>`__

Web address of RRIS: `<https://www.ntu.edu.sg/rris>`__

.. _code-rst-ref-links-external-links-2:

External link as named reference
--------------------------------

By using one underscore ``_``, a named reference is created.

#. The target URL may directly embedded inline with an anchor text. 
   Notice that a named reference of *anchor text* is created and this label can be used anywhere else in the document.

   **Syntax**

   .. code-block:: rst

      `Anchor text <URL>`_

   **Example**

   .. code-block:: rst

      This is `NTU website <https://www.ntu.edu.sg/>`_

      Using named reference `NTU website` again.

   **How it looks**

   This is `NTU website <https://www.ntu.edu.sg/>`_

   Using named reference `NTU website`_ again.

#. We can also seperate the link and the target definition:

   **Syntax**

   .. code-block:: rst

      `Anchor text`_

      .. _Anchor text: URL

   **Example**

   .. code-block:: rst

      This is a paragraph that contains a `link to Google`_.

      .. _link to Google: https://www.google.com/

   **How it looks**

   This is a paragraph that contains a `link to Google`_.

   .. _link to Google: https://www.google.com/

----

Internal link targets
=====================

Internal linking is done via a special reST role provided by Sphinx.

.. _code-rst-ref-link-explicit-target:

Explicit link targets (Labels for cross referencing)
----------------------------------------------------

You can define an explicit link target with a label for a section (or chapter):

A section label of the name ``columns-inline`` is set:

.. code-block:: rst

   .. _columns-inline:

Here, the link target *columns-inline* will be defined.

* Place the link target definition directly before the section header:

.. code-block:: rst

   .. _columns-inline:

   Inline columns
   ==============

* You can define more than one link target definition (for example if you want to keep some for historical reasons to not break links but the name has changed considerably)

.. _code-rst-ref-link-implicit-target:

Implicit link targets
---------------------

For every section (or chapter), an implicit link target is created from the header automatically.
To reference it, simply add a single underscore behind section text.

**Example**

.. code-block:: rst

   Implicit references, like `Internal link targets`_

**How it looks**

Implicit references, like `Internal link targets`_

However, there are some disadvantages in using these, so we still encourage creating `Explicit link targets (Labels for cross referencing)`_.

.. _code-rst-ref-links-cross-ref:

Cross referencing (``:ref``)
----------------------------

This section describes how to link to sections of the current or other documents correctly.

Additional information: See the `Sphinx documentation <https://www.sphinx-doc.org/en/1.6/markup/inline.html#cross-referencing-arbitrary-locations>`_.

In the same document
~~~~~~~~~~~~~~~~~~~~

A :ref:`section label <code-rst-ref-link-explicit-target>` of the name ``columns-inline`` has been set somewhere:

.. code-block:: rst

   .. _columns-inline:

   Inline columns
   ==============

You can then link it like this from the same manual:

.. code-block:: rst

   :ref:`columns-inline`

This will use the header of the section as anchor text.

You can also explicitly set an anchor text:

.. code-block:: rst

   :ref:`Inline columns <columns-inline>`

.. _code-rst-ref-links-cross-ref-intersphinx:

From another document
~~~~~~~~~~~~~~~~~~~~~

#. We can still use the unique label within the documentation as `In the same document`_, if the label is unique throughout the whole documentation.
   
   **Example**

   .. code-block:: rst

      Refer to :ref:`spelling-ref`.

   **How it looks**

   Refer to :ref:`spelling-ref`.

#. Using `Intersphinx <https://docs.readthedocs.io/en/stable/guides/intersphinx.html>`_

   To use Intersphinx you need to add it to the list of extensions in your conf.py file.

   .. code-block:: py

      # conf.py file

      extensions = [
         'sphinx.ext.intersphinx',
      ]

   And use the ``intersphinx_mapping`` configuration to indicate the name and link of the projects you want to use.

   .. code-block:: py

      # conf.py file

      intersphinx_mapping = {
         'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
      }

   Now you can use the ``sphinx`` name with a cross-reference role:

   .. code-block:: rst

      - :ref:`sphinx:ref-role`
      - :ref:`:ref: role <sphinx:ref-role>`
      - :doc:`sphinx:usage/extensions/intersphinx`
      - :doc:`Intersphinx <sphinx:usage/extensions/intersphinx>`

   **How it looks**

   - :ref:`sphinx:ref-role`
   - :ref:`:ref: role <sphinx:ref-role>`
   - :doc:`sphinx:usage/extensions/intersphinx`
   - :doc:`Intersphinx <sphinx:usage/extensions/intersphinx>`


Using Intersphinx for this documentation
""""""""""""""""""""""""""""""""""""""""

This documentation is going to be hosted on Read the Docs eventually. 
Therefore if you intend to use Intersphinx to cross-referencing within the documentation, it is recommended to use the hosted url for ``intersphinx_mapping``.

**Example**

.. code-block:: py

      # conf.py file

      intersphinx_mapping = {
         't3doc': ('https://rris-doc-testing.readthedocs.io/en/latest/', None),
      }

.. code-block:: rst

   Refer to :ref:`t3doc:spelling-ref`

**How it looks**

Refer to :ref:`t3doc:spelling-ref`

.. note:: 

   This will require editting ``conf.py``, which consists of some important configurations of this documentation. 
   Please enquire the :ref:`maintainers <team-doc-maintainers>` before doing so. Otherwise, we still suggest creating a unique label method.
   

----
   
.. _code-rst-ref-links-prevent-links:

Preventing links
================

Sphinx automatically converts simple URLs into links. This can be unintentional in certain contexts. 
To prevent linking, use ``:samp:`` directive to wrap the URL.

**Example**

.. code-block:: rst

   RRIS webpage is :samp:`https://www.ntu.edu.sg/rris`.

RRIS webpage is :samp:`https://www.ntu.edu.sg/rris`.

To emphasize parts of the URL, use curly braces:

.. code-block:: rst

   For example :samp:`https://www.ntu.edu.sg/{rris}`.

For example :samp:`https://www.ntu.edu.sg/{rris}`.

