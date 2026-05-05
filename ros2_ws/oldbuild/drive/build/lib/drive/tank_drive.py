import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import sys
import os

# add roboclaw library to path
sys.path.append('/home/lunabotics/TAMU_SEDS_Lunabotics/roboclaw')
from roboclaw_3 import Roboclaw

ADDRESS = 0x80

class TankDriveNode(Node):
    def __init__(self):
        super().__init__('tank_drive')

        # connect to RoboClaw
        self.rc = Roboclaw("/dev/ttyACM0", 38400)
        if not self.rc.Open():
            self.get_logger().error("Failed to open RoboClaw!")
            return

        self.get_logger().info("RoboClaw connected!")

        # subscribe to joy topic
        self.sub = self.create_subscription(
            Joy, 'joy', self.joy_callback, 10)

    def joy_callback(self, msg: Joy):
        # left stick Y axis  → left motor  (axes[1])
        # right stick Y axis → right motor (axes[3])
        # axes go from -1.0 to 1.0
        left  = msg.axes[1]   # left stick up/down
        right = msg.axes[4]   # right stick up/down

        # convert -1.0→1.0 to -127→127
        left_speed  = int(left  * 127)
        right_speed = int(right * 127)

        self.drive(left_speed, right_speed)

        self.get_logger().info(
            f'L: {left_speed}  R: {right_speed}')

    def drive(self, left: int, right: int):
        # left motor
        if left >= 0:
            self.rc.ForwardM1(ADDRESS, left)
        else:
            self.rc.BackwardM1(ADDRESS, -left)

        # right motor
        if right >= 0:
            self.rc.ForwardM2(ADDRESS, right)
        else:
            self.rc.BackwardM2(ADDRESS, -right)

    def stop(self):
        self.rc.ForwardM1(ADDRESS, 0)
        self.rc.ForwardM2(ADDRESS, 0)

    def destroy_node(self):
        self.stop()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = TankDriveNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.stop()
        node.destroy_node()
        rclpy.shutdown()