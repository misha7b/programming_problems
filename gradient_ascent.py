
from sympy import *
from sympy.plotting import plot

x = Symbol('x')
f = exp(-(x-5)**2) + 0.1*sin(x-2)

c = 1

theta = -3

epsilon = 0.001

step = 6

max_iter = 1000

while abs(diff(f,x).subs(x,theta).evalf()) > epsilon and max_iter > 0:

    gradient = diff(f,x).subs(x,theta).evalf()

    theta_new = theta + step*gradient

    if f.subs(x,theta_new).evalf() < f.subs(x,theta).evalf() + c*step*gradient:
        step = step/2

    theta = theta_new

    max_iter -= 1

print(theta)

#plot graph of f

plot(f,(x,-4,6))

