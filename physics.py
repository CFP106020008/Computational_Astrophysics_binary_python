import numpy as np
import constants as c

class PhysicsBody:
    
    def __init__(self,initPosx,initPosy,initPosz,
                 initvelx,initvely,initvelz,mass):
        
        self.reset(initPosx,initPosy,initPosz,
                   initvelx,initvely,initvelz,mass)
        return

    def reset(self,posx,posy,posz,velx,vely,velz,mass):
        
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.velx = velx
        self.vely = vely
        self.velz = velz
        self.mass = mass
               
        return

    def force(self, Star_list):
        F = np.zeros(3)
        for i in Star_list:
            if i is self:
                fx1 = 0
                fy1 = 0
                fz1 = 0
            else:
                radius = np.linalg.norm(np.array([(self.posx-i.posx),(self.posy-i.posy),(self.posz-i.posz)]))
                force = -c.G*self.mass*i.mass/radius**2
                fx1 = force*(self.posx-i.posx)/radius
                fy1 = force*(self.posy-i.posy)/radius
                fz1 = force*(self.posz-i.posz)/radius
            F += np.array([fx1,fy1,fz1])

        return F

    def update(self,dt,Star_list):
        x = self.posx
        y = self.posy
        z = self.posz
        velx = self.velx
        vely = self.vely
        velz = self.velz

        fin = np.array([x,y,z,velx,vely,velz])

        def derive(fin):
            dfdt0 = fin[3]
            dfdt1 = fin[4]
            dfdt2 = fin[5]
            dfdt3 = self.force(Star_list)[0]/self.mass
            dfdt4 = self.force(Star_list)[1]/self.mass
            dfdt5 = self.force(Star_list)[2]/self.mass

            dfdt = np.array([dfdt0,dfdt1,dfdt2,dfdt3,dfdt4,dfdt5])
            return dfdt

        fout = self.rk2(dt,fin,derive)
        self.set_info(fout)

        return
        
    def rk2(self,dt,fin,derive):
        k1 = derive(fin) * dt
        fstar = fin+k1
        self.set_info(fstar)
        k2 = derive(fstar) * dt
        fout = fin + 0.5 * (k1 + k2)
        return fout

    def set_info(self,In):
        self.posx = In[0]
        self.posy = In[1]
        self.posz = In[2]
        self.velx = In[3]
        self.vely = In[4]
        self.velz = In[5]
        return

