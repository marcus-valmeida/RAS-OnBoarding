from coppeliasim_zmqremoteapi_client import*
import numpy as np


client = RemoteAPIClient()
sim = client.require('sim')

handle_robo = sim.getObject("/Cylinder")

left_robo =  sim.getObject("/Cylinder/Revolute_joint[0]")
right_robo =  sim.getObject("/Cylinder/Revolute_joint[1]")

# inicio da simulaçao
sim.startSimulation()

#dados do robo

# distancia entre as rodas
l = 0.1998

# raio do pneu
r = 0.0425
# velocidade angular e linear
w = np.deg2rad(30)
v = 1

# calculo das velocidades dos motores

wr = ((2 * v) + (w * l)) / (2 * r)
wl = ((2 * v) - (w * l)) / (2 * r)

wr = np.deg2rad(wr)
wl = np.deg2rad(wl)

vel_left = sim.setJointTargetVelocity(left_robo, wl)
vel_right = sim.setJointTargetVelocity(right_robo, wr)

while(t:=sim.getSimulationTime()) < 20:
    pos = sim.getObjectPosition(handle_robo, -1)
    orient = sim.getObjectOrientation(handle_robo, -1)
    print(pos)
    print(orient)

# fim da simulaçao
sim.stopSimulation()

print(handle_robo)
print(right_robo)
print(left_robo)