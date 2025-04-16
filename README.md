# restaurant_world
# 🧭 TurtleBot3 Restaurant Navigation Project

This project demonstrates autonomous navigation using a TurtleBot3 (Burger model) inside a simulated restaurant environment in ROS 2 Humble with Gazebo and Navigation2.

## 📦 Package: `restaurant_world`

The `restaurant_world` package includes:
- A custom Gazebo world (`restaurant.world`)
- A predefined navigation map (`restaurant_map.yaml`)
- A Python script (`multi_point_nav.py`) for multi-point autonomous navigation (e.g., home → kitchen → table)

## 🚀 How to Run

### 1. Environment Setup

Before launching, set the TurtleBot3 model and update the Gazebo model path:

```bash
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models
source ~/.bashrc
(Optional: Check if the model is available)

bash
Copy
Edit
ls /opt/ros/humble/share/turtlebot3_gazebo/models/turtlebot3_burger
2. Launch the Restaurant World in Gazebo
bash
Copy
Edit
gazebo --verbose ~/turtlebot3_ws/src/restaurant_world/restaurant.world
3. Launch TurtleBot3 Navigation
bash
Copy
Edit
source ~/turtlebot3_ws/install/setup.bash
export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  map:=/home/surya/turtlebot3_ws/src/restaurant_world/maps/restaurant_map.yaml \
  use_sim_time:=True
4. Run Multi-Point Navigation Script
This script sends the robot to predefined goal points such as:

🏠 Home

🍳 Kitchen

🍽️ Table

bash
Copy
Edit
python3 ~/turtlebot3_ws/src/restaurant_world/scripts/multi_point_nav.py
🧠 Features
Custom restaurant simulation world

Autonomous waypoint navigation

Integration with TurtleBot3 Navigation2 stack

Easy launch and script-based automation

📁 File Structure
cpp
Copy
Edit
restaurant_world/
├── launch/
│   └── world_launch.py
├── maps/
│   └── restaurant_map.yaml
├── models/
│   └── [Custom models if any]
├── scripts/
│   └── multi_point_nav.py
├── worlds/
│   └── restaurant.world
└── README.md
🛠️ Dependencies
ROS 2 Humble

TurtleBot3

Navigation2

Gazebo

🧑‍💻 Author
Suryaprakash SP
📧 suryaprakashsp1999@gmail.com
🐙 GitHub: suryaprakash-V520S-08IKL
