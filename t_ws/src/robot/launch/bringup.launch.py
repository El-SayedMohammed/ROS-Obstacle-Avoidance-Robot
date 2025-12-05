from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    pkg_share = os.path.join(os.path.expanduser('~'), 't_ws', 'src', 'robot')
    urdf_path = os.path.join(pkg_share, 'urdf', 'robot.urdf')
    controllers_yaml = os.path.join(pkg_share, 'config', 'controllers.yaml')

    # start Gazebo Sim (empty world)
    gz = ExecuteProcess(cmd=['gz', 'sim', '-r'], output='screen')

    # start ros2_control_node (controller_manager) with robot_description and controllers yaml
    ros2_control_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[{'robot_description': open(urdf_path).read()}, controllers_yaml],
        output='screen'
    )

    # spawner for joint_state_broadcaster
    spawner_jsb = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
        output='screen'
    )

    # spawner for diff_drive_controller
    spawner_diff = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diff_drive_controller', '--controller-manager', '/controller_manager'],
        output='screen'
    )

    return LaunchDescription([gz, ros2_control_node, spawner_jsb, spawner_diff])

