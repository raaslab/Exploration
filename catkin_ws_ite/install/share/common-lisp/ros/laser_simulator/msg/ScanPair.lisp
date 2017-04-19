; Auto-generated. Do not edit!


(cl:in-package laser_simulator-msg)


;//! \htmlinclude ScanPair.msg.html

(cl:defclass <ScanPair> (roslisp-msg-protocol:ros-message)
  ((scan1
    :reader scan1
    :initarg :scan1
    :type sensor_msgs-msg:LaserScan
    :initform (cl:make-instance 'sensor_msgs-msg:LaserScan))
   (scan2
    :reader scan2
    :initarg :scan2
    :type sensor_msgs-msg:LaserScan
    :initform (cl:make-instance 'sensor_msgs-msg:LaserScan))
   (pose1
    :reader pose1
    :initarg :pose1
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (pose2
    :reader pose2
    :initarg :pose2
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (transform
    :reader transform
    :initarg :transform
    :type geometry_msgs-msg:Transform
    :initform (cl:make-instance 'geometry_msgs-msg:Transform)))
)

(cl:defclass ScanPair (<ScanPair>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ScanPair>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ScanPair)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name laser_simulator-msg:<ScanPair> is deprecated: use laser_simulator-msg:ScanPair instead.")))

(cl:ensure-generic-function 'scan1-val :lambda-list '(m))
(cl:defmethod scan1-val ((m <ScanPair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader laser_simulator-msg:scan1-val is deprecated.  Use laser_simulator-msg:scan1 instead.")
  (scan1 m))

(cl:ensure-generic-function 'scan2-val :lambda-list '(m))
(cl:defmethod scan2-val ((m <ScanPair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader laser_simulator-msg:scan2-val is deprecated.  Use laser_simulator-msg:scan2 instead.")
  (scan2 m))

(cl:ensure-generic-function 'pose1-val :lambda-list '(m))
(cl:defmethod pose1-val ((m <ScanPair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader laser_simulator-msg:pose1-val is deprecated.  Use laser_simulator-msg:pose1 instead.")
  (pose1 m))

(cl:ensure-generic-function 'pose2-val :lambda-list '(m))
(cl:defmethod pose2-val ((m <ScanPair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader laser_simulator-msg:pose2-val is deprecated.  Use laser_simulator-msg:pose2 instead.")
  (pose2 m))

(cl:ensure-generic-function 'transform-val :lambda-list '(m))
(cl:defmethod transform-val ((m <ScanPair>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader laser_simulator-msg:transform-val is deprecated.  Use laser_simulator-msg:transform instead.")
  (transform m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ScanPair>) ostream)
  "Serializes a message object of type '<ScanPair>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'scan1) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'scan2) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose1) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose2) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'transform) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ScanPair>) istream)
  "Deserializes a message object of type '<ScanPair>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'scan1) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'scan2) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose1) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose2) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'transform) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ScanPair>)))
  "Returns string type for a message object of type '<ScanPair>"
  "laser_simulator/ScanPair")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ScanPair)))
  "Returns string type for a message object of type 'ScanPair"
  "laser_simulator/ScanPair")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ScanPair>)))
  "Returns md5sum for a message object of type '<ScanPair>"
  "8b8f9cfc12d41180f8cbbd1515a00b5e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ScanPair)))
  "Returns md5sum for a message object of type 'ScanPair"
  "8b8f9cfc12d41180f8cbbd1515a00b5e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ScanPair>)))
  "Returns full string definition for message of type '<ScanPair>"
  (cl:format cl:nil "sensor_msgs/LaserScan scan1 ~%sensor_msgs/LaserScan scan2~%geometry_msgs/Pose pose1~%geometry_msgs/Pose pose2~%geometry_msgs/Transform transform # Transformation from scan1 to scan2~%~%~%================================================================================~%MSG: sensor_msgs/LaserScan~%# Single scan from a planar laser range-finder~%#~%# If you have another ranging device with different behavior (e.g. a sonar~%# array), please find or create a different message, since applications~%# will make fairly laser-specific assumptions about this data~%~%Header header            # timestamp in the header is the acquisition time of ~%                         # the first ray in the scan.~%                         #~%                         # in frame frame_id, angles are measured around ~%                         # the positive Z axis (counterclockwise, if Z is up)~%                         # with zero angle being forward along the x axis~%                         ~%float32 angle_min        # start angle of the scan [rad]~%float32 angle_max        # end angle of the scan [rad]~%float32 angle_increment  # angular distance between measurements [rad]~%~%float32 time_increment   # time between measurements [seconds] - if your scanner~%                         # is moving, this will be used in interpolating position~%                         # of 3d points~%float32 scan_time        # time between scans [seconds]~%~%float32 range_min        # minimum range value [m]~%float32 range_max        # maximum range value [m]~%~%float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)~%float32[] intensities    # intensity data [device-specific units].  If your~%                         # device does not provide intensities, please leave~%                         # the array empty.~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ScanPair)))
  "Returns full string definition for message of type 'ScanPair"
  (cl:format cl:nil "sensor_msgs/LaserScan scan1 ~%sensor_msgs/LaserScan scan2~%geometry_msgs/Pose pose1~%geometry_msgs/Pose pose2~%geometry_msgs/Transform transform # Transformation from scan1 to scan2~%~%~%================================================================================~%MSG: sensor_msgs/LaserScan~%# Single scan from a planar laser range-finder~%#~%# If you have another ranging device with different behavior (e.g. a sonar~%# array), please find or create a different message, since applications~%# will make fairly laser-specific assumptions about this data~%~%Header header            # timestamp in the header is the acquisition time of ~%                         # the first ray in the scan.~%                         #~%                         # in frame frame_id, angles are measured around ~%                         # the positive Z axis (counterclockwise, if Z is up)~%                         # with zero angle being forward along the x axis~%                         ~%float32 angle_min        # start angle of the scan [rad]~%float32 angle_max        # end angle of the scan [rad]~%float32 angle_increment  # angular distance between measurements [rad]~%~%float32 time_increment   # time between measurements [seconds] - if your scanner~%                         # is moving, this will be used in interpolating position~%                         # of 3d points~%float32 scan_time        # time between scans [seconds]~%~%float32 range_min        # minimum range value [m]~%float32 range_max        # maximum range value [m]~%~%float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)~%float32[] intensities    # intensity data [device-specific units].  If your~%                         # device does not provide intensities, please leave~%                         # the array empty.~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ScanPair>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'scan1))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'scan2))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose1))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose2))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'transform))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ScanPair>))
  "Converts a ROS message object to a list"
  (cl:list 'ScanPair
    (cl:cons ':scan1 (scan1 msg))
    (cl:cons ':scan2 (scan2 msg))
    (cl:cons ':pose1 (pose1 msg))
    (cl:cons ':pose2 (pose2 msg))
    (cl:cons ':transform (transform msg))
))
