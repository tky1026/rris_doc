.. _code-cpp:

===
C++
===

This page describes general guidelines for C++ coding. For C++ with ROS, please refer to :ref:`code-cppros`.

----

Style guide
===========

In general, we follow `Google C++ Style Guide`_, as it is a well-written document on the topic at hand.

There are several points that we like to highlight as mentioned below. 

The styles emphasized below are prefered by our team, please follow whenever possible in order to be consistent throughout our codebase.

Do note that some of the below-mentioned styles may contradict with the `Google C++ Style Guide`_, follow what is being mentioned below instead.

File names
----------

* Filenames should be all lowercase and include underscores ``_`` only, as **camel_case**. Do not use whitespaces or dashes ``-`` for filenames.
* C++ source files must end with extension ``.cpp``, and ``.hpp`` for header files.
* Use only ``.c`` and ``.h`` for C files.

Indentation
-----------

* Use **4 spaces** indentation at a time.
* Use only **spaces** for indentation. Do not use tabs character.
  
   .. note:: 
      Set editor to emit spaces when hitting the :kbd:`Tab` key.

* The contents of a namespace are not indented. 

   .. code-block:: c++

      // In the .hpp file
      namespace mynamespace 
      {
      // All declarations are within the namespace scope.
      // Notice the lack of indentation.
      class MyClass 
      {
          public:
              ...
              void Foo();
      };

      }  // namespace mynamespace

   .. code-block:: c++

      // In the .cpp file
      namespace mynamespace 
      {
      // Definition of functions is within scope of the namespace.
      void MyClass::Foo() 
      {
          ...
      }

      }  // namespace mynamespace

Braces
------

* Braces, both open and close, go on their own lines (no "cuddled braces")

   .. code-block:: c++

      if(a < b)
      {
          // do stuff
      }
      else
      {
          // do other stuff
      }

* Braces can be omitted if the enclosed block is a single-line statement

   .. code-block:: c++

      if (a < b)
          x = 2 * a + b;

Spaces
------

* For conditional statements and loop control statements, always put one space between the statement keyword and the opening parenthesis, 
  but no spaces between the parentheses and the condition or initializer.

   .. code-block:: c++
      
      if (condition)
      {
          DoFirst();
          DoSecond();
      }
      else if (CheckTerm(); a != 3)
          DoThird();
      else
          DoNothing();

* Put one space between operators and variables, except increment ``++`` and decrement ``--``.

   .. code-block:: c++

      int sum = val_1 + val_2 + (val_3 * val_4);
      if ((a < b) && c != d)
      {
          DoSomething();
          i++;
      }

Using namespace std
-------------------

Avoid :code:`using namespace std` at all. It is considered a bad practice in C++ coding.

The whole point of namespaces is to prevent namespace collisions between two independently developed piles of code. 
The ``using`` directive effectively dumps one namespace into another, which can subvert that goal, considering the ``std`` namespace is huge.

Instead of importing entire namespaces, import a truncated namespace:

.. code-block:: c++

   #include <chrono>
   #include <iostream>
   
   // Import only the chrono namespace under std
   using std::chrono;
   
   auto start = high_performance_clock::now();
   
   // Do Something
   auto stop = high_performance_clock::now();
   auto duration duration_cast<milliseconds>(stop - start);

Or use the ``using`` statement for importing a single identifier only:

.. code-block:: c++

   using std::cout;
   cout << "Hello World\n";

If you still insisted to import entire namespaces, try to do so inside functions or limited scope and not in global scope.

.. code-block:: c++

   #include <iostream>

   // Avoid this
   using namespace std;

   void foo()
   {
       // Inside function
       // Use the import statement inside limited scope
       using namespace std;

       // Proceed with function
   }

----

Non-conforming code
===================

C++ code that was written prior to the release of this style guide may not conform to this guide.
The following advice is intended for the developer working with non-conforming code:

* All new C++ code should conform to this guide.
* Unless you have copious free time, don't undertake converting the existing codebase to conform to this guide. 
* If you are author of a non-conforming package, try to find time to update the code to conform. 
* If you are doing minor edits to a non-conforming package, follow the existing stylistic conventions in that package (if any). Don't mix styles. 
* If you are doing major work on a non-conforming package, take the opportunity to re-style it to conform to this guide. 

----

Resources
=========

* `Google C++ Style Guide`_

.. _Google C++ Style Guide: https://google.github.io/styleguide/cppguide.html

