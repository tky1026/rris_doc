.. _code-rst-pitfall-inline:

==========================
Problems With Inline Style
==========================

If you use **bold** or *italic*, make sure there is no space between the markup and the styled text.

Correct syntax
==============

.. code-block:: rst

   This is normal text. **This is bold text.**

How it looks:

   This is normal text. **This is bold text.**

Wrong syntax
============

.. code-block:: rst

   This is normal text. ** This is bold text.**

How it looks:

   This is normal text. ** This is bold text.**

Additional information
======================

* `Docutils cheat-sheet for reStructuredText: Inline markup <https://docutils.sourceforge.io/docs/user/rst/quickref.html#inline-markup>`_