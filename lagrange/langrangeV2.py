def lagrange (x, y):
    #eq do polinomio de lagrange
    n=len(x)
    if n == len(y):
        eq = ''
        for k in range(n):
            numer = '*'.join([f'(x{-xi:+})' for i, xi in enumerate(x) if i!=k])
            denom = '*'.join([f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i!=k])
            eq += f'{y[k]:+}*({numer})/({denom})'
        return eq
    else:
        raise TypeError('O numero de coordenadas X é diferente do número de coordenadas Y')




if __name__ == '__main__':
    x = [1, 2, 3, 3.2, 4.1, 5.7]
    y = [2, 5, 1, 2, 1, 10]

    eq = lagrange(x, y)
    
    def subs(x):
        return eval(eq)

    print('p(x) =', eq)
    #print(subs(0.025), subs(4.648), subs(5.13))

    #def f(x):
        #return 1/(1+25*x**2)
    
    #num = 5
    #x2 = [-1 + (2/(num -1)) * i for i  in range(num)]
    #y2 = [f(i) for i in x2]
    #eq2 = lagrange(x2, y2)
    #print(x2)
    #print(y2)

    from matplotlib import pyplot as plt
    import numpy as np

    t = np.linspace(1, 5.7, 100)
    plt.plot(t, subs(t))
    plt.scatter(x,y)
    plt.savefig('lagrange.png')