#!/usr/bin/env python
#launch and get the occupancy grid
import rospy
import roslib; roslib.load_manifest('technologicExploration')
from std_msgs.msg import Bool
from std_msgs.msg import Int8
from nav_msgs.msg import (
    OccupancyGrid,
    MapMetaData,
)
from tf import TransformListener
from geometry_msgs.msg import (
    PoseArray,
    PoseStamped,
    Pose,
    Point,
    Twist,
    TransformStamped,
    Quaternion,
)
from tf2_msgs.msg import TFMessage
import numpy as np
from collections import deque
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import tf
import cv2
import math
from matplotlib import pyplot as plt
from sensor_msgs.msg import PointCloud2
import std_msgs.msg
import sys
import sensor_msgs.point_cloud2 as pcl2

count=0
stack=[]
unreachable_poses=[]
visited_poses=[]
def callback(data):
	print("callback called")
	global count
	global stack
	global visited_poses
	length=4000
	delta=0.05
	size=100
	scan_range=6.0
	
	frontierCells=[]
	frontier=[]

	#Getting the occupancy grid
	grid = data.data
	resolution = data.info.resolution
	occupancyGridMat=np.asarray(grid, dtype=np.int8)
	occupancyGridMatFin=np.reshape(occupancyGridMat, (length, length))
	current_pose=get_pose()
	pose_x=current_pose.position.x
	pose_y=current_pose.position.y
	#frontier=getFrontiers(pose_x,pose_x,occupancyGridMatFin)
	#Getting the matrix coordinates of the robot from the x and y
	pose_i = int((round(pose_x,2)/delta + 2000))
	pose_j = int((round(pose_y,2)/delta + 2000))
		

	print(pose_x)
	print(pose_y)
	print(pose_i)
	print(pose_j)
	

	

	#Populating the frontiers
	scan_area_i= int(pose_i - scan_range/delta)
	while (scan_area_i <= int(pose_i + (scan_range/delta))):
		scan_area_j= int(pose_j - scan_range/delta)
		while(scan_area_j <= int(pose_j + (scan_range/delta))):	
			if (occupancyGridMatFin[scan_area_i][scan_area_j] == 0 and (occupancyGridMatFin[scan_area_i -1][scan_area_j] == -1 or occupancyGridMatFin[scan_area_i][scan_area_j -1] == -1 or occupancyGridMatFin[scan_area_i][scan_area_j +1] == -1 or occupancyGridMatFin[scan_area_i+1][scan_area_j ] == -1) and ( occupancyGridMatFin[scan_area_i +1][scan_area_j+1] != 100 and occupancyGridMatFin[scan_area_i +1][scan_area_j -1] != 100 and occupancyGridMatFin[scan_area_i -1][scan_area_j +1] != 100 and occupancyGridMatFin[scan_area_i -1][scan_area_j-1] != 100 and occupancyGridMatFin[scan_area_i -1][scan_area_j] != 100 and occupancyGridMatFin[scan_area_i][scan_area_j -1] != 100 and occupancyGridMatFin[scan_area_i][scan_area_j +1] != 100 and occupancyGridMatFin[scan_area_i+1][scan_area_j ] != 100)):
				frontierCell=[]
				valid=1
				#This is to make sure that there are no frontiers too close to the obstacles
				count_i=scan_area_i-10
				while(count_i <= scan_area_i+10):
					count_j=scan_area_j-10
					while(count_j <= scan_area_j+10):
						#print(scan_area_i)
						#print(scan_area_j)
						if occupancyGridMatFin[count_i][count_j]==100:
							valid=0
						count_j+=1
					count_i+=1
				if (valid==1):
					frontierCell.append(scan_area_i)
					frontierCell.append(scan_area_j)
					frontier.append(frontierCell)
			scan_area_j+=1
		#print(scan_area_i)
		scan_area_i+=1
	#return frontier

	print(len(frontier))
	if (len(frontier)==0):
		explorationcomplete()
	else:
		publishFrontiers(frontier)
	 	#frontier=frontierCells[0]
	 	x, y=getcoords(frontier)
	 	print(x)
	 	print(y)
	 	#sendGoal(x,y,frontier,current_pose)


def getFrontiers(pose_x,pose_y,occupancyGridMatFin):
	global count
	global stack
	global visited_poses
	length=4000
	delta=0.05
	size=100
	scan_range=6.0
	frontierCells=[]
	frontier=[]

	

def publishFrontiers(frontier):
	delta=0.05
	size=100
	cloud=[]
	for frontierCell in frontier:
		point=[]
		i= frontierCell[0]
		j= frontierCell[1]
		#y=pose.x / resolution + 2000
		x= -100 + j * delta
		y= -100 + i * delta
		point.append(x)
		point.append(y)
		point.append(0.0)
		cloud.append(point)
	cloud_points=np.delete(cloud,(0), axis=0)
	pcl_pub = rospy.Publisher("/frontiers", PointCloud2,queue_size=10)
	rospy.sleep(1.)
	header = std_msgs.msg.Header()
	header.stamp = rospy.Time.now()
	header.frame_id = 'map'
    #create pcl from points
	scaled_polygon_pcl = pcl2.create_cloud_xyz32(header, cloud_points)
    #publish    
	rospy.loginfo("Publishing Frontiers.. !")
	pcl_pub.publish(scaled_polygon_pcl)

def sendGoal(x,y,frontier,prev_pose):
	goal_states = ['PENDING', 'ACTIVE', 'PREEMPTED', 
                       'SUCCEEDED', 'ABORTED', 'REJECTED',
                       'PREEMPTING', 'RECALLING', 'RECALLED',
                       'LOST']
	move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Waiting for move_base action server...")
	move_base.wait_for_server(rospy.Duration(60))
	rospy.loginfo("Connected to move base server")
	rospy.loginfo("Starting Exploration")
	#while not rospy.is_shutdown():
	goal = MoveBaseGoal()
	goal.target_pose.pose.position.x = (x) 
   	goal.target_pose.pose.position.y = (y)
   	goal.target_pose.pose.orientation.w = 1
   	goal.target_pose.header.frame_id = 'map'
   	goal.target_pose.header.stamp = rospy.Time.now()
   	rospy.loginfo("Goal Set!")
   	move_base.send_goal(goal)
   	finished_within_time = move_base.wait_for_result(rospy.Duration(60)) 
   	
   	if not finished_within_time:
   		move_base.cancel_goal()
   		rospy.loginfo("Timed out achieving goal")
   		current_pose=get_pose()
   		print("current pose : x: " + str(round(current_pose.position.x,1)) + " y : " + str(round(current_pose.position.y,1)) )
   		print("prev pose : x: " + str(round(prev_pose.position.x,1)) + " y : " + str(round(prev_pose.position.y,1)) )
   		if (round(current_pose.position.x,1) == round(prev_pose.position.x,1) and round(current_pose.position.y,1)==round(prev_pose.position.y,1)):
   			newFrontier=np.delete(frontier,np.s_[1:8], axis=0)
   			if (len(newFrontier)<8):
   				explorationcomplete()
   			else:
   				a, b=getcoords(newFrontier)
   				#print(newFrontier)
   				print(a)
   				print(b)
   				sendGoal(a,b,newFrontier,current_pose)
   		else:
   			scan()
   	else:
   		state = move_base.get_state()
   		if state == GoalStatus.SUCCEEDED:
   			rospy.loginfo("Goal succeeded!")
   			stack.append(goal.target_pose.pose)
   			scan()
   		else:
   			rospy.loginfo("Goal failed with error code: " + str(goal_states[state]))
   			unreachable_poses.append(frontier[0])
   			newFrontier=np.delete(frontier,np.s_[1:8], axis=0)
   						
   			if (len(newFrontier)<8):
   				explorationcomplete()
   			else:
   				a, b=getcoords(newFrontier)
   				#print(newFrontier)
   				print(a)
   				print(b)
   				sendGoal(a,b,newFrontier,prev_pose)

def explorationcomplete():
	global stack
	if (len(stack)==0):
		print("Exploration Complete")
	else:
		prev_pos=stack.pop()
		goal=prev_pos
		goal_x = goal.position.x
		goal_y = goal.position.y
		PrevPos(goal_x,goal_y)

def PrevPos(goal_x,goal_y):
	print("prev pose called")
	length=4000
	current_pose=get_pose()
	msg = rospy.wait_for_message("/map", OccupancyGrid)
	grid = msg.data
	occupancyGridMat=np.asarray(grid, dtype=np.int8)
	occupancyGridMatFin=np.reshape(occupancyGridMat, (length, length))
	frontier = getFrontiers(goal_x,goal_y,occupancyGridMatFin)
	if (len(frontier)==0):
		explorationcomplete()
	else:
		publishFrontiers(frontier)
	 	#frontier=frontierCells[0]
	 	x, y=getcoords(frontier)
	 	print(x)
	 	print(y)
	 	sendGoal(x,y,frontier,current_pose)

def getcoords(frontier):
	delta=0.05
	size=100
	frontierCell=frontier[8]
	i= frontierCell[0]
	j= frontierCell[1]
	x= -100 + j * delta
	y= -100 + i * delta
	return(x, y)

def scan():	    	
	print('Scanning...')
	msg = rospy.wait_for_message("/map", OccupancyGrid)
	callback(msg)


def get_pose():
	pose = rospy.wait_for_message("/robot_pose", Pose)
	return pose

def insert_origin():
	global stack
	print("Adding origin")
	current_pose=get_pose()
	stack.append(current_pose)
	print(stack)

def rotateInPlace():
	print("This is to make the robot rotate in place!")
	#rostopic pub -1 /RosAria/cmd_vel geometry_msgs/Twist '[0.0, 0.0, 0.0]' '[0.0, 0.0, 0.5]'

class node:
	def __init__( self , parent):
		self.parent=parent

if __name__ == '__main__':
	print('Initialized')
	rospy.init_node('SubscribeOccupancyGrid', anonymous=True)
	insert_origin()
	scan()