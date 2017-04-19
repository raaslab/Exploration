// Generated by gencpp from file roboclaw/motor_state.msg
// DO NOT EDIT!


#ifndef ROBOCLAW_MESSAGE_MOTOR_STATE_H
#define ROBOCLAW_MESSAGE_MOTOR_STATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace roboclaw
{
template <class ContainerAllocator>
struct motor_state_
{
  typedef motor_state_<ContainerAllocator> Type;

  motor_state_()
    : left_duty_sp(0.0)
    , left_duty(0.0)
    , right_duty_sp(0.0)
    , right_duty(0.0)
    , left_qpps_sp(0)
    , left_qpps(0)
    , right_qpps_sp(0)
    , right_qpps(0)
    , left_sp(0.0)
    , left(0.0)
    , right_sp(0.0)
    , right(0.0)
    , v_sp(0.0)
    , v(0.0)
    , w_sp(0.0)
    , w(0.0)
    , left_pid_pe(0.0)
    , left_pid_ie(0.0)
    , left_pid_de(0.0)
    , right_pid_pe(0.0)
    , right_pid_ie(0.0)
    , right_pid_de(0.0)  {
    }
  motor_state_(const ContainerAllocator& _alloc)
    : left_duty_sp(0.0)
    , left_duty(0.0)
    , right_duty_sp(0.0)
    , right_duty(0.0)
    , left_qpps_sp(0)
    , left_qpps(0)
    , right_qpps_sp(0)
    , right_qpps(0)
    , left_sp(0.0)
    , left(0.0)
    , right_sp(0.0)
    , right(0.0)
    , v_sp(0.0)
    , v(0.0)
    , w_sp(0.0)
    , w(0.0)
    , left_pid_pe(0.0)
    , left_pid_ie(0.0)
    , left_pid_de(0.0)
    , right_pid_pe(0.0)
    , right_pid_ie(0.0)
    , right_pid_de(0.0)  {
  (void)_alloc;
    }



   typedef double _left_duty_sp_type;
  _left_duty_sp_type left_duty_sp;

   typedef double _left_duty_type;
  _left_duty_type left_duty;

   typedef double _right_duty_sp_type;
  _right_duty_sp_type right_duty_sp;

   typedef double _right_duty_type;
  _right_duty_type right_duty;

   typedef int32_t _left_qpps_sp_type;
  _left_qpps_sp_type left_qpps_sp;

   typedef int32_t _left_qpps_type;
  _left_qpps_type left_qpps;

   typedef int32_t _right_qpps_sp_type;
  _right_qpps_sp_type right_qpps_sp;

   typedef int32_t _right_qpps_type;
  _right_qpps_type right_qpps;

   typedef double _left_sp_type;
  _left_sp_type left_sp;

   typedef double _left_type;
  _left_type left;

   typedef double _right_sp_type;
  _right_sp_type right_sp;

   typedef double _right_type;
  _right_type right;

   typedef double _v_sp_type;
  _v_sp_type v_sp;

   typedef double _v_type;
  _v_type v;

   typedef double _w_sp_type;
  _w_sp_type w_sp;

   typedef double _w_type;
  _w_type w;

   typedef double _left_pid_pe_type;
  _left_pid_pe_type left_pid_pe;

   typedef double _left_pid_ie_type;
  _left_pid_ie_type left_pid_ie;

   typedef double _left_pid_de_type;
  _left_pid_de_type left_pid_de;

   typedef double _right_pid_pe_type;
  _right_pid_pe_type right_pid_pe;

   typedef double _right_pid_ie_type;
  _right_pid_ie_type right_pid_ie;

   typedef double _right_pid_de_type;
  _right_pid_de_type right_pid_de;




  typedef boost::shared_ptr< ::roboclaw::motor_state_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::roboclaw::motor_state_<ContainerAllocator> const> ConstPtr;

}; // struct motor_state_

typedef ::roboclaw::motor_state_<std::allocator<void> > motor_state;

typedef boost::shared_ptr< ::roboclaw::motor_state > motor_statePtr;
typedef boost::shared_ptr< ::roboclaw::motor_state const> motor_stateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::roboclaw::motor_state_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::roboclaw::motor_state_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace roboclaw

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'roboclaw': ['/home/aravind/catkin_ws_ite/src/scarab/roboclaw/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::roboclaw::motor_state_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::roboclaw::motor_state_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roboclaw::motor_state_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::roboclaw::motor_state_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roboclaw::motor_state_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::roboclaw::motor_state_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::roboclaw::motor_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "10585f422ced85d5c376eb502ea760c3";
  }

  static const char* value(const ::roboclaw::motor_state_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x10585f422ced85d5ULL;
  static const uint64_t static_value2 = 0xc376eb502ea760c3ULL;
};

template<class ContainerAllocator>
struct DataType< ::roboclaw::motor_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "roboclaw/motor_state";
  }

  static const char* value(const ::roboclaw::motor_state_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::roboclaw::motor_state_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 left_duty_sp\n\
float64 left_duty\n\
float64 right_duty_sp\n\
float64 right_duty\n\
int32 left_qpps_sp\n\
int32 left_qpps\n\
int32 right_qpps_sp\n\
int32 right_qpps\n\
float64 left_sp\n\
float64 left\n\
float64 right_sp\n\
float64 right\n\
float64 v_sp\n\
float64 v\n\
float64 w_sp\n\
float64 w\n\
float64 left_pid_pe\n\
float64 left_pid_ie\n\
float64 left_pid_de\n\
float64 right_pid_pe\n\
float64 right_pid_ie\n\
float64 right_pid_de\n\
";
  }

  static const char* value(const ::roboclaw::motor_state_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::roboclaw::motor_state_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.left_duty_sp);
      stream.next(m.left_duty);
      stream.next(m.right_duty_sp);
      stream.next(m.right_duty);
      stream.next(m.left_qpps_sp);
      stream.next(m.left_qpps);
      stream.next(m.right_qpps_sp);
      stream.next(m.right_qpps);
      stream.next(m.left_sp);
      stream.next(m.left);
      stream.next(m.right_sp);
      stream.next(m.right);
      stream.next(m.v_sp);
      stream.next(m.v);
      stream.next(m.w_sp);
      stream.next(m.w);
      stream.next(m.left_pid_pe);
      stream.next(m.left_pid_ie);
      stream.next(m.left_pid_de);
      stream.next(m.right_pid_pe);
      stream.next(m.right_pid_ie);
      stream.next(m.right_pid_de);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct motor_state_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::roboclaw::motor_state_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::roboclaw::motor_state_<ContainerAllocator>& v)
  {
    s << indent << "left_duty_sp: ";
    Printer<double>::stream(s, indent + "  ", v.left_duty_sp);
    s << indent << "left_duty: ";
    Printer<double>::stream(s, indent + "  ", v.left_duty);
    s << indent << "right_duty_sp: ";
    Printer<double>::stream(s, indent + "  ", v.right_duty_sp);
    s << indent << "right_duty: ";
    Printer<double>::stream(s, indent + "  ", v.right_duty);
    s << indent << "left_qpps_sp: ";
    Printer<int32_t>::stream(s, indent + "  ", v.left_qpps_sp);
    s << indent << "left_qpps: ";
    Printer<int32_t>::stream(s, indent + "  ", v.left_qpps);
    s << indent << "right_qpps_sp: ";
    Printer<int32_t>::stream(s, indent + "  ", v.right_qpps_sp);
    s << indent << "right_qpps: ";
    Printer<int32_t>::stream(s, indent + "  ", v.right_qpps);
    s << indent << "left_sp: ";
    Printer<double>::stream(s, indent + "  ", v.left_sp);
    s << indent << "left: ";
    Printer<double>::stream(s, indent + "  ", v.left);
    s << indent << "right_sp: ";
    Printer<double>::stream(s, indent + "  ", v.right_sp);
    s << indent << "right: ";
    Printer<double>::stream(s, indent + "  ", v.right);
    s << indent << "v_sp: ";
    Printer<double>::stream(s, indent + "  ", v.v_sp);
    s << indent << "v: ";
    Printer<double>::stream(s, indent + "  ", v.v);
    s << indent << "w_sp: ";
    Printer<double>::stream(s, indent + "  ", v.w_sp);
    s << indent << "w: ";
    Printer<double>::stream(s, indent + "  ", v.w);
    s << indent << "left_pid_pe: ";
    Printer<double>::stream(s, indent + "  ", v.left_pid_pe);
    s << indent << "left_pid_ie: ";
    Printer<double>::stream(s, indent + "  ", v.left_pid_ie);
    s << indent << "left_pid_de: ";
    Printer<double>::stream(s, indent + "  ", v.left_pid_de);
    s << indent << "right_pid_pe: ";
    Printer<double>::stream(s, indent + "  ", v.right_pid_pe);
    s << indent << "right_pid_ie: ";
    Printer<double>::stream(s, indent + "  ", v.right_pid_ie);
    s << indent << "right_pid_de: ";
    Printer<double>::stream(s, indent + "  ", v.right_pid_de);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOCLAW_MESSAGE_MOTOR_STATE_H
