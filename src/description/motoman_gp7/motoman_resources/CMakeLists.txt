cmake_minimum_required(VERSION 3.8)

project(motoman_resources)

find_package(ament_cmake REQUIRED)

install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)


ament_package()