; Auto-generated. Do not edit!


(cl:in-package ite_command-msg)


;//! \htmlinclude ExploreSystemData.msg.html

(cl:defclass <ExploreSystemData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (local_planner
    :reader local_planner
    :initarg :local_planner
    :type cl:string
    :initform "")
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (global_actions
    :reader global_actions
    :initarg :global_actions
    :type ite_command-msg:TeamActions
    :initform (cl:make-instance 'ite_command-msg:TeamActions))
   (global
    :reader global
    :initarg :global
    :type ite_command-msg:InfoTraj
    :initform (cl:make-instance 'ite_command-msg:InfoTraj))
   (local
    :reader local
    :initarg :local
    :type ite_command-msg:InfoTraj
    :initform (cl:make-instance 'ite_command-msg:InfoTraj))
   (global_remainder
    :reader global_remainder
    :initarg :global_remainder
    :type ite_command-msg:InfoTraj
    :initform (cl:make-instance 'ite_command-msg:InfoTraj))
   (optimized
    :reader optimized
    :initarg :optimized
    :type ite_command-msg:InfoTraj
    :initform (cl:make-instance 'ite_command-msg:InfoTraj))
   (optimize_local
    :reader optimize_local
    :initarg :optimize_local
    :type cl:boolean
    :initform cl:nil)
   (select_optimize
    :reader select_optimize
    :initarg :select_optimize
    :type cl:boolean
    :initform cl:nil)
   (optimization_duration
    :reader optimization_duration
    :initarg :optimization_duration
    :type cl:float
    :initform 0.0)
   (total_duration
    :reader total_duration
    :initarg :total_duration
    :type cl:float
    :initform 0.0))
)

(cl:defclass ExploreSystemData (<ExploreSystemData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExploreSystemData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExploreSystemData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_command-msg:<ExploreSystemData> is deprecated: use ite_command-msg:ExploreSystemData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:header-val is deprecated.  Use ite_command-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:name-val is deprecated.  Use ite_command-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'local_planner-val :lambda-list '(m))
(cl:defmethod local_planner-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:local_planner-val is deprecated.  Use ite_command-msg:local_planner instead.")
  (local_planner m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:pose-val is deprecated.  Use ite_command-msg:pose instead.")
  (pose m))

(cl:ensure-generic-function 'global_actions-val :lambda-list '(m))
(cl:defmethod global_actions-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:global_actions-val is deprecated.  Use ite_command-msg:global_actions instead.")
  (global_actions m))

(cl:ensure-generic-function 'global-val :lambda-list '(m))
(cl:defmethod global-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:global-val is deprecated.  Use ite_command-msg:global instead.")
  (global m))

(cl:ensure-generic-function 'local-val :lambda-list '(m))
(cl:defmethod local-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:local-val is deprecated.  Use ite_command-msg:local instead.")
  (local m))

(cl:ensure-generic-function 'global_remainder-val :lambda-list '(m))
(cl:defmethod global_remainder-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:global_remainder-val is deprecated.  Use ite_command-msg:global_remainder instead.")
  (global_remainder m))

(cl:ensure-generic-function 'optimized-val :lambda-list '(m))
(cl:defmethod optimized-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:optimized-val is deprecated.  Use ite_command-msg:optimized instead.")
  (optimized m))

(cl:ensure-generic-function 'optimize_local-val :lambda-list '(m))
(cl:defmethod optimize_local-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:optimize_local-val is deprecated.  Use ite_command-msg:optimize_local instead.")
  (optimize_local m))

(cl:ensure-generic-function 'select_optimize-val :lambda-list '(m))
(cl:defmethod select_optimize-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:select_optimize-val is deprecated.  Use ite_command-msg:select_optimize instead.")
  (select_optimize m))

(cl:ensure-generic-function 'optimization_duration-val :lambda-list '(m))
(cl:defmethod optimization_duration-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:optimization_duration-val is deprecated.  Use ite_command-msg:optimization_duration instead.")
  (optimization_duration m))

(cl:ensure-generic-function 'total_duration-val :lambda-list '(m))
(cl:defmethod total_duration-val ((m <ExploreSystemData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_command-msg:total_duration-val is deprecated.  Use ite_command-msg:total_duration instead.")
  (total_duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExploreSystemData>) ostream)
  "Serializes a message object of type '<ExploreSystemData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'local_planner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'local_planner))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'global_actions) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'global) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'local) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'global_remainder) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'optimized) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'optimize_local) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'select_optimize) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'optimization_duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'total_duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExploreSystemData>) istream)
  "Deserializes a message object of type '<ExploreSystemData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'local_planner) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'local_planner) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'global_actions) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'global) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'local) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'global_remainder) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'optimized) istream)
    (cl:setf (cl:slot-value msg 'optimize_local) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'select_optimize) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'optimization_duration) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'total_duration) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExploreSystemData>)))
  "Returns string type for a message object of type '<ExploreSystemData>"
  "ite_command/ExploreSystemData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExploreSystemData)))
  "Returns string type for a message object of type 'ExploreSystemData"
  "ite_command/ExploreSystemData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExploreSystemData>)))
  "Returns md5sum for a message object of type '<ExploreSystemData>"
  "a966e5115c1090ab6bcb0ea613336a66")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExploreSystemData)))
  "Returns md5sum for a message object of type 'ExploreSystemData"
  "a966e5115c1090ab6bcb0ea613336a66")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExploreSystemData>)))
  "Returns full string definition for message of type '<ExploreSystemData>"
  (cl:format cl:nil "std_msgs/Header header~%~%string name # Robot's name~%string local_planner # Name of local planner~%~%geometry_msgs/PoseStamped pose # Robot's pose~%TeamActions global_actions # Last global plan~%~%InfoTraj global # Best global path~%InfoTraj local # Best local trajectory~%InfoTraj global_remainder # Local portion of global plan~%InfoTraj optimized # Optimized version of global_remainder or local~%bool optimize_local # If true, the local was optimized, otherwise global_remainder was~%bool select_optimize # If true, optimized was selected over global~%~%float64 optimization_duration # Time to run the SQP~%float64 total_duration # Total time~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: ite_command/TeamActions~%std_msgs/Header header~%string planner_type~%float64 duration # How long to plan (sec)~%~%RobotActions scarab~%RobotActions quad~%~%================================================================================~%MSG: ite_command/RobotActions~%std_msgs/String name~%geometry_msgs/PoseStamped pose # Robot's pose~%InfoPath[] paths~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: ite_command/InfoPath~%geometry_msgs/Pose[] poses~%float64 info # Information of path~%float64 endpose_info # Information at final pose~%float64 time # Time to execute path~%~%================================================================================~%MSG: ite_command/InfoTraj~%ite_trajopt/StatesControls state_controls~%float64 info # Information of path~%float64 cost # Objective function cost~%float64 time # Time to execute trajectory~%float64 info_rate ~%float64 dynfunc_viol~%~%================================================================================~%MSG: ite_trajopt/StatesControls~%std_msgs/Header header~%std_msgs/Float32MultiArray[] X~%std_msgs/Float32MultiArray[] U~%~%================================================================================~%MSG: std_msgs/Float32MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float32[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExploreSystemData)))
  "Returns full string definition for message of type 'ExploreSystemData"
  (cl:format cl:nil "std_msgs/Header header~%~%string name # Robot's name~%string local_planner # Name of local planner~%~%geometry_msgs/PoseStamped pose # Robot's pose~%TeamActions global_actions # Last global plan~%~%InfoTraj global # Best global path~%InfoTraj local # Best local trajectory~%InfoTraj global_remainder # Local portion of global plan~%InfoTraj optimized # Optimized version of global_remainder or local~%bool optimize_local # If true, the local was optimized, otherwise global_remainder was~%bool select_optimize # If true, optimized was selected over global~%~%float64 optimization_duration # Time to run the SQP~%float64 total_duration # Total time~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: ite_command/TeamActions~%std_msgs/Header header~%string planner_type~%float64 duration # How long to plan (sec)~%~%RobotActions scarab~%RobotActions quad~%~%================================================================================~%MSG: ite_command/RobotActions~%std_msgs/String name~%geometry_msgs/PoseStamped pose # Robot's pose~%InfoPath[] paths~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: ite_command/InfoPath~%geometry_msgs/Pose[] poses~%float64 info # Information of path~%float64 endpose_info # Information at final pose~%float64 time # Time to execute path~%~%================================================================================~%MSG: ite_command/InfoTraj~%ite_trajopt/StatesControls state_controls~%float64 info # Information of path~%float64 cost # Objective function cost~%float64 time # Time to execute trajectory~%float64 info_rate ~%float64 dynfunc_viol~%~%================================================================================~%MSG: ite_trajopt/StatesControls~%std_msgs/Header header~%std_msgs/Float32MultiArray[] X~%std_msgs/Float32MultiArray[] U~%~%================================================================================~%MSG: std_msgs/Float32MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float32[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExploreSystemData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'local_planner))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'global_actions))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'global))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'local))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'global_remainder))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'optimized))
     1
     1
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExploreSystemData>))
  "Converts a ROS message object to a list"
  (cl:list 'ExploreSystemData
    (cl:cons ':header (header msg))
    (cl:cons ':name (name msg))
    (cl:cons ':local_planner (local_planner msg))
    (cl:cons ':pose (pose msg))
    (cl:cons ':global_actions (global_actions msg))
    (cl:cons ':global (global msg))
    (cl:cons ':local (local msg))
    (cl:cons ':global_remainder (global_remainder msg))
    (cl:cons ':optimized (optimized msg))
    (cl:cons ':optimize_local (optimize_local msg))
    (cl:cons ':select_optimize (select_optimize msg))
    (cl:cons ':optimization_duration (optimization_duration msg))
    (cl:cons ':total_duration (total_duration msg))
))
