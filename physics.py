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

    def force(self):
        F = np.ones(3)
        def force1(self,AO):
            if self is AO:
                fx1 = 0
                fy1 = 0
                fz1 = 0
            else:
                radius = np.linalg.normi(np.array([(AO.posx-self.posx),(AO.posy-self.posy),(AO.posz-self.posz)]))
                force = -c.G*self.mass*AO.mass/radius**2
                fx1 = force*(AO.posx-self.posx)/radius
                fy1 = force*(AO.posy-self.posy)/radius
                fz1 = force*(AO.posz-self.posz)/radius
            return np.array([fx1,fy1,fz1])
        for i in Star_list:
            F += force1(i)

        return F

    def update(self,dt = 0.01):
        x = self.posx
        y = self.posy
        z = self.posz
        velx = self.velx
        vely = self.vely
        velz = self.velz
        mass = self.mass

        fin = np.array([x,y,z,velx,vely,velz,mass])

        def derive(fin):
            dfdt0 = fin[3]
            dfdt1 = fin[4]
            dfdt2 = fin[5]
            dfdt3 = self.force()[0]/self.mass
            dfdt4 = self.force()[1]/self.mass
            dfdt5 = self.force()[2]/self.mass

            dfdt = np.array([dfdt0,dfdt1,dfdt2,dfdt3,dfdt4,dfdt5])
            return dfdt

        fout = self.rk2(dt,fin,derive)
        self.posx = fout[0]
        self.posy = fout[1]
        self.posz = fout[2]
        self.velx = fout[3]
        self.vely = fout[4]
        self.vlez = fout[5]
        
        return
        
    def rk2(self,dt,fin,derive):
        dfdt = derive(fin)
        fstar = fin + dfdt * dt
        dfdt = derive(fstar)
        fout = fstar + dfdt * dt
        fout = 0.5 * (fin + fout)
        return fout

