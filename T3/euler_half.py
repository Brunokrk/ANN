import math

def euler_half(f, x0, y0, h, n):
    r = []
    for i in range(n):
        #realizar iterações do método
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        yk = y0 + h * m2
        #atualizando para a proxima iteração
        y0 = yk
        x0 += h
        #colocando valores numa lista
        r.append((x0, y0))
    
    return r


if __name__ == "__main__":
    def f(x,y):
        return y*(1-x) + x + 2
    
    
    x0 = 0.28654
    y0 = 1.90557

    r = euler_half(f, x0, y0, h=0.1264 , n=10)

    print(r)

