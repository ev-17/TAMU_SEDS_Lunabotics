// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/IMURaw.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/imu_raw__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_IMURaw_angvelz
{
public:
  explicit Init_IMURaw_angvelz(::tutorial_interfaces::msg::IMURaw & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::IMURaw angvelz(::tutorial_interfaces::msg::IMURaw::_angvelz_type arg)
  {
    msg_.angvelz = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::IMURaw msg_;
};

class Init_IMURaw_angvely
{
public:
  explicit Init_IMURaw_angvely(::tutorial_interfaces::msg::IMURaw & msg)
  : msg_(msg)
  {}
  Init_IMURaw_angvelz angvely(::tutorial_interfaces::msg::IMURaw::_angvely_type arg)
  {
    msg_.angvely = std::move(arg);
    return Init_IMURaw_angvelz(msg_);
  }

private:
  ::tutorial_interfaces::msg::IMURaw msg_;
};

class Init_IMURaw_angvelx
{
public:
  explicit Init_IMURaw_angvelx(::tutorial_interfaces::msg::IMURaw & msg)
  : msg_(msg)
  {}
  Init_IMURaw_angvely angvelx(::tutorial_interfaces::msg::IMURaw::_angvelx_type arg)
  {
    msg_.angvelx = std::move(arg);
    return Init_IMURaw_angvely(msg_);
  }

private:
  ::tutorial_interfaces::msg::IMURaw msg_;
};

class Init_IMURaw_accelz
{
public:
  explicit Init_IMURaw_accelz(::tutorial_interfaces::msg::IMURaw & msg)
  : msg_(msg)
  {}
  Init_IMURaw_angvelx accelz(::tutorial_interfaces::msg::IMURaw::_accelz_type arg)
  {
    msg_.accelz = std::move(arg);
    return Init_IMURaw_angvelx(msg_);
  }

private:
  ::tutorial_interfaces::msg::IMURaw msg_;
};

class Init_IMURaw_accely
{
public:
  explicit Init_IMURaw_accely(::tutorial_interfaces::msg::IMURaw & msg)
  : msg_(msg)
  {}
  Init_IMURaw_accelz accely(::tutorial_interfaces::msg::IMURaw::_accely_type arg)
  {
    msg_.accely = std::move(arg);
    return Init_IMURaw_accelz(msg_);
  }

private:
  ::tutorial_interfaces::msg::IMURaw msg_;
};

class Init_IMURaw_accelx
{
public:
  Init_IMURaw_accelx()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_IMURaw_accely accelx(::tutorial_interfaces::msg::IMURaw::_accelx_type arg)
  {
    msg_.accelx = std::move(arg);
    return Init_IMURaw_accely(msg_);
  }

private:
  ::tutorial_interfaces::msg::IMURaw msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::IMURaw>()
{
  return tutorial_interfaces::msg::builder::Init_IMURaw_accelx();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__BUILDER_HPP_
