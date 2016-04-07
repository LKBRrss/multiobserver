'''
Created on Apr 5, 2016

@author: Jakub Bernat
'''
import numpy as np
import core.tools as ctls
import core.identificationlibrary as idy

class MMObserverLTI:
    '''
        Multi Observer for linear time invariant system
    '''
    
    def __init__(self, N, M, Tp, A, B, C, L, mapping = 'integral-finite', observerType = 'RLS', RLSGain = 1000.0, RLSForgetting = 1.0, xe0 = []):
        # time sample
        self.Tp = Tp
        # number of estimated state variables
        self.N = N
        # number of estimated output variables
        self.M = M
        # number of multi observers
        self.MM = self.N + 1
        # observer matrixes
        self.A = A
        self.B = B
        self.C = C
        self.L = L
        # type of mapping between output and xi
        self.mapping = mapping
        # method of update of alpha weights 
        self.observerType = observerType
        # size of memory
        if self.mapping == 'integral-finite':
            self.finiteMemoryDelay = 10
        # estimated state for m-observer
        self.xemCurr = []
        self.xemNext = []
        # estimated output for m-observer
        self.yem = np.asmatrix(np.zeros((self.M,1)))
        # xi signal for m-observer
        self.ksim = []
        if self.mapping == 'integral-finite':
            # memory for xi signal for m-observer
            self.memory = []   
        # initialized signals with zeros for m-observers     
        for _ in range(self.MM):
            self.xemCurr.append(np.asmatrix(np.zeros((self.N,1))))
            self.xemNext.append(np.asmatrix(np.zeros((self.N,1))))
            self.ksim.append(np.asmatrix(np.zeros((self.N,1))))
            if mapping == 'integral-finite':                        
                self.memory.append(np.asmatrix(np.zeros((self.N,self.finiteMemoryDelay))))        
        self.__integralChainInitialization()
        # initial points for m-observers
        self.xe0 = xe0 
        self.__setXemPoints(self.xe0)                                                                 
        # weights for m-observers
        self.alfa = np.asmatrix((1.0/self.MM)*np.ones((self.MM,1)))
        if self.observerType == 'RLS':      
            self.idyRLS = idy.IdentifierRLSMIMO(self.MM-1,self.MM-1, RLSGain, RLSForgetting, self.alfa[0:self.MM-1,0])

    def __integralChainInitialization(self):
        # integral of output error for m-observer
        Nz = self.M*(self.N-1)
        Nones = self.M*(self.N-2)
        self.Az = np.asmatrix(np.diagflat(np.ones(Nones), self.M))
        self.Bz = np.asmatrix(np.zeros((Nz,self.M)))
        self.Bz[Nones:Nz,:] = np.asmatrix(np.diagflat(self.M))
        self.__createMatrixT()
        self.izmCurr = []
        self.izmNext = []        
        for _ in range(self.MM):
            self.izmCurr.append(np.asmatrix(np.zeros((Nz,1))))
            self.izmNext.append(np.asmatrix(np.zeros((Nz,1))))

    def __createMatrixT(self):
        NM = self.N*self.M
        self.T = np.asmatrix(np.zeros((NM, NM)))
        for j in range(NM):
            for k in range(NM):
                js = j*self.M
                je = (j+1)*self.M
                ks = k*self.M
                ke = (k+1)*self.M                
                if j == k:                    
                    self.T[js:je,ks:ke] = np.eye(self.M)
                elif j > k:
                    p = j - k
                    self.T[js:je,ks:ke] = self.C*(self.A**(p-1))*self.L

    def __setXemPoints(self, xe0):
        # initial points for m-observers 
        if len(xe0) == 0:
            # default vectors for 3D: [1 0 0]^T, [0 1 0]^T, [0 0 1]^T  [0 0 0]^T
            for m in range(self.MM-1):
                self.xemNext[m][m,0] = 1.0
        else:
            # user defined (initial condition multiplied by 1.0/alfa_k)
            for m in range(self.MM-1):
                self.xemNext[m][m,0] = self.MM*xe0[m]
            
    def __singleObserver(self, m, u, etam):
        # derivative of estimated state                             
        dxem = self.A*self.xemCurr[m][:,0] + self.B*u - self.L*(etam[:,0])        
        # estimated state
        self.xemNext[m][:,0] = self.xemCurr[m][:,0] + self.Tp*dxem
                        
    def __calculateMapping(self, m, etam):
        # mapping between output and xi for m-observer
        tmp = np.asmatrix(np.zeros((self.N*self.M,1)))
        tmp[0:(self.N-1)*self.M,0] = self.izmCurr[m][:,0]
        tmp[(self.N-1)*self.M:self.N*self.M] = etam[:,0]
        self.ksim[m][:,0] = self.T*tmp                
        if self.mapping == 'integral-finite':
            # calculate integral of xi between from t-td to t
            ksimd = ctls.delay(self.ksim[m][:,0], self.memory[m], self.finiteMemoryDelay)
            self.ksim[m][:,0] = self.ksim[m][:,0] - ksimd

    def __weightsRLS(self):
        # left side of regressor equation
        idyY = -self.ksim[self.MM-1][:,0]
        # right side of regressor equation 
        M = np.matrix(np.zeros((self.MM-1,self.MM-1)))
        for m in range(self.MM-1):
            M[:,[m]] = self.ksim[m][:,0] - self.ksim[self.MM-1][:,0]                
        # weights update
        tmp = self.idyRLS.update(idyY, M)
        for m in range(self.MM-1): 
            self.alfa[m,0] = tmp[m]            
        self.alfa[self.MM-1,0] = 1.0 - self.alfa[0:self.MM-1,0].sum()        

    def observe(self, u, y):
        # estimated state
        xe = np.asmatrix(np.zeros((self.N,1)))        
        # calculate for m-observer
        for m in range(self.MM):
            # change 
            self.xemCurr[m][:,0] = self.xemNext[m][:,0]
            self.izmCurr[m][:,0] = self.izmNext[m][:,0]
            # observer estimated output
            self.yem[:,0] = self.C*self.xemCurr[m][:,0]
            # observer estimated output error
            etam = self.yem[:,0] - y
            # integral of error
            self.izmNext[m][:,0]  = self.izmCurr[m][:,0]  + self.Tp*(self.Az*self.izmCurr[m][:,0] + self.Bz*etam[:,0]) 
            self.__singleObserver(m, u, etam)            
            self.__calculateMapping(m, etam)
            # virtual single model
            xe[:,0] = xe[:,0] + np.squeeze(np.asarray(self.alfa[m,0]))*self.xemCurr[m][:,0]
        
        # if self.observerType == 'none':
        # no weights estimation (equal to single mode)        
        if self.observerType == 'RLS':
            # weights estimation based on RLS
            self.__weightsRLS()
        
        # return estimated state
        return xe[:,0]
    
    def restart(self, p0):
        self.__setXemPoints(self.xe0)
        if self.observerType == 'RLS':   
            self.idyRLS.restart(p0)            
    