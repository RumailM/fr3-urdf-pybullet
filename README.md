# fr3-urdf-pybullet
This repo contains a modified version of the [franka_description](https://github.com/frankaemika/franka_ros/tree/develop/franka_description) package, producing a .urdf model for the Franka Emika FR3 more suited to basic pybullet simulations. There is a test script showing that it can successfully be imported. Tested with pybullet==3.2.5 on python-3.11.0.

## Modifications

 - Removed gazebo specific-tag generation in franka_arm.xacro
 - Changed default value of hand and gazebo to true. Without the gazebo tag, the .urdf produced does not contain inertial parameters. We always want the end effector.
 - Replaced commands that dynamically look for the franka_description path on the system as referenced during the xacro parsing. Replaced with relative paths from the robots/fr3 folder. This is to ensure that we are using our modified xacro files.

## Usage

    git clone https://github.com/RumailM/fr3-urdf-pybullet
    cd fr3-urdf-pybullet/franka_description_pybullet/robots/fr3
    xacro fr3.urdf.xacro > fr3_pybullet.urdf.xml
We can run the test script to verify that we've generated a compatible .urdf file representing the fr3 robot

    cd ../..
    python pybullet-test.py
    
## Notes 
The original xacro file already a
