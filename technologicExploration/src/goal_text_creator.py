#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time
from nav_msgs.msg import Odometry
import math
from geometry_msgs.msg import (
    PoseArray,
    PoseStamped,
    PointStamped,
    Pose,
    Point,
    Twist,
    TransformStamped,
    Quaternion,
)
import numpy as np

def listener(ClickedPoint):
	file = open("goals.txt", "a")
	goal_x=ClickedPoint.point.x
	goal_y=ClickedPoint.point.y

	goal_line=str(goal_x)
	goal_line+="\t"
	goal_line+=str(goal_y)

	file.write(goal_line)

	print("added the following goal to the line")
	print(goal_line)
	file.close()
	#get the next point
	scan()

def scan():
	msg = rospy.wait_for_message("/clicked_point", PointStamped)
	listener(msg)

if __name__ == '__main__':
	open("goals.txt", 'w').close()
	scan()
