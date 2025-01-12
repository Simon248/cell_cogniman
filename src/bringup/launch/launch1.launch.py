from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution,PythonExpression
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription, LaunchContext
import xacro
from launch.actions import IncludeLaunchDescription, RegisterEventHandler, DeclareLaunchArgument, LogInfo  
from launch.substitutions import Command

robot_model_config_pkg = "cogniman_scene_description"

def evaluate_substitution(context, substitution):
    return substitution.perform(context)

def generate_launch_description():
#========================================== SIM_TIME ===========================================

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

     # Node to publish the state of the joints
    JSP=Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_gui': True}],
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
                    {"publish_frequency": LaunchConfiguration("publish_frequency")},],
    )
    
    # Node to launch RViz
    rviz=Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', PathJoinSubstitution([FindPackageShare('bringup'), "config", "config_rviz1.rviz"])],
    )

    return LaunchDescription([
        RSP_freq,
        robot_description_arg,
        log_robot_description_path,
        JSP,
        RSP,
        rviz,
    ])