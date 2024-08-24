#. Escreva uma função que recebe uma matriz e retorne a soma de todos os valores da matriz.
 
matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]

def somamaluca(matriz):
    soma = 0 
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            soma = soma + matriz[linha][coluna]
    return soma

resultado = somamaluca(matriz)
print("A soma dos valores da matriz é:", resultado)