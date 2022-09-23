# CS 69.13, Fall 2022, Elliot Potter

## Method Description
This program is a modified version of the simple_motion program that you provided to us. I decided to import that program as a library, and then write a
separate class to handle subscribing to odometry and publishing error messages. 
My program essentially is a for-loop where the robot drives forward, then rotates by 360 deg / num_sides. It accepts parameters from the launch file, and 
these determine the size of polygon, number of sides, and direction of travel.

## Evaluation
This program worked fine. I essentially wrote it without testing it, and it pretty much worked as soon as I was able to get the file to run. 
I had the most difficulty figuring out the configuration of the package -- I ended up iteratively converting simple_motion into the final package so that
I knew exactly what was preventing the build. I ended up with a set of rules around creating ROS packages. You can find them in <TODO>
