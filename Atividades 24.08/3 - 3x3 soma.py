#A partir de uma matriz 3 x 3 numérica, percorra a matriz e some os maiores valores de cada linha.

def somar(matriz):
    soma = 0 
    for linha in range(len(matriz)):
        maiordalinha = 0
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] >= maiordalinha:
                maiordalinha = matriz[linha][coluna]
        soma = maiordalinha + soma
    return soma


def mostra_matiz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna],end="\t")
        print("")

def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    resultado = somar(matriz)
    mostra_matiz(matriz)
    print("A soma dos indices de maiores valores:", resultado)
main()
