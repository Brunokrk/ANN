import math


def f(x):
    #A-B -> 0.924467937749
    #return 1.846080719038 * x + 1.735122531328
    #B-C -> 2.478625329599
    #return -0.885273266837 * x + 3.582282604896
    #C-D -> 0.563396888050
    #return -0.432488910070 * x + 2.836655437548    
    #D-E -> 0.002407656000
    #return -0.166666666666 * x + 2.326401666666
    #E-F -> 0.805631084099
    #return 0.2336593815273 * x + 1.557483416119
    #F-G -> 1.039143834799
    #return 0.9728527147285 * x + 0.152499913508
    #G-H -> 4.71682531079874
    #return 0.0031993411257 * x + 2.478509067756
    #H-I -> 0.9562062142508106
    return  -0.144249361899 * x + 3.157877492458

def trapz(f, a, b, n):
    h = (b - a)/n
    soma = 0
    for k in range(1, n):
        soma += (f(a + k * h))
    soma *= 2
    soma += (f(a) + f(b))
    return (h / 2) * soma

vetor = [0.924467937749, 2.478625329599, 0.563396888050, 0.002407656000, 0.805631084099, 1.039143834799, 4.71682531079874, 0.9562062142508106]

area = 0
for item in vetor:
    area = area + item


a, b =4.60749, 4.99536
n = 1_000_000 # numero de pontos na partição

r = trapz(f, a, b, n)
print(r)
print(area)