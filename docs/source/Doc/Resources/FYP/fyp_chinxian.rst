====================================================================================
Development of Haptic Feedback Joystick on Powered Wheelchair for Obstacle Avoidance
====================================================================================

:Project title:
   Development of haptic feedback joystick on powered wheelchair for obstacle avoidance

:Academic year:
   2020/21

:Student:
   :ref:`Ang Chin Xian <rris_staff_chinxian>`

:Supervisor:
   Assoc Prof Ang Wei Tech

:Researchers:
   :ref:`Li Lei <rris_staff_lilei>`

:School:
   NTU MAE

:DR-NTU:
   https://hdl.handle.net/10356/150884

:Final report:
   <report-link>

:GitHub:
   <github-link>

:Documentation:
   :ref:`Kuan Yuee <rris_staff_kuanyuee>`

:Latest update:
   17 Nov 2022

----

Haptic joystick is an interface incorporating force feedback to enhance the task performance
and improve reaction time of wheelchair drivers. It is able to help the wheelchair drivers with
visual impairment to compensate for the lack of visual information and raise their situational
awareness by introducing haptic feedback. Most of the joystick design are inefficient in terms
of energy transmission and focus on active force feedback. 

This project presents a development of a 2 degree of freedom (DOF) haptic joystick with direct-drive 
mechanism for efficient energy transmission. The force feedback is powered by 2 high torque direct 
drive brushless DC motor (BLDC) connected in gimbal structure for decoupled mechanism and stiffen control.
The project also focuses on passive force feedback mechanism with the BLDC being
programmed as spring and damper system using proportional-derivative (PD) controller. The
joystick stiffness of the virtual spring would increase based on level of dangerousness
computed by obstacle avoidance algorithms. As user move closer to obstacle, a larger stiffness
would be produced. Thus, preventing user from moving into that particular direction. 

Lastly, three obstacle avoidance algorithms, namely Dynamic Window Approach(DWA), Potential
Field Algorithm(PFA) and Obstacle Dependent Gaussian Potential Field Algorithm(ODG-
PFA), are integrated into the haptic feedback algorithms. An experiment was carried out where
participants are required to drive a series of obstacle course to evaluate both the effectiveness
of the haptic feedback system and the compatibility of the three different obstacle avoidance
algorithms. Results shows that haptic joystick helps to reduce number of collisions. However,
it increases the time taken to completion due to more difficult to accelerate caused by stiffen
haptic joystick. According to user reviews, it shows that ODG-PFA has the best compatibility
with the feedback mechanism due to its advancement in identifying obstacle and steady force
increment.
