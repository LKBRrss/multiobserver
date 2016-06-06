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

Definition of function realizing points for observer:

`def __setXemPoints(self, xe0,  n = 0):`

If length of xe0 is equal to zero then initial state xem is filled in values = 1 otherwise (if legnth is not equal zero) this initial state xem is filled in values equals product of number of observers and initial state xe0.

Definition of observer function:

`def observe(self, u, y):`

u: observer input

y: observer output

In above function follows realizing the main algorithm of Luenberger observer. Function computes inputs and outputs states and  returns estimated values of particular parametrs. Initially alfa-values are computed without counting weights, and then by executed RLS method counts weights computed from it. Last step is cyclic weigths updating.

Definition of function realizing restarting:

`def restart(self, p0):`

In case of meet comparison variable responsible for uptdating alfa-parameter weights with text values "RLS" follows restart all RLS method parameters values by variable p0.
