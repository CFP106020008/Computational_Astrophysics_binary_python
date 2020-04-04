import numpy as np
import matplotlib.pyplot as plt
import constants as c
from physics import PhysicsBody
import time

T1 = time.time()

#Parameters
dt = 0.01 * c.year
tmax = 10 * c.year
N = 2
Speed = 10
N_frame = tmax/dt

#Storages
D1 = np.ones((int(tmax/dt),6))
D2 = np.ones((int(tmax/dt),6))

#initialize
t = 0

#Functions


#Stars
m1 = 1 * c.Msun
m2 = 2 * c.Msun
r = 1.0 * c.au

Star_list = []

M1 = PhysicsBody(initPosx=0,initPosy=0,initPosz=0,
                 initvely=(c.G*m2/r*m2/(m1+m2))**0.5,
                 initvelx=0,initvelz=0,mass=1*c.Msun)

Star_list.append(M1)

M2 = PhysicsBody(initPosx=1*c.au,initPosy=0,initPosz=0,
                 initvelx=0,initvely=-(c.G*m1/r*m1/(m1+m2))**0.5,
                 initvelz=0,mass=2*c.Msun)

Star_list.append(M2)

#Main Code
for n in range(int(N_frame)):
    for i in Star_list:
        i.update(dt,Star_list)
    D1[n,:6] = np.array([M1.posx,M1.posy,M1.posz,M1.velx,M1.vely,M1.velz])
    D2[n,:6] = np.array([M2.posx,M2.posy,M2.posz,M2.velx,M2.vely,M2.velz])
    t += dt

np.savetxt("M1.dat",D1)
np.savetxt("M2.dat",D2)
T2 = time.time()
print(T2-T1)
