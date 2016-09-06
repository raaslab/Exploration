#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import Tkinter as tk
import sys
import time

def update_timeText():
	(trans,rot) = listener.lookupTransform('odom', 'base_link', rospy.Time(0))
	current="Position of the center of the tag from the drone: \n"
	current+="x: " + str(trans[0]) +"\n"
	current+="y: " + str(trans[1]) +"\n"
	current+="z: " + str(trans[2]) +"\n"
	timeText.configure(text=current)
	root.after(1000, update_timeText)
    
rospy.init_node('pose_gui')
listener = tf.TransformListener()
root = tk.Tk()
root.geometry("640x200")
root.wm_title("Relative Pose")
# Create a timeText Label (a text box)
timeText = tk.Label(root, text="", font=("Helvetica", 20))
timeText.pack()
update_timeText()
root.mainloop()