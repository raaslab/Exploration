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

count=0
stack=[]
root=[]
root_robot1=()
root_robot2=()
global_root=(0,0)
unreachable_poses=[]
visited_poses=[]
global_goals=[]
orig_x=0.00
orig_y=0.00
visited_nodes=[]
robot1Goal=()
robot2Goal=()
prevStatus1=""
prevStatus2=""
robot1Stack=[]
robot2Stack=[]
G=nx.DiGraph()
global_BVs=[]
check=0
start_time=int(math.floor(time.time()))
def callback(data,curr_root,robot1=None,robot2=None):
    print("callback called by ")
    if(robot2 is None):
        print("robot1")
    else:
        print(robot2)
    print("current root")
    print(curr_root)


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
    global global_root

    print("length of BVs")
    print(len(global_BVs))

    print("length of goals")
    print(len(global_goals))
    delta=0.25
    epsilon = 0.25
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
    dictBVGoals={}
    
    #Getting the occupancy grid
    grid = data.data
    resolution = data.info.resolution
    height=data.info.height
    width=data.info.width
    orig_x=data.info.origin.position.x
    orig_y=data.info.origin.position.y

    
    occupancyGridMat=np.asarray(grid, dtype=np.int8)
    occupancyGridMatFin=np.reshape(occupancyGridMat, (height, width))
    
    if(curr_root==(0,0)):
        pose_x=0.0
        pose_y=0.0
    else:
        if (robot2 is None):
            robotName="robot1"
        else:
            robotName="robot2"
        current_pose=get_pose(robotName)
        pose_x=current_pose.position.x
        pose_y=current_pose.position.y
    #frontier=getFrontiers(pose_x,pose_x,occupancyGridMatFin)
    #Getting the matrix coordinates of the robot from the x and y
    pose_i = int((round(pose_y,2) - orig_y)/delta)
    pose_j = int((round(pose_x,2) - orig_x)/delta)
    print(pose_i)
    print(pose_j)
    
    #Populating the frontiers
    scan_area_i= 3
    while (scan_area_i <= height-3):
        scan_area_j= 3
        while(scan_area_j <= width-3): 
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
    scan_area_i= 3
    while (scan_area_i < height-3):
        scan_area_j= 3
        while(scan_area_j < width-3): 
            if (occupancyGridMatFin[scan_area_i][scan_area_j] == 100 and ( ([scan_area_i-1,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j-1,rejectedFrontiers)) or ([scan_area_i-1,scan_area_j] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j,rejectedFrontiers)) or ([scan_area_i-1,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i-1,scan_area_j +1,rejectedFrontiers)) or ([scan_area_i,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i,scan_area_j -1,rejectedFrontiers)) or ([scan_area_i,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i,scan_area_j +1,rejectedFrontiers)) or ([scan_area_i+1,scan_area_j -1] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j -1,rejectedFrontiers)) or ([scan_area_i+1,scan_area_j] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j,rejectedFrontiers)) or ([scan_area_i+1,scan_area_j +1] in blockingFrontier and check8neighbours(scan_area_i+1,scan_area_j +1,rejectedFrontiers)))):
                blockingVertices.append([scan_area_i,scan_area_j])
            scan_area_j+=1
        #print(scan_area_i)
        scan_area_i+=1
    #return frontier

    

    validBlockingVertices=blockingVertices

    for vbv in validBlockingVertices:
        bi=vbv[0]
        bj=vbv[1]
        valid=1
        if ((bi==height or bj==width)or(occupancyGridMatFin[bi-2][bj] == 100 and occupancyGridMatFin[bi][bj-2] == 100)or (occupancyGridMatFin[bi-2][bj] == 100 and occupancyGridMatFin[bi][bj+2] == 100) or (occupancyGridMatFin[bi+2][bj] == 100 and occupancyGridMatFin[bi][bj-2] == 100) or (occupancyGridMatFin[bi+2][bj] == 100 and occupancyGridMatFin[bi][bj+2] == 100) or (occupancyGridMatFin[bi-1][bj] == 100 and occupancyGridMatFin[bi+1][bj] == 100) or (occupancyGridMatFin[bi][bj-1] == 100 and occupancyGridMatFin[bi][bj+1] == 100) or (occupancyGridMatFin[bi][bj-1] == 100 and occupancyGridMatFin[bi][bj+1] == -1) or (occupancyGridMatFin[bi][bj-1] == -1 and occupancyGridMatFin[bi][bj+1] == 100) or (occupancyGridMatFin[bi-1][bj] == 100 and occupancyGridMatFin[bi+1][bj] == -1) or (occupancyGridMatFin[bi-1][bj] == -1 and occupancyGridMatFin[bi+1][bj] == 100)):
            valid = 0
        if (valid==1):
            print(vbv)
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
        for bv in filter3:
            bi1=bv[0]
            bj1=bv[1]
            if(not(bi==bi1 and bj==bj1) and [bi,bj] in filter4):
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
                        filter4.remove([bi1,bj1])
                elif(bi==bi1):
                    lower=min(bj,bj1)
                    lower=lower+5
                    higher=max(bj,bj1)
                    #print(lower)
                    #print(higher)
                    remove=1
                    while(lower<higher-5):
                        lower+=1
                       # print(lower)
                        if(occupancyGridMatFin[bi][lower]==100 or occupancyGridMatFin[bi][lower]==-1):
                            remove=0
                    if(remove==1):
                        filter4.remove([bi1,bj1])

    for bv in filter4:
        bi=bv[0]
        bj=bv[1]
        bx,by=getcoords(bv)
        bearing= math.atan2(by-pose_y,bx-pose_x)
        dictBlockingAngles[bearing]=[bi,bj]

    filter5=sorted(dictBlockingAngles)
    f=[]

    for bear in filter5:
        frontierLine=[]
        bv=dictBlockingAngles[bear]
        bi=bv[0]
        bj=bv[1]
        #f.append(bv)
        bx,by=getcoords(bv)
        bvc=[bx,by]
        invalid_counter=0
        bv_tup=(bx,by)
        posex=pose_x +delta/2
        posey=pose_y +delta/2
        a = (posey - by) / (posex - bx)
        b = posey - a * posex
        invalid_counter=0
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
        if(checkExisting(bvc)):
            if(invalid_counter<5):
                global_BVs.append(bvc)
                f.append(bv)
                counter_to_check=0
                if(bi>4 and occupancyGridMatFin[bi-4][bj] == 100):
                    if(bj>5 and occupancyGridMatFin[bi][bj-5] == 0):
                        clearance=1
                        while(bj-clearance!=0 and occupancyGridMatFin[bi][bj-clearance]!=100):
                            frontierLine.append([bi,bj-clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+10,bj-5])
                        gx,gy=getcoords([bi+10,bj-5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx+0.25,gy+0.25) not in global_goals and (gx-0.25,gy) not in global_goals and (gx-0.25,gy-0.25) not in global_goals and (gx+0.25,gy-0.25) not in global_goals and (gx-0.25,gy+0.25) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                            
                    elif (bj< width-5 and occupancyGridMatFin[bi][bj+5] == 0):
                        clearance=1
                        while(bj+clearance!=width and occupancyGridMatFin[bi][bj+clearance]!=100 and occupancyGridMatFin[bi][bj+clearance]!=100):
                            frontierLine.append([bi,bj+clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+10,bj+5])
                        gx,gy=getcoords([bi+10,bj+5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx-0.25,gy) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                else:
                    counter_to_check+=1
                if(bi <height-4 and occupancyGridMatFin[bi+4][bj] == 100):
                    if(bj>5 and occupancyGridMatFin[bi][bj-5] == 0):
                        clearance=1
                        while(bj-clearance!=0 and occupancyGridMatFin[bi][bj-clearance]!=100 and occupancyGridMatFin[bi][bj-clearance]!=-1):
                            frontierLine.append([bi,bj-clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-10,bj-5])
                        gx,gy=getcoords([bi-10,bj-5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx-0.25,gy) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                    elif (bj< width-5 and occupancyGridMatFin[bi][bj+5] == 0):
                        clearance=1
                        while(bj+clearance!=width and occupancyGridMatFin[bi][bj+clearance]!=100 and occupancyGridMatFin[bi][bj+clearance]!=100):
                            frontierLine.append([bi,bj+clearance])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-10,bj+5])
                        gx,gy=getcoords([bi-10,bj+5])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx-0.25,gy) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                else:
                    counter_to_check+=1
                if(bj>4 and occupancyGridMatFin[bi][bj-4] == 100):
                    if(bj>5 and occupancyGridMatFin[bi-5][bj] == 0):
                        clearance=1
                        while(bi-clearance!=0 and occupancyGridMatFin[bi-clearance][bj]!=100 and occupancyGridMatFin[bi-clearance][bj]!=-1):
                            frontierLine.append([bi-clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-5,bj+10])
                        gx,gy=getcoords([bi-5,bj+10])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx-0.25,gy) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                    elif (bi<height-5 and occupancyGridMatFin[bi+5][bj] == 0):
                        clearance=1
                        while(bi+clearance!=height and occupancyGridMatFin[bi+clearance][bj]!=100 and occupancyGridMatFin[bi+clearance][bj]!=-1):
                            frontierLine.append([bi+clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+5,bj+10])
                        gx,gy=getcoords([bi+5,bj+10])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx-0.25,gy) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                if(bj<width-4 and occupancyGridMatFin[bi][bj+4] == 100):
                    if(bi>5 and occupancyGridMatFin[bi-5][bj] == 0):
                        clearance=1
                        while(bi-clearance!=0 and occupancyGridMatFin[bi-clearance][bj]!=100 and occupancyGridMatFin[bi-clearance][bj]!=-1):
                            frontierLine.append([bi-clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi-5,bj-10])
                        gx,gy=getcoords([bi-5,bj-10])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx-0.25,gy) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                    elif (bi<height-5 and occupancyGridMatFin[bi+5][bj] == 0):
                        clearance=1
                        while(bi+clearance!=height and occupancyGridMatFin[bi+clearance][bj]!=100 and occupancyGridMatFin[bi+clearance][bj]!=-1):
                            frontierLine.append([bi+clearance,bj])
                            clearance=clearance+1
                        dictFrontierLines[bear]=frontierLine
                        goals.append([bi+5,bj-10])
                        gx,gy=getcoords([bi+5,bj-10])
                        goal_tup=(gx,gy)
                        dictBVGoals[bv_tup]=goal_tup
                        if ((gx,gy) not in global_goals and (gx+0.25,gy) not in global_goals and (gx-0.25,gy) not in global_goals and (gx,gy+0.25) not in global_goals and (gx,gy-0.25) not in global_goals):
                            global_goals.append(goal_tup)
                            G.add_node(goal_tup)
                            G.add_edge(curr_root,goal_tup)
                else:
                    counter_to_check+=1
                if(counter_to_check==4):
                    print("goal not added")

        else:
            print("this node was invalid")
            #f.append(bv)

            
    tup_pose=(pose_i,pose_j)
    closed_list=[]
    node_in_tree={}
    
    print(dictBVGoals)
   
    for bear in filter5:
        frontierLine=[]
        #print(bear)
        dominators=[]
        bv=dictBlockingAngles[bear]
        
        bi=bv[0]
        bj=bv[1]
        bx,by=getcoords([bi,bj])
        bv_tup=(bx,by)

        #print(curr_root)
        print("current")
        print(bv_tup)

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
                            #f.append([scan_area_i,scan_area_j])
                            #print("in frontier line")
                            for blockVert in dictFrontierLines:
                                if(blockVert!=bear):
                                    if([scan_area_i,scan_area_j] in dictFrontierLines[blockVert]):
                                        vbv=dictBlockingAngles[blockVert]
                                        vbx,vby=getcoords([vbv[0],vbv[1]])
                                        tupvbv=(vbx,vby)
                                        print(tupvbv)
                                        if(tupvbv in dictBVGoals and G.has_node(dictBVGoals[tupvbv])):
                                            dominators.append(tupvbv)
                                            print("dominator")
                    scan_area_j+=1
                scan_area_i+=1
            max_l=0
            #lev=len(G.predecessors(dictBVGoals[bv_tup]))
            lev=getLevel(dictBVGoals[bv_tup],0)
            #print(lll)
            for d in dominators:
                    #l=len(G.predecessors(dictBVGoals[d]))
                    l=getLevel(dictBVGoals[d],0)
                    # if(l==lev):
                    #     if d in closed_list:
                    #         max_l=l
                    #         max_d=d
                    #         print("this is the dominator")
                    #         print(max_d)
                    # else:    
                    if l>max_l:
                        max_l=l
                        max_d=d
                        print("this is the dominator")
                        print(max_d)

            if(max_l>0):
                G.remove_node(dictBVGoals[bv_tup])
                G.add_edge(dictBVGoals[max_d],dictBVGoals[bv_tup])
            else:
                print("No dominators")
            closed_list.append(bv_tup)
            #f.append([bi,bj])
            publishFrontiers(f)

    
    
    plt.clf()
    plt.title("Tree generated")
    pos=graphviz_layout(G,prog='dot')
    nx.draw(G,pos,with_labels=True,arrows=False)
    plt.savefig('nx_test.png')

    node_in_tree={}
    
    succ=G.successors(curr_root)
    succ_temp = succ
    for s in succ_temp:
        print("checking s")
        print(s)
        if(s in visited_nodes):
            succ.remove(s)
    print("visited_nodes")
    print(visited_nodes)
    print("actual successors")
    print(succ_temp)
    print("successors at")
    print(curr_root)
    print(succ)
    

    node_in_tree[curr_root]=succ

    if(succ):
        publishFrontiers(f)
        if(robot1=="robot1" and robot2=="robot2"):
            if(len(succ)==1):
                robot1Stack.append(node_in_tree)
                robot2Stack.append(node_in_tree)
                visited_nodes.append(succ[0])
                robot1Goal=succ[0]
                if (occupancyGridMatFin[robot1Goal[0]-4][robot1Goal[1]]==0):
                    robot2Goal=(robot1Goal[0]-4,robot1Goal[1])
                elif(occupancyGridMatFin[robot1Goal[0]+4][robot1Goal[1]]==0):
                    robot2Goal=(robot1Goal[0]+4,robot1Goal[1])
                elif(occupancyGridMatFin[robot1Goal[0]][robot1Goal[1]-4]==0):
                    robot2Goal=(robot1Goal[0]+4,robot1Goal[1]-4)
                else:
                    robot2Goal=(robot1Goal[0],robot1Goal[1]+4)
            else:
                rotateInPlace("robot2")
                robot1Stack.append(node_in_tree)
                robot2Stack.append(node_in_tree)
                visited_nodes.append(succ[0])
                visited_nodes.append(succ[1])
                robot1Goal=succ[0]
                robot2Goal=succ[1]
            sendGoalRectilinear(robot1Goal,"robot1")
            sendGoalRectilinear(robot2Goal,"robot2")
        else:
            if(robot2 is None):
                robot1Goal=succ[0]
                robot1Stack.append(node_in_tree)
                visited_nodes.append(robot1Goal)
                sendGoalRectilinear(robot1Goal,"robot1")
            else:
                robot2Goal=succ[0]
                robot2Stack.append(node_in_tree)
                visited_nodes.append(robot2Goal)
                sendGoalRectilinear(robot2Goal,"robot2")
    else:
        if(robot2 is None):
            if(len(robot1Stack)>2):
                prevNode=robot1Stack.pop()
                popStackRobot1(prevNode)
            else:
                if(len(visited_nodes)!=len(global_goals)):
                    for g in global_goals:
                        if(g not in visited_nodes):
                            print("unvisited node from other tree")
                            print(g)
                            robot1Goal=g
                            visited_nodes.append(robot1Goal)
                            sendGoalRectilinear(robot1Goal,"robot1")
                else:
                    checkForCompletion(curr_root,robot1)
                    explorationcomplete()
        else:
            if(len(robot2Stack)>2):
                n=robot2Stack.pop()
                popStackRobot2(n)
            else:
                if(len(visited_nodes)!=len(global_goals)):
                    for g in global_goals:
                        if(g not in visited_nodes):
                            print("unvisited node from other tree")
                            print(g)
                            robot1Goal=g
                            visited_nodes.append(robot1Goal)
                            sendGoalRectilinear(robot1Goal,"robot1")
                else:
                    checkForCompletion(curr_root,robot2)
                    explorationcomplete()
    checkStatus(robot1Goal,robot2Goal)



def popStackRobot1(prevNode):
    global robot1Stack
    global visited_nodes
    global robot1Goal
    global robot2Goal
    print("leaf popping")
    print("robot1")
    r=prevNode.keys()
    root=r[0]
    print("current root")
    print(root)
    prevGoalList=prevNode[root]
    if(prevGoalList):
        for prevGoal in prevGoalList:
            if(prevGoal not in visited_nodes):
                print("got a previous goal")
                visited_nodes.append(prevGoal)
                sendGoalRectilinear(prevGoal,"robot1")
                checkStatus(robot1Goal,robot2Goal)
    if(len(robot1Stack)>2):
        n=robot1Stack.pop()
        popStackRobot1(n)
    else:
        if(len(visited_nodes)!=len(global_goals)):
            for g in global_goals:
                if(g not in visited_nodes):
                    print("unvisited node from other tree")
                    print(g)
                    robot1Goal=g
                    visited_nodes.append(robot1Goal)
                    sendGoalRectilinear(robot1Goal,"robot1")
                    checkStatus(robot1Goal,robot2Goal)

def popStackRobot2(prevNode):
    global robot2Stack
    global robot1Goal
    global robot2Goal
    global visited_nodes
    print("leaf popping")
    print("robot2")
    r=prevNode.keys()
    root=r[0]
    print("current root")
    print(root)
    prevGoalList=prevNode[root]
    if(prevGoalList):
        for prevGoal in prevGoalList:
            if(prevGoal not in visited_nodes):
                print("got a previous goal")
                visited_nodes.append(prevGoal)
                robot2Goal=prevGoal
                sendGoalRectilinear(prevGoal,"robot2")
                checkStatus(robot1Goal,robot2Goal)
    if(len(robot2Stack)>2):
        n=robot2Stack.pop()
        popStackRobot2(n)
    else:
        if(len(visited_nodes)!=len(global_goals)):
            for g in global_goals:
                if(g not in visited_nodes):
                    print("unvisited node from other tree")
                    print(g)
                    robot2Goal=g
                    visited_nodes.append(robot2Goal)
                    sendGoalRectilinear(robot2Goal,"robot2")
                    checkStatus(robot1Goal,robot2Goal)

def checkForCompletion(curr_root,robotName):
    successStatus="status: 3"
    if(robotName=="robot2"):
        status2 = rospy.wait_for_message("/robot1/move_base/status", GoalStatusArray)
        l2=status2.status_list
        statusString=str(l2[0])
        if successStatus in statusString:
            explorationcomplete()
        else:
            checkForCompletion(curr_root,robotName)
    else:
        status1 = rospy.wait_for_message("/robot2/move_base/status", GoalStatusArray)
        l1=status1.status_list
        statusString=str(l1[0])
        if successStatus in statusString:
            explorationcomplete()
        else:
            checkForCompletion(curr_root,robotName)

def checkStatus(tup_goal1, tup_goal2):

    global prevStatus1
    global prevStatus2
    status1 = rospy.wait_for_message("/robot1/move_base/status", GoalStatusArray)
    l1=status1.status_list
    statuslength1=len(l1)
    if(statuslength1>0):
        statusString=str(l1[0])
        if(statusString==prevStatus1):
            print("same status : continue checking")
        else:
            prevStatus1=statusString
            successStatus="status: 3"
            abortedStatus="status: 4"
            if successStatus in statusString:
                print("reached goal : going to call callback with this root")
                print(tup_goal1)
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                callback(msg,tup_goal1,robot1="robot1",robot2=None)
            elif(abortedStatus in statusString):
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                tup_goal1 = robot1Stack.pop()
                callback(msg,tup_goal1,robot1="robot1",robot2=None)
    status2 = rospy.wait_for_message("/robot2/move_base/status", GoalStatusArray)
    l2=status2.status_list
    statuslength2=len(l2)
    if(statuslength2>0):
        statusString=str(l2[0])
        if(statusString==prevStatus2):
            print("same status : continue checking")
        else:
            prevStatus2=statusString
            successStatus="status: 3"
            abortedStatus="status: 4"
            if successStatus in statusString:
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                print("reached goal: going to call callback with this root")
                print(tup_goal2)
                callback(msg,tup_goal2,robot1=None,robot2="robot2")
            elif(abortedStatus in statusString):
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                tup_goal2 = robot2Stack.pop()
                callback(msg,tup_goal2,robot1=None,robot2="robot2")
    rospy.sleep(2.0)
    checkStatus(tup_goal1,tup_goal2)
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


def checkExisting(bvc):
    print("check existing called")
    global global_BVs
    f=[]
    delta=0.25
    bi=(bvc[1] - orig_y)/delta
    bj=(bvc[0] - orig_x)/delta

    checkAreai=bi-1
    while (checkAreai <= bi+1):
        checkAreaj=bj-1
        while(checkAreaj <= bj+1):
            #f.append([checkAreai,checkAreaj])
            check_x,check_y=getcoords([checkAreai,checkAreaj])
            
            if([check_x,check_y] in global_BVs):
                #publishFrontiers(f)
                print("found existing")
                return False
            checkAreaj+=1
        checkAreai+=1
    print("not found earlier")
    return True



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
    global orig_x
    global orig_y
    delta=0.25
    size=100
    print(orig_x)
    print(orig_y)
    cloud=[]
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



def sendGoalRectilinear(tup_goal,robotName):
    global G
    print("in goal")
    print(robotName)
    delta=0.25
    goal_states = ['PENDING', 'ACTIVE', 'PREEMPTED', 
                       'SUCCEEDED', 'ABORTED', 'REJECTED',
                       'PREEMPTING', 'RECALLING', 'RECALLED',
                       'LOST']
    topicName="/"
    topicName+=robotName
    topicName+="/move_base"
    move_base = actionlib.SimpleActionClient(topicName, MoveBaseAction)
    rospy.loginfo("Waiting for move_base action server...")
    move_base.wait_for_server(rospy.Duration(60))
    rospy.loginfo("Connected to move base server")
    rospy.loginfo("Starting Exploration")
    #while not rospy.is_shutdown():
    goal = MoveBaseGoal()
    goal.target_pose.pose.position.x = (tup_goal[0])
    goal.target_pose.pose.position.y = (tup_goal[1])
    goal.target_pose.pose.orientation.w = 1
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    rospy.loginfo("Goal Set!")
    move_base.send_goal(goal)
    #finished_within_time = move_base.wait_for_result(rospy.Duration(60)) 
    # if not finished_within_time:
    #     move_base.cancel_goal()
    #     rospy.loginfo("Timed out achieving goal")
    #     scan(tup_next_root)
    # else:
    #     state = move_base.get_state()
    #     if state == GoalStatus.SUCCEEDED:
    #         rospy.loginfo("Goal succeeded!")
    #         rotateInPlace()
    #         current_pose=get_pose(robotName)
    #         pose_x=current_pose.position.x
    #         pose_y=current_pose.position.y
    #         pose_i = int((round(pose_y,3)/delta - orig_y))
    #         pose_j = int((round(pose_x,3)/delta - orig_x))
    #         #tup_goal=(pose_i,pose_j)
    #         #G.add_node(tup_goal)
    #         #G.add_edge(tup_pose,tup_goal)
    #         scan(tup_next_root)
    #     else:
    #         rospy.loginfo("Goal failed with error code: " + str(goal_states[state]))
    #         scan()
def sendGoal(x,y,frontier,prev_pose,robotName):
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
        current_pose=get_pose(robotName)
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

    def add_child(self, obj):
        self.children.append(obj)

    def has_children(self):
        if (self.children):
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
    global orig_x
    global orig_y
    delta=0.25
    size=100
    i= frontier[0]
    j= frontier[1]
    x= orig_x + (j * delta)
    y= orig_y + (i * delta)
    return(x, y)

def scan(curr_root,robotName):
    global robot1Stack
    global robot2Stack
    print('Scanning...')
    robot1Stack.append(curr_root)
    robot2Stack.append(curr_root)
    try:
        msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
    except:
        print("Exception thrown")
    #callback(msg)
    robot_pose=get_pose(robotName)
    
    print(robot_pose)

    callback(msg,curr_root,robotName,"robot2")
   


def get_pose(robotName):
    top="/"
    top+=str(robotName)
    top+="_pose"
    pose = rospy.wait_for_message(top, Pose)
    return pose

def insert_origin():
    global stack
    global G
    print("Adding origin")
    global root
    delta=0.25
    #current_pose=get_pose()
    #pose_x=current_pose.position.x
    #pose_y=current_pose.position.y
    #pose_i = int((round(pose_y,2)/delta + orig_y))
    #pose_j = int((round(pose_x,2)/delta + orig_x))
    tup_pose=(0,0)
    print(tup_pose)
    G.add_node(tup_pose)
    #stack.append(current_pose)
    #rotateInPlace()
    root.append(tup_pose)
    #print(stack)

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
    for i in range(80):
        #print("here")
        p.publish(twist)
        rospy.sleep(0.1) 
    #rostopic pub -1 /RosAria/cmd_vel geometry_msgs/Twist '[0.0, 0.0, 0.0]' '[0.0, 0.0, 0.5]'
    #rospy.spin()
    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)
    #rospy.spin()

class node:
    def __init__( self , parent):
        self.parent=parent



if __name__ == '__main__':
    print('Initialized')
    start_time=time.time()
    rospy.init_node('SubscribeOccupancyGrid', anonymous=True)
    insert_origin()
    #try:
    #    thread.start_new_thread( rotateInPlace, ("robot1",) )
    #    thread.start_new_thread( rotateInPlace, ("robot2",) )
    #except:
    #   print "Error: unable to start thread"
    #rotateInPlace("robot1")
    #rotateInPlace("robot2")
    global_root=(0,0)
    #try:
    #    thread.start_new_thread( scan, (root,"robot1",) )
    #    thread.start_new_thread( scan, (root,"robot2",) )
    #except:
    #    print "Error: unable to start thread"
    scan(global_root,"robot1")