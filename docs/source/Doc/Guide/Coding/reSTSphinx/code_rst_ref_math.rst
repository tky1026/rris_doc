.. include:: /includes.rst.txt
.. _code-rst-ref-math:

====
Math
====

reST supports LaTeX-style math. Use :rst:`math` directive to render math elements.

Inline math
===========

.. code-block:: rst

   This is an inline math :math:`x^2+y^2=z^2`.

This is an inline math :math:`x^2+y^2=z^2`.

Block math
==========

- Multiple equations should be seperated by a blank link

   .. code-block:: rst

      .. math::

         (a + b)^2 = a^2 + 2ab + b^2

         (a - b)^2 = a^2 - 2ab + b^2

   .. math::

      (a + b)^2 = a^2 + 2ab + b^2

      (a - b)^2 = a^2 - 2ab + b^2

- Having multiple aligned lines in an equation, aligned at ``&`` and separated by ``\\``

   .. code-block:: rst

      .. math:: 

         (a + b)^2 &= (a + b)(a + b) \\
                   &= a^2 + 2ab + b^2

   .. math:: 

      (a + b)^2 &= (a + b)(a + b) \\
                &= a^2 + 2ab + b^2

- When the math is only one line of text, it can also be given as a directive argument:

   .. code-block:: rst

      .. math:: (a + b)^2 = a^2 + 2ab + b^2

- Normally, equations are not numbered. If you want your equation to get a number, use the :rst:`label` option. When given, it selects an internal label for the equation, by which it can be cross-referenced, and causes an equation number to be issued.

- There is also an option :rst:`nowrap` that prevents any wrapping of the given math in a math environment.
  When you give this option, you must make sure yourself that the math is properly set up. For example:

   .. code-block:: rst

      .. math:: some equations
         :nowrap:

         \begin{eqnarray}
            y    & = & ax^2 + bx + c \\
            f(x) & = & x^2 + 2xy + y^2
         \end{eqnarray}

.. math:: some equations
   :nowrap: 

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}


Reference
=========

- `math directive <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-math>`__
- For more details, look into the documentation of the `AmSMath LaTeX package <https://www.ams.org/publications/authors/tex/amslatex>`__ .