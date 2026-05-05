import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import serial
import time

class MotorControlNode(Node):

    
    M1_MAX_SPEED  = 0.8   # LB/RB drive motor   (-1.0 to 1.0)
    M2_MAX_SPEED  = 0.8   # Y/A button motor     (-1.0 to 1.0)
    M3_MAX_SPEED  = 0.8   # X/B button motor     (-1.0 to 1.0)
   

    # Xbox controller button indices
    BUTTON_LB     = 4
    BUTTON_RB     = 5
    BUTTON_Y      = 3     # M2 forward
    BUTTON_A      = 0     # M2 backward
    BUTTON_X      = 2     # M3 backward
    BUTTON_B      = 1     # M3 forward

    def __init__(self):
        super().__init__('motor_control')

        # Find Pico serial port
        self.pico_port = self.find_pico()
        self.ser = serial.Serial(self.pico_port, 115200, timeout=1)
        time.sleep(2)  # wait for Pico to arm
        self.get_logger().info(f'Connected to Pico on {self.pico_port}')

        # Subscribe to joystick
        self.sub = self.create_subscription(Joy, '/joy', self.joy_callback, 10)

        self.get_logger().info('Motor control node started!')
        self.get_logger().info(f'M1 max speed: {self.M1_MAX_SPEED}')
        self.get_logger().info(f'M2 max speed: {self.M2_MAX_SPEED}')
        self.get_logger().info(f'M3 max speed: {self.M3_MAX_SPEED}')

    def find_pico(self):
        """Auto-detect Pico serial port"""
        import glob
        ports = glob.glob('/dev/ttyACM*') + glob.glob('/dev/ttyUSB*')
        if ports:
            return ports[0]
        raise RuntimeError('Pico not found! Check USB connection.')

    def send_motor(self, motor, speed):
        """Send command to Pico"""
        cmd = f'{motor}:{speed:.3f}\n'
        try:
            self.ser.write(cmd.encode())
        except Exception as e:
            self.get_logger().error(f'Serial error: {e}')

    def joy_callback(self, msg):
        buttons = msg.buttons

        def btn(index):
            return bool(buttons[index]) if len(buttons) > index else False

        #Motor 1: LB/RB drive 
        lb = btn(self.BUTTON_LB)
        rb = btn(self.BUTTON_RB)

        if lb and rb:
            m1_speed = 0.0
        elif lb:
            m1_speed = -self.M1_MAX_SPEED   # reverse
        elif rb:
            m1_speed =  self.M1_MAX_SPEED   # forward
        else:
            m1_speed = 0.0

        self.send_motor('M1', m1_speed)

        # Motor 2: Y = forward, A = backward 
        y = btn(self.BUTTON_Y)
        a = btn(self.BUTTON_A)

        if y and not a:
            m2_speed =  self.M2_MAX_SPEED
        elif a and not y:
            m2_speed = -self.M2_MAX_SPEED
        else:
            m2_speed = 0.0

        self.send_motor('M2', m2_speed)

        # Motor 3: B = forward, X = backward 
        x = btn(self.BUTTON_X)
        b = btn(self.BUTTON_B)

        if b and not x:
            m3_speed =  self.M3_MAX_SPEED
        elif x and not b:
            m3_speed = -self.M3_MAX_SPEED
        else:
            m3_speed = 0.0

        self.send_motor('M3', m3_speed)

    def destroy_node(self):
        """Stop all motors on shutdown"""
        self.get_logger().info('Shutting down — stopping all motors')
        self.send_motor('ALL', 0.0)
        self.ser.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = MotorControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
