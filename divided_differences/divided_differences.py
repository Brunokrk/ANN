#método das diferenças divididas (de Newton)

x = [1.645, 2.88, 3.603, 5.954]
y = [2.647959002231413,3.597017331779781,3.2346337773880025,4.039633225212058]

def divided_differences(x, y):
    Y = [item for item in y] # vai mudando em cada iteração
    coeffs = [y[0], 0, 0, 0]
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