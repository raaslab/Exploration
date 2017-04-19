; Auto-generated. Do not edit!


(cl:in-package ite_command-msg)


;//! \htmlinclude TrajectoryData.msg.html

(cl:defclass <TrajectoryData> (roslisp-msg-protocol:ros-message)
  ((robot_poses
    :reader robot_poses
    :initarg :robot_poses
    :type (cl:vector geometry_msgs-msg:Pose)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Pose :initial-element (cl:make-instance 'geometry_msgs-msg:Pose)))
   (sensor_poses
    :reader sensor_poses
    :initarg :sensor_poses
    :type (cl:vector geometry_msgs-msg:Pose)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Pose :initial-element (cl:make-instance 'geometry_msgs-msg:Pose)))
   (total_info
    :reader total_info
    :initarg :total_info
    :type cl:float
    :initform 0.0)
   (infos
    :reader infos
    :initarg :infos
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass TrajectoryData (<TrajectoryData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrajectoryData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrajectoryData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_command-msg:<TrajectoryData> is deprecated: use ite_command-msg:TrajectoryData instead.")))

(cl:ensure-generic-function 'robot_poses-val :lambda-list '(m))
(cl:defmethod robot_poses-val ((m <TrajectoryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:robot_poses-val is deprecated.  Use ite_command-msg:robot_poses instead.")
  (robot_poses m))

(cl:ensure-generic-function 'sensor_poses-val :lambda-list '(m))
(cl:defmethod sensor_poses-val ((m <TrajectoryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:sensor_poses-val is deprecated.  Use ite_command-msg:sensor_poses instead.")
  (sensor_poses m))

(cl:ensure-generic-function 'total_info-val :lambda-list '(m))
(cl:defmethod total_info-val ((m <TrajectoryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:total_info-val is deprecated.  Use ite_command-msg:total_info instead.")
  (total_info m))

(cl:ensure-generic-function 'infos-val :lambda-list '(m))
(cl:defmethod infos-val ((m <TrajectoryData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:infos-val is deprecated.  Use ite_command-msg:infos instead.")
  (infos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrajectoryData>) ostream)
  "Serializes a message object of type '<TrajectoryData>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'robot_poses))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'robot_poses))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'sensor_poses))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'sensor_poses))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'total_info))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'infos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'infos))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrajectoryData>) istream)
  "Deserializes a message object of type '<TrajectoryData>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'robot_poses) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'robot_poses)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Pose))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'sensor_poses) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'sensor_poses)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Pose))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'total_info) (roslisp-utils:decode-double-float-bits bits)))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'infos) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'infos)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrajectoryData>)))
  "Returns string type for a message object of type '<TrajectoryData>"
  "ite_command/TrajectoryData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrajectoryData)))
  "Returns string type for a message object of type 'TrajectoryData"
  "ite_command/TrajectoryData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrajectoryData>)))
  "Returns md5sum for a message object of type '<TrajectoryData>"
  "8f69a1bb71500cb87fbf01e2ad7a25b9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrajectoryData)))
  "Returns md5sum for a message object of type 'TrajectoryData"
  "8f69a1bb71500cb87fbf01e2ad7a25b9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrajectoryData>)))
  "Returns full string definition for message of type '<TrajectoryData>"
  (cl:format cl:nil "geometry_msgs/Pose[] robot_poses~%geometry_msgs/Pose[] sensor_poses~%float64 total_info~%float64[] infos # Information~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrajectoryData)))
  "Returns full string definition for message of type 'TrajectoryData"
  (cl:format cl:nil "geometry_msgs/Pose[] robot_poses~%geometry_msgs/Pose[] sensor_poses~%float64 total_info~%float64[] infos # Information~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrajectoryData>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'robot_poses) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'sensor_poses) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     8
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'infos) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrajectoryData>))
  "Converts a ROS message object to a list"
  (cl:list 'TrajectoryData
    (cl:cons ':robot_poses (robot_poses msg))
    (cl:cons ':sensor_poses (sensor_poses msg))
    (cl:cons ':total_info (total_info msg))
    (cl:cons ':infos (infos msg))
))
