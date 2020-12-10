from pprint import pprint
a = [[7.24229, -1.6835, -1.88212, 1.83101], [-2.58775, 7.5959, -1.36297, -1.79952], [-1.54237, -1.43558, -4.8774, -0.05379], [-1.39104, 2.77018, -2.46263, 8.46952]]

b =[-1.55614, -2.21242, 2.45819, 2.82215],


def matriz_extendida(matriz_a: list, matriz_b: list):
    matriz_aux = matriz_a.copy()
    for i in range(len(matriz_a)):
        matriz_aux[i].append(matriz_b[i])
    return matriz_aux


def trocar_linha(matriz, linha_a, linha_b):
    matriz_aux = matriz.copy()
    matriz_aux[linha_a], matriz_aux[linha_b] = matriz[linha_b], matriz[linha_a]
    return matriz_aux


def multiplicar_por_escalar(matriz, escalar, linha):
    matriz_aux = matriz.copy()
    for index, item in enumerate(matriz[linha]):
        matriz_aux[linha][index] = item*escalar
    return matriz_aux


def trocar_linha_combinacao(matriz, linha_a, linha_b, escalar):
    matriz_aux = matriz.copy()
    # print(f"L1: {linha_a + 1} L2: {linha_b + 1} E: {escalar}")
    for index in range(len(matriz[linha_a])):
        matriz_aux[linha_b][index] = escalar * matriz[linha_a][index] + matriz[linha_b][index]
    return matriz_aux


def escalonar(matriz_est):
    matriz_aux = matriz_est.copy()
    for i in range(len(matriz_aux)):
        for j in range(i+1, len(matriz_aux)):
            matriz_aux = trocar_linha_combinacao(
                matriz_aux, i, j, -matriz_aux[j][i] / matriz_aux[i][i])
    return matriz_aux


def print_matriz(matriz):
    print('[')
    for index_linha, linha in enumerate(matriz):
        print('\t[', end="")
        for index, item in enumerate(linha):
            print(f"{item:.4f}", end=(", " if index+1 != len(linha) else ""))
        print('],' if index_linha+1 != len(matriz) else "]")
    print(']')


if __name__ == "__main__":
    print_matriz(escalonar(matriz_extendida(a, b)))
