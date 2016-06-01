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

    ![equiation](http://latex.codecogs.com/gif.latex?%5Chat%7Bx%7D%28k&plus;1%29%3DA%5Chat%7Bx%7D%28k%29&plus;Bu%28k%29&plus;%5Cunderbrace%7BL%28y%28k%29-C%5Chat%7Bx%7D%28k%29%29%7D)

              gsgjkhj

![equiation](http://latex.codecogs.com/gif.latex?%5Ctilde%7Bx%7D%28k%29%3Dx%28k%29-%5Chat%7Bx%7D%28t%29)

![equiation](http://latex.codecogs.com/gif.latex?%5Ctilde%7Bx%7D%28k&plus;1%29%3DAx%28k%29&plus;Bu%28k%29-A%5Chat%7Bx%7D%28k%29-Bu%28k%29-L%5Cleft%20%5B%20y%28k%29-C%5Chat%7Bx%7D%28k%29%20%5Cright%20%5D%3D%28A-LC%29%5Ctilde%7Bx%7D%28k%29)

![equiation]()
![equiation]()
