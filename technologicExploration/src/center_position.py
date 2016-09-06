#!/usr/bin/env python  
import roslib
import rospy

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
    rospy.init_node('center_tf_broadcaster')

    pose = rospy.wait_for_message("/vanishing_points", Pose)

    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        tf_x=pose.position.x
        tf_y=pose.position.y
        
        br.sendTransform((tf_x, tf_y, tf_z),
                         (0.0, 0.0, 0.0, pose.orientation.w),
                         rospy.Time.now(),
                         "mapgmap",
                         "map")
        rate.sleep()