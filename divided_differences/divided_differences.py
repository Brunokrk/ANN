#método das diferenças divididas (de Newton)

#(1,2), (2,5), (3,1), (4,3)
x = [2.014, 4.232, 6.052]
y = [4.768, 2.516, 2.55]

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