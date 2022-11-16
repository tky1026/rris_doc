===========================
Documentation Writing Style
===========================

By using this style guide we ensure that all written texts have the same general grammar and writing style — even when many people contribute.

Style guides can become very, very long. We keep this guide short to make sure you read it, but it means we only cover the most important topics. 
If you would like to read more about style and usage, check out `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_.

----

Writing style
=============

Spelling
--------

We write using British (UK) spelling, as Singapore uses the British English in the spelling system. That means, we write *colour*, rather than *color*, 
and use *-yse* endings, rather than *-yze* english, i.e. *paralyse* vs *paralyze*.

.. _doc-sgl-title-case:

Title case
----------

We capitalize all principal words of a title, including the first and the last words. We do not capitalize articles, prepositions or conjunctions that have fewer than four letters, such as: 

* a
* an
* and
* at
* but
* by
* for
* in
* nor
* of
* on
* or
* so
* the
* to
* up
* yet

For reference, check the "AP" capitalization at `capitalizemytitle.com <https://capitalizemytitle.com/>`_.

**Examples:**

   Rehabilitation Research Institute of Singapore

   How to Configure Your Development Environment

.. _doc-sgl-sentence-case:

Sentence case
-------------

Sentence case is a capitalization style in which only the first word of a sentence and proper nouns are capitalized, with the rest of the words in lowercase.

We use sentence case in this documentation for all headings and subheadings.

**Examples:**

   There is rain in the forecast this week in New York City.

Numbers
-------

Numbers are written using a dot “.” as decimal separator, while comma “,” as thousands separator is optional. We normally use max two decimals. The number of decimals used should reflect the text's need for accuracy.

A zero should be included before the dot in numbers less than 1.0.

Very large integer numbers (those above 999,999), if not representing actual raw data values, should be written using million, billion, or trillion, replacing the last six or nine digits.

Numbers less than ten are spelt out, unless they are dates or part of a list with larger values.

**Examples:**

   The difference is less than 0.5.

   The experiment has 12,481 participants.

   The function nesting limit is set to 1000.

   That is exactly 99.96% true.

   The file has more than 30 million lines.

   We need at least five developers.

Currency
--------

Currency values are written using the three-letter ISO code, followed by a space, followed by the value written according to our number style. 

Currency symbols, such as € and $ can be used as a shortened form. They are placed in front of the value, with no space separating them

**Examples:**

   The PC cost $3500.

   We made a profit of exactly SGD 25,060.17.

Dates
-----

We prefer the internation date style: **day, month, year**. 
Days are written in digits and years are always written in four digits.
We always write the month name as dates wirtten as numbers only will always cause confusion.
For example 1/11/2011, people might understand it as 1-Nov or 11-Jan.

Month names are normally written in full, but can be abbreviated if needed: 
Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

**Examples:**

   25 December 2018

   12 Sep 2019

Comma in Lists
--------------

The Oxford comma (also known as the ‘serial comma’ in the US) is a comma placed before the last item in a list of three or more things. Sometimes, this can help ensure clarity.

Typically, in British English, we only use an Oxford comma when a list would be unclear without one, such as in the example sentence below:

   I’m going out with my brothers, Tim and Dave.

This sentence is ambiguous. Is it a list of three items? Or are my brothers named Tim and Dave? We can clarify this instantly by adding an Oxford comma before ‘Dave’, as shown below:

   I’m going out with my brothers, Tim, and Dave.

Quotes
------

Exact quotes are written between double quotation marks. Quotes within quotes are written between single quotes. 
For long quoted sections, we use indented block quotations without quotation marks. 
Periods and commas are placed within quotation marks. Colons and semicolons are placed outside of quotation marks.

**Examples:**

   I felt great each time he said “I love Singapore.”

   “I love Singapore,” he said enthusiastically.

   The poem goes:

      Roses are red

      Violets are blue

Emphasis
--------

We use *italics* for emphasis on single words or compound words. **Bold** text is used to increase visibility on words, compound words, parts of sentences, and sentences. We *never* use underlined text.

**Examples:**

   This text is *not* underlined for emphasis.

   This year’s **accounts are looking very good**.

----

.. _doc-sgl-rules-title:

Rules for titles & section headers
==================================

We use :ref:`title case <doc-sgl-title-case>` for document title:

  * Capitalize all principal world of a title.
  * Do not capitalize articles, prepositions or conjunctions.

Use :ref:`sentence case <doc-sgl-sentence-case>` for section headers:

  * The first word is capitalized.
  * All other words are spelled as they would be spelled elsewhere; Proper nouns are capitalized, all other words written in lowercase.

The rationale of enforcing this rule is to ensure clear differentiation between a title of a document and the sections within the document.

In reST, headers are created by underlining / overlining with (``====``, ``----``, etc.) as described in :ref:`code-rst-ref-headline-section`:

.. code-block:: rst

   =================
   This Is the Title
   =================

   This is heading level 1
   =======================

----

Rules for buttons & links
=========================

The same spelling rules as in the title apply to buttons and links.

----

Rules for referring to GUI elements
===================================

If the text refers to terms used in the GUI (for example a clickpath for selecting something from the menu is described), the exact spelling used in the GUI should be used, and use text role ``guilabel`` on it, for example :guilabel:`File > Open` or “click on :guilabel:`TOOLS > Extensions`”.

See :ref:`doc-cgl-refer-gui` for information about how to use reST markup for this.

----

Rules for plain text
====================

Compound words
--------------

Compound words (or compounds) are words that have been glued together from one or more separate words to create a new term with a new meaning as in backyard (back and yard) or New Age (new and age).

But how should they be spelled? Backend, back-end or back end? Site package or sitepackage?

.. important:: 

   If a spelling has been explicitly defined in the :ref:`spelling-term-glossary`, please use that spelling.

How can you decide for yourself in other edge cases?

.. tip:: 

   If in doubt, use what is commonly used in the documentation. If you see inconsistencies between documentation and English dictionaries or within the documentation, raise the issue in `GitHub issues`_.

.. _`GitHub issues`: https://github.com/tky1026/rris_doc/issues

Capitalization
--------------

#. If a word has special spelling, for example a special word like TypeScript or an acronym like PHP, this spelling is applied.
#. :ref:`Proper nouns and brand names <doc-sgl-brand-names>` are capitalized, for example Docker.
#. Most other words begin with a lowercase letter.

There are some edge cases and some terms are not spelled consistently throughout various resources. Often it also depends on the context. 
Capitalization may change over the course of time, for example see `The Associated Press style guide will no longer capitalize ‘internet’ <https://www.theverge.com/2016/4/2/11352744/ap-style-guide-will-no-longer-capitalize-internet>`_. 
In other texts, “internet” is still capitalized.

For this reason we have put together a :ref:`spelling reference <spelling-term-glossary>` to list some common terms that may be difficult to spell or that are spelled differently in this documentation.

Exceptions for specific terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are some specific terms defined in :ref:`spelling-term-glossary`. If defined, please follow the spelling.

Exceptions for words taken from source code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are using class names, function names, databases tables or fields, configuration options etc, use the spelling that is used in the source code.

Acronyms
--------

Often acronyms are written with capital letters only. If terms are commonly spelled that way, this is how we spell them as well, for example HTML, PHP or LTS. If a specific term has been explicitly defined in the :ref:`spelling-term-glossary`, please use that spelling.

.. _doc-sgl-brand-names:

Proper names, brand names
-------------------------

General rules of the English language apply here:

If `proper names <https://en.wikipedia.org/wiki/Proper_noun>`_ or brand names (for example Coca-Cola) are used in normal text (not headlines), they are capitalized.

These can be countries, names of people, corporations or brand names.

**Examples:**

   * “This manual is designed to be readable by someone with basic UNIX command-line skills, but no previous knowledge of **Git**.”: Git is capitalized, because it is a brand name.
   * **Europe**
   * **Rowan Atkinson** is an **English** actor.

Tools with executables
~~~~~~~~~~~~~~~~~~~~~~

Some tools have a program, which you can run. For example, **Git** has the command line tool ``git``. 
When the documentation explicitly refers to the command ``git``, its appropriate spelling is used, which is lowercase. 
In all other cases, we use capital spelling for Git, because it applies to the rules for :ref:`doc-sgl-brand-names`.

It is also recommended to use backticks **\`** to highlight the commands, like ``cd ~/Desktop``, ``sudo apt-get install``.

The same goes for **Docker**, **Conda**, etc.

----

Spelling & preferred terms reference
====================================
Some specific terms have a special spelling, please refer to :ref:`spelling-term-glossary`.