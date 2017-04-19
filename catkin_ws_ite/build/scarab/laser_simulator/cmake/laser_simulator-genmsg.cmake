# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "laser_simulator: 3 messages, 0 services")

set(MSG_I_FLAGS "-Ilaser_simulator:/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg;-Inav_msgs:/opt/ros/indigo/share/nav_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/indigo/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(laser_simulator_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg" NAME_WE)
add_custom_target(_laser_simulator_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "laser_simulator" "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg" "geometry_msgs/Point:geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg" NAME_WE)
add_custom_target(_laser_simulator_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "laser_simulator" "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg" "geometry_msgs/Point:laser_simulator/PoseStampedNamed:geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg" NAME_WE)
add_custom_target(_laser_simulator_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "laser_simulator" "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg" "geometry_msgs/Point:geometry_msgs/Vector3:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Transform:sensor_msgs/LaserScan:geometry_msgs/Pose"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/laser_simulator
)
_generate_msg_cpp(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/laser_simulator
)
_generate_msg_cpp(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/LaserScan.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/laser_simulator
)

### Generating Services

### Generating Module File
_generate_module_cpp(laser_simulator
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/laser_simulator
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(laser_simulator_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(laser_simulator_generate_messages laser_simulator_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_cpp _laser_simulator_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_cpp _laser_simulator_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_cpp _laser_simulator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(laser_simulator_gencpp)
add_dependencies(laser_simulator_gencpp laser_simulator_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS laser_simulator_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/laser_simulator
)
_generate_msg_lisp(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/laser_simulator
)
_generate_msg_lisp(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/LaserScan.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/laser_simulator
)

### Generating Services

### Generating Module File
_generate_module_lisp(laser_simulator
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/laser_simulator
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(laser_simulator_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(laser_simulator_generate_messages laser_simulator_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_lisp _laser_simulator_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_lisp _laser_simulator_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_lisp _laser_simulator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(laser_simulator_genlisp)
add_dependencies(laser_simulator_genlisp laser_simulator_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS laser_simulator_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/laser_simulator
)
_generate_msg_py(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/laser_simulator
)
_generate_msg_py(laser_simulator
  "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/LaserScan.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/laser_simulator
)

### Generating Services

### Generating Module File
_generate_module_py(laser_simulator
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/laser_simulator
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(laser_simulator_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(laser_simulator_generate_messages laser_simulator_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamed.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_py _laser_simulator_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/PoseStampedNamedArray.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_py _laser_simulator_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/scarab/laser_simulator/msg/ScanPair.msg" NAME_WE)
add_dependencies(laser_simulator_generate_messages_py _laser_simulator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(laser_simulator_genpy)
add_dependencies(laser_simulator_genpy laser_simulator_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS laser_simulator_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/laser_simulator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/laser_simulator
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(laser_simulator_generate_messages_cpp nav_msgs_generate_messages_cpp)
add_dependencies(laser_simulator_generate_messages_cpp sensor_msgs_generate_messages_cpp)
add_dependencies(laser_simulator_generate_messages_cpp geometry_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/laser_simulator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/laser_simulator
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(laser_simulator_generate_messages_lisp nav_msgs_generate_messages_lisp)
add_dependencies(laser_simulator_generate_messages_lisp sensor_msgs_generate_messages_lisp)
add_dependencies(laser_simulator_generate_messages_lisp geometry_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/laser_simulator)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/laser_simulator\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/laser_simulator
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(laser_simulator_generate_messages_py nav_msgs_generate_messages_py)
add_dependencies(laser_simulator_generate_messages_py sensor_msgs_generate_messages_py)
add_dependencies(laser_simulator_generate_messages_py geometry_msgs_generate_messages_py)
