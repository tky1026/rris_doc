=====================================================
Human-aware Robot Navigation for Assistive Wheelchair
=====================================================

:Project title:
   Human-aware robot navigation for assistive wheelchair

:Academic year:
   2021/22

:Student:
   Yeoh Yong Shan

:Supervisor:
   Assoc Prof Ang Wei Tech

:Researchers:
   :ref:`Wee Ching <rris_staff_weeching>`

:School:
   NTU MAE

:DR-NTU:
   https://hdl.handle.net/10356/154661

:Final report:
   <report-link>

:GitHub:
   <github-link>

:Documentation:
   :ref:`Kuan Yuee <rris_staff_kuanyuee>`

:Latest update:
   17 Nov 2022

----

Human tracking is an important task in a robotic wheelchair operating in a human crowded
environment. It enables the robot to interact with humans in the environment effectively while
ensuring their safety. However, this is a challenging task as human crowded environment are
unstructured in nature. Unexpected events such as occlusions or non-linear human motion
occurs frequently. The task becomes more difficult when the camera is mounted on a mobile
robot platform. Camera motion results in a change in perspective of the camera, and thus a
change in appearance of the targets. Furthermore, if camera motion is unaccounted for in the
motion model of the human tracking system, an unexpected motion of the targets will be
perceived by the system.

In this report, we present a Multiple Object Tracking (MOT) module towards achieving realtime
human tracking on a robotic wheelchair platform. The MOT module utilizes a YOLOv4 model for
object detection. Camera projection matrix is used to convert the bounding box to a point in the
world coordinates system. A Kalman Filter is used to track motion of the targets. A ReID network
is used to generate an appearance descriptor of the detections. Track association is performed
by evaluating a combined metric that describes both the positional distance and appearance
distance of detections in the current time step compared to those in previous time step.

Apart from a human tracking system, this report will also present the design and implementation
of a tracking camera and a human following module. These implementations complement the
MOT module in enhancing the capabilities of the robotic wheelchair.

Experimental results validate the performance of the proposed MOT module to track humans in
a real-world environment. The proposed MOT system managed to outperform existing MOT
approaches such as Deep SORT in terms of accuracy without a compromise in speed.

----

<details>