matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]

def mostra_matriz(invertida):
    for linha in range(len(invertida)):
        for coluna in range(len(invertida[linha])):
            print(invertida[linha][coluna],end="\t")
        print("")

def inverter_matriz():
    linhas = len(matriz)
    colunas = len(matriz[0])
    matriz_invertida = [[0 for i in range(linhas)] for x in range(colunas)]

    for linha in range(linhas):
        for coluna in range(colunas):
            matriz_invertida[coluna][linha] = matriz[linha][coluna]
    
    return matriz_invertida

def main():
    invertida = inverter_matriz()
    mostra_matriz(invertida)

main()