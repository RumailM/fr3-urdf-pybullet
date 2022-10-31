import time

import pybullet
import pybullet_data

physcisClient = pybullet.connect(pybullet.GUI)

pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = pybullet.loadURDF("plane.urdf")
robot = pybullet.loadURDF("/franka_description_pybullet/robots/fr3/fr3_pybullet.urdf")

print("Press enter to quit")
input()
