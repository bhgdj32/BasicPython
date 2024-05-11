from math import sin
from math import pi
def f1(x):
    return sin(x)
def f2(x):
    return 4/(1+x**2)
def f3(x):
    return pi**(1/2)*exp(-x**2)
def f(d, a=0,b=1,n=100):
    h =(b-a)/n
    S1 = 0
    for k in range (1 , n+1):
        S1 +=d(a + (k - 1) * h) + d(a + k * h)
        S2 = S1 * h/2
        return S2
print(f(f1,0,pi/2,50))
print(f(f2,0,1,100))
print(f(f3,-100,100,1000))