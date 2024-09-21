# Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
# Exemplo:
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
# Saída: [100-105], [110-111], [113-115], [150]

def preencherlista(lista):
    for i in range(0 , 10):
        N = int(input("Digite um numero: "))
        lista.append(N)
    return lista

def agruparlista(lista, grupos):
    inicio = lista[0]
    fim = lista[0]
    for i in range(1, len(lista)):
        if lista[i] == fim + 1:
            fim = lista[i]
        else:
            if inicio == fim:
                grupos.append([inicio])
            else:
                grupos.append([inicio, fim]) 
            inicio = fim = lista[i]
    if inicio == fim:
        grupos.append([inicio])
    else:
        grupos.append([inicio, fim])
    
    return grupos
    

def main():
    lista = []
    grupos = []
    preencherlista(lista)
    agrupar = agruparlista(lista, grupos)
    print(grupos)


main()