def depositar(saldo):
    try:
        while True:
            print("Você escolheu a opção de Deposito!")
            print("Seu saldo atua e de R$", saldo)
            s = float(input("Quanto deseja Depositar? "))
            if s < 0:
                print("Valor de Deposito Não pode ser negativo!!")
            else:
                float(saldo)
                resultado = saldo + s
                saldo = resultado
                print("Você Depositou R$",s )
                registros = open('Registro_de_extrato.txt', 'a')
                registros.write(f"Você Depositou, R${s} Seu saldo atual e de R${saldo}\n")
                registros.close()
                break
        return saldo
    except TypeError:
        print("Valor invalido!!")
    except ValueError:
        print("Valor invalido!!")