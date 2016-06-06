Difine observer class realizing assignment variables particular parameters:
`def restart(self, p0):`

Definition of initial variables:
`def __init__(self, N, M, Np, Tp, A, B, C, L, mapping, obstype, RLSGain = 1000.0, RLSForgetting = 1.0, xe0 = []):`

self: class pointer 
N: number of estimated states
M: number of estimated outputs
Np: number of samples
Tp: sampling time
A: matrix of states in system
B: matrix of inputs in system
C: matrix of outputs in system
L: matrix of observer gains in system
mapping: mapping
obstype: variable responsible for updating alfa-parametrer weigths
RLSGain: gain value of RLS function
RLSForgetting: value of forgetting rate of RLS function
xe0: initial value for ovserver points

