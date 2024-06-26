ros2 run xacro xacro $(ros2 pkg prefix cogniman_scene_description)/share/cogniman_scene_description/urdf/cogniman_description.xacro > $(ros2 pkg prefix cogniman_scene_description)/share/cogniman_scene_description/urdf/robot.urdf
cp $(ros2 pkg prefix cogniman_scene_description)/share/cogniman_scene_description/urdf/robot.urdf ./urdf
