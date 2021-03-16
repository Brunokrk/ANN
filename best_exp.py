import math
import random
import matplotlib.pyplot as plt
import numpy as np
from typing import List

def modelo(x):
    return 2 * math.exp(0.3*x) + 4 * random.random()


a, b = 0.0, 10
x = a + (b - a) * np.random.rand(100)
x.sort()

y = [modelo(xi) for xi in x]

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




#t = np.linspace(0, 5, 100)
