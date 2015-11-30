# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/indigo/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/indigo/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in "/home/technologic/catkin_ws/devel_isolated/robot_setup_tf;/home/technologic/catkin_ws/devel_isolated/my_robot_name_2dnav;/home/technologic/catkin_ws/devel_isolated/move_base;/home/technologic/catkin_ws/devel_isolated/rotate_recovery;/home/technologic/catkin_ws/devel_isolated/global_planner;/home/technologic/catkin_ws/devel_isolated/navfn;/home/technologic/catkin_ws/devel_isolated/move_slow_and_clear;/home/technologic/catkin_ws/devel_isolated/dwa_local_planner;/home/technologic/catkin_ws/devel_isolated/clear_costmap_recovery;/home/technologic/catkin_ws/devel_isolated/carrot_planner;/home/technologic/catkin_ws/devel_isolated/base_local_planner;/home/technologic/catkin_ws/devel_isolated/nav_core;/home/technologic/catkin_ws/devel_isolated/costmap_2d;/home/technologic/catkin_ws/devel_isolated/voxel_grid;/home/technologic/catkin_ws/devel_isolated/tech_control;/home/technologic/catkin_ws/devel_isolated/simple_navigation_goals;/home/technologic/catkin_ws/devel_isolated/rosaria;/home/technologic/catkin_ws/devel_isolated/robot_pose_ekf;/home/technologic/catkin_ws/devel_isolated/p3dx_gazebo;/home/technologic/catkin_ws/devel_isolated/p3dx_description;/home/technologic/catkin_ws/devel_isolated/p3dx_control;/home/technologic/catkin_ws/devel_isolated/navigation;/home/technologic/catkin_ws/devel_isolated/amcl;/home/technologic/catkin_ws/devel_isolated/map_server;/home/technologic/catkin_ws/devel_isolated/fake_localization;/home/technologic/catkin_ws/devel_isolated/beginner_tutorials;/home/technologic/catkin_ws/devel;/opt/ros/indigo".split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/technologic/catkin_ws/devel_isolated/navigation/env.sh')

output_filename = '/home/technologic/catkin_ws/build_isolated/navigation/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
