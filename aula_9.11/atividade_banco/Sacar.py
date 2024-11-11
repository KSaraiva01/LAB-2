
def sacar(saldo):
    try:
        while True:
            print("Você escolheu a opção de saque!")
            print("Seu saldo atua e de R$", saldo)
            s = float(input("Quanto deseja sacar?"))

            if s > saldo:
                print("Valor invalido!!")
            elif s < 0:
                print("Saldo invalido!!")
            
            else:
                resultado = saldo - s
                saldo = resultado
                print("Você sacou R$",s )
                registros = open('Registro_de_extrato.txt', 'a')
                registros.write(f"Você sacou, R${s} Seu saldo atual e de R${saldo}\n")
                registros.close()
                break
        return saldo
    except TypeError:
        print("Valor invalido!")
    except ValueError:
        print("Valor invalido!!")