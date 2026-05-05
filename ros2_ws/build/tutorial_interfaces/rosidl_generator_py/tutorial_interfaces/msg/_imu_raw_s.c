// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from tutorial_interfaces:msg/IMURaw.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "tutorial_interfaces/msg/detail/imu_raw__struct.h"
#include "tutorial_interfaces/msg/detail/imu_raw__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool tutorial_interfaces__msg__imu_raw__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[40];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("tutorial_interfaces.msg._imu_raw.IMURaw", full_classname_dest, 39) == 0);
  }
  tutorial_interfaces__msg__IMURaw * ros_message = _ros_message;
  {  // accelx
    PyObject * field = PyObject_GetAttrString(_pymsg, "accelx");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->accelx = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // accely
    PyObject * field = PyObject_GetAttrString(_pymsg, "accely");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->accely = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // accelz
    PyObject * field = PyObject_GetAttrString(_pymsg, "accelz");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->accelz = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angvelx
    PyObject * field = PyObject_GetAttrString(_pymsg, "angvelx");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angvelx = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angvely
    PyObject * field = PyObject_GetAttrString(_pymsg, "angvely");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angvely = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angvelz
    PyObject * field = PyObject_GetAttrString(_pymsg, "angvelz");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angvelz = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * tutorial_interfaces__msg__imu_raw__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of IMURaw */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("tutorial_interfaces.msg._imu_raw");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "IMURaw");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  tutorial_interfaces__msg__IMURaw * ros_message = (tutorial_interfaces__msg__IMURaw *)raw_ros_message;
  {  // accelx
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->accelx);
    {
      int rc = PyObject_SetAttrString(_pymessage, "accelx", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // accely
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->accely);
    {
      int rc = PyObject_SetAttrString(_pymessage, "accely", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // accelz
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->accelz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "accelz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angvelx
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angvelx);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angvelx", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angvely
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angvely);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angvely", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angvelz
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angvelz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angvelz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
