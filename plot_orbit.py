import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

D1 = np.loadtxt("M1.dat")
D2 = np.loadtxt("M2.dat")
#D3 = np.loadtxt("binary_003.dat")
plt.plot(D1[:,0],D1[:,1])
plt.plot(D2[:,0],D2[:,1])
plt.scatter(D1[-1,0],D1[-1,1])
plt.scatter(D2[-1,0],D2[-1,1])

#plt.plot(D3[:,3],D3[:,4])
#plt.show()
plt.savefig("Orbit.jpg")
