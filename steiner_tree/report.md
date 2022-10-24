# CS 69.13, Fall 2022, Elliot Potter

## Method Description
This system is decomposed into six core Python files:

### initialpose_broadcaster
For each robot, this broadcasts the robot's initial pose, so that tf_broadcaster can sniff it.

### tf_broadcaster
This takes those poses and publishes transforms to them from the world frame (validated in rviz)

### waypoint_broadcaster
This publishes the waypoints that the robot needs to visit. It has a random point generation function and another 
function that prevents points from being too near each other.

### simple_motion
I wrote most of this last fall. It basically just has code to rotate to and drive to a point. (I didn't want to re-write
this, because I already did all the debugging work last year)

### robot_follower
The follower has a few main behaviors:
``` 
1. It listens to requests for followers, and replies on that respective service with its own name
2. It listens to the resource list for auctions -- it uses a service to bid on these resources
3. It listens to the winners for auctions -- if it wins an auction, it will drive to the associated point
```

### robot_leader
The leader does the following:
``` 
1. It listens to the waypoints channel, and sets waypoints that robots should visit
2. It requests that robots sign up using its service -- it publishes this service's name on the '/request_followers' topic
3. It listens to the service, adding robot names to a list of followers
4. When it has both waypoints and followers, and waypoints==followers, it begins the auction process:
    - it publishes all outstanding points
    - it waits for bids on these points
    - it selects the "winner" as the robot that delivered the lowest price bid, and broadcasts that this robot should
        drive to the associated point.
    - repeats
Once the auction had completed, the auctioneer goes inactive until it receives a new set of target points.
```

## Evaluation
This system worked pretty well. The final robot positions were a little off (less than 1m), but I think this was just
an issue with accuracy in my driving code. If I used a PID or some other system with feedback, this would have worked 
better. For the most part, I was able to get all desired functionality by adding a little extra to PA3

