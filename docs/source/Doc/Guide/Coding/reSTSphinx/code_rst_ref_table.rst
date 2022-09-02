.. _code-rst-ref-table:

======
Tables
======

There are several ways to create tables in reST. Use what works best for your use case.

Grid table
==========

.. code-block:: rst

   +----------+----------+
   | Header 1 | Header 2 |
   +==========+==========+
   | 1        | one      |
   +----------+----------+
   | 2        | two      |
   +----------+----------+

+----------+----------+
| Header 1 | Header 2 |
+==========+==========+
| 1        | one      |
+----------+----------+
| 2        | two      |
+----------+----------+

.. tip:: 

   You can use this `table generator <https://www.tablesgenerator.com/text_tables>`__ to create a grid table.

----

Simple table
============

.. code-block:: rst

   ========  ========
   Header 1  Header 2
   ========  ========
   1         one
   2         two
   ========  ========

========  ========
Header 1  Header 2
========  ========
1         one
2         two
========  ========

----

CSV table
=========

.. code-block:: rst

   .. csv-table:: Numbers
      :header: "Header 1", "Header 2"
      :widths: 15, 15

      1, "one"
      2, "two"

.. csv-table:: Numbers
   :header: "Header 1", "Header 2"
   :widths: 15, 15

   1, "one"
   2, "two"

----

Reference
=========

* https://docutils.sourceforge.io/docs/user/rst/quickref.html#tables