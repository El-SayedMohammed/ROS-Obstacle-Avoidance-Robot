import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    pkg_name = 'robot'  # اسم الـ package بتاعك
    pkg_share = get_package_share_directory(pkg_name)
    urdf_file = os.path.join(pkg_share, 'urdf', 'robot.urdf')
    world_file = os.path.join(pkg_share, 'worlds', 'obstacles_world.sdf')
    
    with open(urdf_file, 'r') as file:
        robot_desc = file.read()
    
    # فتح Gazebo
    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', '-r', world_file],  
        output='screen'
    )
    
    # Robot State Publisher
    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_desc,
            'use_sim_time': True
        }]
    )
    
    # Spawn الروبوت (بيتأخر شوية لحد ما Gazebo يفتح)
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', '/robot_description',
            '-name', 'four_wheel_robot',
            '-z', '0.5'
        ],
        output='screen'
    )
    
    # Bridge بين ROS 2 و Gazebo
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/camera/image_raw@sensor_msgs/msg/Image[gz.msgs.Image',
                '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
        ],
        output='screen'
    )
    
    return LaunchDescription([
        gazebo,
        robot_state_pub,
        spawn_robot,
        bridge
    ])
