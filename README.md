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

![equiation]()
![equiation]()
![equiation]()
![equiation]()
![equiation]()
