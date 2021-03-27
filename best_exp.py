import math
import random
import matplotlib.pyplot as plt
import numpy as np
from typing import List

def modelo(x):
    return 2 * math.exp(0.3*x) + 4 * random.random()


a, b = 0.0, 10
#x = a + (b - a) * np.random.rand(100)
#x.sort()
x =  [0.3486, 0.6869, 0.8612, 1.3314, 1.8492, 1.8861, 2.27, 2.7251]
y = [3.1143, 3.9647, 4.5676, 7.9277, 12.2942, 12.6438, 18.0965, 27.4685]

#y = [modelo(xi) for xi in x]

def best_exp(x: List[float], y: List[float]):
    #y = a * exp(b*x)
    #a = exp (a0) e b = a1
    #y_ = a0 + a1x, onde y_ é a reta que melhor se ajusta à lista de pontos x, ln(y)

    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    A = [[len(x), sum_x],[sum_x, sum_x2 ]]
    y_ = [math.log(yi) for yi in y]
    sum_xy = sum(xi * yi for xi, yi in zip(x, y_))
    B = [sum(y_), sum_xy]
    a0, a1 = np.linalg.solve(A, B)
    a, b = math.exp(a0), a1
    return a, b

a, b =best_exp(x, y)

def bexp(x):
    return a * math.exp(b*x)

t=np.linspace(min(x), max(x), 100)
bexpt = [bexp(i) for i in t]
plt.plot(t, bexpt)
plt.scatter(x, y)
plt.savefig('pontos_exp.png')
print(a)
print(b)



#t = np.linspace(0, 5, 100)
