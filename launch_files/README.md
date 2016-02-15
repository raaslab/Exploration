#######Steps for getting the pioneer running on gazebo############

1. Make sure Nav Stack and gmapping are installed.

 gmapping: sudo apt-get install ros-indigo-slam-gmapping
 	wiki: http://wiki.ros.org/gmapping

 navstack: sudo apt-get install ros-indigo-navigation
 	wiki: http://wiki.ros.org/navigation

2. Launch /launch/pioneer_gazebo_navigation.launch to bringup the gazebo environment.
3. Launch /pioneer_2dnav/launch/move_base_gmapping.launch to launch move_base and gmapping.
4. Launch /p3dx_description/launch/rviz.launch to launch rviz and visualize the robot





#####Steps for running the exploration code#######

1.Make sure Nav Stack and gmapping and robot_pose_publisher are installed.

 gmapping: sudo apt-get install ros-indigo-slam-gmapping
 	wiki: http://wiki.ros.org/gmapping

 navstack: sudo apt-get install ros-indigo-navigation
 	wiki: http://wiki.ros.org/navigation

robot pose publisher: http://wiki.ros.org/robot_pose_publisher


2. You would need to launch the following files:
- Exploration/launch_files/kinect/launch/pioneer.launch
	This will spawn the robot on gazebo with the kinect in gazebo.

- Exploration/launch_files/pioneer_2dnav/launch/move_base_gmap_gazebo.launch
    This will launch gmapping,move_base and the robot_pose_publisher nodes.

3. You can then launch rviz to visualize the robot and the topics being published.

4. Now execute the following command to launch the exploration node:
	rosrun technologicExploration SubscribeOccupancyGrid.py 

