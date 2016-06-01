# Multiobserver
A tool for state observation by multi observer method.

Luenberger observer is  a design for nonlinear single-input single-output systems:

![equiation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20x%28t%29%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%20Ax%28t%29&plus;B%5Cphi%20%28x%28t%29%2Cu%28t%29%29)

![equiation](http://latex.codecogs.com/gif.latex?y%28t%29%3DCx%28t%29)


where:

![equiation](http://latex.codecogs.com/gif.latex?x%28t%29%5Cin%20R%5E%7BN%7D) in the system state

![equiation](http://latex.codecogs.com/gif.latex?u%28t%29%5Cin%20R) is the input variable

![equiation](http://latex.codecogs.com/gif.latex?y%28t%29%5Cin%20R) is the output variable

function ![equiation](http://latex.codecogs.com/gif.latex?%5Cphi%20%28x%28t%29%2Cu%28t%29%29)  : ![equiation](http://latex.codecogs.com/gif.latex?R%5E%7BN&plus;1%7D%5Crightarrow%20R) is locally Lipschitz and describes the system nonlinearities.
The matrix ![equiation](http://latex.codecogs.com/gif.latex?A%5Cin%20R%5E%7Bnxn%7D), ![equiation](http://latex.codecogs.com/gif.latex?B%5Cin%20R%5E%7Bnx1%7D) and ![equiation](http://latex.codecogs.com/gif.latex?C%5Cin%20R%5E%7B1xn%7D) are defined as:

![equiation](http://latex.codecogs.com/gif.latex?A%3D%5Cbegin%7Bbmatrix%7D%200%20%26%201%20%26%20%5Ccdots%20%26%20%5Ccdots%20%26%200%20%5C%5C%200%20%26%200%20%26%201%20%26%20%5Ccdots%20%26%200%5C%5C%20%5Cvdots%20%26%20%26%20%5Cddots%20%26%20%26%20%5Cvdots%20%5C%5C%200%20%26%20%5Ccdots%20%26%20%5Ccdots%20%26%200%20%26%201%20%5C%5C%200%20%26%20%5Ccdots%20%26%20%5Ccdots%20%26%20%5Ccdots%20%26%200%20%5Cend%7Bbmatrix%7D)

![equiation](http://latex.codecogs.com/gif.latex?B%3D%5Cbegin%7Bbmatrix%7D%200%5C%5C%200%5C%5C%20%5Cvdots%20%5C%5C%200%5C%5C%201%20%5Cend%7Bbmatrix%7D)

![equiation](http://latex.codecogs.com/gif.latex?C%3D%5Cbegin%7Bbmatrix%7D%201%20%26%200%20%26%200%20%26%200%20%26%200%20%5Cend%7Bbmatrix%7D)

Aim of Luenberger observer is to correct the states estimation equation with a feedback from the estimation error  y(k) -  based on measurements in and out signals of dynamical process in order to give estimates of internal states of system.

druga strona:
1:
<a href="http://www.codecogs.com/eqnedit.php?latex=\hat{x}(k&plus;1)=A\hat{x}(k)&plus;Bu(k)&plus;\underbrace{L(y(k)-C\hat{x}(k))}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\hat{x}(k&plus;1)=A\hat{x}(k)&plus;Bu(k)&plus;\underbrace{L(y(k)-C\hat{x}(k))}" title="\hat{x}(k+1)=A\hat{x}(k)+Bu(k)+\underbrace{L(y(k)-C\hat{x}(k))}" /></a>
2:
<a href="http://www.codecogs.com/eqnedit.php?latex=\tilde{x}(k)=x(k)-\hat{x}(k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\tilde{x}(k)=x(k)-\hat{x}(k)" title="\tilde{x}(k)=x(k)-\hat{x}(k)" /></a>
3:
<a href="http://www.codecogs.com/eqnedit.php?latex=\tilde{x}(k&plus;1)=Ax(k)&plus;Bu(k)-A\hat{x}(k)-Bu(k)-L\left&space;[&space;y(k)-C\hat{x}(k)&space;\right&space;]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\tilde{x}(k&plus;1)=Ax(k)&plus;Bu(k)-A\hat{x}(k)-Bu(k)-L\left&space;[&space;y(k)-C\hat{x}(k)&space;\right&space;]" title="\tilde{x}(k+1)=Ax(k)+Bu(k)-A\hat{x}(k)-Bu(k)-L\left [ y(k)-C\hat{x}(k) \right ]" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex==(A-LC)\tilde{x}(k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?=(A-LC)\tilde{x}(k)" title="=(A-LC)\tilde{x}(k)" /></a>
4:
<a href="http://www.codecogs.com/eqnedit.php?latex=\tilde{x}(k)=(A-LC)^{k}(x(0)-\hat{x}(0))" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\tilde{x}(k)=(A-LC)^{k}(x(0)-\hat{x}(0))" title="\tilde{x}(k)=(A-LC)^{k}(x(0)-\hat{x}(0))" /></a>
5:
<a href="http://www.codecogs.com/eqnedit.php?latex=\dot{x}(t)=Ax(t)&plus;Bu(t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\dot{x}(t)=Ax(t)&plus;Bu(t)" title="\dot{x}(t)=Ax(t)+Bu(t)" /></a>
6:
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}\hat{x}(t)}{\mathrm{d}t}=A\hat{x}(t)&plus;Bu(t)&plus;L\left&space;[&space;y(t)-C\hat{x}(t)&space;\right&space;]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\hat{x}(t)}{\mathrm{d}t}=A\hat{x}(t)&plus;Bu(t)&plus;L\left&space;[&space;y(t)-C\hat{x}(t)&space;\right&space;]" title="\frac{\mathrm{d}\hat{x}(t)}{\mathrm{d}t}=A\hat{x}(t)+Bu(t)+L\left [ y(t)-C\hat{x}(t) \right ]" /></a>
7:
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}\tilde{x}(t)}{\mathrm{d}t}=(A-LC)\tilde{x}(t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}\tilde{x}(t)}{\mathrm{d}t}=(A-LC)\tilde{x}(t)" title="\frac{\mathrm{d}\tilde{x}(t)}{\mathrm{d}t}=(A-LC)\tilde{x}(t)" /></a>


![equiation]()
![equiation]()
![equiation]()
![equiation]()
![equiation]()
