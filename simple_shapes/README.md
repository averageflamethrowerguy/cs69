# simple_shapes ROS package
This ROS package drives the robot in a pattern corresponding to a regular polygon, with specified number of sides
and side length.

## Requirements
- ROS -- tested on Melodic, but other versions may work.

## Configuration
The number of sides, side length, and rotation direction are all determined by the launch file

## Build
Once cloned in a ROS workspace, e.g., `ros_workspace/src/`, run the following commands to build it:

	cd ros_workspace
    catkin_make
	
## Run
Run first the robot nodes or simulator. 
Then, source and use the launch file:

	source ros_workspace/install/setup.sh
	roslaunch simple_shapes simple_shapes.launch

## Attribution & Licensing

Materials substantially authored by Alberto Quattrini Li. 
Copyright 2020 by Amazon.com, Inc. or its affiliates. Licensed MIT-0 - See LICENSE for further information

Source was modified by Elliot Potter in Fall 2022