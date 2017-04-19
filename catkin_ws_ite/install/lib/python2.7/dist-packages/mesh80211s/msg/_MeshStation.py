# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mesh80211s/MeshStation.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MeshStation(genpy.Message):
  _md5sum = "0af11ca5c838b248549e689ebe504453"
  _type = "mesh80211s/MeshStation"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string mac
string device
uint32 inactive_time
uint32 rx_bytes
uint32 rx_packets
uint32 tx_bytes
uint32 tx_packets
int32 signal
uint16 tx_bitrate
uint16 llid
uint16 plid
string plink
"""
  __slots__ = ['mac','device','inactive_time','rx_bytes','rx_packets','tx_bytes','tx_packets','signal','tx_bitrate','llid','plid','plink']
  _slot_types = ['string','string','uint32','uint32','uint32','uint32','uint32','int32','uint16','uint16','uint16','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       mac,device,inactive_time,rx_bytes,rx_packets,tx_bytes,tx_packets,signal,tx_bitrate,llid,plid,plink

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MeshStation, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.mac is None:
        self.mac = ''
      if self.device is None:
        self.device = ''
      if self.inactive_time is None:
        self.inactive_time = 0
      if self.rx_bytes is None:
        self.rx_bytes = 0
      if self.rx_packets is None:
        self.rx_packets = 0
      if self.tx_bytes is None:
        self.tx_bytes = 0
      if self.tx_packets is None:
        self.tx_packets = 0
      if self.signal is None:
        self.signal = 0
      if self.tx_bitrate is None:
        self.tx_bitrate = 0
      if self.llid is None:
        self.llid = 0
      if self.plid is None:
        self.plid = 0
      if self.plink is None:
        self.plink = ''
    else:
      self.mac = ''
      self.device = ''
      self.inactive_time = 0
      self.rx_bytes = 0
      self.rx_packets = 0
      self.tx_bytes = 0
      self.tx_packets = 0
      self.signal = 0
      self.tx_bitrate = 0
      self.llid = 0
      self.plid = 0
      self.plink = ''

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
      _x = self.mac
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.device
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_5Ii3H.pack(_x.inactive_time, _x.rx_bytes, _x.rx_packets, _x.tx_bytes, _x.tx_packets, _x.signal, _x.tx_bitrate, _x.llid, _x.plid))
      _x = self.plink
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mac = str[start:end].decode('utf-8')
      else:
        self.mac = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.device = str[start:end].decode('utf-8')
      else:
        self.device = str[start:end]
      _x = self
      start = end
      end += 30
      (_x.inactive_time, _x.rx_bytes, _x.rx_packets, _x.tx_bytes, _x.tx_packets, _x.signal, _x.tx_bitrate, _x.llid, _x.plid,) = _struct_5Ii3H.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.plink = str[start:end].decode('utf-8')
      else:
        self.plink = str[start:end]
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
      _x = self.mac
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.device
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_5Ii3H.pack(_x.inactive_time, _x.rx_bytes, _x.rx_packets, _x.tx_bytes, _x.tx_packets, _x.signal, _x.tx_bitrate, _x.llid, _x.plid))
      _x = self.plink
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mac = str[start:end].decode('utf-8')
      else:
        self.mac = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.device = str[start:end].decode('utf-8')
      else:
        self.device = str[start:end]
      _x = self
      start = end
      end += 30
      (_x.inactive_time, _x.rx_bytes, _x.rx_packets, _x.tx_bytes, _x.tx_packets, _x.signal, _x.tx_bitrate, _x.llid, _x.plid,) = _struct_5Ii3H.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.plink = str[start:end].decode('utf-8')
      else:
        self.plink = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5Ii3H = struct.Struct("<5Ii3H")
