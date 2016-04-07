'''
Created on Apr 5, 2016

@author: Jakub Bernat
'''
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import random
import core.observerlibrary as mo
import core.tools as ctls
import logging 

class Simulation:    
    
    logger = logging.getLogger('Simulation') 
    
    def __init__(self, name, x0_1 = -0.25, x0_2 = -0.25, x0_3 = -0.25):
        self.name = name;
        self.Tp = 0.0001;
        self.Np = 450;
        self.N = 3 # state size
        self.M = 1 # output number
        self.P = 1 # input number
        # motor parameters
        self.R  = 3.2         # Ohm
        self.L  = 0.0086      # mH
        self.Kt = 0.0319      # Nm/A       
        self.fd = 0.00012     # Nms/rad
        self.J  = 30*10.0**-6 # kgm2
        self.mi = -0.06     # Nm/As
        # DC motor 
        self.A = np.matrix(np.zeros((self.N-1,self.N-1)))
        self.A[0,0] = - self.fd/self.J        
        self.A[0,1] =   self.Kt/self.J        
        self.A[1,0] = - self.Kt/self.L        
        self.A[1,1] = -  self.R/self.L        
        self.B = np.matrix(np.zeros((self.N-1,self.N-1)))        
        self.B[0,0] = - 1.0/self.J
        self.B[1,1] =   1.0/self.L
        self.C = np.matrix(np.zeros((1,self.N-1)))
        self.C[0,0] = 0.0
        self.C[0,1] = 1.0 
        # observer definition
        self.Ao = np.matrix(np.zeros((self.N,self.N)))
        self.Ao[0,0] = - self.fd/self.J        
        self.Ao[0,1] =   self.Kt/self.J
        self.Ao[0,2] = -     1.0/self.J
        self.Ao[1,0] = - self.Kt/self.L        
        self.Ao[1,1] = -  self.R/self.L        
        self.Bo = np.matrix(np.zeros((self.N,1)))
        self.Bo[0,0] = 0.0
        self.Bo[1,0] = 1.0/self.L
        self.Bo[2,0] = 0.0
        self.Co = np.matrix(np.zeros((1,self.N)))
        self.Co[0,0] = 0.0
        self.Co[0,1] = 1.0
        self.Co[0,2] = 0.0   
        # observer gain
        self.Lo = np.matrix(np.zeros((self.N,1)))
        self.Lo[2,0] = -self.mi 
        # check closed loop
        self.logger.debug('Ao-LoCo:')
        self.logger.debug(self.Ao-self.Lo*self.Co)
        w, _ = la.eig(self.Ao-self.Lo*self.Co)
        self.logger.debug('Poles of matrix Ao-LoCo:')
        self.logger.debug(w)
                        
def runObserverMulti(s, observerType='RLS', mapping='integral-finite'):

    # time definition
    time = np.linspace(0.0, (s.Np-1)*s.Tp, s.Np)        
    # input signal
    u = np.asmatrix(10.0*np.sign(np.sin(2*np.pi*(1.0/8.0)*time)))
    # DC motor virtual input
    v = np.asmatrix(np.zeros((2,1)))
    # output signal
    y = np.asmatrix(np.zeros((1,s.Np)))    
    # plant state    
    x = np.asmatrix(np.zeros((2,s.Np)))    
    # load torque
    Tload = 0.01*np.asmatrix(np.ones((1,s.Np))) 
    # multi-observer    
    mmObserver = mo.MMObserverLTI(s.N, s.M, s.Tp, s.Ao, s.Bo, s.Co, s.Lo, mapping, observerType, 50.0, 1.0, [100.0, 1.0, 0.02])    
    # estimated state
    xe = np.asmatrix(np.zeros((3,s.Np)))    
    # simulation
    for n in range(s.Np-1):    
        # virtual input - load torque
        v[0,0] = Tload[0,n]
        # virtual input - voltage
        v[1,0] = u[0,n]
        # calculate system state
        x[:,n+1] = x[:,n] + s.Tp*(s.A*x[:,n] + s.B*v)
        y[:,n]   = s.C*x[:,n] + 0.05*(random.random()-0.5)
        # call observer
        xe[:,n] = mmObserver.observe(u[:,n], y[:,n])
    # last iteration
    n = s.Np-1         
    y[:,n]   = s.C*x[:,n] + 0.05*(random.random()-0.5)
    xe[:,n] = mmObserver.observe(u[:,n], y[:,n])
            
    result = dict()
    result['time'] = time
    result['e1'] = xe[0,:]-x[0,:]
    result['e2'] = xe[1,:]-x[1,:]
    result['e3'] = xe[2,:]-Tload
    result['x1'] = x[0,:]
    result['x2'] = x[1,:]
    result['x3'] = Tload    
    result['xe1'] = xe[0,:]
    result['xe2'] = xe[1,:]
    result['xe3'] = xe[2,:]
    result['u'] = u
    return result

ctls.configureLogger()

s = Simulation('Simple example')

# run simulation without second layer (single model)
ra = runObserverMulti(s, 'none')
# run simulation with second layer (multi model)
rMMa = runObserverMulti(s, 'RLS')

time = ra['time']

x1  = ra['x1']
x2  = ra['x2']
x3  = ra['x3']

xe1S = ra['xe1']
xe2S = ra['xe2']
xe3S = ra['xe3']

xe1M = rMMa['xe1']
xe2M = rMMa['xe2']
xe3M = rMMa['xe3']

e1 = ra['e1']
e2 = ra['e2']
e3 = ra['e3']

e1MM = rMMa['e1']
e2MM = rMMa['e2']
e3MM = rMMa['e3']

con = 10000.0
suffix = '.png'

ax = plt.subplot(111)
ax.plot(time, ctls.to_plot_array(x1, con), label='motor speed $\\omega(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(xe1S, con), label='estimated motor speed (SO) $\\hat{\\omega}(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(xe1M, con), label='estimated motor speed (MO) $\\hat{\\omega}(t)$', linewidth=3.0)
plt.xlabel('time $[s]$')
plt.ylabel('motor speed $[rad/s]$')
plt.legend(loc = 4)
plt.savefig('sensorless_speed' + suffix, bbox_inches=0);
plt.clf();

ax = plt.subplot(111)                      
ax.plot(time, ctls.to_plot_array(x2, con), label='motor current $i(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(xe2S, con), label='estimated motor current (SO) $\\hat{i}(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(xe2M, con), label='estimated motor current (MO) $\\hat{i}(t)$', linewidth=3.0)
plt.xlabel('time $[s]$')
plt.ylabel('motor current $[A]$')
plt.legend(loc = 4)
plt.savefig('sensorless_current' + suffix, bbox_inches=0);
plt.clf();

ax = plt.subplot(111)                
ax.plot(time, ctls.to_plot_array(x3, con), label='load torque $T_L(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(xe3S, con), label='estimated load torque (SO) $\\hat{T}_L(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(xe3M, con), label='estimated load torque (MO) $\\hat{T}_L(t)$', linewidth=3.0)
plt.xlabel('time $[s]$')
plt.ylabel('load torque $[Nm]$')
plt.legend(loc = 4)
plt.savefig('sensorless_load_torque' + suffix, bbox_inches=0);
plt.clf();

ax = plt.subplot(111)                      
ax.plot(time, ctls.to_plot_array(e1, con), label='single layer observer $e_1(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(e1MM, con), label='multi layer observer $e_1(t)$', linewidth=3.0)
plt.xlabel('time $[s]$')
plt.ylabel('observation error $e_1$')
plt.savefig('sensorless_e1' + suffix, bbox_inches=0);
plt.clf();

ax = plt.subplot(111)                       
ax.plot(time, ctls.to_plot_array(e2, con), label='single layer observer $e_2(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(e2MM, con), label='multi layer observer $e_2(t)$', linewidth=3.0)
plt.xlabel('time $[s]$')
plt.ylabel('observation error $e_2$')
plt.savefig('sensorless_e2' + suffix, bbox_inches=0);
plt.clf();

ax = plt.subplot(111)                    
ax.plot(time, ctls.to_plot_array(e3, con), label='single layer observer $e_3(t)$', linewidth=3.0)
ax.plot(time, ctls.to_plot_array(e3MM, con), label='multi layer observer $e_3(t)$', linewidth=3.0)
plt.xlabel('time $[s]$')
plt.ylabel('observation error $e_3$')
plt.savefig('sensorless_e3' + suffix, bbox_inches=0);
plt.clf();
