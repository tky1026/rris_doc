.. include:: /includes.rst.txt
.. _code-rst-ref-video:

======
Videos
======

.. note:: 
   Currently, only support embedding of YouTube videos.

----

Embed YouTube videos
--------------------

1. Get the YouTube id

   Example: The URL is :samp:`https://www.youtube.com/watch?v={4HYztlv5enY}`.

   The id is the text after ``v=`` and up to the next ``&`` or the end of the URL.

   Here: ``4HYztlv5enY``.

2. Embed the video using the id

   .. code-block:: rst

      .. youtube:: 4HYztlv5enY

   .. youtube:: 4HYztlv5enY

   By default, the embedded video will be sized for 720p content. 
   To control this, the parameters ``aspect``, ``width``, and ``height`` may optionally be provided:

   .. code-block:: rst

      .. youtube:: 4HYztlv5enY
         :width: 640
         :height: 480

      .. youtube:: 4HYztlv5enY
         :aspect: 4:3

      .. youtube:: 4HYztlv5enY
         :width: 100%

      .. youtube:: 4HYztlv5enY
         :height: 200px

   To set the alignment of the embedded video’s iframe in the HTML output, an optional ``align`` parameter can be specified, similar to the :rst:`image` directive:

   .. code-block:: rst

      .. youtube:: 4HYztlv5enY
         :align: center


----

Reference
---------

* `sphinxcontrib.youtube <https://github.com/sphinx-contrib/youtube>`__