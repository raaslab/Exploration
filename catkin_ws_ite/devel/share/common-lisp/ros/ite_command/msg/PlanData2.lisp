; Auto-generated. Do not edit!


(cl:in-package ite_command-msg)


;//! \htmlinclude PlanData2.msg.html

(cl:defclass <PlanData2> (roslisp-msg-protocol:ros-message)
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
    :type cl:boolean
    :initform cl:nil)
   (quad
    :reader quad
    :initarg :quad
    :type cl:boolean
    :initform cl:nil)
   (scarab_action
    :reader scarab_action
    :initarg :scarab_action
    :type cl:boolean
    :initform cl:nil)
   (quad_action
    :reader quad_action
    :initarg :quad_action
    :type cl:boolean
    :initform cl:nil)
   (scarab_trajs
    :reader scarab_trajs
    :initarg :scarab_trajs
    :type (cl:vector geometry_msgs-msg:PoseArray)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:PoseArray :initial-element (cl:make-instance 'geometry_msgs-msg:PoseArray)))
   (quad_trajs
    :reader quad_trajs
    :initarg :quad_trajs
    :type (cl:vector geometry_msgs-msg:PoseArray)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:PoseArray :initial-element (cl:make-instance 'geometry_msgs-msg:PoseArray))))
)

(cl:defclass PlanData2 (<PlanData2>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlanData2>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlanData2)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_command-msg:<PlanData2> is deprecated: use ite_command-msg:PlanData2 instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:header-val is deprecated.  Use ite_command-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'planner_type-val :lambda-list '(m))
(cl:defmethod planner_type-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:planner_type-val is deprecated.  Use ite_command-msg:planner_type instead.")
  (planner_type m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:duration-val is deprecated.  Use ite_command-msg:duration instead.")
  (duration m))

(cl:ensure-generic-function 'scarab-val :lambda-list '(m))
(cl:defmethod scarab-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:scarab-val is deprecated.  Use ite_command-msg:scarab instead.")
  (scarab m))

(cl:ensure-generic-function 'quad-val :lambda-list '(m))
(cl:defmethod quad-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:quad-val is deprecated.  Use ite_command-msg:quad instead.")
  (quad m))

(cl:ensure-generic-function 'scarab_action-val :lambda-list '(m))
(cl:defmethod scarab_action-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:scarab_action-val is deprecated.  Use ite_command-msg:scarab_action instead.")
  (scarab_action m))

(cl:ensure-generic-function 'quad_action-val :lambda-list '(m))
(cl:defmethod quad_action-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:quad_action-val is deprecated.  Use ite_command-msg:quad_action instead.")
  (quad_action m))

(cl:ensure-generic-function 'scarab_trajs-val :lambda-list '(m))
(cl:defmethod scarab_trajs-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:scarab_trajs-val is deprecated.  Use ite_command-msg:scarab_trajs instead.")
  (scarab_trajs m))

(cl:ensure-generic-function 'quad_trajs-val :lambda-list '(m))
(cl:defmethod quad_trajs-val ((m <PlanData2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:quad_trajs-val is deprecated.  Use ite_command-msg:quad_trajs instead.")
  (quad_trajs m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlanData2>) ostream)
  "Serializes a message object of type '<PlanData2>"
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
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'scarab) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'quad) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'scarab_action) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'quad_action) 1 0)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'scarab_trajs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'scarab_trajs))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'quad_trajs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'quad_trajs))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlanData2>) istream)
  "Deserializes a message object of type '<PlanData2>"
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
    (cl:setf (cl:slot-value msg 'scarab) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'quad) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'scarab_action) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'quad_action) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'scarab_trajs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'scarab_trajs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:PoseArray))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'quad_trajs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'quad_trajs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:PoseArray))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlanData2>)))
  "Returns string type for a message object of type '<PlanData2>"
  "ite_command/PlanData2")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlanData2)))
  "Returns string type for a message object of type 'PlanData2"
  "ite_command/PlanData2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlanData2>)))
  "Returns md5sum for a message object of type '<PlanData2>"
  "10929a349c15b7d172c404c6c7b2ff74")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlanData2)))
  "Returns md5sum for a message object of type 'PlanData2"
  "10929a349c15b7d172c404c6c7b2ff74")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlanData2>)))
  "Returns full string definition for message of type '<PlanData2>"
  (cl:format cl:nil "std_msgs/Header header # Contains plan number and planning start time~%string planner_type~%float64 duration       # How long to plan (sec)~%~%bool scarab            # True if planning for scarab~%bool quad              # True if planning for quad~%~%bool scarab_action     # True if generated action for scarab~%bool quad_action       # True if generated action for quad~%~%geometry_msgs/PoseArray[] scarab_trajs~%geometry_msgs/PoseArray[] quad_trajs~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/PoseArray~%# An array of poses with a header for global reference.~%~%Header header~%~%Pose[] poses~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlanData2)))
  "Returns full string definition for message of type 'PlanData2"
  (cl:format cl:nil "std_msgs/Header header # Contains plan number and planning start time~%string planner_type~%float64 duration       # How long to plan (sec)~%~%bool scarab            # True if planning for scarab~%bool quad              # True if planning for quad~%~%bool scarab_action     # True if generated action for scarab~%bool quad_action       # True if generated action for quad~%~%geometry_msgs/PoseArray[] scarab_trajs~%geometry_msgs/PoseArray[] quad_trajs~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/PoseArray~%# An array of poses with a header for global reference.~%~%Header header~%~%Pose[] poses~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlanData2>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'planner_type))
     8
     1
     1
     1
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'scarab_trajs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'quad_trajs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlanData2>))
  "Converts a ROS message object to a list"
  (cl:list 'PlanData2
    (cl:cons ':header (header msg))
    (cl:cons ':planner_type (planner_type msg))
    (cl:cons ':duration (duration msg))
    (cl:cons ':scarab (scarab msg))
    (cl:cons ':quad (quad msg))
    (cl:cons ':scarab_action (scarab_action msg))
    (cl:cons ':quad_action (quad_action msg))
    (cl:cons ':scarab_trajs (scarab_trajs msg))
    (cl:cons ':quad_trajs (quad_trajs msg))
))
