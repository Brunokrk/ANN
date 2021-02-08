

def lagrange(x, y):
    """eq do polinomio de lagrange"""
    n = len(x)
    if n == len(y):
        eq = ''
        for k in range(n):
            numer = '*'.join([f'(x{-xi:+})' for i, xi in enumerate(x) if i != k])
            denom = '*'.join([f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i != k])
            eq += f'{y[k]:+}*{numer}/{denom}'
            return eq
    else:
        raise TypeError(
            "O número de coordenadas x é diferente do numero de coordenadas y")


def subs():
    """valor do polinomio de lagrange num ponto x"""
    pass

if __name__ == '__main__':
    x = [1, 2, 3]
    y = [2, 5, 1]
    eq = lagrange(x,y)
    print('p(x) = ',eq)


