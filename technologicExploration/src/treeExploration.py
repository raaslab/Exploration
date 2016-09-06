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
robot3Goal=()
robot4Goal=()

prevStatus1=""
prevStatus2=""
prevStatus3=""
prevStatus4=""
robot1Stack=[]
robot2Stack=[]
robot3Stack=[]
robot4Stack=[]

cluster1Status=""
cluster2Status=""
cluster3Status=""
cluster4Status=""

Status1Checker=0
Status2Checker=0
Status3Checker=0
Status4Checker=0

G=nx.DiGraph()
global_BVs=[]
check=0
start_time=int(math.floor(time.time()))
def callback(data,curr_root,robot1=None,robot2=None,robot3=None,robot4=None):
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

    print("callback called by ")
    if(robot1=="robot1"):
        print("robot1")
    elif(robot2=="robot2"):
        print(robot2)
    elif(robot3=="robot3"):
        print(robot3)
    elif(robot4=="robot4"):
        print(robot4)
    elif(robot1=="both" and robot2=="both"):
        print("called by robot1 and robot2")
    elif(robot3=="both" and robot4=="both"):
        print("called by robot3 and robot4")
    else:
        print("called by all")
    print("current root")
    print(curr_root)


    
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
    
    #if(robot1=="all" or robot2=="both" or robot3=="both"):
    pose_x=curr_root[0]
    pose_y=curr_root[1]
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
            if(invalid_counter<3):
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
                elif(bi <height-4 and occupancyGridMatFin[bi+4][bj] == 100):
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
                elif(bj>4 and occupancyGridMatFin[bi][bj-4] == 100):
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
                elif(bj<width-4 and occupancyGridMatFin[bi][bj+4] == 100):
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
                #f.extend(frontierLine)
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
            lev=len(G.predecessors(dictBVGoals[bv_tup]))
            #lev=getLevel(dictBVGoals[bv_tup],0)
            #print(lll)
            for d in dominators:
                l=len(G.predecessors(dictBVGoals[d]))
                #l=getLevel(dictBVGoals[d],0)
                    # if(l==lev):
                    #     if d in closed_list:
                    #         max_l=l
                    #         max_d=d
                    #         print("this is the dominator")
                    #         print(max_d)
                    # else:    
                if (l>max_l):
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
            #publishFrontiers(f)
    
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
        if(robot1=="robot1"):
            if(s==robot2Goal or s==robot3Goal or s==robot4Goal):
                succ.remove(s)
        elif(robot2=="robot2"):
            if(s==robot1Goal or s==robot3Goal or s==robot4Goal):
                succ.remove(s)
        elif(robot1 =="both"):
            if(s==robot3Goal or s==robot4Goal):
                succ.remove(s)
        elif(robot3=="robot3"):
            if(s==robot1Goal or s==robot2Goal or s==robot4Goal):
                succ.remove(s)
        elif(robot4=="robot4"):
            if(s==robot1Goal or s==robot2Goal or s==robot3Goal):
                succ.remove(s)
        elif(robot3 =="both"):
            if(s==robot1Goal or s==robot2Goal):
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
        if(robot1=="all" and robot2=="all" and robot3=="all" and robot4=="all"):
            rotateInPlace("robot1")
            if(len(succ)==1):
                #Single goal: all robots go to the same node
                robot1Stack.append(node_in_tree)
                robot2Stack.append(node_in_tree)
                robot3Stack.append(node_in_tree)
                robot4Stack.append(node_in_tree)
                # adding goals

                robot1Goal=succ[0]
                gi = int((round(robot1Goal[1],2) - orig_y)/delta)
                gj = int((round(robot1Goal[0],2) - orig_x)/delta)
                
                f.append([gi,gj])
                #gi,gj=getindices(robot1Goal)
                if (occupancyGridMatFin[gi-4][gj]==0):
                    
                    robot2Goal=getcoords([gi-2,gj])
                    robot3Goal=getcoords([gi-4,gj])
                    robot4Goal=getcoords([gi-6,gj])
                elif(occupancyGridMatFin[gi+4][gj]==0):
                    robot2Goal=getcoords([gi+2,gj])
                    robot3Goal=getcoords([gi+4,gj])
                    robot4Goal=getcoords([gi+6,gj])
                elif(occupancyGridMatFin[gi][gj-4]==0):
                    robot2Goal=getcoords([gi,gj-2])
                    robot3Goal=getcoords([gi,gj-4])
                    robot4Goal=getcoords([gi,gj-6])
                else:
                    robot2Goal=getcoords([gi,gj+2])
                    robot3Goal=getcoords([gi,gj+4])
                    robot4Goal=getcoords([gi,gj+6])
                #send goals to each robot
                sendGoalRectilinear(robot1Goal,"robot1")
                sendGoalRectilinear(robot2Goal,"robot2")
                sendGoalRectilinear(robot3Goal,"robot3")
                sendGoalRectilinear(robot4Goal,"robot4")

                cluster1Status="all"
                cluster2Status="all"
                cluster3Status="all"
                cluster4Status="all"
                #check if robots reached the goals
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            elif(len(succ)==2):
                robot1Stack.append(node_in_tree)
                robot2Stack.append(node_in_tree)
                robot3Stack.append(node_in_tree)
                robot4Stack.append(node_in_tree)
                #assign first goal to the first cluster
                robot1Goal=succ[0]
                gi = int((round(robot1Goal[1],2) - orig_y)/delta)
                gj = int((round(robot1Goal[0],2) - orig_x)/delta)
                f.append([gi,gj])
                if (occupancyGridMatFin[gi-4][gj]==0):
                    robot2Goal=getcoords([gi-4,gj])
                elif(occupancyGridMatFin[gi+4][gj]==0):
                    robot2Goal=getcoords([gi+4,gj])
                elif(occupancyGridMatFin[gi][gj-4]==0):
                    robot2Goal=getcoords([gi,gj-4])
                else:
                    robot2Goal=getcoords([gi,gj+4])
                #assign second goal to the second cluster
                robot3Goal=succ[1]
                gi = int((round(robot3Goal[1],2) - orig_y)/delta)
                gj = int((round(robot3Goal[0],2) - orig_x)/delta)
                if (occupancyGridMatFin[gi-4][gj]==0):
                    robot4Goal=getcoords([gi-4,gj])
                elif(occupancyGridMatFin[gi+4][gj]==0):
                    robot4Goal=getcoords([gi+4,gj])
                elif(occupancyGridMatFin[gi][gj-4]==0):
                    robot4Goal=getcoords([gi,gj-4])
                else:
                    robot4Goal=getcoords([gi,gj+4])
                sendGoalRectilinear(robot1Goal,"robot1")
                sendGoalRectilinear(robot2Goal,"robot2")
                sendGoalRectilinear(robot3Goal,"robot3")
                sendGoalRectilinear(robot4Goal,"robot4")
                #check if robots reached the goals
                cluster1Status="both"
                cluster2Status="both"
                cluster3Status="both"
                cluster4Status="both"
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            else:
                if(robot1 =="robot1"):
                    robot1Goal=succ[0]
                    robot1Stack.append(node_in_tree)
                    cluster1Status="robot1"
                    #visited_nodes.append(robot1Goal)
                    sendGoalRectilinear(robot1Goal,"robot1")
                elif(robot2=="robot2"):
                    robot2Goal=succ[0]
                    robot2Stack.append(node_in_tree)
                    cluster2Status="robot2"
                    #visited_nodes.append(robot2Goal)
                    sendGoalRectilinear(robot2Goal,"robot2")
                elif(robot3=="robot3"):
                    robot3Goal=succ[0]
                    robot3Stack.append(node_in_tree)
                    cluster3Status="robot3"
                    #visited_nodes.append(robot2Goal)
                    sendGoalRectilinear(robot3Goal,"robot3")
                elif(robot4=="robot4"):
                    robot4Goal=succ[0]
                    robot4Stack.append(node_in_tree)
                    cluster4Status="robot4"
                    #visited_nodes.append(robot2Goal)
                    sendGoalRectilinear(robot2Goal,"robot4")             
        elif(robot1=="both"):
            print("robot 1 and 2")
            if(len(succ)==1):
                    #Single goal: all robots go to the same node
                    robot1Stack.append(node_in_tree)
                    robot2Stack.append(node_in_tree)
                    # adding goals
                    robot1Goal=succ[0]
                    gi = int((round(robot1Goal[1],2) - orig_y)/delta)
                    gj = int((round(robot1Goal[0],2) - orig_x)/delta)
                    f.append([gi,gj])
                    if (occupancyGridMatFin[gi-4][gj]==0):
                        robot2Goal=getcoords([gi-4,gj])
                    elif(occupancyGridMatFin[gi+4][gj]==0):
                        robot2Goal=getcoords([gi+4,gj])
                    elif(occupancyGridMatFin[gi][gj-4]==0):
                        robot2Goal=getcoords([gi,gj-4])
                    else:
                        robot2Goal=getcoords([gi,gj+4])
                    #send goals to each robot
                    sendGoalRectilinear(robot1Goal,"robot1")
                    sendGoalRectilinear(robot2Goal,"robot2")
                    cluster1Status="both"
                    cluster2Status="both"
                    #check if robots reached the goals
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            else:
                robot1Stack.append(node_in_tree)
                robot2Stack.append(node_in_tree)
                robot1Goal=succ[0]
                robot2Goal=succ[1]
                sendGoalRectilinear(robot1Goal,"robot1")
                sendGoalRectilinear(robot2Goal,"robot2")
                cluster1Status="robot1"
                cluster2Status="robot2"
                #check if robots reached the goals
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
        elif(robot3=="both"):
            print("robot 3 and 4")
            if(len(succ)==1):
                    #Single goal: all robots go to the same node
                    robot3Stack.append(node_in_tree)
                    robot4Stack.append(node_in_tree)
                    # adding goals
                    robot3Goal=succ[0]
                    gi = int((round(robot3Goal[1],2) - orig_y)/delta)
                    gj = int((round(robot3Goal[0],2) - orig_x)/delta)
                    if (occupancyGridMatFin[gi-4][gj]==0):
                        robot4Goal=getcoords([gi-4,gj])
                    elif(occupancyGridMatFin[gi+4][gj]==0):
                        robot4Goal=getcoords([gi+4,gj])
                    elif(occupancyGridMatFin[gi][gj-4]==0):
                        robot4Goal=getcoords([gi,gj-4])
                    else:
                        robot4Goal=getcoords([gi,gj+4])
                    #send goals to each robot
                    cluster3Status="both"
                    cluster4Status="both"
                    sendGoalRectilinear(robot3Goal,"robot3")
                    sendGoalRectilinear(robot4Goal,"robot4")
                    #check if robots reached the goals
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            else:
                robot3Stack.append(node_in_tree)
                robot4Stack.append(node_in_tree)
                robot3Goal=succ[0]
                robot4Goal=succ[1]
                sendGoalRectilinear(robot3Goal,"robot3")
                sendGoalRectilinear(robot4Goal,"robot4")
                cluster3Status="robot3"
                cluster4Status="robot4"
                #check if robots reached the goals
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
        elif(robot1=="robot1"):
            #Single goal: single goal
            robot1Stack.append(node_in_tree)
            # adding goals
            robot1Goal=succ[0]
            #send goals to each robot
            cluster1Status="robot1"
            sendGoalRectilinear(robot1Goal,"robot1")
            #check if robots reached the goals
            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
        elif(robot2=="robot2"):
            #Single goal: single goal
            robot2Stack.append(node_in_tree)
            # adding goals
            robot2Goal=succ[0]
            #send goals to each robot
            cluster2Status="robot2"
            sendGoalRectilinear(robot2Goal,"robot2")
            #check if robots reached the goals
            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
        elif(robot3=="robot3"):
            #Single goal: single goal
            robot3Stack.append(node_in_tree)
            # adding goals
            robot3Goal=succ[0]
            #send goals to each robot
            cluster3Status="robot3"
            sendGoalRectilinear(robot3Goal,"robot3")
            #check if robots reached the goals
            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
        elif(robot4=="robot4"):
            #Single goal: single goal
            robot4Stack.append(node_in_tree)
            # adding goals
            robot4Goal=succ[0]
            #send goals to each robot
            cluster4Status="robot4"
            sendGoalRectilinear(robot4Goal,"robot4")
            #check if robots reached the goals
            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
    else:
        if(robot1 =="robot1" or robot1 =="both"):
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
                            #visited_nodes.append(robot1Goal)
                            #cluster1Status="robot1"
                            sendGoalRectilinear(robot1Goal,"robot1")
                            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
                else:
                    checkForCompletion(curr_root,robot1)
                    explorationcomplete()
        elif(robot2=="robot2"):
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
                            #visited_nodes.append(robot1Goal)
                            #cluster2Status="robot2"
                            sendGoalRectilinear(robot2Goal,"robot2")
                            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
                else:
                    checkForCompletion(curr_root,robot2)
                    explorationcomplete()
        elif(robot3=="robot3" or robot3=="both"):
            if(len(robot3Stack)>2):
                n=robot3Stack.pop()
                popStackRobot3(n)
            else:
                if(len(visited_nodes)!=len(global_goals)):
                    for g in global_goals:
                        if(g not in visited_nodes):
                            print("unvisited node from other tree")
                            print(g)
                            robot3Goal=g
                            #visited_nodes.append(robot1Goal)
                            #cluster3Status="robot3"
                            sendGoalRectilinear(robot3Goal,"robot3")
                            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
                else:
                    checkForCompletion(curr_root,robot3)
                    explorationcomplete()
        elif(robot4=="robot4"):
            if(len(robot4Stack)>2):
                n=robot4Stack.pop()
                popStackRobot4(n)
            else:
                if(len(visited_nodes)!=len(global_goals)):
                    for g in global_goals:
                        if(g not in visited_nodes):
                            print("unvisited node from other tree")
                            print(g)
                            robot4Goal=g
                            #visited_nodes.append(robot1Goal)
                            #cluster4Status="robot4"
                            sendGoalRectilinear(robot4Goal,"robot4")
                            checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
                else:
                    checkForCompletion(curr_root,robot4)
                    explorationcomplete()
    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)



def popStackRobot1(prevNode):
    global robot1Stack
    global visited_nodes
    global robot1Goal
    global robot2Goal
    global robot3Goal
    global robot4Goal
    print("leaf popping")
    print("robot1")
    r=prevNode.keys()
    root=r[0]
    print("current root")
    print(root)
    prevGoalList=prevNode[root]
    if(prevGoalList):
        for prevGoal in prevGoalList:
            if(prevGoal not in visited_nodes and prevGoal!=robot2Goal and prevGoal!=robot3Goal and prevGoal!=robot4Goal):
                print("got a previous goal")
                print(prevGoal)
                robot1Goal=prevGoal
                if(cluster1Status=="robot1"):
                        sendGoalRectilinear(robot1Goal,"robot1")
                else:
                    gi,gj=getindices([robot1Goal])
                    if (occupancyGridMatFin[gi-4][gj]==0):
                        robot2Goal=getcoords([gi-4,gj])
                    elif(occupancyGridMatFin[gi+4][gj]==0):
                        robot2Goal=getcoords([gi+4,gj])
                    elif(occupancyGridMatFin[gi][gj-4]==0):
                        robot2Goal=getcoords([gi,gj-4])
                    else:
                        robot2Goal=getcoords([gi,gj+4])
                    sendGoalRectilinear(robot1Goal,"robot1")
                    sendGoalRectilinear(robot2Goal,"robot2")
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
    goals_to_check=[]
    if(len(robot1Stack)>2):
        n=robot1Stack.pop()
        popStackRobot1(n)
    else:
        if(len(visited_nodes)!=len(global_goals)):
            for k in robot2Stack:
                if(type(k) is dict):
                    r=k.keys()
                    root=r[0]
                    list_from_cluster=k[root]
                    for g in list_from_cluster:
                        if(g not in visited_nodes):
                            print("topmost unvisited node")
                            print(g)
                            goals_to_check.append(g)
                            if(g!=robot2Goal):
                                robot1Goal=g
                                sendGoalRectilinear(robot1Goal,"robot1")
                                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            for g in goals_to_check:
                if(g not in visited_nodes):
                    print("topmost unvisited node")
                    print(g)
                    robot1Goal=g
                    if(cluster1Status=="robot1"):
                        sendGoalRectilinear(robot1Goal,"robot1")
                    else:
                        gi,gj=getindices([robot1Goal])
                        if (occupancyGridMatFin[gi-4][gj]==0):
                            robot2Goal=getcoords([gi-4,gj])
                        elif(occupancyGridMatFin[gi+4][gj]==0):
                            robot2Goal=getcoords([gi+4,gj])
                        elif(occupancyGridMatFin[gi][gj-4]==0):
                            robot2Goal=getcoords([gi,gj-4])
                        else:
                            robot2Goal=getcoords([gi,gj+4])
                        sendGoalRectilinear(robot1Goal,"robot1")
                        sendGoalRectilinear(robot2Goal,"robot2")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)

            for g in global_goals:
                if(g not in visited_nodes):
                    print("topmost unvisited node from other tree")
                    print(g)
                    robot1Goal=g
                    #visited_nodes.append(robot1Goal)
                    if(cluster1Status=="robot1"):
                        sendGoalRectilinear(robot1Goal,"robot1")
                    else:
                        gi,gj=getindices([robot1Goal])
                        if (occupancyGridMatFin[gi-4][gj]==0):
                            robot2Goal=getcoords([gi-4,gj])
                        elif(occupancyGridMatFin[gi+4][gj]==0):
                            robot2Goal=getcoords([gi+4,gj])
                        elif(occupancyGridMatFin[gi][gj-4]==0):
                            robot2Goal=getcoords([gi,gj-4])
                        else:
                            robot2Goal=getcoords([gi,gj+4])
                        sendGoalRectilinear(robot1Goal,"robot1")
                        sendGoalRectilinear(robot2Goal,"robot2")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)

def popStackRobot2(prevNode):
    global robot2Stack
    global robot1Goal
    global robot2Goal
    global robot3Goal
    global robot4Goal
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
            if(prevGoal not in visited_nodes and prevGoal!=robot1Goal and prevGoal!=robot3Goal and prevGoal!=robot4Goal):
                print("got a previous goal")
                print(prevGoal)
                #visited_nodes.append(prevGoal)
                robot2Goal=prevGoal
                sendGoalRectilinear(prevGoal,"robot2")
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
    goals_to_check=[]
    if(len(robot2Stack)>2):
        n=robot2Stack.pop()
        popStackRobot2(n)
    else:
        if(len(visited_nodes)!=len(global_goals)):
            for k in robot1Stack:
                print(k)
                if(type(k) is dict):
                    r=k.keys()
                    root=r[0]
                    list_from_cluster=k[root]
                    for g in list_from_cluster:
                        if(g not in visited_nodes):
                            print("topmost unvisited node")
                            print(g)
                            goals_to_check.append(g)
                            if(g!=robot1Goal):
                                robot2Goal=g
                                sendGoalRectilinear(robot2Goal,"robot2")
                                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            for g in goals_to_check:
                if(g not in visited_nodes):
                    print("topmost unvisited node")
                    print(g)
                    robot2Goal=g
                    sendGoalRectilinear(robot2Goal,"robot2")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)

            for g in global_goals:
                if(g not in visited_nodes):
                    print("topmost unvisited node from other tree")
                    print(g)
                    robot2Goal=g
                    #visited_nodes.append(robot1Goal)
                    sendGoalRectilinear(robot2Goal,"robot2")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)

def popStackRobot3(prevNode):
    global robot3Stack
    global robot1Goal
    global robot2Goal
    global robot3Goal
    global robot4Goal
    global visited_nodes
    global cluster3Status
    print("leaf popping")
    print("robot3")
    r=prevNode.keys()
    root=r[0]
    print("current root")
    print(root)
    prevGoalList=prevNode[root]
    if(prevGoalList):
        for prevGoal in prevGoalList:
            if(prevGoal not in visited_nodes and prevGoal!=robot1Goal and prevGoal!=robot2Goal and prevGoal!=robot4Goal):
                print("got a previous goal")
                print(prevGoal)
                #visited_nodes.append(prevGoal)
                robot3Goal=prevGoal
                if(cluster3Status=="robot3"):
                    sendGoalRectilinear(prevGoal,"robot3")
                else:
                    gi,gj=getindices([prevGoal])
                    if (occupancyGridMatFin[gi-4][gj]==0):
                        robot4Goal=getcoords([gi-4,gj])
                    elif(occupancyGridMatFin[gi+4][gj]==0):
                        robot4Goal=getcoords([gi+4,gj])
                    elif(occupancyGridMatFin[gi][gj-4]==0):
                        robot4Goal=getcoords([gi,gj-4])
                    else:
                        robot4Goal=getcoords([gi,gj+4])
                    sendGoalRectilinear(robot3Goal,"robot3")
                    sendGoalRectilinear(robot4Goal,"robot4")
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
    goals_to_check=[]
    if(len(robot3Stack)>2):
        n=robot3Stack.pop()
        popStackRobot3(n)
    else:
        if(len(visited_nodes)!=len(global_goals)):
            for k in robot4Stack:
                print(k)
                if(type(k) is dict):
                    r=k.keys()
                    root=r[0]
                    list_from_cluster=k[root]
                    for g in list_from_cluster:
                        if(g not in visited_nodes):
                            print("topmost unvisited node")
                            print(g)
                            goals_to_check.append(g)
                            if(g!=robot4Goal):
                                robot3Goal=g
                                sendGoalRectilinear(robot3Goal,"robot3")
                                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            for g in goals_to_check:
                if(g not in visited_nodes):
                    print("topmost unvisited node")
                    print(g)
                    robot3Goal=g
                    if(cluster3Status=="robot3"):
                        sendGoalRectilinear(robot3Goal,"robot3")
                    else:
                        gi,gj=getindices([robot3Goal])
                        if (occupancyGridMatFin[gi-4][gj]==0):
                            robot4Goal=getcoords([gi-4,gj])
                        elif(occupancyGridMatFin[gi+4][gj]==0):
                            robot4Goal=getcoords([gi+4,gj])
                        elif(occupancyGridMatFin[gi][gj-4]==0):
                            robot4Goal=getcoords([gi,gj-4])
                        else:
                            robot4Goal=getcoords([gi,gj+4])
                        sendGoalRectilinear(robot3Goal,"robot3")
                        sendGoalRectilinear(robot4Goal,"robot4")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            for g in global_goals:
                if(g not in visited_nodes):
                    print("topmost unvisited node from other tree")
                    print(g)
                    robot3Goal=g
                    #visited_nodes.append(robot1Goal)
                    if(cluster3Status=="robot3"):
                        sendGoalRectilinear(robot3Goal,"robot3")
                    else:
                        gi,gj=getindices([robot3Goal])
                        if (occupancyGridMatFin[gi-4][gj]==0):
                            robot4Goal=getcoords([gi-4,gj])
                        elif(occupancyGridMatFin[gi+4][gj]==0):
                            robot4Goal=getcoords([gi+4,gj])
                        elif(occupancyGridMatFin[gi][gj-4]==0):
                            robot4Goal=getcoords([gi,gj-4])
                        else:
                            robot4Goal=getcoords([gi,gj+4])
                        sendGoalRectilinear(robot3Goal,"robot3")
                        sendGoalRectilinear(robot4Goal,"robot4")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)

def popStackRobot4(prevNode):
    global robot4Stack
    global robot1Goal
    global robot2Goal
    global robot3Goal
    global robot4Goal
    global visited_nodes
    print("leaf popping")
    print("robot4")
    r=prevNode.keys()
    root=r[0]
    print("current root")
    print(root)
    prevGoalList=prevNode[root]
    if(prevGoalList):
        for prevGoal in prevGoalList:
            if(prevGoal not in visited_nodes and prevGoal!=robot1Goal and prevGoal!=robot2Goal and prevGoal!=robot3Goal):
                print("got a previous goal")
                print(prevGoal)
                #visited_nodes.append(prevGoal)
                robot4Goal=prevGoal
                sendGoalRectilinear(prevGoal,"robot4")
                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
    goals_to_check=[]
    if(len(robot4Stack)>2):
        n=robot4Stack.pop()
        popStackRobot4(n)
    else:
        if(len(visited_nodes)!=len(global_goals)):
            for k in robot3Stack:
                print(k)
                if(type(k) is dict):
                    r=k.keys()
                    root=r[0]
                    list_from_cluster=k[root]
                    for g in list_from_cluster:
                        if(g not in visited_nodes):
                            print("topmost unvisited node")
                            print(g)
                            goals_to_check.append(g)
                            if(g!=robot3Goal):
                                robot4Goal=g
                                sendGoalRectilinear(robot4Goal,"robot4")
                                checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            for g in goals_to_check:
                if(g not in visited_nodes):
                    print("topmost unvisited node")
                    print(g)
                    robot4Goal=g
                    sendGoalRectilinear(robot4Goal,"robot4")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)
            for g in global_goals:
                if(g not in visited_nodes):
                    print("topmost unvisited node from other tree")
                    print(g)
                    robot1Goal=g
                    #visited_nodes.append(robot1Goal)
                    sendGoalRectilinear(robot4Goal,"robot4")
                    checkStatus(robot1Goal,robot2Goal,robot3Goal,robot4Goal)

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

def checkStatus(tup_goal1, tup_goal2,tup_goal3, tup_goal4):

    global prevStatus1
    global prevStatus2
    global robot1Stack
    global robot2Stack
    global prevStatus3
    global prevStatus4
    global robot3Stack
    global robot4Stack
    global cluster1Status
    global cluster2Status
    global cluster3Status
    global cluster4Status
    global visited_nodes
    global Status1Checker
    global Status2Checker
    global Status3Checker
    global Status4Checker

    print(cluster1Status)
    #print(prevStatus1)
    successStatus="status: 3"
    acceptedStatus="status: 1"
    status1 = rospy.wait_for_message("/robot1/move_base/status", GoalStatusArray)
    l1=status1.status_list
    statuslength1=len(l1)
    if(statuslength1>0):
        statusString=str(l1[0])
        if(prevStatus1 in statusString and prevStatus1!="" and Status1Checker<5):
            if(prevStatus1=="status: 3"):
                Status1Checker+=1
            else:
                Status1Checker=0 
            print("same status : continue checking")
        else:
            Status1Checker=0
            successStatus="status: 3"
            abortedStatus="status: 4"
            if successStatus in statusString:
                prevStatus1=successStatus
                print("reached goal : going to call callback with this root")
                print(tup_goal1)
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                if(cluster1Status=="all"):
                    visited_nodes.append(tup_goal1)
                    prevStatus2=successStatus
                    prevStatus3=successStatus
                    prevStatus4=successStatus
                    callback(msg,tup_goal1,robot1="all",robot2="all",robot3="all",robot4="all")
                elif(cluster1Status=="both"):
                    visited_nodes.append(tup_goal1)
                    prevStatus2=successStatus
                    callback(msg,tup_goal1,robot1="both",robot2="both",robot3=None,robot4=None)
                else:
                    visited_nodes.append(tup_goal1)
                    callback(msg,tup_goal1,robot1="robot1",robot2=None,robot3=None,robot4=None)
            elif(acceptedStatus in statusString):
                prevStatus1=acceptedStatus
    print(cluster2Status)
    #print(prevStatus2)
    status2 = rospy.wait_for_message("/robot2/move_base/status", GoalStatusArray)
    l2=status2.status_list
    statuslength2=len(l2)
    if(statuslength2>0):
        statusString=str(l2[0])
        print(statusString)
        if(prevStatus2 in statusString and prevStatus2!="" and Status2Checker<5):

            if(prevStatus2=="status: 3"):
                Status2Checker+=1
            else:
                Status2Checker=0
            print("same status : continue checking")
        else:
            Status2Checker=0
            successStatus="status: 3"
            abortedStatus="status: 2"
            if successStatus in statusString:
                prevStatus2=successStatus
                #visited_nodes.append(tup_goal2)
                print("reached goal: going to call callback with this root")
                print(tup_goal2)
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                
                if(cluster2Status=="all"):
                    visited_nodes.append(tup_goal1)
                    prevStatus1=successStatus
                    prevStatus3=successStatus
                    prevStatus4=successStatus
                    callback(msg,tup_goal1,robot1="all",robot2="all",robot3="all",robot4="all")
                elif(cluster2Status=="both"):
                    visited_nodes.append(tup_goal1)
                    prevStatus1=successStatus
                    callback(msg,tup_goal1,robot1="both",robot2="both",robot3=None,robot4=None)
                else:
                    visited_nodes.append(tup_goal2)
                    callback(msg,tup_goal2,robot1=None,robot2="robot2",robot3=None,robot4=None)
            elif(acceptedStatus in statusString):
                prevStatus2=acceptedStatus
    print(cluster3Status)
    #print(prevStatus3)
    status3 = rospy.wait_for_message("/robot3/move_base/status", GoalStatusArray)
    l3=status3.status_list
    statuslength3=len(l3)
    if(statuslength3>0):
        statusString=str(l3[0])
        #print(statusString)
        if(prevStatus3 in statusString and prevStatus3!="" and Status3Checker<5):  
            if(prevStatus3=="status: 3"):
                Status3Checker+=1
            else:
                Status3Checker=0
            print("same status : continue checking")
        else:
            if successStatus in statusString:
                prevStatus3=successStatus
                #visited_nodes.append(tup_goal3)
                print("reached goal: going to call callback with this root")
                print(tup_goal3)
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                
                if(cluster3Status=="all"):
                    visited_nodes.append(tup_goal1)
                    prevStatus1=successStatus
                    prevStatus2=successStatus
                    prevStatus4=successStatus
                    callback(msg,tup_goal1,robot1="all",robot2="all",robot3="all",robot4="all")
                elif(cluster3Status=="both"):
                    visited_nodes.append(tup_goal3)
                    prevStatus4=successStatus
                    callback(msg,tup_goal3,robot1=None,robot2=None,robot3="both",robot4="both")
                else:
                    visited_nodes.append(tup_goal3)
                    callback(msg,tup_goal3,robot1=None,robot2=None,robot3="robot3",robot4=None)
            elif(acceptedStatus in statusString):
                prevStatus3=acceptedStatus
    print(cluster4Status)
    #print(prevStatus4)
    status4 = rospy.wait_for_message("/robot4/move_base/status", GoalStatusArray)
    l4=status4.status_list
    statuslength4=len(l4)
    if(statuslength4>0):
        statusString=str(l4[0])
        if(prevStatus4 in statusString and prevStatus4!="" and Status4Checker<5):
            if(prevStatus4=="status: 3"):
                Status4Checker+=1
            else:
                Status4Checker=0   
            print("same status : continue checking")
        else:
            Status4Checker=0
            if successStatus in statusString:
                prevStatus4=successStatus
                #visited_nodes.append(tup_goal4)
                print("reached goal: going to call callback with this root")
                print(tup_goal4)
                msg = rospy.wait_for_message("/projected_map", OccupancyGrid)
                
                if(cluster4Status=="all"):
                    visited_nodes.append(tup_goal1)
                    prevStatus1=successStatus
                    prevStatus2=successStatus
                    prevStatus3=successStatus
                    callback(msg,tup_goal1,robot1="all",robot2="all",robot3="all",robot4="all")
                elif(cluster4Status=="both"):
                    visited_nodes.append(tup_goal3)
                    prevStatus3=successStatus
                    callback(msg,tup_goal3,robot1=None,robot2=None,robot3="both",robot4="both")
                else:
                    visited_nodes.append(tup_goal4)
                    callback(msg,tup_goal4,robot1=None,robot2=None,robot3=None,robot4="robot4")
            elif(acceptedStatus in statusString):
                prevStatus4=acceptedStatus
    rospy.sleep(2.0)
    checkStatus(tup_goal1,tup_goal2,tup_goal3,tup_goal4)
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
    print(tup_goal)
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

def getindices(frontier):
    global orig_x
    global orig_y
    delta=0.25
    x= frontier[0]
    y= frontier[1]
    j = (x - orig_x)/delta
    i = (y - orig_y)/delta
    return(i, j)

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

    callback(msg,curr_root,"all","all","all","all")
   


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
        p.publish(twist)
        rospy.sleep(0.1) 

    twist = Twist()
    rospy.loginfo("Stopping!")
    p.publish(twist)

if __name__ == '__main__':
    print('Initialized')
    start_time=time.time()
    rospy.init_node('SubscribeOccupancyGrid', anonymous=True)
    insert_origin()
    #rotateInPlace("robot1")
    #rotateInPlace("robot2")
    global_root=(0,0)
    scan(global_root,"robot1")