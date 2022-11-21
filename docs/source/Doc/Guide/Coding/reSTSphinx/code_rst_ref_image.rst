.. _code-rst-ref-image:

======
Images
======

Image
=====

Use the ``.. image::`` directive followed by path to source image to display a simple picture.

.. code-block:: rst

   .. image:: picture.png

Optional parameters:

``:alt:``
  
   Alternate text, a short discription of the image, displayed by applications that cannot display images

``:height:``
  
   Image height in pixels, used to reserve space or scale the image vertically. When the ``scale`` option is also specified, they are combined.

   For example, a height of 200 and a scale of 50 is equivalent to a height of 100 with no scale.

``:width:``
  
   Image width in pixels, used to reserve space or scale the image horizontally. As with ``height`` above, when the ``scale`` option is also specified, they are combined.

``:scale:``
  
   The uniform scaling factor of the image, in percentage. "100" means full-size, and is equivalent to omitting the ``scale`` option.

``:align:``

   The alignment of the image, equivalent to the HTML ``<img>`` tag's "align" attribute. Available options: ``left``, ``center``, ``right``.

``:target``

   Makes the image into a hyperlink reference. The option argument may be a URI (relative or absolute), or a reference name.

``:class``

   Set a "class" attribute value on the image element.

.. code-block:: rst

   .. image:: ../../../../Asset/rris-home.jpeg
      :alt: RRIS front door image
      :scale: 20
      :align: left
      :target: https://www.ntu.edu.sg/rris

.. image:: ../../../../Asset/rris-home.jpeg
   :alt: RRIS front door
   :scale: 20
   :align: center
   :target: https://www.ntu.edu.sg/rris

----

Figure
======

Use ``.. figure::`` to add a caption to the image.

The figure directive supports all of the options of the `Image`_ directive. In addition, the following options are recognized:

``:figwidth:``

   The width of the figure in pixels, to limit the horizontal space used.

   This option does not scale the included image; use the ``:width:``, ``:height:``, or ``:scale:`` image option for that.

   .. code-block:: text

      +---------------------------+
      |        figure             |
      |                           |
      |<------ figwidth --------->|
      |                           |
      |  +---------------------+  |
      |  |     image           |  |
      |  |                     |  |
      |  |<--- width --------->|  |
      |  +---------------------+  |
      |                           |
      |The figure's caption should|
      |wrap at this width.        |
      +---------------------------+

``:figclass:``

   Set a "class" attribute value on the figure element.

.. figure:: /Asset/rris-home.jpeg
   :figwidth: 250
   :scale: 10
   :alt: RRIS front door figure

   Welcome to Rehabilitation Research Institute of Singapore

----

Inline image
============

Inline images can be defined with an `Image`_ directive in a `substitution definition <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions>`__.

.. code-block:: rst

   Click this icon |rris icon| to go to RRIS website.

   .. |rris icon| image:: /Asset/rris-logo.jpeg
      :target: https://www.ntu.edu.sg/rris
      :height: 40
      :width: 40

Click this icon |rris icon| to go to RRIS website.

.. |rris icon| image:: /Asset/rris-logo.jpeg
   :target: https://www.ntu.edu.sg/rris
   :height: 40
   :width: 40
