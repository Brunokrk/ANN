import math
def ralston(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0) 
        m2 = f(x0 + (3/4)*h, y0+(3/4)*h*m1)
        yk = y0 + h *(m1 +2*m2)/3
        #atualizar os valores
        x0 += h
        y0 = yk

        r.append((x0,y0))
    return r


if __name__ == '__main__':

    def f(x, y):
        return y*math.cos(x)+1
    
    x0 = 0.40462
    y0 = 1.97076

    r = ralston(f, x0, y0, h=0.15218, n=10)
    print(r)