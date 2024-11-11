def menu():
    try: 
        print("===banco Confiavel===")
        print("1 - Sacar\n2 - Depositar\n3 - Consultar\n4 - Ver Extrato\n5 - Sair")
        opc = int(input("Digite uma opção : "))
        if opc < 1 or opc > 5:
            print("Valor invalido!!")
        return opc
    except ValueError:
        print("Valor invalido!! ")