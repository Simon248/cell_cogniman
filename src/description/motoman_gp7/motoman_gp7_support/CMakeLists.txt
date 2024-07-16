cmake_minimum_required(VERSION 3.8)

project(motoman_gp7_support)

find_package(ament_cmake REQUIRED)
find_package(environment_hooks_package REQUIRED)


install(DIRECTORY  meshes urdf
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY  urdf
  DESTINATION share/${PROJECT_NAME}
)
ament_environment_hooks("${environment_hooks_package_DIR}/../../../share/environment_hooks_package/hooks/resource_paths.dsv.in")

ament_package()
