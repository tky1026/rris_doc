.. _code-rst-ref-inline-roles:

========================
Inline Code & Text Roles
========================

Semantically mark up specific Text
==================================

There are several ways to semantically mark specific parts of the text. 
The main goal is to be able to use a consistent style for specific parts of the text, for example code fragments, file names and GUI elements.

Text roles
----------

#. **Preferred**: Use `Sphinx interpreted text roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`__ to explicitly specify what kind of text / code (text role) it is. 
   This shows the semantics and in the output there may be a a special coloring or highlighting:

   `Standard Sphinx interpreted text roles
   <http://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#other-semantic-markup>`__:

   .. table:: 
      :widths: grid
      
      ================ ================================================== ============================================== ====
      Role             Source                                             Output                                         Note
      ================ ================================================== ============================================== ====
      abbr             ``:abbr:`LIFO (last-in, first-out)```              :abbr:`LIFO (last-in, first-out)`              An abbreviation. If the role content contains a parenthesized explanation, it will be treated specially: it will be shown in a tool-tip in HTML, and output only once in LaTeX.
      code             ``:code:`result = (1 + x) * 32```                  :code:`result = (1 + x) * 32`
      command          ``:command:`rm```                                  :command:`rm`                                  The name of an OS-level command, such as rm.
      dfn              ``:dfn:`something```                               :dfn:`something`                               Mark the defining instance of a term in the text. (No index entries are generated.)
      file             ``:file:`/etc/passwd```                            :file:`/etc/passwd`
      guilabel         ``:guilabel:`&Cancel```,                           :guilabel:`&Cancel`,                           Labels presented as part of an interactive user interface should be marked using guilabel. This includes labels from text-based interfaces such as those created using curses or other text-based libraries. Any label used in the interface should be marked with this role, including button labels, window titles, field names, menu and menu selection names, and even values in selection lists.
                       ``:guilabel:`O&k```,                               :guilabel:`O&k`,
                       ``:guilabel:`&Reset```,                            :guilabel:`&Reset`,
                       ``:guilabel:`F&&Q```                               :guilabel:`F&&Q`
      kbd              ``Press :kbd:`ctrl` + :kbd:`s```                   Press :kbd:`ctrl` + :kbd:`s`                   Mark a sequence of keystrokes. What form the key sequence takes may depend on platform- or application-specific conventions. When there are no relevant conventions, the names of modifier keys should be spelled out, to improve accessibility for new users and non-native speakers. For example, an xemacs key sequence may be marked like :kbd:`C` + :kbd`x`, :kbd:`C` + :kbd:`f`, but without reference to a specific application or platform, the same sequence should be marked as :kbd:`ctrl` + :kbd:`x`, :kbd:`ctrl` + :kbd:`f`.
      mailheader       ``:mailheader:`Content-Type```                     :mailheader:`Content-Type`                     The name of an RFC 822-style mail header. This markup does not imply that the header is being used in an email message, but can be used to refer to any header of the same â€œstyle.â€ This is also used for headers defined by the various MIME specifications. The header name should be entered in the same way it would normally be found in practice, with the camel-casing conventions being preferred where there is more than one common usage.
      ref              ``:ref:`Inline-Code <code-rst-ref-inline-roles>``` :ref:`Inline-Code <code-rst-ref-inline-roles>` Sphinx cross-referencing
      ================ ================================================== ============================================== ====


   `Standard Docutils interpreted text roles
   <http://docutils.sourceforge.net/docs/ref/rst/roles.html#standard-roles>`__:
   
   .. table:: 
      :widths: grid

      ================== ================================================= ============================================ ===
      Role               Source                                            Output                                       Note
      ================== ================================================= ============================================ ===
      emphasis           ``:emphasis:`text`, *text*``                      :emphasis:`text`, *text*
      literal            ``:literal:`\ \ abc```                            :literal:`\ \ abc`
      literal            ``:literal:`text`, ''text''``                     :literal:`text`, ``text``
      math               ``:math:`A_\text{c} = (\pi/4) d^2```              :math:`A_\text{c} = (\pi/4) d^2`             The math role marks its content as mathematical notation (inline formula). The input format is LaTeX math syntax without the â€œmath delimitersâ€œ ($ $).
      rfc, rfc-reference ``:RFC:`2822```                                   :RFC:`2822`
      strong             ``:strong:`text`, **text**``                      :strong:`text`, **text**                     Implements strong emphasis.
      subscript          ``:subscript:`subscripted```                      :subscript:`subscripted`
      superscript        ``:superscript:`superscripted```                  :superscript:`superscripted`
      t, title-reference ``:t:`Design Patterns```                          :t:`Design Patterns`                         The :title-reference: role is used to describe the titles of books, periodicals, and other materials.
      ================== ================================================= ============================================ ===

   .. tip::

      For more information about the ``:ref:`` directive, see :ref:`code-rst-ref-links`.

#. As an alternative, use the `default text role <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-default_role>`__ for small inline code snippets, but it is better to use specific text roles.
   However, if no text role exists, you may use this to mark the text.

   Surround the code by *single backticks* and don't start or end the code with whitespace. Example: Type ```2 + 2 = 4``` to get `2 + 2 = 4` as result.

#. Just write the code as it is. This may make the text more difficult to read.
   Use your common sense.

When to use literal code ```...``` 
----------------------------------

Things get tricky if your inline code already contains single backquotes (backticks).

4. In many cases you can still use the *interpreted text role* as described in 1. to 3.
   For example we can write ``:code:`:html:`<br>```` to get :code:`:html:`<br>``

   This is possible if (a) your code doesn't start with a backtick and (b) if no backtick in
   your code has a trailing whitespace.

5. **But:** To be really free to include inline any code containing backticks you will want to use
   `inline literals <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-literals>`__. 
   Again: Don't escape or double anything, whitespace is maintained.

   *Example*

   Write::

      SQL-example code: ``SELECT  `tt_content` . `bodytext`  AS  `t1` . `text`;``

   to get:

   SQL-example code: ``SELECT  `tt_content` . `bodytext`  AS  `t1` . `text`;``

   **The drawbacks** of literal inline code notation are:

   -  there is no way to semantically classify the kind of code
   -  there is no special coloring or highlighting
   -  the raw reST code looks less beautiful and is less readable

----

Inline code vs code blocks
==========================

Inline code
-----------

The name for  **very small** code snippets that occur within normal text flow within sentences is *inline code*.

-  is styled somewhat differently,
-  has **no** syntax highlighting,
-  does **not** need to be syntactically correct,
-  can be compared to ``<span>...</span>`` tags in html,
-  and is made up by self-defined names.

   .. code-block:: rst

      .. How to define custom code role

      .. role:: bash(code)
         :language: bash

      .. Using defined code role

      Test inline: :bash:`export FOO="bar"`.

   **How it looks**

   .. role:: bash(code)
      :language: bash

   Test inline: :bash:`export FOO="bar"`.

- see `here <https://docutils.sourceforge.io/docs/ref/rst/roles.html#toc-entry-5>`__ for more information.

Code block
----------

-  appear "as a box",
-  can have syntax highlighting,
-  need to be syntactically correct in order to have highlighting,
-  can be compared to `<pre>...</pre>` blocks in html,
-  use predefined names for the different languages that come with Pygments,
   the syntax highlighter.

   .. code-block:: rst

      .. code-block:: bash

         export FOO="bar"

   **How it looks**

   .. code-block:: bash

      export FOO="bar"


----

Custom text role
================

You are free to define additional text roles for an individual pages as you like. 
Make use of the `role directive <http://docutils.sourceforge.net/docs/ref/rst/directives.html#role>`__.

For example, you want a custom role ``haskell``? Define that role as derivative of ``code``:

.. code-block:: rst

   .. role:: haskell(code)

You may then write:

.. code-block:: rst

   Here is some :haskell:`haskell inline code` in the sentence.

The immediate advantage will be that you can explicitly markup your source code semantically and declare snippets to be ``haskell``.
The visual appearance will be that of ``code`` until a special css class has been defined.

Look at this HTML to under stand the technical background:

.. code-block:: html

   <code class="code haskell docutils literal">
      <span class="pre">haskell inline code</span>
   </code>

.. role:: html(code)
   :language: html

A default styling for :html:`class="code"` exists and is in effect until
overridden by a special styling :html:`class="code.haskell"` that needs to
be defined.

Another example
---------------

Applying CSS to custom text roles. This example demonstrate a custom role to add colour span to some text.

Within the ``.rst`` file, define the custom role, and applying the role in some text:

.. code-block:: rst

   .. role:: green

   An example of using :green:`interpreted text`

In order to have the ``interpreted text`` coloured in green, we can add a style class definition in CSS

.. code-block:: css

   /* in _static/css/my_theme.css */

   .green {
      color:green;
   }

**How it looks**

.. role:: green

An example of using :green:`interpreted text`

.. note:: 

   Adding CSS style to custom role would require to modify the style sheet for this documentation. 
   Please enquire the :ref:`maintainers <team-doc-maintainers>` before doing so.

