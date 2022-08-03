.. _doc-cgl-rest:

================================
Coding Guidelines for reST Files
================================

Basic formatting rules
----------------------


.. _doc-cgl-headline-underline:

Headline underlining
--------------------


.. _doc-cgl-refer-gui:

Referring to GUI elements
-------------------------

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
-----------------------

When pointing out keyboard shortcuts or keystroke sequences, use text role ``kbd``.

Example:

.. code:: rst

   Press :kbd:`ctrl` + :kbd:`s`

How it looks:

   Press :kbd:`ctrl` + :kbd:`s`