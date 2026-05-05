import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lunabotics/TAMU_SEDS_Lunabotics/install/pico_motor_control'
