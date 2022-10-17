# leader_follower ROS package
This ROS package corresponds to PA3. It has a leader robot that controls some number of followers, and greedily assigns
them to visit points.

## Requirements
- ROS -- tested on Melodic, but other versions may work.

## Configuration
The number of robots and their locations are determined by `robot_group.launch`. The positions to visit are determined
by `./nodes/waypoint_broadcaster`

## Build
Once cloned in a ROS workspace, e.g., `ros_workspace/src/`, run the following commands to build it:

	cd ros_workspace
    catkin_make
	
## Run
Terminal 1

    source ros_workspace/install/setup.sh
    roslaunch leader_follower empty_world.launch

Terminal 2

	source ros_workspace/install/setup.sh
	roslaunch leader_follower robot_group.launch

## Attribution & Licensing

Materials substantially authored by Alberto Quattrini Li. 
Copyright 2020 by Amazon.com, Inc. or its affiliates. Licensed MIT-0 - See LICENSE for further information

Source was modified by Elliot Potter in Fall 2022