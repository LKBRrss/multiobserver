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

<a href="http://www.codecogs.com/eqnedit.php?latex=A=\begin{bmatrix}&space;0&space;&&space;1&space;&&space;\cdots&space;&&space;\cdots&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;1&space;&&space;\cdots&space;&&space;0\\&space;\vdots&space;&&space;&&space;\ddots&space;&&space;&&space;\vdots&space;\\&space;0&space;&&space;\cdots&space;&&space;\cdots&space;&&space;0&space;&&space;1&space;\\&space;0&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;0&space;\end{bmatrix}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?A=\begin{bmatrix}&space;0&space;&&space;1&space;&&space;\cdots&space;&&space;\cdots&space;&&space;0&space;\\&space;0&space;&&space;0&space;&&space;1&space;&&space;\cdots&space;&&space;0\\&space;\vdots&space;&&space;&&space;\ddots&space;&&space;&&space;\vdots&space;\\&space;0&space;&&space;\cdots&space;&&space;\cdots&space;&&space;0&space;&&space;1&space;\\&space;0&space;&&space;\cdots&space;&&space;\cdots&space;&&space;\cdots&space;&&space;0&space;\end{bmatrix}" title="A=\begin{bmatrix} 0 & 1 & \cdots & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0\\ \vdots & & \ddots & & \vdots \\ 0 & \cdots & \cdots & 0 & 1 \\ 0 & \cdots & \cdots & \cdots & 0 \end{bmatrix}" /></a>

![equiation]()
