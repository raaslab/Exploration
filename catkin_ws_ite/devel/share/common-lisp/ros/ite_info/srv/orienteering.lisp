; Auto-generated. Do not edit!


(cl:in-package ite_info-srv)


;//! \htmlinclude orienteering-request.msg.html

(cl:defclass <orienteering-request> (roslisp-msg-protocol:ros-message)
  ((source
    :reader source
    :initarg :source
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (goal
    :reader goal
    :initarg :goal
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (budget
    :reader budget
    :initarg :budget
    :type cl:float
    :initform 0.0)
   (robotname
    :reader robotname
    :initarg :robotname
    :type cl:string
    :initform "")
   (input_graph
    :reader input_graph
    :initarg :input_graph
    :type geometry_msgs-msg:PoseArray
    :initform (cl:make-instance 'geometry_msgs-msg:PoseArray)))
)

(cl:defclass orienteering-request (<orienteering-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <orienteering-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'orienteering-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_info-srv:<orienteering-request> is deprecated: use ite_info-srv:orienteering-request instead.")))

(cl:ensure-generic-function 'source-val :lambda-list '(m))
(cl:defmethod source-val ((m <orienteering-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_info-srv:source-val is deprecated.  Use ite_info-srv:source instead.")
  (source m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <orienteering-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_info-srv:goal-val is deprecated.  Use ite_info-srv:goal instead.")
  (goal m))

(cl:ensure-generic-function 'budget-val :lambda-list '(m))
(cl:defmethod budget-val ((m <orienteering-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_info-srv:budget-val is deprecated.  Use ite_info-srv:budget instead.")
  (budget m))

(cl:ensure-generic-function 'robotname-val :lambda-list '(m))
(cl:defmethod robotname-val ((m <orienteering-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_info-srv:robotname-val is deprecated.  Use ite_info-srv:robotname instead.")
  (robotname m))

(cl:ensure-generic-function 'input_graph-val :lambda-list '(m))
(cl:defmethod input_graph-val ((m <orienteering-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_info-srv:input_graph-val is deprecated.  Use ite_info-srv:input_graph instead.")
  (input_graph m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <orienteering-request>) ostream)
  "Serializes a message object of type '<orienteering-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'source) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'budget))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'robotname))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'robotname))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'input_graph) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <orienteering-request>) istream)
  "Deserializes a message object of type '<orienteering-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'source) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'budget) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'robotname) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'robotname) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'input_graph) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<orienteering-request>)))
  "Returns string type for a service object of type '<orienteering-request>"
  "ite_info/orienteeringRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'orienteering-request)))
  "Returns string type for a service object of type 'orienteering-request"
  "ite_info/orienteeringRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<orienteering-request>)))
  "Returns md5sum for a message object of type '<orienteering-request>"
  "9f2296b6b4b8ad3a36051f1ff187b6db")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'orienteering-request)))
  "Returns md5sum for a message object of type 'orienteering-request"
  "9f2296b6b4b8ad3a36051f1ff187b6db")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<orienteering-request>)))
  "Returns full string definition for message of type '<orienteering-request>"
  (cl:format cl:nil "geometry_msgs/Pose source~%geometry_msgs/Pose goal~%float64 budget~%string robotname~%geometry_msgs/PoseArray input_graph~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/PoseArray~%# An array of poses with a header for global reference.~%~%Header header~%~%Pose[] poses~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'orienteering-request)))
  "Returns full string definition for message of type 'orienteering-request"
  (cl:format cl:nil "geometry_msgs/Pose source~%geometry_msgs/Pose goal~%float64 budget~%string robotname~%geometry_msgs/PoseArray input_graph~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/PoseArray~%# An array of poses with a header for global reference.~%~%Header header~%~%Pose[] poses~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <orienteering-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'source))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
     8
     4 (cl:length (cl:slot-value msg 'robotname))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'input_graph))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <orienteering-request>))
  "Converts a ROS message object to a list"
  (cl:list 'orienteering-request
    (cl:cons ':source (source msg))
    (cl:cons ':goal (goal msg))
    (cl:cons ':budget (budget msg))
    (cl:cons ':robotname (robotname msg))
    (cl:cons ':input_graph (input_graph msg))
))
;//! \htmlinclude orienteering-response.msg.html

(cl:defclass <orienteering-response> (roslisp-msg-protocol:ros-message)
  ((orienteering_path
    :reader orienteering_path
    :initarg :orienteering_path
    :type geometry_msgs-msg:PoseArray
    :initform (cl:make-instance 'geometry_msgs-msg:PoseArray)))
)

(cl:defclass orienteering-response (<orienteering-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <orienteering-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'orienteering-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_info-srv:<orienteering-response> is deprecated: use ite_info-srv:orienteering-response instead.")))

(cl:ensure-generic-function 'orienteering_path-val :lambda-list '(m))
(cl:defmethod orienteering_path-val ((m <orienteering-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_info-srv:orienteering_path-val is deprecated.  Use ite_info-srv:orienteering_path instead.")
  (orienteering_path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <orienteering-response>) ostream)
  "Serializes a message object of type '<orienteering-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'orienteering_path) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <orienteering-response>) istream)
  "Deserializes a message object of type '<orienteering-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'orienteering_path) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<orienteering-response>)))
  "Returns string type for a service object of type '<orienteering-response>"
  "ite_info/orienteeringResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'orienteering-response)))
  "Returns string type for a service object of type 'orienteering-response"
  "ite_info/orienteeringResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<orienteering-response>)))
  "Returns md5sum for a message object of type '<orienteering-response>"
  "9f2296b6b4b8ad3a36051f1ff187b6db")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'orienteering-response)))
  "Returns md5sum for a message object of type 'orienteering-response"
  "9f2296b6b4b8ad3a36051f1ff187b6db")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<orienteering-response>)))
  "Returns full string definition for message of type '<orienteering-response>"
  (cl:format cl:nil "geometry_msgs/PoseArray orienteering_path~%~%================================================================================~%MSG: geometry_msgs/PoseArray~%# An array of poses with a header for global reference.~%~%Header header~%~%Pose[] poses~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'orienteering-response)))
  "Returns full string definition for message of type 'orienteering-response"
  (cl:format cl:nil "geometry_msgs/PoseArray orienteering_path~%~%================================================================================~%MSG: geometry_msgs/PoseArray~%# An array of poses with a header for global reference.~%~%Header header~%~%Pose[] poses~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <orienteering-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'orienteering_path))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <orienteering-response>))
  "Converts a ROS message object to a list"
  (cl:list 'orienteering-response
    (cl:cons ':orienteering_path (orienteering_path msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'orienteering)))
  'orienteering-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'orienteering)))
  'orienteering-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'orienteering)))
  "Returns string type for a service object of type '<orienteering>"
  "ite_info/orienteering")