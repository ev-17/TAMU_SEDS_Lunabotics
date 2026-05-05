#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "tutorial_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__tutorial_interfaces__msg__Num() -> *const std::ffi::c_void;
}

#[link(name = "tutorial_interfaces__rosidl_generator_c")]
extern "C" {
    fn tutorial_interfaces__msg__Num__init(msg: *mut Num) -> bool;
    fn tutorial_interfaces__msg__Num__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Num>, size: usize) -> bool;
    fn tutorial_interfaces__msg__Num__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Num>);
    fn tutorial_interfaces__msg__Num__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Num>, out_seq: *mut rosidl_runtime_rs::Sequence<Num>) -> bool;
}

// Corresponds to tutorial_interfaces__msg__Num
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Num {

    // This member is not documented.
    #[allow(missing_docs)]
    pub num1: i64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub num2: i64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub num3: i64,

}



impl Default for Num {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !tutorial_interfaces__msg__Num__init(&mut msg as *mut _) {
        panic!("Call to tutorial_interfaces__msg__Num__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Num {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__Num__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__Num__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__Num__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Num {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Num where Self: Sized {
  const TYPE_NAME: &'static str = "tutorial_interfaces/msg/Num";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__tutorial_interfaces__msg__Num() }
  }
}


#[link(name = "tutorial_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__tutorial_interfaces__msg__Sphere() -> *const std::ffi::c_void;
}

#[link(name = "tutorial_interfaces__rosidl_generator_c")]
extern "C" {
    fn tutorial_interfaces__msg__Sphere__init(msg: *mut Sphere) -> bool;
    fn tutorial_interfaces__msg__Sphere__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Sphere>, size: usize) -> bool;
    fn tutorial_interfaces__msg__Sphere__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Sphere>);
    fn tutorial_interfaces__msg__Sphere__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Sphere>, out_seq: *mut rosidl_runtime_rs::Sequence<Sphere>) -> bool;
}

// Corresponds to tutorial_interfaces__msg__Sphere
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sphere {

    // This member is not documented.
    #[allow(missing_docs)]
    pub center: geometry_msgs::msg::rmw::Point,


    // This member is not documented.
    #[allow(missing_docs)]
    pub radius: f64,

}



impl Default for Sphere {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !tutorial_interfaces__msg__Sphere__init(&mut msg as *mut _) {
        panic!("Call to tutorial_interfaces__msg__Sphere__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Sphere {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__Sphere__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__Sphere__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__Sphere__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Sphere {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Sphere where Self: Sized {
  const TYPE_NAME: &'static str = "tutorial_interfaces/msg/Sphere";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__tutorial_interfaces__msg__Sphere() }
  }
}


#[link(name = "tutorial_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__tutorial_interfaces__msg__IMURaw() -> *const std::ffi::c_void;
}

#[link(name = "tutorial_interfaces__rosidl_generator_c")]
extern "C" {
    fn tutorial_interfaces__msg__IMURaw__init(msg: *mut IMURaw) -> bool;
    fn tutorial_interfaces__msg__IMURaw__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<IMURaw>, size: usize) -> bool;
    fn tutorial_interfaces__msg__IMURaw__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<IMURaw>);
    fn tutorial_interfaces__msg__IMURaw__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<IMURaw>, out_seq: *mut rosidl_runtime_rs::Sequence<IMURaw>) -> bool;
}

// Corresponds to tutorial_interfaces__msg__IMURaw
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct IMURaw {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accelx: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub accely: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub accelz: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub angvelx: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub angvely: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub angvelz: f64,

}



impl Default for IMURaw {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !tutorial_interfaces__msg__IMURaw__init(&mut msg as *mut _) {
        panic!("Call to tutorial_interfaces__msg__IMURaw__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for IMURaw {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__IMURaw__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__IMURaw__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { tutorial_interfaces__msg__IMURaw__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for IMURaw {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for IMURaw where Self: Sized {
  const TYPE_NAME: &'static str = "tutorial_interfaces/msg/IMURaw";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__tutorial_interfaces__msg__IMURaw() }
  }
}


