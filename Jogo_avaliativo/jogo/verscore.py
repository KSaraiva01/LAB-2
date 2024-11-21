def score():
    pontuacao = open('score.txt', 'r')
    listar = pontuacao.readlines()
    pontuacao.close()
    print(listar)