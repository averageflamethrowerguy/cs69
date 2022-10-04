import math # use of pi.

AVOIDANCE_RANGE = 4
NUM_SEGMENTS = 12

def get_force_vec(laserscan_information, current_orientation):
    """Gives back a force vector away from the centroid of the wall

    """
    current_angle = laserscan_information.angle_min + current_orientation

    force_vec = [0., 0.]
    num_hits = 0

    for i in laserscan_information.ranges:
        if i < AVOIDANCE_RANGE:
            force_intensity = 1 / i
            force_vec = [force_vec[0] - force_intensity*math.cos(current_angle),
                         force_vec[1] - force_intensity*math.sin(current_angle)]
            num_hits += 1

        current_angle += laserscan_information.angle_increment

    if num_hits == 0:
        return [0., 0.]
    return [force_vec[0] / num_hits, force_vec[1] / num_hits]

