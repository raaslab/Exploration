#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
from geometry_msgs.msg import (
    PoseArray,
    PoseStamped,
    Pose,
    Point,
    Twist,
    TransformStamped,
    Quaternion,
)

if __name__ == '__main__':
    rospy.init_node('base_unrotated_publisher')
    #p = rospy.Publisher('base_unrotated_pose', Pose)
    listener = tf.TransformListener()
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('odom', 'base_link', rospy.Time(0))
            tf_x=trans[0]
            tf_y=trans[1]
            tf_z=trans[2]   
        
            br.sendTransform((tf_x, tf_y, tf_z),(0.0, 0.0, 0.0, 1.0),rospy.Time.now(),"base_link_unrotated","odom")                      

            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rate.sleep()