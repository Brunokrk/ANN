import math
import random
import numpy as np

def prod(lst):
    p = 1
    for i in lst:
        p*= i
    return p


def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        #para construir a matriz A
        A.append([0] * (n))
        for j in range(n):
            A[i][j] = xs[j] ** i 
        
        #para construir a matriz B
        potencias = [k +1 for k in range(i - ordem,  i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i-ordem)
        B.append(termo)
    A = np.array(A, dtype = 'float')
    B = np.array(B, dtype = 'float')
    cs = np.linalg.solve(A,B)
    soma = 0
    for ck,xk in zip(cs, xs):
        soma += ck * f(xk)
    return soma


if __name__ == '__main__':

    def f(x):
        return (x**2) *math.e**(-x) + 1

    x0 =  3.74306
    ordem = 2

    #pontos para contruir a fórmula
    num_pontos = 4
    a = x0 - 0.25
    b = x0 + 0.25
    xs = [3.10021, 3.41833, 3.63586, 3.9471, 4.38066]

    r = finite_diffs(xs, ordem, x0, f)
    print(xs)
    print(f'aproximação para a derivada de ordem {ordem} de f no ponto {x0}', r)