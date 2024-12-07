# https://github.com/meard/ros2_orb_slam3

import rclpy
from rclpy.node import Node

import time
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

from sensor_msgs.msg import Image
from std_msgs.msg import String, Float64


class CameraNode(Node):

    def __init__(self):
        super().__init__('camera_node')

        self.settings_file_name = "Gazebo"
        self.update_rate = 1/30

        self.send_config = True

        self.img_data = np.array([])
        self.br = CvBridge()
        self.timestep = Float64()

        self.handshake_publisher = self.create_publisher(
            String,
            "/mono_py_driver/experiment_settings",
            10)

        self.handshake_subscriber = self.create_subscription(
            String,
            "/mono_py_driver/exp_settings_ack",
            self.ack_callback,
            10)

        self.image_timestep_publisher = self.create_publisher(
            Float64,
            "/mono_py_driver/timestep_msg",
            10)

        self.image_raw_publisher = self.create_publisher(
            Image,
            "/mono_py_driver/img_msg",
            10)

        self.image_raw_subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.img_callback,
            10)

        self.timer = self.create_timer(self.update_rate, self.timer_callback)

    def img_callback(self, msg):
        self.timestep.data = float(time.time_ns() / 1000)

        # self.get_logger().info(f"Got data: {msg}")
        msg = self.br.imgmsg_to_cv2(msg)
        msg = cv2.resize(msg, (640, 480),
                         interpolation=cv2.INTER_LINEAR)
        self.img_data = cv2.cvtColor(msg, cv2.COLOR_BGR2GRAY)

    def ack_callback(self, msg):
        self.get_logger().info(f"Got ack: {msg.data}")

        if(msg.data == "ACK"):
            self.send_config = False

    def handshake_with_cpp_node(self):
        if self.send_config:
            msg = String()
            msg.data = self.settings_file_name
            self.handshake_publisher.publish(msg)
            time.sleep(0.01)

    def timer_callback(self):
        if self.send_config:
            return
        if self.img_data.size == 0:
            return

        msg = self.br.cv2_to_imgmsg(self.img_data, encoding='passthrough')
        timestep_msg = Float64()
        timestep_msg = self.timestep

        self.get_logger().info("sending messages")

        try:
            self.image_timestep_publisher.publish(timestep_msg)
            self.image_raw_publisher.publish(msg)
        except CvBridgeError as e:
            print(e)


def main(args=None):
    rclpy.init(args=args)

    camera_node = CameraNode()

    while camera_node.send_config:
        camera_node.handshake_with_cpp_node()
        rclpy.spin_once(camera_node)

    rclpy.spin(camera_node)
    camera_node.destroy_node()
    camera_node.get_logger().info("Camera node exiting")
    rclpy.shutdown()


if __name__ == '__main__':
    main()
