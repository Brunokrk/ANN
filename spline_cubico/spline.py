#algoritmo spline cubico
import matplotlib.pyplot as plt 
import numpy as np

def spline(x, y):
    n = len(x)
    a = {k: v for k,v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in range(n - 1)}
    A = [[1] + [0] *(n - 1)]
    for i in range(1, n-1):
        row = [0] * n
        row[i-1] = h[i-1]
        row[i] = 2*(h[i-1] + h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0] * (n - 1) + [1])
    B = [0]
    for k in range (1, n-1):
        row = 3 * (a[k+1] - a[k]) / h[k] -3 * (a[k] - a[k-1])/ h[k-1]
        B.append(row)
    B.append(0)
    c = dict(zip(range(n), np.linalg.solve(A,B))) 
    b={}
    d={}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])
    s = {}
    for k in range(n-1):
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        #s[k] = {'coefs': [a[k], b[k], c[k], d[k]], 'domain': [x[k], x[k+1]]} 
        s[k] = {'eq': eq, 'domain': [x[k], x[k+1]]} 
    return s

#(1,1), (2,4), (4,2), (5,3)
x = [1.645, 2.88, 3.603, 5.954]
y = [2.9926662214570587,2.034270600027393,2.104575480697977,3.9463060250722504]
eqs = spline(x, y)
print(eqs)

print(1.713+1.525633721382972*(-6.677+6.997)+0.0*(-6.677+6.997)**2-0.07862155659424055*(-6.677+6.997)**3)
print(3.364-0.6704886636212832*(-2.819+2.747)+0.4150864559117228*(-2.819+2.747)**2-0.03350953694990103*(-2.819+2.747)**3)
print(2.709-0.8801930379007001*(4.101-4.001)+0.6349125927146375*(4.101-4.001)**2-0.10153450580009153*(4.101-4.001)**3)
print(2.709-0.8801930379007001*(7.116-4.001)+0.6349125927146375*(7.116-4.001)**2-0.10153450580009153*(7.116-4.001)**3)
print(0.005-1.4263103067247018*(11.378-10.079)+0.2982295130568242*(11.378-10.079)**2+0.046463101023488884*(11.378-10.079)**3)

#for key, value in eqs.items():
#    def p(x):
#        return eval(value['eq'])
#    t= np.linespace(*value['domain'], 100)
#    plt.plot(t, p(t), label=f"$S_{key}(x)$")
#plt.scatter(x, y)
#plt.savefig('spline.png')
