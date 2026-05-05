# TAMU_SEDS_Lunabotics

This repo contains code for interfacing with and controlling the various systems on the rover. This repo contains the following files:

Nodes map and packages

# Package: drive

 Node: auto_drive
 
 command: ros2 run drive auto_drive
 
 Start a publisher for the encoders and a listener for drive command
 
 Topic: /encoder
 
 publish both drive wheel encoder raw ticks values (+) forward (-)negative

 Topic: auto_drive
 
listens to 2 INT32 vales first one for the left motor 2nd for right motor positive values will spin the robot forward negative valeus will reversed

Values expeted from -127 to 127 (-127 max reveserd, 127 max forward , 0 stop)

# Package: sensors 
NODE : imu_raw_pub

command:ros2 run sensors imu_raw

publishes imu raw data to imu_raw topic

# Package:unilidar_sdk2
command ros2 launch unitree_lidar_ros2 launch.py

must be inside the TAMU_SEDS_Lunabotics/ros2_ws/src/unilidar_sdk2/unitree_lidar_ros2

publishes point and imu data

Topics :
- /unilidar/cloud
- /unilidar/imu

