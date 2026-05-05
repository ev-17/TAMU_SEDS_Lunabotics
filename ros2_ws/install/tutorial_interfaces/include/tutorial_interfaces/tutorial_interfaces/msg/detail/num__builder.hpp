// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/Num.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__NUM__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__NUM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/num__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_Num_num3
{
public:
  explicit Init_Num_num3(::tutorial_interfaces::msg::Num & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::Num num3(::tutorial_interfaces::msg::Num::_num3_type arg)
  {
    msg_.num3 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::Num msg_;
};

class Init_Num_num2
{
public:
  explicit Init_Num_num2(::tutorial_interfaces::msg::Num & msg)
  : msg_(msg)
  {}
  Init_Num_num3 num2(::tutorial_interfaces::msg::Num::_num2_type arg)
  {
    msg_.num2 = std::move(arg);
    return Init_Num_num3(msg_);
  }

private:
  ::tutorial_interfaces::msg::Num msg_;
};

class Init_Num_num1
{
public:
  Init_Num_num1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Num_num2 num1(::tutorial_interfaces::msg::Num::_num1_type arg)
  {
    msg_.num1 = std::move(arg);
    return Init_Num_num2(msg_);
  }

private:
  ::tutorial_interfaces::msg::Num msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::Num>()
{
  return tutorial_interfaces::msg::builder::Init_Num_num1();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__NUM__BUILDER_HPP_
