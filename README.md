# Multiobserver
A tool for state observation by multi observer method.

Luenberger observer is  a design for nonlinear single-input single-output systems:

![equiation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20x%28t%29%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%20Ax%28t%29&plus;B%5Cphi%20%28x%28t%29%2Cu%28t%29%29)

![equiation](http://latex.codecogs.com/gif.latex?y%28t%29%3DCx%28t%29)

<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;x(t)}{\mathrm{d}&space;t}=&space;Ax(t)&plus;B\phi&space;(x(t),u(t))" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;x(t)}{\mathrm{d}&space;t}=&space;Ax(t)&plus;B\phi&space;(x(t),u(t))" title="\frac{\mathrm{d} x(t)}{\mathrm{d} t}= Ax(t)+B\phi (x(t),u(t))" /></a>

where:
x(t) ϵ Rᴺ in the system state
u(t) ϵ R is the input variable
y(t) ϵ R is the output variable
function Ø(x(t), u(t)) : Rᴺ+1 → R is locally Lipschitz and describes the system nonlinearities.
The matrix A ϵ Rnxn, B ϵ Rnx1 and C ϵ R1xn are defined as
