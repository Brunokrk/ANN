from math import *

def f(x):
    return 4 + sin(x) - ((x**2) / 30)


x =  [0.488, 2.587, 5.163]

vetY = "["
for i in x:
    vetY = vetY + str(f(i)) +","
vetY = vetY + "]"
print (vetY)