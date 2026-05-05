// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg/IMURaw.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__msg__IMURaw __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__msg__IMURaw __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct IMURaw_
{
  using Type = IMURaw_<ContainerAllocator>;

  explicit IMURaw_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accelx = 0.0;
      this->accely = 0.0;
      this->accelz = 0.0;
      this->angvelx = 0.0;
      this->angvely = 0.0;
      this->angvelz = 0.0;
    }
  }

  explicit IMURaw_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accelx = 0.0;
      this->accely = 0.0;
      this->accelz = 0.0;
      this->angvelx = 0.0;
      this->angvely = 0.0;
      this->angvelz = 0.0;
    }
  }

  // field types and members
  using _accelx_type =
    double;
  _accelx_type accelx;
  using _accely_type =
    double;
  _accely_type accely;
  using _accelz_type =
    double;
  _accelz_type accelz;
  using _angvelx_type =
    double;
  _angvelx_type angvelx;
  using _angvely_type =
    double;
  _angvely_type angvely;
  using _angvelz_type =
    double;
  _angvelz_type angvelz;

  // setters for named parameter idiom
  Type & set__accelx(
    const double & _arg)
  {
    this->accelx = _arg;
    return *this;
  }
  Type & set__accely(
    const double & _arg)
  {
    this->accely = _arg;
    return *this;
  }
  Type & set__accelz(
    const double & _arg)
  {
    this->accelz = _arg;
    return *this;
  }
  Type & set__angvelx(
    const double & _arg)
  {
    this->angvelx = _arg;
    return *this;
  }
  Type & set__angvely(
    const double & _arg)
  {
    this->angvely = _arg;
    return *this;
  }
  Type & set__angvelz(
    const double & _arg)
  {
    this->angvelz = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::msg::IMURaw_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::msg::IMURaw_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::IMURaw_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::IMURaw_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__msg__IMURaw
    std::shared_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__msg__IMURaw
    std::shared_ptr<tutorial_interfaces::msg::IMURaw_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const IMURaw_ & other) const
  {
    if (this->accelx != other.accelx) {
      return false;
    }
    if (this->accely != other.accely) {
      return false;
    }
    if (this->accelz != other.accelz) {
      return false;
    }
    if (this->angvelx != other.angvelx) {
      return false;
    }
    if (this->angvely != other.angvely) {
      return false;
    }
    if (this->angvelz != other.angvelz) {
      return false;
    }
    return true;
  }
  bool operator!=(const IMURaw_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct IMURaw_

// alias to use template instance with default allocator
using IMURaw =
  tutorial_interfaces::msg::IMURaw_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__IMU_RAW__STRUCT_HPP_
