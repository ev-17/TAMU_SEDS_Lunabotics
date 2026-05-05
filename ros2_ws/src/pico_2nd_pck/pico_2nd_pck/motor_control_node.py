import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import serial
import time
import glob

class MotorControlNode(Node):
    M1_MAX_SPEED = 0.2
    M2_MAX_SPEED = 0.2
    M3_MAX_SPEED = 0.2

    BUTTON_LB = 4
    BUTTON_RB = 5
    BUTTON_Y  = 3
    BUTTON_A  = 0
    BUTTON_X  = 2
    BUTTON_B  = 1

    JOY_TIMEOUT   = 0.3   # seconds without a Joy msg → stop motors
    HEARTBEAT_HZ  = 20    # how often to re-send current state

    def __init__(self):
        super().__init__('motor_control')

        self.pico_port = self.find_pico()
        self.ser = serial.Serial(self.pico_port, 115200, timeout=1)
        time.sleep(2)

        # Current desired speeds
        self.speeds = {'M1': 0.0, 'M2': 0.0, 'M3': 0.0}
        self.last_joy_time = self.get_clock().now()

        self.sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)

        # Heartbeat: re-sends speeds and enforces timeout
        period = 1.0 / self.HEARTBEAT_HZ
        self.timer = self.create_timer(period, self.heartbeat)

        self.get_logger().info(f'Connected to Pico on {self.pico_port}')
        self.get_logger().info('Motor control node started!')

    def find_pico(self):
        ports = glob.glob('/dev/ttyACM0')
        if ports:
            return ports[0]
        raise RuntimeError('Pico not found! Check USB connection.')

    def send_motor(self, motor, speed):
        cmd = f'{motor}:{speed:.3f}\n'
        try:
            self.ser.write(cmd.encode())
        except Exception as e:
            self.get_logger().error(f'Serial error: {e}')

    def heartbeat(self):
        """Re-send current speeds; zero out if Joy has gone silent."""
        now = self.get_clock().now()
        elapsed = (now - self.last_joy_time).nanoseconds / 1e9

        if elapsed > self.JOY_TIMEOUT:
            # Joystick went silent — safety stop
            for key in self.speeds:
                self.speeds[key] = 0.0

        for motor, speed in self.speeds.items():
            self.send_motor(motor, speed)

    def joy_callback(self, msg):
        self.last_joy_time = self.get_clock().now()   # ← reset watchdog

        buttons = msg.buttons
        def btn(i):
            return bool(buttons[i]) if len(buttons) > i else False

        lb, rb = btn(self.BUTTON_LB), btn(self.BUTTON_RB)
        if lb and rb:       self.speeds['M1'] = 0.0
        elif lb:            self.speeds['M1'] = -self.M1_MAX_SPEED
        elif rb:            self.speeds['M1'] =  self.M1_MAX_SPEED
        else:               self.speeds['M1'] = 0.0

        y, a = btn(self.BUTTON_Y), btn(self.BUTTON_A)
        if   y and not a:   self.speeds['M2'] =  self.M2_MAX_SPEED
        elif a and not y:   self.speeds['M2'] = -self.M2_MAX_SPEED
        else:               self.speeds['M2'] = 0.0

        b, x = btn(self.BUTTON_B), btn(self.BUTTON_X)
        if   b and not x:   self.speeds['M3'] =  self.M3_MAX_SPEED
        elif x and not b:   self.speeds['M3'] = -self.M3_MAX_SPEED
        else:               self.speeds['M3'] = 0.0

    def destroy_node(self):
        self.get_logger().info('Shutting down — stopping all motors')
        for motor in self.speeds:
            self.send_motor(motor, 0.0)
        self.ser.close()
        super().destroy_node()

def main(args=None):
    print("test")
    rclpy.init(args=args)
    node = MotorControlNode()
    print("test")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
