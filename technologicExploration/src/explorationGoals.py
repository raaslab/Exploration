#! /usr/bin/env python

import roslib; roslib.load_manifest('actionlib_tutorials')
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import move_base_msgs.msg

def movebase_client():
    client = actionlib.SimpleActionClient('MoveBaseClient', move_base_msgs.msg.MoveBaseAction)

    # Waits until the action server has started up and started
    # listening for goals.
    print('right here')
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = move_base_msgs.msg.MoveBaseAction

    # Sends the goal to the action server.
    #client.send_goal(goal)

    # Waits for the server to finish performing the action.
    #client.wait_for_result()
    
    goal.target_pose.header.frame_id = "base_link"
    goal.target_pose.header.stamp = rospy.get_time()
    goal.target_pose.pose.position.x = 1.5
    goal.target_pose.pose.position.y = 0.9
    client.send_goal(goal)
    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult



if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('movebase_client')
        result=movebase_client()
        print "Result:", ', '.join([str(n) for n in result.sequence])
    except rospy.ROSInterruptException:
        print "program interrupted before completion"