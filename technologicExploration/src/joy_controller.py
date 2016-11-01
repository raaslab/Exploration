#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time
from sensor_msgs.msg import Joy
import math
from geometry_msgs.msg import (
    PoseArray,
    PoseStamped,
    Pose,
    Point,
    Twist,
    TransformStamped,
    Quaternion,
)
import roslaunch

current_status=0
launched=None
def listener():
	global current_status
	global launched
	rospy.init_node('joy_controller')
	top="/joy"
	while (True):
		message = rospy.wait_for_message(top, Joy)
		buttons=message.buttons
		turn_on=buttons[10]
		turn_off=buttons[11]
		
		if (current_status==0 and turn_on==1):
			package = 'beginner_tutorials'
			executable = 'ControlRob'
			node = roslaunch.core.Node(package, executable)
			launch = roslaunch.scriptapi.ROSLaunch()
			launch.start()
			process = launch.launch(node)
			launched=process
			print process.is_alive()
			rospy.sleep(2)
			current_status=1
		elif(current_status==1 and turn_off==1):
			process.stop()
			rospy.sleep(2)
			current_status=0

if __name__ == '__main__':
	listener()