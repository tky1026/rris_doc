.. include:: /includes.rst.txt

==============
File Structure
==============

This page explains the general file structure of this documentation.

General
=======

All content related files must resides within :dir:`source` folder.

Further conventions are:

* reST files have the extension ``.rst``.
* Markdown files have the extension ``.md``.
* Included reST files have the extension ``.rst.txt``.
* Use **CamelCase** for directory and **camel_case** for file names, for example: ``Documentation/MyProject/file_a.rst``.
* All documenation files are recommended to named with appropriate prefixes.

These conventions pave the way for the documentation style and organization, they are being preferred for several reasons.

----

Top level structure
===================

Files and folders within :dir:`source` defines the structure of how the documentation being rendered.

.. important:: 
   Please do not modify anything at this level. 
   Contributors are only to contribute contents belong to :dir:`source/Doc`.
   
   Approach :ref:`maintainers <team-doc-maintainers>` for more info.

.. code-block:: 

   source/
   ├── Asset
   ├── Doc
   ├── _static
   ├── conf.py
   ├── includes.rst.txt
   ├── index.rst
   └── TOC.rst

**Asset**
   The :dir:`Asset` folder contains general documentation-wide materials.

**Doc**
   All documenation files are to reside within :dir:`Doc` folder. See `Documentation`_ for details.

**_static**
   Contains custom defined CSS stylesheet at :dir:`_static/css/my_theme.css`.

**conf.py**
   Configuration file for the Sphinx documentation builder.

**includes.rst.txt**
   Defined general custom text roles that can be included in documentation file. 
   To include this file, put :code:`.. include:: /includes.rst.txt` at the very top of the documentation file.

**index.rst**
   The documentation index file at :dir:`index.rst` is the starting point of the main documentation.
   It contains general information about the documentation, a summary of its purpose and a table of contents that refers to further pages.

   All variables of the \|name\| pattern are automatically replaced by the Sphinx when being rendered.

**TOC.rst**
   Top level toctree that defines the documentation structure.

----

Documentation
=============

All documentation files resides within :dir:`source/Doc`. 
The organization of this directory has been categorized into ...

Naming conventions

**_Templates**
   .txt

**Guide**




TODO