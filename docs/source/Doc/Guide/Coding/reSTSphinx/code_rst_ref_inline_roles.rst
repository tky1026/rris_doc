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

   ================== ================================================= ============================================ ===
   Role               Source                                            Output                                       Note
   ================== ================================================= ============================================ ===
   emphasis           ``:emphasis:`text`, *text*``                      :emphasis:`text`, *text*
   literal            ``:literal:`\ \ abc```                            :literal:`\ \ abc`
   literal            ``:literal:`text`, ''text''`` (backticks!)        :literal:`text`, ``text``
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
