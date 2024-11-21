def contar(x, y, minas):
    direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    contador = 0
    for dx, dy in direcoes:
        if (x + dx, y + dy) in minas:
            contador += 1
    return contador
