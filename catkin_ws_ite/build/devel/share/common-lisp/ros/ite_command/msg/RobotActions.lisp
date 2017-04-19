; Auto-generated. Do not edit!


(cl:in-package ite_command-msg)


;//! \htmlinclude RobotActions.msg.html

(cl:defclass <RobotActions> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (paths
    :reader paths
    :initarg :paths
    :type (cl:vector ite_command-msg:InfoPath)
   :initform (cl:make-array 0 :element-type 'ite_command-msg:InfoPath :initial-element (cl:make-instance 'ite_command-msg:InfoPath))))
)

(cl:defclass RobotActions (<RobotActions>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RobotActions>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RobotActions)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_command-msg:<RobotActions> is deprecated: use ite_command-msg:RobotActions instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <RobotActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:name-val is deprecated.  Use ite_command-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <RobotActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:pose-val is deprecated.  Use ite_command-msg:pose instead.")
  (pose m))

(cl:ensure-generic-function 'paths-val :lambda-list '(m))
(cl:defmethod paths-val ((m <RobotActions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:paths-val is deprecated.  Use ite_command-msg:paths instead.")
  (paths m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RobotActions>) ostream)
  "Serializes a message object of type '<RobotActions>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'name) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'paths))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'paths))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RobotActions>) istream)
  "Deserializes a message object of type '<RobotActions>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'name) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'paths) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'paths)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ite_command-msg:InfoPath))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RobotActions>)))
  "Returns string type for a message object of type '<RobotActions>"
  "ite_command/RobotActions")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RobotActions)))
  "Returns string type for a message object of type 'RobotActions"
  "ite_command/RobotActions")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RobotActions>)))
  "Returns md5sum for a message object of type '<RobotActions>"
  "d9cec365aace15b18e050f08b37b8f61")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RobotActions)))
  "Returns md5sum for a message object of type 'RobotActions"
  "d9cec365aace15b18e050f08b37b8f61")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RobotActions>)))
  "Returns full string definition for message of type '<RobotActions>"
  (cl:format cl:nil "std_msgs/String name~%geometry_msgs/PoseStamped pose # Robot's pose~%InfoPath[] paths~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: ite_command/InfoPath~%geometry_msgs/Pose[] poses~%float64 info # Information of path~%float64 endpose_info # Information at final pose~%float64 time # Time to execute path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RobotActions)))
  "Returns full string definition for message of type 'RobotActions"
  (cl:format cl:nil "std_msgs/String name~%geometry_msgs/PoseStamped pose # Robot's pose~%InfoPath[] paths~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: ite_command/InfoPath~%geometry_msgs/Pose[] poses~%float64 info # Information of path~%float64 endpose_info # Information at final pose~%float64 time # Time to execute path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RobotActions>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'paths) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RobotActions>))
  "Converts a ROS message object to a list"
  (cl:list 'RobotActions
    (cl:cons ':name (name msg))
    (cl:cons ':pose (pose msg))
    (cl:cons ':paths (paths msg))
))
