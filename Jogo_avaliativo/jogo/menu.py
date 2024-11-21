class negativo(Exception):
    pass

def menu():
    try:
        while True:
            print("1 - Iniciar novo jogo\n2 - Ver score\n3 - Minhas pontuações\n4 - Sair do jogo")
            opc = int(input("Digite uma opcção: "))
            if opc < 0:
                raise negativo 
            return opc
    except ValueError:
        print("Valor invalido!!")
    except negativo:
        print("Valor não pode ser negativo!!")