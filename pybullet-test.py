import pybullet
import time
import pybullet_data

physcisClient = pybullet.connect(pybullet.GUI)

pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = pybullet.loadURDF("plane.urdf")
robot = pybullet.loadURDF("/franka_description_no_gazebo_specific_tags/robots/fr3/fr3_pybullet.urdf.xml")

print("Press enter to quit")
input()
