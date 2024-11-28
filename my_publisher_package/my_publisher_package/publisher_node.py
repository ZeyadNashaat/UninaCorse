#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from sysmonitor_interfaces.msg import Sysmon

class SystemDataPublisher(Node):
    def __init__(self):
        super().__init__('publisher_node')
        
        # Publisher for /test topic
        self.publisher_ = self.create_publisher(Float64, '/test', 10)
        
        # Subscriber to system topic, e.g., /system/status
        self.subscription = self.create_subscription(
            Sysmon,  # Change this to the message type of your system topic
            '/system_info',  # Replace with your system topic
            self.listener_callback,
            10
        )
        
        # Add logging to confirm node creation
        self.get_logger().info("System Data Publisher Node started.")
        
    def listener_callback(self):
        # Every time data is received from the system topic, publish a Float64 message on /test
        self.get_logger().info("Received system data")
        
        # Create a Float64 message
        float_msg = Float64()
        
        # Here, you can extract or generate a numeric value based on the system message
        # Example: setting a fixed value (could be replaced with dynamic data)
        float_msg.data = 42.0
        
        # Publish the Float64 message to the /test topic
        self.publisher_.publish(float_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SystemDataPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
