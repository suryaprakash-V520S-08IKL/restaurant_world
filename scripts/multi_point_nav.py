#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from tf_transformations import quaternion_from_euler
import time

class MultiPointNavigator(Node):
    def __init__(self):
        super().__init__('multi_point_navigator')
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()

        self.locations = {
            'Home': (0.0, 0.0, 0.0),
            'Kitchen': (-2.5, 2.5, 1.57),
            'Buffer Zone': (-1.0, 1.5, 0.0),
            'Table 1': (2.0, 2.5, 0.0),
            'Table 2': (-2.0, -2.5, 0.0)
        }

    def create_pose(self, x, y, yaw):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0
        q = quaternion_from_euler(0, 0, yaw)
        pose.pose.orientation.x = q[0]
        pose.pose.orientation.y = q[1]
        pose.pose.orientation.z = q[2]
        pose.pose.orientation.w = q[3]
        return pose

    def navigate_to(self, location_name, max_attempts=2):
        x, y, yaw = self.locations[location_name]
        pose = self.create_pose(x, y, yaw)

        for attempt in range(max_attempts):
            self.get_logger().info(f"🚀 Navigating to {location_name} (Attempt {attempt+1})...")
            self.navigator.goToPose(pose)

            while not self.navigator.isTaskComplete():
                time.sleep(0.5)

            result = self.navigator.getResult()
            if result == TaskResult.SUCCEEDED:
                self.get_logger().info(f"✅ Successfully reached {location_name}")
                return True
            else:
                self.get_logger().warn(f"⚠️ Failed to reach {location_name}")
                time.sleep(2)

        self.get_logger().error(f"❌ Unable to reach {location_name} after {max_attempts} attempts.")
        return False

    def deliver(self, table_name):
        if self.navigate_to("Kitchen"):
            time.sleep(2)  # Simulate waiting for food
            if self.navigate_to("Buffer Zone"):
                if self.navigate_to(table_name):
                    self.navigate_to("Home")

    def run(self):
        try:
            while rclpy.ok():
                print("\n=== Delivery Menu ===")
                print("1 - Deliver to Table 1")
                print("2 - Deliver to Table 2")
                print("q - Return to Home and Quit")
                choice = input("Enter your choice: ").strip()

                if choice == '1':
                    self.deliver("Table 1")
                elif choice == '2':
                    self.deliver("Table 2")
                elif choice.lower() == 'q':
                    self.get_logger().info("Returning to Home before exit...")
                    self.navigate_to("Home")
                    self.get_logger().info("✅ Delivery session ended. Goodbye!")
                    break
                else:
                    print("❌ Invalid input. Please try again.")
        except KeyboardInterrupt:
            self.get_logger().info("⛔ Keyboard interrupt detected. Returning to Home...")
            self.navigate_to("Home")
            self.get_logger().info("Shutdown complete.")

def main():
    rclpy.init()
    node = MultiPointNavigator()
    node.run()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

