.. include:: /includes.rst.txt

===============
Design Elements
===============

This documentation utilizes ``sphinx-design`` extension to enable responsive web components.

----

Grids
=====

Grids are based on a 12 column system, which can adapt to the size of the viewing screen.

.. code-block:: rst

   .. grid:: 1 2 3 4
      :outline:

      .. grid-item::

         A

      .. grid-item::

         B

      .. grid-item::

         C

      .. grid-item::

         D

.. grid:: 1 2 3 4
   :outline:

   .. grid-item::

      A

   .. grid-item::

      B

   .. grid-item::

      C

   .. grid-item::

      D

.. seealso:: 

   `Grids <https://sphinx-design.readthedocs.io/en/rtd-theme/grids.html>`__

----

Cards
=====

Cards contain content and actions about a single subject. 

A card is a flexible and extensible content container, it can be formatted with components including headers and footers, titles and images.

.. code-block:: rst

   .. card:: Card Title

      Card content

.. card:: Card Title

   Card content

.. seealso:: 

   `Cards <https://sphinx-design.readthedocs.io/en/rtd-theme/cards.html>`__

----

Dropdowns
=========

Dropdowns can be used to toggle, content and show it only when a user clicks on the header panel.

.. code-block:: rst

   .. dropdown:: Dropdown title

      Dropdown content

.. dropdown:: Dropdown title

   Dropdown content

.. seealso:: 

   `Dropdowns <https://sphinx-design.readthedocs.io/en/rtd-theme/dropdowns.html>`__

----

Inline icons
============

Inline icon roles are available for the `GitHub octicon <https://primer.style/octicons/>`__.

Octicon icons are added as SVG's directly into the page with the :rst:`octicon` role.

By default the icon will be of height ``1em`` (i.e. the height of the font). 
A specific height can be set after a semi-colon ``;`` with units of either ``px``, ``em`` or ``rem``. 
Additional CSS classes can also be added to the SVG after a second semi-colon ``;`` delimiter.

For example:

.. tabs:: 

   .. code-tab:: rst

      A coloured icon :octicon:`report;1em;sd-text-info`, some more text.

   .. tab:: output

      A coloured icon :octicon:`report;1em;sd-text-info`, some more text.

.. seealso:: 

   More available inline icons can be found at `oction icons <https://sphinx-design.readthedocs.io/en/rtd-theme/badges_buttons.html#octicon-icons>`__.

.. note:: 

   Instead of using :rst:`octicon` directive, one can also :rst:`.. include:: /includes/rst.txt`, then use :rst:`icon` directive.

----

Article-info
============

This directive is used to display a block of information about an article, normally positioned just below the title of the article (shown below with non-standard outline).

.. code-block:: rst

   .. article-info::
      :avatar: /Asset/rris-logo.jpeg
      :avatar-link: https://rris-doc-testing.readthedocs.io/en/latest/
      :avatar-outline: muted
      :author: RRIS documentation contributors
      :date: 1 Jan 2023
      :read-time: 3 hour read
      :class-container: sd-p-2 sd-outline-muted sd-rounded-1

.. article-info::
   :avatar: /Asset/rris-logo.jpeg
   :avatar-link: https://rris-doc-testing.readthedocs.io/en/latest/
   :avatar-outline: muted
   :author: RRIS documentation contributors
   :date: 1 Jan 2023
   :read-time: 3 hour read
   :class-container: sd-p-2 sd-outline-muted sd-rounded-1

----

Reference
=========

* `sphinx-design GitHub <https://github.com/executablebooks/sphinx-design>`__
* `sphinx-design documentation <https://sphinx-design.readthedocs.io/en/rtd-theme/index.html>`__