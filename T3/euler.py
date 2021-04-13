import math
def euler(f, x0: float, y0: float, h: float, n: int):
    xs, ys = [], []
    
    for k in range(n):
        x = x0 + k *h
        y = y0 + h*f(x, y0)
        #print(f'x_{k+1} = {x+h}\ny_{k+1} = {y}\n')
        xs.append(x+h)
        ys.append(y)
        y0 = y
    return xs, ys

x0 = 0.96859
y0 = 1.91499
h = 0.18026


def f(x, y):
    return y*math.cos(x) + 1


r = euler(f, x0, y0, h, n=10)
k = 1
for x, y in zip(*r):
    print(f'x_{k} = {x}\ny_{k} = {y}\n')
    k+=1