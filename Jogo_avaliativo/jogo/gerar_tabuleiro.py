import random 
tamanho = 7
Qminas = 20

def tabu():
    tabuleiro = []
    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            linha.append("⬜")
        tabuleiro.append(linha)
    minas = set()
    while len(minas) < Qminas:
        mina = (random.randint(0, tamanho - 1), random.randint(0, tamanho - 1))
        minas.add(mina)

    return tabuleiro, minas