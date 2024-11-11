def tomate(saldo):
    registros = open('Registro_de_extrato.txt', 'r')
    linhas = registros.readlines()
    for i, linha in enumerate(linhas):
        isso = linha
        print(isso)
    registros.close
    

