#  Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo.
#  Sabendo que cada cartela devera conter 5 linhas de 5 números, gere estes dados de modo a não ter números repetidos dentro das cartelas.
#  O programa deve exibir na tela a cartela gerada.

from random import randint 
matriz = []
tamanho = 5
def gerarmatrizaleatoria(tamanho):
    matriz = []
    usados = []
    for linha in range(tamanho):
        lista_temp = []
        for i in range(tamanho):
            while True:
                valor = randint(0, 99)
                if valor not in usados:
                    lista_temp.append(valor)
                    usados.append(valor) 
                    break
        matriz.append(lista_temp)
    return matriz
def mostra_matiz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna],end="\t")
        print("")

def main():    
    nova_matriz = gerarmatrizaleatoria(5)
    print("-------------Bingoooo-------------")
    mostra_matiz(nova_matriz)

main ()