// Generated by gencpp from file ite_grid/VoxelGrid.msg
// DO NOT EDIT!


#ifndef ITE_GRID_MESSAGE_VOXELGRID_H
#define ITE_GRID_MESSAGE_VOXELGRID_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Point.h>

namespace ite_grid
{
template <class ContainerAllocator>
struct VoxelGrid_
{
  typedef VoxelGrid_<ContainerAllocator> Type;

  VoxelGrid_()
    : header()
    , origin()
    , num_x(0)
    , num_y(0)
    , num_z(0)
    , resolution(0.0)
    , probability()  {
    }
  VoxelGrid_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , origin(_alloc)
    , num_x(0)
    , num_y(0)
    , num_z(0)
    , resolution(0.0)
    , probability(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _origin_type;
  _origin_type origin;

   typedef uint32_t _num_x_type;
  _num_x_type num_x;

   typedef uint32_t _num_y_type;
  _num_y_type num_y;

   typedef uint32_t _num_z_type;
  _num_z_type num_z;

   typedef float _resolution_type;
  _resolution_type resolution;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _probability_type;
  _probability_type probability;




  typedef boost::shared_ptr< ::ite_grid::VoxelGrid_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ite_grid::VoxelGrid_<ContainerAllocator> const> ConstPtr;

}; // struct VoxelGrid_

typedef ::ite_grid::VoxelGrid_<std::allocator<void> > VoxelGrid;

typedef boost::shared_ptr< ::ite_grid::VoxelGrid > VoxelGridPtr;
typedef boost::shared_ptr< ::ite_grid::VoxelGrid const> VoxelGridConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ite_grid::VoxelGrid_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ite_grid::VoxelGrid_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ite_grid

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'ite_grid': ['/home/aravind/catkin_ws_ite/src/ite_core/ite_grid/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ite_grid::VoxelGrid_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ite_grid::VoxelGrid_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ite_grid::VoxelGrid_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ite_grid::VoxelGrid_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ite_grid::VoxelGrid_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ite_grid::VoxelGrid_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ite_grid::VoxelGrid_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ad016ce9327630fcea2105b0338c9d37";
  }

  static const char* value(const ::ite_grid::VoxelGrid_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xad016ce9327630fcULL;
  static const uint64_t static_value2 = 0xea2105b0338c9d37ULL;
};

template<class ContainerAllocator>
struct DataType< ::ite_grid::VoxelGrid_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ite_grid/VoxelGrid";
  }

  static const char* value(const ::ite_grid::VoxelGrid_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ite_grid::VoxelGrid_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header\n\
geometry_msgs/Point origin\n\
uint32 num_x\n\
uint32 num_y\n\
uint32 num_z\n\
float32 resolution\n\
# Subscript (xi, yi, zi) indexes probability[xi + num_x * yi + zi * num_x * num_y] \n\
# represents (origin.x + xi * resolution, origin.y + yi * resolution, origin.z + zi * resolution)\n\
uint8[] probability\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::ite_grid::VoxelGrid_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ite_grid::VoxelGrid_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.origin);
      stream.next(m.num_x);
      stream.next(m.num_y);
      stream.next(m.num_z);
      stream.next(m.resolution);
      stream.next(m.probability);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VoxelGrid_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ite_grid::VoxelGrid_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ite_grid::VoxelGrid_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "origin: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.origin);
    s << indent << "num_x: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.num_x);
    s << indent << "num_y: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.num_y);
    s << indent << "num_z: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.num_z);
    s << indent << "resolution: ";
    Printer<float>::stream(s, indent + "  ", v.resolution);
    s << indent << "probability[]" << std::endl;
    for (size_t i = 0; i < v.probability.size(); ++i)
    {
      s << indent << "  probability[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.probability[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ITE_GRID_MESSAGE_VOXELGRID_H
