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
from geometry_msgs.msg import Twist
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import time
from std_msgs.msg import String

count=0
stack=[]
root=[]
unreachable_poses=[]
visited_poses=[]
global_goals=[]
G=nx.DiGraph()
global_BVs=[]
check=0
start_time=int(math.floor(time.time()))
def callback(data):
    print("callback called")
    global count
    global stack
    global visited_poses
    global global_goals
    global G
    global root
    global global_BVs
    global check

    length=800
    delta=0.25
    size=50
    scan_range=10.0

    
    frontierCells=[]
    frontier=[]
    rejectedFrontiers=[]
    blockingVertices=[]
    blockingFrontier=[]

    validBlockingVertices=[]
    filter2=[]
    filter3=[]
    filter4=[]
    goals=[]
    filter5=[]
    dictBlockingAngles={}
    dictFrontierLines={}
    
    #Getting the occupancy grid
    grid = data.data
    resolution = data.info.resolution
    height=data.info.height
    width=data.info.width
    
    occupancyGridMat=np.asarray(grid, dtype=np.int8)
    occupancyGridMatFin=np.reshape(occupancyGridMat, (height, width))
    current_pose=get_pose()
    pose_x=current_pose.position.x
    pose_y=current_pose.position.y
    #frontier=getFrontiers(pose_x,pose_x,occupancyGridMatFin)
    #Getting the matrix coordinates of the robot from the x and y
    pose_i = int((round(pose_y,3)/delta + 400))
    pose_j = int((round(pose_x,3)/delta + 400))

    #Populating the frontiers
    scan_area_i= int(pose_i - scan_range/delta)
    while (scan_area_i <= int(pose_i + (scan_range/delta))):
        scan_area_j= int(pose_j - scan_range/delta)
        while(scan_area_j <= int(pose_j + (scan_range/delta))): 
            if (occupancyGridMatFin[scan_area_i][scan_area_j] == 0 and (occupancyGridMatFin[scan_area_i -1][scan_area_j] == -1 or occupancyGridMatFin[scan_area_i][scan_area_j -1] == -1 or occupancyGridMatFin[scan_area_i][scan_area_j +1] == -1 or occupancyGridMatFin[scan_area_i+1][scan_area_j ] == -1)):
                frontierCell=[]
                frontierCell.append(scan_area_i)
                frontierCell.append(scan_area_j)
                valid=1

                if(occupancyGridMatFin[scan_area_i -1][scan_area_j-1] == 100 or occupancyGridMatFin[scan_area_i -1][scan_area_j] == 100 or occupancyGridMatFin[scan_area_i -1][scan_area_j+1] == 100 or occupancyGridMatFin[scan_area_i][scan_area_j-1] == 100 or occupancyGridMatFin[scan_area_i ][scan_area_j+1] == 100 or occupancyGridMatFin[scan_area_i +1][scan_area_j-1] == 100 or occupancyGridMatFin[scan_area_i +1][scan_area_j] == 100 or occupancyGridMatFin[scan_area_i +1][scan_area_j+1] == 100):
                    blockingFrontier.append([scan_area_i,scan_area_j])

                #This is to make sure that there are no frontiers too close to the obstacles
                count_i=scan_area_i-2
                while(count_i <= scan_area_i+2):
                    count_j=scan_area_j-2
                    while(count_j <= scan_area_j+2):
                        if occupancyGridMatFin[count_i][count_j]==100:
                            valid=0
                        count_j+=1
                    count_i+=1              
                if (valid==1):
                    frontier.append(frontierCell)
                else:
                    rejectedFrontiers.append(frontierCell)
            scan_area_j+=1
        scan_area_i+=1
    #return frontier
    scan_area_i= int(pose_i - scan_range/delta)
    while (scan_area_i <= int(pose_i + (scan_range/delta))):
        scan_area_j= int(pose_j - scan_range/delta)
        while(scan_area_j <= int(pose_j + (scan_range/delta))): 
            if (occupancyGridMatFin[scan_area_i][scan_area_j] == 100 and ( ([scan_area_i-1,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j-1,rejectedFrontiers)) or ([scan_area_i-1,scan_area_j] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j,rejectedFrontiers)) or ([scan_area_i-1,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j +1,rejectedFrontiers)) or ([scan_area_i,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i,scan_area_j -1,rejectedFrontiers)) or ([scan_area_i,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i,scan_area_j +1,rejectedFrontiers)) or ([scan_area_i+1,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j -1,rejectedFrontiers)) or ([scan_area_i+1,scan_area_j] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j,rejectedFrontiers)) or ([scan_area_i+1,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j +1,rejectedFrontiers)))):
                blockingVertices.append([scan_area_i,scan_area_j])
            scan_area_j+=1
        #print(scan_area_i)
        scan_area_i+=1
    #return frontier

    epsilon = 0.25;

    validBlockingVertices=blockingVertices

    for vbv in validBlockingVertices:
        bi=vbv[0]
        bj=vbv[1]
        valid=1
        if ((occupancyGridMatFin[bi-2][bj] == 100 and occupancyGridMatFin[bi][bj-2] == 100)or (occupancyGridMatFin[bi-2][bj] == 100 and occupancyGridMatFin[bi][bj+2] == 100) or (occupancyGridMatFin[bi+2][bj] == 100 and occupancyGridMatFin[bi][bj-2] == 100) or (occupancyGridMatFin[bi+2][bj] == 100 and occupancyGridMatFin[bi][bj+2] == 100) or (occupancyGridMatFin[bi-1][bj] == 100 and occupancyGridMatFin[bi+1][bj] == 100) or (occupancyGridMatFin[bi][bj-1] == 100 and occupancyGridMatFin[bi][bj+1] == 100) or (occupancyGridMatFin[bi][bj-1] == 100 and occupancyGridMatFin[bi][bj+1] == -1) or (occupancyGridMatFin[bi][bj-1] == -1 and occupancyGridMatFin[bi][bj+1] == 100) or (occupancyGridMatFin[bi-1][bj] == 100 and occupancyGridMatFin[bi+1][bj] == -1) or (occupancyGridMatFin[bi-1][bj] == -1 and occupancyGridMatFin[bi+1][bj] == 100)):
            valid = 0
        if (valid==1):
            filter2.append(vbv)
    
    for bv in filter2:
        valid = 0
        if(checkNeighbours(bv,occupancyGridMatFin,rejectedFrontiers,frontier)):
            valid=1
        if (valid==1):
            filter3.append(bv)
    filter4=filter3
    for vbv in filter3:
        bi=vbv[0]
        bj=vbv[1]
        bx= -100 + bj * delta + delta/2
        by= -100 + bi * delta + delta/2
        for bv in filter3:
            bi1=bv[0]
            bj1=bv[1]
            bx= -100 + bj * delta + delta/2
            by= -100 + bi * delta + delta/2
            if(not(bi==bi1 and bj==bj1) and [bi,bj] in filter4):
                if(bi==bi1 or bj==bj1):
                    filter4.remove([bi1,bj1])

    for bv in filter4:
        bi=bv[0]
        bj=bv[1]

        bx= -100 + bj * delta + delta/2
        by= -100 + bi * delta + delta/2

        bearing= math.atan2(by-pose_y,bx-pose_x)
        dictBlockingAngles[bearing]=[bi,bj]
    
    filter5=sorted(dictBlockingAngles)
    print(len(dictBlockingAngles))
    curr_root=root[len(root)-1]
    for bear in filter5:
        frontierLine=[]
        bv=dictBlockingAngles[bear]
        bi=bv[0]
        bj=bv[1]
        if(bv not in global_BVs and [bi-1,bj] not in global_BVs and [bi+1,bj] not in global_BVs and [bi,bj-1] not in global_BVs and [bi,bj+1] not in global_BVs):
            global_BVs.append(bv)
            bv_tup=(bv[0],bv[1])
            G.add_node(bv_tup)
            G.add_edge(curr_root,bv_tup)
        
        if(occupancyGridMatFin[bi-1][bj] == 100):
            if(occupancyGridMatFin[bi][bj-5] == 0):
                clearance=1
                while(occupancyGridMatFin[bi][bj-clearance]!=100):
                    frontierLine.append([bi,bj-clearance])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi+15,bj-5])
            elif (occupancyGridMatFin[bi][bj+5] == 0):
                clearance=1
                while(occupancyGridMatFin[bi][bj+clearance]!=100):
                    frontierLine.append([bi,bj+clearance])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi+15,bj+5])
        if(occupancyGridMatFin[bi+1][bj] == 100):
            if(occupancyGridMatFin[bi][bj-5] == 0):
                clearance=1
                while(occupancyGridMatFin[bi][bj-clearance]!=100):
                    frontierLine.append([bi,bj-clearance])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi-15,bj-5])
            elif (occupancyGridMatFin[bi][bj+5] == 0):
                clearance=1
                while(occupancyGridMatFin[bi][bj+clearance]!=100):
                    frontierLine.append([bi,bj+clearance])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi-15,bj+5])
        if(occupancyGridMatFin[bi][bj-1] == 100):
            if(occupancyGridMatFin[bi-5][bj] == 0):
                clearance=1
                while(occupancyGridMatFin[bi-clearance][bj]!=100):
                    frontierLine.append([bi-clearance,bj])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi-5,bj+15])
            elif (occupancyGridMatFin[bi+5][bj] == 0):
                clearance=1
                while(occupancyGridMatFin[bi+clearance][bj]!=100):
                    frontierLine.append([bi+clearance,bj])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi-5,bj+15])
        if(occupancyGridMatFin[bi][bj+1] == 100):
            if(occupancyGridMatFin[bi-5][bj] == 0):
                clearance=1
                while(occupancyGridMatFin[bi-clearance][bj]!=100):
                    frontierLine.append([bi-clearance,bj])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi-5,bj-15])
            elif (occupancyGridMatFin[bi+5][bj] == 0):
                clearance=1
                while(occupancyGridMatFin[bi+clearance][bj]!=100):
                    frontierLine.append([bi+clearance,bj])
                    clearance=clearance+1
                dictFrontierLines[bear]=frontierLine
                goals.append([bi-5,bj-15])
    tup_pose=(pose_i,pose_j)
    closed_list=[]
    
    for bear in filter5:
        frontierLine=[]
        dominators=[]
        bv=dictBlockingAngles[bear]
        bv_tup=(bv[0],bv[1])
        bi=bv[0]
        bj=bv[1]
        bx= -100 + bj * delta + delta/2
        by= -100 + bi * delta + delta/2
        if(G.has_edge(curr_root,bv_tup)):
            posex=pose_x +delta/2
            posey=pose_y +delta/2
            a = (posey - by) / (posex - bx)
            b = posey - a * posex
            scan_area_i= int(pose_i - scan_range/delta)
            while (scan_area_i <= int(pose_i + (scan_range/delta))):
                scan_area_j= int(pose_j - scan_range/delta)
                while(scan_area_j <= int(pose_j + (scan_range/delta))): 
                    px= -100 + scan_area_j * delta + delta/2
                    py= -100 + scan_area_i * delta + delta/2
                    if (((px>bx and px<posex)or (px<bx and px>posex))and((py>by and py<posey)or (py<by and py>posey))):
                        if (abs(py - (a*px+b)) <= epsilon):
                            for blockVert in dictFrontierLines:
                                if(blockVert!=bear):
                                    if([scan_area_i,scan_area_j] in dictFrontierLines[blockVert]):
                                        vbv=dictBlockingAngles[blockVert]
                                        tup_dominant=(vbv[0],vbv[1])
                                        dominators.append(tup_dominant)
                                        #G.remove_node(bv_tup)
                                        #G.add_edge(tup_dominant,bv_tup)
                    scan_area_j+=1
            #print(scan_area_i)
                scan_area_i+=1
            max_l=0
            lev=len(G.predecessors(bv_tup))
            for d in dominators:
                    l=len(G.predecessors(d))
                    if(l==lev):
                        if d in closed_list:
                            max_l=l
                            max_d=d
                    else:    
                        if l>max_l:
                            max_l=l
                            max_d=d
            if(max_l>0):
                G.remove_node(bv_tup)
                G.add_edge(max_d,bv_tup)
            closed_list.append(bv_tup)

     
            
                


    if(goals):
        for goal in goals:
            if(goal not in global_goals):
                #n.add_child(goal)
                global_goals.append(goal)
                tup_goal=(goal[0],goal[1])
                #G.add_node(tup_goal)
                #G.add_edge(tup_pose,tup_goal)

    if (goals):
        publishFrontiers(filter4)
        frontier=goals[0]
        r=dictBlockingAngles[filter5[0]]
        tup_root=(r[0],r[1])
        root.append(tup_root)
        x, y=getcoords(frontier)
        print(x)
        print(y)
        if(check==0):
            plt.clf()
            plt.title("Tree generated")
            pos=graphviz_layout(G,prog='dot')
            nx.draw(G,pos,with_labels=True,arrows=False)
            plt.savefig('nx_test.png')
        sendGoalRectilinear(x,y,tup_pose)
        
    else:
        check=check+1
        explorationcomplete()

    #   explorationcomplete()
    # else:
    


    


        
    scan()
def check8neighbours(curri,currj,rejectedFrontiers):
    if([curri-1,currj-1] in rejectedFrontiers or [curri-1,currj] in rejectedFrontiers or [curri-1,currj +1] in rejectedFrontiers or [curri,currj -1] in rejectedFrontiers or [curri,currj +1] in rejectedFrontiers or [curri+1,currj -1] in rejectedFrontiers or [curri+1,currj] in rejectedFrontiers or [curri+1,currj +1] in rejectedFrontiers):
        return True 

def checkNeighbours(bv,occupancyGridMatFin,rejectedFrontiers,frontier):
    bi=bv[0]
    bj=bv[1]
    valid =0
    if((occupancyGridMatFin[bi-1][bj]==100 or occupancyGridMatFin[bi-2][bj]==100) and (occupancyGridMatFin[bi+1][bj] == 0 ) and  (occupancyGridMatFin[bi+2][bj] == 0) and (occupancyGridMatFin[bi+3][bj] == 0 )  and (occupancyGridMatFin[bi+4][bj] == 0 and [bi+4,bj] not in frontier and [bi+4,bj] not in rejectedFrontiers)):
        valid =1
    if((occupancyGridMatFin[bi+1][bj]==100 or occupancyGridMatFin[bi+2][bj]==100) and (occupancyGridMatFin[bi-1][bj] == 0 ) and  (occupancyGridMatFin[bi-2][bj] == 0) and (occupancyGridMatFin[bi-3][bj] == 0 )  and (occupancyGridMatFin[bi-4][bj] == 0 and [bi-4,bj] not in frontier and [bi-4,bj] not in rejectedFrontiers)):
        valid =1
    if((occupancyGridMatFin[bi][bj-1]==100 or occupancyGridMatFin[bi][bj-2]==100) and (occupancyGridMatFin[bi][bj+1] == 0 ) and  (occupancyGridMatFin[bi][bj+2] == 0) and (occupancyGridMatFin[bi][bj+3] == 0 ) and (occupancyGridMatFin[bi][bj+4] == 0 and [bi,bj+4] not in frontier and [bi,bj+4] not in rejectedFrontiers)):
        valid =1
    if((occupancyGridMatFin[bi][bj+1]==100 or occupancyGridMatFin[bi][bj+2]==100) and (occupancyGridMatFin[bi][bj-1] == 0 ) and  (occupancyGridMatFin[bi][bj-2] == 0) and (occupancyGridMatFin[bi][bj-3] == 0 ) and (occupancyGridMatFin[bi][bj-4] == 0 and [bi,bj-4] not in frontier and [bi,bj-4] not in rejectedFrontiers)):
        valid =1
    #if(( (occupancyGridMatFin[bi][bj-1] == 100 or occupancyGridMatFin[bi][bj-2] == 100 or ) and occupancyGridMatFin[bi][bj+4] == 0 and [bi,bj+4] not in frontier) or (occupancyGridMatFin[bi][bj-4] == 0 and [bi,bj-4] not in frontier) or (occupancyGridMatFin[bi+4][bj] == 0 and [bi+4,bj] not in frontier) or (occupancyGridMatFin[bi-4][bj] == 0 and [bi-4,bj] not in frontier)):
    #   valid =1
        
    return valid


def getFrontiers(pose_x,pose_y,occupancyGridMatFin):
    global count
    global stack
    global visited_poses
    length=800
    delta=0.25
    size=100
    scan_range=40.0
    frontierCells=[]
    frontier=[]
    pose_i = int((round(pose_y,3)/delta + 400))
    pose_j = int((round(pose_x,3)/delta + 400)) 
    scan_area_i= int(pose_i - scan_range/delta)
    while (scan_area_i <= int(pose_i + (scan_range/delta))):
        scan_area_j= int(pose_j - scan_range/delta)
        while(scan_area_j <= int(pose_j + (scan_range/delta))): 
            if (occupancyGridMatFin[scan_area_i][scan_area_j] == 0 and (occupancyGridMatFin[scan_area_i -1][scan_area_j] == -1 or occupancyGridMatFin[scan_area_i][scan_area_j -1] == -1 or occupancyGridMatFin[scan_area_i][scan_area_j +1] == -1 or occupancyGridMatFin[scan_area_i+1][scan_area_j ] == -1) and ( occupancyGridMatFin[scan_area_i +1][scan_area_j+1] != 100 and occupancyGridMatFin[scan_area_i +1][scan_area_j -1] != 100 and occupancyGridMatFin[scan_area_i -1][scan_area_j +1] != 100 and occupancyGridMatFin[scan_area_i -1][scan_area_j-1] != 100 and occupancyGridMatFin[scan_area_i -1][scan_area_j] != 100 and occupancyGridMatFin[scan_area_i][scan_area_j -1] != 100 and occupancyGridMatFin[scan_area_i][scan_area_j +1] != 100 and occupancyGridMatFin[scan_area_i+1][scan_area_j ] != 100)):
                frontierCell=[]
                valid=1
                #This is to make sure that there are no frontiers too close to the obstacles
                count_i=scan_area_i-2
                while(count_i <= scan_area_i+2):
                    count_j=scan_area_j-2
                    while(count_j <= scan_area_j+2):
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
    return frontier


    

def publishFrontiers(frontier):
    delta=0.25
    size=100
    cloud=[]
    for frontierCell in frontier:
        point=[]
        i= frontierCell[0]
        j= frontierCell[1]
        x= (-100 + j * delta) +delta/2
        y= (-100 + i * delta) +delta/2
        point.append(x)
        point.append(y)
        point.append(0.0)
        cloud.append(point)
    cloud_points=cloud
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



def sendGoalRectilinear(x,y,tup_pose):
    global G
    delta=0.25
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
        scan()
    else:
        state = move_base.get_state()
        if state == GoalStatus.SUCCEEDED:
            rospy.loginfo("Goal succeeded!")
            rotateInPlace()
            current_pose=get_pose()
            pose_x=current_pose.position.x
            pose_y=current_pose.position.y
            pose_i = int((round(pose_y,3)/delta + 400))
            pose_j = int((round(pose_x,3)/delta + 400))
            #tup_goal=(pose_i,pose_j)
            #G.add_node(tup_goal)
            #G.add_edge(tup_pose,tup_goal)
            scan()
        else:
            rospy.loginfo("Goal failed with error code: " + str(goal_states[state]))
            scan()
def sendGoal(x,y,frontier,prev_pose):
    global stack
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
            newFrontier=np.delete(frontier,np.s_[1:2], axis=0)
            if (len(newFrontier)<2):
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
            rotateInPlace()
            scan()
        else:
            rospy.loginfo("Goal failed with error code: " + str(goal_states[state]))
            unreachable_poses.append(frontier[0])
            newFrontier=np.delete(frontier,np.s_[1:2], axis=0)
                        
            if (len(newFrontier)<2):
                explorationcomplete()
            else:
                a, b=getcoords(newFrontier)
                #print(newFrontier)
                print(a)
                print(b)
                sendGoal(a,b,newFrontier,prev_pose)

def explorationcomplete():
    #global stack
    ##global root
    #if not root:
    no_nodes=len(global_BVs)+1  #adding 1 for the root
    curr_time=int(math.floor(time.time()))
    d = rospy.wait_for_message("/ExplorationDistance", String)
    dist=d.data
    print(d)
    time_elapsed= curr_time- start_time
    #print("Time elapsed       :  %s  seconds " % (time_elapsed))
    print("Number of nodes  :  %s " % no_nodes)
    print("Exploration Complete")
    sys.exit()
    #else:
    #   prev_root=root.pop()
    #   prev_pos=stack.pop()
    #   print(len(stack))
    #   goal=prev_pos
    #   goal_x = goal.position.x
    #   goal_y = goal.position.y
    #   PrevPos(goal_x,goal_y)
# def getFrontiers(data):
#   linked=[]
#   labels=  np.zeros((length, length))
#   for i in range(0, length):
#       for j in range(0, length):
#           if data[i][j] in frontiers:
#               neighbors

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent=[]

    def add_child(self, obj):
        self.children.append(obj)

    def has_children(self):
        if (self.children):
            return True
        return False

    def add_parent(self, obj):
        self.parent.append(obj)

    def has_children(self):
        if (self.parent):
            return True
        return False


def PrevPos(goal_x,goal_y):
    print("prev pose called")
    length=800
    current_pose=get_pose()
    msg = rospy.wait_for_message("/map", OccupancyGrid)
    grid = msg.data
    occupancyGridMat=np.asarray(grid, dtype=np.int8)
    occupancyGridMatFin=np.reshape(occupancyGridMat, (length, length))
    frontier = getFrontiers(goal_x,goal_y,occupancyGridMatFin)
    if not frontier:
        explorationcomplete()
    else:
        publishFrontiers(frontier)
        #frontier=frontierCells[0]
        x, y=getcoords(frontier)
        print(x)
        print(y)
        sendGoal(x,y,frontier,current_pose)

def getcoords(frontier):
    delta=0.25
    size=100
    frontierCell=frontier
    i= frontierCell[0]
    j= frontierCell[1]
    x= -100 + j * delta
    y= -100 + i * delta
    return(x, y)

def scan():         
    print('Scanning...')
    msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
    callback(msg)


def get_pose():
    pose = rospy.wait_for_message("/robot_pose", Pose)
    return pose

def insert_origin():
    global stack
    global G
    print("Adding origin")
    global root
    delta=0.25
    current_pose=get_pose()
    pose_x=current_pose.position.x
    pose_y=current_pose.position.y
    pose_i = int((round(pose_y,3)/delta + 400))
    pose_j = int((round(pose_x,3)/delta + 400))
    tup_pose=(pose_i,pose_j)
    G.add_node(tup_pose)
    stack.append(current_pose)
    rotateInPlace()
    root.append(tup_pose)
    print(stack)

def rotateInPlace():
    print("This is to make the robot rotate in place!")
    p = rospy.Publisher('cmd_vel', Twist)
    twist = Twist()
    twist.linear.x = 0
    twist.linear.y = 0
    twist.linear.z = 0            
    twist.angular.x = 0
    twist.angular.y = 0  
    twist.angular.z = 0.5
    for i in range(80):
        p.publish(twist)
        rospy.sleep(0.1) 
    #rostopic pub -1 /RosAria/cmd_vel geometry_msgs/Twist '[0.0, 0.0, 0.0]' '[0.0, 0.0, 0.5]'
    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)

class node:
    def __init__( self , parent):
        self.parent=parent

if __name__ == '__main__':
    print('Initialized')
    start_time=time.time()
    rospy.init_node('SubscribeOccupancyGrid', anonymous=True)
    insert_origin()
    scan()