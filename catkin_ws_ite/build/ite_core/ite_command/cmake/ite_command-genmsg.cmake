# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ite_command: 8 messages, 0 services")

set(MSG_I_FLAGS "-Iite_command:/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Iite_trajopt:/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ite_command_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg" "ite_trajopt/StatesControls:std_msgs/MultiArrayLayout:std_msgs/Header:std_msgs/MultiArrayDimension:std_msgs/Float32MultiArray"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg" "ite_command/RobotActions:geometry_msgs/Point:geometry_msgs/Quaternion:std_msgs/String:std_msgs/Header:geometry_msgs/PoseStamped:ite_command/InfoPath:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg" "geometry_msgs/Point:std_msgs/String:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/PoseStamped:ite_command/InfoPath:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg" "geometry_msgs/Quaternion:geometry_msgs/Point:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg" "geometry_msgs/Point:geometry_msgs/Pose:geometry_msgs/Quaternion:std_msgs/Header:ite_command/TrajectoryData"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg" "ite_command/RobotActions:geometry_msgs/Point:std_msgs/Float32MultiArray:ite_command/TeamActions:std_msgs/MultiArrayLayout:ite_command/InfoTraj:std_msgs/String:geometry_msgs/Quaternion:std_msgs/MultiArrayDimension:ite_trajopt/StatesControls:geometry_msgs/Pose:geometry_msgs/PoseStamped:ite_command/InfoPath:std_msgs/Header"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg" "geometry_msgs/Quaternion:geometry_msgs/Point:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg" NAME_WE)
add_custom_target(_ite_command_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_command" "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg" "geometry_msgs/Point:geometry_msgs/Pose:geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/PoseArray"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg/StatesControls.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Float32MultiArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg/StatesControls.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)
_generate_msg_cpp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
)

### Generating Services

### Generating Module File
_generate_module_cpp(ite_command
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ite_command_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ite_command_generate_messages ite_command_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_cpp _ite_command_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ite_command_gencpp)
add_dependencies(ite_command_gencpp ite_command_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ite_command_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg/StatesControls.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Float32MultiArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg/StatesControls.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)
_generate_msg_lisp(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
)

### Generating Services

### Generating Module File
_generate_module_lisp(ite_command
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ite_command_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ite_command_generate_messages ite_command_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_lisp _ite_command_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ite_command_genlisp)
add_dependencies(ite_command_genlisp ite_command_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ite_command_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg/StatesControls.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Float32MultiArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Float32MultiArray.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayLayout.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/MultiArrayDimension.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_trajopt/msg/StatesControls.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg"
  "${MSG_I_FLAGS}"
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/String.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)
_generate_msg_py(ite_command
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseArray.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
)

### Generating Services

### Generating Module File
_generate_module_py(ite_command
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ite_command_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ite_command_generate_messages ite_command_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoTraj.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TeamActions.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/RobotActions.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/TrajectoryData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/ExploreSystemData.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/InfoPath.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_command/msg/PlanData2.msg" NAME_WE)
add_dependencies(ite_command_generate_messages_py _ite_command_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ite_command_genpy)
add_dependencies(ite_command_genpy ite_command_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ite_command_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_command
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(ite_command_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(ite_command_generate_messages_cpp geometry_msgs_generate_messages_cpp)
add_dependencies(ite_command_generate_messages_cpp ite_trajopt_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_command
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(ite_command_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(ite_command_generate_messages_lisp geometry_msgs_generate_messages_lisp)
add_dependencies(ite_command_generate_messages_lisp ite_trajopt_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_command
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(ite_command_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(ite_command_generate_messages_py geometry_msgs_generate_messages_py)
add_dependencies(ite_command_generate_messages_py ite_trajopt_generate_messages_py)
