import math
import numpy as np
import matplotlib.pyplot as plt


def trapz(f, a, b, n):
    h = (b-a)/n
    soma = 0
    for k in range (1,n):
        soma+= f(a+ k * h)
    return (h/2) * (f(a)+ 2 *soma +f(b))

def best_func(f, a, b, fs, intervalos=100):
    n = len(fs)
    A =  [[0]*n for _ in range(n)]
    B =  []
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            if i >= j: 
               #integral fj * fi  em [a. b]
                def f_ji(x):
                    return fs[j](x) * fs[i](x)

                a_ij =  trapz(f_ji, a, b, intervalos)
                A[i][j] = a_ij
            else:
                A[i][j] = A[j][i]
            
        def ff_i(x):
            return f(x) * fs[i](x)

        b_i = trapz(ff_i, a, b, intervalos)
        B.append(b_i)
    coeffs = np.linalg.solve(A, B)
    return coeffs

def f(x):
    if x<=0:
        return 2
    else:
        return 1


def f1(x):
    return 1

def f2(x):
    return math.sin(x)

def f3(x):
    return math.cos(x)

a,b = [-math.pi, math.pi]

fs = [f1, f2, f3] #lista contendo f1, f2, f3

coeffs = best_func(f, a, b, fs, intervalos = 128)

def g(x):
    soma =0
    for c_k, f_k in zip (coeffs, fs):
        soma += c_k *f_k(x)
    return soma


#plotar graficos
t = np.linspace(a,b,200)
ft = [f(i) for i in t]
gt = [g(i) for i in t]

plt.plot(t,ft,lable="grafico de f")
plt.plot(t,ft,lable="grafico de f")
plt.savefig('best_fun.png')
