.. _doc-cgl-rest:

================================
Coding Guidelines for reST Files
================================

Basic formatting rules
======================

Encoding
--------

* use utf-8

.. _doc-cgl-rest-indent:

Whitespace and indentation
--------------------------

.. important:: 

   Always use indentation levels correctly. Your code may not be rendered as expected if you do not.

* remove white space from the end of lines (no trailing tabs or spaces)
* don’t use tabs, configure your editor to insert space characters when pressing :kbd:`Tab` key instead of tab characters.
* one indentation level consists of **three spaces**
* code examples use three spaces as indentation leve as well

Example:

.. code-block:: rst

   .. image:: ../images/a4.jpg
      :alt: RRIS image
      :target: https://www.ntu.edu.sg/rris
      :class: with-shadow

* Here, lines 2-4 must be indented one level (3 spaces)




.. _doc-cgl-headline-underline:

Headline underlining
====================


.. _doc-cgl-refer-gui:

Referring to GUI elements
=========================

If you describe something that needs to be selected from a menu or other GUI
element or clicked one after the other, use ``>`` as separator and use
text role ``guilabel``.

.. important::

   Use the spelling of the word as used in the GUI!

Examples:

.. code-block:: rest

   Select :guilabel:`File > Open`


Select :guilabel:`File > Open`

.. code-block:: rest

   Click on :guilabel:`ADMIN TOOLS > Extensions` in the backend.

Click on :guilabel:`ADMIN TOOLS > Extensions` in the backend.

----

Referring to keystrokes
=======================

When pointing out keyboard shortcuts or keystroke sequences, use text role ``kbd``.

Example:

.. code:: rst

   Press :kbd:`ctrl` + :kbd:`s`

How it looks:

   Press :kbd:`ctrl` + :kbd:`s`