import math
n8 = [(-0.1834346424956498, 0.362683783378362), (0.1834346424956498, 0.362683783378362), (-0.525532409916329, 0.31370664587788727), (0.525532409916329, 0.31370664587788727), (-0.7966664774136267, 0.22238103445337448), (0.7966664774136267, 0.22238103445337448), (-0.9602898564975363, 0.10122853629037626), (0.9602898564975363, 0.10122853629037626 )]

print ('{x:<20}{c:<20}'.format(x='x_k', c='c_k'))
for x_k, c_k in n8:
    print ('{x:<20}{c:<20}'.format(x=x_k, c=c_k))


def f(x):
    return (x**2) * math.exp(-x) * math.cos(x) + 1 


def quadratura(f, pontos_e_pesos):
    soma = 0
    for x_k, c_k in pontos_e_pesos:
        soma += c_k *f(x_k)
    return soma

def change(f, a, b, u):
    return f((b+a)/2 + (b-a)/2 *u/2) * (b-a)/2

a, b = [0.67045, 4.4175]

def g(u):
    return change (f, a, b, u)

r = quadratura(g, n8)
print(r)