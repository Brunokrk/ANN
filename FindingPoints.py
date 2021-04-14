from math import *

def f(x):
    return cos(x**2) + x**2 + exp(-x**4)


x =  [-1.05747, -0.48983, 0.07781, 0.64545, 1.21309, 1.78073]

vetY = "["
for i in x:
    vetY = vetY + str(f(i)) +","
vetY = vetY + "]"
print (vetY)