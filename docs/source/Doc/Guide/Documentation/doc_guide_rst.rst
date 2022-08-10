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
* code examples use three spaces as indentation level as well

Example:

.. code-block:: rst

   .. image:: ../images/a4.jpg
      :alt: RRIS image
      :target: https://www.ntu.edu.sg/rris
      :class: with-shadow

* Here, lines 2-4 must be indented one level (3 spaces)

Line length
-----------

* We do not enforce maximum line length in this documentation although some may suggest it is best to keep lines shorter than 80 characters.
* If in doubt about the length: use short line!

   * That way reST is readable as source as well
   * Files can be easily edited directly on GitHub
   * Files can be compared in a diff view

Special characters
------------------

The only way to include "special" characters is to use them directly. 

----

.. _doc-cgl-headline-underline:

Headline underlining
====================

In reStructuredText it is possible to use any type of underlining. The first used will be recognized as level 1 etc.

However, in order to make this documentation tidy and make it easier for other contributors to find their way around a file and pick the correct underlining for the header level.

Use the conventions as defined in :ref:`code-rst-ref-headline-section`.

This underlining is used **per (.rst)** file. It does not matter where in the toctree the file is. You always start with underlining for level 1 (title) in each file:

.. code-block:: text

   ========
   1. Title
   ========

   2. Header Level 1
   =================

   3. Header Level 2
   -----------------

   4. Header Level 3
   ~~~~~~~~~~~~~~~~~

   5. Header Level 4
   """""""""""""""""

   6. Header Level 5
   '''''''''''''''''

   7. Header Level 6
   ^^^^^^^^^^^^^^^^^

   8. Header Level 7
   #################

   etc.

----

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