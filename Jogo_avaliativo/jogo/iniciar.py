import gerar_tabuleiro
import contar

tamanho = 7
Qminas = 20


def jogar():
    tabuleiro, minas = gerar_tabuleiro.tabu()
    nome = input("Digite seu nome: ")
    jogadas = 0
    while True:
        for linha in tabuleiro:
            for coluna in linha:
                print(coluna, end=" ")
            print("")

        try:
            x = int(input("Digite um valor de 0 a 6 para linha(X): "))
            y = int(input("Digite um valor de 0 a 6 para coluna(Y): "))
            if x < 0 or x >= tamanho or y < 0 or y >= tamanho:
                print("Valor inválido. Tente novamente.")
                continue
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue

        if (x, y) in minas:
            tabuleiro[x][y] = "💣"
            for linha in range(len(tabuleiro)):
                for coluna in range(len(tabuleiro[linha])):
                    if (linha, coluna) in minas:
                        tabuleiro[linha][coluna] = "💣"
            for linha in tabuleiro:
                for coluna in linha:
                    print(coluna, end=" ")
                print("")
            
            print("Você encontrou uma mina! Fim de jogo.")
            break
        
        num_minas_vizinhas = contar.contar(x, y, minas)
        tabuleiro[x][y] = str(num_minas_vizinhas) if num_minas_vizinhas > 0 else " "
        jogadas += 1
    pontuacoes = open('score.txt', 'a')
    pontuacoes.write(f"O jogador {nome}, tem {jogadas} pontos\n")
    pontuacoes.close()
