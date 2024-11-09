# 4. Utilizando dicionários, crie um programa que simule um caixa eletrônico. O usuário poderá optar pelas
# seguintes funcionalidades:

# Depositar dinheiro – Usuário pode depositar valor ilimitado, desde que seja positivo;
# Sacar dinheiro – Usuário pode sacar um valor limitado que deve ser validado pelo campo
# “transaction_limit”;
# Verificar saldo bancário – Usuário pode consultar o saldo atual;
# Histórico de movimentações – Usuário pode consultar todas as movimentações efetuadas;
# Sair – Usuário pode sair do sistema.
class invalidOptionError(BaseException):
    pass
class valornegatico(BaseException):
    pass
class limitetrans(BaseException):
    pass
class maiorquebanco(BaseException):
    pass

def menu():
    while True:
        try:
            print("-----O MENU-----\n1. Depositar\n2. Sacar\n3. Extrato\n4. Historico de movimento\n5. sair")
            opcao = int(input("Digite uma opção :"))
            if opcao < 1 or opcao > 5:
                raise invalidOptionError
            return opcao
        except ValueError:
            print("Erro : Valor invalido!")
        except invalidOptionError:
            print("Error : Valor digitado não e opção valida!!")

def depositar(banco):
    try:
        print(" -- DEPOSITAR --")
        valor = float(input("Digite o valor que quer depositar: "))
        if valor <= 0:
            raise valornegatico
        banco["balance"] += valor
        banco["historic"].append(print("Depositro de R$:", valor))
        print("Deposito efetuado com susesso!!!")
        return banco
    except ValueError:
        print("Error : Valor invalido!!")
    except valornegatico:
        print("Valor não pode ser negativo!!!")
        

def sacar(banco):
    try:
        print(" -- SACAR --")
        valor = float(input("Quanto deseja sacar ? :"))
        if valor <= 0:
            raise valornegatico
        if valor >= banco["transaction_limit"]:
            raise limitetrans
        if valor > banco["balance"]:
            raise maiorquebanco
        banco["balance"] -= valor
        banco["historic"].append(print("Saque de R$:", valor))
        print("Funcionou :)")
        return banco

    except ValueError:
        print("Valor invalido !!")
    except valornegatico:
        print("Valor invalido!!!")
    except limitetrans:
        print("Valor invalido!!!")
    except maiorquebanco:
        print("Valor invalido")

def main():
    banco = {
    "balance" : 0,
    "transaction_limit" : 1000,
    "historic" : []
    } 
    print(banco)
    while  True:
        opcao = menu()
        if opcao == 1:
            banco = depositar(banco)
        elif opcao ==2:
            banco = sacar(banco)
        elif opcao ==3:
            pass
        elif opcao == 4:
            pass 
        elif opcao == 5:
            print("A DEUS")
            break





main()