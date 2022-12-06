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
* Do not use whitespace and hypen ``-`` for filenames, use underscores ``_`` instead.
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
The organization of this directory has been categorized into:

* `Intro`_
* `Project`_
* `Package`_
* `Guide`_
* `Resources`_
* `Other`_
* `Templates`_

Intro
-----

:dir:`Intro` contains only two files:

- ``overview.rst``

   Overview of the project team, and brief description about this documentation.

- ``team.rst``

   Contains team members information, members' reference tag, and documentation maintainers and contributors information.

Project
-------

Project description documentation should resides within :dir:`Project`.

Project documentation should follow :ref:`rsrs_template_project`.

Package
-------

In :dir:`Package` directory, files are further categorized into several directories based on their topics:

- CCloud
- CControl
- CEmbedded
- CExperiment
- CMisc
- CPerception
- CPlanning
- CUserInterface

.. code-block::

   source/Doc/Package/
   └── CTopics
       ├── index.rst
       ├── Packages
       │   ├── pkg_1.rst
       │   ├── pkg_2.rst
       │   └── ...
       └── Tools
           ├── lib_1.rst
           ├── lib_2.rst
           └── ...

**index.rst**
   :rst:`toctree` of the subdirectory.

**Packages**
   ROS packages docmentation goes to :dir:`CTopics/Packages`.
   
   All documentation file should follow :ref:`rsrs_template_package`, and file naming should start with prefix ``pkg_``.

**Tools**
   Non-ROS related topics goes to :dir:`CTopics/Tools`.
   
   Usually documents belongs to this category are further description of some software, third-party libraries, tools etc. 
   
   Hence it is not necessary to follow any templates.

Guide
-----

:dir:`Guide` contains guidelines for documentation, coding guidelines, and serveral other topics.

* Documentation related guide should resides in :dir:`Documentation` and have prefix ``doc_``.
* Coding related guide should resides in :dir:`Coding/<language>` and have prefix ``code_<language>_``.

Resources
---------

:dir:`Resources` contains dataset, publication, learning resources and student related materials.

* FYP related information please refer to :ref:`rsrs_student`.

Other
-----

Other uncategorized topics goes to :dir:`Other`.

Templates
---------

Boilerplates are stored within :dir:`_Templates`.

.. important:: 

   Boilerplate files should end with extension ``.rst.txt``.
