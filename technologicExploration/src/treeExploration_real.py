#!/usr/bin/env python
#launch and get the occupancy grid
import rospy
import string
import roslib;
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

from nav_msgs.srv import GetPlan
from geometry_msgs.msg import PoseStamped,Pose
import cv2
from cv_bridge import CvBridge, CvBridgeError
import pygraphviz as pg
from tf2_msgs.msg import TFMessage
import numpy as np
from collections import deque
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionFeedback, MoveBaseActionResult
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
import thread
from actionlib_msgs.msg import GoalStatusArray
import itertools
from string import ascii_uppercase
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from sensor_msgs.msg import Image
count=0
stack=[]
root=[]
root_robot1=()
root_robot2=()
global_counter=1
unreachable_poses=[]
visited_poses=[]
global_goals=[]
orig_x=0.00
orig_y=0.00
delta=0.25
visited_nodes=[]
assigned_nodes=[]
explored_nodes=[]
global_nodes=[]
under_exploration_nodes=[]
unexplored_nodes=[]
global_frontiers=[]

robot1Goal=()
robot2Goal=()
robot3Goal=()
robot4Goal=()
height=0
width=0
prevStatus1=""
prevStatus2=""
prevStatus3=""
prevStatus4=""
robot1Stack=[]
robot2Stack=[]
robot3Stack=[]
robot4Stack=[]
StatusChecker=[]
prevStatus=[]
sensor_range=4.5

current_status=[]
move_base_list=[]
aborted_list=[]
origin_root=0

global_frontier_goals=[]

list_of_robots=[]
cluster_status=[]

cluster1Status=""
cluster2Status=""
cluster3Status=""
cluster4Status=""

AG=pg.AGraph(directed=False, strict=True)


G=nx.DiGraph()
global_BVs=[]
check=0
start_time=int(math.floor(time.time()))
def callback(data,curr_root,robotsList):
    global global_frontiers
    global origin_root
    global AG
    global count
    global stack
    global visited_poses
    global global_goals
    global G
    global root
    global global_BVs
    global check
    global orig_x
    global orig_y
    global visited_nodes
    global robot1Goal
    global robot2Goal
    global robot1Stack
    global robot2Stack
    global robot3Goal
    global robot4Goal
    global robot3Stack
    global robot4Stack
    global global_root
    global cluster1Status
    global cluster2Status
    global cluster3Status
    global cluster4Status
    global prevStatus1
    global prevStatus2
    global prevStatus3
    global prevStatus4
    global height
    global width
    global global_counter
    global global_nodes
    global delta
    global global_frontier_goals

    allFrontiers=[]

    f=[]
    print("callback called by ")
    for robot in robotsList:
        print(robot)

    edge_length=300
    
    epsilon = 0.5
    frontierCells=[]
    frontier=[]
    rejectedFrontiers=[]
    blockingVertices=[]
    blockingFrontier=[]
    processedFrontiers=[]
    validBlockingVertices=[]
    filter2=[]
    filter3=[]
    filter4=[]
    goals=[]
    filter5=[]
    dictBlockingAngles={}
    dictFrontierLines={}
    dictBVGoals={}
    current_BVs=[]
    
    #Getting the occupancy grid
    grid = data.data
    resolution = data.info.resolution
    height=data.info.height
    width=data.info.width
    orig_x=data.info.origin.position.x
    orig_y=data.info.origin.position.y

    alpha_list=list(string.ascii_uppercase)
    occupancyGridMat=np.asarray(grid, dtype=np.int8)
    occupancyGridMatFin=np.reshape(occupancyGridMat, (height, width))

    pose_x=curr_root[0]
    pose_y=curr_root[1]


    pose_i = int((round(pose_y,2) - orig_y)/delta)
    pose_j = int((round(pose_x,2) - orig_x)/delta)
    #Get the window size
    window_size=int(5/delta)

    #Populating the frontiers
    scan_area_i= 0
    while (scan_area_i <= height-1):
        scan_area_j= 0
        while(scan_area_j <= width-1): 
            if (occupancyGridMatFin[scan_area_i][scan_area_j] == 0 and  ( (scan_area_i==0 or scan_area_j==0 or scan_area_i==height or scan_area_j==width) or (((scan_area_i-1 >=0) and occupancyGridMatFin[scan_area_i -1][scan_area_j] == -1) or ((scan_area_j-1>=0) and occupancyGridMatFin[scan_area_i][scan_area_j -1] == -1) or ((scan_area_j+1<width) and occupancyGridMatFin[scan_area_i][scan_area_j +1]) == -1 or ((scan_area_i+1<height) and occupancyGridMatFin[scan_area_i+1][scan_area_j] == -1)))):
                frontierCell=[]
                frontierCell.append(scan_area_i)
                frontierCell.append(scan_area_j)
                valid=1

                if(((scan_area_i-1>=0 and scan_area_j-1>=0) and occupancyGridMatFin[scan_area_i -1][scan_area_j-1] == 100) or ((scan_area_i-1>=0) and occupancyGridMatFin[scan_area_i -1][scan_area_j] == 100) or ((scan_area_i-1>=0 and scan_area_j+1<width) and occupancyGridMatFin[scan_area_i -1][scan_area_j+1] == 100) or ((scan_area_j-1>=0) and occupancyGridMatFin[scan_area_i][scan_area_j-1] == 100) or ((scan_area_j+1<width) and occupancyGridMatFin[scan_area_i ][scan_area_j+1] == 100) or ((scan_area_i+1<height and scan_area_j-1>=0) and occupancyGridMatFin[scan_area_i +1][scan_area_j-1] == 100) or ((scan_area_i+1<height) and occupancyGridMatFin[scan_area_i +1][scan_area_j] == 100) or ((scan_area_i+1<height and scan_area_j+1<width) and occupancyGridMatFin[scan_area_i +1][scan_area_j+1] == 100)):
                    blockingFrontier.append([scan_area_i,scan_area_j])

                #This is to make sure that there are no frontiers too close to the obstacles
                count_i=scan_area_i-2
                while(count_i <= scan_area_i+2):
                    count_j=scan_area_j-2
                    while(count_j <= scan_area_j+2):
                        if (count_i>=0 and count_j>=0 and count_i<height and count_j<width and occupancyGridMatFin[count_i][count_j]==100):
                            valid=0
                        count_j+=1
                    count_i+=1              
                if (valid==1):
                    frontier.append(frontierCell)
                else:
                    rejectedFrontiers.append(frontierCell)
                allFrontiers.append(frontierCell)
            scan_area_j+=1
        scan_area_i+=1
    #return frontier
    
    for af in allFrontiers:
        fx,fy=getcoords([af[0],af[1]])
        global_frontiers.append([fx,fy])


    listOfFrontiers=[]

    
    scan_area_i= 0
    while (scan_area_i < height-1):
        scan_area_j= 0
        while(scan_area_j < width-1): 
            if (occupancyGridMatFin[scan_area_i][scan_area_j] == 100 and (((scan_area_i-1>=0 and scan_area_j-1>=0) and [scan_area_i-1,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j-1,rejectedFrontiers)) or ((scan_area_i-1>=0) and [scan_area_i-1,scan_area_j] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j,rejectedFrontiers)) or ( (scan_area_i-1>=0 and scan_area_j+1<width) and [scan_area_i-1,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j +1,rejectedFrontiers)) or ((scan_area_j-1>=0) and [scan_area_i,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i,scan_area_j -1,rejectedFrontiers)) or ( (scan_area_j+1<width) and [scan_area_i,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i,scan_area_j +1,rejectedFrontiers)) or ((scan_area_i-1>=0 and scan_area_j-1>=0) and [scan_area_i+1,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j -1,rejectedFrontiers)) or ((scan_area_i+1<height) and [scan_area_i+1,scan_area_j] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j,rejectedFrontiers)) or ( (scan_area_i+1<height and scan_area_j+1<width) and [scan_area_i+1,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j +1,rejectedFrontiers)))):
                blockingVertices.append([scan_area_i,scan_area_j])
            scan_area_j+=1
        scan_area_i+=1

    

    validBlockingVertices=blockingVertices[:]

    for vbv in validBlockingVertices:
        bi=vbv[0]
        bj=vbv[1]
        valid=1
        if ( (bi+2>=height-2 or bj+2>=width or bi-2<=0 or bj-2<=0)or(occupancyGridMatFin[bi-2][bj] == 100 and occupancyGridMatFin[bi][bj-2] == 100)or (bi-2>=0 and occupancyGridMatFin[bi-2][bj] == 100 and occupancyGridMatFin[bi][bj+2] == 100) or (occupancyGridMatFin[bi+2][bj] == 100 and occupancyGridMatFin[bi][bj-2] == 100) or (occupancyGridMatFin[bi+2][bj] == 100 and occupancyGridMatFin[bi][bj+2] == 100) or (occupancyGridMatFin[bi-1][bj] == 100 and occupancyGridMatFin[bi+1][bj] == 100) or (occupancyGridMatFin[bi][bj-1] == 100 and occupancyGridMatFin[bi][bj+1] == 100) or (occupancyGridMatFin[bi][bj-1] == 100 and occupancyGridMatFin[bi][bj+1] == -1) or (occupancyGridMatFin[bi][bj-1] == -1 and occupancyGridMatFin[bi][bj+1] == 100) or (occupancyGridMatFin[bi-1][bj] == 100 and occupancyGridMatFin[bi+1][bj] == -1) or (occupancyGridMatFin[bi-1][bj] == -1 and occupancyGridMatFin[bi+1][bj] == 100)  or  (([bi,bj+2] in allFrontiers or occupancyGridMatFin[bi][bj+2] == -1) and (occupancyGridMatFin[bi][bj-2] == 100 or occupancyGridMatFin[bi][bj-1] == 100))  or (([bi,bj-2] in allFrontiers or occupancyGridMatFin[bi][bj-2] == -1) and (occupancyGridMatFin[bi][bj+2] == 100 or occupancyGridMatFin[bi][bj+1] == 100 ))  or  (([bi+2,bj] in allFrontiers or occupancyGridMatFin[bi+2][bj] == -1) and (occupancyGridMatFin[bi-2][bj] == 100 or occupancyGridMatFin[bi-1][bj] == 100))  or (([bi-2,bj] in allFrontiers or occupancyGridMatFin[bi-2][bj] == -1) and (occupancyGridMatFin[bi+2][bj] == 100 or occupancyGridMatFin[bi+1][bj] == 100))   ):
            valid = 0
        if (valid==1):
            filter2.append(vbv)
    
    for bv in filter2:
        valid = 0
        if(checkNeighbours(bv,occupancyGridMatFin,rejectedFrontiers,frontier)):
            valid=1
        if (valid==1):
            filter3.append(bv)
    filter4=filter3[:]
    for vbv in filter3:
        bi=vbv[0]
        bj=vbv[1]
        for bv in filter3:
            bi1=bv[0]
            bj1=bv[1]
            if(not(bi==bi1 and bj==bj1) and [bi1,bj1] in filter4):
                if(bj==bj1):
                    lower=min(bi,bi1)
                    lower=lower+5
                    higher=max(bi,bi1)
                    remove=1
                    while(lower<higher-5):
                        lower+=1
                        if(occupancyGridMatFin[lower][bj]==100):
                            remove=0
                    if(remove==1):
                        bx,by=getcoords([bi1,bj1])
                        filter4.remove([bi1,bj1])
                elif(bi==bi1):
                    lower=min(bj,bj1)
                    lower=lower+5
                    higher=max(bj,bj1)
                    remove=1
                    while(lower<higher-5):
                        lower+=1
                        if(occupancyGridMatFin[bi][lower]==100 or occupancyGridMatFin[bi][lower]==-1):
                            remove=0
                    if(remove==1):
                        bx,by=getcoords([bi1,bj1])
                        filter4.remove([bi1,bj1])

    for bv in filter4:
        bi=bv[0]
        bj=bv[1]
        bx,by=getcoords(bv)
        bearing= math.atan2(by-pose_y,bx-pose_x)
        dictBlockingAngles[bearing]=[bi,bj]

    filter5=sorted(dictBlockingAngles)


    for bear in filter5:
        frontierLine=[]
        bv=dictBlockingAngles[bear]
        bi=bv[0]
        bj=bv[1]
        f.append(bv)
        bx,by=getcoords(bv)
        bvc=[bx,by]
        invalid_counter=0
        bv_tup=(bx,by)
        posex=pose_x +delta/2
        posey=pose_y +delta/2
        a = (posey - by) / (posex - bx)
        b = posey - a * posex
        invalid_counter=0
        rob=np.array((posex,posey))
        gol=np.array((bx,by))
        dist_gol_to_root=np.linalg.norm(rob-gol)
        if(dist_gol_to_root>5 and origin_root>0):
            invalid_counter+=3
        scan_area_i= 3
        while (scan_area_i <= height-3):
            scan_area_j= 3
            while(scan_area_j <= width-3): 
                px,py=getcoords([scan_area_i,scan_area_j])
                if (((px>bx and px<posex)or (px<bx and px>posex))and((py>by and py<posey)or (py<by and py>posey))):
                    if (abs(py - (a*px+b)) <= epsilon):
                        if(occupancyGridMatFin[scan_area_i][scan_area_j]==-1):
                            invalid_counter+=1
                scan_area_j+=1
            scan_area_i+=1
        if(checkExisting(bvc,occupancyGridMatFin)):
            if(invalid_counter<3):
                f.append(bv)
                counter_to_check=0
                if(bi>4 and occupancyGridMatFin[bi-4][bj] == 100):
                    if(bj>5 and occupancyGridMatFin[bi][bj-5] == 0):
                        clearance=1
                        while(bj-clearance!=0 and occupancyGridMatFin[bi][bj-clearance]!=100):
                            frontierLine.append([bi,bj-clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+5,bj-5])
                        gx,gy=getcoords([bi+5,bj-5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            current_BVs.append(bvc)
                            global_BVs.append(bvc)
                    elif (bj< width-5 and occupancyGridMatFin[bi][bj+5] == 0):
                        clearance=1
                        while(bj+clearance!=width and occupancyGridMatFin[bi][bj+clearance]!=100 and occupancyGridMatFin[bi][bj+clearance]!=100):
                            frontierLine.append([bi,bj+clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+5,bj+5])
                        gx,gy=getcoords([bi+5,bj+5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            current_BVs.append(bvc)
                            global_BVs.append(bvc)
                elif(bi <height-4 and occupancyGridMatFin[bi+4][bj] == 100):
                    if(bj>5 and occupancyGridMatFin[bi][bj-5] == 0):
                        clearance=1
                        while(bj-clearance!=0 and occupancyGridMatFin[bi][bj-clearance]!=100 and occupancyGridMatFin[bi][bj-clearance]!=-1):
                            frontierLine.append([bi,bj-clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-5,bj-5])
                        gx,gy=getcoords([bi-5,bj-5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            global_BVs.append(bvc)
                            current_BVs.append(bvc)
                    elif (bj< width-5 and occupancyGridMatFin[bi][bj+5] == 0):
                        clearance=1
                        while(bj+clearance!=width and occupancyGridMatFin[bi][bj+clearance]!=100 and occupancyGridMatFin[bi][bj+clearance]!=100):
                            frontierLine.append([bi,bj+clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-5,bj+5])
                        gx,gy=getcoords([bi-5,bj+5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            global_BVs.append(bvc)
                            current_BVs.append(bvc)
                elif(bj>4 and occupancyGridMatFin[bi][bj-4] == 100):
                    if(bj>5 and occupancyGridMatFin[bi-5][bj] == 0):
                        clearance=1
                        while(bi-clearance!=0 and occupancyGridMatFin[bi-clearance][bj]!=100 and occupancyGridMatFin[bi-clearance][bj]!=-1):
                            frontierLine.append([bi-clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-5,bj+5])
                        gx,gy=getcoords([bi-5,bj+5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            global_BVs.append(bvc)
                            current_BVs.append(bvc)
                    elif (bi<height-5 and occupancyGridMatFin[bi+5][bj] == 0):
                        clearance=1
                        while(bi+clearance!=height and occupancyGridMatFin[bi+clearance][bj]!=100 and occupancyGridMatFin[bi+clearance][bj]!=-1):
                            frontierLine.append([bi+clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+5,bj+5])
                        gx,gy=getcoords([bi+5,bj+5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            global_BVs.append(bvc)
                            current_BVs.append(bvc)
                elif(bj<width-4 and occupancyGridMatFin[bi][bj+4] == 100):
                    if(bi>5 and occupancyGridMatFin[bi-5][bj] == 0):
                        clearance=1
                        while(bi-clearance!=0 and occupancyGridMatFin[bi-clearance][bj]!=100 and occupancyGridMatFin[bi-clearance][bj]!=-1):
                            frontierLine.append([bi-clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-5,bj-5])
                        gx,gy=getcoords([bi-5,bj-5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            global_BVs.append(bvc)
                            current_BVs.append(bvc)
                    elif (bi<height-5 and occupancyGridMatFin[bi+5][bj] == 0):
                        clearance=1
                        while(bi+clearance!=height and occupancyGridMatFin[bi+clearance][bj]!=100 and occupancyGridMatFin[bi+clearance][bj]!=-1):
                            frontierLine.append([bi+clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+5,bj-5])
                        gx,gy=getcoords([bi+5,bj-5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if (checkGoals(gx,gy)):
                            global_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            global_BVs.append(bvc)
                            current_BVs.append(bvc)
        else:
            print("this node was invalid")

            
    tup_pose=(pose_i,pose_j)
    closed_list=[]
    node_in_tree={}

   
    for bear in filter5:
        frontierLine=[]
        dominators=[]
        bv=dictBlockingAngles[bear]
        invalid_goal=0
        bi=bv[0]
        bj=bv[1]
        bx,by=getcoords([bi,bj])
        bv_tup=(bx,by)
        if(bv_tup in dictBVGoals and G.has_node(dictBVGoals[bv_tup])):
            posex=pose_x +delta/2
            posey=pose_y +delta/2
            a = (posey - by) / (posex - bx)
            b = posey - a * posex
            scan_area_i= 3

            while (scan_area_i <= height-3):
                scan_area_j= 3
                while(scan_area_j <= width-3): 
                    px,py=getcoords([scan_area_i,scan_area_j])
                    if (((px>bx and px<posex)or (px<bx and px>posex))and((py>by and py<posey)or (py<by and py>posey))):
                        if (abs(py - (a*px+b)) <= epsilon):
                            for blockVert in dictFrontierLines:
                                if(blockVert!=bear):
                                    if([scan_area_i,scan_area_j] in dictFrontierLines[blockVert]):
                                        vbv=dictBlockingAngles[blockVert]
                                        vbx,vby=getcoords([vbv[0],vbv[1]])
                                        tupvbv=(vbx,vby)
                                        if(tupvbv in dictBVGoals and G.has_node(dictBVGoals[tupvbv])):
                                            dominators.append(tupvbv)
                    scan_area_j+=1
                scan_area_i+=1
            max_l=0
            lev=getLevel(dictBVGoals[bv_tup],0)
            for d in dominators:
                l=getLevel(dictBVGoals[d],0)   
                if (l>max_l):
                    max_l=l
                    max_d=d

            if(max_l>0):
                G.remove_node(dictBVGoals[bv_tup])
                G.add_edge(dictBVGoals[max_d],dictBVGoals[bv_tup],length=edge_length)
            else:
                print("No dominators")
            closed_list.append(bv_tup)
    
    for frontiercell in allFrontiers:
        
        if(frontiercell in rejectedFrontiers):
            currentFrontier=[]
            currentFrontierCell=frontiercell

            while(check8neighbours(currentFrontierCell[0],currentFrontierCell[1],allFrontiers) and currentFrontierCell not in currentFrontier):
                currentFrontier.append(currentFrontierCell)
                curri=currentFrontierCell[0]
                currj=currentFrontierCell[1]
                processedFrontiers.append(currentFrontierCell)
                if([curri-1,currj-1] in allFrontiers and [curri-1,currj-1] not in currentFrontier and [curri-1,currj-1] not in processedFrontiers):
                    currentFrontierCell=[curri-1,currj-1]
                elif([curri-1,currj] in allFrontiers and [curri-1,currj] not in currentFrontier and [curri-1,currj] not in processedFrontiers):
                    currentFrontierCell=[curri-1,currj]
                elif([curri-1,currj+1] in allFrontiers and [curri-1,currj+1] not in currentFrontier and [curri-1,currj+1] not in processedFrontiers):
                    currentFrontierCell=[curri-1,currj+1]
                elif([curri,currj-1] in allFrontiers and [curri,currj-1] not in currentFrontier and [curri,currj-1] not in processedFrontiers):
                    currentFrontierCell=[curri,currj-1]
                elif([curri,currj+1] in allFrontiers and [curri,currj+1] not in currentFrontier and [curri,currj+1] not in processedFrontiers):
                    currentFrontierCell=[curri,currj+1]
                elif([curri+1,currj-1] in allFrontiers and [curri+1,currj-1] not in currentFrontier and [curri+1,currj-1] not in processedFrontiers):
                    currentFrontierCell=[curri+1,currj-1]
                elif([curri+1,currj] in allFrontiers and [curri+1,currj] not in currentFrontier and [curri+1,currj] not in processedFrontiers):
                    currentFrontierCell=[curri+1,currj]
                elif([curri+1,currj+1] in allFrontiers and [curri+1,currj+1] not in currentFrontier and [curri+1,currj+1] not in processedFrontiers):
                    currentFrontierCell=[curri+1,currj+1]
                else:
                    valid=1
                    for gl in currentFrontier:
                        glx,gly=getcoords(gl)
                        if (checkneighbourBVs(gl,current_BVs)):
                            valid=0
                    if(valid==1):
                        listOfFrontiers.append(currentFrontier)
                    continue
                processedFrontiers.append(currentFrontierCell)

    for frontiercell in allFrontiers:
        
        if(frontiercell not in processedFrontiers):
            currentFrontier=[]
            currentFrontierCell=frontiercell


            while(check8neighbours(currentFrontierCell[0],currentFrontierCell[1],allFrontiers) and currentFrontierCell not in currentFrontier):
                currentFrontier.append(currentFrontierCell)
                curri=currentFrontierCell[0]
                currj=currentFrontierCell[1]
                processedFrontiers.append(currentFrontierCell)
                if([curri-1,currj-1] in allFrontiers and [curri-1,currj-1] not in currentFrontier and [curri-1,currj-1] not in processedFrontiers):
                    currentFrontierCell=[curri-1,currj-1]
                elif([curri-1,currj] in allFrontiers and [curri-1,currj] not in currentFrontier and [curri-1,currj] not in processedFrontiers):
                    currentFrontierCell=[curri-1,currj]
                elif([curri-1,currj+1] in allFrontiers and [curri-1,currj+1] not in currentFrontier and [curri-1,currj+1] not in processedFrontiers):
                    currentFrontierCell=[curri-1,currj+1]
                elif([curri,currj-1] in allFrontiers and [curri,currj-1] not in currentFrontier and [curri,currj-1] not in processedFrontiers):
                    currentFrontierCell=[curri,currj-1]
                elif([curri,currj+1] in allFrontiers and [curri,currj+1] not in currentFrontier and [curri,currj+1] not in processedFrontiers):
                    currentFrontierCell=[curri,currj+1]
                elif([curri+1,currj-1] in allFrontiers and [curri+1,currj-1] not in currentFrontier and [curri+1,currj-1] not in processedFrontiers):
                    currentFrontierCell=[curri+1,currj-1]
                elif([curri+1,currj] in allFrontiers and [curri+1,currj] not in currentFrontier and [curri+1,currj] not in processedFrontiers):
                    currentFrontierCell=[curri+1,currj]
                elif([curri+1,currj+1] in allFrontiers and [curri+1,currj+1] not in currentFrontier and [curri+1,currj+1] not in processedFrontiers):
                    currentFrontierCell=[curri+1,currj+1]
                else:
                    valid=1
                    for gl in currentFrontier:
                        glx,gly=getcoords(gl)
                        if (checkneighbourBVs(gl,current_BVs)):
                            valid=0
                    if(valid==1):
                        listOfFrontiers.append(currentFrontier)
                    continue
                processedFrontiers.append(currentFrontierCell)


    frontierGoalsIntermediate=[elem for elem in listOfFrontiers if len(elem) > 7] 
    
    frontierGoals=[]
    for frontierIntermediate in frontierGoalsIntermediate:
        si=[]
        for fr in frontierIntermediate:
            if (check15neighboursForOccupied(fr[0],fr[1],occupancyGridMatFin)):
                si.append(fr)
                f.append(fr)
        frontierGoals.append(si)


    count_no_of_frontiers=0

    for front in frontierGoals:
        if(front):
            currentFrontierGoals=[]
            for i in range(0,len(front)-1,2):
                goal_front=(front[i])
                gi=goal_front[0]
                gj=goal_front[1]
                gx,gy=getcoords([gi,gj])
                goal_cell=goal_front

                topicName="/"
                topicName+=robotsList[0]
                topicName+="/move_base/NavfnROS/make_plan"
                start_pose=get_pose(robotsList[0])
                rospy.wait_for_service(topicName)
                start = PoseStamped()
                start.header.frame_id = 'map'
                start.pose=start_pose
                #start.pose.position.x = start_pose.position.x
                #start.pose.position.y = start_pose.position.y
                #start.pose.orientation.w = 1

                goal = PoseStamped()
                goal.header.frame_id = 'map'
                goal.pose.position.x = gx
                goal.pose.position.y = gy
                goal.pose.orientation.w = 1

                tolerance=1.0

                move_base_plan = rospy.ServiceProxy(topicName, GetPlan)
                plan_ret = move_base_plan(start,goal,tolerance)

                if(plan_ret.plan.poses):
                    posex=pose_x +delta/2
                    posey=pose_y +delta/2
                    bx,by=getcoords(goal_cell)
                    a = (posey - by) / (posex - bx)
                    b = posey - a * posex
                    invalid_goal=1
                    scan_area_i= 0
                    if(global_counter>1):
                        while (scan_area_i < height):
                            scan_area_j=0
                            while(scan_area_j < width): 
                                px,py=getcoords([scan_area_i,scan_area_j])
                                if (((px>=bx and px<=posex)or (px<=bx and px>=posex))and((py>=by and py<=posey)or (py<=by and py>=posey))):
                                    if (abs(py - (a*px+b)) <= epsilon):
                                        #f.append([scan_area_i,scan_area_j])
                                        if(occupancyGridMatFin[scan_area_i][scan_area_j] ==-1 ):
                                            invalid_goal+=2
                                scan_area_j+=1
                            scan_area_i+=1
                    global_counter+=1
                    rob=np.array((posex,posey))
                    gol=np.array((bx,by))
                    dist_gol_to_root=np.linalg.norm(rob-gol)
                    if(dist_gol_to_root>4.5 and origin_root>0):
                        invalid_goal+=5
                    goals.append(goal_cell)
                    gx,gy=getcoords(goal_cell)
                    goal_tup=(gx,gy)
                    for current_frontier_goal in currentFrontierGoals:
                        d=computeDistance(current_frontier_goal,goal_tup)
                        if(d<sensor_range):
                            invalid_goal+=5
                    if (checkGoals(gx,gy)):
                        if(invalid_goal<5):
                            global_goals.append(goal_tup)
                            currentFrontierGoals.append(goal_tup)
                            global_frontier_goals.append(goal_tup)
                            AG.add_edge(curr_root,goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup,length=edge_length)
                            #break
                    #else:
                        #break
                    #rospy.sleep(1.0)
    number_of_labels=len(G)
    #labels=list(islice(multiletters(ascii_uppercase),10))
    labels={}
    counter=0

    for n in G.nodes():
        if n not in global_nodes:
            global_nodes.append(n)

    for s in iter_all_strings():
        node_to_label=global_nodes[counter]
        AG.get_node(node_to_label).attr['label'] = s
        labels[node_to_label]=s
        counter+=1
        if counter == number_of_labels:
            break
    topic = '/visualization_marker_array'
    MarkerPublisher = rospy.Publisher(topic, MarkerArray)
    markerArray = MarkerArray()
    for n in global_nodes:
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.type = marker.TEXT_VIEW_FACING
        marker.text=labels[n]
        marker.scale.z = 1.5
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x=n[0]
        marker.pose.position.y=n[1]
        marker.pose.position.z=0
        markerArray.markers.append(marker)
        id=0
        for m in markerArray.markers:
            m.id = id
            id += 1
        MarkerPublisher.publish(markerArray)
        rospy.sleep(0.01)
    plt.clf()
    #plt.figure(figsize=(1,1))
    


    #P.figure(figsize=(20,20))
    AG.write('ademo.dot')

    # pygraphviz renders graphs in neato by default, 
    # so you need to specify dot as the layout engine
    AG.layout(prog='dot')

    plt.title("Tree generated")
    #pos=graphviz_layout(G,prog='neato')
    pos=graphviz_layout(G,prog='dot',args='-Eminlen=5 -Gnodesep=25')
    #nx.draw(G,pos,with_labels=False,arrows=False,font_size=16)
    nx.draw(G, pos=pos,node_size=500, with_labels=False,arrows=False,)
    nx.draw_networkx_nodes(G,pos,node_color='r',node_size=500)
    nx.draw_networkx_edges(G,pos,width=3.0,alpha=0.5,arrows=False,length=edge_length)
    #nx.draw_networkx_labels(G,pos,labels,font_size=16)
    nx.draw_networkx_labels(G,pos, labels,font_size=12)
    
    #tree_name="tree"
    #+=str(global_counter)
    #tree_name+=".pdf"
    #plt.show()
    plt.savefig("tree_generated.png")

    #TreeImagePub = rospy.Publisher('TreeImage', Image, queue_size=10)
    #treeImg=

    node_in_tree={}
    
    actual_successors=G.successors(curr_root)
    #publishFrontiers(f)
    origin_root+=1
    assignGoals(curr_root,actual_successors,robotsList,occupancyGridMatFin)


def computeDistance(p1,p2):
    gol1=np.array((p1[0],p1[1]))
    gol2=np.array((p2[0],p2[1]))
    dist_gol_to_root=np.linalg.norm(gol1-gol2)
    return dist_gol_to_root

def checkGoals(gx,gy):
    global global_goals
    for goal in global_goals:
        gol1=np.array((goal[0],goal[1]))
        gol2=np.array((gx,gy))
        dist_gol_to_root=np.linalg.norm(gol1-gol2)
        if(dist_gol_to_root<1.5):
            return False
    return True



def assignGoals(curr_root,actual_successors,robotsList,occupancyGridMatFin):
    global G
    global global_goals
    global assigned_nodes
    global move_base_list
    global global_frontiers
    global global_frontier_goals
    print("goals to assign to")
    print(robotsList)
    r=len(robotsList)
    succ = actual_successors[:]
    listOfRobots=robotsList[:]
    under_exploration_successors=[]
    print("before filter")
    print(len(succ))
    for s in actual_successors:
        goal_tup=s
        gi,gj=getindices(goal_tup)
        #print(goal_tup in assigned_nodes or gi==0 or gj==0 or gi==height or gj==width or  occupancyGridMatFin[gi-1][gj]==-1 or occupancyGridMatFin[gi][gj-1]==-1 or occupancyGridMatFin[gi+1][gj]==-1 or occupancyGridMatFin[gi][gj+1]==-1)
        if(s in explored_nodes):
            succ.remove(s)
        elif(s in under_exploration_nodes):
            under_exploration_successors.append(s)                
            succ.remove(s)
        elif(notFrontier(gi,gj,occupancyGridMatFin) and goal_tup in global_frontier_goals):
            explored_nodes.append(s)
            succ.remove(s)

    print("number of un-explored goals")
    s=len(succ)
    print(s)
    if(under_exploration_successors):
        print("number of under-exploration goals")
        s=len(under_exploration_successors)

    us=len(under_exploration_successors)
    listOfSuccessors=succ[:]
    listOfUnexploredSuccessors=under_exploration_successors[:]
    #sendGoalsToRobots(succ)

    if(succ):
        if(s==1):
            goal_tup=succ[0]
            next_root=goal_tup
            counter=0
            under_exploration_nodes.append(goal_tup)
            for robot in listOfRobots:
                index_robot = int(robot[-1])-1
                assigned_nodes[index_robot]=next_root
                sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
                gi,gj=getindices(goal_tup)
                if (gi>2 and occupancyGridMatFin[gi-2][gj]==0):
                    gfx,gfy=getcoords([gi-2,gj])
                    if([gfx,gfy] not in global_frontiers):
                        goal_tup=getcoords([gi-2,gj])  
                elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                    gfx,gfy=getcoords([gi+2,gj])
                    if([gfx,gfy] not in global_frontiers):
                        goal_tup=getcoords([gi+2,gj])
                elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                    gfx,gfy=getcoords([gi,gj-2])
                    if([gfx,gfy] not in global_frontiers):
                        goal_tup=getcoords([gi,gj-2]) 
                elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                    gfx,gfy=getcoords([gi,gj+2])
                    if([gfx,gfy] not in global_frontiers):
                        goal_tup=getcoords([gi,gj+2]) 
            checkStatus()
        elif(s==2):
            if(r==1):
                robot=listOfRobots[0]
                # if(robot in ("robot1","robot3","robot5","robot7")):
                #     goal_tup=succ[0]
                # else:
                goal_tup=succ[0]
                next_root=goal_tup
                index_robot = int(robot[-1])-1
                assigned_nodes[index_robot]=next_root
                cluster_status[index_robot]=1
                under_exploration_nodes.append(next_root)
                sendGoalRectilinear(next_root,goal_tup,listOfRobots[0],occupancyGridMatFin)
            else:
                goal_tup1=succ[1]
                next_root1=goal_tup1
                goal_tup2=succ[0]
                next_root2=goal_tup2
                under_exploration_nodes.append(goal_tup1)
                under_exploration_nodes.append(goal_tup2)
                counter=0
                for index, robot in enumerate(listOfRobots):
                    if index < len(listOfRobots)/2:
                        index_robot = int(robot[-1])-1
                        if(cluster_status[index_robot]>=2):
                            cluster_status[index_robot]/=2
                        assigned_nodes[index_robot]=next_root1
                        sendGoalRectilinear(next_root1,goal_tup1,robot,occupancyGridMatFin)
                        gi,gj=getindices(goal_tup1)
                        if (gi>1 and occupancyGridMatFin[gi-2][gj]==0):
                            goal_tup1=getcoords([gi-2,gj])
                        elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                            goal_tup1=getcoords([gi+2,gj])
                        elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                            goal_tup1=getcoords([gi,gj-2])
                        elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                            goal_tup1=getcoords([gi,gj+2])
                    else:
                        index_robot = int(robot[-1])-1
                        if(cluster_status[index_robot]>=2):
                            cluster_status[index_robot]/=2
                        assigned_nodes[index_robot]=next_root2
                        sendGoalRectilinear(next_root2,goal_tup2,robot,occupancyGridMatFin)
                        gi,gj=getindices(goal_tup2)
                        if (gi>1 and occupancyGridMatFin[gi-2][gj]==0):
                            goal_tup2=getcoords([gi-2,gj])
                        elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                            goal_tup2=getcoords([gi+2,gj])
                        elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                            goal_tup2=getcoords([gi,gj-2])
                        elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                            goal_tup2=getcoords([gi,gj+2])
            checkStatus()
        elif(s<=r):
            for successor in succ:
                if(len(listOfSuccessors)>1):
                    goal_tup=successor
                    next_root=goal_tup
                    under_exploration_nodes.append(goal_tup)
                    listOfSuccessors.remove(successor)
                    robot=listOfRobots[0]
                    index_robot = int(robot[-1])-1
                    cluster_status[index_robot]=1
                    assigned_nodes[index_robot]=next_root
                    listOfRobots.remove(robot)
                    sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
                else:
                    goal_tup=listOfSuccessors[0]
                    under_exploration_nodes.append(goal_tup)
                    next_root=goal_tup
                    for robot in listOfRobots:
                        index_robot = int(robot[-1])-1
                        cluster_status[index_robot]=len(listOfRobots)
                        assigned_nodes[index_robot]=next_root
                        sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
                        gi,gj=getindices(goal_tup)
                        if (gi>1 and occupancyGridMatFin[gi-2][gj]==0):
                            goal_tup=getcoords([gi-2,gj])
                        elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                            goal_tup=getcoords([gi+2,gj])
                        elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                            goal_tup=getcoords([gi,gj-2])
                        elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                            goal_tup=getcoords([gi,gj+2])
            checkStatus()
        elif(s>r):
            counter=0
            for robot in robotsList:
                goal_tup=listOfSuccessors[counter]
                next_root=goal_tup
                under_exploration_nodes.append(goal_tup)
                index_robot = int(robot[-1])-1
                cluster_status[index_robot]=1
                assigned_nodes[index_robot]=next_root
                counter+=1
                sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
            checkStatus()
    elif(under_exploration_successors):
        if(us==1):
            goal_tup=under_exploration_successors[0]
            next_root=goal_tup
            gi,gj=getindices(goal_tup)
            if(goal_tup in assigned_nodes or not notFrontier(goal_tup[0],goal_tup[1],occupancyGridMatFin)):
                for robot in listOfRobots:
                    index_robot = int(robot[-1])-1
                    assigned_nodes[index_robot]=next_root
                    sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
                    gi,gj=getindices(goal_tup)
                    if (gi>1 and occupancyGridMatFin[gi-2][gj]==0):
                        goal_tup=getcoords([gi-2,gj])
                    elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                        goal_tup=getcoords([gi+2,gj])
                    elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                        goal_tup=getcoords([gi,gj-2])
                    elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                        goal_tup=getcoords([gi,gj+2])
                checkStatus()
            else:
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                callback(msg,goal_tup,listOfRobots)      
        elif(us==2):
            if(r==1):
                robot=listOfRobots[0]
                if(robot in ("robot1","robot3","robot5","robot7")):
                    goal_tup=under_exploration_successors[0]
                else:
                    goal_tup=under_exploration_successors[1]
                next_root=goal_tup
                index_robot = int(robot[-1])-1
                assigned_nodes[index_robot]=next_root
                gi,gj=getindices(goal_tup)
                if(goal_tup in assigned_nodes or not notFrontier(goal_tup[0],goal_tup[1],occupancyGridMatFin)):
                    sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
                else:
                    msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                    callback(msg,goal_tup,listOfRobots)
            else:
                goal_tup1=under_exploration_successors[1]
                next_root1=goal_tup1
                goal_tup2=under_exploration_successors[0]
                next_root2=goal_tup2
                for index, robot in enumerate(listOfRobots):
                    if index <= len(listOfRobots)/2:
                        index_robot = int(robot[-1])-1
                        assigned_nodes[index_robot]=next_root1
                        sendGoalRectilinear(next_root1,goal_tup1,robot,occupancyGridMatFin)
                        gi,gj=getindices(goal_tup1)
                        if (gi>1 and occupancyGridMatFin[gi-2][gj]==0):
                            goal_tup=getcoords([gi-2,gj])
                        elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                            goal_tup=getcoords([gi+2,gj])
                        elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                            goal_tup=getcoords([gi,gj-2])
                        elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                            goal_tup=getcoords([gi,gj+2])
                    else:
                        index_robot = int(robot[-1])-1
                        assigned_nodes[index_robot]=next_root2
                        sendGoalRectilinear(next_root2,goal_tup2,robot,occupancyGridMatFin)
                        gi,gj=getindices(goal_tup2)
                        if (gi>1 and occupancyGridMatFin[gi-2][gj]==0):
                            goal_tup=getcoords([gi-2,gj])
                        elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                            goal_tup=getcoords([gi+2,gj])
                        elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                            goal_tup=getcoords([gi,gj-2])
                        elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                            goal_tup=getcoords([gi,gj+2])
            checkStatus()
        elif(us<=r):
            for successor in under_exploration_successors:
                if(len(listOfUnexploredSuccessors)>1):
                    goal_tup=successor
                    under_exploration_nodes.append(goal_tup)
                    listOfUnexploredSuccessors.remove(successor)
                    robot=listOfRobots[0]
                    index_robot = int(robot[-1])-1
                    assigned_nodes[index_robot]=next_root
                    listOfRobots.remove(robot)
                    gi,gj=getindices(goal_tup)
                    if(goal_tup in assigned_nodes or not notFrontier(goal_tup[0],goal_tup[1],occupancyGridMatFin)):
                        sendGoalRectilinear(goal_tup,robot,occupancyGridMatFin)
                    else:
                        msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                        callback(msg,goal_tup,robotsList)
                else:
                    goal_tup=under_exploration_successors[0]
                    next_root=goal_tup
                    gi,gj=getindices(goal_tup)
                    if(goal_tup in assigned_nodes or not notFrontier(goal_tup[0],goal_tup[1],occupancyGridMatFin)):
                        for robot in listOfRobots:
                            index_robot = int(robot[-1])-1
                            assigned_nodes[index_robot]=next_root
                            sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
                            gi,gj=getindices(goal_tup)
                            if (gi>1 and occupancyGridMatFin[gi-2][gj]==0):
                                goal_tup=getcoords([gi-2,gj])
                            elif(gi<height-2 and occupancyGridMatFin[gi+2][gj]==0):
                                goal_tup=getcoords([gi+2,gj])
                            elif(gj>2 and occupancyGridMatFin[gi][gj-2]==0):
                                goal_tup=getcoords([gi,gj-2])
                            elif(gj<width-2 and occupancyGridMatFin[gi][gj+2]==0):
                                goal_tup=getcoords([gi,gj+2])
                    else:
                        msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                        callback(msg,goal_tup,robotsList)
            checkStatus()
        elif(us>r):
            counter=0
            for robot in robotsList:
                goal_tup=listOfUnexploredSuccessors[counter]
                next_root=goal_tup
                index_robot = int(robot[-1])-1
                assigned_nodes[index_robot]=next_root
                counter+=1
                sendGoalRectilinear(next_root,goal_tup,robot,occupancyGridMatFin)
            checkStatus()
    else:
        print("no more goals to explore , this node has been explored")
        explored_nodes.append(curr_root)
        if(len(explored_nodes)!=len(global_goals)):
            prev_root_list=G.predecessors(curr_root)
            if(prev_root_list):
                print("heading out to a previous goal")  
                prev_root=prev_root_list[0]
                print(prev_root)
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                callback(msg,prev_root,robotsList)
            else:
                explorationcomplete()
    checkStatus()

def checkneighbourBVs(gl,BVs):
    global delta
    gi,gj=getcoords(gl)
    checkAreai=gi-0.5
    while (checkAreai <= gi+0.5):
        checkAreaj=gj-0.5
        while(checkAreaj <= gj+0.5):
            if([checkAreai,checkAreaj] in BVs):
                print("found existing")
                return True
            checkAreaj+=delta
        checkAreai+=delta


def notFrontier(curri,currj,occupancyGridMatFin):
    scan_area_i= curri-4
    while (scan_area_i <= curri+4):
        scan_area_j= currj-4
        while(scan_area_j <= currj+4): 
            if(scan_area_i>=0 and scan_area_j>=0 and scan_area_j<width and scan_area_i<height):
                #print("didn't get in")
                if(occupancyGridMatFin[scan_area_i][scan_area_j]==-1 or scan_area_i==0 and scan_area_j==0 and scan_area_j==width-1 and scan_area_i==height-1):
                    #print("should be false")
                    return False
            scan_area_j+=1
        scan_area_i+=1
    return True

def check15neighboursForOccupied(curri,currj,occupancyGridMatFin):
    scan_area_i= curri-3
    while (scan_area_i <= curri+3):
        scan_area_j= currj-3
        while(scan_area_j <= currj+3): 
            if(scan_area_i>=0 and scan_area_j>=0 and scan_area_j<width and scan_area_i<height):
                #print("didn't get in")
                if(occupancyGridMatFin[scan_area_i][scan_area_j]==100):
                    #print("should be false")
                    return False
            scan_area_j+=1
        scan_area_i+=1
    return True

def checkStatus():
    rospy.loginfo("Checking status!")
    global move_base_list
    global list_of_robots
    global aborted_list
    global G
    counter=1
    if(move_base_list):
        for move_base in move_base_list:
            goal_states = ['PENDING', 'ACTIVE', 'PREEMPTED', 'SUCCEEDED', 'ABORTED', 'REJECTED','PREEMPTING', 'RECALLING', 'RECALLED','LOST']
            failed_states=['ABORTED', 'REJECTED','RECALLED','LOST']
            move_base.wait_for_server(rospy.Duration(60))
            robot="robot"
            robot+=str(counter)
            index_robot=counter-1
            next_root=assigned_nodes[index_robot]
            state = move_base.get_state()
            print("THIS IS THE CURRENT STATE:")
            print(state)
            current_status=cluster_status[move_base_list.index(move_base)]
            if (state == GoalStatus.SUCCEEDED and StatusChecker[index_robot]>2):
                StatusChecker[index_robot]=0
                rotateInPlace(robot)
                print("reached goal : going to call callback with this root")
                print(next_root)
                #rotateInPlace(robot)
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                print(robot)
                print(current_status)
                print(index_robot)
                if(current_status==8):
                    callback(msg,next_root,list_of_robots[:])
                elif(current_status==4):
                    if(index_robot in (0,1,2,3)):
                        callback(msg,next_root,list_of_robots[0:4])
                    else:
                        callback(msg,next_root,list_of_robots[4:8])
                elif(current_status==2):
                    if(index_robot in (0,1)):
                        callback(msg,next_root,list_of_robots[0:2])
                    elif(index_robot in (2,3)):
                        callback(msg,next_root,list_of_robots[2:4])
                    elif(index_robot in (4,5)):
                        callback(msg,next_root,list_of_robots[4:6])
                    elif(index_robot in (6,7)):
                        callback(msg,next_root,list_of_robots[6:8])
                else:
                    callback(msg,next_root,list_of_robots[index_robot:index_robot+1])
            elif(state in (GoalStatus.ABORTED,GoalStatus.REJECTED,GoalStatus.RECALLED,GoalStatus.LOST)):
                aborted_list[index_robot]=1
                if(current_status==8):
                    if(all(i == 1 for i in aborted_list)):
                        prev_root_list=G.predecessors(next_root)
                        print("ABORTED: heading out to a previous goal")
                        prev_root=prev_root_list[0]
                        print(prev_root)
                        #G.remove_node(next_root)
                        msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                        callback(msg,next_root,list_of_robots[:])
                elif(current_status==4):
                    if(index_robot in (0,1,2,3)):
                        working_list=aborted_list[0:4]
                        if(all(i == 1 for i in working_list)):
                            prev_root_list=G.predecessors(next_root)
                            print("ABORTED: heading out to a previous goal")
                            prev_root=prev_root_list[0]
                            print(prev_root)
                            #G.remove_node(next_root)
                            msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                            callback(msg,next_root,list_of_robots[0:4])
                    else:
                        working_list=aborted_list[4:8]
                        if(all(i == 1 for i in working_list)):
                            prev_root_list=G.predecessors(next_root)
                            print("ABORTED: heading out to a previous goal")
                            prev_root=prev_root_list[0]
                            print(prev_root)
                            #G.remove_node(next_root)
                            msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                            callback(msg,next_root,list_of_robots[4:8])
                elif(current_status==2):
                    if(index_robot in (0,1)):
                        working_list=aborted_list[0:2]
                        if(all(i == 1 for i in working_list)):
                            prev_root_list=G.predecessors(next_root)
                            print("ABORTED: heading out to a previous goal")
                            prev_root=prev_root_list[0]
                            print(prev_root)
                            #G.remove_node(next_root)
                            msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                            callback(msg,next_root,list_of_robots[0:2])
                    elif(index_robot in (2,3)):
                        working_list=aborted_list[2:4]
                        if(all(i == 1 for i in working_list)):
                            prev_root_list=G.predecessors(next_root)
                            print("ABORTED: heading out to a previous goal")
                            prev_root=prev_root_list[0]
                            print(prev_root)
                            #G.remove_node(next_root)
                            msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                            callback(msg,next_root,list_of_robots[2:4])
                    elif(index_robot in (4,5)):
                        working_list=aborted_list[4:6]
                        if(all(i == 1 for i in working_list)):
                            prev_root_list=G.predecessors(next_root)
                            print("ABORTED: heading out to a previous goal")
                            prev_root=prev_root_list[0]
                            print(prev_root)
                            #G.remove_node(next_root)
                            msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                            callback(msg,next_root,list_of_robots[4:6])
                    elif(index_robot in (6,7)):
                        working_list=aborted_list[6:8]
                        if(all(i == 1 for i in working_list)):
                            prev_root_list=G.predecessors(next_root)
                            print("ABORTED: heading out to a previous goal")
                            prev_root=prev_root_list[0]
                            print(prev_root)
                            #G.remove_node(next_root)
                            msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                            callback(msg,next_root,list_of_robots[6:8])
                else:
                    prev_root_list=G.predecessors(next_root)
                    explored_nodes.append(next_root)
                    print("ABORTED: heading out to a previous goal")
                    prev_root=prev_root_list[0]
                    print(prev_root)
                    #G.remove_node(next_root)
                    msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                    callback(msg,next_root,list_of_robots[index_robot:index_robot+1])
            else:
                StatusChecker[index_robot]+=1
            counter+=1
        #rospy.loginfo("Goals Active! let's check again!")
        rospy.sleep(2)
        checkStatus()


def getLevel(d1,lev):
    global G
    d=G.predecessors(d1)
    level=lev+1
    if(d):
        getLevel(d[0],level)
    return level

def check8neighbours(curri,currj,rejectedFrontiers):
    if([curri-1,currj-1] in rejectedFrontiers or [curri-1,currj] in rejectedFrontiers or [curri-1,currj +1] in rejectedFrontiers or [curri,currj -1] in rejectedFrontiers or [curri,currj +1] in rejectedFrontiers or [curri+1,currj -1] in rejectedFrontiers or [curri+1,currj] in rejectedFrontiers or [curri+1,currj +1] in rejectedFrontiers):
        return True 
    return False

def check8neighboursForOccupied(curri,currj,occupancyGridMatFin):
    if(occupancyGridMatFin[curri-1][currj-1]==100 or occupancyGridMatFin[curri-1][currj]==100 or occupancyGridMatFin[curri-1][currj+1]==100 or occupancyGridMatFin[curri][currj-1]==100 or occupancyGridMatFin[curri][currj+1]==100 or occupancyGridMatFin[curri+1][currj-1]==100 or occupancyGridMatFin[curri+1][currj]==100 or occupancyGridMatFin[curri+1][currj+1]==100):
        return False 
    return True    


def checkNeighbours(bv,occupancyGridMatFin,rejectedFrontiers,frontier):
    bi=bv[0]
    bj=bv[1]
    valid =0
    if((occupancyGridMatFin[bi-1][bj]==100 or occupancyGridMatFin[bi-2][bj]==100) and (occupancyGridMatFin[bi+1][bj] == 0 ) and  (occupancyGridMatFin[bi+2][bj] == 0) and (occupancyGridMatFin[bi+3][bj] == 0 )  and (occupancyGridMatFin[bi+4][bj] == 0 and [bi+4,bj] not in frontier and [bi+4,bj] not in rejectedFrontiers and check8neighboursForOccupied(bi+4,bj,occupancyGridMatFin))):
        valid =1
    if((occupancyGridMatFin[bi+1][bj]==100 or occupancyGridMatFin[bi+2][bj]==100) and (occupancyGridMatFin[bi-1][bj] == 0 ) and  (occupancyGridMatFin[bi-2][bj] == 0) and (occupancyGridMatFin[bi-3][bj] == 0 )  and (occupancyGridMatFin[bi-4][bj] == 0 and [bi-4,bj] not in frontier and [bi-4,bj] not in rejectedFrontiers and check8neighboursForOccupied(bi-4,bj,occupancyGridMatFin))):
        valid =1
    if((occupancyGridMatFin[bi][bj-1]==100 or occupancyGridMatFin[bi][bj-2]==100) and (occupancyGridMatFin[bi][bj+1] == 0 ) and  (occupancyGridMatFin[bi][bj+2] == 0) and (occupancyGridMatFin[bi][bj+3] == 0 ) and (occupancyGridMatFin[bi][bj+4] == 0 and [bi,bj+4] not in frontier and [bi,bj+4] not in rejectedFrontiers and check8neighboursForOccupied(bi,bj+4,occupancyGridMatFin))):
        valid =1
    if((occupancyGridMatFin[bi][bj+1]==100 or occupancyGridMatFin[bi][bj+2]==100) and (occupancyGridMatFin[bi][bj-1] == 0 ) and  (occupancyGridMatFin[bi][bj-2] == 0) and (occupancyGridMatFin[bi][bj-3] == 0 ) and (occupancyGridMatFin[bi][bj-4] == 0 and [bi,bj-4] not in frontier and [bi,bj-4] not in rejectedFrontiers and check8neighboursForOccupied(bi,bj-4,occupancyGridMatFin))):
        valid =1
    #if(( (occupancyGridMatFin[bi][bj-1] == 100 or occupancyGridMatFin[bi][bj-2] == 100 or ) and occupancyGridMatFin[bi][bj+4] == 0 and [bi,bj+4] not in frontier) or (occupancyGridMatFin[bi][bj-4] == 0 and [bi,bj-4] not in frontier) or (occupancyGridMatFin[bi+4][bj] == 0 and [bi+4,bj] not in frontier) or (occupancyGridMatFin[bi-4][bj] == 0 and [bi-4,bj] not in frontier)):
    #   valid =1
        
    return valid


def checkNearbyFrontieirs(curri,currj,occupancyGridMatFin):
    global height
    global width
    scan_area_i= curri-5
    while (scan_area_i <= curri+5):
        scan_area_j= currj-5
        while(scan_area_j <= currj+5): 
            if(scan_area_i>=0 and scan_area_j>=0 and scan_area_j<width and scan_area_i<height):
                #print("didn't get in")
                if(occupancyGridMatFin[scan_area_i][scan_area_j]==0):
                    #print("should be false")
                    return False
            scan_area_j+=1
        scan_area_i+=1
    return True

def checkExisting(bvc,occupancyGridMatFin):
    print("check existing called")
    global global_BVs
    global delta
    global height
    global width
    global orig_x
    global orig_y
    #f=[]
    bi=(bvc[1] - orig_y)/delta
    bj=(bvc[0] - orig_x)/delta

    checkAreai=bi-3
    while (checkAreai <= bi+3):
        checkAreaj=bj-3
        while(checkAreaj <= bj+3):
            #f.append([checkAreai,checkAreaj])
            if(checkAreai>=0 and checkAreaj>=0 and checkAreaj<width and checkAreai<height):
                check_x,check_y=getcoords([checkAreai,checkAreaj]) 
                if([check_x,check_y] in global_BVs):
                    #publishFrontiers(f)
                    print("found existing")
                    return False
            checkAreaj+=1
        checkAreai+=1
    print("not found earlier")
    valid=False
    if(bi+5>=height or occupancyGridMatFin[bi+5][bj]==-1 or bi-5<=0 or occupancyGridMatFin[bi-5][bj]==-1 or bj+5>=width or occupancyGridMatFin[bi][bj+5]==-1 or bj-5<=0 or occupancyGridMatFin[bi][bj-5]==-1):
        valid=True
    if(valid):
        return True
    return False


def getFrontiers(pose_x,pose_y,occupancyGridMatFin):
    global count
    global stack
    global visited_poses
    global delta
    length=800
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
    global orig_x
    global orig_y
    global delta
    size=100
    print(orig_x)
    print(orig_y)
    cloud=[]
    print(frontier)
    for frontierCell in frontier:
        point=[]
        i= frontierCell[0]
        j= frontierCell[1]
        x= (orig_x + j * delta) + delta/2
        y= (orig_y + i * delta) + delta/2
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



def sendGoalRectilinear(next_root,tup_goal,robotName,occupancyGridMatFin):
    global G
    global move_base_list
    print("in goal")
    print(tup_goal)
    print(robotName)
    index_robot = int(robotName[-1])-1
    goal_states = ['PENDING', 'ACTIVE', 'PREEMPTED', 
                       'SUCCEEDED', 'ABORTED', 'REJECTED',
                       'PREEMPTING', 'RECALLING', 'RECALLED',
                       'LOST']
    topicName="/"
    topicName+=robotName
    topicName+="/move_base"
    move_base = actionlib.SimpleActionClient(topicName, MoveBaseAction)
    rospy.loginfo("Waiting for move_base action server...")
    move_base.wait_for_server(rospy.Duration(300))
    rospy.loginfo("Connected to move base server")
    rospy.loginfo("Starting Exploration")
    #while not rospy.is_shutdown():
    goal = MoveBaseGoal()
    goal.target_pose.pose.position.x = (tup_goal[0])
    goal.target_pose.pose.position.y = (tup_goal[1])
    goal.target_pose.pose.orientation.w = 1
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    move_base_list[index_robot]=(move_base)
    rospy.loginfo("Goal Set!")
    move_base.send_goal(goal)


def explorationcomplete():
    #global stack
    ##global root
    #if not root:
    print("Exploration Complete")
    sys.exit()
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
        #publishFrontiers(frontier)
        #frontier=frontierCells[0]
        x, y=getcoords(frontier)
        print(x)
        print(y)
        sendGoal(x,y,frontier,current_pose)

def getcoords(frontier):
    global orig_x
    global orig_y
    global delta
    i= frontier[0]
    j= frontier[1]
    x= orig_x + (j * delta)
    y= orig_y + (i * delta)
    return(x, y)

def getindices(frontier):
    global orig_x
    global orig_y
    global delta
    x= frontier[0]
    y= frontier[1]
    j = (x - orig_x)/delta
    i = (y - orig_y)/delta
    return(i, j)

def scan(curr_root,no_of_robs):
    global G
    global list_of_robots
    global cluster_status
    global StatusChecker
    global prevStatus
    global assigned_nodes
    global current_status
    global move_base_list
    global aborted_list
    print('Scanning...')
    robotsList=[]
    counter=1
    G.add_node(curr_root)
    print("number of ROBOTS")
    print(no_of_robs)
    while(counter<=int(no_of_robs)):
        rob="robot" + str(counter)
        rotateInPlace(rob)
        robotsList.append(rob)
        print("counter   :  "+str(counter))
        counter+=1
    try:
        msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
    except:
        print("Exception thrown")
    total_no_of_robots=len(robotsList)
    list_of_robots=robotsList[:]
    cluster_status=[total_no_of_robots] * total_no_of_robots
    StatusChecker=[0] * total_no_of_robots
    current_status=[0] * total_no_of_robots
    move_base_list=[None] * total_no_of_robots
    aborted_list=[0] * total_no_of_robots
    prevStatus=[""] * total_no_of_robots    
    assigned_nodes=[curr_root] * total_no_of_robots
    callback(msg,curr_root,robotsList)
   

def get_pose(robotName):
    top="/"
    top+=str(robotName)
    top+="/pose"
    pose = rospy.wait_for_message(top, Pose)
    return pose

def insert_origin():
    global stack
    global G
    print("Adding origin")
    global root
    global delta
    origin=get_pose("robot1")
    tup_pose=(origin.position.x,origin.position.y)
    print(tup_pose)
    G.add_node(tup_pose)
    root=tup_pose
    return tup_pose

def iter_all_strings():
    size = 1
    while True:
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)
        size +=1

def rotateInPlace(robotName):
    print("This is to make the robot rotate in place!")
    top='/'
    top+=robotName
    top+='/cmd_vel'
    print(str(top))
    p = rospy.Publisher(top, Twist)
    twist = Twist()
    twist.linear.x = 0
    twist.linear.y = 0
    twist.linear.z = 0            
    twist.angular.x = 0
    twist.angular.y = 0  
    twist.angular.z = 0.5
    for i in range(60):
        p.publish(twist)
        rospy.sleep(0.1) 

    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    print('Initialized')
    no_of_robs=sys.argv[1]
    start_time=time.time()
    rospy.init_node('SubscribeOccupancyGrid', anonymous=True)
    curr_root=insert_origin()
    #rotateInPlace("robot1")
    #rotateInPlace("robot2")
    #global_root=(0,0)
    scan(curr_root,no_of_robs)
