matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]

def verificarmenor (matriz,):
    menor = matriz[1][1]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if menor > matriz[linha][coluna]:
                menor = matriz[linha][coluna]
    return menor

resultado = verificarmenor(matriz)
print("O menor valor é:", resultado)