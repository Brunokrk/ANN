#método das diferenças divididas (de Newton)

x = [-1.05747, -0.48983, 0.07781, 0.64545, 1.21309, 1.78073]
y = [1.8418772707173348,2.155344870516019,2.0059994132595937,2.171739888380491,1.6853182875054062,2.171474638323083]

def divided_differences(x, y):
    Y = [item for item in y] # vai mudando em cada iteração
    coeffs = [y[0], 0, 0, 0, 0, 0]
    n = len(y)
    for i in range(n - 1):
        for j in range(n -1 -i):
            numer = Y[j+1] - Y[j]     
            denom = x[j+1+i] - x[j] 
            Y[j] = numer / denom
        coeffs[i+1] = Y[0]
    return coeffs


def eq(x, coefss):
    n = len(x)
    equation = f'{coeffs[0]:+}'
    for i in range(n ):
        equation += f'{coeffs[i]:+}' + '*'.join([f'(x{-xj:+})' for j,xj in enumerate(x) if j <i])
    return equation


coeffs = divided_differences(x, y)
print (coeffs)
poly = eq(x, coeffs)
print('p(x) =',poly)