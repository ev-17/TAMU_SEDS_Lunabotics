# generated from rosidl_generator_py/resource/_idl.py.em
# with input from tutorial_interfaces:msg/IMURaw.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_IMURaw(type):
    """Metaclass of message 'IMURaw'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('tutorial_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'tutorial_interfaces.msg.IMURaw')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__imu_raw
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__imu_raw
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__imu_raw
            cls._TYPE_SUPPORT = module.type_support_msg__msg__imu_raw
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__imu_raw

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class IMURaw(metaclass=Metaclass_IMURaw):
    """Message class 'IMURaw'."""

    __slots__ = [
        '_accelx',
        '_accely',
        '_accelz',
        '_angvelx',
        '_angvely',
        '_angvelz',
    ]

    _fields_and_field_types = {
        'accelx': 'double',
        'accely': 'double',
        'accelz': 'double',
        'angvelx': 'double',
        'angvely': 'double',
        'angvelz': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accelx = kwargs.get('accelx', float())
        self.accely = kwargs.get('accely', float())
        self.accelz = kwargs.get('accelz', float())
        self.angvelx = kwargs.get('angvelx', float())
        self.angvely = kwargs.get('angvely', float())
        self.angvelz = kwargs.get('angvelz', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.accelx != other.accelx:
            return False
        if self.accely != other.accely:
            return False
        if self.accelz != other.accelz:
            return False
        if self.angvelx != other.angvelx:
            return False
        if self.angvely != other.angvely:
            return False
        if self.angvelz != other.angvelz:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accelx(self):
        """Message field 'accelx'."""
        return self._accelx

    @accelx.setter
    def accelx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'accelx' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'accelx' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._accelx = value

    @builtins.property
    def accely(self):
        """Message field 'accely'."""
        return self._accely

    @accely.setter
    def accely(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'accely' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'accely' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._accely = value

    @builtins.property
    def accelz(self):
        """Message field 'accelz'."""
        return self._accelz

    @accelz.setter
    def accelz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'accelz' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'accelz' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._accelz = value

    @builtins.property
    def angvelx(self):
        """Message field 'angvelx'."""
        return self._angvelx

    @angvelx.setter
    def angvelx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angvelx' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'angvelx' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._angvelx = value

    @builtins.property
    def angvely(self):
        """Message field 'angvely'."""
        return self._angvely

    @angvely.setter
    def angvely(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angvely' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'angvely' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._angvely = value

    @builtins.property
    def angvelz(self):
        """Message field 'angvelz'."""
        return self._angvelz

    @angvelz.setter
    def angvelz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angvelz' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'angvelz' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._angvelz = value
