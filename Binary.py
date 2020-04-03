import numpy as np
import matplotlib.pyplot as plt
import constants as c
from physics import PhysicsBody

#Parameters
dt = 0.01 * c.year
tmax = 10 * c.year
N = 2

#Storages
#D = np.ones((N,7))

#initialize
t = 0

#Functions

#Stars
M1 = PhysicsBody(initPosx=0,initPosy=0,initPosz=0,
                 initvelx=0,initvely=0,initvelz=0,mass=1*c.Msun)

M2 = PhysicsBody(initPosx=1*c.au,initPosy=0,initPosz=0,
                 initvelx=0,initvely=3e6,initvelz=0,mass=1*c.Mearth)

Star_list = [M1,M2]

#Main Code
while t<tmax:
    for i in Star_list:
        i.update(dt)
    t += dt

