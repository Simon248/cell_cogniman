

# COGNIMAN CELL DESCRIPTION
 ### **shema is wrong**
![shema drawio de la scene](description.svg)

## Graph architecture
 * All _palpable_ elements (ie position can be learned by robot) are linked to the robot baselink frame. 
 * All of those elements have an origin in a _palpable_ area (ie corner...). This is made by cad design.
 * i didnt make a joint between tool0 and tcp and then from tcp to tool. I used to do that for easy learning and positionning of TCP with robot. I don't know if it's usefull here.. to be discuss, could be done.

## generate urdf
By using this way of doing, it guaranty that urdf is always generated in the same folder hence guaranty his uniqueness.

```
source ros2  
cd src/description/cogniman_scene_description  
chmod +x ./build_urdf.sh  
./build_urdf  
```

## gazebo usage
the package _environment_hooks_package_ provide the hooks.  
Hooks are used in each package where mesh files are by adding in _CMakeList.txt_:  
```
find_package(environment_hooks_package REQUIRED)
ament_environment_hooks("${environment_hooks_package_DIR}/../../../share/environment_hooks_package/hooks/resource_paths.dsv.in")
```

So you need to source to update the 
