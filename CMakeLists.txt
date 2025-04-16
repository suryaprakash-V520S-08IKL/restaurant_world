cmake_minimum_required(VERSION 3.8)
project(restaurant_world)

# Uncomment the following lines if you need to add additional ROS2 dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/
)

# Install world files
install(DIRECTORY worlds/
  DESTINATION share/${PROJECT_NAME}/
)

# Install scripts (Python files)
install(DIRECTORY scripts/
  DESTINATION share/${PROJECT_NAME}/
)

# ament package will finalize the package setup
ament_package()

