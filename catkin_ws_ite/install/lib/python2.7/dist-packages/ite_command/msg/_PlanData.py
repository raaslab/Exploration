# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ite_command/PlanData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ite_command.msg
import geometry_msgs.msg
import std_msgs.msg

class PlanData(genpy.Message):
  _md5sum = "67d65d37a8c6e26d680a2ee5641e5b2f"
  _type = "ite_command/PlanData"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header # Contains plan number and planning start time
string planner_type
float64 duration       # How long to plan (sec)

# Plan parameters used by InfoPlanner
float64 lethal_occ_dist
int64 num_angles
float64 eval_res
float64 min_info
float64 min_ttl_info
float64 max_seg_length
float64 max_seg_angle

float64 min_distance   # Minimum distance used to make trajectories
float64 max_distance   # Maximum distance used to make trajectories

# Trajectories
ite_command/TrajectoryData[] trajectories

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: ite_command/TrajectoryData
geometry_msgs/Pose[] robot_poses
geometry_msgs/Pose[] sensor_poses
float64 total_info
float64[] infos # Information

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','planner_type','duration','lethal_occ_dist','num_angles','eval_res','min_info','min_ttl_info','max_seg_length','max_seg_angle','min_distance','max_distance','trajectories']
  _slot_types = ['std_msgs/Header','string','float64','float64','int64','float64','float64','float64','float64','float64','float64','float64','ite_command/TrajectoryData[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,planner_type,duration,lethal_occ_dist,num_angles,eval_res,min_info,min_ttl_info,max_seg_length,max_seg_angle,min_distance,max_distance,trajectories

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlanData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.planner_type is None:
        self.planner_type = ''
      if self.duration is None:
        self.duration = 0.
      if self.lethal_occ_dist is None:
        self.lethal_occ_dist = 0.
      if self.num_angles is None:
        self.num_angles = 0
      if self.eval_res is None:
        self.eval_res = 0.
      if self.min_info is None:
        self.min_info = 0.
      if self.min_ttl_info is None:
        self.min_ttl_info = 0.
      if self.max_seg_length is None:
        self.max_seg_length = 0.
      if self.max_seg_angle is None:
        self.max_seg_angle = 0.
      if self.min_distance is None:
        self.min_distance = 0.
      if self.max_distance is None:
        self.max_distance = 0.
      if self.trajectories is None:
        self.trajectories = []
    else:
      self.header = std_msgs.msg.Header()
      self.planner_type = ''
      self.duration = 0.
      self.lethal_occ_dist = 0.
      self.num_angles = 0
      self.eval_res = 0.
      self.min_info = 0.
      self.min_ttl_info = 0.
      self.max_seg_length = 0.
      self.max_seg_angle = 0.
      self.min_distance = 0.
      self.max_distance = 0.
      self.trajectories = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.planner_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2dq7d.pack(_x.duration, _x.lethal_occ_dist, _x.num_angles, _x.eval_res, _x.min_info, _x.min_ttl_info, _x.max_seg_length, _x.max_seg_angle, _x.min_distance, _x.max_distance))
      length = len(self.trajectories)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectories:
        length = len(val1.robot_poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.robot_poses:
          _v1 = val2.position
          _x = _v1
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v2 = val2.orientation
          _x = _v2
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.sensor_poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.sensor_poses:
          _v3 = val2.position
          _x = _v3
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v4 = val2.orientation
          _x = _v4
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_d.pack(val1.total_info))
        length = len(val1.infos)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.infos))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.trajectories is None:
        self.trajectories = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_type = str[start:end].decode('utf-8')
      else:
        self.planner_type = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.duration, _x.lethal_occ_dist, _x.num_angles, _x.eval_res, _x.min_info, _x.min_ttl_info, _x.max_seg_length, _x.max_seg_angle, _x.min_distance, _x.max_distance,) = _struct_2dq7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectories = []
      for i in range(0, length):
        val1 = ite_command.msg.TrajectoryData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.robot_poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v5 = val2.position
          _x = _v5
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v6 = val2.orientation
          _x = _v6
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.robot_poses.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.sensor_poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v7 = val2.position
          _x = _v7
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v8 = val2.orientation
          _x = _v8
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.sensor_poses.append(val2)
        start = end
        end += 8
        (val1.total_info,) = _struct_d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.infos = struct.unpack(pattern, str[start:end])
        self.trajectories.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.planner_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2dq7d.pack(_x.duration, _x.lethal_occ_dist, _x.num_angles, _x.eval_res, _x.min_info, _x.min_ttl_info, _x.max_seg_length, _x.max_seg_angle, _x.min_distance, _x.max_distance))
      length = len(self.trajectories)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectories:
        length = len(val1.robot_poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.robot_poses:
          _v9 = val2.position
          _x = _v9
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v10 = val2.orientation
          _x = _v10
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.sensor_poses)
        buff.write(_struct_I.pack(length))
        for val2 in val1.sensor_poses:
          _v11 = val2.position
          _x = _v11
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v12 = val2.orientation
          _x = _v12
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_d.pack(val1.total_info))
        length = len(val1.infos)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.infos.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.trajectories is None:
        self.trajectories = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_type = str[start:end].decode('utf-8')
      else:
        self.planner_type = str[start:end]
      _x = self
      start = end
      end += 80
      (_x.duration, _x.lethal_occ_dist, _x.num_angles, _x.eval_res, _x.min_info, _x.min_ttl_info, _x.max_seg_length, _x.max_seg_angle, _x.min_distance, _x.max_distance,) = _struct_2dq7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectories = []
      for i in range(0, length):
        val1 = ite_command.msg.TrajectoryData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.robot_poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v13 = val2.position
          _x = _v13
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v14 = val2.orientation
          _x = _v14
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.robot_poses.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.sensor_poses = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v15 = val2.position
          _x = _v15
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v16 = val2.orientation
          _x = _v16
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.sensor_poses.append(val2)
        start = end
        end += 8
        (val1.total_info,) = _struct_d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.infos = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        self.trajectories.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d = struct.Struct("<d")
_struct_3I = struct.Struct("<3I")
_struct_3d = struct.Struct("<3d")
_struct_4d = struct.Struct("<4d")
_struct_2dq7d = struct.Struct("<2dq7d")
