# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ite_info: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ite_info_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv" NAME_WE)
add_custom_target(_ite_info_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ite_info" "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv" "geometry_msgs/Quaternion:std_msgs/Header:geometry_msgs/Point:geometry_msgs/PoseArray:geometry_msgs/Pose"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(ite_info
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseArray.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_info
)

### Generating Module File
_generate_module_cpp(ite_info
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_info
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ite_info_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ite_info_generate_messages ite_info_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv" NAME_WE)
add_dependencies(ite_info_generate_messages_cpp _ite_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ite_info_gencpp)
add_dependencies(ite_info_gencpp ite_info_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ite_info_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(ite_info
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseArray.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_info
)

### Generating Module File
_generate_module_lisp(ite_info
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_info
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ite_info_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ite_info_generate_messages ite_info_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv" NAME_WE)
add_dependencies(ite_info_generate_messages_lisp _ite_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ite_info_genlisp)
add_dependencies(ite_info_genlisp ite_info_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ite_info_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(ite_info
  "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/PoseArray.msg;/opt/ros/indigo/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_info
)

### Generating Module File
_generate_module_py(ite_info
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_info
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ite_info_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ite_info_generate_messages ite_info_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aravind/catkin_ws_ite/src/ite_core/ite_info/srv/orienteering.srv" NAME_WE)
add_dependencies(ite_info_generate_messages_py _ite_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ite_info_genpy)
add_dependencies(ite_info_genpy ite_info_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ite_info_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_info)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ite_info
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(ite_info_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(ite_info_generate_messages_cpp geometry_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_info)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ite_info
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(ite_info_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(ite_info_generate_messages_lisp geometry_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_info)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_info\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ite_info
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(ite_info_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(ite_info_generate_messages_py geometry_msgs_generate_messages_py)
