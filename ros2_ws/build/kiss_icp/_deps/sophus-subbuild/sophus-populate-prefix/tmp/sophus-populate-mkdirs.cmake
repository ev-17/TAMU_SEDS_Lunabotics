# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-src"
  "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-build"
  "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-subbuild/sophus-populate-prefix"
  "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-subbuild/sophus-populate-prefix/tmp"
  "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-subbuild/sophus-populate-prefix/src/sophus-populate-stamp"
  "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-subbuild/sophus-populate-prefix/src"
  "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-subbuild/sophus-populate-prefix/src/sophus-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-subbuild/sophus-populate-prefix/src/sophus-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/lunabotics/TAMU_SEDS_Lunabotics/ros2_ws/build/kiss_icp/_deps/sophus-subbuild/sophus-populate-prefix/src/sophus-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
