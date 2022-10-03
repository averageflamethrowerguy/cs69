# simple_shapes ROS package
This ROS package drives the robot in a pattern corresponding to a regular polygon, with specified number of sides
and side length.

## Requirements
- ROS -- tested on Melodic, but other versions may work.

## Configuration
Launch files specify the world files and robots

## Build
Once cloned in a ROS workspace, e.g., `ros_workspace/src/`, run the following commands to build it:

	cd ros_workspace
    catkin_make
	
## Run

### GAZEBO
Run first the robot nodes or simulator. 
Then, source and use the launch file:

	source catkin_ws/devel/setup.sh
    roslaunch flocking gazebo_world.launch
	roslaunch flocking flocking_gazebo.launch

### STAGE
Then, source and use the launch file:

	source catkin_ws/devel/setup.sh
    roslaunch flocking stage_world.launch

## Attribution & Licensing

Materials substantially authored by Alberto Quattrini Li. 
Copyright 2020 by Amazon.com, Inc. or its affiliates. Licensed MIT-0 - See LICENSE for further information

Source was modified by Elliot Potter in Fall 2022