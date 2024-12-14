import rclpy
from rclpy.node import Node

from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
from ultralytics import YOLO

from sensor_msgs.msg import Image
from std_msgs.msg import String, Float64


class CameraNode(Node):

    def __init__(self):
        super().__init__('camera_node')

        self.br = CvBridge()
        self.model = YOLO("yolo11n.pt")

        self.image_raw_subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.img_callback,
            10)

    def img_callback(self, msg):
        img = self.br.imgmsg_to_cv2(msg, desired_encoding="rgb8")
        img = cv2.resize(img, (640, 480),
                         interpolation=cv2.INTER_LINEAR)

        results = next(self.model(img, stream=True, imgsz=(640, 480)))
        self.get_logger().info(f"{results.boxes}")

        if results:
            cv2.imshow("img", results.plot())
        else:
            cv2.imshow("img", img)
        cv2.waitKey(0)


def main(args=None):
    rclpy.init(args=args)

    camera_node = CameraNode()

    rclpy.spin(camera_node)
    camera_node.destroy_node()
    camera_node.get_logger().info("Camera node exiting")

    rclpy.shutdown()


if __name__ == '__main__':
    main()
