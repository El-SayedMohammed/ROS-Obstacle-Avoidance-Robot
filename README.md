
# 🤖 Robot - Obstacle Avoidance Simulation

A ROS-based mobile robot project that simulates autonomous obstacle avoidance 
using Python, developed and tested on a Gazebo simulation environment.

## 📋 Overview

This project implements a mobile robot capable of navigating a simulated 
environment while detecting and avoiding obstacles in real-time. The robot 
model, sensors, and simulation world are fully defined using ROS's standard 
tools and file structures.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **ROS (Robot Operating System)** | Core robotics framework |
| **Python** | Robot control logic & node scripting |
| **Gazebo** | 3D physics simulation environment |
| **URDF** | Robot model & structure description |

## 📁 Project Structure


t_ws/src/robot/
├── config/      # Configuration files (parameters, RViz configs)
├── launch/      # ROS launch files to start nodes & simulation
├── resource/    # Package resource files
├── robot/       # Core robot control logic (Python nodes)
├── test/        # Test scripts
├── urdf/        # Robot model description (Unified Robot Description Format)
├── worlds/      # Gazebo simulation environments
├── package.xml  # ROS package metadata
├── setup.py     # Python package setup
└── setup.cfg    # Package configuration


## ⚙️ How It Works

- The robot uses sensor data (e.g., LiDAR or distance sensors) to detect 
  nearby obstacles in its path.
- A Python-based control node processes sensor readings in real-time and 
  adjusts the robot's movement direction to avoid collisions.
- The entire behavior is tested and validated inside a Gazebo simulation 
  world before any real-world deployment.

## 🎓 Context

Developed independently as a personal robotics learning project, running 
on a Virtual Machine with ROS and Python.

---
🤖 Built as a personal robotics project by **Elsayed Mohamed**
