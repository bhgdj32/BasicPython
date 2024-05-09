from math import sin
from math import pi
a = 0
b = pi / 2
N = 100
h = (b - a) / N
S1 = 0


for k in range (1 , N+1):
    S1 +=sin(a + (k - 1) * h) + sin(a + k * h)

S2  = S1 * h/2
print(S2)