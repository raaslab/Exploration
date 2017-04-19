; Auto-generated. Do not edit!


(cl:in-package ite_trajopt-msg)


;//! \htmlinclude StatesControls.msg.html

(cl:defclass <StatesControls> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (X
    :reader X
    :initarg :X
    :type (cl:vector std_msgs-msg:Float32MultiArray)
   :initform (cl:make-array 0 :element-type 'std_msgs-msg:Float32MultiArray :initial-element (cl:make-instance 'std_msgs-msg:Float32MultiArray)))
   (U
    :reader U
    :initarg :U
    :type (cl:vector std_msgs-msg:Float32MultiArray)
   :initform (cl:make-array 0 :element-type 'std_msgs-msg:Float32MultiArray :initial-element (cl:make-instance 'std_msgs-msg:Float32MultiArray))))
)

(cl:defclass StatesControls (<StatesControls>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StatesControls>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StatesControls)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_trajopt-msg:<StatesControls> is deprecated: use ite_trajopt-msg:StatesControls instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <StatesControls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_trajopt-msg:header-val is deprecated.  Use ite_trajopt-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'X-val :lambda-list '(m))
(cl:defmethod X-val ((m <StatesControls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_trajopt-msg:X-val is deprecated.  Use ite_trajopt-msg:X instead.")
  (X m))

(cl:ensure-generic-function 'U-val :lambda-list '(m))
(cl:defmethod U-val ((m <StatesControls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_trajopt-msg:U-val is deprecated.  Use ite_trajopt-msg:U instead.")
  (U m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StatesControls>) ostream)
  "Serializes a message object of type '<StatesControls>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'X))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'X))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'U))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'U))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StatesControls>) istream)
  "Deserializes a message object of type '<StatesControls>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'X) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'X)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'std_msgs-msg:Float32MultiArray))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'U) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'U)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'std_msgs-msg:Float32MultiArray))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StatesControls>)))
  "Returns string type for a message object of type '<StatesControls>"
  "ite_trajopt/StatesControls")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StatesControls)))
  "Returns string type for a message object of type 'StatesControls"
  "ite_trajopt/StatesControls")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StatesControls>)))
  "Returns md5sum for a message object of type '<StatesControls>"
  "406d66282d3640a0cf3e1d5ea7de169a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StatesControls)))
  "Returns md5sum for a message object of type 'StatesControls"
  "406d66282d3640a0cf3e1d5ea7de169a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StatesControls>)))
  "Returns full string definition for message of type '<StatesControls>"
  (cl:format cl:nil "std_msgs/Header header~%std_msgs/Float32MultiArray[] X~%std_msgs/Float32MultiArray[] U~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Float32MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float32[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StatesControls)))
  "Returns full string definition for message of type 'StatesControls"
  (cl:format cl:nil "std_msgs/Header header~%std_msgs/Float32MultiArray[] X~%std_msgs/Float32MultiArray[] U~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Float32MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float32[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StatesControls>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'X) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'U) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StatesControls>))
  "Converts a ROS message object to a list"
  (cl:list 'StatesControls
    (cl:cons ':header (header msg))
    (cl:cons ':X (X msg))
    (cl:cons ':U (U msg))
))
