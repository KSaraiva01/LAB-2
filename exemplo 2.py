def verificar (matriz, numeroa):
    sim = False
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == numeroa:
                sim = True
    if sim == True:
        print("Esta presente") 
    else:
        print("não esta presente")     

matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]


def main():
    numeroa = int(input("Digite um numeoro : "))
    verificar(matriz, numeroa)

main()