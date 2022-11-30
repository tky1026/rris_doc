.. include:: /includes.rst.txt
.. _code-rst-ref-tab:

====
Tabs
====

Create tabbed content in Sphinx documentation when building HTML.

Tabs provide a compact way to present a topic from different perspectives, with each perspective presented in a tab. 
When the reader changes tabs, this change is synchronized in all tab content elements.

----

Syntax
======

All sphinx-tabs use the :rst:`.. tabs::` directive to define a tab set. There are mainly 3 different tab directive:

* `Basic tabs`_
* `Grouped tabs`_
* `Code tabs`_

----

Basic tabs
----------

Basic tabs are added using the :rst:`.. tab::` directive, which takes the tab’s label as an argument:

The contents of each tab can be displayed by clicking on the tab that you wish to show. Clicking on the tab that is currently open will hide the tab's content, leaving only the tab set labels visible.

.. code-block:: rst

   .. tabs::

      .. tab:: Apples

         Apples are green, or sometimes red.

      .. tab:: Pears

         Pears are green.

      .. tab:: Oranges

         Oranges are orange.

.. tabs::

   .. tab:: Apples

      Apples are green, or sometimes red.

   .. tab:: Pears

      Pears are green.

   .. tab:: Oranges

      Oranges are orange.

Tabs can also be nested inside one another

.. code-block:: rst

   .. tabs::

      .. tab:: Stars

         .. tabs::

            .. tab:: The Sun

               The closest star to us.

            .. tab:: Proxima Centauri

               The second closest star to us.

            .. tab:: Polaris

               The North Star.

      .. tab:: Moons

         .. tabs::

            .. tab:: The Moon

               Orbits the Earth

            .. tab:: Titan

               Orbits Jupiter

.. tabs::

   .. tab:: Stars

      .. tabs::

         .. tab:: The Sun

            The closest star to us.

         .. tab:: Proxima Centauri

            The second closest star to us.

         .. tab:: Polaris

            The North Star.

   .. tab:: Moons

      .. tabs::

         .. tab:: The Moon

            Orbits the Earth

         .. tab:: Titan

            Orbits Jupiter

----

Grouped tabs
------------

Tabs can be grouped, so that changing the current tab in one tabset changes the current tab in all other tabsets containing a tab with a matching label. 
For example:

.. code-block:: rst

   .. tabs::

      .. group-tab:: Linux

         Linux Line 1

      .. group-tab:: Mac OSX

         Mac OSX Line 1

      .. group-tab:: Windows

         Windows Line 1

   .. tabs::

      .. group-tab:: Linux

         Linux Line 1

      .. group-tab:: Mac OSX

         Mac OSX Line 1

      .. group-tab:: Windows

         Windows Line 1

.. tabs::

   .. group-tab:: Linux

      Linux Line 1

   .. group-tab:: Mac OSX

      Mac OSX Line 1

   .. group-tab:: Windows

      Windows Line 1

.. tabs::

   .. group-tab:: Linux

      Linux Line 2

   .. group-tab:: Mac OSX

      Mac OSX Line 2

   .. group-tab:: Windows

      Windows Line 2

The tab selection in these groups is synchronised, so selecting the ‘Linux’ tab of one tab set will open the ‘Linux’ tab contents in all tab sets on the current page.

----

Code tabs
---------

A common use of group tabs is to show code examples in multiple programming languages. The :rst:`.. code-tab::` directive creates a group tab and treats the tab content as a code-block.

The first argument to a :rst:`.. code-tab::` is the name of the language to use for code highlighting, while the optional second argument is a custom label for the tab. 
By default, the tab is labelled using the lexer name. The tab label is used to group tabs, so the same custom label should be used to group related tabs.

.. code-block:: rst

   .. tabs::

      .. code-tab:: c

            C Main Function

      .. code-tab:: c++

            C++ Main Function

      .. code-tab:: py

            Python Main Function

      .. code-tab:: java

            Java Main Function

      .. code-tab:: julia

            Julia Main Function

      .. code-tab:: fortran

            Fortran Main Function

      .. code-tab:: r R

            R Main Function

   .. tabs::

      .. code-tab:: c

            int main(const int argc, const char **argv) {
               return 0;
            }

      .. code-tab:: c++

            int main(const int argc, const char **argv) {
               return 0;
            }

      .. code-tab:: py

            def main():
               return

      .. code-tab:: java

            class Main {
                  public static void main(String[] args) {
               }
            }

      .. code-tab:: julia

            function main()
            end

      .. code-tab:: fortran

            PROGRAM main
            END PROGRAM main

      .. code-tab:: r R

            main <- function() {
               return(0)
            }

.. tabs::

   .. code-tab:: c

         C Main Function

   .. code-tab:: c++

         C++ Main Function

   .. code-tab:: py

         Python Main Function

   .. code-tab:: java

         Java Main Function

   .. code-tab:: julia

         Julia Main Function

   .. code-tab:: fortran

         Fortran Main Function

   .. code-tab:: r R

         R Main Function

.. tabs::

   .. code-tab:: c

         int main(const int argc, const char **argv) {
            return 0;
         }

   .. code-tab:: c++

         int main(const int argc, const char **argv) {
            return 0;
         }

   .. code-tab:: py

         def main():
            return

   .. code-tab:: java

         class Main {
               public static void main(String[] args) {
            }
         }

   .. code-tab:: julia

         function main()
         end

   .. code-tab:: fortran

         PROGRAM main
         END PROGRAM main

   .. code-tab:: r R

         main <- function() {
            return(0)
         }

----

Reference
=========

- `sphinx-tabs <https://github.com/executablebooks/sphinx-tabs>`__
