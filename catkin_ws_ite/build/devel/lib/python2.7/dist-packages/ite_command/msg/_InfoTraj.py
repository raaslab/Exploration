# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ite_command/InfoTraj.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import ite_trajopt.msg

class InfoTraj(genpy.Message):
  _md5sum = "bdf81493a6f3c81fb359606599ee9176"
  _type = "ite_command/InfoTraj"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """ite_trajopt/StatesControls state_controls
float64 info # Information of path
float64 cost # Objective function cost
float64 time # Time to execute trajectory
float64 info_rate 
float64 dynfunc_viol

================================================================================
MSG: ite_trajopt/StatesControls
std_msgs/Header header
std_msgs/Float32MultiArray[] X
std_msgs/Float32MultiArray[] U

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
MSG: std_msgs/Float32MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
float32[]         data          # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding elements at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = "height"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = "width"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = "channel"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.

================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
uint32 stride  # stride of given dimension"""
  __slots__ = ['state_controls','info','cost','time','info_rate','dynfunc_viol']
  _slot_types = ['ite_trajopt/StatesControls','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       state_controls,info,cost,time,info_rate,dynfunc_viol

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InfoTraj, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.state_controls is None:
        self.state_controls = ite_trajopt.msg.StatesControls()
      if self.info is None:
        self.info = 0.
      if self.cost is None:
        self.cost = 0.
      if self.time is None:
        self.time = 0.
      if self.info_rate is None:
        self.info_rate = 0.
      if self.dynfunc_viol is None:
        self.dynfunc_viol = 0.
    else:
      self.state_controls = ite_trajopt.msg.StatesControls()
      self.info = 0.
      self.cost = 0.
      self.time = 0.
      self.info_rate = 0.
      self.dynfunc_viol = 0.

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
      buff.write(_struct_3I.pack(_x.state_controls.header.seq, _x.state_controls.header.stamp.secs, _x.state_controls.header.stamp.nsecs))
      _x = self.state_controls.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.state_controls.X)
      buff.write(_struct_I.pack(length))
      for val1 in self.state_controls.X:
        _v1 = val1.layout
        length = len(_v1.dim)
        buff.write(_struct_I.pack(length))
        for val3 in _v1.dim:
          _x = val3.label
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3
          buff.write(_struct_2I.pack(_x.size, _x.stride))
        buff.write(_struct_I.pack(_v1.data_offset))
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.data))
      length = len(self.state_controls.U)
      buff.write(_struct_I.pack(length))
      for val1 in self.state_controls.U:
        _v2 = val1.layout
        length = len(_v2.dim)
        buff.write(_struct_I.pack(length))
        for val3 in _v2.dim:
          _x = val3.label
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3
          buff.write(_struct_2I.pack(_x.size, _x.stride))
        buff.write(_struct_I.pack(_v2.data_offset))
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.data))
      _x = self
      buff.write(_struct_5d.pack(_x.info, _x.cost, _x.time, _x.info_rate, _x.dynfunc_viol))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.state_controls is None:
        self.state_controls = ite_trajopt.msg.StatesControls()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.state_controls.header.seq, _x.state_controls.header.stamp.secs, _x.state_controls.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_controls.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.state_controls.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.state_controls.X = []
      for i in range(0, length):
        val1 = std_msgs.msg.Float32MultiArray()
        _v3 = val1.layout
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v3.dim = []
        for i in range(0, length):
          val3 = std_msgs.msg.MultiArrayDimension()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.label = str[start:end].decode('utf-8')
          else:
            val3.label = str[start:end]
          _x = val3
          start = end
          end += 8
          (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
          _v3.dim.append(val3)
        start = end
        end += 4
        (_v3.data_offset,) = _struct_I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = struct.unpack(pattern, str[start:end])
        self.state_controls.X.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.state_controls.U = []
      for i in range(0, length):
        val1 = std_msgs.msg.Float32MultiArray()
        _v4 = val1.layout
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v4.dim = []
        for i in range(0, length):
          val3 = std_msgs.msg.MultiArrayDimension()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.label = str[start:end].decode('utf-8')
          else:
            val3.label = str[start:end]
          _x = val3
          start = end
          end += 8
          (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
          _v4.dim.append(val3)
        start = end
        end += 4
        (_v4.data_offset,) = _struct_I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = struct.unpack(pattern, str[start:end])
        self.state_controls.U.append(val1)
      _x = self
      start = end
      end += 40
      (_x.info, _x.cost, _x.time, _x.info_rate, _x.dynfunc_viol,) = _struct_5d.unpack(str[start:end])
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
      buff.write(_struct_3I.pack(_x.state_controls.header.seq, _x.state_controls.header.stamp.secs, _x.state_controls.header.stamp.nsecs))
      _x = self.state_controls.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.state_controls.X)
      buff.write(_struct_I.pack(length))
      for val1 in self.state_controls.X:
        _v5 = val1.layout
        length = len(_v5.dim)
        buff.write(_struct_I.pack(length))
        for val3 in _v5.dim:
          _x = val3.label
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3
          buff.write(_struct_2I.pack(_x.size, _x.stride))
        buff.write(_struct_I.pack(_v5.data_offset))
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.data.tostring())
      length = len(self.state_controls.U)
      buff.write(_struct_I.pack(length))
      for val1 in self.state_controls.U:
        _v6 = val1.layout
        length = len(_v6.dim)
        buff.write(_struct_I.pack(length))
        for val3 in _v6.dim:
          _x = val3.label
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          if python3:
            buff.write(struct.pack('<I%sB'%length, length, *_x))
          else:
            buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3
          buff.write(_struct_2I.pack(_x.size, _x.stride))
        buff.write(_struct_I.pack(_v6.data_offset))
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.data.tostring())
      _x = self
      buff.write(_struct_5d.pack(_x.info, _x.cost, _x.time, _x.info_rate, _x.dynfunc_viol))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.state_controls is None:
        self.state_controls = ite_trajopt.msg.StatesControls()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.state_controls.header.seq, _x.state_controls.header.stamp.secs, _x.state_controls.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_controls.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.state_controls.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.state_controls.X = []
      for i in range(0, length):
        val1 = std_msgs.msg.Float32MultiArray()
        _v7 = val1.layout
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v7.dim = []
        for i in range(0, length):
          val3 = std_msgs.msg.MultiArrayDimension()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.label = str[start:end].decode('utf-8')
          else:
            val3.label = str[start:end]
          _x = val3
          start = end
          end += 8
          (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
          _v7.dim.append(val3)
        start = end
        end += 4
        (_v7.data_offset,) = _struct_I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.state_controls.X.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.state_controls.U = []
      for i in range(0, length):
        val1 = std_msgs.msg.Float32MultiArray()
        _v8 = val1.layout
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v8.dim = []
        for i in range(0, length):
          val3 = std_msgs.msg.MultiArrayDimension()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.label = str[start:end].decode('utf-8')
          else:
            val3.label = str[start:end]
          _x = val3
          start = end
          end += 8
          (_x.size, _x.stride,) = _struct_2I.unpack(str[start:end])
          _v8.dim.append(val3)
        start = end
        end += 4
        (_v8.data_offset,) = _struct_I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.state_controls.U.append(val1)
      _x = self
      start = end
      end += 40
      (_x.info, _x.cost, _x.time, _x.info_rate, _x.dynfunc_viol,) = _struct_5d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5d = struct.Struct("<5d")
_struct_3I = struct.Struct("<3I")
_struct_2I = struct.Struct("<2I")
