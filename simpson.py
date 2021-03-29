import math


def simps(f, a, b, n):
    if( n % 2) != 0 or n < 1:
        raise ValueError("n deve ser par e maior que 1")
    h = (b-a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1, n, 2):
        soma_odd += f(a+k *h)
    for k in range(2, n, 2):
        soma_even +=f(a+k*h)
    return (h / 3) * (f(a) + 4 * soma_odd + 2 *soma_even +f(b))


a, b = 0,1
n = 8
h = (b-a)/n
particao = [a + k * h for k in range (n+1)]
particao_odd = [a + k * h for k in range (1, n, 2)]
particao_even = [a + k * h for k in range (2, n, 2)]

print(particao)
print(particao_odd)
print(particao_even)

def f(x):
    return math.exp(-x**2)

a,b = -0.522, 1.121
n=1_096# n é o número de subintervalos
i1 = simps(f, a, b, n)
print(i1)


def g(x):
    return math.cos(x**2)

a,b = -0.522, 1.121
n = 8
#i2 = simps(g, a, b, n)