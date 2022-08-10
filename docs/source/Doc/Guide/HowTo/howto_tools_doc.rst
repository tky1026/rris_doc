.. _howto-tools-doc:

======================
Tools for Editing reST
======================

When editing reST files locally, you should use an editor or IDE with good support for syntax highlighting and marking errors in reST.
We will cover some IDEs here, that may be useful if you edit locally.

* :ref:`configure-vscode` comes with plugins for reStructuredText.

Other alternatives can be found in the "Free Editors" section of `StackOverflow: reStructuredText tool support <https://stackoverflow.com/questions/2746692/restructuredtext-tool-support/2747041#2747041>`_.

The editor or IDE should ideally have the following features:

* syntax highlighting for reST
* show syntax errors
* provide possibility to use (configurable) code snippets for easy insertion of directives
* provide keyboard shortcuts and configurable commands
* built in spell checking (English)

----

.. _configure-vscode:

Visual Studio Code
==================

Plugins
-------

reStructuredText
~~~~~~~~~~~~~~~~

reStructuredText language support.

**Installation**

Launch VS Code Quick Open (:kbd:`Ctrl` + :kbd:`P`), paste the following command, and press enter.

.. code-block:: bash

   ext install lextudio.restructuredtext


reStructuredText Syntax highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Syntax highlighting and document symbols for reStructuredText.

**Installation**

Launch VS Code Quick Open (:kbd:`Ctrl` + :kbd:`P`), paste the following command, and press enter.

.. code-block:: bash

   ext install trond-snekvik.simple-rst

Configurations
--------------

Editor tab size
~~~~~~~~~~~~~~~

reST indentation level is **3 spaces** as mentioned here :ref:`doc-cgl-rest-indent`. 

Configure VSCode editor to insert 3 spaces when :kbd:`Tab` is pressed for ``.rst`` files.

#. Open the Command Palette (:kbd:`Ctrl` + :kbd:`Shift` + :kbd:`P`)
#. Search for the ``Preferences: Configure Language Specific Settings...``
#. Select the language ``reStructuredText``
#. Add ``"editor.tabSize": 3"`` to the corresponding JSON object
#. Save file

The ``settings.json`` should have the corresponding JSON object:

.. code-block:: json

   {
      "[restructuredtext]": {
         "editor.tabSize": 3
      }
   }