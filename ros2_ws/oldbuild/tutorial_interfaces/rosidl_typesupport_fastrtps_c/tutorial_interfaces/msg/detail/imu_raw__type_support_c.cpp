// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from tutorial_interfaces:msg/IMURaw.idl
// generated code does not contain a copyright notice
#include "tutorial_interfaces/msg/detail/imu_raw__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "tutorial_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "tutorial_interfaces/msg/detail/imu_raw__struct.h"
#include "tutorial_interfaces/msg/detail/imu_raw__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _IMURaw__ros_msg_type = tutorial_interfaces__msg__IMURaw;

static bool _IMURaw__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _IMURaw__ros_msg_type * ros_message = static_cast<const _IMURaw__ros_msg_type *>(untyped_ros_message);
  // Field name: accelx
  {
    cdr << ros_message->accelx;
  }

  // Field name: accely
  {
    cdr << ros_message->accely;
  }

  // Field name: accelz
  {
    cdr << ros_message->accelz;
  }

  // Field name: angvelx
  {
    cdr << ros_message->angvelx;
  }

  // Field name: angvely
  {
    cdr << ros_message->angvely;
  }

  // Field name: angvelz
  {
    cdr << ros_message->angvelz;
  }

  return true;
}

static bool _IMURaw__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _IMURaw__ros_msg_type * ros_message = static_cast<_IMURaw__ros_msg_type *>(untyped_ros_message);
  // Field name: accelx
  {
    cdr >> ros_message->accelx;
  }

  // Field name: accely
  {
    cdr >> ros_message->accely;
  }

  // Field name: accelz
  {
    cdr >> ros_message->accelz;
  }

  // Field name: angvelx
  {
    cdr >> ros_message->angvelx;
  }

  // Field name: angvely
  {
    cdr >> ros_message->angvely;
  }

  // Field name: angvelz
  {
    cdr >> ros_message->angvelz;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
size_t get_serialized_size_tutorial_interfaces__msg__IMURaw(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _IMURaw__ros_msg_type * ros_message = static_cast<const _IMURaw__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name accelx
  {
    size_t item_size = sizeof(ros_message->accelx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name accely
  {
    size_t item_size = sizeof(ros_message->accely);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name accelz
  {
    size_t item_size = sizeof(ros_message->accelz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name angvelx
  {
    size_t item_size = sizeof(ros_message->angvelx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name angvely
  {
    size_t item_size = sizeof(ros_message->angvely);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name angvelz
  {
    size_t item_size = sizeof(ros_message->angvelz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _IMURaw__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_tutorial_interfaces__msg__IMURaw(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_tutorial_interfaces
size_t max_serialized_size_tutorial_interfaces__msg__IMURaw(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: accelx
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: accely
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: accelz
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: angvelx
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: angvely
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: angvelz
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = tutorial_interfaces__msg__IMURaw;
    is_plain =
      (
      offsetof(DataType, angvelz) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _IMURaw__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_tutorial_interfaces__msg__IMURaw(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_IMURaw = {
  "tutorial_interfaces::msg",
  "IMURaw",
  _IMURaw__cdr_serialize,
  _IMURaw__cdr_deserialize,
  _IMURaw__get_serialized_size,
  _IMURaw__max_serialized_size
};

static rosidl_message_type_support_t _IMURaw__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_IMURaw,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, tutorial_interfaces, msg, IMURaw)() {
  return &_IMURaw__type_support;
}

#if defined(__cplusplus)
}
#endif
