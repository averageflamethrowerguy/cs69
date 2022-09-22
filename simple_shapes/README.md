# Simple Shapes ROS package
When invoked, the robot will draw a regular polygon with the number of sides equal to a parameter.

## Requirements
- ROS -- tested on Melodic, but other versions may work.
- colcon -- used for building the application. 

## Build
Once cloned in a ROS workspace, e.g., `ros_workspace/src/`, run the following commands to build it:

	cd ros_workspace
	colcon build
	
## Run
Run first the robot nodes or simulator. 
Then, source and use the launch file:

	source ros_workspace/install/setup.sh
	roslaunch simple_motion simple_motion.launch

## Attribution & Licensing
Simple Motion was written by Professor Quattrini Li. Simple Shapes was written on top of this package by Elliot Potter.

