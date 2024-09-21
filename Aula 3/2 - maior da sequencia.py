from random import randint 
matriz = []
tamanho = 5
def gerarmatrizaleatoria(tamanho):
    lista_temp = []
    for linha in range(tamanho):
        lista_temp = []
        for coluna in range(tamanho):
            valor = randint(0,10)
            lista_temp.append(valor)
    
        matriz.append(lista_temp)   
    return matriz
def mostra_matiz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna],end="\t")
        print("")
        

def somamatriz(nova_matriz):
    maiorsoma = 0
    direcao = ""
    posicao = ()
    for linha in range(len(nova_matriz)):
        for coluna in range(len(nova_matriz[0]) - 4): 
            soma = 0
            for i in range(5):
                soma += nova_matriz[linha][coluna + i]
            if soma > maiorsoma:
                maiorsoma = soma
                direcao = "Linha"
                posicao = (linha, coluna)

    for linha in range(len(nova_matriz) - 4):
        for coluna in range(len(nova_matriz[0])): 
            soma = 0
            for i in range(5): 
                soma += nova_matriz[linha + i][coluna]  
            if soma > maiorsoma:
                maiorsoma = soma
                direcao = "Coluna"
                posicao = (linha, coluna)
    for linha in range(len(nova_matriz) - 4):
        for coluna in range(len(nova_matriz[0]) - 4):
            soma = 0
            for i in range(5):
                soma += nova_matriz[linha + i][coluna + i]  
            if soma > maiorsoma:
                maiorsoma = soma
                direcao = "Diagonal Principal"
                posicao = (linha, coluna)

    print("A maior sequência está na", direcao, "na posição", posicao, "e a soma final foi", maiorsoma)
    return

        
def main():
    
    nova_matriz = gerarmatrizaleatoria(5)
    mostra_matiz(nova_matriz)
    soma = somamatriz(nova_matriz) 
main()
