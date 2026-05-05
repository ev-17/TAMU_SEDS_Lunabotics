import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


CAMERA_TOPIC = 'camera/image_raw'


# ─── CAMERA SETTINGS ─────────────────────────────────────────────
CAMERA_INDEX  = 0       # USB cam is usually 0, try 1 if not working
FRAME_WIDTH   = 640
FRAME_HEIGHT  = 480
PUBLISH_RATE  = 30.0    # Hz
# ─────────────────────────────────────────────────────────────────


class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')

        self.bridge = CvBridge()

        # publisher
        self.pub = self.create_publisher(Image, CAMERA_TOPIC, 10)

        # open USB camera
        self.cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

        if not self.cap.isOpened():
            self.get_logger().error(
                f"Failed to open camera at index {CAMERA_INDEX}! "
                "Try changing CAMERA_INDEX.")
            return

        # set resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        self.get_logger().info(
            f"Camera opened — publishing to '{CAMERA_TOPIC}' "
            f"at {PUBLISH_RATE}Hz ({FRAME_WIDTH}x{FRAME_HEIGHT})")

        self.create_timer(1.0 / PUBLISH_RATE, self.publish_frame)

    def publish_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warn("Failed to grab frame")
            return

        # convert OpenCV BGR image → ROS2 Image message
        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        msg.header.stamp    = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera'

        self.pub.publish(msg)

    def destroy_node(self):
        self.cap.release()
        self.get_logger().info("Camera released")
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()