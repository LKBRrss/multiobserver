'''
Created on Apr 5, 2016

@author: Jakub Bernat
'''
import numpy as np
import logging
import sys

def configureLogger():
    FORMAT = '%(asctime)-15s %(lineno)d %(name)s %(message)s'
    logging.basicConfig(format=FORMAT,level=logging.DEBUG,stream=sys.stdout)
    
def to_plot_array(v, con):
    'vector as matrix'
    arr = np.squeeze(np.asarray(v))
    if con > 0:
        for k in range(0, arr.size):
            if arr[k] > con:
                arr[k] = con
            if arr[k] < -con:
                arr[k] = -con
    return arr            

def delay(signalIn, memory, delay):        
    signalOut = memory[:,0]
    lastIndex = delay-1
    for n in range(0, lastIndex):
        memory[:,n] = memory[:,n+1]
    memory[:,lastIndex] = signalIn        
    return signalOut
