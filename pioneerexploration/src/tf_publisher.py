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
    rospy.init_node('map_tf_broadcaster')

    pose = rospy.wait_for_message("/robot_pose", Pose)

    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        tf_x=pose.position.x -50
        tf_y=pose.position.y -50
        
        br.sendTransform((tf_x, tf_y, 0.0),
                         (0.0, 0.0, 0.0, pose.orientation.w),
                         rospy.Time.now(),
                         "mapgmap",
                         "map")
        rate.sleep()