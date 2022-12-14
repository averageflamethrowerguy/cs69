#!/usr/bin/env python
#The line above is important so that this file is interpreted with Python when running it.

# Import of python modules.
import math # use of pi.

# import of relevant libraries.
import rospy # module for ROS APIs
from geometry_msgs.msg import Twist # message type for cmd_vel
from sensor_msgs.msg import LaserScan # message type for scan

# Constants.
FREQUENCY = 10 #Hz.
LINEAR_VELOCITY = 0.2 # m/s
ANGULAR_VELOCITY = math.pi/4 # rad/s
LASER_ANGLE_FRONT = 0 # radians
MIN_THRESHOLD_DISTANCE = 0.5 # m, threshold distance.
DEFAULT_CMD_VEL_TOPIC = 'cmd_vel'
DEFAULT_SCAN_TOPIC = 'scan'


class SimpleMotion:
    def __init__(self, linear_velocity=LINEAR_VELOCITY, angular_velocity=ANGULAR_VELOCITY):
        """Constructor."""

        # Setting up publishers/subscribers.
        self._cmd_pub = rospy.Publisher(DEFAULT_CMD_VEL_TOPIC, Twist, queue_size=1)

        # Other variables.
        self.linear_velocity = linear_velocity # Constant linear velocity set.
        self.angular_velocity = angular_velocity # Constant angular velocity set.
        self._close_obstacle = False # Flag variable that is true if there is a close obstacle.

    def move_forward(self, distance):
        """Function to move_forward for a given distance."""
        # Rate at which to operate the while loop.
        rate = rospy.Rate(FREQUENCY)

        # Setting velocities. 
        twist_msg = Twist()
        twist_msg.linear.x = self.linear_velocity
        start_time = rospy.get_rostime()
        duration = rospy.Duration(distance/twist_msg.linear.x)

        # Loop.
        while not rospy.is_shutdown():
            # Check if traveled of given distance based on time.
            if rospy.get_rostime() - start_time >= duration:
                break

            # Publish message.
            if self._close_obstacle:
                self.stop()
            else:
                self._cmd_pub.publish(twist_msg)

            # Sleep to keep the set publishing frequency.
            rate.sleep()

        # Traveled the required distance, stop.
        self.stop()
        
    def rotate_in_place(self, rotation_angle):
        """
        Rotate in place the robot of rotation_angle (rad) based on fixed velocity.
        Assumption: Counterclockwise rotation.
        """
        twist_msg = Twist()
        twist_msg.angular.z = self.angular_velocity
        
        duration = rotation_angle / twist_msg.angular.z
        if duration < 0:
            # flip velocity if angle is negative
            twist_msg.angular.z = -twist_msg.angular.z
            duration = -duration

        start_time = rospy.get_rostime()
        rate = rospy.Rate(FREQUENCY)
        while not rospy.is_shutdown():
            # Check if done
            if rospy.get_rostime() - start_time >= rospy.Duration(duration):
                break
                
            # Publish message.
            self._cmd_pub.publish(twist_msg)
            
            # Sleep to keep the set frequency.
            rate.sleep()

        # Rotated the required angle, stop.
        self.stop()

    def rotate_to_point(self, initial_orientation, current_point, desired_point):
        """
        Rotates in the direction of the specified point
        """
        difference = [desired_point[0] - current_point[0],
                      desired_point[1] - current_point[1]]
        # find the angle that we need to rotate to
        # this is from the reference frame of the previous point, where the +x direction
        # of that point is in the +x direction of the robot when it was at 0,0.
        # the angle is just opp / adj; in this case y / x

        # We use math.atan2 because Python 2 has a stupid issue where
        # it uses integer division for integers.
        # This would be fine in a typed language, but is not when
        # we are dealing with interpreted variables!
        # Fortunately, this is fixed in Python 3.
        angle = math.atan2(difference[1], difference[0])

        # We find the angle to rotate and calculate the modulo so we don't spin in a circle
        angle_to_rotate = (angle - initial_orientation) % ( 2 * math.pi )
        # we do the faster rotation if the angle is more than 180 degrees
        if angle_to_rotate > math.pi:
            angle_to_rotate = angle_to_rotate - ( 2 * math.pi )

        # rotate to the angle
        self.rotate_in_place(angle_to_rotate)

    def drive_to_point(self, current_point, desired_point):
        """
        Drives to the point
        """
        # find the difference between the current point and the next one
        difference = [desired_point[0] - current_point[0],
                      desired_point[1] - current_point[1]]

        # find the length that we need to travel
        length = math.sqrt(difference[0] ** 2 + difference[1] ** 2)
        self.move_forward(length)

    def stop(self):
        """Stop the robot."""
        twist_msg = Twist()
        self._cmd_pub.publish(twist_msg)


if __name__ == "__main__":
    """Run the main function."""
    main()
