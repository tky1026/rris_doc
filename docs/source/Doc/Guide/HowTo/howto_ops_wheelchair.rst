.. _howto-ops-wheelchair:

=========================
Operate Wheelchair (MRCA)
=========================

This guide covers how to operate the wheelchair and how to configure your laptop for ROS and SSH to the Intel NUC on the wheelchair.

Power-on Wheelchair
===================

#. Switch on the main power.
#. Turn on Intel NUC by pressing the power button.
#. Turn on the switch to motor.
#. Make sure the motor is engaged.
#. Reset STM32 (optional).

----

Connect through LAN cable
=========================

Configure laptop
----------------

#. Add this ip address to ``etc/hosts``

   .. code-block:: text

      10.42.0.63     scatwheel-NUC11PAHi5

#. Configure wired network
#. Export ``ROS_IP`` and ``ROS_MASTER_URI`` to ``~/.bashrc``

   .. code-block:: bash

      export ROS_IP=10.42.0.1
      export ROS_MASTER_URI=http://10.42.0.63:11311

#. Check the connectivity by

   .. code-block:: shell

      ping scatwheel-NUC11PAHi5

----

Connect through Wi-Fi
=====================

TODO

----

Launch wheelchair hardware
==========================

In every terminal, SSH to Intel NUC by

.. code-block:: shell

   ssh scatwheel@scatwheel-NUC11PAHi5

#. Start wheelchair hardware

   For the very first time since power-on before launching the hardware, give port permission for the sensors using the following command:

   .. code-block:: shell

      enableUSB

   Launch the hardware

   .. code-block:: shell

      roslaunch SharedControlWheelchair_demos hardware.launch joystick_control:=true

#. Run command velocity multiplexer node (for manual control)

   .. code-block:: shell

      rosrun door_cmd_vel_mux door_cmd_vel_mux_node

----

Tasks
=====

Shared control
--------------

#. Start wheelchair hardware

   .. code-block:: shell

      roslaunch SharedControlWheelchair_demos hardware.launch joystick_control:=true

#. Start ``move_base``

   .. code-block:: shell

      roslaunch scat_move_base move_base.launch

#. Start ``gmapping``

   .. code-block:: shell

      roslaunch mapping_launch gmapping.launch

#. Run ``shared_dwa``

   .. code-block:: shell

      roslaunch shared_dwa shared_dwa.launch

#. Run ``path_belief_update``

   .. code-block:: 

      roslaunch path_belief_update belief_update.launch