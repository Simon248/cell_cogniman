from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution,PythonExpression
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription, LaunchContext
import xacro
from launch.actions import IncludeLaunchDescription, RegisterEventHandler, DeclareLaunchArgument, LogInfo  
from launch.substitutions import Command
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

robot_model_config_pkg = "cogniman_scene_description"

def evaluate_substitution(context, substitution):
    return substitution.perform(context)

def generate_launch_description():
#========================================== SIM_TIME ===========================================
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    
    simu_arg = DeclareLaunchArgument(
        'simu',
        default_value='true',
        description='Set to "false" to run nodes for the real robot'
    )
    simu = LaunchConfiguration('simu')
    use_sim_time = PythonExpression(["'true'" if simu else "'false'"])

#========================================== ROBOT_DESCRIPTION ===========================================
    context = LaunchContext()
    
    robot_description_path = PathJoinSubstitution(
           [FindPackageShare(robot_model_config_pkg), "urdf", "robot.urdf"])
        
    # robot_description_path = PathJoinSubstitution(
    #        [FindPackageShare(robot_model_config_pkg), config_dir_name, f"{robot_name}_motoros.urdf.xacro"])

    robot_description_config = xacro.process_file(evaluate_substitution(context, robot_description_path))
    robot_description = {"robot_description": robot_description_config.toxml()}

    robot_description_arg = DeclareLaunchArgument(
        'robot_description',
        default_value=robot_description,
        description='Absolute path to robot urdf file'
    )

    log_robot_description_path = LogInfo(msg=LaunchConfiguration('robot_description'))

#========================================== ROBOT_DESCRIPTION_SEMANTIC ===========================================
    srdf_path = PathJoinSubstitution(
        [FindPackageShare(robot_model_config_pkg), "config", "robot.srdf"])

    srdf_config = xacro.process_file(evaluate_substitution(context, srdf_path))
    robot_description_semantic = {"robot_description_semantic": srdf_config.toxml()}

    robot_description_semantic_arg = DeclareLaunchArgument(
        'robot_description_semantic',
        default_value=robot_description_semantic,
        description='Absolute path to robot srdf file'
    )

     # Node to publish the state of the joints
    JSP=Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_gui': True},{"use_sim_time": use_sim_time}],
    )

    # Node to publish the state of the robot to tf
    RSP_freq=DeclareLaunchArgument("publish_frequency", default_value="15.0")

    RSP=Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time},
                    {"robot_description": robot_description_config.toxml()},
                    {"publish_frequency": LaunchConfiguration("publish_frequency")},
                    ],
    )
    
    # Node to launch RViz
    rviz=Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', PathJoinSubstitution([FindPackageShare('bringup'), "config", "config_rviz1.rviz"])],
        parameters=[{"use_sim_time": use_sim_time},{"robot_description": robot_description_config.toxml()},{"robot_description_semantic": srdf_config.toxml()},],
    )

    # # Include Gazebo launch file
    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])]),
    #     launch_arguments={'world': PathJoinSubstitution([FindPackageShare(robot_model_config_pkg), 'worlds', 'empty.world'])}.items(),
    # )

    # Gazebo Sim
    robot_descr_path=get_package_share_directory('cogniman_scene_description')
    scene_path = os.path.join(robot_descr_path, 'urdf', 'gazebo_world.sdf')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': f'-v 4 -r {scene_path}'}.items(),
    )

    # Spawn robot in Gazebo
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', '/robot_description',
            '-entity', 'robot_description'],
        output='screen'
    )

    # Gz bridge
    pkg_bringup_path = get_package_share_directory('bringup')
    DeclareLaunchArgument(
        'config_file_gz_bridge',
        default_value=os.path.join(pkg_bringup_path, 'config','gz_bridge_config.yaml'),
        description='Path to the configuration file'
        )
    
    gz_bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_bringup_path, 'config', 'gz_bridge_config.yaml'),
            'qos_overrides./tf_static.publisher.durability': 'transient_local',
        }],
        output='screen'
    )



    return LaunchDescription([
        RSP_freq,
        robot_description_arg,
        log_robot_description_path,
        # JSP,
        RSP,
        rviz,
        gazebo,
        spawn_robot,
        gz_bridge_node
    ])