import numpy as np
import matplotlib.pyplot as plt

PixelX = 100
PixelY = 100

Msun = 2e33
G = 6.67e-8
m1 = 1*Msun
m2 = 2*Msun

m1x = 50
m2x = 50
m1y = 30
m2y = 60

P = np.zeros((PixelX,PixelY))
for i in range(PixelX):
    for j in range(PixelY):
        if i==m1x and j==m1y:
            P[i,j]=0
        elif i==m2x and j==m2y:
            P[i,j]=0
        else: 
            P[i,j] = G*m1/((i-m1x)**2 + (j-m1y)**2)**0.5 + G*m2/((i-m2x)**2 + (j-m2y)**2)**0.5

plt.imshow(np.log10(P),cmap='jet')
plt.colorbar()
plt.contour(np.log10(P),levels=np.array([25.1,25.2,25.3,25.4,25.5]))
plt.savefig("Potential.png",dpi=300)
#plt.show()
