'''
Created on Apr 5, 2016

@author: Jakub Bernat
'''
import numpy as np
import logging 

class IdentifierRLSMIMO:
    
    logger = logging.getLogger('IdentifierRLSMIMO')
    
    def __init__(self, n, m, p0 = 1000.0, forgetting = 1.0, theta0 = []):
        self.n = n # number of parameters
        self.m = m # number of outputs        
        self.forgetting = forgetting # forgetting factor
        self.theta = np.matrix(np.zeros((self.n,1))) # parameters        
        self.K = np.matrix(np.zeros((self.n,self.m))) # gain
        self.P = p0*np.matrix(np.eye(self.n,self.n)) # gain
        self.In = np.matrix(np.eye(self.n,self.n)) # identity matrix
        self.Im = np.matrix(np.eye(self.m,self.m)) # identity matrix
        self.setInitialTheta(theta0)
        
    def setInitialTheta(self, theta0):
        theta0 = np.squeeze(np.asarray(theta0))
        if self.n == 1:
            self.theta[0] = theta0
        elif len(theta0) == self.n:
            for i in range(self.n):
                self.theta[i] = theta0[i]            
       
    def update(self, y, phi):
        self.error = y - phi*self.theta
        # update gain
        tmp = self.forgetting*self.Im + phi*self.P*phi.T        
        self.K = self.P*phi.T*tmp.I
        # update P
        self.P = ((self.In - self.K*phi)*self.P)/self.forgetting
        # update parameters
        self.theta = self.theta + self.K*self.error
        return self.theta
    
    def output(self, phi):
        return phi*self.theta
    
    def restart(self, p0 = 1000.0):
        self.P = p0*np.matrix(np.eye(self.n,self.n)) # gain 
            