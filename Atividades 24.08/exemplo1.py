from random import randint 

matriz = []
tamanho = 5 

def gerarmatrizaleatoria(tamanho):
    lista_temp = []
    for linha in range(tamanho):
        lista_temp = []

        for coluna in range(tamanho):
            valor = randint(0,100)
            lista_temp.append(valor)
    
        matriz.append(lista_temp)   
    return matriz

#mostrar
def mostra_matiz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna],end="\t")
        print("")


nova_matriz = gerarmatrizaleatoria(5)
mostra_matiz(nova_matriz)







