import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math

x0 = -0.87
y0 = -0.13
delta = 0.1
def f1(x):
     return math.sin(x)+2/2
def f2(y):
    return 0.7 - math.cos(y-1)

def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(yn)
    yn1 = f1(xn)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn)>=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print('Simple iteration:')
    print('x=', xn, '\ny=',yn,'\nThe amount of money = ',n)
    iter(x0,x0,0.0001)

    def f3(x):
        return (math.sin(x[0])-x[1]-2)/2, 0.7 + math.cos(x[0])+x[1]+0.5
    s = optimize.root(f3,[0.,0.], method = 'hybr')
    print('Check',s.x)
