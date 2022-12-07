.. _ros-ros-pkg-structure:

=====================
ROS Package Structure
=====================

This page describes general guidelines for structuring ROS packages. For ROS coding guidelines, please refer to :ref:`code-cppros` and :ref:`code-pyros`.

----

.. _ros-ros-pkg-structure-python:

Python Package
==============

Package Structure
-----------------
ROS Python packages should have the following structure:

.. code-block:: text

    sample_pkg
    |- launch/
        |- sample_launch_file.launch
    |- scripts/
        |- sample_ros_node.py
    |- rviz/
        |- cfg.rviz
    |- src/
        |- sample_python_module/
        |- __init__.py
        |- main.py
        |- sample_class.py
        |- python_sub_module/
            |- __init__.py
            |- sub_class.py
    - CMakeLists.txt
    - LICENSE
    - package.xml
    - README.md
    - setup.py


.. note::

    Note that standard convention is to name the Python module (sample_python_module) the same as the ROS package name (sample_pkg). They are named differently here for clarity.


* Place python nodes in the ``scripts/`` folder.

* Python nodes have to be given execute permisions with chmod
    .. code-block:: text
        
        chmod +x scripts/sample_ros_node.py


* Place python modules and submodules under ``src/`` folder.
   - Python requires each module to have an ``__init__.py`` file.

* Any rviz files can be stored in the ``rviz/`` folder.

Naming conventions
~~~~~~~~~~~~~~~~~~
   - Standard convention is to name the Python module the same as the ROS package name.
    
    .. note::

        Note that in this package, the ROS package name and Python module names are named differently for clarity.
   
   - ROS node name should be the same as the script name.
   

References
----------
1. `ROS PyStyleGuide`_
2. `ROS docs (Jade)`_
3. `Understanding how ROS sources Python modules`_

.. _ROS PyStyleGuide: http://wiki.ros.org/PyStyleGuide
.. _ROS docs (Jade): http://docs.ros.org/en/jade/api/catkin/html/howto/format2/installing_python.html
.. _Understanding how ROS sources Python modules: http://www.artificialhumancompanions.com/structure-python-based-ros-package/#:~:text=Python%2Dbased%20ROS%20packages%20will,it%20isn't%20already%20running.