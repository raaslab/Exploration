; Auto-generated. Do not edit!


(cl:in-package mesh80211s-msg)


;//! \htmlinclude MeshStation.msg.html

(cl:defclass <MeshStation> (roslisp-msg-protocol:ros-message)
  ((mac
    :reader mac
    :initarg :mac
    :type cl:string
    :initform "")
   (device
    :reader device
    :initarg :device
    :type cl:string
    :initform "")
   (inactive_time
    :reader inactive_time
    :initarg :inactive_time
    :type cl:integer
    :initform 0)
   (rx_bytes
    :reader rx_bytes
    :initarg :rx_bytes
    :type cl:integer
    :initform 0)
   (rx_packets
    :reader rx_packets
    :initarg :rx_packets
    :type cl:integer
    :initform 0)
   (tx_bytes
    :reader tx_bytes
    :initarg :tx_bytes
    :type cl:integer
    :initform 0)
   (tx_packets
    :reader tx_packets
    :initarg :tx_packets
    :type cl:integer
    :initform 0)
   (signal
    :reader signal
    :initarg :signal
    :type cl:integer
    :initform 0)
   (tx_bitrate
    :reader tx_bitrate
    :initarg :tx_bitrate
    :type cl:fixnum
    :initform 0)
   (llid
    :reader llid
    :initarg :llid
    :type cl:fixnum
    :initform 0)
   (plid
    :reader plid
    :initarg :plid
    :type cl:fixnum
    :initform 0)
   (plink
    :reader plink
    :initarg :plink
    :type cl:string
    :initform ""))
)

(cl:defclass MeshStation (<MeshStation>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MeshStation>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MeshStation)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mesh80211s-msg:<MeshStation> is deprecated: use mesh80211s-msg:MeshStation instead.")))

(cl:ensure-generic-function 'mac-val :lambda-list '(m))
(cl:defmethod mac-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:mac-val is deprecated.  Use mesh80211s-msg:mac instead.")
  (mac m))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:device-val is deprecated.  Use mesh80211s-msg:device instead.")
  (device m))

(cl:ensure-generic-function 'inactive_time-val :lambda-list '(m))
(cl:defmethod inactive_time-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:inactive_time-val is deprecated.  Use mesh80211s-msg:inactive_time instead.")
  (inactive_time m))

(cl:ensure-generic-function 'rx_bytes-val :lambda-list '(m))
(cl:defmethod rx_bytes-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:rx_bytes-val is deprecated.  Use mesh80211s-msg:rx_bytes instead.")
  (rx_bytes m))

(cl:ensure-generic-function 'rx_packets-val :lambda-list '(m))
(cl:defmethod rx_packets-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:rx_packets-val is deprecated.  Use mesh80211s-msg:rx_packets instead.")
  (rx_packets m))

(cl:ensure-generic-function 'tx_bytes-val :lambda-list '(m))
(cl:defmethod tx_bytes-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:tx_bytes-val is deprecated.  Use mesh80211s-msg:tx_bytes instead.")
  (tx_bytes m))

(cl:ensure-generic-function 'tx_packets-val :lambda-list '(m))
(cl:defmethod tx_packets-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:tx_packets-val is deprecated.  Use mesh80211s-msg:tx_packets instead.")
  (tx_packets m))

(cl:ensure-generic-function 'signal-val :lambda-list '(m))
(cl:defmethod signal-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:signal-val is deprecated.  Use mesh80211s-msg:signal instead.")
  (signal m))

(cl:ensure-generic-function 'tx_bitrate-val :lambda-list '(m))
(cl:defmethod tx_bitrate-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:tx_bitrate-val is deprecated.  Use mesh80211s-msg:tx_bitrate instead.")
  (tx_bitrate m))

(cl:ensure-generic-function 'llid-val :lambda-list '(m))
(cl:defmethod llid-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:llid-val is deprecated.  Use mesh80211s-msg:llid instead.")
  (llid m))

(cl:ensure-generic-function 'plid-val :lambda-list '(m))
(cl:defmethod plid-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:plid-val is deprecated.  Use mesh80211s-msg:plid instead.")
  (plid m))

(cl:ensure-generic-function 'plink-val :lambda-list '(m))
(cl:defmethod plink-val ((m <MeshStation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mesh80211s-msg:plink-val is deprecated.  Use mesh80211s-msg:plink instead.")
  (plink m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MeshStation>) ostream)
  "Serializes a message object of type '<MeshStation>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'mac))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'mac))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'inactive_time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'inactive_time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'inactive_time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'inactive_time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'rx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'rx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rx_packets)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rx_packets)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'rx_packets)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'rx_packets)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'tx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'tx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'tx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'tx_bytes)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'tx_packets)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'tx_packets)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'tx_packets)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'tx_packets)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'signal)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'tx_bitrate)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'tx_bitrate)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'llid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'llid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'plid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'plid)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'plink))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'plink))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MeshStation>) istream)
  "Deserializes a message object of type '<MeshStation>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mac) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'mac) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'device) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'device) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'inactive_time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'inactive_time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'inactive_time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'inactive_time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'rx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'rx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rx_packets)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rx_packets)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'rx_packets)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'rx_packets)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'tx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'tx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'tx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'tx_bytes)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'tx_packets)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'tx_packets)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'tx_packets)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'tx_packets)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'signal) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'tx_bitrate)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'tx_bitrate)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'llid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'llid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'plid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'plid)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'plink) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'plink) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MeshStation>)))
  "Returns string type for a message object of type '<MeshStation>"
  "mesh80211s/MeshStation")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MeshStation)))
  "Returns string type for a message object of type 'MeshStation"
  "mesh80211s/MeshStation")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MeshStation>)))
  "Returns md5sum for a message object of type '<MeshStation>"
  "0af11ca5c838b248549e689ebe504453")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MeshStation)))
  "Returns md5sum for a message object of type 'MeshStation"
  "0af11ca5c838b248549e689ebe504453")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MeshStation>)))
  "Returns full string definition for message of type '<MeshStation>"
  (cl:format cl:nil "string mac~%string device~%uint32 inactive_time~%uint32 rx_bytes~%uint32 rx_packets~%uint32 tx_bytes~%uint32 tx_packets~%int32 signal~%uint16 tx_bitrate~%uint16 llid~%uint16 plid~%string plink~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MeshStation)))
  "Returns full string definition for message of type 'MeshStation"
  (cl:format cl:nil "string mac~%string device~%uint32 inactive_time~%uint32 rx_bytes~%uint32 rx_packets~%uint32 tx_bytes~%uint32 tx_packets~%int32 signal~%uint16 tx_bitrate~%uint16 llid~%uint16 plid~%string plink~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MeshStation>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'mac))
     4 (cl:length (cl:slot-value msg 'device))
     4
     4
     4
     4
     4
     4
     2
     2
     2
     4 (cl:length (cl:slot-value msg 'plink))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MeshStation>))
  "Converts a ROS message object to a list"
  (cl:list 'MeshStation
    (cl:cons ':mac (mac msg))
    (cl:cons ':device (device msg))
    (cl:cons ':inactive_time (inactive_time msg))
    (cl:cons ':rx_bytes (rx_bytes msg))
    (cl:cons ':rx_packets (rx_packets msg))
    (cl:cons ':tx_bytes (tx_bytes msg))
    (cl:cons ':tx_packets (tx_packets msg))
    (cl:cons ':signal (signal msg))
    (cl:cons ':tx_bitrate (tx_bitrate msg))
    (cl:cons ':llid (llid msg))
    (cl:cons ':plid (plid msg))
    (cl:cons ':plink (plink msg))
))
