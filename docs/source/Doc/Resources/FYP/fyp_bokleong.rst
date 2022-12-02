============================================================================================
Performance Evaluation of Local Planner Algorithms for Assistive Wheelchairs in Dense Crowds
============================================================================================

:Project title:
   Performance evaluation of local planner algorithms for assistive wheelchairs in dense crowds

:Academic year:
   2021/22

:Student:
   Chua Bok Leong

:Supervisor:
   Assoc Prof Ang Wei Tech

:Researchers:
   |rris_weeching|

:School:
   NTU MAE

:DR-NTU:
   https://hdl.handle.net/10356/159131

:Final report:
   <report-link>

:GitHub:
   <github-link>

:Documentation:
   |rris_kuanyuee|

:Latest update:
   17 Nov 2022

----

Assistive wheelchairs are an invaluable tool in assisting people with movement difficulties in
gaining back some semblance of mobility in their lives. However, one problem encountered by
wheelchair users is the difficulty they face in navigating through dense crowds. Autonomous
assistive wheelchairs aim to solve this problem by offloading the navigation decisions from the
user to a computer, however current state-of-the-art local planner algorithms like the Dynamic
Window Approach (DWA) or Timed-Elastic Band (TEB) algorithm often meet with the freezing
robot problem when attempting to navigate in a dense crowd. In recent years, new algorithms
based on deep reinforcement learning have shown promise in providing safe and efficient
navigation through crowded spaces. A notable example is the Collision Avoidance with Deep
Reinforcement Learning (CADRL) algorithm as its authors have demonstrated the algorithm in a
real-world setting. What is missing is a way to compare the performance of these algorithms
against one another to determine if these new algorithms have the potential to replace the current
state-of-the-art.

Thus, this report presents an evaluation system that quantifies the navigation performance of
different local planner algorithms in a dense crowd. This evaluation system consists of four
modules, namely a dense crowd simulator, a data collection module, a data processing module,
and a data visualization module. The system was used to evaluate the performance of 3 algorithms
(DWA, TEB, and CADRL) as well as 5 human participants.

This evaluation system revealed that CADRL refused to navigate through the dense crowd, instead
opting to navigate around it. Additionally, comparing the current algorithms, TEB performed
2
better than DWA in this particular dense crowd scenario. Lastly, the human participants performed
similar or better in general than all three algorithms.

----

<details>