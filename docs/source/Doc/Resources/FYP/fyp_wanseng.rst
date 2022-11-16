========================================
LWS - Seamless Indoor Outdoor Navigation
========================================

:Project title:
   Seamless Indoor Outdoor Navigation

:Academic year:
   2021/22

:Student:
   Liew Wan Seng

:Supervisor:
   Assoc Prof Ang Wei Tech

:Researchers:
   Wee Ching, :ref:`Kuan Yuee <rris_staff_kuanyuee>`

:School:
   NTU MAE

:DR-NTU:
   https://hdl.handle.net/10356/154671

:Final report:
   <report-link>

:GitHub:
   <github-link>

:Documentation:
   :ref:`Kuan Yuee <rris_staff_kuanyuee>`

:Latest update:
   16 Nov 2022

----

Nowadays, autonomous robotic applications that operated indoor and outdoor are gaining popularity in
the delivery, cleaning, and disinfection field due to the Coronavirus pandemic. Ideally, whenever there
is a mobile robot applied in the real world, the robot should be capable to perform seamless indoor-
outdoor navigation so that their functionalities could be more diversified. Compared to indoor
navigation, which is a mostly solved topic and widely used nowadays, there is still no definite way in
performing outdoor navigation, let alone travel from indoor to outdoor and vice versa. This is because
the cost of applying the state-of-the-art Simultaneous Localization and Mapping (SLAM) on outdoor
navigation is high and not realistic. Hence, there is a need to develop an indoor-outdoor navigation
system for mobile robots to travel indoor and outdoor reliably at a reasonable cost.

In this report, the navigation framework developed aims to integrate the map data extracted from the
Google Maps Platform and a civil-standard GPS sensor with the conventional navigation stack of the
mobile robot without utilising any SLAM element. The benefits of this framework include it eliminates
the need of doing the tedious pre-mapping process and does not require any LIDAR sensor, which is
commonly used in SLAM. The mobile robot platform used in this report is a wheelchair that aims to
facilitate the movement of a patient with acute mobility impairment.

Apart from that, this report will explore the other key components that are necessary for indoor-outdoor
navigation such as the computer vision in identifying travelable outdoor paths and indoor localization
sensor, Ultra-Wideband (UWB). The computer vision model utilizes the techniques of OpenCV and the
performance is compared with the Nvidia Free Space Segmentation. The localization of the mobile
robot is dependent on the GPS sensor outdoor while UWB at indoor, this report will also evaluate the
effectiveness of both localization sensors in the navigation system.

----

<details>