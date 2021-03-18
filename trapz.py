import math


def f(x):
    return -3.00641* x +13.31250


def trapz(f, a, b, n):
    h = (b - a)/n
    soma = 0
    for k in range(1, n):
        soma += (f(a + k * h))
    soma *= 2
    soma += (f(a) + f(b))
    return (h / 2) * soma


a, b = 3.511, 3.823
n = 1_000_000 # numero de pontos na partição

r = trapz(f, a, b, n)
print(r)
