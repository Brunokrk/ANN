import math
import matplotlib.pyplot as plt
import numpy as np
import random

def modelo(x):
    return 2*x**2.43 + 1.3* random.random()

x0,x1 = 0, 10
n = 10
x = x0+(x1-x0)* np.random.rand(n)
x.sort()

y = [modelo(xi) for xi in x]

def best_pow(x, y):
    """
    Encontra a melhor função y = a*x**b em que 
    a = exp(a0) e b = a1, onde a0 e a1 são os coeficientes
    da reta que melhor se ajusta a lista de pontos 
    x_ = log(x) e y_=log(y)
    """
    new_y=[math.log(yi)for yi in y]
    new_x = [math.log(yi)for yi in y]

    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)
    A = [[len(x), sum_x], [sum_x, sum_x2]]

    sum_new_y = sum(new_y)
    sum_new_xy = sum(xi * yi for xi,yi in zip(new_x, new_y))
    B = [sum_new_y, sum_new_xy]
    a0,a1 = np.linalg.solve(A,B)
    a, b = math.exp(a0), a1
    
    return a, b

a,b = best_pow(x,y)
print(a,b)

#def bpow(x):
    #return a * x ** b

#t=np.linspace(x0,x1,100)
#bpowt = [bpow(i) for i in t]
#plt.plot(t, bpowt)
#plt.scatter(x, y)
#plt.savefig("best_pow.png")
