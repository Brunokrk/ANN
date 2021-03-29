from math import *

def f(x):
    return exp(-x**2) + cos(x) + 3

x =  [0.193, 0.627, 1.402, 1.918, 2.355, 3.25, 3.635, 4.197, 4.915, 5.723, 6.072, 6.571]

vetY = "["
for i in x:
    vetY = vetY + str(f(i)) +","
vetY = vetY + "]"
print (vetY)