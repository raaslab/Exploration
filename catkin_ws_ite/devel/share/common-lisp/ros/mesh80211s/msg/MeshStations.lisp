; Auto-generated. Do not edit!


(cl:in-package mesh80211s-msg)


;//! \htmlinclude MeshStations.msg.html

(cl:defclass <MeshStations> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (stations
    :reader stations
    :initarg :stations
    :type (cl:vector mesh80211s-msg:MeshStation)
   :initform (cl:make-array 0 :element-type 'mesh80211s-msg:MeshStation :initial-element (cl:make-instance 'mesh80211s-msg:MeshStation))))
)

(cl:defclass MeshStations (<MeshStations>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MeshStations>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MeshStations)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mesh80211s-msg:<MeshStations> is deprecated: use mesh80211s-msg:MeshStations instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <MeshStations>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:header-val is deprecated.  Use mesh80211s-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'stations-val :lambda-list '(m))
(cl:defmethod stations-val ((m <MeshStations>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:stations-val is deprecated.  Use mesh80211s-msg:stations instead.")
  (stations m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MeshStations>) ostream)
  "Serializes a message object of type '<MeshStations>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'stations))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'stations))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MeshStations>) istream)
  "Deserializes a message object of type '<MeshStations>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'stations) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'stations)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'mesh80211s-msg:MeshStation))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MeshStations>)))
  "Returns string type for a message object of type '<MeshStations>"
  "mesh80211s/MeshStations")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MeshStations)))
  "Returns string type for a message object of type 'MeshStations"
  "mesh80211s/MeshStations")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MeshStations>)))
  "Returns md5sum for a message object of type '<MeshStations>"
  "fa4702b9dc887621257c88e89f258184")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MeshStations)))
  "Returns md5sum for a message object of type 'MeshStations"
  "fa4702b9dc887621257c88e89f258184")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MeshStations>)))
  "Returns full string definition for message of type '<MeshStations>"
  (cl:format cl:nil "Header header~%mesh80211s/MeshStation[] stations~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: mesh80211s/MeshStation~%string mac~%string device~%uint32 inactive_time~%uint32 rx_bytes~%uint32 rx_packets~%uint32 tx_bytes~%uint32 tx_packets~%int32 signal~%uint16 tx_bitrate~%uint16 llid~%uint16 plid~%string plink~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MeshStations)))
  "Returns full string definition for message of type 'MeshStations"
  (cl:format cl:nil "Header header~%mesh80211s/MeshStation[] stations~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: mesh80211s/MeshStation~%string mac~%string device~%uint32 inactive_time~%uint32 rx_bytes~%uint32 rx_packets~%uint32 tx_bytes~%uint32 tx_packets~%int32 signal~%uint16 tx_bitrate~%uint16 llid~%uint16 plid~%string plink~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MeshStations>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'stations) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MeshStations>))
  "Converts a ROS message object to a list"
  (cl:list 'MeshStations
    (cl:cons ':header (header msg))
    (cl:cons ':stations (stations msg))
))
