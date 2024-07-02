from coppeliasim_zmqremoteapi_client import*
import numpy as np


client = RemoteAPIClient()
sim = client.require('sim')

handle_robo = sim.getObject("/PioneerP3DX")

left_robo =  sim.getObject("/PioneerP3DX/leftMotor")
right_robo =  sim.getObject("/PioneerP3DX/rightMotor")
wr = np.deg2rad(30)
wl = np.deg2rad(30)

vel_left = sim.setJointTargetVelocity(left_robo, wl)
vel_right = sim.setJointTargetVelocity(right_robo, wr)
sim.startSimulation()
while(t:=sim.getSimulationTime()) < 3:
    pos = sim.getObjectPosition(handle_robo, -1)
    orient = sim.getObjectOrientation(handle_robo, -1)
    print(pos)
    print(orient)
sim.stopSimulation()
print(handle_robo)
print(right_robo)
print(left_robo)


