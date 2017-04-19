; Auto-generated. Do not edit!


(cl:in-package ite_command-msg)


;//! \htmlinclude TeamActions.msg.html

(cl:defclass <TeamActions> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (planner_type
    :reader planner_type
    :initarg :planner_type
    :type cl:string
    :initform "")
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0)
   (scarab
    :reader scarab
    :initarg :scarab
    :type ite_command-msg:RobotActions
    :initform (cl:make-instance 'ite_command-msg:RobotActions))
   (quad
    :reader quad
    :initarg :quad
    :type ite_command-msg:RobotActions
    :initform (cl:make-instance 'ite_command-msg:RobotActions)))
)

(cl:defclass TeamActions (<TeamActions>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TeamActions>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TeamActions)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_command-msg:<TeamActions> is deprecated: use ite_command-msg:TeamActions instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <TeamActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:header-val is deprecated.  Use ite_command-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'planner_type-val :lambda-list '(m))
(cl:defmethod planner_type-val ((m <TeamActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:planner_type-val is deprecated.  Use ite_command-msg:planner_type instead.")
  (planner_type m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <TeamActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:duration-val is deprecated.  Use ite_command-msg:duration instead.")
  (duration m))

(cl:ensure-generic-function 'scarab-val :lambda-list '(m))
(cl:defmethod scarab-val ((m <TeamActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:scarab-val is deprecated.  Use ite_command-msg:scarab instead.")
  (scarab m))

(cl:ensure-generic-function 'quad-val :lambda-list '(m))
(cl:defmethod quad-val ((m <TeamActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:quad-val is deprecated.  Use ite_command-msg:quad instead.")
  (quad m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TeamActions>) ostream)
  "Serializes a message object of type '<TeamActions>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'planner_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'planner_type))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'scarab) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'quad) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TeamActions>) istream)
  "Deserializes a message object of type '<TeamActions>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'planner_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'planner_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'scarab) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'quad) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TeamActions>)))
  "Returns string type for a message object of type '<TeamActions>"
  "ite_command/TeamActions")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TeamActions)))
  "Returns string type for a message object of type 'TeamActions"
  "ite_command/TeamActions")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TeamActions>)))
  "Returns md5sum for a message object of type '<TeamActions>"
  "a2644f81083808082cfaa9c0d038a7ce")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TeamActions)))
  "Returns md5sum for a message object of type 'TeamActions"
  "a2644f81083808082cfaa9c0d038a7ce")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TeamActions>)))
  "Returns full string definition for message of type '<TeamActions>"
  (cl:format cl:nil "std_msgs/Header header~%string planner_type~%float64 duration # How long to plan (sec)~%~%RobotActions scarab~%RobotActions quad~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ite_command/RobotActions~%std_msgs/String name~%geometry_msgs/PoseStamped pose # Robot's pose~%InfoPath[] paths~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: ite_command/InfoPath~%geometry_msgs/Pose[] poses~%float64 info # Information of path~%float64 endpose_info # Information at final pose~%float64 time # Time to execute path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TeamActions)))
  "Returns full string definition for message of type 'TeamActions"
  (cl:format cl:nil "std_msgs/Header header~%string planner_type~%float64 duration # How long to plan (sec)~%~%RobotActions scarab~%RobotActions quad~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: ite_command/RobotActions~%std_msgs/String name~%geometry_msgs/PoseStamped pose # Robot's pose~%InfoPath[] paths~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: ite_command/InfoPath~%geometry_msgs/Pose[] poses~%float64 info # Information of path~%float64 endpose_info # Information at final pose~%float64 time # Time to execute path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TeamActions>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'planner_type))
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'scarab))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'quad))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TeamActions>))
  "Converts a ROS message object to a list"
  (cl:list 'TeamActions
    (cl:cons ':header (header msg))
    (cl:cons ':planner_type (planner_type msg))
    (cl:cons ':duration (duration msg))
    (cl:cons ':scarab (scarab msg))
    (cl:cons ':quad (quad msg))
))
