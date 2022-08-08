=====================
Problems With Indents
=====================

Common mistake #1: Incorrect indents
====================================

Always indent correctly (3 spaces per level)

Correct syntax
--------------

.. code-block:: rst

   .. image:: ../../images/a4.jpg
      :width: 100px
      :class: with-shadow

How it looks:

.. image:: ../../../../Asset/ntu-icon.png
   :width: 100px
   :class: with-shadow

Incorrest syntax
----------------

Here, ``:width:`` is indented with only 2 spaces. The image will not be rendered properly.

.. code-block:: rst

   .. image:: ../../images/a4.jpg
     :width: 100px
     :class: with-shadow
