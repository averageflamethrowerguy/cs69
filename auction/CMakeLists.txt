## For full information http://wiki.ros.org/catkin/CMakeLists.txt 
# Used this tutorial to compile actions: https://roboticsbackend.com/ros-create-custom-action/

#############################################################################
## Set minimum required version of cmake, project name and compile options ##
#############################################################################
cmake_minimum_required(VERSION 2.8.3)
project(auction)

###########################################################################
## Find catkin packages and libraries for catkin and system dependencies ##
###########################################################################
find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  actionlib_msgs
  std_msgs
  message_generation
)

##########################################
## Setup for python modules and scripts ##
##########################################
catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################
# No new message declared.

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################
# No new parameters declared.

###################################
## catkin specific configuration ##
###################################
add_message_files(
  FILES
  FollowerReq.msg
)

add_service_files(
  FILES
  RequestFollowers.srv
  Bid.srv
)

add_action_files(
  FILES
  DriveToTarget.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS
    rospy
    geometry_msgs
    message_runtime
)

###########
## Build ##
###########
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

catkin_install_python(PROGRAMS 
  nodes/tf_broadcaster
  nodes/initialpose_broadcaster
  nodes/auctioneer
  nodes/robot_follower
  nodes/waypoint_broadcaster
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############
# No unit test performed.
