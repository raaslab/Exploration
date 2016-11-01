#!/usr/bin/env python
import rospy
import roslaunch

if __name__ == '__main__':
	while(True):
		package = 'beginner_tutorials'
		executable = 'merge_occ_grids'
		node = roslaunch.core.Node(package, executable)
		launch = roslaunch.scriptapi.ROSLaunch()
		launch.start()
		process = launch.launch(node)
		print process.is_alive()
		rospy.sleep(5)
		process.stop()
		rospy.sleep(20)




