import numpy as np

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

    def force(self,):
        fx = 
        fy = 
        fz = 
        return np.array([fx,fy,fz])

    def update(self,dt = 0.01):
        x = self.posx
        y = self.posy
        z = self.posz
        velx = self.velx
        vely = self.vely
        velz = self.velz
        mass = self.mass

        fin = np.array([x,y,z,velx,vely,velz,mass])

        def derive(fin,force):
            dfdt0 = fin[3]
            dfdt1 = fin[4]
            dfdt2 = fin[5]
            dfdt3 = force[0]
            dfdt4 = force[1]
            dfdt5 = force[2]

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

    def rk2(self,dt,fin,derive)
        dfdt = derive(fin)
        fstar = fin + dfdt * dt
        dfdt = derive(fstar)
        fout = fstar + dfdt * dt
        fout = 0.5 * (fin + fout)
        return fout


