#!/usr/bin/env python
import rospy
import roslib; roslib.load_manifest('technologicExploration')
from geometry_msgs.msg import (
    PoseArray,
    PoseStamped,
    Pose,
    Point,
    Twist,
    TransformStamped,
    Quaternion,
)

def assignGoals():
	msg = rospy.wait_for_message(top, Pose)

if __name__ == '__main__':
	print('Initialized')
	rospy.init_node('mover', anonymous=True)
	assignGoals()
    
