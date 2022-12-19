.. include:: /includes.rst.txt
.. _doc-cgl-rest:

=============================
Documentation Code Formatting
=============================

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
   :linenos:

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

   1. Header Level 1
   =================

   1. Header Level 2
   -----------------

   1. Header Level 3
   ~~~~~~~~~~~~~~~~~

   1. Header Level 4
   """""""""""""""""

   1. Header Level 5
   '''''''''''''''''

   1. Header Level 6
   ^^^^^^^^^^^^^^^^^

   1. Header Level 7
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

.. tabs::

   .. code-tab:: rst

      Select :guilabel:`File > Open`

   .. tab:: Result

      Select :guilabel:`File > Open`

.. tabs::

   .. code-tab:: rst

      Click on :guilabel:`ADMIN TOOLS > Extensions` in the backend.

   .. tab:: Result

      Click on :guilabel:`ADMIN TOOLS > Extensions` in the backend.

----

Referring to keystrokes
=======================

When pointing out keyboard shortcuts or keystroke sequences, use text role ``kbd``.

.. tabs::

   .. code-tab:: rst

      Press :kbd:`ctrl` + :kbd:`a`

   .. tab:: Result

      Press :kbd:`ctrl` + :kbd:`a`

----

Referring to directories
========================

When pointing out folders/directories, use text role ``dir``.

.. tabs:: 

   .. code-tab:: rst

      .. include:: /includes.rst.txt
      
      Full path to this file is :dir:`docs/source/Doc/Guide/Documentation/doc_guide_rst.rst`.

   .. tab:: Result

      Full path to this file is :dir:`docs/source/Doc/Guide/Documentation/doc_guide_rst.rst`.

.. note:: 

   Need to include ``includes.rst.txt`` for text role ``dir``.

   .. code-block:: rst

      .. include:: /includes.rst.txt

----

.. _doc-cgl-member-tag:

Addressing team members
=======================

All team members are assigned a unique substitution tag, see the ``sub`` field of each member at :ref:`intro-team`.

When addressing any of the team members inline, use substitution tag associated to each person to have the tag auto replaced
by a permanent link with a preset name to the person's details at :ref:`intro-team`.

.. tabs::

   .. code-tab:: rst

      For example, |rris_kuanyuee| wrote this page.

   .. tab:: Result

      For example, |rris_kuanyuee| wrote this page.

----

Text substitution
=================

Text substitution takes place when the documentation is being rendered to HTML. 

Currently available text substitution tag and corresponding replacement:

.. list-table:: 

   * - ``|rris_copyright|``
     - |rris_copyright|
   * - ``|rris_license|``
     - |rris_license|
   * - ``|lang_cpp|``
     - |lang_cpp|
   * - ``|lang_py3|``
     - |lang_py3|
   * - ``|lang_js|``
     - |lang_js|
   * - ``|lang_css|``
     - |lang_css|
   * - ``|lang_html|``
     - |lang_html|
   * - ``|ros_melodic|``
     - |ros_melodic|
   * - ``|ros_noetic|``
     - |ros_noetic|
   * - ``|ros_foxy|``
     - |ros_foxy| 


For team members' substitution tag, please refer to :ref:`intro-team`.
