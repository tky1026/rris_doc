.. _code-rst-ref-comment:

========
Comments
========


Parts of the text in reST source can be "commented out":

.. pull-quote:: 

   Any text which begins with an explicit markup start but doesn't
   use the syntax of any of the constructs above, is a comment.

See http://docutils.sourceforge.net/docs/user/rst/quickref.html#comments

This means: write :literal:`..\ `, that is dot-dot-blank at the beginning of the
line, taking the indentation level into account.

Examples
========

Example:

.. code-block:: rst

   .. So here we have a comment.
      It can spread over lines as
      long as you keep the indentation.

Example:

.. code-block:: rst

   .. This text will not be shown,
      but, for instance, in HTML might be
      rendered as an HTML comment, if the html writer is set up for that.

Example:

.. code-block:: rst

   .. here we start an unordered list:

   -  one

   -  two

      .. this is another comment. Since it's within the list it is aligned
         with 'two', which is the contents of the second list item

   -  three
