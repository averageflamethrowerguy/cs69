# Import of python modules.
import math # use of pi.

ROBOT_COHESION_RANGE = 3
ROBOT_SEPARATION_RANGE = 0.5
ROBOT_ALIGNMENT_RANGE = 3

ROBOT_COHESION_INTENSITY = 0.25
ROBOT_SEPARATION_INTENSITY = 0.75
ROBOT_ALIGNMENT_INTENSITY = 0.15


def get_direction_between_boids(boid_pos_1, boid_pos_2):
    """Gets the vector between boid_1 and boid_2"""
    return boid_pos_2[0]-boid_pos_1[0], boid_pos_2[1]-boid_pos_1[1]


def get_distance_between_boids(boid_pos_1, boid_pos_2):
    """Calculate the Cartesian distance between two boids"""
    return math.pow((math.pow(boid_pos_1[0] - boid_pos_2[0], 2.0) + math.pow(boid_pos_1[1] - boid_pos_2[1], 2.0)), 0.5)


def constrain_angle(angle):
    """Converts an arbitrary angle (in radians) between -2*pi and 2*pi into one between negative pi and pi"""
    if angle > math.pi:
        return angle - math.pi
    elif angle < -math.pi:
        return angle + math.pi
    else:
        return angle


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
    separation_count = 0

    cohesion_term = (0.0, 0.0)
    cohesion_count = 0

    alignment_term = 0
    alignment_count = 0

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
            separation_count += 1

        # calculate cohesion part
        if distance < ROBOT_COHESION_RANGE:
            # robot steers towards other nearby robots
            force_vec = (ROBOT_COHESION_INTENSITY*direction[0],
                         ROBOT_COHESION_INTENSITY*direction[1])
            cohesion_term = (cohesion_term[0]+force_vec[0], cohesion_term[1]+force_vec[1])
            cohesion_count += 1

        # calculate alignment part
        if distance < ROBOT_ALIGNMENT_RANGE:
            # robot aligns with other nearby robots
            # this value should be bounded by +/- pi
            alignment_term += ROBOT_ALIGNMENT_INTENSITY*(flock_positions[i][2] - robot_position[2])
            alignment_count += 1

    # calculate direction of force vec
    force_vec = (separation_term[0]+cohesion_term[0], separation_term[1]+cohesion_term[1])
    # use atan2 rather than atan to find the correct quadrant
    direction = math.atan2(force_vec[1], force_vec[0])
    # essentially taking the current angle and perturbing it
    desired_alignment = constrain_angle(alignment_term / alignment_count + robot_position[2])

    # calculate a weighted average of the force vec and desired_alignment
    return constrain_angle(
        ((ROBOT_COHESION_INTENSITY+ROBOT_SEPARATION_INTENSITY)*direction + ROBOT_ALIGNMENT_INTENSITY*desired_alignment)
        / (ROBOT_ALIGNMENT_INTENSITY+ROBOT_COHESION_INTENSITY+ROBOT_SEPARATION_INTENSITY)
    )
