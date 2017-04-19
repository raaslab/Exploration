; Auto-generated. Do not edit!


(cl:in-package laser_simulator-msg)


;//! \htmlinclude PoseStampedNamedArray.msg.html

(cl:defclass <PoseStampedNamedArray> (roslisp-msg-protocol:ros-message)
  ((poses
    :reader poses
    :initarg :poses
    :type (cl:vector laser_simulator-msg:PoseStampedNamed)
   :initform (cl:make-array 0 :element-type 'laser_simulator-msg:PoseStampedNamed :initial-element (cl:make-instance 'laser_simulator-msg:PoseStampedNamed))))
)

(cl:defclass PoseStampedNamedArray (<PoseStampedNamedArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PoseStampedNamedArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PoseStampedNamedArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name laser_simulator-msg:<PoseStampedNamedArray> is deprecated: use laser_simulator-msg:PoseStampedNamedArray instead.")))

(cl:ensure-generic-function 'poses-val :lambda-list '(m))
(cl:defmethod poses-val ((m <PoseStampedNamedArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader laser_simulator-msg:poses-val is deprecated.  Use laser_simulator-msg:poses instead.")
  (poses m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PoseStampedNamedArray>) ostream)
  "Serializes a message object of type '<PoseStampedNamedArray>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'poses))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'poses))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PoseStampedNamedArray>) istream)
  "Deserializes a message object of type '<PoseStampedNamedArray>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'poses) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'poses)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'laser_simulator-msg:PoseStampedNamed))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PoseStampedNamedArray>)))
  "Returns string type for a message object of type '<PoseStampedNamedArray>"
  "laser_simulator/PoseStampedNamedArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PoseStampedNamedArray)))
  "Returns string type for a message object of type 'PoseStampedNamedArray"
  "laser_simulator/PoseStampedNamedArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PoseStampedNamedArray>)))
  "Returns md5sum for a message object of type '<PoseStampedNamedArray>"
  "3b8df607d1aa74fc669faf952f38163b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PoseStampedNamedArray)))
  "Returns md5sum for a message object of type 'PoseStampedNamedArray"
  "3b8df607d1aa74fc669faf952f38163b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PoseStampedNamedArray>)))
  "Returns full string definition for message of type '<PoseStampedNamedArray>"
  (cl:format cl:nil "laser_simulator/PoseStampedNamed[] poses~%~%================================================================================~%MSG: laser_simulator/PoseStampedNamed~%std_msgs/Header header~%string child_frame_id~%geometry_msgs/Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PoseStampedNamedArray)))
  "Returns full string definition for message of type 'PoseStampedNamedArray"
  (cl:format cl:nil "laser_simulator/PoseStampedNamed[] poses~%~%================================================================================~%MSG: laser_simulator/PoseStampedNamed~%std_msgs/Header header~%string child_frame_id~%geometry_msgs/Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PoseStampedNamedArray>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'poses) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PoseStampedNamedArray>))
  "Converts a ROS message object to a list"
  (cl:list 'PoseStampedNamedArray
    (cl:cons ':poses (poses msg))
))
