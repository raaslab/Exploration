; Auto-generated. Do not edit!


(cl:in-package ite_grid-msg)


;//! \htmlinclude VoxelGrid.msg.html

(cl:defclass <VoxelGrid> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (origin
    :reader origin
    :initarg :origin
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (num_x
    :reader num_x
    :initarg :num_x
    :type cl:integer
    :initform 0)
   (num_y
    :reader num_y
    :initarg :num_y
    :type cl:integer
    :initform 0)
   (num_z
    :reader num_z
    :initarg :num_z
    :type cl:integer
    :initform 0)
   (resolution
    :reader resolution
    :initarg :resolution
    :type cl:float
    :initform 0.0)
   (probability
    :reader probability
    :initarg :probability
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass VoxelGrid (<VoxelGrid>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VoxelGrid>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VoxelGrid)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ite_grid-msg:<VoxelGrid> is deprecated: use ite_grid-msg:VoxelGrid instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <VoxelGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_grid-msg:header-val is deprecated.  Use ite_grid-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'origin-val :lambda-list '(m))
(cl:defmethod origin-val ((m <VoxelGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_grid-msg:origin-val is deprecated.  Use ite_grid-msg:origin instead.")
  (origin m))

(cl:ensure-generic-function 'num_x-val :lambda-list '(m))
(cl:defmethod num_x-val ((m <VoxelGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_grid-msg:num_x-val is deprecated.  Use ite_grid-msg:num_x instead.")
  (num_x m))

(cl:ensure-generic-function 'num_y-val :lambda-list '(m))
(cl:defmethod num_y-val ((m <VoxelGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_grid-msg:num_y-val is deprecated.  Use ite_grid-msg:num_y instead.")
  (num_y m))

(cl:ensure-generic-function 'num_z-val :lambda-list '(m))
(cl:defmethod num_z-val ((m <VoxelGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_grid-msg:num_z-val is deprecated.  Use ite_grid-msg:num_z instead.")
  (num_z m))

(cl:ensure-generic-function 'resolution-val :lambda-list '(m))
(cl:defmethod resolution-val ((m <VoxelGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_grid-msg:resolution-val is deprecated.  Use ite_grid-msg:resolution instead.")
  (resolution m))

(cl:ensure-generic-function 'probability-val :lambda-list '(m))
(cl:defmethod probability-val ((m <VoxelGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ite_grid-msg:probability-val is deprecated.  Use ite_grid-msg:probability instead.")
  (probability m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VoxelGrid>) ostream)
  "Serializes a message object of type '<VoxelGrid>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'origin) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_z)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_z)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_z)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_z)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'resolution))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'probability))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'probability))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VoxelGrid>) istream)
  "Deserializes a message object of type '<VoxelGrid>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'origin) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_z)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_z)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_z)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_z)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'resolution) (roslisp-utils:decode-single-float-bits bits)))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'probability) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'probability)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VoxelGrid>)))
  "Returns string type for a message object of type '<VoxelGrid>"
  "ite_grid/VoxelGrid")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VoxelGrid)))
  "Returns string type for a message object of type 'VoxelGrid"
  "ite_grid/VoxelGrid")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VoxelGrid>)))
  "Returns md5sum for a message object of type '<VoxelGrid>"
  "ad016ce9327630fcea2105b0338c9d37")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VoxelGrid)))
  "Returns md5sum for a message object of type 'VoxelGrid"
  "ad016ce9327630fcea2105b0338c9d37")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VoxelGrid>)))
  "Returns full string definition for message of type '<VoxelGrid>"
  (cl:format cl:nil "std_msgs/Header header~%geometry_msgs/Point origin~%uint32 num_x~%uint32 num_y~%uint32 num_z~%float32 resolution~%# Subscript (xi, yi, zi) indexes probability[xi + num_x * yi + zi * num_x * num_y] ~%# represents (origin.x + xi * resolution, origin.y + yi * resolution, origin.z + zi * resolution)~%uint8[] probability~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VoxelGrid)))
  "Returns full string definition for message of type 'VoxelGrid"
  (cl:format cl:nil "std_msgs/Header header~%geometry_msgs/Point origin~%uint32 num_x~%uint32 num_y~%uint32 num_z~%float32 resolution~%# Subscript (xi, yi, zi) indexes probability[xi + num_x * yi + zi * num_x * num_y] ~%# represents (origin.x + xi * resolution, origin.y + yi * resolution, origin.z + zi * resolution)~%uint8[] probability~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VoxelGrid>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'origin))
     4
     4
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'probability) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VoxelGrid>))
  "Converts a ROS message object to a list"
  (cl:list 'VoxelGrid
    (cl:cons ':header (header msg))
    (cl:cons ':origin (origin msg))
    (cl:cons ':num_x (num_x msg))
    (cl:cons ':num_y (num_y msg))
    (cl:cons ':num_z (num_z msg))
    (cl:cons ':resolution (resolution msg))
    (cl:cons ':probability (probability msg))
))
