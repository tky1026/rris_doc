============================================================================
Development of Eye Gaze System for Object Selection in Cluttered Environment
============================================================================

:Project title:
   Development of eye gaze system for object selection in cluttered environment

:Academic year:
   2020/21

:Student:
   Sin Wei Zheng

:Supervisor:
   Assoc Prof Ang Wei Tech

:Researchers:
   |rris_lilei|, Neha, |rris_marcus|

:School:
   NTU MAE

:DR-NTU:
   https://hdl.handle.net/10356/150484

:Final report:
   <report-link>

:GitHub:
   <github-link>

:Documentation:
   |rris_kuanyuee|

:Latest update:
   17 Nov 2022

----

In recent years, eye gaze or eye tracking is gaining a lot of traction, particularly in
gaze-based human-robot interaction (HRI). The information obtained from eye
tracking can be used for a variety of purposes including but not limited to object
grasping, wheelchair navigation and accessing computers or communication aids.
There is a need to accurately decipher the eye gaze information collected. However,
modelling eye gaze information as a fixation or fixing it onto one point is not sufficient
as natural eye gaze fluctuates around an area. This issue is further exacerbated in a
cluttered environment, as the user’s eye gaze is scattered across many objects. This
project aims to explore a feasible solution to ensure the user is able to correctly convey
their intentions for object selection in a cluttered environment while maintaining user
comfort.

This project uses an eye gaze system, Pupil Core from Pupil Labs and is implemented
in a ROS environment. This project also utilizes a Mask R-CNN, Detectron2 for object
detection. This project also makes use of the Wasserstein metric as an evaluator to
compare the probability distribution between the objects’ saliency map and the user’s
eye gaze distribution to predict the user’s intention for object selection.