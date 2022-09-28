# Import of python modules.
import math # use of pi.

# import of relevant libraries.
import rospy # module for ROS APIs

ROBOT_COHESION_RANGE = 5
ROBOT_SEPARATION_RANGE = 2
ROBOT_ALIGNMENT_RANGE = 5

ROBOT_COHESION_INTENSITY = 0.25
ROBOT_SEPARATION_INTENSITY = 0.75
ROBOT_ALIGNMENT_INTENSITY = 0.15


def get_direction_between_boids(boid_pos_1, boid_pos_2):
    """Gets the vector between boid_1 and boid_2"""
    return boid_pos_2[0]-boid_pos_1[0], boid_pos_2[1]-boid_pos_1[1]


def get_distance_between_boids(boid_pos_1, boid_pos_2):
    """Calculate the Cartesian distance between two boids"""
    return math.pow((math.pow(boid_pos_1[0] - boid_pos_2[0], 2.0) + math.pow(boid_pos_1[1] - boid_pos_2[1], 2.0)), 0.5)


def get_goal_orientation(flock_positions, robot_index):
    """
    Gets the goal orientation (in radians) for the robot to travel in

    Algorithm:
    1. Calculate the SEPARATION and COHESION terms
    2. Add the SEPARATION and COHESION terms to calculate a force vector
    3. Calculate the direction of the force vector
    4. Bias the direction of the force vector in the direction of alignment
    """

    separation_term = (0.0, 0.0)
    cohesion_term = (0.0, 0.0)
    alignment_term = 0

    robot_position = flock_positions[robot_index]

    for i in range(len(flock_positions)):
        # ignore our own robot
        if i == robot_index:
            continue

        distance = get_distance_between_boids(robot_position, flock_positions[i])
        direction = get_direction_between_boids(robot_position, flock_positions[i])

        # calculate separation part
        if distance < ROBOT_SEPARATION_RANGE:
            # robot steers away from other nearby robots
            force_vec = (-ROBOT_SEPARATION_INTENSITY*distance*direction[0],
                         -ROBOT_SEPARATION_INTENSITY*distance*direction[1])
            separation_term = (separation_term[0]+force_vec[0], separation_term[1]+force_vec[1])

        # calculate cohesion part
        if distance < ROBOT_COHESION_RANGE:
            # robot steers towards other nearby robots
            force_vec = (ROBOT_COHESION_INTENSITY*direction[0],
                         ROBOT_COHESION_INTENSITY*direction[1])
            cohesion_term = (cohesion_term[0]+force_vec[0], cohesion_term[1]+force_vec[1])

        # TODO -- calculate alignment part

    # TODO -- calculate direction of force vec

    # TODO -- bias force vec by alignment
