import math

def heun (f, x0, y0, h, n):
    r= []
    for _ in range(10):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h *m1)
        y1 = y0 + h * (m1+m2) / 2

        x0 += h
        y0 += y1
        r.append((x0,y0))
    return r


if __name__ == '__main__':

    def f(x, y):
        return y*(1-x) + x +2
    
    x0 = 0.79936
    y0 = 2.84756

    r = heun(f, x0, y0, h=0.17741, n=10)
    print(r)