===================
Problems With Links
===================

There are several ways to write links, here we assume you are using external links with the following syntax. For more information see the references at the bottom on this page.

Correct syntax
==============

.. code-block:: rst

   `anchor text <url>`_

Example:

.. code-block:: rst

   `RRIS <https://www.ntu.edu.sg/rris>`_

How it looks:

   `RRIS <https://www.ntu.edu.sg/rris>`_

Common mistake #1: Missing space
================================

Make sure there is a space between the anchor text and the opening ``<``.

Wrong syntax
------------

.. code-block:: rst

   `RRIS<https://www.ntu.edu.sg/rris>`_

Common mistake #2: Missing underscore (_)
=========================================

Missing ``_`` or ``__`` at the end:

Wrong syntax
------------

.. code-block:: rst

   `RRIS <https://www.ntu.edu.sg/rris>`

Additional information
======================

* :ref:`code-rst-ref-links-external-links`