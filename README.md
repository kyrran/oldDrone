# TommyWoodleyMEngProject

## Abstract

The utilisation of Unmanned Aerial Vehicles (UAVs) for data collection in hard-to-reach areas, such as dense forests, has garnered significant attention. However, the limited flight time of UAVs, due to their inherent battery constraints, remains a significant challenge. Existing solutions focus on increasing battery capacity or integrating energy-harvesting methods, which are often limited by environmental conditions. Inspired by birds, this project explores a tethered perching mechanism. This approach aims to conserve energy by allowing drones to perch on branches, reducing their environmental impact and enabling silent operation for wildlife observation.
This project provides a simulation environment capable of being used for reinforcement learning for tethered drone perching. A key outcome of this project is a reinforcement learning agent capable of performing tethered drone perching. It can perform faster trajectories without the need for a long period of waiting during the manoeuvre. The approaching stage showed a 17% improvement compared to existing baselines. This agent was able to achieve a higher number of wraps around the branch leading to more stability during the latter half of the manoeuvre. Finally, the agent has been deployed on a real system using a custom drone controller. In practical experiments, this agent achieved a 93% success rate at tethered perching.

## Acknowledgements

I would like to extend my deepest gratitude to my project supervisor, Dr. Basaran Bahadir Kocer, for his invaluable guidance and support. Many thanks to Dr. Antoine Cully for his support as my second marker. Special thanks to Atar Babgei for his active collaboration and assistance throughout practical experiments. I would also like to thank Dr. Ronald Clark, Lucas Romanello, and Hann Nguyen for their stimulating discussions and insights.

## Structure
This repositroy contains two directories `progress_updates` and `src`:
- `src`- main content of the repository - check out the ReadMe in that folder for more information.
- `progress_updates` - in the process of being migrated to a private repo

### Aim
Design and Implement a Framework for Learning Agile Perching Trajectories from Non-Expert Demonstrations.

Using a small number of demonstrations to perform the required task.
Following demonstrations the agent should improve energy efficiency while still completing the perching task.

### Steps

