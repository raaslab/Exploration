// Generated by gencpp from file scarab_msgs/MoveGoal.msg
// DO NOT EDIT!


#ifndef SCARAB_MSGS_MESSAGE_MOVEGOAL_H
#define SCARAB_MSGS_MESSAGE_MOVEGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/PoseStamped.h>

namespace scarab_msgs
{
template <class ContainerAllocator>
struct MoveGoal_
{
  typedef MoveGoal_<ContainerAllocator> Type;

  MoveGoal_()
    : stop(false)
    , target_poses()  {
    }
  MoveGoal_(const ContainerAllocator& _alloc)
    : stop(false)
    , target_poses(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _stop_type;
  _stop_type stop;

   typedef std::vector< ::geometry_msgs::PoseStamped_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::PoseStamped_<ContainerAllocator> >::other >  _target_poses_type;
  _target_poses_type target_poses;




  typedef boost::shared_ptr< ::scarab_msgs::MoveGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::scarab_msgs::MoveGoal_<ContainerAllocator> const> ConstPtr;

}; // struct MoveGoal_

typedef ::scarab_msgs::MoveGoal_<std::allocator<void> > MoveGoal;

typedef boost::shared_ptr< ::scarab_msgs::MoveGoal > MoveGoalPtr;
typedef boost::shared_ptr< ::scarab_msgs::MoveGoal const> MoveGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::scarab_msgs::MoveGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::scarab_msgs::MoveGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace scarab_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'scarab_msgs': ['/home/aravind/catkin_ws_ite/build/devel/share/scarab_msgs/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::scarab_msgs::MoveGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::scarab_msgs::MoveGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::scarab_msgs::MoveGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0fa2c12c260793ee9a0440fc6255c58d";
  }

  static const char* value(const ::scarab_msgs::MoveGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0fa2c12c260793eeULL;
  static const uint64_t static_value2 = 0x9a0440fc6255c58dULL;
};

template<class ContainerAllocator>
struct DataType< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "scarab_msgs/MoveGoal";
  }

  static const char* value(const ::scarab_msgs::MoveGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
bool stop                                 # If true, stop, otherwise go to target\n\
geometry_msgs/PoseStamped[] target_poses  # Target goals\n\
\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
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
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::scarab_msgs::MoveGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stop);
      stream.next(m.target_poses);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::scarab_msgs::MoveGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::scarab_msgs::MoveGoal_<ContainerAllocator>& v)
  {
    s << indent << "stop: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.stop);
    s << indent << "target_poses[]" << std::endl;
    for (size_t i = 0; i < v.target_poses.size(); ++i)
    {
      s << indent << "  target_poses[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::PoseStamped_<ContainerAllocator> >::stream(s, indent + "    ", v.target_poses[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SCARAB_MSGS_MESSAGE_MOVEGOAL_H
