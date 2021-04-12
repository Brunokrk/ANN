import math


def rk4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0+(h/2)*m1)
        m3 = f(x0 + h / 2, y0+(h/2)*m2)
        m4 = f(x0 + h, y0 + h*m3)
        yk = y0 + h * (m1 + 2*m2 + 2 * m3 + m4) / 6
        #atualizar x0 e y0
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r

if __name__ == '__main__':

    def f(x, y):
        return y + math.exp(-x**2) + 1

    x0 = 0.59247
    y0 = 1.99599

    r = rk4(f, x0, y0, h=0.1545, n=10)
    print(r)
