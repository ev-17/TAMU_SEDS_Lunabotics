#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to tutorial_interfaces__msg__Num

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Num::default())
  }
}

impl rosidl_runtime_rs::Message for Num {
  type RmwMsg = super::msg::rmw::Num;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        num1: msg.num1,
        num2: msg.num2,
        num3: msg.num3,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      num1: msg.num1,
      num2: msg.num2,
      num3: msg.num3,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      num1: msg.num1,
      num2: msg.num2,
      num3: msg.num3,
    }
  }
}


// Corresponds to tutorial_interfaces__msg__Sphere

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Sphere {

    // This member is not documented.
    #[allow(missing_docs)]
    pub center: geometry_msgs::msg::Point,


    // This member is not documented.
    #[allow(missing_docs)]
    pub radius: f64,

}



impl Default for Sphere {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Sphere::default())
  }
}

impl rosidl_runtime_rs::Message for Sphere {
  type RmwMsg = super::msg::rmw::Sphere;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        center: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Owned(msg.center)).into_owned(),
        radius: msg.radius,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        center: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Borrowed(&msg.center)).into_owned(),
      radius: msg.radius,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      center: geometry_msgs::msg::Point::from_rmw_message(msg.center),
      radius: msg.radius,
    }
  }
}


// Corresponds to tutorial_interfaces__msg__IMURaw

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::IMURaw::default())
  }
}

impl rosidl_runtime_rs::Message for IMURaw {
  type RmwMsg = super::msg::rmw::IMURaw;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        accelx: msg.accelx,
        accely: msg.accely,
        accelz: msg.accelz,
        angvelx: msg.angvelx,
        angvely: msg.angvely,
        angvelz: msg.angvelz,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      accelx: msg.accelx,
      accely: msg.accely,
      accelz: msg.accelz,
      angvelx: msg.angvelx,
      angvely: msg.angvely,
      angvelz: msg.angvelz,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      accelx: msg.accelx,
      accely: msg.accely,
      accelz: msg.accelz,
      angvelx: msg.angvelx,
      angvely: msg.angvely,
      angvelz: msg.angvelz,
    }
  }
}


