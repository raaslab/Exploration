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
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import base64

def convert(messagepayload):
    t = open('newpic.bmp','w')
    t.write(messagepayload)
    t.close()

def on_message():
    #img = base64.b64decode(msg.payload)

    #convert(img)
    #time.sleep(5) 
    source = cv2.imread('tree_generated.png')  #this should be a mat file

    # talk to ROS
    bridge = CvBridge()
    
    pub2.publish(bridge.cv2_to_imgmsg(source, "bgr8"))
    print "uh..... done??"

if __name__ == '__main__':
    rospy.init_node('BringInAnImage', log_level = rospy.INFO)
    #rospy.init_node('robot4_pose_publisher')
    pub2 = rospy.Publisher('/BringInAnImage', Image, queue_size = 10)
    on_message()