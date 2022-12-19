.. include:: /includes.rst.txt
.. _ros-ros-pkg-structure:

=====================
ROS Package Structure
=====================

This page describes general guidelines for structuring ROS packages. For ROS coding guidelines, please refer to :ref:`code-cppros` and :ref:`code-pyros`.

----

C++ packages
============

Package structure
-----------------

TODO

Naming conventions
------------------

TODO

----

.. _ros-ros-pkg-structure-python:

Python packages
===============

Package structure
-----------------
ROS Python packages should have the following structure:

.. code-block:: none

   sample_pkg/
   ├── scripts
   │   └── sample_ros_node.py
   ├── src
   │   └── sample_python_module
   │       ├── python_sub_module
   │       │   ├── __init__.py
   │       │   └── sub_class.py
   │       ├── __init__.py
   │       ├── main.py
   │       └── sample_class.py
   ├── CMakeLists.txt
   ├── LICENSE
   ├── package.xml
   ├── README.md
   └── setup.py


.. note::

   Note that standard convention is to name the Python module (sample_python_module) the same as the ROS package name (sample_pkg). 
   They are named differently here for clarity.


* Place python nodes in the :dir:`scripts` folder.

* Python nodes have to be given execute permisions with ``chmod``
  
   .. code-block:: text
      
      chmod +x scripts/sample_ros_node.py


* Place python modules and submodules under :dir:`src` folder.
  
   - Python requires each module to have an ``__init__.py`` file.

Naming conventions
------------------
- Standard convention is to name the Python module the same as the ROS package name.

   .. note::

      Note that in the example package above, the ROS package name and Python module names are named differently for clarity.

- ROS node name should be the same as the script name.
- All folder names and file names are **camel_cased**.
   
----

Common files
============

These common files should be included in all RRIS's ROS packages.

``LICENSE``
   RRIS proprietary license file must be included in every package.

``README.md``
   A readme describing the package, installation, nodes, parameters, etc. 
   
   We have the templates of readme at TODO.

``package.xml``
   The package manifest is an XML file called ``package.xml`` that must be included with any catkin-compliant package's root folder.

   Fill in the following required tags accordingly:

   .. code-block:: xml

      <maintainer email="email@todo.todo">name</maintainer>
      <license>Proprietary</license>


----

Other directories
=================

Regardless of C++ or Python ROS packages, the following naming conventions for common directories are preferred.

:dir:`config`
   Configuration files like ``yaml``, ``json``, etc. 

:dir:`data`
   Input/Output data to be stored within :dir:`data` by default.
   
:dir:`launch`
   Directory for ROS launch files.

:dir:`rviz`
   Any RViz configuration files can be stored within :dir:`rviz`

Hence, a common ROS package structure may look similar:

.. tabs:: 

   .. code-tab:: none C++

      sample_pkg/
      ├── config/
      ├── data/
      ├── include/
      ├── launch/
      ├── rviz/
      ├── src/
      ├── CMakeLists.txt
      ├── LICENSE
      ├── package.xml
      └── README.md

   .. code-tab:: none Python

      sample_pkg/
      ├── config/
      ├── data/
      ├── launch/
      ├── rviz/
      ├── scripts/
      ├── src/
      ├── CMakeLists.txt
      ├── LICENSE
      ├── package.xml
      ├── README.md
      └── setup.py


----

References
==========
1. `ROS PyStyleGuide`_
2. `ROS docs (Jade)`_
3. `Understanding how ROS sources Python modules`_

.. _ROS PyStyleGuide: http://wiki.ros.org/PyStyleGuide
.. _ROS docs (Jade): http://docs.ros.org/en/jade/api/catkin/html/howto/format2/installing_python.html
.. _Understanding how ROS sources Python modules: http://www.artificialhumancompanions.com/structure-python-based-ros-package/#:~:text=Python%2Dbased%20ROS%20packages%20will,it%20isn't%20already%20running.