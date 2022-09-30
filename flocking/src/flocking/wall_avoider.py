import math # use of pi.

AVOIDANCE_RANGE = 0.5
NUM_SEGMENTS = 12


def calculate_safe_range_from_index(index, laserscan_information):
    """
    Calculate a range of angle values that are safe from a certain index
    Note that for turtlebot, the laser scanner is pointed so that 0 deg is forwards,
    and 0 is the start angle of the array

    """
    min_safe_index = index
    max_safe_index = index

    target_index = index

    # starting from index, go down until we hit the end of the array or a barrier
    while 0 <= target_index < len(laserscan_information.ranges):
        # we see a barrier
        if laserscan_information.ranges[target_index] <= AVOIDANCE_RANGE:
            if target_index == index:
                return 0., 0., 0.
            min_safe_index = target_index+1
            break
        target_index -= 1

    target_index = index
    # starting from index, go up until we hit the end of the array or a barrier
    while target_index < len(laserscan_information.ranges):
        # we see a barrier
        if laserscan_information.ranges[target_index] <= AVOIDANCE_RANGE:
            max_safe_index = target_index-1
            break
        target_index += 1

    min_safe_angle = laserscan_information.angle_increment*min_safe_index + laserscan_information.angle_min
    max_safe_angle = laserscan_information.angle_increment*max_safe_index + laserscan_information.angle_min
    return max_safe_angle - min_safe_angle, min_safe_angle, max_safe_angle


def get_safe_range(laserscan_information):
    """Gives back a safe range of headings -- prefers (min, max),
    but will send (max, min) if safe direction is other
    Returns 0-2pi range

    How should this work?
        1. Break 360 deg into 30 deg segments
        2. For each segment, shoot a vector into the center
            if hits a wall, abort
            otherwise, spread out from the center, going until a spreading edge finds a wall or we hit an array end
            if width of the clear area is more than math.pi, we've found our range and can abort early
            (Limitation -- finding big gaps directly behind the robot)

    """
    angle_range = laserscan_information.angle_max - laserscan_information.angle_min
    index_increment_per_segment = int(angle_range / laserscan_information.angle_increment)

    largest_range_size = 0.0
    largest_range_value = (0.0, 0.0)

    # bottom range is ~0-30 deg
    # top range is ~330-360 deg
    # they can be combined
    bottom_range_size = 0.0
    bottom_range = (0.0, 0.0)
    top_range_size = 0.0
    top_range = (0.0, 0.0)

    # go through the segments; find the start index for each
    for i in range(NUM_SEGMENTS):
        # Math: index is in middle of range, which changes by index_increment
        start_index = int((i + 0.5) * index_increment_per_segment)
        safe_size, min_safe, max_safe = calculate_safe_range_from_index(start_index, laserscan_information)

        if i == 0:
            bottom_range = (min_safe, max_safe)
            bottom_range_size = safe_size

        if i == NUM_SEGMENTS-1:
            top_range = (min_safe, max_safe)
            top_range_size = safe_size

        if safe_size > largest_range_size:
            largest_range_size = safe_size
            largest_range_value = (min_safe, max_safe)
        if safe_size > math.pi:
            break

    if bottom_range_size+top_range_size > largest_range_size:
        return top_range[0], bottom_range[1]

    return largest_range_value

