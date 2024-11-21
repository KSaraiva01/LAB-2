def score():
    nome = input("Digite o nome que quer verificar: ")
    pontuacao = open('score.txt', 'r')
    for linha in pontuacao:
        if nome in linha:
            print(linha)
    pontuacao.close()