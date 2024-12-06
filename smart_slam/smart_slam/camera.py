import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image


class CameraNode(Node):

    def __init__(self):
        super().__init__('camera_node')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info('%d' % msg.height)


def main(args=None):
    rclpy.init(args=args)

    camera_node = CameraNode()

    rclpy.spin(camera_node)
    camera_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
