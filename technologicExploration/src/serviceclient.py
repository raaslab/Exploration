#!/usr/bin/env python

import sys
import rospy
from nav_msgs.srv import GetPlan
from geometry_msgs.msg import PoseStamped,Pose


def get_plan(robotName):
    print("in method")
    topicName="/"
    topicName+=robotName
    topicName+="/move_base/NavfnROS/make_plan"

    rospy.wait_for_service(topicName)
    start = PoseStamped()
    start.header.frame_id = 'map'
    start.pose.position.x = -15
    start.pose.position.y = 3
    start.pose.orientation.w = 1

    goal = PoseStamped()
    goal.header.frame_id = 'map'
    goal.pose.position.x = -13
    goal.pose.position.y = -3
    goal.pose.orientation.w = 1

    tolerance=0.5

    try:
        move_base_plan = rospy.ServiceProxy(topicName, GetPlan)
        plan = move_base_plan(start,goal,tolerance)
        return plan
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def get_pose(robotName):
    top="/"
    top+=str(robotName)
    top+="_pose"
    pose = rospy.wait_for_message(top, Pose)
    return pose

if __name__ == "__main__":
    print("Initialized")
    while (True):
        plan_ret=get_plan("robot1")
        poses=plan_ret.plan.poses
        if(poses):
            print(len(poses))
            print("GOT A PLAN!!!!")
        else:
            print("NADA")
        rospy.sleep(2.0)
    