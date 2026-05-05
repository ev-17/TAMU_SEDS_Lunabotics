// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg/IMURaw.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/msg/detail/imu_raw__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace tutorial_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const IMURaw & msg,
  std::ostream & out)
{
  out << "{";
  // member: accelx
  {
    out << "accelx: ";
    rosidl_generator_traits::value_to_yaml(msg.accelx, out);
    out << ", ";
  }

  // member: accely
  {
    out << "accely: ";
    rosidl_generator_traits::value_to_yaml(msg.accely, out);
    out << ", ";
  }

  // member: accelz
  {
    out << "accelz: ";
    rosidl_generator_traits::value_to_yaml(msg.accelz, out);
    out << ", ";
  }

  // member: angvelx
  {
    out << "angvelx: ";
    rosidl_generator_traits::value_to_yaml(msg.angvelx, out);
    out << ", ";
  }

  // member: angvely
  {
    out << "angvely: ";
    rosidl_generator_traits::value_to_yaml(msg.angvely, out);
    out << ", ";
  }

  // member: angvelz
  {
    out << "angvelz: ";
    rosidl_generator_traits::value_to_yaml(msg.angvelz, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const IMURaw & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accelx
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accelx: ";
    rosidl_generator_traits::value_to_yaml(msg.accelx, out);
    out << "\n";
  }

  // member: accely
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accely: ";
    rosidl_generator_traits::value_to_yaml(msg.accely, out);
    out << "\n";
  }

  // member: accelz
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accelz: ";
    rosidl_generator_traits::value_to_yaml(msg.accelz, out);
    out << "\n";
  }

  // member: angvelx
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angvelx: ";
    rosidl_generator_traits::value_to_yaml(msg.angvelx, out);
    out << "\n";
  }

  // member: angvely
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angvely: ";
    rosidl_generator_traits::value_to_yaml(msg.angvely, out);
    out << "\n";
  }

  // member: angvelz
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angvelz: ";
    rosidl_generator_traits::value_to_yaml(msg.angvelz, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IMURaw & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace tutorial_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tutorial_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tutorial_interfaces::msg::IMURaw & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::msg::IMURaw & msg)
{
  return tutorial_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::msg::IMURaw>()
{
  return "tutorial_interfaces::msg::IMURaw";
}

template<>
inline const char * name<tutorial_interfaces::msg::IMURaw>()
{
  return "tutorial_interfaces/msg/IMURaw";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::IMURaw>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::IMURaw>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<tutorial_interfaces::msg::IMURaw>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__TRAITS_HPP_
